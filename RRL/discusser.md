# Chapter 2 RRL Drafting — Instruction Handoff

## What You Are Doing

You are drafting sections of **Chapter II: Review of Related Literature and Studies** for a thesis called **Odin** — an intelligent personal budget management system (PBMS) for Filipino young professionals aged 20–40 in Metro Manila. The thesis is written in academic English. All output must be a `.md` file.

Chapter 2 is organized into **numbered Topics** (e.g., Topic 1, Topic 2, ...). Each topic contains **lettered subtopics** (e.g., 1.A, 1.B, 1.C). Each topic produces **one section** of Chapter 2.

---

## Input You Will Receive

For each topic, you will receive one compilation file per subtopic (e.g., `1_A_Compilation.md`, `1_B_Compilation.md`, `1_C_Compilation.md`). Each file contains multiple source summaries in this structure:

```
## Source: `[filename]`

**Title:** [Paper title]

### TL;DR
[One-paragraph summary]

### Findings
[Numbered or bulleted key findings with statistics]

### Relevance to Odin
**Topics:** [list of subtopic codes this source is mapped to]
**Contribution to Odin:** [how the source informs Odin's design]
**Directly justifies:** [specific quotable claims]
**Limits of relevance:** [scope and applicability caveats]

### Limitations
[Methodological limitations of the source study itself]
```

The same source may appear in multiple compilation files. It is **not** duplicated in error — it is relevant to multiple subtopics.

---

## Output Structure

Each topic produces **one section** with this exact structure:

### Section Header
Use the topic's full name as a Markdown H1, **bold**:
```
# **[Topic Name]**
```

### Discussion (body paragraphs)
Write **1–2 paragraphs total** covering all subtopics under the current topic. Do not write one paragraph per subtopic. Group findings thematically across subtopics, not by subtopic label. The number of paragraphs is determined by content density: if all subtopic findings can be synthesized coherently into one paragraph, use one; if the findings span clearly distinct thematic angles that resist compression, use two. Never exceed two. There are no subheadings between body paragraphs.

### Synthesis
Write **exactly two paragraphs** under a `## Synthesis` subheading:
- **Paragraph 1:** Summarizes the methodological range of reviewed works and states the convergent finding across the full topic. Ends by connecting those findings to Odin's design decisions.
- **Paragraph 2:** Identifies research gaps in the existing literature and explains how Odin addresses each gap. Must connect gaps to specific Odin modules or design decisions.

---

## How to Write the Discussion Paragraphs

### Source selection
- A topic may have 10–20+ sources across its subtopics. **Do not cite every source.** Select the most relevant and methodologically strongest sources per subtopic. Aim for 4–8 sources per paragraph.
- When a source appears in multiple compilation files, use only the findings most relevant to the subtopic that paragraph covers.
- Prioritize sources with: (a) Filipino-specific data, (b) quantitative findings with specific statistics, (c) direct design implications for Odin. Deprioritize: highly geographically limited studies, studies with very small samples whose findings are fully subsumed by stronger sources, and studies whose relevance is only to later topics.

### Prose style
- Write in dense, continuous academic prose. **No bullet points. No numbered lists. No subheadings within paragraphs.**
- Integrate statistics directly into sentences: *"Dimaunahan et al. (2025) find that financial literacy has no significant direct effect on financial planning behavior (β = 0.077, p = 0.153)"* — not a bullet.
- Begin each paragraph with a topic sentence that frames the subtopic's angle for the reader.
- End each paragraph with a sentence that connects the reviewed evidence to a specific Odin design implication.
- Do not editorialize with phrases like "importantly," "notably," or "it is worth noting." Let the findings speak.
- Use author-year in-text citations: *Author et al. (year)*, *Author and Author (year)*, *Author (year)*.

### Citation accuracy
- **Reproduce statistics exactly as they appear in the source summary's "Directly justifies" or "Findings" sections.** Do not round, paraphrase, or estimate numbers you were not given.
- Do not fabricate statistics that do not appear in the compiled source summaries.
- If a source's finding is used, its citation must appear in the text.

### Odin design connections
- Every paragraph must connect findings to at least one Odin module or design decision (e.g., the forecasting module, the behavioral profiling module, the anomaly detection module, the budget recommendation module, the protected-category architecture, the expense categorization structure, the mobile-first architecture).
- These connections should be specific: *"a pattern with direct implications for anomaly detection calibration"* is acceptable; *"this is relevant to Odin"* is not.
- Do not repeat the same Odin design connection across paragraphs within one section unless each instance adds a distinct design implication.

---

## How to Write the Synthesis

### Paragraph 1 — Methodological summary and convergence
- Open by naming the methodological range of the reviewed works (e.g., nationally representative surveys, quantitative cross-sectional studies, qualitative investigations, behavioral economics experiments, systematic reviews).
- Name specific studies as examples of each method type using author-year citations.
- State the single convergent finding that runs across the reviewed works.
- Close by connecting the convergent finding to Odin's design at the module level.

### Paragraph 2 — Gaps and Odin's response
- Open by naming the most significant gaps in the existing literature.
- Be specific: name what is missing (e.g., "no longitudinal tracking of budgeting behavior change," "no category-level spending weights derived from Filipino transaction data"), not just that gaps exist.
- For each gap, state how Odin addresses it. Be specific about which module or design decision closes the gap.
- Do not introduce new sources in the Synthesis that were not discussed in the body paragraphs.

---

## Hard Rules

1. **Never use bullet points, numbered lists, or subheadings within body paragraphs.**
2. **Never fabricate a statistic.** If a number is not in the compilation, do not include it.
3. **Never cite a source not present in the compilation files.** Do not add sources from your own training data or prior knowledge.
4. **Never add sources from your training knowledge** that are not in the compilations, even if you are certain they are real and relevant. The source registry is controlled by the research team, not by you.
5. **Do not repeat the same source in multiple subtopic paragraphs** unless it contributes clearly distinct findings relevant to each subtopic. When in doubt, place the source in the paragraph where its strongest finding sits and omit it from others.
6. **The Synthesis must not introduce new sources** not cited in the body paragraphs.
7. **The topic section is exactly one H1 header + N body paragraphs (one per subtopic) + one H2 Synthesis with two paragraphs.** No additional structure.
8. **Output must be a `.md` file.** Never produce `.docx`.
9. **Read all compilation files in full before writing.** Truncated readings produce omissions.

---

## Quality Benchmark

The approved output for Topic 1 (three subtopics: 1.A, 1.B, 1.C) is reproduced below as the canonical example. All future sections must match its density, citation integration, prose style, paragraph structure, and specificity of Odin design connections.

---

### APPROVED EXAMPLE — Topic 1: Filipino Young Professionals and the Financial Problem

> **Note on paragraph count:** Topic 1 has three body paragraphs because its three subtopics (demographic structure, cultural financial obligations, behavioral mechanics) cover sufficiently distinct thematic territory that compression into two paragraphs would sacrifice coherence. This is the upper bound, not the default. Most topics with 2–3 subtopics should produce 1–2 body paragraphs. Do not use this example to infer that three paragraphs is standard.

# **Filipino Young Professionals and the Financial Problem**

Albert et al. (2025) establish the structural baseline of income inequality among Filipinos: the Gini coefficient for per capita income declined from 0.453 in 2015 to 0.406 in 2023, yet income stratification remains steep, with households headed by college graduates earning a 2:1 income share relative to their population share. Women's labor force participation stagnates at approximately 50% against 74% for men, with 90% of married women citing household duties as their primary reason for not working — a pattern directly relevant to Odin's assumption that a significant portion of target users may carry irregular or part-time income and unpaid care responsibilities that weight their expense structures. Jandoc et al. (2026) characterize the rising platform worker segment, showing that approximately 8.2% of Filipino workers — predominantly young, urban, and highly educated, with 31% concentrated in the NCR — now rely on platform work as their sole source of livelihood, yet face significantly lower odds of employer-provided pension contributions, health insurance, and separation benefits. Flores (2025) documents that among corporate workers in large firms, 43% are aged 31–40 and 40% earn ₱30,000 or more monthly, yet the same population reports common reliance on informal cash storage, reluctance to engage with formal financial instruments, and a regression analysis that finds no significant contribution of cash, debt, risk, or wealth management practices to actual financial freedom. Amado (2026) and Am-una (2026) demonstrate, respectively, that Filipino professionals under semi-monthly pay cycles experience persistent financial stress between pay periods despite perceiving the structure as beneficial for short-term planning, and that among public school teachers, a moderately positive mean financial behavior score of 2.69 out of 4.00 is sustained primarily by compensatory constraint rather than financial security, with financial literacy seminar attendance showing no measurable effect on behavior whatsoever (p = .991).

The financial structures within which Filipino young professionals operate are further shaped by a constellation of culturally specific obligations that have no direct equivalent in Western personal finance frameworks. Donato et al. (2023) document that Filipino working millennials express utang na loob — the deeply felt obligation to repay those who have helped them — primarily through financial support to parents in the form of allowances, household bills, and necessities, with the same obligation simultaneously generating fulfillment and compromising personal savings when demands exceed income. Dimaranan and Dy (2025) confirm the prevalence of remittance-driven budgeting among Filipino families, finding that all nine study participants committed monthly remittances across the income spectrum, with emergency requests from Philippine-based relatives consistently placing otherwise well-managed household budgets at risk. Bongalonta et al. (2024) find that even among government-salaried faculty members, 60% save less than 15% of their income, with paluwagan and piggy bank saving mechanisms remaining widely used alongside formal bank accounts, and delayed salary releases and automatic loan deductions compressing available cash flow at the start of each month. Canete and Liwanag (2024) situate these patterns within the Filipino concepts of ubos-biyaya — the culturally conditioned tendency to spend immediately upon receipt of income — and petsa de peligro, the pre-payday period of scarcity that follows, noting that 87% of Filipinos buy more than planned when shopping, a rate exceeding comparable figures from other countries. Banta (2025) demonstrates, in the context of OFW financial obligation, that family-driven spending is structural rather than discretionary: Filipino workers incur debt to finance migration and family emergencies rather than through conspicuous consumption, and that financial literacy training which moralizes debt without accounting for these structural drivers risks alienating and shaming users rather than improving their outcomes.

The behavioral dimension of Filipino young professional finance reveals a consistent and well-documented gap between financial knowledge and financial action. Dimaunahan et al. (2025) find that financial literacy has no significant direct effect on financial planning behavior among Filipino millennials (β = 0.077, p = 0.153), while monthly expenses (β = 0.205), monthly income (β = 0.180), and occupation (β = 0.164) are the strongest structural predictors — and goal acceptance (β = 0.924) and goal commitment (β = 0.809) are the strongest psychological ones. Lim and Cordova (2024) find that financial attitude, not financial literacy, is the only significant predictor of spending behavior among Filipino millennials (β = -0.176, p = 0.034), with literacy showing no direct significant relationship (β = -0.045, p = 0.477). Apao et al. (2025) corroborate this across a student sample, reporting very high financial knowledge (M = 3.74/4) that carries no significant correlation with actual financial behavior (r = -0.46, p = 0.652), and Cadayunan et al. (2025) document that Filipino university students self-report high financial literacy yet struggle specifically with creating and sticking to budgets and resisting impulse purchases. Rodriguez et al. (2024) model this gap formally: using structural equation modeling on a Gen Z sample, they show that financial behavior mediates the literacy-to-spending relationship (indirect effect estimate = 0.180, 95% CI [0.114, 0.245]), with literacy alone explaining only 51.9% of behavioral variance, meaning that nearly half of behavioral variation is driven by factors other than knowledge. From a behavioral economics perspective, Ma et al. (2026) document that consumers self-impose monthly mental budgets that renew on paydays, with first-trip-after-payday spending running 3.3% higher than later trips and payday-specific salience producing a further expenditure overshoot — a cyclical pattern with direct implications for anomaly detection calibration. Cheng et al. (2023) demonstrate that income source interacts with psychological state to determine spending allocation: windfall gains increase hedonic spending preference by 30–40 percentage points over utilitarian alternatives, but a high scarcity mindset eliminates this effect, making Odin's budget recommendation logic dependent not only on income amount but on how income is received and how financially constrained the user perceives themselves to be. Nokhiz and Ruwanpathirana (2025) formally prove that obligatory fixed payments — subscriptions, contributions, fees — can drive even rational utility-maximizing consumers to financial ruin without a deliberate priority-ordering strategy, and that value deliberation, or allocating to essentials before discretionary spending, is the structurally sound countermeasure. Askhiyah (2026) provides large-scale empirical reinforcement from an ASEAN-adjacent context: digital finance adoption increases household consumption by 8.7%, raises debt-to-income ratios by 6.4 percentage points among young lower-middle-income users, and lowers savings balances despite increasing formal account ownership — a cautionary portrait of what engagement without behavioral structure produces. Amrith (2026) situates the underlying cultural driver: Filipino workers abroad report returning home after 15–25 years without savings because they "give in" to never-ending family demands, a breadwinner mentality that budget recommendation modules must accommodate rather than oppose.

## Synthesis

The studies reviewed across subtopics 1.A through 1.C collectively construct a layered and empirically grounded portrait of the Filipino young professional as a financial actor operating under structural constraint, cultural obligation, and a persistent gap between financial knowledge and financial action. Methodologically, the evidence spans nationally representative employment and income surveys (Albert et al., Jandoc et al.), profession-specific quantitative studies of Filipino financial behavior (Dimaunahan et al., Am-una, Amado, Flores), qualitative investigations of cultural financial practices (Donato et al., Dimaranan and Dy, Canete and Liwanag, Banta), and international behavioral economics studies whose mechanisms generalize to the Filipino context (Ma et al., Cheng et al., Nokhiz and Ruwanpathirana, Askhiyah). The convergent finding across this methodological diversity is that demographic factors — income type and stability, employment category, marital status, and the weight of culturally obligated expenses — are stronger predictors of financial behavior than financial literacy, and that knowledge-focused interventions consistently fail to bridge the literacy-to-behavior gap without structural behavioral support. The evidence that income type determines not only spending capacity but spending volatility, that culturally obligated categories (family remittances, paluwagan, utang na loob expressions) function as non-negotiable expense floors rather than discretionary choices, and that payday-cycle dynamics predictably shape spending peaks and troughs, collectively provide the empirical foundation for Odin's four-profile classification framework, its protected-category architecture, and its need for cycle-aware forecasting and anomaly detection.

Several critical gaps emerge from this body of literature that directly motivate Odin's design. Most Filipino studies are cross-sectional and profession-skewed — concentrated in teachers, faculty members, and institutional workers — with limited quantitative coverage of private-sector young professionals in Metro Manila's mixed employment landscape of salaried, gig, and freelance work. Culturally specific financial behaviors, particularly paluwagan cycles, utang na loob obligations, and petsa de peligro spending patterns, are well-documented qualitatively but rarely operationalized in ways that can directly inform algorithmic design: no existing study provides category-level spending weights derived from transaction data for these cultural expenditure types. The behavioral findings confirm that effective financial tools must prioritize behavioral infrastructure — automated tracking, structured budget periods aligned to pay cycles, protected category allocation, and obligation-aware anomaly thresholds — over educational content alone. Odin addresses these gaps by grounding its profiling module in observed transaction behavior rather than self-reported literacy, its categorization structure in FIES and BSP Consumer Finance Survey frameworks extended with Filipino-specific obligation categories, and its budget recommendation and anomaly detection logic in the cycle-aware, culturally-sensitive behavioral patterns documented across the reviewed literature.