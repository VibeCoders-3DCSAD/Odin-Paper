```yaml
paper_id: 10.32890/jdsd2025.3.2.9
designation: international
title: Development and Evaluation of My Money Manager: An Intelligent Mobile App for Personalized Financial Insight
authors: Parameswaran, S.; Saad, S. Z.
year: 2025
venue: Journal of Digital System Development
odin_topics:
  - 3.A
  - 3.B
  - 8.A
  - 9.A
  - 9.B
  - 12.A
  - 13.A
shorthand_tags:
  - /expense-categorization
  - /category-design
  - /anomaly-detection
  - /mobile-first
  - /ux-design
  - /evaluation-framework
  - /savings-management
tldr: My Money Manager mobile app uses algorithmic expense categorization and 90-day spending analysis to provide personalized savings recommendations and anomaly detection, with a usability study showing high effectiveness in tracking and habit improvement.
problem_and_motivation: Existing personal finance apps lack intelligent analysis and personalized guidance, often offering generic one-size-fits-all advice that fails to account for individual spending patterns. Most apps do not differentiate fixed versus variable expenses or detect abnormal spending behaviors, leading to irrelevant recommendations.
approach:
  - Iterative and incremental development methodology with agile principles and user-centered design.
  - Android app following Model-View-Controller pattern and Material Design guidelines.
  - Key calculations: monthly income, expenses, savings, income/expense ratio, budget status, category expense, and category percentage.
  - Evaluation with 35 participants using six-point Likert-scale questionnaires across four dimensions: App Experience, Perceived Ease of Use, Perceived Usefulness, and Perceived Acceptance.
  - Features include automated expense categorization, fixed/variable expense differentiation, spending anomaly detection, and 90-day trend analysis.
findings:
  - "num: 82.8% of users confirmed income and expense tracking was efficient and reliable."
  - "num: 74.3% reported the app encouraged them to manage finances more effectively."
  - "num: 71.4% agreed that financial insights helped guide their financial decision-making."
  - "num: 77.1% rated navigation, adding entries, and setting budgets as very easy (strongly agree)."
  - "num: 45.7% strongly agreed and 37.1% agreed that tracking income/expenses was easy."
  - "Only 37.1% strongly agreed that viewing and understanding financial insights was easy; 14.3% found it somewhat difficult."
  - "Data security confidence was low: 31.4% somewhat disagreed that their data was safe."
key_figures_tables:
  - "Figure 2: Home screen dashboard → Central hub with balance, quick actions, and recent transactions."
  - "Figure 6: Financial insights interface → Charts for spending patterns, trends, and anomaly detection."
  - "Figure 8: Perceived ease of use → Navigation and data entry highly rated; insights comprehension lowest."
  - "Table 1: Responses on Perceived Ease of Use → 77.1% strongly agreed navigation was easy."
  - "Table 2: Responses on Perceived Usefulness → 82.8% agreed expense tracking was effective."
key_equations:
  - equation: "Monthly Income = \\sum(\\text{all income entries for selected month})"
    explanation: "Sum of income entries in a month."
  - equation: "Monthly Expenses = \\sum(\\text{all expense entries for selected month})"
    explanation: "Sum of expense entries in a month."
  - equation: "Monthly Savings = Monthly Income - Monthly Expenses"
    explanation: "Difference between income and expenses."
  - equation: "Income/Expense Ratio = Monthly Income \\div Monthly Expenses"
    explanation: "Ratio of income to expenses."
  - equation: "Budget Status = Monthly Budget - Monthly Expenses"
    explanation: "Surplus or deficit relative to budget."
  - equation: "Category Expense = \\sum(\\text{expenses for specific category in month})"
    explanation: "Total spending per category."
  - equation: "Category Percentage = (Category Expense \\div Monthly Expenses) \\times 100"
    explanation: "Category share of total expenses."
definitions:
  - term: Fixed expenses
    definition: Essential recurring costs such as rent, loan payments, and utilities.
  - term: Variable expenses
    definition: Discretionary costs such as entertainment, dining out, and shopping.
  - term: Anomaly detection
    definition: Identification of unusual spending behaviors compared to historical patterns.
  - term: 90-day analysis
    definition: Review of financial trends over a 90-day period to generate actionable insights.
critical_citations:
  - "[Shaikh et al., 2022] — Found existing apps fail to differentiate fixed vs variable expenses."
  - "[Mijić & Ćebić, 2023] — Identified static, one-size-fits-all recommendations as a key limitation."
  - "[Carlin et al., 2022] — Showed mobile apps reduce barriers and improve financial behavior."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      justification: App automatically categorizes expenses and distinguishes fixed vs variable costs.
    - code: 3.B
      name: Expense Category Design Considerations
      justification: Custom category creation and predefined options inform category design.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      justification: Financial insights interface highlights unusual spending behaviors.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      justification: App follows Material Design and mobile-first principles for Android.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      justification: Usability evaluation measured ease of navigation, data entry, and budget setting.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      justification: Structured Likert-scale evaluation across four dimensions with 35 participants.
    - code: 13.A
      name: Savings Goal Management in PFMS
      justification: Personalized savings recommendations based on 90-day spending patterns.
  contribution: "This paper provides a validated implementation of automated expense categorization and anomaly detection for a mobile PFMS, directly informing Odin's expense categorization module (3.A, 3.B) and anomaly detection module (8.A). The usability evaluation framework (12.A) offers a template for Odin's system evaluation. The mobile-first UX design and user acceptance results (9.A, 9.B) guide Odin's mobile interface decisions. The savings recommendation logic (13.A) can be adapted for Odin's savings and debt management features."
  directly_justifies:
    - "Automated differentiation between fixed and variable expenses improves personalized financial guidance."
    - "Spending anomaly detection can be implemented using simple threshold or deviation calculations on 90-day windows."
    - "Mobile PFMS evaluation should measure ease of use for navigation, data entry, and insights comprehension separately."
    - "User trust in data security is a critical barrier that requires explicit design attention."
  limits:
    - "Small sample size (n=35) limits generalizability of usability findings."
    - "Evaluation was short-term; long-term retention and behavior change not measured."
    - "Data security concerns were identified but not resolved by the app's design. [unacknowledged]"
    - "Financial insights comprehension was low for 14.3% of users, indicating visualization issues."
    - "No comparison against algorithmic baselines (e.g., rule-based vs ML) for anomaly detection. [unacknowledged]"
  mapping_rationale: "The paper was screened against all Odin functional domains. Strong relevance found for expense categorization (3.A, 3.B) due to automated fixed/variable distinction, anomaly detection (8.A) via unusual spending alerts, mobile UX (9.A, 9.B) through usability evaluation, evaluation frameworks (12.A) from structured Likert testing, and savings management (13.A) via personalized recommendations. Behavioral profiling (5.A-C) was rejected because no user clustering or cold-start profiling is performed. Spending forecasting (6.A-B) was rejected as no predictive modeling is used. Budget recommendation (7.A-C) was rejected because the app provides savings advice but not algorithmic budget allocation. Data privacy (10.A-B) and retention (11.A-B) were flagged as limitations but not contributions."
limitations:
  - "Small sample size (n=35) limits statistical power and generalizability."
  - "No longitudinal follow-up to assess sustained behavior change or retention."
  - "Financial insights comprehension was problematic for 14.3% of users, but no redesign was tested. [unacknowledged]"
  - "Data security confidence was low (31.4% somewhat disagreed), yet no encryption or privacy features were evaluated in depth. [unacknowledged]"
  - "The anomaly detection method is not specified algorithmically (e.g., statistical vs ML), limiting reproducibility. [unacknowledged]"
remember_this:
  - "82.8% of users found income and expense tracking reliable."
  - "74.3% reported improved financial management habits."
  - "Only 37.1% strongly agreed financial insights were easy to understand."
  - "Data security confidence was the lowest-rated dimension."
  - "77.1% rated navigation and data entry as very easy."
```