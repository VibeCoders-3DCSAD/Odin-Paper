# THE IMPACT OF CATEGORIZATION ON CONSUMPTION BEHAVIOR

## Metadata

```yaml
---
paper_id: "6ba7b810-9dad-11d1-80b4-00c04fd430c8"
designation: international
title: "THE IMPACT OF CATEGORIZATION ON CONSUMPTION BEHAVIOR"
authors: "Yin, S."
year: 2025
venue: "University of Pennsylvania"
odin_topics: ["1.C", "2.C", "4.A", "4.B", "7.A", "7.B", "11.B"]
shorthand_tags: ["/budget-failure-points", "/intelligent-vs-literacy", "/priority-config", "/pfms-intelligent-features", "/pfms-limitations", "/budgeting-evidence", "/budget-rec-evidence", "/goal-engagement"]
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

Categorizing financial resources as used (vs. unused) increases spending likelihood by devaluing remaining balances, while saving for experiential goals (vs. material goods) boosts motivation and sustained saving streaks.

## Problem and Motivation

Consumers constantly decide whether to spend or save money and time, but existing research has not systematically examined how the categorization of an account as “used” or “unused” influences future spending decisions. Understanding this effect could help design better budgeting tools and savings interventions. Prior work on mental accounting focused on labeling resources for different needs, leaving open how prior spending from an account changes valuation of what remains.

## Approach

- **Essay 1 (Chapters 1)**: Seven experimental studies (N = 8,667; six preregistered) manipulating used vs. unused accounts across gift cards, checking accounts, credit card reward points, and incentive-compatible behavioral tasks.
- **Essay 2 (Chapter 2)**: Analysis of American Time Use Survey (ATUS) data plus controlled experiments examining when within a categorized time period (e.g., end vs. start of an hour) people choose leisure activities.
- **Essay 3 (Chapter 3)**: Multiple experiments comparing experiential savings goals (e.g., hiking trips) vs. material savings goals (e.g., hiking gear) on saving motivation, perceived versatility, and actual saving streaks.
- Key manipulations: used account (e.g., $10 left from $100 gift card) vs. unused account (e.g., $10 gift card); proportion remaining (60%, 40%, 20%) to test moderation.
- Mechanism measures: valuation of remaining resources (0–100 scale), mediation analysis via bootstrap (10,000 samples).

## Findings

1. **Essay 1**: Participants were more likely to spend from a used account than an unused account (Study 1: Mused = 60.63 vs. Munused = 44.80, d = .44).  
2. **Essay 1**: **Valuation of remaining resources was lower in used accounts (Mused = 61.45) than unused accounts (Munused = 70.70, d = .40)** — this devaluation mediated the spending effect.  
3. **Essay 1**: The effect increases as the proportion remaining decreases (Study 3: linear trend b = -7.99 for used accounts, p < .001; no trend for unused accounts, p = .69).  
4. **Essay 2**: People are more likely to start leisure activities near the end of a temporal category (e.g., 1:50 PM) than at the beginning (e.g., 2:00 PM) — the “end-of-period effect.”  
5. **Essay 3**: Experiential savings goals generated stronger saving intentions and longer saving streaks than material goals; perceived versatility of experiences (they cannot be owned in advance) was the key mechanism.

## Key Figures and Tables

- Figure 1 (Chapter 1): Spending likelihood — used gift card (60.63) > unused without reference (44.80) > unused with reference (49.49).  
- Figure 4 (Chapter 1): Spending likelihood decreases as account remaining increases only for used accounts (b = -7.99).  
- Figure 11 (Chapter 3): Saving intentions across three studies — experiential goals consistently outperform material goals.  
- Table 3 (Chapter 3): Regression results for mechanism — perceived versatility mediates the goal-type effect on saving motivation.  

## Key Equations

None.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| Used account | An account from which some resources have already been spent (e.g., $10 left from $100 gift card). |
| Unused account | An account from which no resources have been spent (e.g., $10 gift card received new). |
| Within-account comparison | Comparing current remaining amount to the original amount in the same account. |
| Psychological value | Perception of importance, worth, or usefulness of a resource. |
| Experiential savings goal | Saving for an activity or experience (e.g., vacation, concert). |
| Material savings goal | Saving for a tangible good (e.g., shoes, gear). |

## Critical Citations

- [Thaler, 1985; 1999] — Foundational mental accounting theory that resources are mentally divided into non-fungible accounts.  
- [Heath & Soll, 1996] — Mental budgeting and earmarking as self-control mechanisms.  
- [Hsee, 1996] — Relative vs. absolute judgments influence valuation and choice.  
- [Arkes et al., 1994] — Windfall gains are spent more readily than earned gains due to lower perceived value.  
- [Dhar & Simonson, 1999] — Goal completion (e.g., spending most of an account) leads to perceiving remaining resources as “extra” and less valuable.

## Relevance to Odin

**Topics:**

1.C — Financial Behavior of Filipino Young Professionals

2.C — User-Declared Financial Preferences

4.A — Landscape of Existing Personal Finance Systems

4.B — Limitations and Gaps in Existing Systems

7.A — Budgeting Strategies as Domain Knowledge

7.B — Budget Recommendation in Personal Finance Systems

11.B — Retention Mechanisms and Engagement Design

**Contribution to Odin:**

This dissertation provides behavioral evidence that the framing of an account as “used” or “unused” directly affects spending propensity — a finding that can inform Odin’s budget recommendation and anomaly detection modules. For example, if Odin displays a user’s remaining budget as a percentage of the original allocation (a “used account” frame), the user may be more likely to spend the remaining amount, potentially undermining saving goals. Conversely, framing a savings goal as an “unused” account (e.g., showing the full target amount without prior progress) could increase perceived value and reduce unnecessary spending. The third essay’s finding that experiential goals drive stronger saving motivation than material goals offers a direct design principle for Odin’s goal-setting feature: encouraging users to save for experiences (trips, events) rather than goods may improve retention and saving streaks. Perceived versatility of experiences (they cannot be owned until the goal is reached) is the mechanism — Odin can leverage this by asking users to visualize the experience during saving.

**Directly justifies:**

- “Remaining financial resources are valued less in a used account than an unused account, increasing spending likelihood by up to 16 percentage points (d = .44).”
- “The spending effect strengthens as the proportion remaining decreases (linear trend b = -7.99, p < .001), implying that showing original budget amounts alongside remaining amounts influences behavior.”
- “Experiential savings goals produce higher saving motivation and longer saving streaks than material goals, mediated by perceived versatility — the sense that experiences cannot be ‘consumed’ before the goal is reached.”
- “People are more likely to spend from an unspecified checking account (default framing) than a clearly unused account, indicating that typical app displays implicitly encourage spending.”
- “The used‑account effect holds for both endowed (gift cards) and earned (checking accounts) resources, and for both spending and donation decisions.”

**Limits of relevance:**

- All studies used U.S. participants; Filipino cultural norms around gift cards, credit card rewards, and savings goals may differ.
- Hypothetical scenarios dominate (except Study 5 incentive‑compatible); real‑world spending with actual money may attenuate effects.
- The temporal category effect (end‑of‑period) was tested only with leisure time, not with financial spending, limiting direct application to Odin.
- Savings goal studies did not measure actual longitudinal behavior beyond short streaks (max 2 weeks in Study 6).

## Limitations

- Sample predominantly U.S.‑based from MTurk and Prolific — may not generalize to Filipino young professionals with different financial infrastructures and cultural practices. [unacknowledged]
- Most studies use hypothetical vignettes rather than real spending with actual financial consequences (except Study 5, which used endowed points). [unacknowledged]
- The mechanism of devaluation is measured via self‑report; causal chain not fully isolated from alternative explanations (e.g., feeling of goal completion).
- No longitudinal field test of the used‑account effect on actual bank account or budget adherence over time.
- The experiential vs. material goals manipulation may confound goal duration or amount; pretests attempted to equate but differences remained (Table 4).

## Remember This

- 🔑 Used accounts boost spending by **16 percentage points** — people treat remaining $10 from $100 as less valuable than a fresh $10.  
- 💡 Experiential savings goals out‑motivate material goals — versatility (can’t own the experience early) drives longer saving streaks.  
- 📌 Showing original budget amounts alongside remaining balances (a “used” frame) encourages spending — Odin might reverse this to curb impulse buys.  
- 🧠 The effect works across gift cards, checking accounts, and reward points — robust for both endowed and earned money.
