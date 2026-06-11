```yaml
paper_id: 10.1145/3760557.3760578
designation: local
title: Understanding the Impulse Buying Behavior in the Digital Age: Influential Factors in Online Consumer Behavior
authors: Gabatin, R. A.; Sierra, S. M.; Maniago, M. G.; Capole, A.; Torres, R.
year: 2025
venue: 16th International Conference on E-business, Management and Economics (ICEME 2025)
odin_topics: []
shorthand_tags: []
tldr: Impulse buying in e-commerce is driven by social and website-related factors, with urgency mediating purchases, but direct effects of marketing and social factors are insignificant.
problem_and_motivation: Online impulse buying has intensified with e-commerce growth, yet the direct drivers remain unclear. Prior research shows conflicting results on the role of discounts and social influence. This gap motivates a systematic examination of social, marketing, website, and consumer factors in the Philippine digital market.
approach:
  - A quantitative survey collected data from 381 respondents in Cabuyao, Laguna, Philippines.
  - The Stimulus-Organism-Response (SOR) framework guides the analysis of social, marketing, website, consumer, and urgency variables.
  - Partial Least Squares Structural Equation Modeling (PLS-SEM) using WarpPLS 8.0 tests direct, mediating, and moderating effects.
  - Reliability and validity are assessed via composite reliability, Cronbach's alpha, AVE, and discriminant validity (Fornell-Larcker).
  - Hypotheses include 13 paths, with age and gender as moderators of the urgency-impulse relationship.
findings:
  - num: Social-related factors do not directly affect impulse buying (β=0.047, p=0.176).
  - num: Marketing-related factors do not directly affect impulse buying (β=0.064, p=0.104).
  - num: Urgency to buy has a large direct effect on impulse buying (β=0.804, p<0.001, f2=0.660).
  - num: Website-related factors affect urgency to buy (β=0.099, p=0.026) but not directly impulse buying (β=0.031, p=0.269).
  - num: Consumer characteristics affect urgency (β=0.562, p<0.001) and impulse buying (β=0.109, p=0.016).
  - num: The model explains 80.4% of variance (R2) in impulse buying.
  - Age and gender do not moderate the urgency-impulse buying relationship (p>0.05).
  - Consumer characteristics mediate the effect of marketing-related factors on impulse buying (β=0.452, p<0.001).
key_figures_tables:
  - Table 4: Path coefficients, standard errors, p-values, and effect sizes for direct and indirect hypotheses → Urgency has largest effect on impulse buying.
  - Figure 2: Final structural model excluding insignificant direct paths → Social and marketing factors only indirect via website usability and consumer characteristics.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: SOR
    definition: Stimulus-Organism-Response framework explaining how external stimuli influence internal states and behavioral outcomes.
  - term: PLS-SEM
    definition: Partial Least Squares Structural Equation Modeling, a variance-based method for complex cause-effect models.
  - term: eWOM
    definition: Electronic word of mouth, online peer recommendations and reviews.
critical_citations:
  - "[Cohen, 1988] — Provides power analysis thresholds for sample size calculation."
  - "[Beatty & Ferrell, 1998] — Foundational model of impulse buying precursors."
  - "[Khare & Pandey, 2017] — Links peer influence to consumer trust and purchase intent."
relevance:
  topics:
    - code: None
      name: None
      justification: contextual only
  contribution: The paper's findings on urgency as a mediator can inform Odin's spending forecasting module (6.A) by incorporating time-pressure cues. The identified role of website usability in impulse purchases justifies Odin's mobile-first design principles (9.A) to reduce friction. The insignificance of age and gender moderators suggests that Odin's behavioral profiling (5.A) should prioritize shopping lifestyle over demographics. The indirect effect of social factors via website quality supports Odin's expense categorization (3.A) by highlighting peer influence on spending patterns.
  directly_justifies:
    - Urgency to buy has a large effect (β=0.804) on impulse buying behavior.
    - Website-related factors significantly affect urgency to buy (β=0.099, p=0.026).
    - Consumer characteristics mediate the effect of marketing discounts on impulse buying.
    - Age and gender do not moderate the urgency-impulse buying relationship.
  limits:
    - Sample limited to one city (Cabuyao, Laguna), not nationally representative. [unacknowledged]
    - Purposive sampling may limit generalizability to all Filipino young professionals. [unacknowledged]
    - Cross-sectional design cannot establish causality between factors. [unacknowledged]
  mapping_rationale: The paper focuses on general impulse buying behavior in e-commerce, not specifically on personal finance management systems for Filipino young professionals. While it touches on financial behavior (e.g., income level, shopping lifestyle), it does not provide citeable claims for Odin's core modules such as expense categorization, budget recommendation, anomaly detection, or savings/debt management. The behavioral factors identified (urgency, website usability) are contextual but not directly applicable to PFMS algorithmic design. Therefore, no topic codes are selected; the paper is treated as contextual background only.
limitations:
  - Sample limited to Cabuyao, Laguna, not nationally representative. [unacknowledged]
  - Purposive sampling may introduce selection bias and limit generalizability. [unacknowledged]
  - Self-reported survey data subject to social desirability and recall bias. [unacknowledged]
  - Cross-sectional design prevents causal inference. [unacknowledged]
  - No control for confounding variables like digital literacy or prior experience. [unacknowledged]
remember_this:
  - Urgency explains 66% of variance in impulse buying.
  - Social and marketing factors only indirectly affect impulse buying.
  - Website usability drives urgency more than direct impulse triggers.
  - Shopping lifestyle mediates discount effects on impulse purchases.
```