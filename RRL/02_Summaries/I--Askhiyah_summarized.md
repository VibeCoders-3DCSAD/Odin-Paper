```yaml
paper_id: 10.59784/journaljoae.v1i1.37
designation: international
title: Digital Finance Usage and Its Impact on Consumer Economic Behavior Based on National Data
authors: Askhiyah, U. M.
year: 2026
venue: Journal of Applied Econometric
odin_topics:
  - 1.C
  - 5.A
  - 7.A
  - 13.A
  - 13.B
shorthand_tags:
  - /financial-behavior
  - /behavioral-profiles
  - /budgeting-strategies
  - /savings-goal-management
  - /debt-management
tldr: Digital finance adoption increases household consumption by 8.7% and financial literacy by 1.4 points but reduces savings balances by 5.8% and raises debt-to-income ratios, with heterogeneous effects by age and income.
problem_and_motivation: The comprehensive impact of digital finance on consumer economic behavior remains inadequately understood despite widespread adoption. Existing research produces mixed findings on whether digital finance promotes prudent behavior or encourages overconsumption and overindebtedness. Robust causal evidence using nationally representative data is needed to inform policy and mitigate risks for vulnerable populations.
approach:
  - Data from 45,678 households in a national survey with stratified random sampling.
  - Propensity score matching with kernel and radius algorithms to control selection bias.
  - Instrumental variable estimation using regional digital infrastructure density as instrument.
  - Panel fixed effects models for subsample with longitudinal observations (8,234 households).
  - Outcomes include consumption expenditure, savings balances, debt-to-income ratios, financial literacy scores, and planning behaviors.
findings:
  - "num: Digital finance users show 8.7% higher consumption expenditure (ATT=742k Rupiah, p<0.001)."
  - "num: Savings balances are 5.8% lower for digital finance users despite higher formal savings account ownership."
  - "num: Financial literacy scores increase by 1.4 points (on 10-point scale) post-adoption."
  - "num: Debt-to-income ratio is 6.4 percentage points higher for digital finance users (34.7% vs 28.3%)."
  - "num: Late payment rate is 6.3 percentage points higher among digital finance users (14.7% vs 8.4%)."
  - Digital finance users are 3.5 times more likely to use financial planning tools and 2.4 times more likely to have explicit financial goals.
  - Heterogeneous effects: strongest consumption increase in middle-income households (10-12%) and young adults (13.6%).
key_figures_tables:
  - "Table 1: Demographic comparison of digital finance users vs non-users → Users younger, more educated, urban."
  - "Table 2: Impact on consumption by category → Largest increases in discretionary goods (14-18%)."
  - "Table 3: Savings behavior and financial management → Users have higher budgeting but lower balances."
  - "Table 4: Digital credit utilization → Higher debt burden and late payments, especially for young lower-middle-income."
  - "Table 5: Financial literacy and wellbeing → Literacy +1.4 points, financial wellbeing index +8.5 points."
  - "Figure 2: Heterogeneous consumption effects → Young and middle-income households show largest gains."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: Digital finance usage intensity index
    definition: Multidimensional score (0-100) reflecting breadth and depth of engagement across mobile banking, payments, e-wallets, digital credit.
  - term: PSM
    definition: Propensity score matching, a method to reduce selection bias by matching treatment and control groups on observable characteristics.
  - term: IV estimation
    definition: Instrumental variable estimation using regional digital infrastructure density to address endogeneity.
  - term: ATT
    definition: Average Treatment Effect on the Treated, the causal impact for those who adopted digital finance.
critical_citations:
  - "[Li et al., 2020] — Documented 7-9% consumption increase from mobile payments."
  - "[Batista & Vicente, 2020] — Found positive mobile money effect on savings in Africa."
  - "[Danisman & Tarazi, 2020] — Raised concerns about digital credit expansion risks."
  - "[See-To & Ngai, 2019] — Showed digital payments reduce pain of paying."
  - "[Banna & Alam, 2021] — Linked digital finance to banking stability in ASEAN."
relevance:
  topics:
    - code: 1.C
      name: Financial Behavior of Filipino Young Professionals
      justification: Paper analyzes consumption, savings, debt, and literacy changes due to digital finance.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      justification: Heterogeneous effects across age, income, and location support need for behavioral profiling.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      justification: Digital finance users show 51.8% budget creation vs 32.4% non-users, informing budget recommendation.
    - code: 13.A
      name: Savings Goal Management in PFMS
      justification: Documents autosave feature usage (28.5%) and goal-based saving (47.3%) among digital finance users.
    - code: 13.B
      name: Debt Management in PFMS
      justification: Provides evidence on debt-to-income ratios (34.7%), late payments (14.7%), and overleveraging risks.
  contribution: This paper provides empirical evidence that digital finance adoption increases consumption expenditure by 8.7% and financial literacy scores by 1.4 points, which can inform Odin's spending forecasting and behavioral profiling modules. The documented reduction in savings balances (5.8%) and increase in debt-to-income ratios (6.4 percentage points) directly supports Odin's savings goal management and debt management modules with quantitative benchmarks. The heterogeneity analysis identifying young lower-middle-income households as vulnerable guides targeted anomaly detection and user retention strategies. The finding that digital finance users are 3.5 times more likely to use planning tools justifies integrating budgeting and planning features into Odin's mobile-first design.
  directly_justifies:
    - Digital finance adoption increases household consumption by 8.7% compared to non-users.
    - Digital finance users have 5.8% lower savings balances despite higher financial inclusion.
    - Financial literacy scores improve by 1.4 points after digital finance adoption.
    - Young lower-middle-income households face highest debt service ratios and late payment risks.
    - Autosave features increase structured saving behavior, with 28.5% of users adopting them.
  limits:
    - Observational data with potential residual confounding despite multiple identification strategies.
    - Short-term horizon (maximum 24 months post-adoption) limits long-term impact assessment.
    - No measurement of individual psychological factors like self-control or risk preferences.
    - Single country context (Indonesia) may limit generalizability to other populations.
  mapping_rationale: The paper was screened against Odin's functional domains. It directly addresses financial behavior (domain Behavioral profiling) via heterogeneous consumption and savings patterns, thus selecting 1.C and 5.A. It provides citeable claims on budgeting behavior (domain Budget recommendation), selecting 7.A. It extensively covers savings goals and debt management (domains Savings & debt management), selecting 13.A and 13.B. Topics related to expense categorization, anomaly detection, mobile design, data privacy, retention, and system evaluation were rejected as the paper does not address these. Borderline case: spending forecasting (6.A) was rejected because the paper does not propose a forecasting model but rather estimates average treatment effects. The selected topics capture the paper's core contributions to PFMS design.
limitations:
  - "Cross-sectional and short-term panel data (max 24 months) cannot assess long-term wealth effects. [unacknowledged]"
  - Self-reported survey data may introduce recall and social desirability bias.
  - No direct measurement of impulse spending or self-control mechanisms.
  - Findings may not generalize beyond Indonesian context due to cultural and economic differences.
remember_this:
  - Digital finance increases consumption by 8.7% but reduces savings by 5.8%.
  - Financial literacy improves by 1.4 points after digital finance adoption.
  - Young lower-middle-income users face highest debt and late payment risks.
  - Autosave features boost structured saving behavior by 25 percentage points.
  - Digital finance users are 3.5 times more likely to use planning tools.
```