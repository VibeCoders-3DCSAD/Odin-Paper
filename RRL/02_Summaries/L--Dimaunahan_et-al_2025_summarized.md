# Financial literacy and sustainable planning assessment among Filipino millennials

## Metadata

```yaml
---
paper_id: "10.1016/j.actpsy.2025.105334"
designation: local
title: "Financial literacy and sustainable planning assessment among Filipino millennials"
authors: "Dimaunahan, D. S. F.; Santiago, A. F. B.; Eusebio, M. C. C.; Loteriña, S. M. M.; Ong, A. K. S.; Chavez, J. X. S."
year: 2025
venue: "Acta Psychologica"
odin_topics: ["A.1", "C.1", "F.1", "F.2"]
shorthand_tags: ["/budgeting-prevalence", "/fil-behavioral-patterns", "/profile-dimensions", "/western-taxonomy-gap", "/classification-vs-clustering"]
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

Low financial literacy among Filipino millennials does not directly drive financial planning; monthly income, expenses, and occupation matter more, with goal acceptance being the strongest predictor of planning behavior.

## Problem and Motivation

Financial literacy among Filipinos is extremely low — only 25% of adults demonstrate basic financial knowledge — yet no recent publicly available study has examined how literacy affects financial planning specifically for Filipino millennials, who now dominate the working-age population. Poor financial decisions and vulnerability to scams are rising concerns in the Philippines, making it urgent to understand what actually drives financial planning behavior in this demographic. Prior research had not applied Goal Setting Theory (GST) to assess financial planning in the Philippine millennial context, leaving a gap in both theory application and local evidence.

## Approach

- Sample: 400 Filipino millennials (ages 28–43) in Makati City; purposive non-probability sampling; Yamane formula used for size calculation.
- Financial literacy measured using "The Big Three" questions (interest compounding, inflation, risk diversification) from Lusardi and Mitchell (2011).
- Financial planning measured via four GST moderators: goal commitment, goal specificity, goal acceptance, and goal difficulty.
- Demographic factors tested: monthly income, occupation, and monthly expenses as lower-order constructs affecting financial planning.
- Analysis method: Partial least squares structural equation modeling (PLS-SEM) with bootstrapping; 5-point Likert scale items; Cronbach's alpha 0.90 after pilot testing.

## Findings

1. **Only 2%** of Filipino adults correctly answer six BSP financial literacy questions; this study's sample scored 0.545 (interest), 0.388 (inflation), and 0.338 (risk diversification) — all well below passing.
2. Financial literacy showed **no significant direct effect** on financial planning (β = 0.077, p = 0.153) — **the most striking negative finding**.
3. Monthly expenses had the strongest demographic effect on planning (β = 0.205, p = 0.001), followed by monthly income (β = 0.180, p = 0.003) and occupation (β = 0.164, p = 0.004).
4. Goal acceptance was the strongest predictor among GST moderators (β = 0.924, p < 0.001), then goal commitment (β = 0.809), goal specificity (β = 0.597), and goal difficulty (β = 0.212).

- Filipino millennials plan finances based on personal needs and goals, not financial knowledge; they do not typically analyze their situation or consult experts before decisions.

## Key Figures and Tables

- Figure 2: Initial SEM with 9 latent variables and 36 indicators → Financial literacy has weakest path coefficient (0.077) and is removed.
- Figure 3: Final SEM after removing low-factor-loading items → Monthly expenses (0.205) and goal acceptance (0.924) dominate.
- Table 1: Demographic profile of 400 respondents → 71.3% full-time employed, 67.5% bachelor's degree, most common income ₱10k–₱30k (38.5%).
- Table 2: Statistical analysis of indicators → Mean correct answers on Big Three: 0.545 (interest), 0.388 (inflation), 0.338 (risk diversification).
- Table 7: Summarized results with beta coefficients and p-values → H1 not supported; H2, H3, H4 all accepted.

## Key Equations

None. The paper uses SEM path coefficients, not mathematical equations.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| GST | Goal Setting Theory [think: goals drive behavior through commitment, specificity, acceptance, and difficulty] |
| SEM | Structural equation modeling — a statistical method that tests multiple relationships at once while accounting for measurement error |
| PLS-SEM | Partial least squares SEM — a variant that works well with smaller samples and prediction-focused research |
| The Big Three | Three standardized financial literacy questions covering interest compounding, inflation, and risk diversification |
| HTMT | Heterotrait-monotrait ratio — a test proving that different concepts in a model are truly distinct |
| AVE | Average variance extracted — a measure of how much of a variable's variation comes from its indicators |
| BSP | Bangko Sentral ng Pilipinas — Philippines' central bank |

## Critical Citations

- [Lusardi & Mitchell, 2011] — Source of "The Big Three" financial literacy measurement used throughout this study.
- [Locke & Latham, 1990; 2019] — Foundational Goal Setting Theory papers that provide the four moderators (commitment, specificity, acceptance, difficulty).
- [Grohmann, 2018] — Establishes the pattern of low financial literacy in emerging Asian middle classes, directly comparable to Philippines.
- [Mohta & Shunmugasundaram, 2022] — Evidence that millennials globally fall into "low-advanced financial literacy" category.

## Relevance to Odin

**Topics:**

A.1 — Spending and Budgeting Behavior of Filipino Young Professionals

C.1 — Budgeting Strategies and Budget Recommendation

F.1 — User Behavioral Profiling in Filipino Personal Finance Contexts

F.2 — Profile Classification Algorithm

**Contribution to Odin:**

This paper directly supports Odin's user profile classification module by demonstrating that income, occupation, and expenses (not financial literacy) are the strongest predictors of financial planning behavior among Filipino millennials — justifying a behavior-driven profiling approach rather than a knowledge-based one. The finding that goal acceptance (β = 0.924) dominates planning behavior suggests Odin's profile dimensions should include goal-related constructs (commitment, specificity, acceptance, difficulty) as classification features. Although financial literacy proved insignificant, the paper's demographic predictors map precisely to Odin's planned profile variables (income type, occupation, spending patterns), providing local Philippine evidence for feature selection in the classifier. The study also confirms that Filipino millennials actively engage in financial planning despite low literacy, which supports Odin's assumption that users will manually input transaction data without requiring financial expertise.

**Directly justifies:**

- "Monthly expenses (β = 0.205) and monthly income (β = 0.180) are the strongest demographic predictors of financial planning behavior among Filipino millennials, outweighing the effect of financial literacy."
- "Goal acceptance (β = 0.924) and goal commitment (β = 0.809) show very strong direct effects on financial planning, indicating these psychological constructs should inform user profile dimensions."
- "Only 2% of Filipino adults correctly answer six financial literacy questions, and financial literacy shows no significant direct effect on financial planning (p = 0.153) — behavior is driven by needs and goals, not knowledge."
- "Filipino millennials do not typically analyze their financial situation or consult experts before making financial decisions, supporting manual-input system design over automated advisory features."

**Limits of relevance:**

- Study confined to Makati City only — not representative of all Filipino young professionals, particularly those in rural or lower-income areas.
- Sample limited to millennials (ages 28–43 at time of study); findings may not apply to Gen Z or Gen X users Odin might target.
- Used only "The Big Three" literacy measure; other literacy dimensions (e.g., digital financial literacy) were not tested.
- Study is correlational, not experimental or predictive — supports feature justification but not algorithm benchmarking.
- Data self-reported via survey, not observed financial behavior, which may introduce social desirability bias.

## Limitations

- Geographic limitation to Makati City only; results cannot be generalized to all Filipino young professionals nationwide.
- Millennial-only sample; financial planning drivers may differ for Gen Z or older adults.
- Cross-sectional design cannot establish causality between demographics and planning behavior. [unacknowledged]
- Self-reported survey data may overstate actual financial planning behavior due to social desirability bias. [unacknowledged]
- Used only "The Big Three" financial literacy measure; other accepted measures might yield different relationships with planning.

## Remember This

- 📌 **No link between literacy and planning** — financial knowledge (β=0.077, p=0.153) does not drive Filipino millennials' financial behavior.
- 🔑 **Monthly expenses matter most** (β=0.205) — spending burden predicts planning more than income or job type.
- 💡 **Goal acceptance drives planning** (β=0.924) — users who embrace financial goals are nearly 5x more committed than those who find goals difficult.
- ⚠️ **Only 2% of Filipinos pass basic literacy** — design for behavior, not financial expertise.
- 🧠 **Occupation still matters** (β=0.164) — job type shapes planning through benefits and income stability, not just salary.
