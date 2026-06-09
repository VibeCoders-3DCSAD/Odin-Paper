```yaml
paper_id: "10.1057/s41264-023-00234-8"
designation: "international"
title: "Impact of financial behaviour on financial well‑being: evidence among young adults in Malaysia"
authors: "Sabri, M. F.; Anthony, M.; Law, S. H.; Rahim, H. A.; Burhan, N. A. S.; Ithnin, M."
year: 2023
venue: "Journal of Financial Services Marketing"
odin_topics:
  - "1.C"
  - "5.A"
shorthand_tags:
  - "/fin-behavior"
  - "/fin-wellbeing"
  - "/young-adults"
tldr: "Financial behaviour fully mediates the relationship between financial literacy, financial socialisation, self-control, financial technology and financial well-being among young Malaysian adults during COVID-19."
problem_and_motivation: "Young adults in Malaysia faced income loss, debt, and housing issues during COVID-19, yet prior research on their financial well-being was mostly descriptive. The mediating role of financial behaviour between key determinants and well-being remained underexplored."
approach:
  - "Survey of 360 young Malaysians aged 18-29 using multi-stage random sampling from five regions."
  - "Structural equation modelling (SEM) with bootstrapping (1000 samples) to test mediation."
  - "Measures: financial literacy, financial behaviour, financial socialisation, self-control, financial technology, and financial well-being (CFPB scale)."
  - "Data collected via youth organisations in Penang, Johor, Terengganu, Selangor, and Sabah."
  - "Reliability: Cronbach's alpha 0.77-0.91; convergent validity (AVE >0.5) and discriminant validity established."
findings:
  - "num: Financial behaviour fully mediates the effect of financial literacy on financial well-being (indirect β=0.071, p<0.05)."
  - "num: Financial behaviour mediates the effect of financial socialisation (indirect β=0.19, p<0.05), self-control (β=0.05), and financial technology (β=0.01)."
  - "num: Financial behaviour has a direct positive effect on financial well-being (β=0.48, p<0.05)."
  - "Financial literacy alone has no direct effect on financial well-being (β=0.09, p>0.05)."
  - "Financial technology alone has no direct effect on financial well-being (β=-0.035, p>0.05)."
  - "num: R-squared: 74% of financial behaviour explained by predictors; 61% of financial well-being explained."
key_figures_tables:
  - "Figure 1: Research model showing financial behaviour as mediator → confirms mediation hypothesis."
  - "Table 7: Demographic profile shows 75% earn <RM1,500 monthly → highlights low-income sample."
  - "Figure 3: Structural model path coefficients → financial behaviour is strongest predictor (0.48)."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "FWB"
    definition: "Financial well-being"
  - term: "SEM"
    definition: "Structural equation modelling"
  - term: "CFA"
    definition: "Confirmatory factor analysis"
  - term: "AVE"
    definition: "Average variance extracted"
  - term: "CR"
    definition: "Composite reliability"
  - term: "Fintech"
    definition: "Financial technology"
critical_citations:
  - "[CFPB, 2015] — Defined financial well-being measurement scale."
  - "[Deacon & Firebaugh, 1988] — Systems theory foundation for financial behaviour."
  - "[Xiao et al., 2009] — Financial behaviour predicts well-being."
  - "[Lusardi & Mitchell, 2007] — Financial literacy and retirement savings."
relevance:
  topics:
    - code: "1.C"
      name: "Financial Behavior of Filipino Young Professionals"
      justification: "Provides empirical evidence on financial behaviour as mediator for young adults in Southeast Asia."
    - code: "5.A"
      name: "Financial Behavioral Profiles in Personal Finance"
      justification: "Identifies key antecedents (literacy, socialisation, self-control, fintech) that shape financial behaviour."
  contribution: "Odin's behavioral profiling module can incorporate financial behaviour as a mediating variable between user attributes (literacy, self-control) and financial well-being outcomes. The finding that financial literacy alone does not improve well-being without behaviour change justifies Odin's focus on actionable nudges rather than just education. Fintech's null direct effect but significant mediated effect suggests Odin's spending forecasting should integrate behavioural data to avoid misleading users. The structural equation modelling approach offers a template for evaluating Odin's own mediation hypotheses."
  directly_justifies:
    - "Financial behaviour fully mediates the effect of financial literacy on financial well-being."
    - "Financial technology alone does not improve financial well-being without positive financial behaviour."
    - "Self-control alone is not sufficient; financial behaviour is the key pathway."
    - "Young adults with better financial socialisation exhibit stronger financial behaviour and well-being."
  limits:
    - "Sample limited to Malaysia, not Philippines."
    - "Cross-sectional design cannot establish causality."
    - "Self-reported measures may bias financial well-being."
    - "Does not examine specific PFMS features or algorithms."
  mapping_rationale: "The paper does not directly address Odin's PFMS design but provides foundational evidence on financial behaviour's mediating role for young adults. I flagged domains: Behavioral profiling (5.A) because it models antecedents of financial behaviour, and Financial behavior of young professionals (1.C) as a comparable Southeast Asian demographic. I rejected codes for budgeting, anomaly detection, and system evaluation as the paper does not cover those. Borderline codes like savings/debt management (13.A/B) were excluded because the paper treats savings as part of behaviour without goal management specifics."
limitations:
  - "Sample only from Malaysia, limiting generalizability to Filipinos [unacknowledged]."
  - "Cross-sectional design prevents causal inference; paper acknowledges this."
  - "No objective financial data, only self-reports."
  - "Does not control for COVID-19 income impact heterogeneity."
remember_this:
  - "Financial behaviour fully mediates the link from literacy to well-being."
  - "Fintech alone does not improve well-being without behaviour change."
  - "Self-control matters only through actual financial actions."
  - "74% of financial behaviour variance explained by four factors."
```