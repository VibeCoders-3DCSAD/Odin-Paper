```yaml
paper_id: 10.23919/JSC.2025.0015
designation: international
title: Consumer Autonomy or Illusion? Rethinking Consumer Agency in the Age of Algorithms
authors: Nokhiz, P.; Ruwanpathirana, A. K.
year: 2025
venue: Journal of Social Computing
odin_topics:
  - 3.A
  - 5.A
  - 7.A
  - 7.B
  - 13.A
shorthand_tags:
  - /expense-categorization
  - /behavioral-profiles
  - /budgeting-strategies
  - /budget-recommendation
  - /savings-goals
tldr: Formal analysis shows that obligatory consumption, algorithmic persuasion, and unstable work schedules lead rational consumers to early financial ruin despite utility-maximizing behavior.
problem_and_motivation: Consumer agency in digital ecosystems is eroded by systemic barriers like obligatory subscriptions, algorithmic manipulation (e.g., BNPL, personalized ads), and unpredictable work schedules. The authenticity of consumer choices is questioned as external pressures undermine financial autonomy. Existing models lack formal treatment of how limited agency impacts long-term financial stability.
approach:
  - Constructs discounted utility models with constraints representing obligatory consumption (fixed amount), impulsive consumption (minimum subsistence plus discretionary spending), and income uncertainty from unstable work schedules.
  - Assumes rational utility-maximizing agents with concave utility functions (CRRA) and no borrowing.
  - Defines financial ruin as assets reaching zero within finite time.
  - Uses Jensen's inequality and concentration inequalities to prove ruin probability.
  - Analyzes three scenarios: fixed obligatory consumption, algorithm-driven impulsive spending, and work schedule unpredictability (lookahead).
  - Draws on prior work on lookahead and Yao's min-max theorem to show utility gaps.
  - Proposes value deliberation and regulatory interventions as solutions, with formal proofs of improved outcomes.
findings:
  - num: Rational consumers with fixed obligatory consumption will go to ruin regardless of utility function concavity.
  - num: With impulsive consumption and minimum subsistence, probability of avoiding ruin decays exponentially as exp(-cT) for sufficiently large T.
  - num: Lookahead of k steps yields utility advantage of Ω(k) over no lookahead under bounded income.
  - Algorithmic persuasion and obligatory consumption create value capture, where consumers adopt externally imposed values without critical reflection.
  - Work schedule instability undermines financial planning and agency, leading to lower achieved utility.
key_figures_tables:
  - Figure 1: Flowchart of three agency constraints (obligatory, algorithmic, temporal) leading to limited agency, lower welfare, and ruin → three distinct dimensions erode autonomy.
  - Figure A1: Distribution of ruin times under impulsive consumption → most agents ruin within first 10 months.
  - Figure A2: Ruin times for low-income vs high-income → low-income agents ruin instantly, high-income show spread.
  - Figure A3: Ruin times by education (college vs high school) → less educated ruin faster.
key_equations:
  - equation: "\\max_{c_t} \\mathbb{E} \\sum_{t=0}^{\\infty} \\beta^t u(c_t)"
    explanation: Discounted utility maximization over infinite horizon.
  - equation: "a_{t+1} = R_t (a_t - c_t) + y_t"
    explanation: Asset evolution with return R_t and income y_t.
  - equation: "0 \\le c_t \\le a_t"
    explanation: Consumption cannot exceed current assets.
definitions:
  - term: Ruin
    definition: State where consumer's assets become zero or negative within finite time horizon.
  - term: Lookahead
    definition: Number of future time steps for which income is known with certainty.
  - term: Obligatory consumption
    definition: Fixed consumption amount required each period, cannot be adjusted.
  - term: Value capture
    definition: Adoption of externally imposed values without critical reflection or personal adaptation.
critical_citations:
  - "[Deaton, 1992] — Foundational discounted utility consumption model."
  - "[Frederick et al., 2002] — Time discounting and preference critical review."
  - "[Nguyen, 2024] — Value capture concept."
  - "[Nokhiz, 2024] — Prior work on lookahead and financial precarity."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      justification: Distinguishes obligatory vs impulsive consumption categories.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      justification: Models consumer agency erosion and value capture as behavioral constraints.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      justification: Formally shows fixed consumption leads to ruin, informing budget design.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      justification: Demonstrates need for flexible budgeting to avoid ruin from algorithmic impulses.
    - code: 13.A
      name: Savings Goal Management in PFMS
      justification: Ruin analysis directly relates to savings depletion under spending pressure.
  contribution: "This paper provides a formal framework for modeling how limited consumer agency leads to financial ruin, which can inform Odin's spending forecasting module by quantifying risk from obligatory payments. The analysis of algorithmic persuasion and impulsive consumption justifies Odin's anomaly detection features that flag potential manipulation-driven spending. The work schedule instability results support Odin's budgeting recommendations that account for income volatility, especially for gig economy users. The proposed value deliberation interventions align with Odin's user engagement strategies to promote financial literacy and autonomous decision-making."
  directly_justifies:
    - "Consumers with fixed obligatory expenses face guaranteed ruin under rational utility maximization."
    - "Algorithmic impulse triggers increase ruin probability exponentially over time."
    - "Workers with advance schedule notice (lookahead) achieve Ω(k) higher utility than those without."
    - "Value deliberation interventions (prioritizing essential needs) enable consumers to avoid ruin indefinitely."
  limits:
    - "Assumes rational utility-maximizing agents, not behavioral biases like present bias."
    - "Does not model debt or credit usage, which can amplify or mitigate ruin risk."
    - "Income distributions assumed known mean and bounds; real-world heterogeneity may affect results."
    - "Experimental data are illustrative simulations, not real-world validation."
  mapping_rationale: "This paper was screened against Odin's functional domains. It strongly relates to Behavioral Profiling (5.A) through its analysis of value capture and agency erosion. It informs Spending Forecasting (6.A) and Budget Recommendation (7.A, 7.B) by providing formal ruin conditions under fixed and impulsive consumption. The distinction between obligatory and discretionary spending maps to Expense Categorization (3.A). Savings and debt management (13.A) is relevant via the ruin concept. Topics like anomaly detection (8) and user trust (10) were rejected as the paper does not discuss detection algorithms or privacy. Temporal uncertainty from work schedules is not directly a PFMS feature but informs user context modeling. Overall, 5 topics were selected as directly citable for Odin's algorithmic and design decisions."
limitations:
  - "Model uses simple intertemporal consumption framework without debt or liabilities."
  - "Does not incorporate behavioral economics insights like present bias or loss aversion."
  - "Macroeconomic factors like inflation and recessions not modeled."
  - "Experimental data uses US statistics, not specific to Filipino context."
remember_this:
  - Fixed obligatory consumption guarantees financial ruin even for rational agents.
  - Algorithmic impulse triggers make ruin exponentially more likely over time.
  - Knowing work schedules 2 weeks ahead yields significantly higher utility.
  - Value deliberation helps consumers avoid ruin by prioritizing essential needs.
```