# Understanding the Impulse Buying Behavior in the Digital Age: Influential Factors in Online Consumer Behavior

## Metadata

```yaml
---
paper_id: "10.1145/3760557.3760578"
designation: local
title: "Understanding the Impulse Buying Behavior in the Digital Age: Influential Factors in Online Consumer Behavior"
authors: "Gabatin, R.; Sierra, S.; Maniago, M.; Capole, A.; Torres, R."
year: 2025
venue: "16th International Conference on E-business, Management and Economics (ICEME 2025)"
odin_topics: ["A.1", "F.1"]
shorthand_tags: ["/expenditure-patterns", "/fil-behavioral-patterns"]
member_checklist:
  - name: "Gabion, Stefanie S."
    status: "[ ]"
  - name: "Guevarra, Joaquin Luis T."
    status: "[ ]"
  - name: "San Jose, Alexa Joanne Paula G."
    status: "[ ]"
  - name: "Togle, Charles Nathaniel B."
    status: "[ ]"
---
```

## TL;DR

Website ease and payment options increase urgency, strongly predicting impulse buying (β=0.804, p<0.001) among Filipino online shoppers.

## Problem and Motivation

The drivers of impulse buying in online shopping—specifically how social, marketing, and website factors interact—remain poorly integrated in a single model. Impulse purchases account for 60% of all purchases, affecting consumer financial well-being and e-commerce strategies. Prior studies lacked a unified framework that includes the mediating roles of website quality and consumer characteristics.

## Approach

- Quantitative design with a self-administered survey (five-point Likert scale) of 381 respondents from Cabuyao, Laguna, Philippines.
- Participants: ages 21–30 (Gen Z) and 31–40 (Millennials) with online shopping experience.
- Theoretical framework: Stimulus-Organism-Response (SOR) model.
- Variables: social-related factors (peer influence, word of mouth), marketing-related (discounts), website-related (ease of use, ease of payment), consumer characteristics (income, shopping lifestyle), urgency to buy, impulse buying.
- Analysis: Partial Least Squares Structural Equation Modeling (PLS-SEM) using WarpPLS 8.0.
- Evaluation metrics: composite reliability, Cronbach’s alpha, AVE, Fornell-Larcker criterion, VIF, R², Q².

## Findings

1. Urgency to buy has the strongest direct effect on impulse buying (**β=0.804**, p<0.001, large effect size).
2. Consumer characteristics strongly affect urgency (β=0.562, p<0.001) and directly affect impulse buying (β=0.109, p=0.016, small effect).
3. Social factors strongly influence website-related factors (β=0.868, p<0.001), but do not directly drive impulse buying (H1 rejected).
4. Marketing factors (discounts) strongly shape consumer characteristics (β=0.714, p<0.001), but do not directly affect impulse buying (H2 rejected).
5. Website-related factors have a small direct effect on urgency (β=0.099, p=0.026) and no direct effect on impulse buying (H8 rejected).

- Age and gender do not moderate the urgency–impulse buying relationship (H12, H13 rejected).
- The model explains 80.4% of variance in impulse buying (R²=0.804).

## Key Figures and Tables

- Figure 1: Conceptual framework (SOR with all constructs) → shows hypothesized paths among six latent variables.
- Figure 2: Final model after removing insignificant paths → highlights website→urgency→impulse and consumer characteristics paths.
- Table 4: Structural model evaluation (path coefficients, p-values, f²) → urgency→impulse has f²=0.660 (large effect).

## Key Equations

None.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| SOR | Stimulus-Organism-Response — a framework where external stimuli trigger internal states that lead to behavioral responses. |
| PLS-SEM | Partial Least Squares Structural Equation Modeling — a statistical method for analyzing complex cause-effect relationships, suited for small samples and non-normal data. |
| eWOM | Electronic word of mouth — online recommendations or reviews from other consumers. |
| Impulse buying | An unplanned, spontaneous purchase driven by immediate urges rather than deliberate consideration. |
| Urgency to buy | The psychological pressure to purchase quickly, often triggered by time limits or scarcity cues. |
| AVE | Average Variance Extracted — a measure of convergent validity; values above 0.5 are acceptable. |

## Critical Citations

- [Aprilia & Wibowo, 2016] — Provides the 60% impulse purchase baseline statistic.
- [Khare & Pandey, 2017] — Foundational SOR framework application to online consumer behavior.
- [Azul et al., 2023] — Connects impulse buying to financial well-being of Filipino young professionals.

## Relevance to Odin

**Topics:**

A.1 — Spending and Budgeting Behavior of Filipino Young Professionals

F.1 — User Behavioral Profiling in Filipino Personal Finance Contexts

**Contribution to Odin:**

This paper directly informs Odin’s understanding of impulse spending as a component of Filipino young professionals’ financial behavior, grounding module designs in local behavioral data. The finding that consumer characteristics (shopping lifestyle, income) significantly drive urgency and impulse buying justifies including these features in Odin’s user profile classification (F.1) to better predict spending deviations. Although the study focuses on e-commerce, its insights apply to any digital environment where users make spending decisions—Odin’s manual transaction interface can similarly trigger unplanned purchases if designed without friction controls. The mediation results also suggest that website ease and payment options indirectly affect spending, which can guide Odin’s interface design to either nudge or mitigate impulsive entries.

**Directly justifies:**

- “Among Filipino online shoppers, urgency to buy has a strong direct effect on impulse buying (β=0.804, p<0.001), the largest path in the model.”
- “Consumer characteristics (shopping lifestyle and income) significantly influence urgency to buy (β=0.562, p<0.001) and directly affect impulse buying (β=0.109, p=0.016).”
- “Social-related factors do not directly drive impulse buying but strongly shape website perception (β=0.868, p<0.001), which then affects urgency.”
- “Marketing-related factors (discounts) do not directly cause impulse buying but strongly shape consumer characteristics (β=0.714, p<0.001).”
- “Age and gender do not moderate the urgency–impulse relationship, suggesting these demographic variables are less critical than behavioral traits in explaining impulse spending.”

**Limits of relevance:**

- The study measures self-reported impulse buying intentions, not actual transaction-level spending data.
- The sample is limited to one city (Cabuyao, Laguna) and may not represent all Filipino young professionals.
- The paper does not evaluate financial outcomes (e.g., budget overages, savings impact) of impulse buying.
- Findings are cross-sectional; causal direction is assumed from the SOR framework but not experimentally proven.

## Limitations

- Purposive (non-probability) sampling limits generalizability to the broader Filipino population.
- Self-reported survey data may suffer from social desirability and recall bias. [unacknowledged]
- No control for financial literacy or existing budgeting habits, which could moderate impulse buying. [unacknowledged]
- The study does not examine long-term consequences of impulse buying on financial health or debt.
- Cross-sectional design cannot confirm causal ordering despite the SOR framework assumptions.

## Remember This

- 🔑 **Urgency→impulse β=0.804** — this single path explains most unplanned online purchases.
- 📌 Shopping lifestyle and income shape urgency — Odin profiles must capture these traits.
- ⚠️ Discounts don't directly cause impulse buys — they work by changing consumer characteristics.
- ✅ Website ease and payment options matter, but only through urgency (β=0.099, small effect).
- 💡 Filipino young adults (21–40) in the sample show strong urgency-driven impulse spending.
