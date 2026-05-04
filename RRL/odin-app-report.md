# Odin Report

This report answers the 10 questions using only materials already present in this repository. Where the basis is a project document rather than a published paper, that is stated directly.

## 1. What is Odin and its purpose?

Odin is proposed as a **personal budget management system for Filipino young professionals in Metro Manila**. Its purpose is not just to record expenses, but to provide **predictive, behavior-aware financial guidance** through spending forecasting, anomaly detection, behavioral profiling, and budget recommendations. The proposal frames Odin as a response to the lack of locally grounded budgeting tools that account for Filipino income structures, obligation patterns, and culturally specific expenses. It is also designed to be available on both **mobile and web**, with mobile as the primary access point for the target users.

**Sources in repo:**
- [Documents/Research-Proposal.md](../Documents/Research-Proposal.md)
- [Documents/Panel-Comments-and-Suggestions.md](../Documents/Panel-Comments-and-Suggestions.md)

## 2. What are the modules that these researchers are trying to aim for?

Based on the proposal, panel notes, and data handoff documents, Odin is aiming for these core modules:

1. **Financial behavioral profiling**
2. **Spending forecasting**
3. **Anomaly or overage detection**
4. **Budget recommendation**
5. **Savings goal tracking and projections**
6. **Debt management guidance** using Snowball and Avalanche
7. **Dashboard analytics and reporting**

The `Data/` handoff also makes the internal forecasting structure explicit by defining the second-node budget architecture as **Essentials, Obligatory, Discretionary, and Financial Allocation**, which the forecasting and recommendation modules will use.

**Sources in repo:**
- [Documents/Research-Proposal.md](../Documents/Research-Proposal.md)
- [Documents/Panel-Comments-and-Suggestions.md](../Documents/Panel-Comments-and-Suggestions.md)
- [Data/data-synthesis-handoff.md](../Data/data-synthesis-handoff.md)

## 3. What are the justifications for those modules?

The modules are justified by a mix of local behavioral evidence and system design needs:

- **Behavioral profiling** is justified because the study argues that users differ meaningfully by **income stability** and **obligation weight**, and that budgets should adapt to those differences rather than treat all users the same.
- **Spending forecasting** is justified because Odin is intended to be an **active planning tool**, not just a passive tracker. The panel notes specifically contrast Odin with apps that only show static statistics.
- **Anomaly detection** is justified because users need alerts when their spending deviates from normal patterns or threatens higher-priority goals.
- **Budget recommendation** is justified because the target users struggle with insufficient income, poor tracking, and discipline; the system is meant to convert tracked behavior into actionable budget guidance.
- **Savings and debt modules** are justified because the proposal explicitly connects the app to personal financial management competencies such as saving and debt management.

At the local evidence level, the proposal cites pilot findings that only **6.7%** of respondents used a dedicated budgeting app, while major problems included not having enough income, difficulty tracking spending, and lack of discipline. BSP and CFS-based materials in the repo also support the need for tools that handle real Filipino spending and obligations.

**Sources in repo:**
- [Documents/Research-Proposal.md](../Documents/Research-Proposal.md)
- [Documents/Panel-Comments-and-Suggestions.md](../Documents/Panel-Comments-and-Suggestions.md)
- [RRL/02_Related Literature/Bangko-Sentral-ng-Pilipinas.md](./02_Related%20Literature/Bangko-Sentral-ng-Pilipinas.md)
- [RRL/02_Related Literature/Cacnio_Romarate.md](./02_Related%20Literature/Cacnio_Romarate.md)
- [RRL/02_Related Literature/Dimaunahan_et-al.md](./02_Related%20Literature/Dimaunahan_et-al.md)

## 4. What are Financial Behavioral Profiling, the 4 profiles mentioned, and the paper they are based on?

In Odin, **financial behavioral profiling** means assigning a user to a budgeting profile so the system can personalize forecasts and budget allocations.

The four profiles in the repo are:

1. **Stable / Obligated**
2. **Stable / Flexible**
3. **Variable / Obligated**
4. **Variable / Flexible**

The two dimensions behind them are consistent across the project materials:

- **Stable vs Variable**: whether spending or income behavior is regular or volatile
- **Obligated vs Flexible**: whether fixed obligations dominate the budget or discretionary spending has more room

Important clarification: the repository does **not** show one single published paper that originally coined these exact four Odin profiles. What the repo supports is that the four-profile model is a **project-defined framework** built from:

- consultation with a subject matter expert, Dr. Pamela A. Go
- BSP/CFS/FIES-backed dimensions such as income structure, expenditure composition, remittances, debt, and savings behavior
- the project’s own data handoff documents

So the most defensible answer from the repository is: **the exact four-profile schema is Odin’s own operational model**, but its dimensions are grounded in local sources like the BSP Consumer Finance Survey and Cacnio & Romarate’s work on Filipino financial behavior.

An important limitation should also be stated here: the repository supports the **conceptual dimensions** behind the four profiles, but it does **not yet provide empirical or literature-backed proof for the exact decision thresholds** used to separate those dimensions in implementation. In practice, the current profile structure is academically strongest when described as a **locally grounded but still provisional operational model**. The BSP/CFS/FIES-backed evidence supports using dimensions such as income structure, expenditure composition, remittances, debt, and savings behavior, but the study still needs statistical justification for the exact numeric cutoffs currently used to divide users into Stable vs Variable and Obligated vs Flexible groups.

**Sources in repo:**
- [Documents/Panel-Comments-and-Suggestions.md](../Documents/Panel-Comments-and-Suggestions.md)
- [Data/data-synthesis-handoff.md](../Data/data-synthesis-handoff.md)
- [RRL/02_Related Literature/Bangko-Sentral-ng-Pilipinas.md](./02_Related%20Literature/Bangko-Sentral-ng-Pilipinas.md)
- [RRL/02_Related Literature/Cacnio_Romarate.md](./02_Related%20Literature/Cacnio_Romarate.md)
- [RRL/01_Reviews/Bangko-Sentral-ng-Pilipinas_summarized.md](./01_Reviews/Bangko-Sentral-ng-Pilipinas_summarized.md)

## 5. What are the algorithms that they will be using?

The repo shows two algorithm framings:

### Original framing
- **LSTM** for spending forecasting
- **Isolation Forest** for anomaly detection
- **Decision Tree** or **Random Forest** for profile classification
- **Constraint-based** or **rule-based** engine for budget recommendation

### Revised framing in the comparison document
- **LSTM** as the **only machine learning model**
- **Rule-based classification** for behavioral profiles
- **Rule-based overage detection**
- **Rule-based or constraint-based** budget recommendation

That means the repository currently contains a design tension:

- the **proposal and panel comments** still present **Isolation Forest** as part of Odin
- the **algorithm comparison** document recommends simplifying the final thesis framing so that only **LSTM** remains as the ML model

If you want the report to reflect the current internal design thinking of the repo, the safest wording is that Odin is centered on **LSTM for forecasting**, while profile assignment, overage detection, and budgeting are increasingly being pushed toward **deterministic logic** for thesis defensibility.

**Sources in repo:**
- [Documents/Research-Proposal.md](../Documents/Research-Proposal.md)
- [Documents/Panel-Comments-and-Suggestions.md](../Documents/Panel-Comments-and-Suggestions.md)
- [algorithm-approach-comparison.md](../algorithm-approach-comparison.md)

## 6. How about statistics and data?

The `Data/` folder gives the clearest answer here. The planned data strategy is:

- scope the study to **Metro Manila / NCR**
- use **FIES NCR aggregate tables** as the statistical basis
- derive per-category means, savings rate, obligated ratio, and Engel coefficient from NCR tables
- request **PSA microdata** if possible for stronger distributional statistics like standard deviation and median
- generate a large **synthetic dataset** for model training and testing

The handoff specifies:

- **10,000 users** for the main dataset
- **1,000 users** for fine-tune testing
- **1,000 users** for fallback testing
- **17,520,000 total records**

The repo also states that the forecast data is organized around four top categories:

- **Essentials**
- **Obligatory**
- **Discretionary**
- **Financial Allocation**

This statistical design is grounded in NCR-specific FIES figures rather than national averages, which the documents repeatedly say should not be substituted.

**Sources in repo:**
- [Data/data-synthesis-handoff.md](../Data/data-synthesis-handoff.md)
- [Data/synthetic-data-parameters-handoff.md](../Data/synthetic-data-parameters-handoff.md)
- [RRL/02_Related Literature/Bangko-Sentral-ng-Pilipinas.md](./02_Related%20Literature/Bangko-Sentral-ng-Pilipinas.md)

## 7. How will they classify people on what behavioral profile they belong?

The repo’s clearest operational classification logic is in the `Data/` handoff. It uses two computed indicators:

1. **Coefficient of Variation (CV)** for consistency
2. **Obligated Ratio** for spending composition

The current rule logic is:

- **Stable** if `CV < 0.2`
- **Variable** if `CV >= 0.2`
- **Obligated** if `Obligated Ratio > 0.5`
- **Flexible** if `Obligated Ratio <= 0.5`

The formula explicitly stated in the repo is:

- `CV = σ / μ`
- `Obligated Ratio = (Essentials + Obligatory) / Total Spend`

There is also evidence from the panel comments that the earlier idea was to classify from onboarding questions alone, but the panel pushed back and required a more defensible clustering or classification basis. The `algorithm-approach-comparison.md` document then shows two possible paths: a real classifier such as Decision Tree/Random Forest, or the current simplified rule-based classification.

However, an important academic limitation must be stated clearly: while the **dimensions themselves** are supported by BSP/CFS/FIES-style variables, the exact thresholds `CV = 0.2` and `Obligated Ratio = 0.5` are **not yet empirically or literature-backed in the repository as fixed validated cutoffs**. At present, these values function as **project-defined operational thresholds** for system design. The repository materials support the use of:

- income and expenditure structure,
- spending composition,
- remittances,
- debt,
- and savings behavior

as profiling dimensions, but they do not yet provide a published study proving that `0.2` is the correct boundary for Stable vs Variable or that `0.5` is the correct boundary for Obligated vs Flexible.

This means the current logic should be described as **provisional**. A stronger academic version of the study would still need **statistical backing** for why those thresholds were chosen. That backing could come from NCR-specific calibration using FIES/CFS distributions, percentile analysis, clustering, or another explicit validation method. In other words, the repository currently justifies the **choice of dimensions**, but not yet the **final numeric cutoffs**.

**Sources in repo:**
- [Data/data-synthesis-handoff.md](../Data/data-synthesis-handoff.md)
- [algorithm-approach-comparison.md](../algorithm-approach-comparison.md)
- [Documents/Panel-Comments-and-Suggestions.md](../Documents/Panel-Comments-and-Suggestions.md)

## 8. Does behavioral profile change from time to time?

Yes. The repository explicitly says that behavioral profile **can change over time**.

There are two versions of that idea in the repo:

- the **panel comments** say profile changes must be tracked progressively and the mechanism must be made clear
- the **data handoff** says reclassification should trigger when a user’s spending pattern deviates from their assigned profile for **2 to 3 consecutive months**
- the **algorithm comparison** says reclassification happens when changes in income variability or obligation ratio become significant and persistent

So the repo’s position is not only that profile change is possible, but that it is expected and should be treated as part of the adaptive logic of the app.

**Sources in repo:**
- [Documents/Panel-Comments-and-Suggestions.md](../Documents/Panel-Comments-and-Suggestions.md)
- [Data/data-synthesis-handoff.md](../Data/data-synthesis-handoff.md)
- [algorithm-approach-comparison.md](../algorithm-approach-comparison.md)

## 9. What is the basis of this study?

The basis of the study in this repository is three-layered:

### Local financial-behavior basis
The study is grounded in Filipino household and millennial behavior using BSP and related local literature. The strongest local basis in the repo includes:

- the **2021 BSP Consumer Finance Survey**
- **Cacnio & Romarate (2024)** on Filipino financial behavior over the life cycle
- **Dimaunahan et al. (2025)** on Filipino millennials and financial planning
- **Albert et al. (2024)** for income structure, class patterns, and expenditure variation

### Odin-specific design basis
The project proposal and panel documents define Odin’s target users, modules, profiling logic, and scope constraints.

### Data-engineering basis
The `Data/` handoff files formalize how NCR statistics, synthetic data, behavioral profiles, and temporal noise will be used to make the forecasting problem implementable.

So the study is based both on **local financial behavior literature** and on **project-specific system design documents** already contained in this repository.

**Sources in repo:**
- [Documents/Research-Proposal.md](../Documents/Research-Proposal.md)
- [RRL/02_Related Literature/Bangko-Sentral-ng-Pilipinas.md](./02_Related%20Literature/Bangko-Sentral-ng-Pilipinas.md)
- [RRL/02_Related Literature/Cacnio_Romarate.md](./02_Related%20Literature/Cacnio_Romarate.md)
- [RRL/02_Related Literature/Dimaunahan_et-al.md](./02_Related%20Literature/Dimaunahan_et-al.md)
- [RRL/02_Related Literature/Albert_et-al.md](./02_Related%20Literature/Albert_et-al.md)
- [Data/data-synthesis-handoff.md](../Data/data-synthesis-handoff.md)

## 10. How will they take into account seasonal spendings and Filipino cultural expenses?

This is one of the clearest parts of the `Data/` documentation. The handoff explicitly says synthetic data must include **Philippine-specific temporal noise** so the model does not learn unrealistically smooth spending behavior.

The named seasonal or cultural spending events in the repo are:

- **Petsa de Peligro**
- **Payday Spree**
- **13th Month Pay**
- **Christmas / Ber Months**
- **Semana Santa**
- **School Enrollment Season**
- **Undas**
- **Metro Manila Film Festival**
- **BPO Payday Variation**

These events are modeled as **time-bound spending multipliers** affecting categories differently. For example:

- Christmas and 13th month pay increase spending sharply
- Semana Santa changes travel and essentials behavior
- school enrollment redirects funds toward education-related essentials
- Undas affects transport, reunion food, and local Metro Manila purchases

For Filipino cultural expenses more broadly, the proposal and related local materials already identify categories that ordinary Western budgeting apps may miss or underrepresent, such as:

- **family support**
- **paluwagan**
- **church donations**
- **barangay or community collections**
- **SSS and Pag-IBIG-related obligations**

So the repository’s answer is that seasonal and cultural spending will be handled through **category design**, **protected or prioritized categories**, and **Philippine-specific noise modeling** in the synthetic data and forecast logic.

**Sources in repo:**
- [Data/data-synthesis-handoff.md](../Data/data-synthesis-handoff.md)
- [Data/synthetic-data-parameters-handoff.md](../Data/synthetic-data-parameters-handoff.md)
- [Documents/Research-Proposal.md](../Documents/Research-Proposal.md)
- [CHAPTER-1/definition-of-terms-list.md](../CHAPTER-1/definition-of-terms-list.md)
- [RRL/02_Related Literature/Bangko-Sentral-ng-Pilipinas.md](./02_Related%20Literature/Bangko-Sentral-ng-Pilipinas.md)

## Short conclusion

Based on the repository, Odin is being shaped as a Filipino-context personal budget management app that combines forecasting, profiling, recommendation, and monitoring. Its strongest local foundations are the BSP/CFS/FIES-based documents and the project’s own NCR-focused `Data/` handoffs. The one major issue you may want to clean up later is the algorithm framing, because some repository documents still describe **Isolation Forest** as part of the final system while another document recommends a simplified **one-ML-model** design centered only on **LSTM**.
