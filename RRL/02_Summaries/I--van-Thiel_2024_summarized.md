# On the human-centered AI transformation of banking: Exploring the impact of behavioral finance & AI on banking transformation

## Metadata

```yaml
---
paper_id: "10.26116/tsb.4096899"
designation: algorithm-specific
title: "On the human-centered AI transformation of banking: Exploring the impact of behavioral finance & AI on banking transformation"
authors: "van Thiel, D."
year: 2025
venue: "Tilburg University"
odin_topics: ["A.2", "D.1", "F.1", "H.1", "I.1"]
shorthand_tags: ["/pfms-typology", "/pfms-features", "/forecasting-methods", "/profiling-role", "/fil-behavioral-patterns", "/data-sensitivity", "/user-trust", "/retention-mechanisms"]
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

Integrating psychometric and behavioral finance principles with AI (random forests, neural nets) improves digital advice adoption and inclusive credit scoring, achieving 30% higher approval and 23% lower default rates during market volatility.

## Problem and Motivation

Traditional financial advice is costly and inaccessible, while conventional credit scoring excludes vulnerable consumers and small businesses due to lack of historical data. Digitalization and AI offer scalability but lack human-centered personalization and inclusive risk assessment. Prior research failed to integrate psychometric determinants and AI into a unified framework for responsible Banking 5.0.

## Approach

- Cross-country surveys (UK, NL, US, CZ) totaling 2,332 (advice) and 897 (credit) respondents, plus 133,152 lender customers.
- Structural equation modeling, factor analysis, and Ward clustering to develop the Digital Customer Experience (DCX) and Digital Psychometric Segmentation (DPS) models.
- Logistic regression to build psychometric credit scoring models (PSM) for low-income consumers and small businesses.
- Random forest and neural network models compared against traditional logistic regression for credit default prediction.

## Findings

1. **DCX model:** Experiential attributes (honesty, reliability, transparency) matter more than price; advising quality (β=0.58) is the strongest driver of customer satisfaction.
2. **DPS model:** Three psychometric factors — convenience (eigenvalue 1.89), financial illiteracy (1.0), and rigidity (0.51) — segment digital advice users.
3. **PSM (consumer):** Achieved **70.7% accuracy** and 0.56 Gini, correctly predicting 72.2% of good payers and 67.5% of arrears.
4. **PSM (small business):** During COVID-19 state of emergency, PSM yielded **30% higher approval rate** and **23% lower default rate** than traditional models.
5. **AI vs. logistic:** Random forests improved AUROC by **18.8–21.3%** across three lender experiments (e.g., 0.87 → 0.95).

- Financial skills (−0.57 correlation) and debt attitude (+0.22) are the strongest psychometric predictors of late payment.

## Key Figures and Tables

- Figure 2 (Ch2): DCX model regression weights — advising quality (0.58) most important → process/outcome attributes drive satisfaction.
- Table 4 (Ch4): Survey questions correlation with arrears — financial skills (−0.57) and debt attitude (0.22) strongest.
- Table 10 (Ch6): Acceptance rates — PSM increases approval from 28.6% to 37.3% for small businesses.
- Figure 2 (Ch5): ROC curve — AI model achieves 0.95 AUROC vs. 0.87 for logistic.
- Table 7 (Ch6): PSM metrics — precision 0.94 in stress period, AUC 0.61.

## Key Equations

$$\text{Log}(arrears) = -0.79 - 0.76(\text{Financial Acumen}) + 0.72(\text{Vulnerable Optimism}) + 0.50(\text{Impulse Control}) - 0.28(\text{Social Desirability}) - 0.01(\text{Age})$$
*Logistic regression for psychometric credit scoring (Chapter 4).*

$$\text{Credit risk} = \text{Exposure at default} \times \text{Probability of Default} \times (1 - \text{Recovery Rate})$$
*Standard credit risk decomposition used in Chapter 5.*

$$AUROC = \int_0^1 \text{Sensitivity}(FPR) \, d(FPR)$$
*Area Under ROC curve metric for model discrimination power.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| AI | Artificial intelligence — machines learning from data to perform human-like tasks. |
| AUC / AUROC | Area under the ROC curve — measures how well a model distinguishes good vs. bad payers (0.5=random, 1=perfect). |
| DCX | Digital Customer Experience — cross-cultural model of satisfaction drivers for digital advice. |
| DPS | Digital Psychometric Segmentation — model segmenting users by convenience, financial literacy, and rigidity. |
| PSM | Psychometric scoring model — credit score based on personality traits (financial skills, debt attitudes, etc.). |
| Random forest | Ensemble of decision trees that reduces overfitting; outperforms logistic regression in credit risk. |
| Financial literacy | Knowledge, skills, and confidence to make effective financial decisions (OECD definition). |
| Social desirability bias | Tendency to present oneself as socially acceptable, distorting self-reported financial behavior. |

## Critical Citations

- [Kahneman & Tversky, 1979] — Foundational behavioral finance theory on heuristics and biases.
- [Lusardi & Mitchell, 2011] — Established financial literacy as a predictor of financial well-being.
- [Klinger et al., 2013] — First to apply psychometrics to credit scoring for small businesses (AUC 0.7).
- [Verhoef et al., 2009] — Defined customer experience as holistic, subjective response to brand interactions.

## Relevance to Odin

**Topics:**

A.2 — Existing Personal Finance and Budget Management Systems

D.1 — Predictive Modeling in Personal Finance Systems

F.1 — User Behavioral Profiling in Filipino Personal Finance Contexts

H.1 — Data Privacy, Security, and User Trust in Personal Finance Systems

I.1 — User Retention and Engagement in Personal Finance Systems

**Contribution to Odin:**

This dissertation directly informs Odin’s **predictive modeling module** (D.1) by demonstrating that random forests and neural networks achieve 18–21% higher AUROC than logistic regression for default prediction (Chapter 5), justifying Odin’s algorithm selection for spending forecasting even though the domain is credit risk. The **user profile classification module** (F.1) benefits from the psychometric segmentation model (Chapter 3), which identifies three stable factors (convenience, financial literacy, rigidity) that predict digital advice adoption — applicable to Odin’s four behavioral profiles. The **customer experience findings** (Chapter 2) show that experiential attributes (honesty, reliability, co-creation) drive satisfaction more than price, guiding Odin’s mobile-first design and retention strategies (I.1). Although the study uses Western populations, the psychometric credit scoring model’s ability to predict payment behavior without traditional credit history (Chapter 4, 6) provides a validated method for Odin’s cold-start profiling of new Filipino users.

**Directly justifies:**

- "Random forest models improve AUROC by 18.8–21.3% over logistic regression for individual default prediction across mortgages and credit cards (p < 0.001)."
- "Three psychometric factors — convenience (eigenvalue 1.89), financial illiteracy (1.0), and rigidity (0.51) — segment financial advice users and predict adoption of robo-advisors."
- "Psychometric credit scoring correctly predicts 72.2% of good payers and 67.5% of arrears in low-income consumers (Gini 0.56), enabling cold-start credit assessment."
- "During the COVID-19 state of emergency, psychometric scoring increased approval rates by 30% and lowered default rates by 23% compared to traditional models."
- "Financial skills (−0.57 correlation) and positive debt attitude (+0.22) are the strongest psychometric predictors of payment behavior, more predictive than age or income."

**Limits of relevance:**

- All studies conducted in Western markets (UK, NL, US, CZ); Filipino spending behavior and cultural obligations not directly measured.
- Predictive models focus on credit default (mortgages, credit cards), not spending forecasting — though methodology transfers.
- The AI models tested are random forests and neural networks, not LSTM (Odin’s current forecasting algorithm).
- Some data sources (e.g., credit bureau data in UK experiment) are unavailable in Philippine context.
- Psychometric questionnaires require user self-reporting, which introduces social desirability bias and may not scale as seamlessly as passive behavioral data.

## Limitations

- Geographic scope limited to Western high-income countries; generalizability to Filipino young professionals is untested. [unacknowledged]
- Data for psychometric models relies on self-reported Likert scales, which may be biased by social desirability.
- The AI credit risk experiments used historical data (2016–2017) pre-COVID; post-pandemic behavior may differ.
- Neural network black-box interpretability limits regulatory acceptance — study preferred random forests for explainability.
- Small sample size for thin-file credit card experiment (N=6,994) and micro-enterprise stress test (N=169 default events).

## Remember This

- 🔑 **+21% AUROC** — random forest beats logistic regression for default prediction (0.87→0.95 in mortgages).
- 💡 **30% higher approval, 23% lower default** — psychometric scoring outperforms traditional models during COVID stress.
- 📌 Financial skills (−0.57) and debt attitude (+0.22) — top two psychometric predictors of payment behavior.
- ⚠️ Western-only samples — apply to Filipino context with caution; cultural spending norms not studied.
- 🧠 Experiential > price — honesty, reliability, and co-creation drive digital advice satisfaction, not just low cost.
