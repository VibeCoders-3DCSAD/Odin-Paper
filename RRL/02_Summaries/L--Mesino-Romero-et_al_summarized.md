```yaml
paper_id: b7e4c5d8-9a2f-4e3c-8b1d-6f7a9c2e5d3b
designation: local
title: From Surge to Stability: Digital Payments Driving a Steady Transition
authors: Mesina-Romero, B. R.; Masangkay, M. C.; Franco, M.; Yambao, M. A. V.; Delgado, K.; Bueno, P. N.; Lingat, P. J.; Natividad, G. M.; Lapus, A. R.; Manuel, R. M.; Yñigo, K. T.
year: 2024
venue: Bangko Sentral ng Pilipinas
odin_topics:
  - 1.C
  - 4.B
  - 10.A
  - 11.A
shorthand_tags:
  - /financial-behavior
  - /system-gaps
  - /data-privacy
  - /user-engagement
tldr: Digital payments accounted for 57.4% of monthly retail payment volume in the Philippines in 2024, up from 52.8% in 2023, driven by merchant, P2P, and B2B transactions.
problem_and_motivation: Despite growth in digital payments, adoption barriers such as high fees and limited digitalization of government collections (only 24.6% for P2G) persist. Understanding use-case dynamics helps prioritize interventions to achieve financial inclusion. The report measures progress against the Philippine Development Plan target of 52-54% digital share.
approach:
  - Identified 24 payment use-cases across government, business, and person categories using a 3x3 payment grid.
  - Estimated digital share using disaggregated quantitative data from sources like BIR, PSA, BSP, and stakeholder interviews.
  - Applied critical assumptions to fill data gaps where direct measurements were unavailable.
  - Computed monthly volume and value of digital and non-digital transactions for each use-case.
  - Compared year-on-year changes from 2013 to 2024 to track progress.
  - No baseline models or statistical tests were used; descriptive statistics only.
findings:
  - "num: Digital payments reached 57.4% of total monthly retail payment volume in 2024, exceeding the PDP target of 52-54%."
  - "num: Merchant payments comprised 66.4% of digital transaction volume, growing 29.1% year-on-year."
  - "num: P2P transfers increased from 19.3% to 20.6% of digital volume, with InstaPay volume rising 67.8%."
  - "num: B2B supplier payments grew 28.1% to 205.0 million transactions but only 6.2% of digital volume."
  - "num: Government disbursements are 97.2% digital, but person-to-government collections are only 24.6% digital."
  - High fees remain a significant barrier to widespread digital payment adoption.
key_figures_tables:
  - "Figure 1: Share of digital payments by volume from 2013 to 2024 → Increased from 1% to 57.4%"
  - "Table 1: Monthly volume by use-case → P2B merchant payments dominate at 3,301M total volume"
  - "Figure 2: Share of digital payments by value → 59.0% in 2024"
  - "Table 2: Digitalization rates by payment direction → G2X 97.2%, P2X 72.2%, B2X 19.8%"
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: BSP
    definition: Bangko Sentral ng Pilipinas, the central bank of the Philippines.
  - term: P2X
    definition: Person-to-X payments, where a person is the payer.
  - term: B2X
    definition: Business-to-X payments.
  - term: G2X
    definition: Government-to-X payments.
  - term: P2P
    definition: Person-to-person transfers.
  - term: P2B
    definition: Person-to-business payments, e.g., merchant payments.
  - term: B2B
    definition: Business-to-business payments, e.g., supplier payments.
  - term: QR Ph
    definition: National QR code standard for interoperable payments in the Philippines.
  - term: InstaPay
    definition: Real-time low-value electronic fund transfer system.
  - term: PESONet
    definition: Batch electronic fund transfer system for high-value payments.
critical_citations:
  - None.
relevance:
  topics:
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      justification: Provides digital payment adoption rates and use-case preferences of Filipino persons.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      justification: Identifies high fees as a barrier and low digitalization of P2G collections as gaps.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      justification: Discusses consumer redress mechanisms (Circular 1195) for electronic fund transfers.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      justification: Emphasizes moving from first-time adoption to sustained habitual use across payment needs.
  contribution: The report's finding that high fees deter adoption justifies Odin's commitment to no-hidden-fee transparency. The emphasis on merchant payments as the dominant use-case suggests Odin should prioritize seamless P2B expense tracking and categorization. The low digitalization of P2G collections (24.6%) indicates an opportunity for Odin to integrate bill payment reminders for government fees. The consumer redress circular supports Odin's design of clear transaction status notifications and dispute resolution workflows.
  directly_justifies:
    - High fees remain a significant barrier to widespread adoption of digital payments.
    - Digital payments account for 57.4% of retail transaction volume in the Philippines.
    - Moving beyond first-time adoption to sustained habitual use is a key goal.
    - Consumer trust requires timely resolution of electronic fund transfer issues.
  limits:
    - Does not distinguish behavior by age or income segment, limiting applicability to young professionals specifically.
    - No causality or predictive modeling; descriptive only.
    - Focuses on payment volume, not personal financial management outcomes.
    - Assumes digital payment adoption directly translates to financial health, which is not validated. [unacknowledged]
  mapping_rationale: The report was screened against Odin's functional domains. Behavioral profiling (5.A) rejected because no individual-level classification. Spending forecasting (6) rejected due to lack of predictive models. Budget recommendation (7) absent. Anomaly detection (8) not discussed. Mobile-first design (9) mentioned only in passing. Data privacy (10.A) selected due to consumer redress circular. User retention (11.A) selected due to discussion of habitual use. Expense categorization (3) not directly relevant. Savings/debt (13) absent. Financial behavior (1.C) selected as core macro behavior. System gaps (4.B) selected for barrier identification. Borderline case: 2.B seasonal patterns not present. Thus 1.C, 4.B, 10.A, 11.A.
limitations:
  - Estimates rely on critical assumptions for data gaps, which may introduce bias.
  - The measurement model does not capture informal economy payments.
  - No analysis of digital payment impact on household financial health. [unacknowledged]
  - Does not address security vulnerabilities beyond consumer redress. [unacknowledged]
remember_this:
  - 57.4% of retail payments are now digital.
  - Merchant payments drive 66.4% of digital volume.
  - High fees remain a key adoption barrier.
  - Government collections are only 24.6% digital.
```