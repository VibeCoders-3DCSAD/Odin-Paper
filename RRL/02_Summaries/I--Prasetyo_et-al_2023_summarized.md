# Integrating Financial Management and Gamification: A Systematic Literature Review and Future Research Agenda

## Metadata

```yaml
---
paper_id: "92b0b6f1-2c1f-5d6a-9c7e-8a9f0b1c2d3e"
designation: international
title: "Integrating Financial Management and Gamification: A Systematic Literature Review and Future Research Agenda"
authors: "Prasetyo, A. P.; Santoso, H. B.; Putra, P. O. H."
year: 2023
venue: "Indonesian Journal of Computer Science"
odin_topics: ["A.2", "I.1"]
shorthand_tags: ["/pfms-gap", "/retention-mechanisms", "/pfms-limitations"]
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

A systematic review of 53 studies (2018–2022) finds that gamification in personal finance is under-researched, with most work in education; self-determination theory and technology acceptance models dominate, and future research should explore cultural factors and financial contexts.

## Problem and Motivation

Low public financial behavior leads to poor spending, saving, and investment decisions. Gamification could improve engagement in personal financial management (PFM) apps, but research on gamification in finance remains limited relative to education and health. No prior review has synthesized financial behavior and gamification together, leaving a gap in understanding how game elements affect financial behavioral intention.

## Approach

- Systematic literature review following Kitchenham (2004) guidelines, searching Emerald, IEEE Xplore, Science Direct, and Taylor & Francis.
- Search strings combined “financial behavior” and “gamification” with theory/framework terms; limited to 2018–2022 journal and proceedings papers.
- Initial 27,888 articles filtered to 53 after title/abstract and full-text screening (27 financial behavior, 26 gamification-related).
- Applied the TCCM (Theory, Context, Characteristics, Methodology) framework for structured synthesis.
- Extracted theories, contexts (education, finance, health, e-commerce, etc.), constructs (antecedents, mediators, moderators, consequences), and research methods.

## Findings

- Most financial behavior studies use Theory of Planned Behavior (TPB) (50%); gamification studies use Self-Determination Theory (SDT) (14.3%) and Technology Acceptance Model (TAM) (11.9%).
- **Only 17.2% of gamification research focuses on finance**, primarily banking contexts; education dominates (20.7%).
- Most studied gamification elements: badges (9.7%), points (9.7%), leaderboards (8.0%).
- Quantitative methods (questionnaires) and cross-sectional designs dominate; longitudinal and experimental studies are scarce.
- The paper presents integrated conceptual models of financial behavior and gamification-related behavioral intention, mapping antecedents, mediators, moderators, and consequences.

## Key Figures and Tables

- Figure 3: Integrated conceptual model of financial behavior → Antecedents (financial literacy, socio-demographics, self-control) mediate through habits to behavior.
- Figure 4: Integrated model of gamification behavioral intention → Psychological and gamification antecedents affect intention via mediators like attitude and satisfaction.
- Table 4: Theories used in gamification research → SDT, TAM, TPB most common; 25 theories total.
- Table 6: Contexts of gamification research → Education (20.7%), Finance (17.2%), Health (17.2%).
- Table 7: Gamification elements → Badges, points, leaderboards top three.

## Key Equations

None.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| PFM | Personal financial management — apps that help users track spending, budget, and save. |
| TCCM | Theory, Context, Characteristics, Methodology — a framework for systematic literature reviews. |
| TPB | Theory of Planned Behavior — intention predicts behavior; influenced by attitudes, norms, and perceived control. |
| SDT | Self-Determination Theory [think: three innate needs: autonomy, competence, relatedness]. |
| TAM | Technology Acceptance Model — perceived usefulness and ease of use drive technology adoption. |
| UTAUT | Unified Theory of Acceptance and Use of Technology — integrates eight prior adoption models. |
| PLS-SEM | Partial Least Squares Structural Equation Modeling — a statistical technique for complex cause-effect models. |

## Critical Citations

- [Goyal et al., 2021] — Prior systematic review of personal financial management behavior antecedents and consequences.
- [Koivisto & Hamari, 2019] — Foundational gamification review identifying research gaps, including limited finance focus.
- [Bitrián et al., 2021] — Empirical study of gamification in the Mint PFM app, cited as a key finance-context example.

## Relevance to Odin

**Topics:**

A.2 — Existing Personal Finance and Budget Management Systems

I.1 — User Retention and Engagement in Personal Finance Systems

**Contribution to Odin:**

Although Odin explicitly excludes gamification, this review’s synthesis of behavioral intention theories (TPB, SDT) provides foundational justification for Odin’s engagement design: users’ perceived usefulness and autonomy support directly influence continued use, independent of game elements. The finding that only 17.2% of gamification research addresses finance highlights a broader gap in understanding user motivation in PFM — a gap Odin’s non-gamified, value-driven forecasting and anomaly detection can fill. The paper’s identification of cultural factors as an underexplored moderator directly supports Odin’s need for Filipino-specific behavioral research. Further, the scarcity of longitudinal studies on sustained behavior change informs Odin’s evaluation plan, which will track retention over time.

**Directly justifies:**

- “Financial behavior research predominantly uses the Theory of Planned Behavior (50% of studies), which underpins the intention-action relationship central to budget adherence.”
- “Self-Determination Theory (14.3% of gamification studies) explains user motivation through autonomy, competence, and relatedness — applicable to non-gamified features like personalized budget recommendations.”
- “Only 17.2% of gamification research focuses on finance, leaving a significant gap in understanding how to drive engagement in PFM apps without gamification.”
- “Most gamification studies use cross-sectional surveys; longitudinal evidence on sustained behavior change is lacking, highlighting a method gap Odin’s evaluation could address.”

**Limits of relevance:**

- The paper is a systematic literature review, not an empirical study; its claims are synthesized from others, not original findings on causality.
- No Filipino-specific data; cultural factors are identified as a research gap, not studied.
- Odin explicitly excludes gamification, so direct application of gamification-element findings is limited to informing what not to do or transferring psychological theory.
- Publication window ends in 2022; newer studies (2023 onward) on PFM engagement are not included.

## Limitations

- Publication window 2018–2022; may miss recent advances in PFM gamification. [unacknowledged]
- Only English articles; may exclude relevant non-English research from Southeast Asia.
- No quality assessment of included studies; all 53 articles treated as equally valid.
- No meta-analysis; findings are qualitative and directional rather than quantitative.
- Does not deeply explore potential negative effects of gamification (e.g., overjustification, reduced intrinsic motivation) despite mentioning them as a future research area. [unacknowledged]

## Remember This

- 🔑 **17.2% of gamification work touches finance** — most research is in education, not PFM.
- 📌 TPB dominates financial behavior studies (50%) — intention models transfer directly to Odin’s budgeting module.
- 💡 SDT’s autonomy/competence/relatedness — non-gamified features (forecasting, anomaly alerts) can satisfy these needs.
- ⚠️ No longitudinal studies on sustained behavior change — Odin’s evaluation plan can fill this gap.
- 🔍 Cultural factors are an unstudied moderator — Filipino behavioral research is explicitly needed.
