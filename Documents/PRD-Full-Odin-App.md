# Full Odin App PRD

## Problem Statement

Filipino young professionals in Metro Manila need a budgeting system that reflects how they actually receive, spend, and allocate money. Existing tools are often generic expense trackers: they help record past spending, but they do not adequately support variable income, fixed obligations, family and community contributions, protected expense categories, culturally cyclical spending, savings goals, debt pressure, or forward-looking budget guidance.

The target user needs a mobile-first and web-accessible personal budget management system that turns manual transaction logging into useful guidance. The system must help users understand their cash position, classify their financial behavior, forecast likely spending, detect unusual or risky transactions, recommend budget allocations, track savings goals, and manage debt repayment strategies.

The research team also needs the app to support thesis evaluation. Odin must be structured so its user-facing modules, data flows, model outputs, and quality attributes can be tested through functional test cases, model evaluation metrics, ISO 25010 quality characteristics, and SUS-based usability evaluation.

## Solution

Build Odin as a mobile-first personal budget management application with web access. The app will provide a guided onboarding flow, classify users into one of four financial behavioral profiles, let users manually record income, expenses, transfers, and recurring transactions, organize spending through a Filipino-context category taxonomy, generate profile-aware budget recommendations, show spending forecasts, detect anomalous or risky spending behavior, track savings goals, and guide debt repayment using Avalanche and Snowball strategies.

Odin should behave as a decision-support tool, not a licensed financial adviser. The app should explain recommendations and alerts in plain user-facing language, preserve user control over final decisions, and avoid shaming users for culturally or personally necessary expenses.

Confirmed primary screens:

1. Login / Register
2. Onboarding questionnaire
3. Profile result / financial behavioral profile
4. Dashboard / overview
5. Add transaction
6. Transactions list / history
7. Recurring transactions
8. Categories / category settings
9. Budget setup
10. Budget recommendation
11. Forecast dashboard
12. Alerts / anomaly review
13. Savings goals
14. Debt accounts
15. Reports / analytics
16. Settings / privacy / account

## User Stories

1. As a new user, I want to create an account, so that my financial records are stored under my own profile.
2. As a returning user, I want to log in securely, so that other people cannot access my financial data.
3. As a privacy-conscious user, I want to understand what data Odin collects before onboarding, so that I can decide whether to proceed.
4. As a first-time user, I want a guided onboarding walkthrough, so that I understand the main features without reading a manual.
5. As a first-time user, I want to enter my income type, so that Odin can understand whether my income is stable, variable, or mixed.
6. As a first-time user, I want to enter my income frequency, so that Odin can align budgets and forecasts to my real pay cycle.
7. As a first-time user, I want to declare fixed obligations, so that Odin can distinguish unavoidable payments from flexible spending.
8. As a first-time user, I want to declare financial dependents or family support obligations, so that Odin can account for Filipino household responsibilities.
9. As a first-time user, I want to mark important expense categories as protected, so that Odin does not recommend reducing non-negotiable spending.
10. As a first-time user, I want Odin to assign a financial behavioral profile, so that my budget guidance is personalized.
11. As a user, I want to see why I was assigned a profile, so that I can trust the profile result.
12. As a user, I want to override or request a reassessment of my profile, so that the system does not trap me in an inaccurate classification.
13. As a user whose income or obligations change, I want Odin to detect sustained behavior changes, so that my profile can adapt over time.
14. As a user, I want to confirm profile changes before they take effect, so that I retain control over my financial identity in the app.
15. As a user, I want to add an income transaction quickly, so that my available balance stays accurate.
16. As a user, I want to add an expense transaction quickly, so that manual logging is not too much work.
17. As a user, I want to add a transfer transaction, so that moving money between accounts does not distort my income or expense totals.
18. As a user, I want to select a clear expense category when adding a transaction, so that my reports and forecasts are meaningful.
19. As a user, I want category suggestions or smart defaults, so that transaction entry takes less effort.
20. As a user, I want to edit transactions, so that I can correct mistakes after logging.
21. As a user, I want to delete transactions, so that accidental entries do not affect my budget.
22. As a user, I want to search and filter transaction history, so that I can review specific expenses.
23. As a user, I want to view transactions by date range, so that I can inspect weekly, semi-monthly, or monthly behavior.
24. As a user, I want to create recurring income transactions, so that salary or regular income can be logged automatically.
25. As a user, I want to create recurring expense transactions, so that rent, subscriptions, bills, and contributions are not forgotten.
26. As a user, I want reminders for recurring transactions before they post, so that I can prepare for upcoming obligations.
27. As a user, I want to pause or stop recurring transactions, so that the app reflects changes in my real obligations.
28. As a user, I want expense categories that include Filipino-specific obligations, so that family support, paluwagan, community contributions, and government contributions are not hidden under generic labels.
29. As a user, I want categories grouped into broad financial buckets, so that I can understand essentials, obligatory spending, discretionary spending, and financial allocation at a glance.
30. As a user, I want to customize category labels where appropriate, so that the system matches my lived financial language.
31. As a user, I want Odin to prevent category ambiguity where possible, so that I do not abandon logging because categories are confusing.
32. As a user, I want a dashboard showing current balance, budget status, recent transactions, alerts, goals, and forecast highlights, so that I can understand my finances quickly.
33. As a user, I want dashboard cards to focus on the most urgent items, so that I know what needs action today.
34. As a user, I want to see spending by category, so that I can identify where my money is going.
35. As a user, I want to see spending by budget period, so that I can compare actual spending against my plan.
36. As a user, I want to set a budget period, so that my plan matches how I receive and spend money.
37. As a user, I want to set total budget size, so that Odin knows how much money can be allocated.
38. As a user, I want to set per-category allocations, so that my plan has practical spending limits.
39. As a user, I want to mark budget categories as protected, so that Odin respects essential or culturally required expenses.
40. As a user, I want Odin to recommend a budget allocation, so that I have a starting point instead of building a plan from scratch.
41. As a user, I want budget recommendations to use my profile and forecasts, so that they fit my actual income and spending behavior.
42. As a user, I want Odin to explain budget recommendations, so that I understand why money is being allocated a certain way.
43. As a user, I want to accept, modify, or reject budget recommendations, so that I remain in control.
44. As a user, I want surplus handling options, so that leftover budget can be carried forward, reallocated, or saved.
45. As a user, I want deficit warnings, so that I can respond before overspending gets worse.
46. As a user, I want spending forecasts for upcoming periods, so that I can plan before expenses happen.
47. As a user, I want forecasts by category, so that I can prepare for specific spending pressure.
48. As a user, I want total forecast views, so that I can understand the overall direction of my spending.
49. As a user, I want a next-month forecast graph with Essentials, Discretionary, Financial Allocation, and Obligatory lines, so that I can compare upcoming spending pressure across the main budget groups.
50. As a new user, I want a cold-start forecast based on profile and population baselines, so that the app is useful before I have enough personal history.
51. As a user, I want the app to clearly label cold-start forecasts, so that I do not mistake population estimates for personalized predictions.
52. As a user, I want forecasts to account for paydays and calendar cycles, so that normal payday or holiday effects are not treated as surprises.
53. As a user, I want forecasts to improve as I log more transactions, so that the app becomes more personalized over time.
54. As a user, I want alerts when spending is unusually high for a category, so that I can correct behavior early.
55. As a user, I want alerts when I am likely to exceed a budget, so that I can adjust before the period ends.
56. As a user, I want anomaly alerts to explain the reason, so that I know whether the alert is useful.
57. As a user, I want to mark an unusual transaction as intentional, so that the same kind of planned spending is not repeatedly flagged.
58. As a user, I want culturally expected spending events to be handled carefully, so that Christmas, enrollment, family support, paluwagan, or community contributions do not create misleading alerts.
59. As a user, I want alert frequency controls, so that I do not ignore Odin because it notifies me too often.
60. As a user, I want savings goals with target amounts and dates, so that I can track progress toward emergency funds or major purchases.
61. As a user, I want to link contributions to savings goals, so that progress updates automatically.
62. As a user, I want to see whether a savings goal is on track, behind, or achieved, so that I know whether to adjust.
63. As a user, I want projected goal completion dates, so that I understand how current saving behavior affects my timeline.
64. As a user with multiple goals, I want to prioritize goals, so that Odin can recommend allocations in the right order.
65. As a user, I want to create debt accounts, so that I can track repayment obligations separately from ordinary expenses.
66. As a user, I want to enter debt interest rates and minimum payments, so that repayment projections are realistic.
67. As a user, I want to compare Avalanche and Snowball repayment strategies, so that I can choose the strategy that fits my needs.
68. As a user, I want projected payoff dates, so that I know when I may become debt-free.
69. As a user, I want to switch debt payoff strategy, so that I can adjust when my priorities change.
70. As a user, I want reports and analytics by week, month, and custom date range, so that I can review my financial behavior.
71. As a user, I want reports that compare planned budget, actual spending, and forecasted spending, so that I can see whether my plan is realistic.
72. As a user, I want reports on protected categories and obligations, so that I understand how much of my money is non-negotiable.
73. As a user, I want progress reports for savings and debt, so that I can see long-term outcomes.
74. As a user, I want notification preferences, so that I can choose how Odin contacts me.
75. As a user, I want privacy settings, so that I can manage consent and data usage.
76. As a user, I want to export or review my data, so that I retain access to my own financial records.
77. As a user, I want to delete my account and data, so that I can exercise control over sensitive information.
78. As a mobile user, I want transaction entry to work well on a small screen, so that I can log expenses immediately.
79. As a mobile user, I want the dashboard to be glanceable, so that I can check finances quickly.
80. As a mobile user with intermittent connectivity, I want draft or offline-tolerant transaction entry, so that a poor connection does not prevent logging.
81. As a web user, I want wider reports and analytics views, so that I can review finances more comfortably on a larger screen.
82. As a thesis evaluator, I want the app's modules to be testable through functional scenarios, so that the system can be evaluated rigorously.
83. As a thesis evaluator, I want model outputs to be measurable with defined metrics, so that the intelligent modules can be assessed separately from the UI.
84. As a thesis evaluator, I want usability evaluation through SUS, so that user experience can be measured consistently.
85. As a thesis evaluator, I want ISO 25010 quality characteristics mapped to app behavior, so that functional suitability, usability, performance efficiency, security, reliability, and portability can be evaluated.

## Implementation Decisions

- Build Odin as a mobile-first application with web access. Mobile is the primary UX target; web should support the same core workflows with more room for analysis and reporting.
- Treat the confirmed screens as the first route map for the full app.
- Use a shared domain model across mobile and web so transaction, budget, forecast, profile, alert, savings, and debt concepts do not diverge between platforms.
- Create a transaction ledger module as a deep module. It should expose a simple interface for income, expense, transfer, recurring transactions, edits, deletes, category assignment, and date-range queries while hiding ledger invariants.
- Create a category taxonomy module as a deep module. It should define detailed categories, broad forecast categories, protected/default categories, Filipino-specific obligations, and mapping rules.
- Create a financial behavioral profile module as a deep module. It should classify users into one of four profiles, store explanation data, support reassessment, and handle user confirmation before profile changes.
- Create a budget recommendation module as a deep module. It should consume current balance, profile, protected categories, goals, obligations, and forecast outputs, then return explainable category allocations.
- Create a forecasting module as a deep module. It should support cold-start forecasts, personalized forecasts, total forecasts, per-category forecasts, and metadata explaining whether the result is personalized or fallback-based.
- The primary forecast visualization should include a next-month multi-line graph for Essentials, Discretionary, Financial Allocation, and Obligatory spending.
- Create an anomaly and overspending detection module as a deep module. It should detect unusual transaction behavior, budget-risk conditions, culturally expected exceptions, and user-whitelisted intentional outliers.
- Create a savings goal module as a deep module. It should manage goals, contributions, progress states, prioritization, and projected achievement dates.
- Create a debt management module as a deep module. It should manage debt accounts and compute Avalanche and Snowball repayment projections.
- Create an alerts and notifications module as a deep module. It should centralize alert generation, acknowledgement, notification preferences, cooldown behavior, and alert fatigue controls.
- Create a reporting module as a deep module. It should produce date-range summaries, category breakdowns, budget-vs-actual reports, forecast-vs-actual comparisons, savings progress, debt progress, and obligation/protected-category summaries.
- Profile classification, forecasting, anomaly detection, and recommendation outputs must include explanation fields suitable for user-facing display.
- The data model must store detailed raw transactions first, then derive model-specific datasets from raw transaction history.
- Broad forecast categories should include Essentials, Obligatory, Discretionary, and Financial Allocation.
- Detailed categories should support Filipino-context categories, including family support, remittances, paluwagan, church or religious donations, barangay or community collections, government contributions, debt payments, insurance, emergency fund, savings, and investments.
- Protected categories must be supported. Defaults should include essentials, debt and loan repayments, insurance, and emergency fund contributions, while allowing user-declared protected categories.
- Budget recommendation must not suggest reducing protected categories unless the user explicitly changes protection settings.
- The app must distinguish advisory guidance from financial advice through clear in-app disclaimers.
- No bank or e-wallet integration will be required for the first full-app PRD. All transaction capture is manual or recurring-template based.
- No OCR receipt scanning will be required for the first full-app PRD.
- No investment portfolio tracking will be required for the first full-app PRD.
- No multi-currency support will be required for the first full-app PRD.
- Authentication, consent, account management, and privacy controls are part of the app, even though they are not the thesis's main research contribution.
- The system should support RA 10173-aligned privacy expectations: consent, data minimization, secure handling, access, correction, and deletion.
- The implementation should preserve separation between user-facing UI, domain logic, persistence, and model-serving boundaries.
- The model architecture decision needs final alignment. Current repository materials support Random Forest for profile classification, LSTM for forecasting, and Isolation Forest for anomaly detection, while some internal framing suggests a simplified LSTM-centered design. This PRD treats the three-model version as the full-app target unless the team formally revises the thesis scope.

## Testing Decisions

- Tests should verify external behavior and user-visible outcomes, not internal implementation details.
- Transaction ledger tests should cover creating, editing, deleting, filtering, recurring generation, transfer handling, and balance effects.
- Category taxonomy tests should cover detailed-to-broad mappings, protected-category defaults, Filipino-context categories, and category validation.
- Profile module tests should cover initial classification, explanation generation, reclassification triggers, and user confirmation behavior.
- Budget recommendation tests should cover protected categories, profile-specific allocations, surplus behavior, deficit behavior, recommendation explanations, and user overrides.
- Forecasting tests should cover cold-start fallback, personalized-forecast availability, forecast metadata, per-category outputs, total outputs, and forecast consumption by dashboard and budget modules.
- Forecasting UI tests should verify that the next-month graph renders all four broad-category lines and remains readable on mobile.
- Anomaly detection tests should cover high category deviation, high income-ratio spending, recurring-payment suppression, user whitelisting, culturally expected exception behavior, and alert explanation output.
- Savings goal tests should cover goal creation, contributions, progress states, target-date projections, prioritization, and completion behavior.
- Debt management tests should cover debt account creation, minimum payments, Avalanche order, Snowball order, projected payoff dates, and strategy switching.
- Alerts tests should cover alert creation, acknowledgement, cooldowns, notification preferences, grouped alerts, and suppression rules.
- Reporting tests should cover budget-vs-actual, forecast-vs-actual, category summaries, date filters, savings progress, and debt progress.
- Authentication and privacy tests should cover login, logout, protected routes, consent state, account deletion flow, and sensitive-data access rules.
- Mobile-first UI tests should cover core workflows on narrow viewports: onboarding, add transaction, dashboard, budget recommendation, forecast, alerts, savings, debt, and settings.
- Web UI tests should cover dashboard, reports, transactions, budget, forecast, savings, debt, and settings on larger viewports.
- Integration tests should cover the main data flow: onboarding to profile, profile to transaction logging, transactions to forecasts, forecasts to budget recommendation, transactions to anomaly alerts, and alerts to user feedback.
- Model evaluation should be separate from UI tests. Forecasting should be evaluated using time-series-appropriate metrics such as MAE, RMSE, and related forecast-error measures. Anomaly detection should be evaluated using precision, recall, and F1-score. Profile classification should be evaluated using classification metrics if the classifier remains in scope.
- Usability evaluation should use SUS for the complete user-facing app.
- Software quality evaluation should map ISO 25010 characteristics to concrete testable criteria.

## Out of Scope

- Bank API integration.
- E-wallet API integration.
- OCR or receipt scanning.
- Automatic transaction import.
- Investment portfolio management.
- Multi-currency support.
- Licensed financial advice, investment advice, retirement planning, or legal/tax advice.
- Users outside the Filipino young professional target demographic.
- Geographic generalization beyond Metro Manila for the thesis scope.
- Full production-grade fraud detection.
- Merchant-level enrichment from third-party providers.
- Social or gamified features unless separately approved.
- Admin dashboards for banks, institutions, or financial advisers.
- Public marketplace deployment requirements beyond what is needed for thesis evaluation.

## Further Notes

- The PRD is based on the full-app scope confirmed by the repository materials and the accepted screen list.
- The app should be framed as a personal budget management system and decision-support tool.
- The strongest product thesis is that Odin is not merely a tracker: it turns consistent manual logging into forecasted, profile-aware, culturally grounded budget guidance.
- The strongest unresolved architecture issue is algorithm scope. The team should explicitly decide whether the final thesis implementation uses Random Forest, LSTM, and Isolation Forest, or narrows the intelligent component to LSTM with deterministic support modules.
- The strongest UX risk is manual logging fatigue. The app must make transaction entry fast, visible, and rewarding through immediate dashboard, forecast, alert, and recommendation value.
- The strongest trust risk is sensitive financial data. The app must explain data usage, protect data, and make intelligent outputs understandable.
