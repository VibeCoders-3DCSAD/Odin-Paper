```yaml
paper_id: 10.4898/jener.v2i3.a32
designation: local
title: "Budgeting Practices and Challenges of Micro-Entrepreneurs in Maria Aurora Public Market: Toward a Strategic Management Plan"
authors: "Delos Santos, D.T.; Austria, M.G.P.; Candelario, C.C.; Garcia, L.E.B.; Gonaranao, B.S."
year: 2026
venue: "JENER Journal of Empirical and Non-Empirical Research"
odin_topics:
  - 3.A
  - 3.B
  - 7.A
  - 13.A
  - 13.B
shorthand_tags:
  - "/expense-categorization"
  - "/category-design"
  - "/budgeting-strategies"
  - "/savings-goals"
  - "/debt-management"
tldr: "Micro-entrepreneurs in Maria Aurora Public Market exhibit high financial discipline in income utilization, expense tracking, savings, and financial planning but face major challenges from debt burdens, inflation, and irregular income."
problem_and_motivation: "Micro-entrepreneurs in rural Philippine public markets often lack structured budgeting systems, hindering their sustainability and growth despite being economic backbones. Existing research does not focus specifically on Maria Aurora's vendors, leaving a gap in localized understanding of their financial practices and barriers."
approach:
  - "Descriptive quantitative design with 68 micro-entrepreneurs sampled via simple random lottery from a population of 82 stall owners, food vendors, and retailers."
  - "Self-constructed Likert-scale survey covering four budgeting dimensions (income utilization, expense tracking, savings, financial planning) and two challenge dimensions (financial liability, income generation)."
  - "Data analyzed using frequency counts, average weighted means (AWM), and verbal interpretation scales (Never to Always for practices; Not a Challenge to Major Challenge for obstacles)."
  - "No baseline comparisons or inferential statistics; findings reported as descriptive means and ranks."
findings:
  - "num: Overall income utilization AWM=3.63 (Always), expense tracking AWM=3.48 (Always), savings AWM=3.49 (Always), financial planning AWM=3.57 (Always)."
  - "num: Financial liability AWM=3.27 (Major Challenge), income generation AWM=3.40 (Major Challenge)."
  - "num: Highest-ranked practice: setting financial goals (AWM=3.77)."
  - "num: Lowest-ranked practice: categorizing expenses into fixed vs variable costs (AWM=3.20)."
  - "num: Managing multiple financial obligations is the top challenge (AWM=3.42)."
  - "num: Only 3.22 AWM for depositing savings in banks or cooperatives, indicating low formal financial integration."
  - "Economic changes (inflation, fuel prices) rank highest among income generation challenges (AWM=3.48)."
  - "Reinvestment of income for business expansion is strongly practiced (AWM=3.67)."
  - "Debt repayments reduce capital for business needs (AWM=3.36)."
  - "Lack of access to affordable financing (AWM=3.38) is a major barrier."
key_figures_tables:
  - "Table 1: Income utilization practices (10 indicators) → Highest AWM=3.77 for allocating income properly, overall discipline is Always."
  - "Table 2: Expense tracking practices → Overall AWM=3.48 (Always), but cost categorization lowest at 3.20."
  - "Table 3: Savings practices → Overall AWM=3.49 (Always), bank deposits lowest at 3.22."
  - "Table 4: Financial planning practices → Overall AWM=3.57 (Always), goal setting highest at 3.77."
  - "Table 5: Financial liability challenges → Overall AWM=3.27 (Major Challenge), managing multiple obligations top at 3.42."
  - "Table 6: Income generation challenges → Overall AWM=3.40 (Major Challenge), economic changes top at 3.48."
  - "Table 7: Strategic plan with five strategies (cost classification, formal banking, forecasting, debt snowball, salary method/two-wallet system)."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "AWM"
    definition: "Average Weighted Mean, a descriptive statistic used to summarize Likert-scale responses."
  - term: "MC"
    definition: "Major Challenge, verbal interpretation for scores 3.26-4.00 in challenge scales."
  - term: "Paluwagan"
    definition: "Informal rotating savings group common among Filipino micro-entrepreneurs."
  - term: "MSMEs"
    definition: "Micro, small, and medium enterprises."
critical_citations:
  - "[Barbosa, 2022] — National study on Filipino micro-entrepreneurs' lack of formal budgeting."
  - "[Dela Cerna, 2025] — Budgeting practices for micro and small business sustainability."
  - "[World Bank, 2019] — Credit exclusion and weak documentation as leading financial constraints."
  - "[Asian Development Bank, 2021] — Debt and high-interest loans as major barriers in Southeast Asia."
relevance:
  topics:
    - code: "3.A"
      name: "Expense Categorization Frameworks"
      justification: "Paper examines expense tracking and the gap in fixed vs variable cost categorization."
    - code: "3.B"
      name: "Expense Category Design Considerations"
      justification: "Findings show manual categorization is weak, supporting need for automated, intuitive category design."
    - code: "7.A"
      name: "Budgeting Strategies as Domain Knowledge"
      justification: "Paper details four budgeting dimensions (income utilization, tracking, savings, planning) that inform rule-based budget recommendations."
    - code: "13.A"
      name: "Savings Goal Management in PFMS"
      justification: "High savings discipline but low formal banking use guides savings goal features that incentivize bank integration."
    - code: "13.B"
      name: "Debt Management in PFMS"
      justification: "Major challenges from multiple obligations and high interest rates justify debt consolidation and repayment strategy modules."
  contribution: "The paper's detailed breakdown of income utilization, expense tracking, savings, and financial planning provides domain knowledge for Odin's budget recommendation module (7.A). The identified gap in fixed vs variable cost categorization (AWM=3.20) directly informs the design of Odin's expense categorization feature (3.A/3.B) to automate classification. The high savings discipline but low use of formal banks (AWM=3.22) suggests that Odin's savings goal management (13.A) should integrate with partner banks or cooperatives to reduce friction. The major debt challenges (AWM=3.27) justify a dedicated debt management module (13.B) featuring snowball/avalanche methods and consolidation advice. The strategic plan's 'Salary Method' and 'Two-Wallet System' can be translated into user-facing budgeting nudges within Odin."
  directly_justifies:
    - "Micro-entrepreneurs struggle to categorize expenses into fixed and variable costs, justifying automated expense categorization in Odin."
    - "High debt repayment pressure reduces capital for business needs, supporting a debt management module with repayment planning."
    - "Low tendency to deposit savings in banks (AWM=3.22) indicates Odin should facilitate micro-savings accounts with low barriers."
    - "Setting financial goals is the strongest practice (AWM=3.77), so Odin should emphasize goal-setting as a core onboarding step."
    - "Managing multiple financial obligations is the top challenge (AWM=3.42), justifying features for viewing and prioritizing liabilities."
  limits: "The study samples only 68 micro-entrepreneurs from one public market, limiting generalizability to other demographics or regions. Self-reported Likert data may suffer from social desirability bias. No qualitative follow-up was conducted despite mention of mixed methods in the introduction. The cross-sectional design cannot establish causality between practices and outcomes. [unacknowledged] The paper does not discuss potential self-selection bias in survey participation."
  mapping_rationale: "The paper focuses on budgeting practices and financial challenges of micro-entrepreneurs, not directly on young professionals or PFMS algorithms. However, its detailed domain knowledge on expense tracking (3.A/3.B), budgeting strategies (7.A), savings behavior (13.A), and debt management (13.B) is highly relevant for Odin's financial modules. Topics related to behavioral profiling (5.A-C), forecasting (6.A-B), anomaly detection (8.A-B), mobile design (9.A-B), privacy (10.A-B), retention (11.A-B), and system evaluation (12.A-B) were rejected because the paper does not address them. The borderline case of expense categorization was selected because the paper's lowest-ranked practice (fixed vs variable cost separation) directly informs Odin's design need for automated categorization."
limitations:
  - "Single-site study (Maria Aurora Public Market) limits external validity."
  - "Reliance on self-reported Likert scales may introduce social desirability and recall bias. [unacknowledged]"
  - "Mixed methods promised in introduction but only quantitative data collected; no qualitative triangulation. [unacknowledged]"
  - "Cross-sectional design prevents causal inference about relationships between practices and challenges."
  - "No statistical tests (e.g., chi-square, regression) were performed; only descriptive means and ranks reported. [unacknowledged]"
remember_this:
  - "Income utilization discipline is high with AWM=3.63 (Always)."
  - "Managing multiple debts is the top financial liability challenge (AWM=3.42)."
  - "Only 3.22 AWM for depositing savings in banks shows low formal integration."
  - "Setting financial goals is the strongest budgeting practice (AWM=3.77)."
  - "Economic changes like inflation rank highest among income generation challenges (AWM=3.48)."
```