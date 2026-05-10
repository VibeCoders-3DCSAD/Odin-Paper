# A User-Centric Exploration of Axiomatic Explainable AI in Participatory Budgeting

## Metadata

```yaml
---
paper_id: "10.1145/3675094.3677599"
designation: international
title: "A User-Centric Exploration of Axiomatic Explainable AI in Participatory Budgeting"
authors: "Hashemi, M.; Darejeh, A.; Cruz, F."
year: 2024
venue: "Companion of the 2024 ACM International Joint Conference on Pervasive and Ubiquitous Computing (UbiComp Companion '24)"
odin_topics: ["H.1", "J.1"]
shorthand_tags: ["/user-trust", "/eval-pfms-applied"]
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

Users find axiomatic explanations helpful for understanding system decisions and perceiving fairness, but trust impact is mixed — 27% increased trust, 23% decreased.

## Problem and Motivation

Participatory budgeting mechanisms often use complex voting rules that satisfy desirable properties (axioms), but users lack transparency into why specific allocations are chosen. Without explanations, users may not trust or perceive the outcome as fair. Prior work did not evaluate whether axiom-based explanations actually improve user understanding, trust, or fairness perceptions in a live participatory budgeting setting.

## Approach

- **Dataset:** 26 participants via Mechanical Turk (16 male, 10 female; 62% aged 25–34; 50% from India, 42.3% from US).
- **Method:** Used integer linear programming (ILP) with axioms (feasibility, exhaustiveness, utilitarian welfare consistency) as constraints to find and justify allocations.
- **Two scenarios:** Case 1 (department budget, two projects), Case 2 (city budget, three projects). Both used greedy rule — majority approval determined outcome.
- **Measurements:** User ratings on transparency, trust, and fairness before and after receiving axiom-based explanations.
- **Comparison:** Personalized vs. counterfactual explanation preference assessed via survey.

## Findings

1. **72.4%** of participants found explanations “extremely helpful” or “very helpful” for understanding the system’s decision.
2. **63.3%** preferred general (personalized) explanations over counterfactual ones.
3. **30%** reported a positive impact on perceived fairness after explanations; none reported a negative impact.
4. Trust changes post-explanation: **27%** increased, **23% decreased**, 50% unchanged — no clear positive effect.

- User understanding of system decisions improved in both cases after explanations (Fig. 1a, 1b).
- Perceived fairness also improved in both cases (Fig. 1e, 1f).

## Key Figures and Tables

- Figure 1a: User understanding before/after explanation, case 1 → understanding shifts from low/mid to high after explanation.
- Figure 1b: User understanding before/after explanation, case 2 → similar improvement pattern.
- Figure 1c: User trust before/after, case 1 → mixed; some decrease after explanation.
- Figure 1e: Fairness perception before/after, case 1 → marked shift toward “fair” after explanation.
- Figure 1f: Fairness perception before/after, case 2 → consistent improvement.

## Key Equations

$$ \max \sum_{j=1}^{m} x_j $$
*Maximize the number of funded projects subject to constraints.*

$$ \sum_{c_k \in C} cost(c_k) \le B $$
*Feasibility: total project cost cannot exceed budget.*

$$ B - \sum_{c_k \in C} cost(c_k) < cost(c'), \forall c' \in X \setminus C $$
*Exhaustiveness: no leftover budget can fund any unfunded project.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| XAI | Explainable Artificial Intelligence — methods that clarify why an AI made a decision. |
| Axiom | A desired property or agreed-upon value that a voting mechanism should satisfy (e.g., feasibility). |
| Participatory Budgeting (PB) | A democratic process where residents vote on how to allocate public funds. |
| ILP | Integer Linear Programming — solving optimization problems where variables are integers (0 or 1 for fund/don’t fund). |
| Counterfactual explanation | A “what if” scenario showing how the outcome would change if your vote differed. |

## Critical Citations

- [Procaccia, 2019] — Argues that axioms should explain solutions in social choice, grounding this paper’s approach.
- [Boixel & Endriss, 2020] — Automated justification via constraint solving; direct methodological precedent.
- [Cailloux & Endriss, 2016] — Logic-based language for arguing about voting rules.

## Relevance to Odin

**Topics:**

H.1 — Data Privacy, Security, and User Trust

J.1 — System Evaluation

**Contribution to Odin:**

This paper directly informs Odin’s design priority of user trust and explainability in automated budget allocation. Although the domain is public participatory budgeting, the finding that axiom-based explanations improve perceived fairness and understanding applies directly to Odin’s budget recommendation module, where users may question why a particular category allocation was suggested. The mixed trust result (23% decreased trust post-explanation) serves as a critical warning: explanations can backfire. Odin’s evaluation plan (ISO 25010, SUS) should explicitly measure explanation impact on trust, not just usability.

**Directly justifies:**

- “Axiom-based explanations improved user understanding in 72.4% of participants, supporting the use of transparent, rule-based justifications in automated budgeting systems.”
- “Explanations increased perceived fairness in 30% of users and caused no fairness decrease, indicating that even simple rule-based explanations enhance outcome legitimacy.”
- “Providing explanations decreased trust in 23% of users — a non-trivial backfire effect that must be measured, not assumed, when adding XAI to a personal finance system.”

**Limits of relevance:**

- Study uses public participatory budgeting (voting on public projects), not personal budget allocation. Users’ relationship to the outcome differs (collective vs. individual).
- Small sample (n=26) and pilot-stage findings; no statistical significance reported.
- Greedy rule is simpler than Odin’s planned constraint optimization or ML-based recommendation; explanatory mechanism may not generalize directly.
- No Filipino participants; cultural attitudes toward algorithmic explanations may vary.

## Limitations

- Pilot study with only 26 participants; results are indicative but not statistically robust.
- No control condition without explanations for direct comparison (pre/post design within same users). [unacknowledged]
- Did not measure whether improved understanding led to better long-term engagement or behavior change.
- Counterfactual explanation preference (63% preferred general) may not hold in personal finance contexts where users have stronger stake in outcomes.
- Trust measurement was crude (increase/decrease/no change); did not capture nuanced reasons for trust loss. [unacknowledged]

## Remember This

- 🔑 **72.4%** found axiom explanations helpful — transparency works for most users.
- ⚠️ 23% **lost trust** after explanation — don’t assume XAI always builds trust.
- 📌 Perceived fairness rose (30% positive, 0% negative) — rule-based justifications improve legitimacy.
- 💡 Users prefer general explanations over “what if” counterfactuals — design for simple, personalized reasons first.
