# Optimized Financial Planning: Integrating Individual and Cooperative Budgeting Models with LLM Recommendations

## Metadata

```yaml
---
paper_id: "10.3390/ai5010006"
designation: algorithm-specific
title: "Optimized Financial Planning: Integrating Individual and Cooperative Budgeting Models with LLM Recommendations"
authors: "de Zarzà, I.; de Curtò, J.; Roig, G.; Calafate, C. T."
year: 2024
venue: "AI (MDPI)"
odin_topics: ["C.1", "C.2"]
shorthand_tags: ["/budget-rec-formulation", "/budget-alloc-algos", "/budget-algo-tradeoffs", "/budget-algo-justification"]
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

LLM-generated budget advice, when used as bounds in linear optimization, produces personalized allocations that align with standard financial planning principles and improve savings over unguided spending.

## Problem and Motivation

Traditional financial planning methods lack personalization and cannot adapt to dynamic individual needs. The growing complexity of economic systems overwhelms non-experts, leading to poor financial decisions and increased inequality. No prior work had integrated real-time, AI-driven personalized recommendations into optimization models for both individual and household budgeting.

## Approach

- Synthetic dataset: 10 households with incomes normally distributed (mean $5000, σ=$1000) and expenses in four categories (rent, groceries, utilities, entertainment).
- Individual model: Linear optimization maximizing savings S = I − ΣE_z subject to non-negativity, total expenses ≤ income, and minimum spending bounds.
- LLM integration: GPT-4 provides percentage-based allocation recommendations (e.g., rent 24% of income, emergency fund 20%), used as upper bounds (E_z ≤ E_rec^z) in the optimization.
- Cooperative household model: Extends to multiple members with combined income, shared expenses (e.g., rent), and preference weights per member and category.
- Validation framework: Proposed multi-tier verification including expert review, contextual analysis, risk assessment, and RAG to ground LLM outputs in empirical data.
- Comparison: Original savings vs. LLM-recommended savings (parsed from textual advice) vs. optimized savings with bounds.

## Findings

- LLM recommendations consistently followed standard financial guidelines (e.g., 20% to emergency fund, 15–20% to retirement, 25–30% to housing).
- **Optimization with LLM bounds produced higher savings than either unguided spending or LLM advice alone** (see Figure 2).
- Cooperative recommendations included shared emergency funds, child funds, and retirement planning, demonstrating long-term life-cycle awareness.
- LLM could incorporate future life events (e.g., pay cut, retirement in 20 years) into its allocations, enabling consumption smoothing.
- The model lacks real-world validation; all results are from synthetic data without statistical significance testing.

## Key Figures and Tables

- Figure 1: Flowchart of LLM-integrated financial planning → iterative cycle from data to recommendation to adjustment.
- Figure 2: Comparative savings across three scenarios → Optimized savings with bounds exceed both original and LLM-only savings by a wide margin.
- Figure 3: Sequence diagram of LLM recommender system → shows caching, LLM analysis, optimization, and database interactions.
- Table 1: Traditional vs. proposed LLM-integrated models → proposed models score high on personalization, adaptability, scalability, and long-term planning.

## Key Equations

$$S = I - \sum_{z} E_z$$
*Savings equals income minus total expenses.*

$$\text{Maximize } TS = \sum_{o} (I_o - \sum_{z} w_{zo} E_{zo})$$
*Household savings maximized with member-specific preference weights per category.*

$$E_z^{\min} \leq E_z \leq E_z^{\text{rec}}$$
*Expenses bounded by minimum necessities and LLM-recommended upper limits.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| LLM | Large Language Model (e.g., GPT-4) that generates financial advice from natural language inputs. |
| EC | Extended Coevolutionary theory — models how agents (household members) co-adapt strategies over time. |
| RAG | Retrieval Augmented Generation — grounds LLM outputs in retrieved data to reduce hallucinations. |
| Consumption smoothing | Maintaining a stable standard of living over time by balancing spending across high-and low-income periods. |
| Cooperative budgeting | Household members pool incomes and share expenses to maximize collective savings and meet shared goals. |

## Critical Citations

- [Markowitz, 1952] — Portfolio optimization theory adapted to household budgeting as a mix of expenses and savings.
- [Ando & Modigliani, 1963] — Life-cycle hypothesis justifying long-term savings maximization over immediate consumption.
- [Thaler, 1980] — Behavioral economics foundation for incorporating subjective category weights into optimization.

## Relevance to Odin

**Topics:**

C.1 — Budgeting Strategies and Budget Recommendation

C.2 — Budget Recommendation Algorithm

**Contribution to Odin:**

This paper directly informs Odin’s budget recommendation module by presenting a linear optimization framework that maximizes savings under income and expense constraints. The use of user-defined preference weights (w_zo) provides a template for personalizing category-level budget allocations, which maps to Odin’s requirement for behavior-driven recommendations. Although Odin does not use LLMs, the optimization model itself — and the concept of using AI-generated bounds to guide allocation — offers a citable justification for constraint-based approaches over static budgeting. The cooperative household extension, while not directly applicable to Odin’s single-user scope, demonstrates how preference weights can reconcile multiple objectives, relevant to any multi-criteria budget recommendation.

**Directly justifies:**

- "Linear optimization with non‑negativity and total‑expense constraints can maximize monthly savings given income and spending category bounds."
- "User‑defined preference weights per expense category allow a budget recommendation algorithm to respect individual financial priorities."
- "LLM‑generated allocation percentages serve as feasible initial solutions for optimization problems in personal finance, reducing the cold‑start burden on new users."
- "Cooperative budgeting models can achieve higher total household savings by pooling incomes and sharing fixed expenses like rent."

**Limits of relevance:**

- Odin does not integrate LLMs; the paper’s core innovation (LLM recommendations as bounds) is not directly implementable without an LLM API.
- All evaluations use synthetic data with US dollar incomes; no validation on Filipino young professionals or Philippine expense categories.
- The cooperative model assumes multiple users sharing finances; Odin is single-user only.
- No comparison to other budget recommendation algorithms (e.g., rule‑based, reinforcement learning) is provided.

## Limitations

- No real‑world user study or empirical validation — all results from synthetic data and simulated LLM prompts. [unacknowledged]
- The LLM’s recommendations are not benchmarked against non‑LLM baselines (e.g., rule‑based expert systems) beyond the trivial “original” savings.
- Verification mechanisms (expert review, RAG) are proposed but not implemented or tested.
- The optimization model assumes fixed monthly income and does not handle variable income or irregular cash flows common among Filipino young professionals. [unacknowledged]
- Long‑term planning examples rely on user‑provided future events (e.g., “pay cut in 3 years”) — no predictive capability.

## Remember This

- 🔑 Linear optimization maximizes savings given income and category bounds — a formal basis for budget recommendation.
- 📌 LLM advice typically allocates 20% to emergency fund and 15–20% to retirement — standard rules of thumb.
- ⚠️ No real‑world validation — all claims rest on synthetic data and simulated LLM outputs.
- 💡 Preference weights per category enable personalized trade‑offs between necessities and discretionary spending.
- 🧠 Cooperative budgeting models require pooling income and sharing fixed expenses — irrelevant to Odin’s single-user design.
