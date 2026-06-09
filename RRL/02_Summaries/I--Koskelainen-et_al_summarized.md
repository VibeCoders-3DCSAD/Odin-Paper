```yaml
paper_id: 10.1111/joca.12510
designation: international
title: Financial literacy in the digital age — A research agenda
authors: Koskelainen, T.; Kalmi, P.; Scornavacca, E.; Vartiainen, T.
year: 2023
venue: Journal of Consumer Affairs
odin_topics:
  - 5.A
  - 10.A
  - 10.B
  - 13.A
  - 13.B
shorthand_tags:
  - /financial_behavior
  - /data_privacy
  - /user_trust
  - /savings_management
  - /debt_management
tldr: Digitalization transforms financial services and consumer behavior, requiring updated financial literacy to address new risks like data privacy and digital nudging.
problem_and_motivation: Digital finance offers convenience but also risks that traditional financial literacy does not cover. There is limited understanding of how digitalization affects financial literacy and capability. This gap motivated a systematic review to propose a research agenda.
approach:
  - Applied an integrative literature review to explore how digitalization affects financial literacy and capability.
  - Searched ProQuest, EBSCO, ACM Digital Library, and Google Scholar using terms like “financial literacy” AND “digital”.
  - Initial screening of 603 papers, narrowed to 29 peer-reviewed papers after excluding off-topic or analog-only studies.
  - Classified selected papers into three themes: Fintech, financial behavior in digital environments, and behavioral interventions.
  - Synthesized findings to propose a conceptual framework for digital financial literacy and capability.
findings:
  - “num: 80% of millennial smartphone owners use their device for transactional financial purposes.”
  - Smartphone apps that track spending and compare loan interest improve financial resilience after shocks.
  - Digital nudging via mobile apps can increase salience of credit card transactions and reduce spending.
  - Financial literacy helps mitigate the effect of mobile payment use on account overdrafts.
  - Digitalization creates risks including data confidentiality breaches, digital profiling, and algorithmic governance.
  - Digital nudging can be used both to improve financial well-being and to drive sales against consumer interests.
key_figures_tables:
  - "Figure 1: Conceptual description of financial literacy vs. financial capability → Financial capability adds opportunity to act."
  - "Figure 2: Conceptual description of digital financial literacy and capability → Digitalization affects knowledge, skills, and tools."
  - "Table 1: Research on digital financial literacy organized by Fintech, financial behavior, and behavioral interventions → Three core themes."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: Fintech
    definition: Technologically enabled financial innovation creating new business models, applications, or products.
  - term: Digital nudging
    definition: Influencing choices through algorithms and user-interface design in digital environments.
  - term: Financial capability
    definition: Broader than literacy, includes both ability and opportunity to act in financial markets.
  - term: DFS
    definition: Digital financial services such as online banking, mobile payments, and digital money.
  - term: Digital financial literacy
    definition: Traditional financial literacy complemented by digital literacy to manage digital finance risks.
critical_citations:
  - "[Lusardi & Mitchell, 2014] — Foundational financial literacy measurement and economic importance."
  - "[Thaler & Sunstein, 2008] — Origin of nudging concept used in behavioral interventions."
  - "[OECD, 2018] — Documents digital finance risks and need for updated financial education."
relevance:
  topics:
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      justification: Reviews how digital environments and nudging influence financial behavior.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      justification: Highlights risks of data breaches, digital profiling, and algorithm governance.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      justification: Discusses transparency, ethical concerns of nudging, and consumer vulnerability.
    - code: 13.A
      name: Savings Goal Management in PFMS
      justification: Mentions automatic savings tools and encouraging saving via mobile apps.
    - code: 13.B
      name: Debt Management in PFMS
      justification: Addresses over-indebtedness, digital debt collection, and easy credit access.
  contribution: "Odin's behavioral profiling module can integrate digital nudging findings to gently guide user spending without restricting choice. The paper’s emphasis on data privacy and digital profiling justifies adding explicit transparency features in Odin's design. For savings and debt management, the review supports building automated nudges (e.g., saving reminders) and spending salience tools. The framework also informs Odin’s evaluation metrics, such as measuring user resilience to financial shocks after using digital tools."
  directly_justifies:
    - "Digital payment methods increase spending due to loss of tangibility compared to cash."
    - "Smartphone apps that compare loan interest and track spending improve financial resilience."
    - "Digital nudging can reduce credit card spending by increasing transaction salience."
    - "Financial literacy mitigates the risk of account overdrafts from mobile payment use."
    - "Digital profiling and algorithmic governance pose privacy risks that PFMS must address."
  limits:
    - "Review only includes papers from finance, economics, and information systems journals; conference proceedings excluded."
  mapping_rationale: "The paper does not focus on Filipino young professionals (domains 1.A–2.C) or algorithmic modules (6–8). However, it directly informs behavioral profiling (5.A) through its review of digital financial behavior and nudging. Data privacy (10.A) and user trust (10.B) are central to its discussion of Fintech risks. Savings (13.A) and debt (13.B) appear in sections on automatic savings, over-indebtedness, and digital collection. Mobile-first design (9) is mentioned but not as a design principle, so omitted. No coverage of expense categorization (3), forecasting (6), budget recommendation (7), anomaly detection (8), retention (11), or evaluation frameworks (12)."
limitations:
  - "Only peer-reviewed journal articles from finance, economics, and IS disciplines were included."
  - "Conference proceedings, which may contain emerging technologies, were excluded. [unacknowledged]"
  - "The review may miss newer digital finance developments published after 2020."
remember_this:
  - "80% of millennials use smartphones for transactional financial tasks."
  - "Digital nudging can reduce credit card spending through salience."
  - "Loss of cash tangibility increases spending in digital payments."
  - "Financial literacy helps prevent overdrafts from mobile payments."
  - "Digital profiling and algorithmic governance raise privacy risks."
```