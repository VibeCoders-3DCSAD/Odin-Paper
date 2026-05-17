# Exploring the Interplay of Life Attitude and Cognitive Ability in Shaping the Intention to Stock Market Participation Among Young Professionals in the Philippines

## Metadata

```yaml
---
paper_id: "10.3390/ijfs13040222"
designation: local
title: "Exploring the Interplay of Life Attitude and Cognitive Ability in Shaping the Intention to Stock Market Participation Among Young Professionals in the Philippines"
authors: "Mutuc, E. B."
year: 2025
venue: "International Journal of Financial Studies"
odin_topics: ["1.A", "1.C", "5.A"]
shorthand_tags: ["/yp-profile", "/literacy-behavior-gap", "/profile-dimensions", "/fil-profile-construction"]
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

Life attitude dimensions, particularly death acceptance and goal seeking, positively influence stock market participation intention among Filipino young professionals, with financial literacy mediating this relationship.

## Problem and Motivation

Behavioral finance research has extensively examined wealth, literacy, and risk aversion but rarely explored how broader life orientations—purpose, meaning, and future orientation—affect stock market participation. Understanding these psychological drivers is crucial for young professionals in emerging economies like the Philippines, where digital finance access is expanding but investment behavior is poorly understood. No prior study had integrated existential psychology constructs (Life Attitude Profile) with cognitive ability to explain equity market engagement intentions in this demographic.

## Approach

- Quantitative cross-sectional survey of 195 randomly selected young professionals (aged 20–39) in Bulacan, Philippines (response rate 50.8%).
- Life Attitude Profile–Revised (LAP-R) measured seven dimensions: life purpose, existential vacuum, life control, death acceptance, will to meaning, goal seeking, and future meaning to fulfil (7-point Likert scale).
- Cognitive ability proxied by 16-item Financial Literacy Inventory (van Rooij et al., 2011), scored as percentage correct (mean = 67.83%, SD = 16.53).
- Intention to stock market participation measured with three adapted items from Ajzen’s theory of planned behavior (5-point scale).
- PLS-SEM with 5000 bootstrap resamples tested direct and mediated effects, controlling for sex, age, education, and employment.
- Discriminant validity assessed via Fornell–Larcker criterion and HTMT (<0.85 threshold); common method variance tested via Harman’s single-factor test (first factor explained 29.32%).

## Findings

1. Overall Life Attitude Profile positively predicts stock market participation intention (β = 0.154, p = 0.025; R² = 0.471–0.582).
2. **Death acceptance (β = 0.312, p < 0.001) and goal seeking (β = 0.396, p = 0.009) are the strongest positive predictors** of investment intention.
3. Life purpose shows a negative relationship with stock market participation (β = -0.243, p = 0.036), suggesting purpose-driven individuals may prefer security over speculative investing.
4. Cognitive ability mediates the LAP→SMP relationship (indirect β = 0.051, p = 0.032; 95% CI [0.004, 0.098]).
5. Financial literacy directly predicts stock market participation (β = 0.329, p < 0.001), reinforcing its enabling role.

- Existential vacuum, life control, will to meaning, and future meaning to fulfil showed non-significant direct effects.
- Males relied more on cognitive ability (C→SMP β = 0.42) while females showed stronger attitudinal influence (LAP→SMP β = 0.38).

## Key Figures and Tables

- Figure 1: Conceptual framework → LAP affects SMP directly and via cognitive ability mediation.
- Figure 3: Lower-order construct → negative paths from life control and life purpose to SMP.
- Figure 4: Higher-order construct → LAP→SMP β=0.154, C→SMP β=0.329, R²=0.471.
- Table 5: Hypothesis testing summary → significant paths for LP (negative), DA, GS, LAP→C, C→SMP, and mediation.
- Table 4: Fornell–Larcker discriminant validity → all √AVE > inter-construct correlations.

## Key Equations

None. The paper presents ordinary least squares regression equations (1)–(6) but no novel mathematical formulations central to the contribution.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| LAP | Life Attitude Profile — measures purpose, control, meaning, and future orientation across seven dimensions. |
| SMP | Intention to Stock Market Participation — the dependent variable measured as planned future investment behavior. |
| C | Cognitive Ability — operationalized as financial literacy score (percentage correct on 16-item test). |
| PLS-SEM | Partial Least Squares Structural Equation Modeling — variance-based technique for mediation and prediction with non-normal data. |
| AVE | Average Variance Extracted — proportion of indicator variance explained by a latent construct; >0.50 indicates convergent validity. |
| HTMT | Heterotrait–Monotrait Ratio — criterion for discriminant validity; values <0.85 confirm constructs are distinct. |
| LAP-R | Life Attitude Profile–Revised — the validated instrument by Reker used to measure life attitude dimensions. |

## Critical Citations

- [van Rooij et al., 2011] — Financial literacy inventory source; foundational for cognitive ability measurement.
- [Fornell & Larcker, 1981] — Discriminant validity criterion used to confirm construct distinctness.
- [Hair et al., 2021] — PLS-SEM best practices guide for bootstrapping and mediation testing.
- [Ajzen, 1991] — Theory of planned behavior source for intention measurement items.
- [Reker et al., 1987] — Original LAP framework establishing life attitude as a psychological construct.

## Relevance to Odin

**Topics:**

1.A — Filipino Young Professionals as a Demographic

1.C — Financial Behavior of Filipino Young Professionals

5.A — Financial Behavioral Profiles in Personal Finance

**Contribution to Odin:**

This paper provides empirical evidence that psychological dispositions (life attitude dimensions) and cognitive ability (financial literacy) jointly determine financial intentions among Filipino young professionals. For Odin’s financial behavioral profiling module, the findings justify incorporating attitudinal measures (e.g., goal orientation, future meaning) alongside literacy assessment to construct richer user profiles. The mediating role of cognitive ability—showing that attitudes translate into behavior only when supported by knowledge—directly supports Odin’s design decision to embed financial literacy scaffolding within the onboarding flow rather than treating it as a separate educational module. Although the outcome is stock market participation rather than budgeting adherence, the psychological mechanism (attitude → cognition → intention) generalizes to Odin’s goal of converting user financial attitudes into consistent budgeting behavior.

**Directly justifies:**

- “Goal seeking positively predicts financial intention among Filipino young professionals (β = 0.396, p = 0.009), supporting the inclusion of goal-orientation items in behavioral profiling instruments.”
- “Financial literacy mediates 51% of the relationship between life attitude and financial intention, indicating that cognitive ability is a necessary conduit for psychological dispositions to translate into action.”
- “Death acceptance (reconciliation with mortality) predicts higher financial risk-taking intention (β = 0.312, p < 0.001), suggesting that existential factors influence financial behavior beyond traditional risk aversion measures.”
- “PLS-SEM with bootstrapping (5000 resamples) is an appropriate analytical method for mediation testing in behavioral finance studies with moderate sample sizes (N = 195).”
- “Life purpose negatively correlates with stock market participation (β = -0.243), implying that strongly purpose-driven individuals may avoid speculative financial activities—a counterintuitive finding that suggests profile segmentation must distinguish between types of purpose.”

**Limits of relevance:**

- The study measures *intention* to participate in stock markets, not actual budgeting or spending behavior—Odin’s core domain is budget adherence, not investment.
- Sample drawn from Bulacan province, not Metro Manila; Metro Manila young professionals may have different income structures and financial access.
- Cross-sectional design cannot establish causality between life attitude, cognitive ability, and financial behavior; Odin’s profiling requires longitudinal updating.
- Cognitive ability measured only as financial literacy; Odin may need broader cognitive assessments (numeracy, reasoning) not covered here.
- No specific algorithm or model is proposed; the paper is theoretical/empirical rather than engineering-focused.

## Limitations

- Self-reported data may introduce social desirability bias despite anonymity assurances.
- Cross-sectional design prevents causal inference; temporal ordering between life attitudes and investment intention cannot be established.
- Common method variance was tested via Harman’s single-factor test (29.32% variance by first factor) but no marker variable was included. [unacknowledged]
- LAP-R was used in original English without cultural adaptation or pilot testing for the Filipino population.
- Sample limited to one province (Bulacan); findings may not generalize to other Philippine regions or to young professionals with different socioeconomic backgrounds.

## Remember This

- 🔑 Death acceptance (β=0.312) and goal seeking (β=0.396) most strongly drive investment intention among Filipino young professionals.
- 📌 Financial literacy mediates the attitude→intention link (indirect β=0.051, p=0.032) — knowledge is the bridge from life orientation to action.
- ⚠️ Life purpose negatively predicts participation (β=-0.243) — meaning-driven individuals may actively avoid speculative investing.
- 💡 PLS-SEM model explains 47–58% of variance in investment intention using psychological and cognitive predictors.
- 🧠 Males rely more on cognitive ability (β=0.42), females on life attitude (β=0.38) — profiling should be gender-sensitive.
