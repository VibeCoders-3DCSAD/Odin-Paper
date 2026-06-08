```yaml
paper_id: 10.20944/preprints202504.2615.v1
designation: international
title: Development of a Platform for Financial Data Analysis and Adaptive Personal Finance Management
authors: Kaarov, A.; Esenalieva, G.
year: 2025
venue: Preprints.org
odin_topics:
  - 3.A
  - 7.B
  - 9.A
  - 9.B
  - 10.A
  - 13.A
shorthand_tags:
  - /expense-categorization
  - /budget-recommendation-ai
  - /cross-platform-mobile
  - /multilingual-ux
  - /data-security
  - /savings-goals
tldr: TYIYN is a multilingual mobile app using AI to provide adaptive budgeting, expense categorization, and cash flow estimation with a Flutter-Django stack.
problem_and_motivation: Many individuals lack intelligent tools to monitor expenses and receive context-appropriate financial advice, especially in developing economies. Financial ignorance and lack of guidance lead to poor spending, saving, and reactive budgeting. AI-powered finance apps can improve user outcomes through behavior-based recommendations.
approach:
  - The app uses Flutter for cross-platform frontend, Django REST Framework for backend API, and PostgreSQL for data storage.
  - AI algorithms provide personalized budget advice, expense categorization, and cash flow estimation using Pandas and Matplotlib for analysis.
  - Asynchronous tasks (notifications, sync) are handled by Celery and Redis.
  - Security includes SQL injection defenses, CSRF protection, token-based authentication, and Docker containerization.
  - Multilingual support for English, Russian, and Kyrgyz was implemented.
findings:
  - num: Users who followed AI recommendations increased average monthly savings by 12–18%.
  - num: 45% of users reduced discretionary spending on non-essential items.
  - num: Overspending prediction engine achieved approximately 85% precision.
  - num: API response times under 200 ms provided a responsive user experience.
  - num: 87% of non-English speaking users appreciated the Russian and Kyrgyz interfaces.
  - Expense classification on 100 test users over three months showed rent 35%, food 25%, transport 15%, entertainment 10%, miscellaneous 15%.
  - Over 60% of users spent disproportionately on discretionary or leisure expenditures; fewer than 40% consistently saved.
key_figures_tables:
  - None.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: FinTech
    definition: Financial technology, technology used to support or enable banking and financial services.
  - term: AI
    definition: Artificial intelligence, machine-based systems that can perform tasks typically requiring human intelligence.
  - term: MFA
    definition: Multi-factor authentication, a security method requiring two or more verification factors.
critical_citations:
  - "[Tversky & Kahneman, 1979] — Prospect theory foundation for behavioral finance."
  - "[Davis, 1989] — Technology Acceptance Model for user adoption."
  - "[Moniruzzaman & Akhand, 2020] — ML for budget optimization and expense prediction."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      justification: Paper classifies user spending into categories like food, transport, entertainment.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      justification: AI provides personalized budget advice and savings recommendations.
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      justification: App built with Flutter for cross-platform mobile delivery.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      justification: Multilingual support and interactive dashboards enhance usability.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      justification: Implements MFA, encryption, token authentication, and CSRF protection.
    - code: 13.A
      name: Savings Goal Management in PFMS
      justification: Tracks savings increases and encourages goal-oriented behavior.
  contribution: TYIYN demonstrates how integrating AI recommendation engines with interactive data visualizations can improve user savings and reduce discretionary spending. The paper validates that multilingual mobile design significantly boosts accessibility and trust among non-English speakers. It also shows that robust security features (MFA, encryption) are prerequisites for user adoption in FinTech.
  directly_justifies:
    - "AI-driven personalized financial advice increases average monthly savings by 12–18%."
    - "Multilingual support improves usability for 87% of non-English speaking users."
    - "Interactive dashboards lead to more frequent engagement than static reports."
  limits:
    - "No integration with banking APIs; users must manually enter transactions."
    - "Recommendation engine required real-world interaction data to reduce false positives [unacknowledged]."
    - "Simulated dataset of only 100 test users over three months; generalizability unclear [unacknowledged]."
  mapping_rationale: The paper focuses on expense categorization (3.A), AI-based budget recommendations (7.B), mobile-first design (9.A), UX with multilingual support (9.B), data security (10.A), and savings management (13.A). No behavioral profiling (5.A), spending forecasting algorithm (6.B), anomaly detection (8.A), or retention mechanisms (11.B) are detailed. Borderline cases like 2.B (seasonal spending) are mentioned anecdotally but not central.
limitations:
  - "Manual transaction entry creates user adoption friction."
  - "Lacks direct banking integration, planned for future using open banking APIs."
  - "Initial recommendation engine performance required real-world data to improve [unacknowledged]."
remember_this:
  - "AI recommendations increased savings by 12-18% for active users."
  - "Multilingual support boosted usability for 87% of non-English speakers."
  - "Interactive dashboards drive more frequent financial engagement."
  - "Security features like MFA are essential for user trust in FinTech."
```