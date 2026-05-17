# Mental Accounting Through Two-stage Budgeting Under Bounded Rationality

## Metadata

```yaml
---
paper_id: "10.21203/rs.3.rs-7730348/v1"
designation: algorithm-specific
title: "Mental Accounting Through Two-stage Budgeting Under Bounded Rationality"
authors: "Pretnar, N.; Olivola, C. Y.; Montgomery, A."
year: 2025
venue: "Research Square"
odin_topics: ["5.A", "5.C", "7.A", "7.B", "8.A"]
shorthand_tags: ["/profiling-role", "/profile-dimensions", "/classifier-candidates", "/classifier-eval-metrics", "/strategy-mechanics", "/budgeting-evidence", "/budget-rec-approaches", "/budget-rec-evidence", "/anomaly-taxonomy", "/overage-vs-deviation"]
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

A structural model of two-stage budgeting with cognitive constraints reveals that low-income consumers update only half their budgets weekly, and relaxing these constraints can cause some to overspend into bankruptcy.

## Problem and Motivation

Classical expenditure models assume perfect fungibility and no timing frictions, while mental accounting theory suggests budgets discipline spending but lacks a generalizable framework. Understanding how consumers actually use budgets is critical for designing effective financial interventions. Prior work had not provided a micro‑founded model that allows varying degrees of bounded rationality and can be estimated from observed expenditure alone.

## Approach

- **Dataset:** Weekly expenditure and income for 2,509 low‑income prepaid debit card users (71,859 weeks) in North America; categories: groceries, gasoline, food away from home, and other.
- **Model:** Two‑stage budgeting with a forward‑looking “planner” (sets budgets) and a myopic “doer” (spends with random shocks). Budgets are ωᵢⱼₜ = θᵢⱼₜ ℓᵢₜ + γᵢ aᵢⱼₜ, where aᵢⱼₜ is the mental account (over/under‑spent last period).
- **Cognitive constraints:** In any period, the consumer re‑evaluates each budget with probability ψᵢⱼ (Bernoulli draw). Narrow choice bracketing is induced by independent draws across categories.
- **Numeracy constraints:** A budget update is implemented only if the absolute change exceeds a threshold (ϵ = 0, 0.01, 0.05, 0.1 or ϵₗ = $0.01, $1).
- **Estimation:** Bayesian MCMC (Metropolis‑within‑Gibbs) that inverts the model’s first‑order conditions to infer latent budgets, mental accounts, and update indicators from expenditure alone.

## Findings

1. Best‑fitting model uses a **$1 numeracy threshold**; consumers update on average **2.11 out of 4 budgets per week** (baseline: 2.48 updates).
2. **78%** of consumers are ex‑ante “budget prioritizers” (reduce budget after over‑spending), but only **11%** show the same pattern in realized spending.
3. Most common type (**37‑38%**): ex‑ante budget prioritizer but ex‑post spendthrift (increase spending regardless of prior over/under‑spending).
4. Relaxing cognitive constraints (forcing full weekly updates) makes **68%** of consumers worse off; **3.3%** go bankrupt under the $1‑threshold model.
5. Bankrupt consumers had significantly fewer budget updates before relaxation (**1.25 vs 2.11 per week**), indicating sticky budgets served as a self‑discipline mechanism.

## Key Figures and Tables

- Figure 2: Predictive mean fits for median‑income consumer → baseline and $1‑threshold models produce nearly identical predictions.
- Figure 3: Distribution of weekly budget updates → $1 threshold reduces updates by 15%; relative thresholds (ϵ=0.1) reduce them by 70%.
- Table 2: Posterior summary statistics → high variance in mental account balances and likelihood errors reflects spending spikiness.
- Table 3: Marginal types → ex‑ante 78‑83% are budget prioritizers; ex‑post only 11% are, while 43‑47% are spendthrifts.
- Table 4: Joint types → 37‑38% are ex‑ante budget prioritizers + ex‑post spendthrifts (planning fallacy syndrome).

## Key Equations

$$ω_{ijt} = θ_{ijt}ℓ_{it} + γ_i a_{ijt}$$
*Budget equals income share plus mental‑account adjustment weighted by γ_i.*

$$x_{ijt} = ω_{ijt} + ζ_{ijt}, \quad ζ_{ijt} ∼ N(0, σ^2_{ij})$$
*Actual expenditure equals budget plus mean‑zero shock (price or taste).*

$$a_{ij,t+1} = ω_{ijt} - x_{ijt} = -ζ_{ijt}$$
*Mental account balance carries forward last period’s over/under‑spending.*

$$ϑ^*_{iyt} = E_{it}\left[ \frac{α_{i,ι_{iyt}}ℓ_{it} - α_{i,ι_{iyt}}∑_{s≠y}(ϑ^*_{ist}ℓ_{it}+γ_i a_{i,ι_{ist},t}+ζ_{i,ι_{ist},t}) - ...}{ℓ_{it}(α_{i,ι_{iyt}}+α_{i,J+1})} \right]$$
*Optimal candidate budget share (inverted from first‑order condition).*

## Definitions

| Term / Acronym | Plain‑English Definition |
| -------------- | ------------------------ |
| Mental accounting | Book‑keeping mechanism where past over/under‑spending influences future budgets. |
| Two‑stage budgeting | Consumer first allocates income to broad categories, then spends within each. |
| Bounded rationality | Decision‑making limited by cognitive attention and numeracy, not full optimization. |
| Planner/doer | Two‑self model: planner sets budgets ex‑ante; doer reacts to shocks ex‑post. |
| Narrow choice bracketing | Re‑evaluating only a subset of budgets each period due to attention limits. |
| Numeracy constraint | Budget change must exceed a minimum absolute or percentage threshold to be implemented. |
| Mental account balance (aᵢⱼₜ) | Positive = under‑spent last period; negative = over‑spent. |
| γᵢ | Anchoring parameter (0 to 1): how strongly mental account affects next budget. |
| ψᵢⱼ | Probability a consumer re‑evaluates category j’s budget each week. |
| Γᵢⱼₜ (underline) | Indicator =1 if category j is re‑evaluated in period t (extensive margin). |
| Γᵢⱼₜ (no underline) | Indicator =1 if re‑evaluation and numeracy constraint are both satisfied. |

## Critical Citations

- [Thaler, 1985] — Mental accounting framework that tracks over/under‑spending across categories.
- [Gabaix, 2014] — Sparse maximization and narrow choice bracketing foundations.
- [Deaton and Muellbauer, 1980a] — Classical two‑stage budgeting and weak separability.
- [Shefrin and Thaler, 1981] — Planner/doer model of self‑control and budgeting.
- [Hastings and Shapiro, 2018] — Empirical evidence of mental accounting in low‑income food spending.

## Relevance to Odin

**Topics:**

5.A — Financial Behavioral Profiles in Personal Finance

5.C — Financial Behavioral Profile Classification Algorithm

7.A — Budgeting Strategies as Domain Knowledge

7.B — Budget Recommendation in Personal Finance Systems

8.A — Anomaly Detection in Personal Finance Systems

**Contribution to Odin:**

This paper provides a rigorous, data‑driven typology of how consumers use budgets (budget prioritizers, spending followers, spendthrifts, frugal savers), which directly informs the design of Odin’s behavioral profiling module. The finding that sticky budgets act as a self‑discipline mechanism for a subset of users justifies Odin’s default design: not forcing frequent budget re‑evaluations and allowing users to set their own update frequency. The counterfactual result that relaxing attention constraints can lead to bankruptcy warns against overly aggressive nudging (e.g., push notifications that demand weekly budget reviews), supporting Odin’s principle of value‑driven retention rather than gamified or high‑frequency interventions.

**Directly justifies:**

- “Low‑income consumers update only 2.11 of 4 budgets per week on average, providing evidence that narrow choice bracketing is the norm, not the exception.”
- “Ex‑ante budget prioritizers (78% of consumers) reduce budgets after over‑spending, but 37‑38% become ex‑post spendthrifts — a ‘planning fallacy’ pattern where intentions fail to control actual spending.”
- “Relaxing cognitive constraints makes 68% of consumers worse off, and 3.3% go bankrupt, proving that sticky budgets can be a beneficial self‑control device for financially vulnerable users.”
- “Bankrupt consumers had significantly fewer budget updates (1.25 per week) before the constraint was relaxed, showing that low attention is not a flaw but a protective discipline for some.”
- “A $1 absolute numeracy threshold fits the data better than percentage thresholds, suggesting consumers think in dollar‑unit changes rather than relative percentages.”

**Limits of relevance:**

- Study population is low‑income North American prepaid card users; Filipino young professionals may have different income volatility and cultural spending obligations.
- The model assumes manual budget setting by consumers; Odin uses algorithm‑recommended budgets, which may alter adherence dynamics.
- Data lacks explicit budget observations (only expenditure); inferences are model‑dependent and require validation on budgeting‑aware datasets.

## Limitations

- No independent budget observations exist to validate latent inferences; results are model‑dependent.
- The sample consists entirely of underbanked prepaid card users; findings may not generalize to banked or credit‑using populations. [unacknowledged]
- The model assumes strong separability and Stone‑Geary utility, which restricts substitution patterns.
- The counterfactual experiment forces all consumers to update all budgets every week; real‑world interventions (e.g., app notifications) are less extreme.
- Filipino cultural practices (family obligations, informal finance, seasonal spending) are not represented in the data or model.

## Remember This

- 🔑 **2.11 of 4 budgets updated weekly** — narrow bracketing is the norm, not full rationality.
- 📌 **78% ex‑ante budget prioritizers vs 11% ex‑post** — most consumers fail to translate good intentions into spending discipline.
- 💡 **$1 numeracy threshold** beats percentage thresholds — users think in absolute dollars, not percentages.
- ⚠️ **Forcing weekly updates makes 68% worse off, 3.3% bankrupt** — sticky budgets protect vulnerable users from themselves.
- 🧠 **Bankrupt consumers updated only 1.25 budgets/week** — low attention can be a beneficial discipline mechanism.
