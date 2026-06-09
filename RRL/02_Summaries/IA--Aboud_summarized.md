```yaml
paper_id: 10.21070/acopen.10.2025.12858
designation: international
title: Goal Programming Model in Financial Planning of the International Development Bank
authors: Aboud, S. F.
year: 2025
venue: Academia Open
odin_topics:
  - 7.A
  - 7.C
  - 12.A
shorthand_tags:
  - /budgeting-strategies
  - /budget-recommendation
  - /evaluation-frameworks
tldr: Goal programming optimizes conflicting financial objectives (revenue, expenses, profit, assets) in a bank's financial planning, achieving near-optimal resource allocation.
problem_and_motivation: Financial institutions struggle to balance multiple conflicting objectives like profit maximization, cost control, and liquidity. Traditional planning models cannot accommodate competing goals under resource constraints. A quantitative method is needed to prioritize and trade off these objectives.
approach:
  - Data: Annual reports of International Development Bank for Investment and Finance (Iraq) from 2016 to 2024.
  - Method: Weighted-preemptive hybrid goal programming with seven prioritized goals and assigned weights.
  - Solved using WINQSB software.
  - Goals: revenue (min 0.290878B/year), expenses (max 0.238279B), net profit (min 0.342094B), fixed assets (min 1.069823B), loans (max 0.684292B), common stock (min 0.337092B), financial management ratio (min 1.608461B).
findings:
  - num: The model achieved near-optimal solutions with minimal deviations across all seven goals.
  - num: Revenue goal met with negative deviation 0.1884 billion.
  - num: Expenses goal met with deviation 0.1873 billion.
  - num: Net profit met with deviation 0.3006 billion.
  - num: Fixed assets exceeded target with positive deviation 0.7833 billion.
  - Loan reduction goal fully achieved (deviations zero).
  - num: Equity goal partially achieved with deviation 0.2956 billion.
key_figures_tables:
  - Table 1: Raw financial data (2016-2024) for seven variables → Provides input to goal programming model.
  - Table 2: Scaled values in billion IQD → Normalizes data for optimization.
key_equations:
  - equation: \min Z = \sum_{i=1}^{m} (w_i^- d_i^- + w_i^+ d_i^+)
    explanation: Weighted method minimizes total weighted deviations.
  - equation: \min Z = \sum_{i=1}^{n} \rho_i (d_i^- + d_i^+)
    explanation: Preemptive method ranks goals by priority.
definitions:
  - term: Goal Programming
    definition: Mathematical model transforming all functions into goals with deviation variables.
  - term: Negative Deviation
    definition: Amount actual value falls below aspiration level.
  - term: Positive Deviation
    definition: Amount actual value exceeds aspiration level.
  - term: Weighted Method
    definition: Assigns numeric weights to each goal and minimizes total deviation.
  - term: Preemptive Method
    definition: Solves multi-criteria problems by ranking goals, satisfying higher priorities first.
critical_citations:
  - "[Alam, 2022] — Applied GP to SABIC financial planning."
  - "[Nyor, 2022] — GP in Nigerian industrial goods firm."
  - "[Lakshmi, 2021] — GP in Indian distribution company."
relevance:
  topics:
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      justification: Goal programming is a quantitative multi-objective optimization strategy applicable to budget allocation.
    - code: 7.C
      name: Budget Recommendation Algorithm
      justification: The weighted-preemptive GP model can inform algorithm design for personal finance budget recommendations.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      justification: The paper evaluates GP model performance using deviation minimization, a framework for algorithm assessment.
  contribution: The weighted-preemptive hybrid goal programming approach can inform Odin's budget recommendation module by providing a method to balance user-defined savings, spending, and debt repayment goals. The deviation minimization objective aligns with Odin's need to respect user priorities (e.g., essential expenses first). The WINQSB implementation demonstrates a practical evaluation pathway for algorithmic modules.
  directly_justifies:
    - Goal programming can resolve conflicting financial objectives by assigning priorities and weights.
    - Near-optimal solutions are achievable with minimal deviation from targets.
    - Preemptive ordering ensures higher-priority goals are satisfied before lower ones.
  limits:
    - The model assumes linear relationships between decision variables.
    - Results are specific to a single bank's data (2016-2024).
    - The paper does not address dynamic or real-time re-planning.
  mapping_rationale: The paper focuses on multi-objective financial planning using goal programming. While applied to a bank rather than personal finance, the methodology directly informs Odin's budget recommendation (7.C) and budgeting strategies (7.A) because personal finance involves similar trade-offs (spending vs saving vs debt). The evaluation approach (12.A) is also relevant as Odin needs to validate its algorithmic modules. Topics related to behavioral profiling (5.A-C), forecasting (6.A-B), anomaly detection (8.A-B), and mobile design (9.A-B) are not addressed. Expense categorization (3.A-B) is not covered. Thus only 7.A, 7.C, and 12.A are selected.
limitations:
  - The model uses annual data, not high-frequency spending data typical of PFMS. [unacknowledged]
  - User-specific preferences or behavioral dynamics are absent. [unacknowledged]
  - No comparison with baseline or alternative algorithms. [unacknowledged]
remember_this:
  - Goal programming balances revenue, expenses, profit, and assets with minimal deviations.
  - The preemptive method satisfies higher-priority goals before lower ones.
  - Achieved near-optimal solutions in a multi-objective banking scenario.
  - Deviations as low as 0.1884 billion for revenue target.
```