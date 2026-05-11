# Impact of financial literacy, mental budgeting and self control on financial wellbeing: Mediating impact of investment decision making

## Metadata

```yaml
---
paper_id: "10.1371/journal.pone.0294466"
designation: international
title: "Impact of financial literacy, mental budgeting and self control on financial wellbeing: Mediating impact of investment decision making"
authors: "Bai, R."
year: 2023
venue: "PLoS ONE"
odin_topics: ["C.1"]
shorthand_tags: ["/strategy-mechanics"]
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

Higher financial literacy, mental budgeting, and self-control each improve subjective financial wellbeing among Chinese university students; investment decisions partially mediate these relationships.

## Problem and Motivation

Existing research has not fully explained how cognitive factors (financial literacy, mental budgeting, self-control) jointly affect subjective financial wellbeing, nor whether investment decision making mediates these effects. Financial distress harms mental health, workplace productivity, and overall life satisfaction — making identification of protective cognitive factors urgent. Prior studies examined these variables in isolation, without an integrated mediation model.

## Approach

- Sample: 449 Chinese university students (55% male, 45% female; 60% business majors).
- Measures: Validated scales for financial literacy (7 items), mental budgeting (4 items), self-control (9 items), investment decision making (9 items), and financial wellbeing (7 items).
- Method: Partial Least Squares Structural Equation Modeling (PLS-SEM) for path analysis.
- Evaluation: Measurement model tested via factor loadings (>0.50), composite reliability (>0.70), and AVE (>0.50).
- Mediation: Baron and Kenny approach testing direct plus indirect effects.

## Findings

1. Financial literacy had the largest direct effect on financial wellbeing (β = **0.299**, p < 0.001).
2. Self-control directly predicted financial wellbeing (β = 0.182, p < 0.001).
3. Mental budgeting directly predicted financial wellbeing (β = 0.102, p < 0.001).
4. Investment decision making partially mediated all three paths (indirect effects: 0.017–0.019, p < 0.05).

- All direct effects remained significant after including the mediator (partial mediation).

## Key Figures and Tables

- Figure 1: Research conceptual model → FL, MB, SC → DMB → FWB with direct paths.
- Table 2: Factor loadings, CR, Cronbach’s alpha, AVE → all constructs meet reliability and validity thresholds.
- Table 3: Path analysis results → all seven hypothesized paths supported at p < 0.001 except DMB→FWB at p = 0.059.
- Table 4: Mediation analysis → all three indirect effects significant (partial mediation).

## Key Equations

None.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| Financial literacy | Knowledge of basic financial concepts and ability to apply them to manage money effectively. |
| Mental budgeting | Cognitive process of mentally categorizing, tracking, and allocating income and expenses. |
| Self-control | Ability to regulate impulses, resist temptation, and adhere to long-term financial plans. |
| Financial wellbeing | Subjective evaluation of one’s current and future financial situation (low anxiety + high security). |
| Investment decision making | Process of making financial and investment choices influenced by knowledge, attitudes, and self-control. |
| PLS-SEM | Partial Least Squares Structural Equation Modeling — a regression-based technique for path analysis with latent variables. |

## Critical Citations

- [Thaler, 1999] — Foundational theory of mental accounting that defines mental budgeting mechanisms.
- [Tangney et al., 2004] — Source of the Brief Self-Control Scale used to measure self-control.
- [Baron & Kenny, 1986] — Statistical framework for testing mediation, applied to all three indirect paths.

## Relevance to Odin

**Topics:**

C.1 — Budgeting Strategies and Budget Recommendation

**Contribution to Odin:**

This paper provides behavioral evidence that mental budgeting — the cognitive practice of categorizing and tracking expenses — is positively associated with financial wellbeing, independent of actual income or wealth. For Odin’s budget recommendation module, this justifies designing features that explicitly support mental budgeting behaviors, such as clear per-category spending limits and real-time tracking. The finding that self-control also predicts financial wellbeing reinforces Odin’s design priority of reducing impulsive spending friction (e.g., alerts before overspending) rather than relying solely on user discipline. Although the study uses Chinese student data and no algorithmic intervention, its psychological framework validates the importance of budgeting strategies as a core module in a PBMS.

**Directly justifies:**

- "Mental budgeting has a significant direct positive effect on subjective financial wellbeing (β = 0.102, p < 0.001) after controlling for financial literacy and self-control."
- "Individuals who practice mental budgeting — mentally categorizing and tracking expenses — exhibit higher financial wellbeing and better investment decision-making behavior."
- "Self-control directly predicts financial wellbeing (β = 0.182, p < 0.001), supporting system designs that help users resist impulsive spending."
- "Investment decision making partially mediates the effect of mental budgeting on financial wellbeing, indicating that budgeting habits translate into better long-term financial outcomes."

**Limits of relevance:**

- Sample comprises Chinese university students, not Filipino young professionals; income patterns and cultural spending norms may differ.
- No algorithm or ML method is tested; the study is purely observational and cross-sectional.
- Financial wellbeing is self-reported and subjective, not measured via objective spending or saving data.
- The mediation effect size is small (indirect β 0.016–0.019), suggesting other unmeasured factors dominate.

## Limitations

- Cross-sectional design prevents causal inference; all reported effects are correlational.
- Sample limited to university students (ages not reported, but likely 18–25), not representative of working professionals.
- Self-reported measures may introduce social desirability and recall bias. [unacknowledged]
- No control for income level or socioeconomic status, which could confound relationships.
- Single-country (China) data limits generalizability to the Philippines.

## Remember This

- 🔑 **FL had strongest direct effect (β=0.299)** — financial literacy matters more than budgeting or self-control for wellbeing.
- 📌 Mental budgeting still improved wellbeing (β=0.102) — even small effects justify building budgeting tools.
- ⚠️ Partial mediation, not full — investment decisions explain only part of the link; other pathways exist.
- 💡 Cross-sectional student data — cannot claim causality; use as correlational evidence only.
