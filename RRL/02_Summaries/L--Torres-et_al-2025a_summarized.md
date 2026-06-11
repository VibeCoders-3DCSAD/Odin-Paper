```yaml
paper_id: 10.1145/3785171.3785192
designation: local
title: Consumer's Financial Habits on Server-Based Electronic Money as It Affects Their Financial Behavior: Moderated By Monthly Transactions
authors: Torres, R. C.; Olaivar, G. M.; Britanico, S. I.
year: 2025
venue: The 9th International Conference on Business and Information Management (ICBIM2025), Bangkok, Thailand
odin_topics:
  - 1.C
  - 5.A
  - 11.A
shorthand_tags:
  - /filipino-young-professionals
  - /behavioral-profiles
  - /engagement-dynamics
tldr: Saving, spending, donating, and investing habits significantly influence financial behavior among GCash users in the Philippines, with monthly transaction frequency moderating only the spending-behavior relationship.
problem_and_motivation: The rapid adoption of e-wallets like GCash in the Philippines has transformed consumer payment behavior, but the specific financial habits (saving, spending, donating, investing, credit) driving overall financial behavior on these platforms remain underexplored. Understanding how transaction frequency moderates these relationships is critical for designing effective financial management tools and promoting responsible digital finance.
approach:
  - Quantitative survey of 300 purposively sampled Filipino GCash users aged 18-60.
  - Five financial habit predictors (saving, spending, donating, investing, credit/loan) measured via 5‑point Likert scales.
  - Multiple regression and moderation analysis using interaction term (spending × monthly transactions) grounded in Theory of Planned Behavior.
  - Diagnostic checks for multicollinearity (VIF 1.26–1.80), autocorrelation (Durbin‑Watson 1.73), and residual normality (Shapiro‑Wilk).
  - Model fit: R=0.633, R²=0.400, F(5,927)=39.6, p<0.001.
findings:
  - num: Investment habit had the strongest positive effect on financial behavior (β=0.243, p<0.001).
  - num: Saving (β=0.178), spending (β=0.115), and donating (β=0.144) habits also significantly influenced financial behavior (p≤0.003).
  - Credit/loan habit showed no significant effect (β=-0.003, p=0.955).
  - num: Monthly transaction frequency significantly moderated only the spending‑behavior relationship (β=-0.163, p<0.001).
  - At low and average transaction levels, spending habit had modest positive effects; the effect strengthened with higher transaction frequency.
  - The model explains 40% of variance in consumer financial behavior on GCash.
key_figures_tables:
  - "Table 1: Regression coefficients for five financial habits → Saving (β=0.178), Spending (β=0.115), Donating (β=0.144), Investing (β=0.243), Credit/Loan (non‑significant)."
  - "Figure 1: Conceptual framework integrating Theory of Planned Behavior → habits predict behavior, moderated by monthly transactions."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: SBEM
    definition: Server‑Based Electronic Money, digital wallets operating via centralized servers.
  - term: GCash
    definition: Leading Philippine mobile wallet with over 60 million registered users.
  - term: TPB
    definition: Theory of Planned Behavior, psychological framework linking attitudes, norms, and perceived control to intentions.
critical_citations:
  - "[Gomber et al., 2017] — Digital finance and FinTech transformation of consumer behavior."
  - "[Ma & Liu, 2004] — Technology Acceptance Model explaining perceived ease of use and usefulness."
  - "[Bosnjak et al., 2020] — Theory of Planned Behavior applications in financial contexts."
relevance:
  topics:
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      justification: Study samples Filipino GCash users and directly measures saving, spending, donating, investing, and credit behaviors.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      justification: Treats five distinct financial habits as behavioral profiles that collectively influence overall financial behavior.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      justification: Monthly transaction frequency is used as a moderator, revealing how usage intensity shapes habit‑behavior relationships.
  contribution: |
    The paper provides empirical evidence that four specific financial habits (saving, spending, donating, investing) directly impact overall financial behavior in a mobile wallet context, with investment habits having the strongest effect. For Odin's spending forecasting module (6.B), the finding that transaction frequency strengthens the spending‑behavior relationship can inform dynamic recalibration of user spending predictions. The non‑significant effect of credit/loan habits suggests that Odin's debt management module (13.B) may need separate treatment rather than being bundled with general spending habits. Additionally, the moderation result directly justifies incorporating usage frequency as an interaction term in behavioral models for user retention (11.B) and anomaly detection (8.A).
  directly_justifies:
    - "Monthly transaction frequency positively moderates the relationship between spending habits and overall financial behavior."
    - "Investment habits have a larger effect on financial behavior than saving or spending habits in digital wallet users."
    - "Credit and loan behaviors do not significantly influence financial behavior among GCash users."
  limits:
    - "Purposive sampling may limit generalizability to all Filipino young professionals."
    - "Cross‑sectional design cannot establish causality between habits and behavior. [unacknowledged]"
    - "Self‑reported Likert scales may introduce response bias. [unacknowledged]"
    - "Study focuses only on GCash, not other e‑wallets or bank digital services."
  mapping_rationale: |
    The paper was screened against Odin's functional domains. Behavioral profiling (5.A) applies because it measures five distinct habits as stable behavioral characteristics. Spending forecasting (6.A) is indirectly supported by the moderation finding that transaction frequency amplifies spending effects, though no prediction algorithm is tested. Budget recommendation (7.A) is not addressed. Anomaly detection (8.A) could use the baseline habit relationships, but the paper does not discuss outliers. Expense categorization (3.A) is absent. Mobile‑first design (9.A) is not a focus. Data privacy (10.A) is not covered. User retention (11.A) is relevant via engagement dynamics (monthly transaction frequency as a behavioral driver). Savings & debt management (13.A/B) are partially covered: saving and credit habits are measured, but goal management is not. Topic codes 1.C (Filipino young professionals) is selected because the sample is Filipino, aged 18‑60, overlapping with young professionals. Code 5.A is selected for profiling. Code 11.A is selected for engagement moderation. Codes 3.A, 7.A, 8.A, 10.A, 13.A/B were rejected due to absence of design or algorithmic contributions.
limitations:
  - "Cross‑sectional data; causal claims cannot be made. [unacknowledged]"
  - "Purposive sampling may introduce selection bias. [unacknowledged]"
  - "Self‑report measures subject to social desirability and recall bias. [unacknowledged]"
  - "Only GCash users; findings may not generalize to other digital finance platforms."
  - "Low R² (0.40) indicates substantial unexplained variance in financial behavior."
remember_this:
  - "Investment habits had the strongest impact on financial behavior (β=0.243)."
  - "Monthly transaction frequency intensifies the effect of spending habits on behavior."
  - "Credit and loan habits showed no significant influence among GCash users."
  - "Four of five financial habits significantly predict overall financial behavior."
```