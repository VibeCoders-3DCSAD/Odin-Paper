```yaml
paper_id: 10.46932/sfjdv7n4-005
designation: local
title: The importance of financial literacy for young adults: a guide to smart money management
authors: Mercado, M. D.; Castillo, A. P.; Araves, J. L. A.
year: 2026
venue: South Florida Journal of Development
odin_topics:
  - 7.A
  - 13.A
  - 13.B
shorthand_tags:
  - /budgeting-strategies
  - /savings-goal-management
  - /debt-management
tldr: Financial literacy empowers young adults to budget, save, manage debt, and invest, reducing stress and expanding life choices.
problem_and_motivation: Young adults face significant financial responsibilities without adequate training, resulting in debt cycles and delayed life milestones. Most lack basic skills in budgeting, credit, and investing. This gap causes financial stress and limits long-term opportunities.
approach:
  - Reviews global survey data from OECD, FINRA, and other sources on financial literacy gaps among young adults aged 18-25.
  - Presents the 50/30/20 budgeting rule as a flexible framework for allocating income to needs, wants, and savings or debt repayment.
  - Discusses saving habits, emergency funds, and compound interest using illustrative figures and tables.
  - Outlines debt management strategies including interest rate awareness, prioritizing high-interest debt, and avoiding minimum payment traps.
  - Advocates for digital tools (apps), community programs, and policy reforms to improve financial literacy access.
findings:
  - "num: Only 31% of young adults aged 18-25 correctly answer basic financial questions on interest, budgeting, and credit (OECD, 2023)."
  - "num: 65% struggle with student loan debt repayment, 58% live paycheck to paycheck, and 54% have no emergency savings."
  - "num: 72% of young adults have little to no investment knowledge, and 60% lack understanding of credit scores."
  - Financial illiteracy delays home buying for 67% and retirement saving for 72% of young adults under 30.
  - Money stress is the number one stressor for adults under 30, leading to anxiety, sleep loss, and avoidance behavior.
key_figures_tables:
  - "Table 1: Common financial challenges faced by young adults → High percentages across debt, paycheck-to-paycheck, no savings, and low investment knowledge."
  - "Figure 1: Areas of financial knowledge young adults struggle with → Investing, credit scores, and budgeting are the weakest areas."
  - "Figure 3: The power of starting early – saving $100/month from age 22 vs. 30 → Starting at 22 yields significantly more wealth due to compound interest."
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: APR
    definition: Annual percentage rate, the yearly cost of borrowing including fees and interest.
  - term: OECD
    definition: Organisation for Economic Co-operation and Development, an intergovernmental economic organization.
  - term: FINRA
    definition: Financial Industry Regulatory Authority, a US private corporation regulating broker-dealers.
  - term: YNAB
    definition: You Need A Budget, a zero-based budgeting software application.
critical_citations:
  - "[OECD, 2023] — Provides foundational literacy gap statistics for young adults."
  - "[FINRA, 2023] — Shows widespread misunderstanding of APR and lack of savings."
  - "[Lusardi & Mitchell, 2008] — Seminal work on financial literacy and planning behavior."
relevance:
  topics:
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      justification: The paper details the 50/30/20 rule as a actionable budgeting framework.
    - code: 13.A
      name: Savings Goal Management in PFMS
      justification: Emphasizes emergency funds, habitual saving, and compound interest for goal achievement.
    - code: 13.B
      name: Debt Management in PFMS
      justification: Covers credit card debt, student loans, interest rates, and repayment prioritization.
  contribution: "Odin can incorporate the 50/30/20 rule as a baseline domain heuristic for its budget recommendation module. The paper's emphasis on emergency savings and compound interest justifies a savings goal feature with automated habit-building and progress visualization. Debt management principles, such as prioritizing high-interest debt and avoiding minimum payments, directly inform Odin's debt payoff algorithm. The finding that 72% of young adults lack investment knowledge suggests a need for in-app educational micro-content integrated with spending forecasts. Finally, the paper's advocacy for digital tools validates Odin's mobile-first approach to reduce user anxiety and increase engagement."
  directly_justifies:
    - "Only 31% of young adults can answer basic financial questions correctly."
    - "58% of young adults live paycheck to paycheck, indicating poor budget adherence."
    - "Starting to save $100/month at age 22 yields far more wealth than starting at 30 due to compound interest."
    - "Financial illiteracy delays home buying for 67% of young adults under 30."
  limits:
    - "The paper is a conceptual guide, not an empirical study of a specific algorithm or system. [unacknowledged]"
    - "Proposed interventions (apps, policy changes) are not experimentally validated. [unacknowledged]"
    - "Findings are aggregated from global surveys and may not generalize to Filipino young professionals specifically. [unacknowledged]"
  mapping_rationale: "This paper maps to three Odin domains: Budget Recommendation (7.A), Savings Management (13.A), and Debt Management (13.B). The 50/30/20 rule directly supports 7.A as domain knowledge for budget heuristics. Sections on emergency funds, compound interest, and goal setting justify 13.A. Discussions of credit card debt, student loans, and interest rates justify 13.B. I rejected Behavioral Profiling (5.A) because the paper does not classify user behaviors algorithmically. I rejected Spending Forecasting (6.A) because no predictive modeling is presented. I rejected Expense Categorization (3.A) because the paper does not propose a taxonomy or labeling system. The paper mentions Filipino authors but the content is not Philippines-specific, so I excluded 1.A–1.C. Borderline topic 2.C (User-Declared Preferences) is absent; the paper does not elicit user input."
limitations:
  - "Relies on secondary survey data without primary data collection or statistical modeling. [unacknowledged]"
  - "Does not address cultural or economic differences across the countries cited in the surveys. [unacknowledged]"
  - "No evaluation of the proposed financial education tools or policy recommendations. [unacknowledged]"
  - "The financial literacy statistics are from 2022-2023 and may not reflect post-pandemic changes. [unacknowledged]"
remember_this:
  - "Only 31% of young adults can answer basic financial questions correctly."
  - "The 50/30/20 rule simplifies budgeting into needs, wants, and savings or debt."
  - "Starting to save early harnesses compound interest for long-term wealth growth."
  - "Financial literacy reduces stress and expands life choices beyond income level."
```