```yaml
paper_id: f4e5d6c7-b8a9-4c2d-9e1f-3a4b5c6d7e8f
designation: local
title: ASSESSING THE FINANCIAL LITERACY OF SENIOR HIGH SCHOOL AND COLLEGE STUDENTS: A COMPREHENSIVE ANALYSIS
authors: Dela Rama, K. A.; Baylon, F.; Balwet, L. F.; Pullos, K. E.; Durias, R. C.; Cabusca, J. F.; Eguia, A. L.; Cabilin, L. M.; Duran, R.; Mante, J.; Prepecio, D.; Gilongos, C. J.; Rosel, M.
year: 2024
venue: The Threshold
odin_topics:
  - 1.A
  - 1.C
  - 5.A
  - 7.A
  - 13.A
  - 13.B
shorthand_tags:
  - /filipino-young-professionals
  - /financial-behavior
  - /behavioral-profile
  - /budgeting-strategy
  - /savings-goal
  - /debt-management
tldr: Senior high school and college students at a Philippine institution show basic financial knowledge but gaps in compound interest and investment, with moderate savings behavior and inconsistent budgeting.
problem_and_motivation: Financial literacy among young Filipino students is understudied, yet critical for economic stability. Existing research focuses on adults, leaving gaps in understanding formative financial development. Without targeted assessment, educational policies cannot address practical skill deficiencies.
approach:
  - Quantitative survey of 345 randomly stratified students at Colegio de San Francisco Javier during 2023-2024.
  - Adapted OECD/INFE questionnaire with 4-point Likert scale measuring financial knowledge and behavior (savings, budgeting, borrowing).
  - Data collected online; pilot study yielded Cronbach's alpha of 0.85.
  - Analysis used descriptive statistics, Welch's t-test, Pearson correlation, and Python libraries.
  - No algorithmic baselines or ML models; purely statistical comparison of demographic groups.
findings:
  - "num: Total weighted mean financial knowledge score 2.10 for SHS and 2.11 for college on a 4-point scale."
  - Less than 30% of respondents could accurately explain compound interest.
  - Budgeting practices are less consistent than saving behaviors; few students consider inflation in long-term planning.
  - No significant gender differences in financial literacy were found across any dimension.
  - Students are cautious about borrowing but lack understanding of interest rate impacts.
  - Family is the primary source of financial knowledge, not formal education.
key_figures_tables:
  - None.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: SHS
    definition: Senior High School
  - term: CSFJ
    definition: Colegio de San Francisco Javier
  - term: BSP
    definition: Bangko Sentral ng Pilipinas
  - term: APY
    definition: Annual Percentage Yield
  - term: OECD/INFE
    definition: Organisation for Economic Co-operation and Development / International Network on Financial Education
critical_citations:
  - "[Lusardi & Mitchell, 2014] — Foundational theory on financial literacy's economic importance."
  - "[OECD, 2016] — Defines financial literacy and role of schools."
  - "[Briones, 2021] — Establishes Philippine financial literacy context."
relevance:
  topics:
    - code: 1.A
      name: Filipino Young Professionals as a Demographic
      justification: "Studies SHS and college students, the immediate precursor demographic to young professionals."
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      justification: "Directly measures savings, budgeting, and borrowing behaviors of Filipino students."
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      justification: "Quantifies behavioral patterns (e.g., inconsistent budgeting) that inform profile construction."
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      justification: "Identifies gaps in consistent budget use, providing evidence for needed budgeting support."
    - code: 13.A
      name: Savings Goal Management in PFMS
      justification: "Reports students have savings goals but lack practical skills to achieve them."
    - code: 13.B
      name: Debt Management in PFMS
      justification: "Documents limited understanding of borrowing costs, critical for debt management modules."
  contribution: "The paper's assessment framework identifies specific financial knowledge gaps (compound interest, investment) and behavioral inconsistencies (budgeting) that Odin's budgeting recommendation and savings goal modules must address. Its finding that family rather than formal education drives financial literacy suggests Odin should incorporate family-oriented educational nudges. The absence of gender differences simplifies Odin's behavioral profiling, avoiding gender-specific calibration. The moderate savings behavior but poor budgeting justifies a module that automatically tracks and recommends budget adjustments. Finally, the low understanding of borrowing terms directly supports Odin's debt management feature to explain interest calculations."
  directly_justifies:
    - "Students demonstrate basic financial knowledge but struggle with compound interest and investment strategies."
    - "Budgeting practices are less consistent than saving behaviors among Filipino students."
    - "No significant gender differences in financial literacy exist in this sample."
    - "Family is the primary source of financial knowledge for young Filipinos."
    - "Less than 30% of students can explain compound interest."
  limits:
    - "Single institution sample limits generalizability to all Filipino young professionals."
    - "Cross-sectional design cannot track how financial literacy evolves with age or experience."
    - "Self-reported Likert responses may overstate actual financial behavior."
    - "No longitudinal validation of educational interventions proposed."
  mapping_rationale: "The paper falls under behavioral profiling (domain 5.A, 5.C) because it quantifies financial knowledge and behavior patterns, though no classification algorithm is presented. It also strongly supports budgeting (7.A) and savings/debt management (13.A, 13.B) via direct measurement of those behaviors. Demographic relevance (1.A, 1.C) is clear as the sample are students on the cusp of young professional life. Topics related to forecasting (6), anomaly detection (8), mobile design (9), privacy (10), retention (11), and system evaluation (12) are rejected because the paper does not address them. Spending forecasting is absent; the paper measures current knowledge, not future spending. Borderline case 5.B (profile dynamics) was rejected because no cold-start or temporal change is analyzed."
limitations:
  - "Sample limited to a single private institution in Mindanao; may not represent all Filipino students."
  - "Self-reported survey data subject to social desirability bias. [unacknowledged]"
  - "No validation of financial literacy measures against actual financial outcomes. [unacknowledged]"
  - "Cross-sectional design cannot assess causality between education and literacy."
remember_this:
  - "Only 30% of students can explain compound interest."
  - "No gender gap in financial literacy among this sample."
  - "Budgeting practices are less consistent than saving behaviors."
  - "Family is the primary source of financial knowledge for students."
  - "Students show basic knowledge but poor application of financial concepts."
```