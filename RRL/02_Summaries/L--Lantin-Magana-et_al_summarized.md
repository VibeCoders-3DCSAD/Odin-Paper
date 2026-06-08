```yaml
paper_id: b9c7a3d4-5e6f-4a7b-8c9d-0e1f2a3b4c5d
designation: local
title: Predictors of Investment Decision among Selected Individuals in Key Cities of Laguna: An Extended Theory of Planned Behavior Approach
authors: Lantin-Magana, L.; Espelita, C. A. M. H.; Calingasan-Habana, C. A.; Atento, A. G. B.; Atento, R. G. O.
year: 2026
venue: Journal of Enterprise Strategy and Management Innovation
odin_topics:
  - 5.A
shorthand_tags:
  - /financial-behavior-profiles
tldr: Investment decision among individuals in Laguna cities is associated with capital market knowledge and attitude toward investment, with attitude and monthly salary explaining 16.2% of variance.
problem_and_motivation: Investment participation in the Philippines remains limited, and decisions to invest are shaped not only by financial capacity but also by evaluative beliefs, risk appraisal, institutional trust, and perceived readiness. An exclusive focus on financial capacity is insufficient for explaining observed differences in investment participation and decision patterns.
approach:
  - A descriptive, cross-sectional online survey was administered to 483 respondents from Calamba, Santa Rosa, and Biñan, Laguna.
  - Constructs measured risk tolerance, attitude toward capital markets, capital market knowledge (financial literacy), government trust, attitude toward investment, and self-reported investment decision using a six-point scale.
  - Descriptive statistics, independent t-tests, ANOVA, Pearson correlations, and stepwise multiple regression were used for analysis.
findings:
  - num: Attitude toward investment (coefficient 0.345) and monthly salary (0.368) were significant predictors in stepwise regression, with R² = 0.162, p < .001.
  - num: Investment decision differed significantly by sex (p = .002) and monthly salary bracket (p < .001).
  - num: Capital market knowledge showed the highest correlation with investment decision (r = 0.210, p = .001), followed by attitude toward investment (r = 0.179, p = .003).
  - Risk tolerance received the highest mean rating (M = 4.81, SD = 1.19), while government trust received the lowest (M = 3.85, SD = 1.33).
key_figures_tables:
  - Table 1: Mean ratings of risk tolerance (4.81), attitude toward capital markets (4.60), capital market knowledge (4.10), government trust (3.85) → favorable risk attitudes but weaker institutional trust.
  - Table 2: Stepwise regression coefficients for attitude toward investment (0.345) and monthly salary (0.368) → both positively predict investment decision.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Theory of Planned Behavior
    definition: A framework emphasizing evaluative beliefs, perceived control, and social influences as determinants of behavioral intention.
  - term: Financial literacy
    definition: Knowledge and understanding of financial concepts and products that enable informed decision-making.
  - term: Risk tolerance
    definition: An individual's disposition or capacity to accept uncertainty and potential loss in investment contexts.
critical_citations:
  - "[Parsai & Chandok, 2025] — financial literacy impacts investment decisions."
  - "[Mahardhika & Zakiyah, 2020] — TPB predicts stock investment intention."
  - "[Espelita et al., 2025] — monetary policy awareness correlates with investment behavior."
relevance:
  topics:
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      justification: Paper examines predictors of investment decision using extended TPB, directly relevant to profiling user financial behavior.
  contribution: This paper provides evidence that attitude toward investment and monthly salary are significant predictors of investment decision, which can inform Odin's behavioral profiling module. The positive association between capital market knowledge and investment decision justifies incorporating financial literacy assessments into user models. The modest explained variance (16.2%) indicates that Odin's prediction systems should include additional behavioral and access-related variables beyond basic demographics and attitudes.
  directly_justifies:
    - Attitude toward investment predicts investment decision (coefficient 0.345).
    - Monthly salary predicts investment decision (coefficient 0.368).
    - Capital market knowledge correlates positively with investment decision (r = 0.210).
  limits:
    - Cross-sectional design prevents causal inference.
    - Purposive and online sampling limits generalizability to broader Philippine population.
    - Model explains only 16.2% of variance, suggesting omitted variables.
    - Stepwise regression may be sensitive to sample-specific patterns.
  mapping_rationale: The paper focuses on investment decision predictors among Filipino individuals, which directly relates to Odin's interest in understanding financial behavioral profiles (topic 5.A). It does not address spending forecasting, budget recommendation, anomaly detection, expense categorization, mobile design, data privacy, retention, system evaluation, or savings/debt management. The use of stepwise regression could be considered evaluation methodology, but the paper is not evaluating a PFMS system. Therefore only 5.A is selected.
limitations:
  - Cross-sectional design cannot establish causality.
  - Purposive and online sampling via Google Forms may exclude individuals with limited digital access. [unacknowledged]
  - Self-reported ratings may be influenced by social desirability or response styles.
  - Modest R² (0.162) indicates important determinants are missing from the model.
remember_this:
  - Attitude and salary explain 16.2% of investment decision variance.
  - Risk tolerance rated highest (4.81/6), government trust lowest (3.85/6).
  - Male respondents had higher investment decision scores than females.
  - Capital market knowledge shows modest positive correlation with investment decision.
```