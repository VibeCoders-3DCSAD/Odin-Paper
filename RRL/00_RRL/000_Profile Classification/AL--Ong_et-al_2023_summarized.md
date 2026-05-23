# Purchasing Intentions Analysis of Hybrid Cars Using Random Forest Classifier and Deep Learning

## Metadata

```yaml
---
paper_id: "10.3390/wevj14080227"
designation: algorithm-specific
title: "Purchasing Intentions Analysis of Hybrid Cars Using Random Forest Classifier and Deep Learning"
authors: "Ong, A. K. S.; Cordova, L. N. Z.; Longanilla, F. A. B.; Caprecho, N. L.; Javier, R. A. V.; Borres, R. D.; German, J. D."
year: 2023
venue: "World Electric Vehicle Journal"
odin_topics: ["5.C", "12.B"]
shorthand_tags: ["/classifier-candidates", "/classifier-eval-metrics", "/eval-ml-design"]
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

Random Forest (94% accuracy) and Deep Learning (96.6% accuracy) identified perceived environmental concern, attitude, and perceived behavioral control as the top predictors of Filipino drivers’ intention to purchase hybrid cars.

## Problem and Motivation

Hybrid cars are widely adopted in developed countries but remain underutilized in the Philippines despite environmental and economic benefits. Understanding consumer purchase intentions is critical for promoting sustainable transportation, yet existing studies rely on linear models (SEM) that may obscure nonlinear relationships. No prior study had applied machine learning algorithms to predict hybrid car purchase intention using an integrated sustainability and technology acceptance framework.

## Approach

- **Dataset:** 1,048 valid responses from Filipino drivers (86.1% male, 67.4% aged 23–36) via convenience and snowball sampling.
- **Framework:** Sustainability Theory of Planned Behavior (STPB) — integration of Pro-Environmental TPB, UTAUT2, and perceived economic concerns.
- **Latent variables (12):** Habit, Price Value, Hedonic Motivation, Performance Expectancy (PE), Effort Expectancy (EE), Facilitating Conditions (FC), Perceived Authority Support (PAS), Perceived Environmental Concern (PENC), Perceived Behavioral Control (PBC), Perceived Economic Concern (PECC), Subjective Norm (SN), Attitude (AT). Outcome: Behavioral Intention (BI).
- **Algorithms:** Decision Tree (DT), Random Forest Classifier (RFC), Deep Learning Neural Network (DLNN). Optimization via ANOVA and grid search over training/testing splits, tree depth, activation functions.
- **Best RFC configuration:** 90:10 train/test, depth 5, Gini criterion, best splitter → **94% accuracy**.
- **Best DLNN configuration:** 3 hidden layers (50,50,20 nodes), tanh activation, sigmoid output, Adam optimizer → **96.6% accuracy**.

## Findings

1. DLNN achieved **96.6% accuracy** — the highest among algorithms tested, validating its suitability for nonlinear behavioral models.
2. RFC achieved 94% accuracy with zero standard deviation at depth 5, producing a stable optimal tree.
3. Top 5 normalized importance scores (DLNN): PENC (100%), AT (96.3%), PBC (94.5%), SN (92.1%), PE (90.2%).
4. PENC was the root node in the optimal RFC tree, directly influencing AT, PBC, and PE to drive “very high” behavioral intention.
5. MLA results diverged from prior SEM results: PENC ranked 1st vs 5th, PECC ranked 10th vs 1st, and FC/EE/HB were significant in MLA but insignificant in SEM — demonstrating MLA’s advantage for mediated, nonlinear frameworks.

## Key Figures and Tables

- Figure 2: Optimum RFC tree (depth 5) → PENC as root; paths through AT and PBC lead to “very high” BI.
- Figure 3: DLNN architecture (3 hidden layers, 50/50/20 nodes) → final classification model with 96.6% accuracy.
- Figure 4: Taylor diagram → All MLAs within acceptable RMSE (≤20%) and correlation ≥0.90; DT excluded due to low correlation.
- Table 5: Normalized importance scores → PENC (100%), AT (96.3%), PBC (94.5%) top three.
- Table 6: MLA vs SEM rank comparison → Clear reordering due to mediation effects.

## Key Equations

$$tanh(x) = \frac{2}{1 + e^{-2x}} - 1$$
*Tanh activation — faster optimization and higher accuracy for hidden layers.*

$$sigmoid(x) = \frac{1}{1 + e^{-x}}$$
*Sigmoid activation — outputs probabilities in the final layer.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| STPB | Sustainability Theory of Planned Behavior — integrated TPB + UTAUT2 + economic domain. |
| RFC | Random Forest Classifier — ensemble of decision trees that picks the best tree per iteration. |
| DLNN | Deep Learning Neural Network — multi‑hidden‑layer neural net for nonlinear pattern learning. |
| PENC | Perceived Environmental Concern — belief that environmental degradation is severe and requires action. |
| AT | Attitude — positive or negative evaluation of adopting hybrid cars. |
| PBC | Perceived Behavioral Control — perceived ease or difficulty of using hybrid cars. |
| SN | Subjective Norm — perceived social pressure from trusted others. |
| PE | Performance Expectancy — belief that hybrid cars improve transportation efficiency. |
| PAS | Perceived Authority Support — perception of government resources and regulations enabling hybrid car use. |
| PECC | Perceived Economic Concern — belief about financial benefits, warranties, and long‑term savings. |
| FC | Facilitating Conditions — availability of resources and knowledge to operate hybrid cars. |
| EE | Effort Expectancy — perceived ease of learning and operating hybrid cars. |
| HB | Habit — automatic behavior from repeated hybrid car use. |

## Critical Citations

- [Ajzen, 1991] — Foundational Theory of Planned Behavior underpinning AT, SN, and PBC constructs.
- [Venkatesh et al., 2012] — UTAUT2 model providing HB, PV, HM, and FC as technology acceptance drivers.
- [German et al., 2022] — Pro‑environmental TPB (PEPB) integrated into STPB, contributing PENC and PAS.
- [Ong et al., 2023] — Prior SEM study on same STPB framework; MLA results directly compared to establish nonlinear advantages.
- [Chen et al., 2020] — Demonstration that RFC outperforms single classifiers like DT, cited to justify ensemble choice.

## Relevance to Odin

**Topics:**

5.C — Financial Behavioral Profile Classification Algorithm

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This paper provides empirical evidence that Random Forest and Deep Learning Neural Networks achieve high accuracy (94–96.6%) in classifying behavioral intention from multi‑latent variable frameworks — directly supporting Odin’s choice of ML algorithms for financial behavioral profiling. Although the target behavior is hybrid car purchase, the methodological approach (survey‑derived latent variables → classification of intention levels) maps cleanly to Odin’s need to classify users into financial profiles (e.g., stable vs. variable income, high vs. low spending adherence). The finding that DLNN outperforms RFC on nonlinear, mediated relationships (e.g., PENC → AT/PBC/SN → BI) justifies Odin’s use of deep learning for profiling when behavioral drivers have indirect effects. Additionally, the paper’s validation using a Taylor diagram establishes a replicable evaluation framework (RMSE ≤20%, correlation ≥90%) that Odin can adopt for module‑level performance assessment.

**Directly justifies:**

- “Deep Learning Neural Networks achieved 96.6% accuracy in classifying behavioral intention from 12 latent predictors, outperforming Random Forest (94%) in a nonlinear mediated framework.”
- “Perceived Environmental Concern (100% normalized importance) and Attitude (96.3%) were the strongest predictors — demonstrating that external beliefs and affective evaluations dominate intention classification.”
- “Machine learning algorithms (RFC/DLNN) identified FC, EE, and HB as significant predictors where SEM found them insignificant, confirming MLA’s advantage for models with mediating variables and nonlinear relationships.”
- “A Taylor diagram validation standard (RMSE ≤20%, correlation ≥0.90) provides a replicable acceptance threshold for comparing classification models in behavioral studies.”

**Limits of relevance:**

- Domain is hybrid car purchase intention, not personal spending behavior — but the classification methodology (intention level from survey items) is transferable to financial profiling.
- Survey data is cross‑sectional (self‑reported intention), whereas Odin requires dynamic profiling from transaction histories — cold‑start and temporal drift are not addressed.
- All predictors are attitudinal (PENC, AT, SN, etc.) — no behavioral transaction data; Odin’s profiling will rely on actual spending patterns, not stated intentions.
- Sample is 86% male and skewed toward employed adults (98.8%) — not fully representative of Filipino young professionals (ages 20–40, both genders).

## Limitations

- Convenience and snowball sampling — results may not generalize to all Filipino drivers; potential self‑selection bias.
- Only two ML algorithms (RFC, DLNN) were optimized; other candidates (Naïve Bayes, SVM, XGBoost) were not compared. [unacknowledged]
- No temporal validation — the model predicts intention at a single point; cannot assess how profiles change over time or after purchase.
- Self‑administered online survey excludes non‑internet users and may overrepresent younger, tech‑savvy demographics. [unacknowledged]
- Dependent variable is behavioral intention, not actual purchase behavior — intention‑behavior gap is not measured.

## Remember This

- 🔑 **96.6% DLNN accuracy** — deep learning bests random forest for nonlinear mediated behavioral models.
- 📌 PENC (100% importance) > AT > PBC > SN > PE — top five drivers of purchase intention.
- 💡 MLA found FC, EE, HB significant; SEM called them insignificant — ensemble methods catch mediated effects.
- ⚠️ Domain is hybrid cars, not spending — method transfers, but predictors (environmental concern) are not financial.
- 🔍 Taylor diagram thresholds: RMSE ≤20%, correlation ≥90% — Odin’s evaluation benchmark for classifiers.
