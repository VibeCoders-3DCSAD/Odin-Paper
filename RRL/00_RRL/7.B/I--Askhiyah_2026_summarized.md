# Digital Finance Usage and Its Impact on Consumer Economic Behavior Based on National Data

## Metadata

```yaml
---
paper_id: "10.59784/journaljoae.v1i1.37"
designation: international
title: "Digital Finance Usage and Its Impact on Consumer Economic Behavior Based on National Data"
authors: "Askhiyah, U. M."
year: 2026
venue: "Journal of Applied Econometric"
odin_topics: ["1.C", "5.A", "7.B", "8.A", "12.A"]
shorthand_tags: ["/income-type-behavior-diff", "/budgeting-prevalence", "/profile-dimensions", "/budget-rec-evidence", "/anomaly-behavioral-evidence", "/eval-pfms-applied"]
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

Digital finance adoption increases household consumption by **8.7%** and improves financial literacy by 1.4 points, but reduces savings balances by 5.8% and raises debt-to-income ratios, especially among young lower-middle-income households.

## Problem and Motivation

The comprehensive impact of digital finance on consumer economic behavior remains inadequately understood, with mixed findings on whether it promotes prudent behavior or encourages overconsumption. This ambiguity creates challenges for policy formulation and raises concerns about potential negative consequences for financially vulnerable populations. Prior studies focused on isolated digital finance modalities or single outcomes, lacking comprehensive frameworks that simultaneously consider multiple behavioral dimensions and heterogeneous effects.

## Approach

- Data: 45,678 households from a nationally representative survey; 62.3% reported digital finance use in the past 12 months.
- Propensity score matching (PSM) with kernel matching constructs comparable treatment/control groups, mitigating selection bias from observable characteristics.
- Instrumental variable (IV) estimation uses regional digital infrastructure density as an instrument (first-stage F-statistic = 48.7).
- Panel fixed effects (FE) for a subsample of 8,234 households with up to 24 months of longitudinal observations.
- Heterogeneity analysis examines differential effects across age, income quintiles, urban/rural residence, education, and financial literacy.

## Findings

1. Digital finance users exhibit **8.7% higher monthly consumption expenditure** than matched non-users (ATT = 742 thousand Rupiah, p < 0.001), concentrated in discretionary goods (eating out +14.3%, electronics +18.5%).
2. Despite a 12.4 percentage point higher probability of having a formal savings account, users have **5.8% lower savings balances** (p = 0.018) and save 2.4 percentage points less of their income.
3. Financial literacy scores rise by 1.4 points (0‑10 scale) post-adoption, with 19.4 percentage point higher monthly budgeting and 35.6 point higher spending tracking.
4. Debt-to-income ratio is 6.4 percentage points higher for users (34.7% vs 28.3%), and late payment rates in the past year are 6.3 points higher (14.7% vs 8.4%).

- Young lower-middle-income households face the most severe trade-offs: highest consumption increases but also highest debt service difficulties.
- Urban users see a 10.2% consumption increase vs 4.7% for rural users, reflecting ecosystem differences.

## Key Figures and Tables

- Table 2: Impact on household consumption expenditure → total consumption +8.7% (PSM), discretionary goods +14–18%.
- Figure 2: Heterogeneous consumption effects by subgroup → strongest for young (+13.6%) and middle-income (+10–12%) households.
- Table 4: Digital credit utilization and debt profile → debt-to-income 34.7% vs 28.3%, late payments 14.7% vs 8.4%.
- Table 5: Financial literacy and wellbeing → literacy +1.4 points, budgeting +19.4pp, financial wellbeing index +8.5 points.
- Figure 3: Multidimensional comparison of savings behavior → higher access but lower balances, better management practices.

## Key Equations

None.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| PSM | Propensity score matching — a statistical method to compare similar treated and untreated units. |
| IV | Instrumental variable — a technique to isolate causal effects when treatment is not randomly assigned. |
| ATT | Average treatment effect on the treated — the causal impact for those who actually received the treatment. |
| FE | Fixed effects — a panel data method that controls for time-invariant unobserved differences between units. |
| Digital finance usage intensity index | A multidimensional score (0–100) capturing both breadth and depth of digital finance engagement. |
| Debt-to-income ratio | Total monthly debt payments divided by monthly income, expressed as a percentage. |
| Financial literacy score | A 0–10 measure of knowledge about basic financial concepts and products. |

## Critical Citations

- [Li et al., 2020] — Foundational benchmark: mobile payment adoption increased household consumption by 7–9%, directly comparable to this study's 8.7% estimate.
- [Batista & Vicente, 2020] — Prior evidence that mobile money increased savings accumulation in Sub-Saharan Africa, contrasting with this study's negative savings effect.
- [Danisman & Tarazi, 2020] — Documented risks of rapid digital credit expansion, supporting this study's debt overhang findings.
- [See-To & Ngai, 2019] — Experimental evidence that digital payments reduce the psychological pain of paying, explaining the consumption increase mechanism.

## Relevance to Odin

**Topics:**

1.C — Financial Behavior of Filipino Young Professionals

5.A — Financial Behavioral Profiles in Personal Finance

7.B — Budget Recommendation in Personal Finance Systems

8.A — Anomaly Detection in Personal Finance Systems

12.A — Evaluation Frameworks for Personal Finance Systems

**Contribution to Odin:**

This paper provides large‑scale empirical evidence that digital finance adoption fundamentally alters consumption, savings, and debt behavior — patterns that directly inform Odin's budget recommendation and anomaly detection modules. The finding that young lower‑middle-income households are most vulnerable to over‑consumption and payment difficulties justifies Odin's emphasis on behavioral profiling and targeted budget guardrails. The methodological use of PSM, IV, and panel FE demonstrates a rigorous evaluation framework that Odin can adopt for module‑level performance assessment, even though the study context is Indonesian rather than Filipino.

**Directly justifies:**

- "Digital finance adoption increases household consumption by 8.7% (p < 0.001), concentrated in discretionary categories like eating out (+14.3%) and electronics (+18.5%)."
- "Digital finance users have 5.8% lower savings balances despite a 12.4 percentage point higher probability of formal account ownership — a trade‑off between access and accumulation."
- "Young lower‑middle‑income households experience the largest debt‑to‑income ratio increase (+6.4 percentage points) and the highest late payment rates (+6.3 percentage points), identifying them as a vulnerable subgroup."
- "Post‑adoption financial literacy improves by 1.4 points (0–10 scale) within 18 months, and financial planning behaviors increase dramatically: monthly budgeting (+19.4pp), spending tracking (+35.6pp), goal‑based saving (+28.7pp)."
- "Propensity score matching with sensitivity analysis (Rosenbaum bounds) and instrumental variable estimation (F-statistic 48.7) provide a template for causal identification in observational financial behavior studies."

**Limits of relevance:**

- The study uses Indonesian national survey data; income levels, spending patterns, and digital finance penetration may differ from the Filipino context.
- Digital finance is defined broadly (mobile banking, e‑wallets, digital credit) rather than focused on manual‑input PFMS like Odin.
- Consumption and savings effects are measured at the household level, not isolated to individual budgeting behavior within a PFMS.
- The study relies on self‑reported survey data, which may contain recall bias and social desirability bias.

## Limitations

- Observational data with self‑reported measures may contain bias despite PSM and IV methods; unobserved confounders cannot be fully ruled out.
- Short time horizon (maximum 24 months post‑adoption) limits understanding of long‑term wealth and debt sustainability effects. [unacknowledged]
- No measurement of individual psychological factors such as self‑control, risk preferences, or time discounting, which could moderate digital finance impacts.
- Spillover effects within households or social networks were not examined, though peer effects likely influence adoption and behavior.
- The study does not evaluate how digital finance impacts differ when users enter with existing debt or low financial literacy — both common in the target population.

## Remember This

- 🔑 Consumption **+8.7%**, savings **−5.8%** — digital finance creates a spending boost at the direct cost of savings.
- 📌 Young lower‑middle‑income households: debt‑to‑income +6.4pp, late payments +6.3pp — most vulnerable to over‑leveraging.
- 💡 Financial literacy **+1.4 points** post‑adoption — digital platforms teach users through embedded tools and transaction feedback.
- 🔍 PSM + IV + panel FE — a three‑method triangulation design for causal claims; use for Odin’s module evaluation.
- ⚠️ Discretionary spending drives the consumption increase (eating out +14%, electronics +18%) — budget recommendations must guard against this channel.
