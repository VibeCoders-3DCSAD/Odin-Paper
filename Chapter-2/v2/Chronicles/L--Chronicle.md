## Source: `1.A/L--Albert_et-al_2025_summarized.md`

**Title:** Gender Equality, Disability, and Social Inclusion in the Philippines: Progress, Challenges, and Opportunities in SDG 5 and SDG 10

### TL;DR

Despite robust legal frameworks, persistent intersectional inequalities in income, disability, and ethnicity undermine inclusive development in the Philippines, with gender gaps in labor force participation and education-linked disability rates remaining severe.

### Findings

1. Income inequality improved: Gini coefficient decreased from 0.453 (2015) to **0.406 (2023)**; bottom 40% income growth (10.6%) exceeded national average (8.6%) in 2023.
2. **Women's labor force participation remains stuck at ~50% vs. 74% for men** — a persistent 24-point gap; married women citing housework as reason for not working reached 90% in 2023.
3. Disability prevalence is 15% among females vs. 9% among males; severe disability reaches 55% among women with no formal education (vs. 23% for men).
4. Teenage pregnancy dropped from 8.6% (2017) to 5.4% (2022), but rates among poorest quintile (10.3%) are six times higher than richest (1.8%).
5. Indigenous Peoples (8.7% of population) face compound exclusion: 37% live in Geographically Isolated and Disadvantaged Areas; indigenous women's unpaid family work is three times higher than non-indigenous counterparts.

### Relevance to Odin

**Topics:**

1.A — Filipino Young Professionals as a Demographic

1.B — Financial Structure of Filipino Young Professionals

1.C — Financial Behavior of Filipino Young Professionals

**Contribution to Odin:**

This paper provides essential baseline data on Filipino income distribution, poverty incidence, and labor force participation patterns that inform Odin's user demographic modeling and financial behavior assumptions. The income quintile data (bottom 20% earn 27,606 pesos average per capita vs. top 20% at 203,210 pesos) justifies Odin's focus on affordability and essential expense floors for low-income young professionals. The finding that women's labor force participation is only 50% (vs. 74% for men) and that housework is the primary reason for not seeking work (90% of married women) directly informs Odin's design assumption that many users may have irregular or part-time income and significant unpaid care responsibilities — affecting budgeting for care-related expenses.

**Directly justifies:**

- "The Gini coefficient for per capita income in the Philippines declined from 0.453 in 2015 to 0.406 in 2023, indicating slowly improving but still high income inequality."
- "Households headed by college graduates earn 2:1 income share relative to population share, while those with no education earn below their population share — education is the primary driver of income inequality."
- "Women's labor force participation remained at approximately 50% in 2023 compared to 74% for men, with married women citing household duties as the main reason for not working (90.4% in 2023)."
- "Teenage pregnancy rates among the poorest wealth quintile (10.3%) are nearly six times higher than the richest quintile (1.8%), demonstrating how poverty compounds reproductive health risks."
- "Among individuals with no formal education, severe disability prevalence reaches 55% for women vs. 23% for men, illustrating extreme intersectional disadvantage."

**Limits of relevance:**

- The paper focuses on broad socio-economic and demographic inequalities, not personal finance app usage or transaction-level spending behavior.
- Data are at household rather than individual level for income; intra-household resource allocation is not captured, which may mask gender disparities in actual spending power.
- The young professional demographic (ages 20-40) is not isolated in most analyses; findings apply to general population.
- Disability prevalence data from 2016 NDPS may not reflect current conditions.

### Limitations

- No disaggregated data specifically for young professionals (20-40) — most findings cover general adult population. [unacknowledged]
- Cross-sectional design in many surveys limits causal inference about income inequality drivers.
- Under-representation of marginalized groups (IPs, PWDs in remote areas) in national surveys due to geographic and documentation barriers. [unacknowledged]
- GAD budget analysis based on compliance reporting rather than outcome-based evaluation of actual gender equality impact.
- Time-use survey not systematically conducted since 2000 pilot; current care work estimates rely on ISSP and ad-hoc surveys with smaller samples.

---

## Source: `1.A/L--Amado_2026_summarized.md`

**Title:** The plight of teachers on the twice-a-month salary release: Financial literacy and survival

### TL;DR

Financial literacy significantly enhances teachers' ability to manage finances under a twice-a-month salary system (mean 4.11 on 5-point scale), though intermittent stress persists between pay periods.

### Findings

1. Twice-a-month salary release was perceived as beneficial for financial well-being (overall mean = **4.18**), helping short-term planning (4.24) and expense management (4.23).
2. Financial stress persisted between pay periods (mean = 4.09 for “salary frequency influences stress”).
3. Teachers employed proactive management: budgeting (4.32), prioritizing essentials (4.46), and seeking supplementary income (3.76).
4. Perceived advantages (overall 4.23) outweighed disadvantages (overall 3.50), but challenges included covering first-half expenses (3.65) and stress between paydays (3.63).

- Financial literacy positively influenced financial management under the twice-a-month system (overall 4.21), with higher literacy equipping teachers to handle unexpected expenses (4.37).
- Survival strategies included strict budgets (4.13), dipping into savings (4.09), and seeking financial advice (3.90).

### Relevance to Odin

**Topics:**

1.A — Filipino Young Professionals as a Demographic

1.B — Financial Structure of Filipino Young Professionals

1.C — Financial Behavior of Filipino Young Professionals

2.A — Culturally Specific Financial Practices

2.B — Seasonal and Cyclical Spending Patterns

4.B — Limitations and Gaps in Existing Systems

7.A — Budgeting Strategies as Domain Knowledge

**Contribution to Odin:**

This paper provides empirical evidence on how a twice-a-month salary schedule shapes budgeting behavior, financial stress, and survival strategies among Filipino professionals (teachers). For Odin, the findings directly inform the design of budget recommendation algorithms by demonstrating that salary frequency affects users’ ability to adhere to budgets — particularly the “inter-payday” liquidity trough. The identification of specific coping mechanisms (e.g., paluwagan, 5-6 lending) grounds Odin’s culturally specific expense categories and anomaly detection for informal financial flows. Moreover, the paper’s conclusion that financial literacy is a critical enabler supports Odin’s need for integrated financial education features alongside algorithmic recommendations.

**Directly justifies:**

- “Public school teachers in the Philippines report that higher financial literacy improves their ability to handle unexpected expenses under a twice-a-month salary system (mean = 4.37 on a 5-point scale).”
- “Filipino professionals experience persistent financial stress between pay periods despite perceiving bi-monthly salary release as helpful for short-term planning (stress mean = 4.09; planning mean = 4.24).”
- “Teachers employ prioritization of essential expenses (mean = 4.46) and strict budgeting (mean = 4.32) as primary survival strategies between paydays.”
- “Informal financial mechanisms such as paluwagan and 5-6 lending are normalized responses to salary timing constraints in the Philippine public sector.”
- “Generic financial literacy programs are insufficient when salary disbursement timing constrains cash flow; interventions must align with actual pay cycles.”

**Limits of relevance:**

- Study population is teachers (primarily public school), not general young professionals; income stability and debt profiles may differ.
- No ML/AI evaluation; relevance is to behavioral domain knowledge, not algorithm benchmarking.
- The twice-a-month schedule is common, but the paper does not compare against weekly or monthly schedules in a controlled design.
- Survey data from one district (Claveria North) may not generalize across Metro Manila or other regions.

### Limitations

- Self-reported survey data subject to recall and social desirability bias (teachers may under-report financial stress).
- Cross-sectional design; no longitudinal tracking of how financial literacy or survival strategies change over time.
- Sample limited to one district; findings may not generalize to urban Metro Manila professionals with different cost-of-living pressures.
- No objective validation of financial literacy (e.g., test scores); literacy measured via self-perceived confidence.
- The study does not disaggregate results by age or income bracket, making direct application to young professionals (20–40) inferential. [unacknowledged]

---

## Source: `1.A/L--Apao_et-al_2025_summarized.md`

**Title:** Maritime Students’ Financial Knowledge, Attitude, and Behavior

### TL;DR

Very high financial knowledge, attitude, and behavior among maritime students do not correlate significantly — knowing and feeling positive about money does not predict responsible spending or saving.

### Findings

1. Financial knowledge: **M = 3.74/4 (SD = 0.14)** — Very High.
2. Financial attitude: **M = 3.71/4 (SD = 0.10)** — Very High.
3. Financial behavior: **M = 3.85/4 (SD = 0.17)** — Very High.
4. Knowledge vs. behavior: r = –0.46, p = 0.652 — **Not significant.**
5. Attitude vs. behavior: r = 0.59, p = 0.558 — **Not significant.**

- Students report strong financial understanding and positive money mindsets, yet these do not translate into consistent financial actions.
- Parental influence and real‑life experiences appear to shape knowledge, but practical application remains weak.
- The gap between knowing/feeling and doing suggests that financial education must include behavioral skills training.

### Relevance to Odin

**Topics:**

1.A — Filipino Young Professionals as a Demographic

1.C — Financial Behavior of Filipino Young Professionals

5.A — Financial Behavioral Profiles in Personal Finance

**Contribution to Odin:**

This paper directly informs Odin’s behavioral profiling module by demonstrating that financial knowledge and positive attitudes do not predict actual financial behavior in a Filipino student sample. For Odin, which targets Filipino young professionals (20‑40), this finding justifies the system’s reliance on behavioral data (transaction logs) rather than self‑reported literacy or intentions. The knowledge‑behavior gap supports Odin’s design choice to use ML‑driven classification and anomaly detection to infer real habits, not assume that users already manage money well because they “know better.”

**Directly justifies:**

- “Filipino maritime students report very high financial knowledge (M=3.74/4) yet no significant correlation with financial behavior (r=-0.46, p=0.652).”
- “Positive financial attitude (M=3.71/4) does not significantly translate into responsible financial actions (p=0.558).”
- “Financial education that only increases knowledge and attitude is insufficient; practical skill‑building and behavioral reinforcement are required.”
- “Parental influence and informal learning produce high self‑reported financial understanding, but this does not guarantee consistent money management.”

**Limits of relevance:**

- Sample is maritime students, not the broader young professional population; income patterns (lump‑sum seafarer pay) may differ from typical office workers.
- Cross‑sectional, self‑reported data; actual spending behavior was not observed.
- No algorithm or predictive model is tested; the paper provides behavioral justification, not technical validation.
- Small sample (N=100) from a single institution limits generalizability.

### Limitations

- Small sample (N=100) from one private institution in Ozamiz City; findings may not generalize to all Filipino young professionals. [unacknowledged]
- Self‑reported Likert scales may overstate financial behavior due to social desirability bias. [unacknowledged]
- Cross‑sectional design cannot establish causation between knowledge/attitude and behavior.
- Allowance threshold (≥ ₱1,000/week) excludes lower‑income students, potentially skewing results upward. [unacknowledged]
- The paper does not report the specific items in the questionnaires, limiting replicability.

---

## Source: `1.A/L--Cadayunan_et-al_2025_summarized.md`

**Title:** A Descriptive-Correlational Analysis of Social Media Usage and Personal Finance Competencies Among University Students

### TL;DR

Social media use correlates moderately positively with financial literacy and decision-making among Filipino university students, but high literacy does not translate into budget adherence or impulse control.

### Findings

1. **Moderate positive correlation** between social media usage frequency and financial literacy (r = **.359**, p < .001).
2. **Moderate positive correlation** between social media usage frequency and financial decision-making abilities (r = **.361**, p < .001).
3. Students reported “High Financial Literacy” (understanding concepts like saving and budgeting) but “Moderate Decision‑Making Abilities.”

- Specific difficulties: creating and sticking to a budget, saving regularly, and resisting impulse purchases.
- Facebook and TikTok are the most preferred social media platforms, used daily upon waking and before sleep.

### Relevance to Odin

**Topics:**

1.A — Filipino Young Professionals as a Demographic

1.C — Financial Behavior of Filipino Young Professionals

5.A — Financial Behavioral Profiles in Personal Finance

7.A — Budgeting Strategies as Domain Knowledge

8.A — Anomaly Detection in Personal Finance Systems

**Contribution to Odin:**

This paper directly supports Odin’s behavioral profiling module by documenting a knowledge‑to‑action gap among Filipino students (high literacy, low practical application). The finding that students struggle with budget adherence and resist impulse purchases informs Odin’s budgeting and anomaly detection features. Although the study focuses on university students, the pattern of knowing without doing mirrors the likely behavior of young professionals, justifying Odin’s emphasis on behavioral interventions rather than purely informational content. The moderate correlation between social media use and competencies also suggests that Odin could leverage social‑media‑style education to raise awareness, but must pair it with in‑app controls to bridge the gap.

**Directly justifies:**

- “Filipino university students report high financial literacy (understanding of saving and budgeting concepts) but exhibit moderate decision‑making abilities, particularly struggling with budget adherence and resisting impulse purchases.”
- “Social media usage frequency shows a moderate positive correlation with financial decision‑making abilities (r=.361, p<.001) among Filipino students, indicating that digital exposure to financial content can raise awareness.”
- “The knowledge‑to‑action gap—knowing financial concepts but failing to apply them—highlights the need for behavioral interventions (e.g., automated savings, spending alerts) rather than purely informational financial education.”
- “Impulse purchases are a reported difficulty for students, suggesting that anomaly detection for overspending should account for emotional triggers and social commerce exposure.”

**Limits of relevance:**

- Study population is university students, not young professionals (20–40), though the transition period makes behavior partially transferable.
- Self‑reported measures of financial literacy and decision‑making may not perfectly reflect actual behavior.
- Correlation does not imply causation; social media content quality (educational vs. commercial) was not distinguished.
- Single campus in Mindanao limits generalizability across the Philippines.
- No longitudinal data; the correlation may change as users gain financial experience.

### Limitations

- Self‑report bias: participants may overstate financial literacy or underreport impulsive spending. [unacknowledged]
- Cross‑sectional design prevents causal inference; the direction of the relationship is unknown.
- Sample limited to BSBA students at one campus; findings may not extend to other majors or regions.
- Social media usage measured by frequency and platform preference, not by content type (educational vs. entertainment/commercial).
- No objective validation of financial decision‑making (e.g., actual bank or budget tracking data).

---

## Source: `1.A/L--Claros_et-al_2026_summarized.md`

**Title:** Determinants of Saving Behavior Among Filipino University Students: A Psychological and Social Perspective

### TL;DR

Financial literacy had the strongest positive effect on saving behavior among Filipino university students (β=0.684), while self-control showed a surprising negative effect.

### Findings

1. Financial literacy had the **strongest positive effect** on saving behavior (β = 0.684, p < .001), supporting H1.
2. Parental influence also positively affected saving behavior (β = 0.284, p < .001), supporting H2.
3. Peer influence was not significant (β = -0.041, p = 0.423), rejecting H3.
4. Self-control showed a significant **negative** effect (β = -0.201, p < .001), rejecting H4.

- The model explained **62.3%** (R² = 0.623) of variance in saving behavior.
- Model fit was excellent: CFI = 0.965, TLI = 0.962, GFI = 0.975.

### Relevance to Odin

**Topics:**

1.A — Filipino Young Professionals as a Demographic

1.C — Financial Behavior of Filipino Young Professionals

2.A — Culturally Specific Financial Practices

5.A — Financial Behavioral Profiles in Personal Finance

**Contribution to Odin:**

This paper directly informs Odin's user profiling and financial behavior modules by identifying which psychological and social factors predict saving behavior among young Filipinos. The finding that financial literacy has the largest effect (β=0.684) justifies integrating financial education content or knowledge assessments within Odin to improve user saving outcomes. The significant role of parental influence (β=0.284) supports designing features that encourage users to reflect on family-taught financial norms, which is culturally relevant in the Philippine context. The counterintuitive negative effect of self-control (β=-0.201) warns Odin's design team not to assume that high self-discipline alone drives better financial outcomes, suggesting that system nudges should focus on knowledge reinforcement rather than willpower activation.

**Directly justifies:**

- "Financial literacy has the strongest positive effect on saving behavior among Filipino university students (β=0.684, p<.001), accounting for 62.3% of variance in saving behavior."
- "Parental influence positively and significantly affects saving behavior (β=0.284, p<.001), supporting family socialization as a primary mechanism for financial habit formation in the Philippines."
- "Self-control exhibits a significant negative effect on saving behavior (β=-0.201, p<.001), challenging conventional assumptions that greater discipline always improves saving."
- "Peer influence does not significantly predict saving behavior (p=0.423), indicating that saving decisions among Filipino students are family-driven rather than peer-driven."

**Limits of relevance:**

- Study population is university students (18–25), not specifically young professionals aged 20–40 with regular employment income.
- The dependent variable is saving behavior, not budgeting or spending forecasting — direct applicability to Odin's core forecasting module is limited.
- Cross-sectional design cannot establish causality; only correlational evidence.
- No demographic subgroup analysis (age, gender, income level) — may mask heterogeneity relevant to profiling.

### Limitations

- Lack of demographic data (age, gender, income level) in the survey instrument limits subgroup comparisons.
- Self-reported saving behavior may suffer from social desirability bias [unacknowledged].
- Cross-sectional design cannot confirm causal direction between determinants and saving behavior.
- Sample limited to university students; findings may not generalize to non-student young Filipinos.
- Negative self-control effect is unexplained and requires replication (possible suppression by financial literacy).

---

## Source: `1.A/L--Dimaunahan_et-al_2025_summarized.md`

**Title:** Financial literacy and sustainable planning assessment among Filipino millennials

### TL;DR

Low financial literacy among Filipino millennials does not directly affect their financial planning; monthly income, expenses, and occupation are the significant drivers.

### Findings

1. **Only 54.5% understood interest compounding, 38.8% inflation, and 33.8% risk diversification** — very low financial literacy.
2. Financial literacy had **no significant effect** on financial planning (β = 0.077, p = 0.153).
3. Monthly expenses had the strongest significant effect (β = 0.205, p = 0.001), followed by monthly income (β = 0.180, p = 0.003), then occupation (β = 0.164, p = 0.004).

- Among goal-setting moderators, goal acceptance had the largest effect on financial planning (β = 0.924, p < 0.001), then goal commitment (β = 0.809), goal specificity (β = 0.597), and goal difficulty (β = 0.212).
- Respondents with higher incomes and stable occupations engaged in more financial planning, but low literacy did not prevent planning entirely.

### Relevance to Odin

**Topics:**

1.A — Filipino Young Professionals as a Demographic

1.B — Financial Structure of Filipino Young Professionals

1.C — Financial Behavior of Filipino Young Professionals

4.B — Limitations and Gaps in Existing Systems

5.A — Financial Behavioral Profiles in Personal Finance

**Contribution to Odin:**

This paper directly informs Odin’s behavioral profiling module by demonstrating that demographic factors (income, expenses, occupation) drive financial planning more strongly than financial literacy among Filipino millennials. The finding that low literacy does not significantly affect planning suggests Odin’s budget recommendation algorithm should prioritize users’ income stability and expense load over their financial knowledge scores. The strong effect of goal acceptance (β=0.924) on planning justifies incorporating user goal acceptance as a key input for engagement and retention mechanisms in Odin. Additionally, the paper’s documentation of very low literacy rates (e.g., 33.8% understanding risk diversification) supports Odin’s need for simple, educational interfaces rather than assumption of financial sophistication.

**Directly justifies:**

- “Only 54.5% of Filipino millennials understand compound interest, 38.8% understand inflation, and 33.8% understand risk diversification (Dimaunahan et al., 2025).”
- “Financial literacy has no significant direct effect on financial planning among Filipino millennials (β = 0.077, p = 0.153); instead, monthly expenses (β = 0.205), monthly income (β = 0.180), and occupation (β = 0.164) are significant predictors.”
- “Goal acceptance is the strongest predictor of financial planning (β = 0.924), exceeding goal commitment, specificity, and difficulty.”
- “Filipino millennials engage in financial planning primarily driven by personal needs and goals rather than financial literacy itself.”

**Limits of relevance:**

- Study conducted only in Makati City (urban, relatively high-income area); findings may not generalize to rural or lower-income Filipino young professionals.
- Sample limited to millennials aged 28–43; Odin targets 20–40, so younger adults (20–27) are not represented.
- Financial literacy measured only with three binary-correct items; does not capture nuanced financial capability or behavioral skills.
- Self-reported survey data, not observed transaction behavior; may overstate actual planning engagement.

### Limitations

- Sample confined to one highly urbanized city (Makati), not representative of all Filipino millennials.
- Cross-sectional design cannot establish causality between demographics and financial planning.
- Use of only “The Big Three” financial literacy questions — a more comprehensive measure might yield different results. [unacknowledged]
- Self-report bias: respondents may overstate their financial planning practices.
- No longitudinal follow-up; cannot assess whether planning behavior persists or changes over time. [unacknowledged]

---

## Source: `1.A/L--Espiritu_2025_summarized.md`

**Title:** Knowledge, Attitudes, and Practices in Financial Literacy among Business Administration Students in Urban College in the Philippines

### TL;DR

Filipino business students report positive financial attitudes and practices, but demographic factors (age, sex, year level, income) create significant differences in financial literacy.

### Findings

1. **48.9%** of respondents were aged 18–20; **65.9%** were male; **48.1%** had monthly family income of PHP 10,001–20,000.
2. Mean scores for knowledge, attitude, and practice all fell in the “Agree” range (2.98–3.13 out of 4), with debt knowledge highest (3.13) and income knowledge lowest (2.98).
3. Age, sex, and year level significantly affected financial knowledge (p < 0.05); monthly income did not (p = 0.092).
4. Age, monthly income, and year level significantly affected financial attitude; sex did not (p = 0.359).
5. **All four demographic factors** (age, sex, monthly income, year level) significantly affected financial practices (all p < 0.001).

- Knowledge, attitude, and practice are significantly correlated (R = 0.697, p < 0.001), indicating a strong relationship.

### Relevance to Odin

**Topics:**

1.A — Filipino Young Professionals as a Demographic

1.B — Financial Structure of Filipino Young Professionals

1.C — Financial Behavior of Filipino Young Professionals

5.A — Financial Behavioral Profiles in Personal Finance

**Contribution to Odin:**

This paper provides empirical evidence on the financial knowledge, attitudes, and practices of Filipino young adults (aged 18–30) in an urban setting, directly informing Odin’s user profiling and behavioral classification modules. The finding that age, sex, year level, and monthly income all significantly affect financial practices justifies designing Odin’s classification algorithm to incorporate these demographic dimensions. The strong correlation between knowledge, attitude, and practice (R = 0.697) supports Odin’s design assumption that improving financial literacy and attitudes can drive better budgeting behavior, which the system aims to reinforce through intelligent recommendations.

**Directly justifies:**

- “Filipino business students aged 18–20 have lower financial knowledge scores than older students, indicating that age is a significant predictor of financial literacy (p = 0.013).”
- “Monthly family income does not significantly affect financial knowledge among Filipino urban college students (p = 0.092), but it does affect attitude (p = 0.038) and practice (p < 0.001).”
- “Male students in this sample (65.9% of respondents) show significant differences in financial knowledge (p = 0.020) and practices (p < 0.001) compared to female students, suggesting sex should be a feature in behavioral profiling.”
- “Financial knowledge, attitude, and practice are strongly correlated (R = 0.697), meaning interventions that improve one dimension likely improve the others.”

**Limits of relevance:**

- The sample is business administration students, not the general population of young professionals; their financial literacy may be higher due to coursework.
- Self‑reported measures (Likert scales) may not reflect actual financial behavior as accurately as transaction‑level data.
- The study does not test any algorithm or computational model; it provides descriptive and correlational evidence only.
- Monthly family income is used as a proxy for personal financial resources, but students may have personal earnings not captured.

### Limitations

- Relatively low subscale reliability (Cronbach’s alpha 0.172 for attitude, 0.158 for practices) suggests measurement instability. [unacknowledged]
- Cross‑sectional design cannot establish causality between knowledge, attitude, and practice.
- Single institution in Metro Manila limits generalizability to other Philippine regions or rural areas.
- No validation of self‑reported practices against actual spending records.
- Sample is predominantly male (65.9%), which may bias findings on sex differences.

---

## Source: `1.A/L--Gerzon_et-al_2023_summarized.md`

**Title:** Financial Literacy and Financial Well-Being of Nurses of a First-Class Province in the Philippines

### TL;DR

Philippine public health nurses have high financial literacy and great financial well-being; monthly income predicts literacy, and literacy strongly predicts well-being (rs=0.660).

### Findings

1. Overall financial literacy level was **“High” (M=3.22, SD=0.39)** on a 4‑point scale.
2. Overall financial well‑being extent was **“Great” (M=3.03, SD=0.46)**.
3. Only monthly income correlated with financial literacy [r(176)=0.223, p=0.003]; age, sex, civil status, and dependents showed no correlation.
4. No demographic factor correlated with financial well‑being.

- **Financial literacy and financial well‑being showed a strong positive correlation [rs(176)=0.660, p=0.000]**.

### Relevance to Odin

**Topics:**

1.A — Filipino Young Professionals as a Demographic

1.C — Financial Behavior of Filipino Young Professionals

**Contribution to Odin:**

This paper provides empirical evidence from a Filipino professional population (public health nurses) that financial literacy is high and strongly correlated with financial well‑being. For Odin’s budget recommendation and behavioral profiling modules, the finding supports the design assumption that improving financial knowledge and tracking behavior leads to better financial outcomes. The sub‑domains of financial well‑being (discipline, security, resiliency) map directly to Odin’s goals of helping users control spending, build savings buffers, and withstand financial shocks. The result that monthly income significantly predicts literacy suggests that income‑based tailoring of financial content or recommendations may be effective in Odin’s target population.

**Directly justifies:**

- “Public health nurses in a first‑class Philippine province have high financial literacy (M=3.22 on a 4‑point scale).”
- “Financial literacy and financial well‑being show a strong positive correlation (rs=0.660, p<0.001) among Filipino professionals.”
- “Monthly income is significantly correlated with financial literacy (r=0.223, p=0.003) in this population, while age, sex, civil status, and dependents are not.”
- “Financial well‑being can be measured through financial discipline, financial security, and financial resiliency using a validated 4‑point Likert instrument.”

**Limits of relevance:**

- Study population is nurses, not specifically young professionals aged 20–40; income levels and spending patterns may differ.
- Cross‑sectional design cannot establish causality between literacy and well‑being (only correlation).
- Sample limited to one province in the Philippines; findings may not generalize to all Filipino young professionals.
- No algorithm, ML model, or system evaluation is discussed — relevance is at the behavioral and demographic background level.

### Limitations

- Sample restricted to one first‑class province and only public health nurses, limiting generalizability to other Filipino workers.
- Self‑reported survey data may be subject to social desirability and recall bias.
- Cross‑sectional design prevents causal inference between financial literacy and well‑being [unacknowledged].
- Researcher‑made instrument, though validated, may not align with international standardized surveys like S&P or OECD [unacknowledged].
- No qualitative component to explain *why* nurses have high literacy or how they practice financial behaviors.

---

## Source: `1.A/L--Jandoc_et-al_2026_summarized.md`

**Title:** Profiling Platform Workers in the Philippines: Evidence from the Jobs and Skills Survey

### TL;DR

Platform workers in the Philippines—disproportionately young, urban, highly educated, and concentrated in NCR—face volatile earnings and weak social protection, with transport workers pushed by necessity and home-based freelancers drawn by flexibility.

### Findings

1. **8.2%** of workers (≈4.1 million) use platforms; **84.5%** report it as their sole job, averaging 42.6 hours/week.
2. Platform workers are 74.0% urban, 69.7% have higher education, and 31.0% are in NCR (vs. 15% of all workers).
3. Flexibility (88.9%) and ease of entry (79.6%) are top motivations; necessity-driven entry is higher for drivers (18.1% lack alternatives) than home-based workers (9.3%).
4. Platform workers have lower RTI (**-0.19**) than non-platform workers (**+0.56**), indicating less routine, more analytical/interpersonal tasks, but drivers/delivery workers show positive RTI (+0.12, +0.15).
5. **Overskilling** is more common among daily platform users (22.5%) than non-users (14.8%), especially for computer/software skills (42.6% vs. 26.4%).
6. After controlling for worker and firm characteristics, platform workers have significantly lower odds of employer pension contributions (logit coeff: **-1.33**), health insurance (**-0.95**), and separation benefits (**-0.81**).

- Home-based and delivery workers face the largest benefit deficits; drivers show no significant pension/health gap but lower paid leave.
- Job satisfaction and perceived safety are high across all groups (≥90%), with no significant difference after controls.

### Relevance to Odin

**Topics:**

1.A — Filipino Young Professionals as a Demographic

1.B — Financial Structure of Filipino Young Professionals

1.C — Financial Behavior of Filipino Young Professionals

2.B — Seasonal and Cyclical Spending Patterns

5.A — Financial Behavioral Profiles in Personal Finance

11.A — Engagement Dynamics in Personal Finance Applications

**Contribution to Odin:**

This paper directly informs Odin's behavioral profiling and engagement modules by characterizing income volatility and financial vulnerability among Filipino platform workers—a segment overlapping heavily with Odin's target demographic of young professionals. The finding that 84.5% of platform workers rely on this as their sole job, combined with volatile earnings and weak social protection, justifies Odin's design for users with irregular income patterns and validates the need for dynamic, adaptive budget recommendations rather than static templates. The high overskilling rate (22.5% among daily platform users) suggests that Odin's users may have cognitive and digital skills exceeding typical financial app demands, supporting a design that avoids patronizing simplicity and instead offers sophisticated controls and explanations. The documented concentration of platform work in urban, highly educated prime-age workers matches Odin's user profile, making the paper's income and employment patterns directly applicable as domain knowledge for forecasting and anomaly detection.

**Directly justifies:**

- "Among Filipino platform workers, 84.5% rely on platform work as their sole job, with average weekly hours (42.6) comparable to full-time employment, indicating that non-traditional work is a primary livelihood, not a marginal supplement."
- "Platform workers face significantly lower odds of employer-provided pension (logit coeff -1.33), health insurance (-0.95), and separation benefits (-0.81) even after controlling for firm characteristics—evidence of systemic benefit precarity that affects income stability and financial planning."
- "Daily platform users report 22.5% overskilling (vs. 14.8% among non-users), with the largest gaps in software (42.6% vs. 26.4%) and communication skills (38.5% vs. 22.0%), indicating that many Filipino young professionals in platform work have skill levels exceeding job demands."
- "Necessity-driven entry (lack of other satisfactory income sources) is nearly twice as high among delivery (17.7%) and driving (18.1%) platform workers than home-based digital workers (9.3%), showing that income volatility and limited alternatives push some users into gig work."

**Limits of relevance:**

- The paper profiles employment characteristics, not spending behavior or budgeting practices—financial management inferences are indirect.
- Data are cross-sectional; causal relationships between platform work and financial outcomes are not established.
- The JSS does not track transaction-level spending, so forecasting or anomaly detection algorithms cannot be directly benchmarked against its findings.
- Platform worker categories (home-based, outside-home, driving, delivery) are distinct from Odin's functional modules; mapping requires care (e.g., income volatility applies to all, but task content relevance differs).

### Limitations

- Cross-sectional design prevents causal claims about whether platform work causes benefit deficits or simply attracts workers from unprotected sectors. [unacknowledged]
- JSS relies on self-reported skills and overskilling, which may be inflated by highly educated workers in low-complexity tasks. [unacknowledged]
- No longitudinal tracking of earnings volatility or income shocks, limiting direct use for forecasting model design.
- RTI index, while standardized, may not capture all task nuances specific to Filipino platform work (e.g., cash handling, algorithmic rating stress).
- Sample sizes for some platform worker subgroups (e.g., drivers) limit statistical power in regressions, reflected in non-significant coefficients for some benefit models.

---

## Source: `1.A/L--Lantin-Magana_et-al_2026_summarized.md`

**Title:** Predictors of Investment Decision among Selected Individuals in Key Cities of Laguna: An Extended Theory of Planned Behavior Approach

### TL;DR

Attitude toward investment and monthly salary predict investment decisions among Filipino young professionals in Laguna, explaining 16% of variance, with male and higher-income participants showing stronger decisions.

### Findings

1. **Stepwise regression identified attitude toward investment (coefficient = 0.345) and monthly salary (coefficient = 0.368) as significant predictors, explaining 16.2% of the variance (R² = 0.162, p < .001).**
2. Investment decision differed significantly by sex (p = .002), with male respondents scoring higher than female respondents.
3. Investment decision differed significantly across monthly salary brackets (p < .001); the lowest salary group (15,000–45,000) reported the lowest scores.
4. Capital market knowledge showed the strongest correlation with investment decision (r = 0.210, p = .001), followed by attitude toward investment (r = 0.179, p = .003).

- Risk tolerance had the highest mean rating (M = 4.81), government trust the lowest (M = 3.85) on a 6-point scale.

### Relevance to Odin

**Topics:**

1.A — Filipino Young Professionals as a Demographic

1.C — Financial Behavior of Filipino Young Professionals

5.A — Financial Behavioral Profiles in Personal Finance

**Contribution to Odin:**

This paper’s finding that attitude toward investment and monthly salary jointly predict financial decisions directly informs Odin’s behavioral profiling module. The significant sex-based difference in investment decisions (p = .002) suggests that financial behavior profiles must account for gender as a moderating variable, particularly when designing interventions or recommendations. Although the paper focuses on investment rather than budgeting, its TPB-informed approach validates the use of attitudinal and capability-related constructs (e.g., financial literacy, risk tolerance) in predicting financial actions — directly applicable to Odin’s classification of user profiles based on spending and saving behaviors.

**Directly justifies:**

- "Attitude toward investment and monthly salary predict 16.2% of the variance in investment decisions among Filipino young professionals in Laguna."
- "Male respondents exhibit significantly higher investment decision scores than female respondents (p = .002), indicating gender as a relevant stratifier in financial behavior profiling."
- "Capital market knowledge correlates with investment decision (r = 0.210, p = .001), supporting the inclusion of financial literacy measures in behavioral classification."
- "Risk tolerance had the highest mean rating (4.81/6) among measured constructs, suggesting that risk acceptance alone does not guarantee investment action without adequate knowledge or institutional trust."

**Limits of relevance:**

- Paper examines investment decisions, not everyday budgeting or spending behavior — Odin’s core domain is personal budget management.
- Study sample includes individuals from key cities of Laguna, not exclusively young professionals aged 20–40 (Odin’s target); generalization to Metro Manila may be limited.
- No algorithm or predictive model is tested; the findings are correlational and descriptive, not directly transferable to ML module design.

### Limitations

- Cross-sectional design prevents causal inference; associations may not reflect true predictive direction.
- Purposive sampling and online-only collection limit representativeness (digital access bias). [unacknowledged]
- Self-reported measures may be influenced by social desirability and response style.
- Modest R² (0.162) indicates substantial variance unexplained; important predictors (e.g., perceived behavioral control, social norms) omitted.
- Stepwise regression may be sample-specific and not generalize across settings.

---

## Source: `1.A/L--Lim_&_Cordova_2024_summarized.md`

**Title:** Decoding the eco-financial mindset: financial literacy, attitudes, and efficacy measures and the spending behavior of Filipino millennials

### TL;DR

Financial attitude negatively predicts spending behavior among Filipino millennials, but financial literacy and efficacy show no direct significant relationship to spending.

### Findings

1. Financial attitude, literacy, and efficacy have **strong positive intercorrelations** (r = 0.52–0.77, p < .001).
2. Spending behavior has a **significant negative relationship with financial attitude** (β = -0.176, p = 0.034).
3. Spending behavior shows no statistically significant relationship with financial literacy (β = -0.045, p = 0.477) or financial efficacy (β = -0.069, p = 0.292).

- 42% of respondents spend 41% or more of total income.
- Spending on beer/wine is highly consistent: 93.7% spend ≤10% of income in this category (SD = 0.521).
- Spending on groceries is also consistent: 77.5% allocate ≤10% of income.

### Relevance to Odin

**Topics:**

1.A — Filipino Young Professionals as a Demographic

1.B — Financial Structure of Filipino Young Professionals

1.C — Financial Behavior of Filipino Young Professionals

3.A — Expense Categorization Frameworks

5.A — Financial Behavioral Profiles in Personal Finance

**Contribution to Odin:**

This paper directly informs Odin's behavioral profiling and expense categorization modules by providing empirically derived spending patterns and financial attitude–spending relationships specific to Filipino millennials — a demographic that overlaps heavily with Odin's target young professionals. The finding that financial attitude (not literacy) predicts spending suggests Odin's user profile should prioritize attitudinal measures over pure knowledge tests when designing budget alerts or recommendations. The detailed category-level spending percentages (e.g., 77.5% of millennials spend ≤10% on groceries) provide baseline anchors for Odin's default category budget floors.

**Directly justifies:**

- "Financial attitude has a significant negative relationship with spending behavior among Filipino millennials (β = -0.176, p = 0.034), meaning more positive financial attitudes correlate with lower spending."
- "42% of Filipino millennials in Laguna spend 41% or more of their total income, indicating high spending propensity in this demographic."
- "93.7% of Filipino millennials allocate ≤10% of income to beer and wine — a culturally specific spending pattern with very low variability (SD = 0.521)."
- "Financial literacy and financial efficacy show no direct statistically significant relationship to spending behavior in this sample (p = 0.477 and p = 0.292, respectively)."
- "Financial literacy, attitude, and efficacy are strongly intercorrelated (r = 0.52–0.77), suggesting they form a composite behavioral construct rather than independent predictors."

**Limits of relevance:**

- Sample drawn only from Laguna, Philippines — may not generalize to all Metro Manila young professionals.
- Self-reported spending percentages, not objective transaction data — recall bias possible.
- Millennial definition (born 1981–1996) extends beyond Odin’s 20–40 age range (includes ages 41–43 at time of study).
- No longitudinal data — cannot assess if attitude–spending relationship persists over time or changes with app usage.

### Limitations

- Cross-sectional design — causal direction cannot be inferred from the attitude–spending correlation.
- Majority of respondents work in finance-related jobs (accounting, banking) — may inflate financial literacy scores. [unacknowledged]
- Cronbach’s alpha for spending constructs is low (α = 0.656) — internal consistency of spending measurement is questionable.
- No validation of spending categories against established frameworks like FIES or BSP CFS.
- Self-reported financial knowledge (not objective test) — may overstate actual literacy levels.

---

## Source: `1.A/L--Mutuc_2025_summarized.md`

**Title:** Exploring the Interplay of Life Attitude and Cognitive Ability in Shaping the Intention to Stock Market Participation Among Young Professionals in the Philippines

### TL;DR

Life attitude dimensions, particularly death acceptance and goal seeking, positively influence stock market participation intention among Filipino young professionals, with financial literacy mediating this relationship.

### Findings

1. Overall Life Attitude Profile positively predicts stock market participation intention (β = 0.154, p = 0.025; R² = 0.471–0.582).
2. **Death acceptance (β = 0.312, p < 0.001) and goal seeking (β = 0.396, p = 0.009) are the strongest positive predictors** of investment intention.
3. Life purpose shows a negative relationship with stock market participation (β = -0.243, p = 0.036), suggesting purpose-driven individuals may prefer security over speculative investing.
4. Cognitive ability mediates the LAP→SMP relationship (indirect β = 0.051, p = 0.032; 95% CI [0.004, 0.098]).
5. Financial literacy directly predicts stock market participation (β = 0.329, p < 0.001), reinforcing its enabling role.

- Existential vacuum, life control, will to meaning, and future meaning to fulfil showed non-significant direct effects.
- Males relied more on cognitive ability (C→SMP β = 0.42) while females showed stronger attitudinal influence (LAP→SMP β = 0.38).

### Relevance to Odin

**Topics:**

1.A — Filipino Young Professionals as a Demographic

1.C — Financial Behavior of Filipino Young Professionals

5.A — Financial Behavioral Profiles in Personal Finance

**Contribution to Odin:**

This paper provides empirical evidence that psychological dispositions (life attitude dimensions) and cognitive ability (financial literacy) jointly determine financial intentions among Filipino young professionals. For Odin’s financial behavioral profiling module, the findings justify incorporating attitudinal measures (e.g., goal orientation, future meaning) alongside literacy assessment to construct richer user profiles. The mediating role of cognitive ability—showing that attitudes translate into behavior only when supported by knowledge—directly supports Odin’s design decision to embed financial literacy scaffolding within the onboarding flow rather than treating it as a separate educational module. Although the outcome is stock market participation rather than budgeting adherence, the psychological mechanism (attitude → cognition → intention) generalizes to Odin’s goal of converting user financial attitudes into consistent budgeting behavior.

**Directly justifies:**

- “Goal seeking positively predicts financial intention among Filipino young professionals (β = 0.396, p = 0.009), supporting the inclusion of goal-orientation items in behavioral profiling instruments.”
- “Financial literacy mediates 51% of the relationship between life attitude and financial intention, indicating that cognitive ability is a necessary conduit for psychological dispositions to translate into action.”
- “Death acceptance (reconciliation with mortality) predicts higher financial risk-taking intention (β = 0.312, p < 0.001), suggesting that existential factors influence financial behavior beyond traditional risk aversion measures.”
- “PLS-SEM with bootstrapping (5000 resamples) is an appropriate analytical method for mediation testing in behavioral finance studies with moderate sample sizes (N = 195).”
- “Life purpose negatively correlates with stock market participation (β = -0.243), implying that strongly purpose-driven individuals may avoid speculative financial activities—a counterintuitive finding that suggests profile segmentation must distinguish between types of purpose.”

**Limits of relevance:**

- The study measures *intention* to participate in stock markets, not actual budgeting or spending behavior—Odin’s core domain is budget adherence, not investment.
- Sample drawn from Bulacan province, not Metro Manila; Metro Manila young professionals may have different income structures and financial access.
- Cross-sectional design cannot establish causality between life attitude, cognitive ability, and financial behavior; Odin’s profiling requires longitudinal updating.
- Cognitive ability measured only as financial literacy; Odin may need broader cognitive assessments (numeracy, reasoning) not covered here.
- No specific algorithm or model is proposed; the paper is theoretical/empirical rather than engineering-focused.

### Limitations

- Self-reported data may introduce social desirability bias despite anonymity assurances.
- Cross-sectional design prevents causal inference; temporal ordering between life attitudes and investment intention cannot be established.
- Common method variance was tested via Harman’s single-factor test (29.32% variance by first factor) but no marker variable was included. [unacknowledged]
- LAP-R was used in original English without cultural adaptation or pilot testing for the Filipino population.
- Sample limited to one province (Bulacan); findings may not generalize to other Philippine regions or to young professionals with different socioeconomic backgrounds.

---

## Source: `1.A/L--Razalan_2024_summarized.md`

**Title:** Scaling the Frame of Mind: Money Attitude and Financial Well-Being of Generation Zoomers (Gen-Zs) in Rizal Province

### TL;DR

Gen-Zs in Rizal Province exhibit developed money attitudes, and positive attitudes correlate significantly with financial well-being across autonomy, competence, and relatedness.

### Findings

1. Spending behavior: overall weighted mean 3.89/5 (Great Extent); “affords essential and basic needs” scored highest at **4.37** (Very Great Extent).
2. Saving behavior: overall mean 3.85/5 (Great Extent); “has specific savings goals” scored 4.14.
3. Financial education: overall mean 3.35/5 (Moderate Extent); “sufficient knowledge of online banking” scored 3.90.
4. Borrowing money: overall mean 3.21/5 (Moderate Extent); “pays off debts timely” scored 4.29 (Very Great Extent).
5. **Overall correlation between money attitudes and financial well-being: r=0.679 (p<0.05)** — a strong, significant holistic impact.

- Qualitative findings: Gen-Zs struggle with unplanned purchases (driven by buy-now-pay-later), difficulty saving, poor debt management, and limited access to financial education.
- Coping strategies: budgeting, tracking expenses, prioritizing needs over wants, and using technology cautiously to avoid scams.

### Relevance to Odin

**Topics:**

1.A — Filipino Young Professionals as a Demographic

1.C — Financial Behavior of Filipino Young Professionals

2.A — Culturally Specific Financial Practices

5.A — Financial Behavioral Profiles in Personal Finance

**Contribution to Odin:**

This paper provides empirical, locally sourced data on money attitudes (power-prestige, retention-time, distrust, anxiety) and financial well-being (autonomy, competence, relatedness) among Filipino Gen-Zs in the education sector — directly informing Odin’s behavioral profiling module by identifying which attitude dimensions correlate with financial outcomes. The finding that Gen-Zs prioritize essential needs, practice budgeting, and struggle with unplanned purchases due to buy-now-pay-later services supports Odin’s expense categorization, anomaly detection, and budget recommendation designs. Although the study does not involve algorithms, its psychological framework validates the importance of profile-based personalization in a Filipino young professional context, and the significant correlation (r=0.679) provides an empirical benchmark for evaluating whether Odin’s classification captures meaningful behavioral drivers.

**Directly justifies:**

- “Gen-Zs in Rizal Province demonstrate a ‘Great Extent’ of power-prestige orientation in spending and saving behavior, and ‘Moderate Extent’ in financial education and distrust dimensions.”
- “Positive money attitudes correlate significantly with financial well-being, with an overall correlation of r=0.679 (p<0.05), supporting a holistic impact of attitudes on financial outcomes.”
- “Gen-Zs face financial challenges including unplanned purchases driven by buy-now-pay-later services, difficulty saving, poor debt management, and limited access to ongoing financial education.”
- “Gen-Zs cope with financial challenges through budgeting, tracking expenses, and prioritizing needs over wants — behaviors that can be reinforced by automated budget tracking and alerts.”
- “Financial literacy positively impacts money management ability (Negara, 2022), cited in the paper to justify the need for financial education within financial management systems.”

**Limits of relevance:**

- Study population is education sector employees in Rizal Province (n=364), not necessarily representative of all Filipino young professionals (e.g., private sector, gig economy workers).
- No algorithm or ML method is evaluated; relevance is contextual for behavioral profiling requirements, not for forecasting or anomaly detection algorithms.
- Self-reported survey data may introduce social desirability bias, especially around saving and debt repayment.
- The paper does not address technology use, mobile app design, or data privacy, limiting direct application to Odin’s mobile-first or privacy modules.

### Limitations

- Sample limited to one province (Rizal) and one sector (education); findings may not generalize to all Filipino Gen-Zs. [unacknowledged]
- Cross-sectional design; cannot establish causality between money attitudes and financial well-being.
- Reliance on self-reported Likert scales; actual behavior may differ from reported attitudes.
- No validation of the newly developed money attitude scale beyond this study. [unacknowledged]
- Qualitative sample size and depth not fully described; thematic analysis may lack saturation.

---

## Source: `1.A/L--Rodriguez_et-al_2024_summarized.md`

**Title:** The Mediation of Financial Behavior to Financial Literacy and Spending Habits of Gen Z: An Exploratory Factor Analysis

### TL;DR

Financial behavior mediates the link between financial literacy and spending habits in Gen Z, with literacy directly influencing spending (coefficient 1.167) and indirectly through behavior (coefficient 0.797).

### Findings

1. Financial literacy and spending habits have a **strong positive correlation (r = 0.821, p < .001)**.
2. Direct effect of financial literacy on spending is **1.167** (unstandardized coefficient from SEM).
3. Financial behavior exerts a mediation effect of **0.797** on the literacy→spending relationship (behavior→spending path).
4. Financial literacy explains 51.9% of variance in financial behavior (R² = 0.519, F = 340.48, p < .001).
5. Construct reliability: financial behavior (Cronbach’s α = 0.75), spending (α = 0.68), literacy (α = 0.66).

- The indirect effect through behavior was significant (estimate 0.180, 95% CI [0.114, 0.245]).

### Relevance to Odin

**Topics:**

1.A — Filipino Young Professionals as a Demographic

1.C — Financial Behavior of Filipino Young Professionals

5.A — Financial Behavioral Profiles in Personal Finance

**Contribution to Odin:**

This paper directly supports Odin’s behavioral profiling module by demonstrating that financial behavior is not merely an outcome of literacy but a necessary mediator that transforms knowledge into spending action. For Odin, which targets Filipino young professionals, the finding that literacy alone explains only 52% of behavior variance means the system must actively measure and shape behavior through features like transaction logging and budget adherence tracking. The mediation evidence justifies why Odin should prioritize behavioral interventions (e.g., alerts, reminders) over pure financial education content. Even though the sample is Gen Z (18–25) rather than the full 20–40 range, the mechanism likely extends upward, and the methodological use of SEM provides a template for validating Odin’s own latent constructs.

**Directly justifies:**

- "Financial behavior mediates the relationship between financial literacy and spending habits, with a significant indirect effect (estimate = 0.180, 95% CI [0.114, 0.245])."
- "Financial literacy explains 51.9% of the variance in financial behavior, indicating that nearly half of behavioral variation is driven by other factors such as self-control and social influences."
- "The path from financial behavior to spending (coefficient = 0.797 in SEM) is comparable in magnitude to the direct literacy→spending path (1.167), making behavior a necessary target for intervention."
- "Reliability of financial behavior as a latent construct (Cronbach’s α = 0.75) supports its operationalization in a Philippine young adult sample."

**Limits of relevance:**

- Sample restricted to 18–25 year olds in Quezon City; may not fully represent young professionals aged 26–40 or other regions of the Philippines.
- No longitudinal data; causal direction claimed (literacy → behavior → spending) relies on cross-sectional SEM assumptions.
- Preprint not peer-reviewed; findings should be triangulated with published studies.
- Relies on self-reported spending, which may suffer from recall and social desirability bias.

### Limitations

- Cross-sectional design prevents establishing true causality despite SEM assumptions. [unacknowledged]
- Sample limited to four barangays in Quezon City, limiting generalizability to other Philippine urban or rural areas.
- Low convergent validity for spending (AVE = 0.415) and literacy (AVE = 0.404) — constructs may not be fully captured by indicators.
- No control for income level or personality traits, which the literature suggests also influence financial behavior.
- The study does not address digital financial behavior (e.g., e-wallet spending), which is highly relevant to Odin’s mobile-first context. [unacknowledged]

---

## Source: `1.A/L--Sanchez_2024_summarized.md`

**Title:** MOTIVATIONAL FACTORS AND BEHAVIORAL INTENTION TO INVEST IN PHILIPPINE STOCK MARKET AMONG MILLENNIAL AND GEN-Z INVESTORS IN CALAMBA CITY

### TL;DR

Motivational factors (financial knowledge, well-being, overconfidence, risk) show low positive correlation with behavioral intention to invest; Millennials and Gen Z differ in overconfidence and risk perception but share similar financial knowledge, well-being, and intention.

### Findings

1. Motivational factors were all **Observed** (means 2.65–2.94); Financial Well-being had highest composite mean (2.83) but indicator “I am behind with my finances” scored lowest (2.58).
2. Behavioral intention showed **Intention** across all three TPB components (means 2.57–3.05); Attitude had highest composite mean (3.05).
3. Significant differences existed between generations in Overconfidence Bias (p=0.048) and Investment Risk (p=0.000), but not in Financial Knowledge (p=0.195) or Financial Well-being (p=0.075).
4. No significant differences in any behavioral intention component (Attitude p=0.667, Subjective Norm p=0.818, Perceived Behavioral Control p=0.351).

- Motivational factors had a **low positive correlation** with behavioral intention (r values from .172 to .372, all p<0.01), rejecting the null hypothesis.
- A gap exists between financial aspirations and current financial status across both generations.

### Relevance to Odin

**Topics:**

1.A — Filipino Young Professionals as a Demographic

1.C — Financial Behavior of Filipino Young Professionals

5.A — Financial Behavioral Profiles in Personal Finance

**Contribution to Odin:**

This paper provides empirical evidence about the financial knowledge, well-being, overconfidence, and risk perceptions of Filipino young professionals (Millennials and Gen Z) in Calamba City, directly informing Odin’s user profiling and behavioral modeling. The finding that respondents have “Observed” financial knowledge yet feel “behind with their finances” (mean 2.58 on a 4-point scale) supports Odin’s design assumption that financial literacy alone does not guarantee financial well-being — a gap that budget recommendation and anomaly detection modules must address. The low positive correlation between motivational factors and behavioral intention (r up to .372) suggests that improving a user’s financial knowledge or risk awareness has limited direct impact on their intention to act, justifying Odin’s focus on practical, system-driven nudges rather than purely educational content.

**Directly justifies:**

- “Filipino Millennial and Gen Z graduates in Calamba City demonstrate observed financial knowledge (mean 2.76) but report being ‘behind with their finances’ (mean 2.58), indicating an aspiration-reality gap in financial well-being.”
- “Overconfidence bias is observed (mean 2.65), with respondents confident in evaluating securities (2.89) but less confident in earning above-average returns (2.50), suggesting a calibration gap relevant to behavioral profiling.”
- “Motivational factors (financial knowledge, well-being, overconfidence, risk) have a low positive correlation (r = .172 to .372) with behavioral intention to invest, meaning education alone is unlikely to drive engagement without system-mediated support.”
- “There is no significant difference between Millennials and Gen Z in financial knowledge or well-being (p>0.05), supporting a unified profiling approach across these generations on those dimensions, but significant differences exist in overconfidence (p=0.048) and risk perception (p=0.000), requiring age-sensitive tuning.”

**Limits of relevance:**

- Study focuses on stock market investment, not personal budgeting or spending tracking — the dependent variable (behavioral intention) is about buying stocks, not using a budget management system.
- Sample is limited to LCBA graduates (college-educated) in Calamba City, not representative of all Filipino young professionals, especially those without higher education or in different regions.
- No algorithm or computational model is tested; the paper is a behavioral survey using TPB, not an evaluation of any ML or statistical technique that Odin would deploy.
- Findings rely on self-reported Likert scales, not observed financial behavior or transaction data, which limits direct transferability to system design decisions.

### Limitations

- Generalizability limited to LCBA college graduates in Calamba City; not representative of all Filipino young professionals, especially non-graduates or those in other cities.
- Self-reported data may be subject to social desirability bias, particularly for overconfidence and financial well-being items. [unacknowledged]
- Cross-sectional design measures intention, not actual investment behavior; intention-action gap is not assessed.
- No validation of the adopted instrument beyond Cronbach’s alpha; no factor analysis or test-retest reliability reported.
- Study does not control for income level, employment status, or prior investment experience, which may confound the observed differences between generations.

---

## Source: `1.B/L--Am-una_2026_summarized.md`

**Title:** Beyond Awareness: Examining Financial Behaviors Among Public School Teachers in the Philippines

### TL;DR

Teachers show moderately positive financial behaviors (mean=2.69) driven by conscious constraint — budgeting is hardest despite frequent practice, and seminars have no effect.

### Findings

1. General weighted mean of financial behaviors = **2.69 (moderately positive)** on a 4-point scale, with "making ends meet" strongest (2.90) and active saving weakest (2.43).
2. Significant difference by marital status (p = .017): single teachers outperform married teachers (Tukey HSD p = .034).
3. Master Teachers score significantly higher (mean = 3.00) than non-Master Teachers (mean = 2.65, p = .002).
4. No significant difference between financial literacy seminar attendees and non-attendees (both means = 2.69, p = .991).

- Budgeting is perceived as most difficult (mean = 2.17) yet performed frequently (mean = 2.68) — a "conscious constraint" paradox where disciplined management occurs under limited income.
- Choosing financial products is perceived as easiest (mean = 4.15) despite low ownership (mean = 2.45), suggesting overconfidence from limited exposure.

### Relevance to Odin

**Topics:**

1.B — Financial Structure of Filipino Young Professionals

1.C — Financial Behavior of Filipino Young Professionals

2.A — Culturally Specific Financial Practices

4.B — Limitations and Gaps in Existing Systems

5.A — Financial Behavioral Profiles in Personal Finance

7.A — Budgeting Strategies as Domain Knowledge

**Contribution to Odin:**

This paper directly informs Odin's understanding of the knowledge-action gap in Filipino financial behavior, demonstrating that positive behavioral scores often mask structural constraint rather than mastery — a critical insight for designing realistic budget recommendation algorithms. The finding that financial literacy seminars have no measurable effect on behavior justifies Odin's focus on behavioral infrastructure (automated tools, just-in-time coaching) over awareness-only interventions. The "conscious constraint" concept provides a behavioral profile archetype that Odin's profiling module can use to distinguish necessity-driven users from mastery-driven users, shaping how budget recommendations and anomaly alerts are calibrated.

**Directly justifies:**

- "Teachers demonstrate a weighted mean financial behavior score of 2.69/4.00 — moderately positive but sustained by compensatory strategies (loan dependence, bill prioritization) rather than financial security."
- "Budgeting is performed frequently (M=2.68) but perceived as the most difficult behavior (M=2.17), indicating that high-frequency budgeting signals endurance under scarcity, not skill mastery."
- "Financial literacy seminar attendance shows no significant effect on financial behavior (p=.991) — one-off informational interventions do not translate into practice without structural support."
- "Single teachers outperform married teachers (p=.034) due to lower household financial obligations, establishing marital status as a meaningful moderator of financial behavior."
- "Master Teachers score higher (M=3.00 vs 2.65, p=.002) because accumulated income and tenure enable deliberate financial practices, not because of greater knowledge."

**Limits of relevance:**

- Sample is public school teachers in Baguio City, not young professionals (20–40) in Metro Manila; income stability and debt structures may differ.
- Study does not evaluate any algorithm or ML method; relevance is conceptual (behavioral patterns, constraints) not technical.
- Cross-sectional design captures reported behavior, not objective transaction data; Odin's behavioral profiles rely on actual spending logs.
- No longitudinal tracking — cannot inform how profiles drift over time or how interventions affect behavior beyond a single measurement.

### Limitations

- Self-reported financial behavior may suffer from social desirability bias, inflating positive scores.
- Cross-sectional design cannot establish causality between marital status/rank and behavior differences. [unacknowledged]
- Single-city sample (Baguio) limits generalizability to other Philippine regions with different costs of living. [unacknowledged]
- No objective validation of financial behavior against bank or loan records.
- Interview sample (n=9) may not capture full range of teacher financial experiences, though saturation was reported.

---

## Source: `1.B/L--Bongalonta_et-al_2024_summarized.md`

**Title:** The Traditional Way of Saving Money Versus the Modern Style of Investment: The Financial Management Styles of Sorsogon State University (Sorsu) Bulan Campus Faculty Members

### TL;DR

Faculty members use both traditional (piggy bank, paluwagan) and modern (bank deposits, stocks) saving methods, but struggle with rising expenses, low financial literacy, debt, and delayed salaries.

### Findings

1. **60%** of faculty save only 0–15% of their income; 35% save 16–30%.
2. Majority (62.5%) earn ₱40,001–₱50,000 monthly, but 82.5% have expenses above ₱12,000.
3. **60%** are female, 53% aged 35–50, and 60% have less than 10 years of service.
- Traditional saving practices: budgeting, paluwagan (rotating savings), piggy bank, bank accounts.
- Modern investment practices: time deposits (30%) and stock investments (10%).
- Main problems: rising utility costs and unexpected expenses; lack of financial literacy; poor debt management (GSIS/Landbank loans consume large salary portions); low and delayed salaries (especially for non‑permanent staff).

### Relevance to Odin

**Topics:**

1.B — Financial Structure of Filipino Young Professionals

1.C — Financial Behavior of Filipino Young Professionals

2.A — Culturally Specific Financial Practices

4.B — Limitations and Gaps in Existing Systems

5.A — Financial Behavioral Profiles in Personal Finance

7.A — Budgeting Strategies as Domain Knowledge

**Contribution to Odin:**

This descriptive study of Filipino faculty members provides baseline evidence on income, expenses, savings rates, and behavioral patterns that directly inform Odin’s user profiling and budget recommendation modules. The finding that 60% of faculty save only 0–15% of income despite stable government salaries justifies Odin’s need for anomaly detection and spending‑leak identification. The prevalence of informal mechanisms (paluwagan, piggy bank) and recurring debt (GSIS loans) highlights culturally specific expense categories and financial obligations that Odin must accommodate. The self‑reported lack of financial literacy argues for Odin’s design to emphasize explainability and educational nudges over complex gamification.

**Directly justifies:**

- “Sixty percent of faculty members save less than 15% of their monthly income, indicating that even stable government salaries do not guarantee adequate savings without intelligent financial tools.”
- “Paluwagan (rotating savings) and piggy banks are used by 30% of respondents, demonstrating that informal saving mechanisms remain relevant and should be supported by digital personal finance systems.”
- “Delayed salaries and automatic GSIS loan deductions reduce available cash flow at the start of the month, a constraint that any budget recommendation algorithm must account for when scheduling budget periods.”
- “Lack of financial literacy is repeatedly cited as a barrier, supporting the inclusion of explainable recommendations and in‑app financial education in Odin.”

**Limits of relevance:**

- Sample is small (n=40) and specific to one provincial campus in Sorsogon, not representative of all Filipino young professionals.
- Study is descriptive, not algorithmic; it provides behavioral context but no benchmark for any AI/ML method.
- Data are self‑reported and may suffer from social desirability bias (e.g., underreporting expenses).
- No evaluation of any digital financial tool; claims about “modern investment” are generic and not tied to app‑based systems.

### Limitations

- Small sample size (40 faculty) limits statistical power and generalizability to other institutions or demographics.
- Relies entirely on self‑reported survey and FGD data; no objective financial records were examined. [unacknowledged]
- No longitudinal tracking; the study captures a single point in time, so seasonal spending patterns or changes in behavior are not observed.
- The “modern style of investment” discussion is superficial (only time deposits and stocks mentioned) and lacks technical depth on digital investment platforms.
- The proposed Bongalonta’s Financial Model is not validated or tested against any outcome metric.

---

## Source: `1.B/L--Canete_&_Liwanag_2024_summarized.md`

**Title:** A Phenomenological Reflection on Ubos-Biyaya and Petsa de Peligro: Capitalism’s Impact on Filipino Attitude of Spending and Church’s Proposition for an Inclusive Economy

### TL;DR

Ubos-biyaya (lavish spending) and petsa de peligro (pre-payday financial strain) are phenomenologically linked: capitalism's planned obsolescence conditions ubos-biyaya, which then produces petsa de peligro.

### Findings

- Ubos-biyaya is not mere impulsive buying but a **preconditioned outcome** of capitalism's planned obsolescence and cathedral-of-consumption design.
- Petsa de peligro emerges as an upshot of ubos-biyaya: the period when money runs low and payday feels far away.
- Capitalism creates a "throwaway culture" (Pope Francis) where persons are reduced to commodities and the poor are excluded from participation.
- 87% of Filipinos buy more than planned when shopping, compared to 75% of Americans (Lagman & Ocampo, 2017).
- The Church proposes an economy of inclusion based on solidarity, prioritizing life over appropriation of goods by the few.

### Relevance to Odin

**Topics:**

1.B — Financial Structure of Filipino Young Professionals

1.C — Financial Behavior of Filipino Young Professionals

2.A — Culturally Specific Financial Practices

2.B — Seasonal and Cyclical Spending Patterns

3.A — Expense Categorization Frameworks

3.B — Expense Category Design Considerations

5.A — Financial Behavioral Profiles in Personal Finance

**Contribution to Odin:**

This paper provides a cultural-behavioral lens for Odin's expense categorization and financial profiling by grounding the concepts of ubos-biyaya and petsa de peligro in Filipino spending habits. The analysis of impulsive buying as a response to planned obsolescence informs Odin's anomaly detection module, distinguishing between normal cultural spending cycles (payday splurge) and genuine over-expenditure. The cyclical nature of petsa de peligro (pre-payday scarcity) directly justifies Odin's spending forecasting module, which must account for payday-driven spending peaks and subsequent low-resource periods. Finally, the critique of capitalism's "throwaway culture" supports Odin's value-driven retention design, emphasizing financial sustainability over consumerist engagement.

**Directly justifies:**

- "Filipinos commonly spend their entire payday immediately upon receipt, leading to petsa de peligro (day of danger) before the next salary."
- "Impulsive buying behavior — spending without premeditation — is the animating force behind ubos-biyaya, where users purchase pseudo-needs rather than essentials."
- "Planned obsolescence intentionally limits product lifespan to stimulate repeat consumption, conditioning the ubos-biyaya attitude."
- "87% of Filipinos buy more than planned when shopping, compared to 75% of Americans (Lagman & Ocampo, 2017)."

**Limits of relevance:**

- Qualitative phenomenological study, not quantitative; findings are interpretive rather than empirically measured.
- No specific algorithm or model is proposed; relevance is conceptual and behavioral.
- The paper focuses on critique of capitalism rather than design of financial systems; direct implementation guidance is limited.
- Data on Filipino spending (e.g., 87% statistic) comes from a single study (Lagman & Ocampo, 2017) on male impulse buying, not generalizable to all genders or updated.

### Limitations

- Relies heavily on unpublished interviews (e.g., Amy Cundangan, Kyle Ramos) and non-peer-reviewed online sources (Pinoy Stop, personal blogs) for behavioral claims.
- The 87% statistic is from a 2017 study on male impulse buying in a specific context; not representative of all Filipino young professionals.
- No empirical validation of the phenomenological linkage; causal claims are argued rather than tested.
- The paper's theological and moral framing may introduce bias in analyzing economic behavior. [unacknowledged]
- Limited discussion of income variability and how petsa de peligro differs across income levels or employment types.

---

## Source: `1.B/L--Dimaranan_&_Dy_2025_summarized.md`

**Title:** Financial Management and Commitment to Sending Remittances of Filipina Wives in Virginia, United States

### TL;DR

Nine Filipina wives in Virginia all send monthly remittances ($40–500) to the Philippines, but emergency requests for extra money risk destabilizing their household budgets.

### Findings

- All nine participants send monthly monetary remittances ($40–$500) plus occasional *balikbayan* boxes; remittances cover household bills, education, food, medical expenses, and allowances.
- Households have different income sources and levels; some Filipina wives are dependent homemakers, while others work full‑time (salaries $2,400–$7,000/month) or part‑time.
- All families practice financial management by setting clear goals (short‑, mid‑, long‑term), maintaining a monthly budget (mentally or written), and **setting aside a desired monthly savings target of $1,000** for most households.
- Budget holders are mostly husbands (especially in American‑Filipina couples), but three households have Filipina wives as sole budget holders; financial decisions are typically joint.
- Emergency requests for additional remittances from families in the Philippines put monthly budgets and savings at risk of mismanagement.
- Commitment to remitting is a personal choice rooted in Filipino values (*utang‑na‑loob*, *pakikipagkapwatao*) and family‑centeredness, not an explicit arrangement.

### Relevance to Odin

**Topics:**

1.B — Financial Structure of Filipino Young Professionals

1.C — Financial Behavior of Filipino Young Professionals

2.A — Culturally Specific Financial Practices

3.A — Expense Categorization Frameworks

4.A — Landscape of Existing Personal Finance Systems

5.A — Financial Behavioral Profiles in Personal Finance

7.A — Budgeting Strategies as Domain Knowledge

8.A — Anomaly Detection in Personal Finance Systems

**Contribution to Odin:**

This paper provides qualitative evidence of how Filipino transnational families actually budget, prioritize spending categories, and handle unexpected financial demands – directly informing Odin’s category design and budget recommendation logic. The finding that emergency requests for extra remittances destabilize otherwise well‑managed budgets justifies Odin’s anomaly detection module, specifically the need to alert users when spending deviations occur due to external obligations. Although the study focuses on Filipina wives in the US, its documented patterns of income pooling, dual‑household budgeting, and culturally driven “debt of gratitude” spending are transferable to Filipino young professionals in Metro Manila who also support parents or siblings.

**Directly justifies:**

- “Filipino households practice financial management by having clear short‑, mid‑, and long‑term goals, with saving for children’s education and retirement as dominant long‑term priorities.”
- “Budgeting methods vary: more than half use mental budgeting (memorized allocation), while others use written logs or spreadsheets – supporting Odin’s flexible budget entry design.”
- “Unplanned remittance requests due to family emergencies put monthly budgets and savings at risk, demonstrating the need for anomaly detection that flags out‑of‑pattern spending.”
- “Filipino wives remit out of *utang‑na‑loob* (debt of gratitude) and family‑centeredness, not explicit contracts – implying that financial apps should allow users to declare protected spending categories for family obligations.”
- “Joint financial decision‑making is common, but budget holder roles vary by couple type (Filipino vs. American husband) – informing Odin’s assumption that single‑user personal finance may need to accommodate shared visibility.”

**Limits of relevance:**

- Sample size is very small (n=9) and limited to Virginia, USA – not representative of all Filipino young professionals in Metro Manila.
- All participants are married women with children; findings may not apply to single young professionals or different family structures.
- Income levels in the US ($5,000–$22,500 monthly) are far higher than typical Metro Manila incomes, so budget allocation proportions may not transfer directly.
- Qualitative study provides no quantitative benchmarks for algorithm design (e.g., forecast error rates, classification accuracy).

### Limitations

- Small, purposive sample (n=9) from a single US state – findings cannot be generalized to all Filipina wives or Filipino migrants.
- All numerical data (income, expenses, savings, remittances) are self‑reported estimates, not verified against bank records.
- Participants who are not the primary budget holder (especially those with American husbands) may have incomplete awareness of household finances. [unacknowledged]
- No longitudinal data – the study captures financial management at one point in time, missing how practices change over years.
- The paper does not compare remittance‑sending households to non‑remitting households, so it cannot isolate the causal effect of remittances on financial stability. [unacknowledged]

---

## Source: `1.B/L--Donato_et-al_2023_summarized.md`

**Title:** The Concept of Utang Na Loob Among Filipino Working Millenials

### TL;DR

Filipino working millennials view utang na loob as a fulfilling obligation to support family financially, but it can also become a burden when demands exceed their means.

### Findings

- Utang na loob is perceived as an obligation, but the urge to repay comes from an inner feeling (pakikiramdam), not external pressure.
- Reciprocity is voluntary (kusang loob) and rooted in recognizing the benefactor’s genuine kindness (kagandahang loob), strengthening pakikipagkapwa (shared identity).
- **Providing financial support to family (allowances, house expenses, necessities) is the primary way millennials express pagtanaw ng utang na loob.**
- Reciprocating family support generates happiness, fulfillment, and increased work motivation.
- Strong family obligation also leads to compromised personal well-being, financial strain, and sacrificed personal goals — revealing utang na loob’s negative side.
- Manifestations extend beyond family to workplace reciprocity (covering shifts, job referral gratitude) and borrowing from siblings/peers during salary delays or pandemic-related income loss.

### Relevance to Odin

**Topics:**

1.B — Financial Structure of Filipino Young Professionals

1.C — Financial Behavior of Filipino Young Professionals

2.A — Culturally Specific Financial Practices

**Contribution to Odin:**

This paper provides qualitative evidence that family obligation (utang na loob) directly shapes how Filipino working millennials allocate income — prioritizing allowances, household expenses, and parents’ needs even at the cost of their own financial security. Odin’s expense categorization and budget recommendation modules must account for this culturally specific “family support” category as a non-negotiable priority. The finding that utang na loob simultaneously generates fulfillment and financial strain informs Odin’s anomaly detection: sustained over-allocation to family may signal overextension rather than discretionary spending. Although the study is qualitative and geographically limited, its behavioral patterns are directly transferable to Metro Manila young professionals.

**Directly justifies:**

- “Filipino working millennials express utang na loob primarily through financial support to parents: allowances, house bills, necessities, and occasional vacations.”
- “Providing for family increases work motivation but also leads to compromised personal savings and sacrificed personal goals when family demands exceed income.”
- “Utang na loob extends to workplace reciprocity — covering colleague shifts and expressing gratitude for job referral assistance — indicating that financial management systems should consider social repayment dynamics.”
- “Salary delays and pandemic-related income loss forced working millennials to borrow from siblings and peers, creating additional utang na loob obligations.”

**Limits of relevance:**

- Qualitative study with 30 participants from a single city (Tuguegarao), not statistically generalizable to all Filipino young professionals.
- No quantitative measurement of spending patterns or budget allocation percentages.
- Does not evaluate any algorithmic or system design; provides behavioral domain knowledge only.
- Focuses on cultural value rather than financial literacy or budgeting practices directly.

### Limitations

- Small sample size (n=30) from one geographic area limits generalizability across Metro Manila and other regions.
- Self-reported interview data may be subject to social desirability bias (e.g., overstating family support).
- No longitudinal data; captures current perceptions but not how utang na loob obligations change over time. [unacknowledged]
- Does not quantify the financial burden (e.g., percentage of income allocated to family), making direct integration into budget algorithms difficult. [unacknowledged]
- Relies on thematic analysis without inter-rater reliability metrics.

---

## Source: `1.B/L--Flores_2025_summarized.md`

**Title:** Financial freedom of Filipinos in personal finance management

### TL;DR

Filipino corporate workers exhibit poor cash and debt habits rooted in traditional attitudes, yet regression analysis finds no significant contribution of cash, debt, risk, or wealth management to financial freedom.

### Findings

1. **57% male**, 63% married, 43% aged 31–40, 57% have 1–2 children.
2. 40% rank‑and‑file, 50% working 11–18 years, 40% earning ₱30,000+ monthly.
3. Cash management weighted mean 3.73 (agree that leaving cash at home risks theft/fire).
4. Debt management weighted mean 3.7 (agree to pay high‑interest debt first and more than minimum).
5. Risk management weighted mean 3.65 (agree that lack of health coverage can erase investments).
6. Wealth management weighted mean 3.7 (agree early investing builds positive spending habits).

- Regression analysis found **no significant contribution** of any of the four variables to financial freedom.

### Relevance to Odin

**Topics:**

1.B — Financial Structure of Filipino Young Professionals

1.C — Financial Behavior of Filipino Young Professionals

2.A — Culturally Specific Financial Practices

4.B — Limitations and Gaps in Existing Systems

5.A — Financial Behavioral Profiles in Personal Finance

**Contribution to Odin:**

This paper provides empirical evidence of Filipino financial behaviors — cash hoarding, debt reliance for emergencies, traditional “alkansya” saving, and avoidance of bank savings — that directly inform Odin’s user profiling and culturally grounded expense categories. The finding that the four standard management dimensions (cash, debt, risk, wealth) do **not** significantly predict financial freedom suggests Odin should look beyond textbook finance variables to factors like income volatility, family obligations, and informal financial mechanisms. The documented distrust of banks and preference for physical cash storage justify Odin’s assumption that users will enter transactions manually rather than via bank APIs, and support the need for educational nudges about emergency funds and deposit insurance.

**Directly justifies:**

- “Filipino corporate workers commonly store cash at home due to distrust of banks (bankruptcy, inflation fears), increasing theft and loss risk (weighted mean 3.73).”
- “Most respondents agree that paying high‑interest debt first and paying more than the minimum are effective debt management strategies, yet regression analysis shows debt management alone does not predict financial freedom.”
- “Forty percent of respondents earn ₱30,000+ monthly, but 40% hold rank‑and‑file positions earning near minimum wage, indicating income segmentation that Odin’s profiling must capture.”
- “Regression analysis found no significant contribution of cash, debt, risk, or wealth management to financial freedom (p > 0.05), suggesting unmeasured factors — such as income stability, family support obligations, or cultural ‘come‑what‑may’ attitudes — drive financial independence.”
- “Many Filipinos avoid life insurance due to perceptions that it is ‘not required, intangible, lack of funds, just an expense,’ informing Odin’s risk management education module.”

**Limits of relevance:**

- Sample limited to employees of ten large corporations (mainly Luzon), not representative of all Filipino young professionals (e.g., freelancers, overseas workers, informal sector).
- No causal inference; linear regression may miss nonlinear effects, interactions, or domain‑specific drivers of financial freedom.
- Self‑reported survey data subject to social desirability bias (respondents may overstate good financial habits).
- Study does not evaluate any digital financial tool or mobile interface; relevance is to user behavior and cultural context, not system architecture or algorithm performance.

### Limitations

- Convenience sample from large corporations only; findings may not generalize to self‑employed, informal, or rural Filipinos. [unacknowledged]
- No validation of regression assumptions (e.g., multicollinearity, linearity) reported; the “no significant contribution” conclusion may be an artifact of model misspecification. [unacknowledged]
- Financial freedom operationalized via a single survey item without external validation (e.g., actual savings, debt‑to‑income ratio). [unacknowledged]
- Data collected during 2020–2021 (pandemic period); behavior may differ from normal economic conditions. (Acknowledged implicitly by date, but not discussed.)

---

## Source: `1.B/L--Lopez_2025_summarized.md`

**Title:** Beyond the Beach: Micro-Entrepreneurship Survival in Philippine Tourism Enclaves

### TL;DR

Philippine tourism micro-entrepreneurs face recurring compound disruptions and deploy culturally embedded survival strategies (utang na loob, bayanihan, paluwagan), but a resilience trap excludes the most vulnerable from transformative adaptation.

### Findings

1. Six major disruption events occurred between 2013–2024 (COVID-19, Boracay closure, Typhoon Haiyan, Bohol earthquake, Taal eruption, Zamboanga crisis) with an average inter-disruption interval of less than two years.
2. Compound disruption dynamics progressively deplete adaptive capacity; pre-crisis savings for most micro-entrepreneurs covered fewer than two months of operating expenses (PIDS, 2021).
3. **Only 38%** of tourism micro-enterprises in enclave destinations held valid business permits, excluding the majority from government relief programs (DTI, 2021).
4. Social capital mechanisms (utang na loob, bayanihan, paluwagan) are the primary survival asset for informal operators, compensating for inaccessible formal credit.

- The four-quadrant typology reveals a “resilience trap”: the most vulnerable operators (informally registered, island-based, women-operated, low-capitalization) are confined to short-term quadrants (contraction and social capital activation) and cannot access long-term transformative strategies (internal transformation and institutional engagement).
- Women-operated micro-enterprises show stronger social capital activation but face greater barriers to institutional credit (ILO, 2020).

### Relevance to Odin

**Topics:**

1.B — Financial Structure of Filipino Young Professionals

2.A — Culturally Specific Financial Practices

**Contribution to Odin:**

This paper documents how Filipino micro-entrepreneurs rely on informal financial mechanisms (utang na loob, paluwagan) and community solidarity (bayanihan) as primary survival strategies during income disruptions. These culturally specific practices directly inform Odin’s understanding of financial behavior in the Philippine context, particularly for users with irregular or volatile income. The finding that variable-income users face greater constraints in accessing formal support (e.g., credit) reinforces the need for Odin’s design to accommodate income typology. While the demographic is tourism micro-entrepreneurs, the social capital mechanisms generalize to Filipino young professionals who also use paluwagan and family-based credit.

**Directly justifies:**

- “Paluwagan (rotating savings associations) serve as de facto microfinance institutions during income disruptions, providing capital access when formal credit is unavailable (Lopez, 2026).”
- “Filipino micro-entrepreneurs have pre-crisis savings covering fewer than two months of operating expenses, indicating extreme financial fragility and high sensitivity to income shocks (PIDS, 2021).”
- “Utang na loob networks are the primary source of informal credit for unbanked Filipino operators, surpassing formal microfinance in both speed and accessibility (Paguia, 2018).”
- “Compound disruption dynamics progressively deplete adaptive capacity, meaning that single-event recovery support is insufficient for users facing sequential income shocks.”

**Limits of relevance:**

- Demographic is tourism micro-entrepreneurs in enclave destinations, not young professionals in Metro Manila; income sources and spending patterns differ.
- The paper does not address personal finance management systems, budgeting, or algorithmic modules.
- Findings are qualitative and secondary; no quantitative benchmarking of classification or forecasting algorithms.
- The context is economic disruption (pandemic, typhoon, closure), not routine personal finance tracking.

### Limitations

- Secondary data corpus geographically concentrated in Boracay and Palawan; underrepresented destinations (Samar-Leyte, Camiguin) may yield different survival patterns.
- No primary data collection; findings are bounded by the quality and framing of existing government and institutional reports.
- Gender analysis is underdeveloped in the Philippines-specific sources; most findings on gender are extrapolated from regional ILO reports. [unacknowledged]
- The study cannot establish causal relationships between structural conditions and survival outcomes; only associations.
- Rapidly evolving post-pandemic policy environment may render some institutional findings outdated.

---

## Source: `1.C/L--Aquino_et-al_2026_summarized.md`

**Title:** A Systematic Literature Review: Present Bias versus Financial Literacy as Determinants of Savings Behavior Among Entrepreneurs

### TL;DR

Present bias more strongly predicts poor savings than financial literacy among entrepreneurs; knowledge improves savings only when paired with high self-control.

### Findings

- **Present bias consistently overrides financial literacy as a predictor of poor savings** – even literate entrepreneurs engage in impulsive spending when present bias is strong.
- Financial literacy’s impact is conditional: it improves savings only among entrepreneurs with high self-control; without self-control, knowledge fails to translate into action.
- Self-control moderates the literacy–savings relationship, reframed as an emotional struggle (immediate rewards vs. long-term planning) rather than a simple cognitive trade-off.
- Most studies (78%) used primary data, predominantly cross-sectional surveys in Asian contexts, limiting causal claims.
- Behavioral interventions (commitment devices, automated savings, framed reminders) are more effective than financial education alone.

### Relevance to Odin

**Topics:**

1.C — Financial Behavior of Filipino Young Professionals

5.A — Financial Behavioral Profiles in Personal Finance

7.B — Budget Recommendation in Personal Finance Systems

8.A — Anomaly Detection in Personal Finance Systems

11.A — Engagement Dynamics in Personal Finance Applications

**Contribution to Odin:**

This paper directly informs Odin’s behavioral profiling module by establishing present bias as a stronger predictor of poor savings than financial literacy – justifying inclusion of bias indicators in user profiles. For budget recommendation, the finding that literacy only works with self-control suggests Odin must embed behavioral guardrails (e.g., commitment devices) rather than assume knowledge alone changes behavior. The review also supports Odin’s anomaly detection design: present bias-driven impulsive spending represents a predictable deviation pattern that can trigger alerts. Finally, the knowledge-behavior gap explains why users may disengage despite financial education, reinforcing Odin’s value-driven retention strategy.

**Directly justifies:**

- “Present bias leads to impulsive spending even among financially literate entrepreneurs, directly reducing savings – a pattern that overrides the effect of financial knowledge alone.”
- “Financial literacy improves savings behavior only when entrepreneurs possess high self-control; without self-control, literacy fails to translate into action (Mpaata et al., 2021).”
- “Behavioral interventions – commitment devices, automated savings defaults, and framed reminders – are more effective than pure financial education in promoting savings behavior.”
- “Cross-sectional surveys dominate the literature (78% of studies), limiting causal inference about the literacy-bias-savings relationship.”
- “Present bias persists across developing economies including the Philippines, as shown in RCTs with Filipino entrepreneurs (McKenzie et al., 2022).”

**Limits of relevance:**

- The review targets entrepreneurs, whose income volatility and business expenses differ from general young professionals – direct transferability requires validation.
- Most studies are cross-sectional and Asia-focused, limiting causal claims for Metro Manila’s specific context.
- No study in the review evaluated mobile-first personal finance apps or manual transaction entry; findings come from survey and experimental contexts.
- The review does not compare specific ML algorithms (e.g., LSTM vs. GRU) for detecting present-bias-driven anomalies.

### Limitations

- Heavy reliance on cross-sectional designs (acknowledged) – cannot establish causality between present bias and savings outcomes.
- Geographical concentration in Asia (56% of studies) – may not fully generalize to other regions, though Filipino studies are present. [unacknowledged]
- No longitudinal tracking of how present bias changes over time – relevant to Odin’s profile dynamics. [unacknowledged]
- Exclusion of grey literature (conference papers, dissertations) may introduce publication bias.
- Does not address how present bias interacts with mobile UX or manual data entry friction. [unacknowledged]

---

## Source: `1.C/L--Bancoro_et-al_2025_summarized.md`

**Title:** The Role of Financial Literacy in Supporting Employee Work-Life Balance

### TL;DR

Filipino employees have moderate financial literacy (8.35/13) and positive attitudes/behaviors, but financial literacy shows no significant correlation (ρ=0.11, p=0.191) with work-life balance.

### Findings

1. Mean financial knowledge score: 8.35/13 (SD=3.13), indicating moderate literacy with high variability.
2. Mean attitude score: 3.99/5 (SD=0.73) — positive; mean behavior score: 3.94/5 (SD=0.58) — positive.
3. **Correlation between financial literacy and work-life balance: ρ=0.11, p=0.191 — not statistically significant.**

- Employees reported positive work-life balance (overall mean 4.06/5), with strongest ratings for family time (4.33) and coworker relationships (4.24).
- Qualitative themes: Financial literacy reduces stress and enables better focus, but work-life balance depends more on time management and organizational support.

### Relevance to Odin

**Topics:**

1.C — Financial Behavior of Filipino Young Professionals

5.A — Financial Behavioral Profiles in Personal Finance

7.A — Budgeting Strategies as Domain Knowledge

**Contribution to Odin:**

This paper provides baseline empirical data on Filipino employees' financial literacy levels, attitudes, and behaviors (budgeting, saving, goal-setting) that directly inform Odin's user profiling module by quantifying typical financial competence and behavioral patterns. The finding that financial literacy correlates weakly with work-life balance suggests that Odin should prioritize practical behavioral tools (budget tracking, alerts) over pure educational content, as knowledge alone does not drive balance. The qualitative mention of budgeting apps (Mint, YNAB) among Filipino respondents supports Odin's mobile-first design and indicates user familiarity with digital financial tools, reducing adoption friction.

**Directly justifies:**

- "Filipino employees have a mean financial knowledge score of 8.35/13 (SD=3.13), indicating moderate literacy with substantial individual variation."
- "Employees report positive financial behaviors including having a spending plan (M=3.91/5) and saving part of monthly income (M=4.08/5)."
- "Budgeting apps like Mint and YNAB are recognized by Filipino employees as tools that support financial management."
- "The gap between financial knowledge and application persists: some employees know concepts but do not use budgeting tools, highlighting the need for behavior-focused design."

**Limits of relevance:**

- Sample consists of university faculty and staff, not specifically young professionals aged 20–40; income and spending patterns may differ.
- Study focuses on work-life balance, not personal finance system usage or algorithm performance.
- Financial literacy measurement is basic (13-item knowledge test), not tailored to PFMS-specific constructs like expense categorization or forecasting.
- No evaluation of manual transaction entry or cold-start user behavior; Odin's manual input constraint is not addressed.

### Limitations

- Weak correlation (ρ=0.11) may be due to small sample size (n=140) or non-normal data; p=0.191 indicates no significance.
- Self-reported measures subject to social desirability bias [unacknowledged].
- No control for income level or occupation type beyond six-month employment minimum.
- Cross-sectional design cannot establish causality between financial literacy and work-life balance.
- Geographic limitation: single university in Dumaguete City, not representative of all Filipino employees.

---

## Source: `1.C/L--Bongado_et-al_2025_summarized.md`

**Title:** INFLUENCE OF DIGITAL WALLETS ON THE FINANCIAL BEHAVIOR OF HEI’S STUDENTS

### TL;DR

Digital wallet usage positively influences HEI students' financial behavior, accounting for 45.4% of variance in cash management and budgeting practices.

### Findings

1. Students agreed with all digital wallet determinants (M = 2.91–2.99). Attractiveness of Alternatives had the lowest variability (SD = 0.77); Perceived Trust had the highest (SD = 1.24).
2. Financial behavior means: Cash Management M = 2.97 (SD = 0.85), Financial Planning & Budgeting M = 3.00 (SD = 0.84), overall M = 2.99 (SD = 0.68).
3. Regression analysis showed digital wallet usage significantly predicts financial behavior (R² = 0.454, β = 0.673, p < .001).

- **45.4% of variance** in financial behavior is explained by digital wallet usage.

### Relevance to Odin

**Topics:**

1.C — Financial Behavior of Filipino Young Professionals

4.A — Landscape of Existing Personal Finance Systems

7.A — Budgeting Strategies as Domain Knowledge

**Contribution to Odin:**

This paper demonstrates that digital wallet usage positively correlates with responsible financial behavior, including budgeting and cash management, among Filipino HEI students. For Odin, this finding supports the design decision to integrate features that reinforce budgeting practices, as users who adopt digital payment methods show improved financial discipline. The regression result—45.4% of financial behavior variance explained by digital wallet use—provides a benchmark for how much technology adoption can influence user outcomes, informing Odin's value proposition and retention strategy.

**Directly justifies:**

- "Digital wallet usage accounts for 45.4% of variance in HEI students' financial behavior, including cash management and budgeting (p < .001)."
- "Filipino students generally perceive digital wallets as easy to use, useful, and valuable, with strong intention to use (M = 2.96)."
- "Perceived trust shows the highest variability (SD = 1.24), indicating that trust concerns remain a differentiating factor in adoption."
- "Financial planning and budgeting (M = 3.00) is slightly higher than cash management (M = 2.97), suggesting proactive budgeting is practiced among students."

**Limits of relevance:**

- Sample is HEI students in a rural coastal town, not young professionals in Metro Manila; income and spending patterns may differ.
- Digital wallets are payment tools, not full PFMS; Odin focuses on manual input without banking integration, so direct technology transfer is limited.
- The paper does not evaluate long-term behavioral change or cold-start scenarios for new users.

### Limitations

- Sample limited to one state university campus; not representative of all Filipino HEI students or young professionals. [unacknowledged]
- Self-reported financial behavior may overstate responsible practices due to social desirability bias.
- Cross-sectional design cannot establish causality between digital wallet usage and improved financial behavior.
- No control for financial literacy level, which may confound the observed relationship. [unacknowledged]

---

## Source: `1.C/L--Carpizo_et-al_2024_summarized.md`

**Title:** The Impact of AUP-CES Livelihood Initiatives, Leadership and Management in Buklod Bahayan

### TL;DR

AUP‑CES livelihood and leadership training enabled a Filipino community cooperative to achieve economic gains, social cohesion, and organizational resilience, sustaining operations for 10 years.

### Findings

1. Members’ share grew from ₱1,000 to **₱3,300** in one year; dividends on a ₱3,300 share reached ₱5,580.
2. The cooperative started with 5 members, grew to 20, and operated for **10 years** after a previous cooperative failed.

- **Economic impact**: alternative income, loans based on membership and loyalty, purchase discounts.
- **Social impact**: camaraderie, mutual help, sense of unity, security during crises and emergencies.
- **Organizational impact**: members learned accounting, leadership, and management from AUP‑CES seminars; those skills and lessons from past failure enabled them to reorganize and sustain the cooperative.

### Relevance to Odin

**Topics:**

1.C — Financial Behavior of Filipino Young Professionals

2.A — Culturally Specific Financial Practices

4.A — Landscape of Existing Personal Finance Systems

**Contribution to Odin:**

This paper documents that Filipino communities actively use *paluwagan* (rotating savings) as a trusted informal financial mechanism, which directly informs Odin’s need to accommodate such culturally specific practices in its expense categorization and budget design. The finding that members value access to emergency loans over dividend returns highlights that security and crisis resilience are primary user priorities — a behavioral insight that can shape Odin’s anomaly detection and alert features. Although the study examines a community cooperative rather than a personal app, the demonstrated role of structured training in building financial resilience suggests that Odin’s educational or onboarding content could similarly improve user outcomes.

**Directly justifies:**

- “Filipino cooperative members prioritize access to emergency loans over financial returns, valuing crisis security as the primary benefit of pooled savings.”
- “Paluwagan (rotating savings) groups in the Philippines succeed because they are built on social cohesion and mutual trust, not purely economic incentives.”
- “Leadership and management training enabled a cooperative to survive an initial failure and sustain operations for 10 years, demonstrating that capacity‑building is critical for financial resilience.”
- “Community cooperatives in the Philippines provide dividends, low‑interest loans, and purchase discounts — features that are directly comparable to the benefits users expect from a personal finance system.”

**Limits of relevance:**

- The study focuses on a community cooperative (group savings/loan organization), not an individual personal finance management system.
- Participants are homeowners association members, not specifically the young professional demographic (20–40) that Odin targets.
- Qualitative findings are from a single subdivision in Cavite; generalizability to Metro Manila or other regions is untested.
- No digital or mobile component is evaluated; the paper offers behavioral insights, not technical design guidance.

### Limitations

- Small sample (one cooperative, <20 members) and single geographic location limit external validity.
- Qualitative methods only; no quantitative causal inference or statistical significance testing.
- The paper does not evaluate the training’s specific content or delivery length, making replication difficult. [unacknowledged]
- No comparison group (e.g., cooperatives without AUP‑CES training) to isolate the training’s effect.
- Retrospective self‑reports may be subject to recall bias and social desirability.

---

## Source: `1.C/L--Cervantes_et-al_2025_summarized.md`

**Title:** The Effect of Online Buying Decision on Personal Budget of Business Administration Students

### TL;DR

Social media engagement, instant gratification, and marketing tactics drive online buying decisions that significantly disrupt personal budgeting among Filipino business administration students.

### Findings

1. Mean online buying decision score was **3.02 (High)** ; highest influence from “likes and positive comments” (M=3.10) and “social media platforms” (M=3.05).
2. Mean personal budget score was **3.15 (High)** ; “necessary expenses” rated highest (M=3.32, Very High).
3. Pearson’s r = **0.612** (p < 0.05) → strong, significant positive relationship between online buying decisions and personal budgeting (i.e., higher online buying is associated with poorer budget management).

- Age significantly affected allowance, expenditure, and savings (p < 0.05).
- Civil status significantly affected allowance and savings (p < 0.05).
- Sex did not affect allowance or expenditure but did affect savings (p < 0.05).

### Relevance to Odin

**Topics:**

1.C — Financial Behavior of Filipino Young Professionals

5.A — Financial Behavioral Profiles in Personal Finance

7.A — Budgeting Strategies as Domain Knowledge

8.A — Anomaly Detection in Personal Finance Systems

**Contribution to Odin:**

This paper directly supports Odin’s design by providing empirical evidence that social media engagement and impulsive buying are strongly correlated (r=0.612) with poor budget management among Filipino students — a demographic similar to Odin’s target young professionals. It confirms that emotional and social triggers weaken financial control, which justifies Odin’s need for anomaly detection that distinguishes between planned vs. impulse‑driven spending. The finding that age and civil status affect budgeting outcomes reinforces Odin’s requirement for dynamic user profiling that adapts to life‑stage changes, not just income levels.

**Directly justifies:**

- “Social media engagement features (likes, comments, shares) significantly shape purchase intentions among Filipino young adults, with mean influence scores of 3.10 out of 4.00.”
- “Online buying decisions and personal budgeting share a strong positive correlation (r = 0.612, p < 0.05), meaning higher impulsive online spending reliably predicts poorer budget adherence.”
- “Younger students (18‑24) show different spending and saving patterns than older peers, indicating that age must be a profiling feature for financial behavior prediction.”
- “Instant gratification motives — stress relief, mood improvement, identity expression — drive impulsive purchases that directly disrupt monthly budgeting.”

**Limits of relevance:**

- Sample limited to business administration students in a rural campus; results may not generalize to all Filipino young professionals (e.g., employed vs. student, Metro Manila vs. provincial).
- The study is correlational, not causal; directionality of the relationship (online buying → poor budget) is assumed but not experimentally established.
- No longitudinal data; the strength of the relationship over time and seasonal spending cycles (e.g., 13th month pay) is unknown.
- Manual survey data only; no transaction‑level objective spending logs used, which may inflate self‑report bias.

### Limitations

- Single‑campus, single‑degree sample (n=153) limits external validity to other student populations or employed young professionals.
- Self‑reported budgeting behavior may suffer from social desirability bias (students over‑report good budgeting habits). [unacknowledged]
- No control for digital literacy or prior financial education, which could moderate the observed relationship.
- Cross‑sectional design cannot establish causality; poor budgeting might also cause more online buying (reverse causation). [unacknowledged]

---

## Source: `1.C/L--Dela-Rama_et-al_2024_summarized.md`

**Title:** Assessing the Financial Literacy of Senior High School and College Students: A Comprehensive Analysis

### TL;DR

Filipino senior high and college students have basic financial knowledge (mean ~2.1/4) but large gaps in compound interest understanding and consistent budgeting, with no gender differences.

### Findings

1. Financial knowledge weighted mean: SHS = 2.10, College = 2.11 (basic understanding, scale 1–4).
2. Financial behavior weighted mean: SHS = 1.92, College = 1.85 (moderate proficiency).
3. **Less than 30% of students could correctly explain compound interest** or calculate APY.

- Students report inconsistent budgeting practices and difficulty sticking to budgets when unexpected expenses arise.
- No significant gender differences in any financial literacy dimension (Welch’s t-test, p > 0.05).

### Relevance to Odin

**Topics:**

1.C — Financial Behavior of Filipino Young Professionals

**Contribution to Odin:**

This paper provides empirical baseline data on financial behavior gaps among young Filipinos, directly informing Odin’s UX and feature design. The finding that students struggle with compound interest and consistent budgeting explains why Odin must include simple, just-in-time explanations for financial concepts and flexible budget adjustment tools. The absence of gender differences supports gender-neutral design choices. Although the sample consists of students, their reported behavioral patterns (e.g., difficulty handling unexpected expenses) are directly transferable to Odin’s target demographic of young professionals.

**Directly justifies:**

- “Filipino SHS and college students have basic financial knowledge (mean 2.1/4) but large gaps in compound interest understanding, with less than 30% able to explain it.”
- “Students report inconsistent budgeting practices and difficulty staying within budgets when unexpected expenses occur, indicating a need for flexible budget adjustment features.”
- “No significant gender differences in financial literacy were found among Filipino students, suggesting gender-neutral design is appropriate for personal finance tools.”
- “Most students learn finance from family rather than formal education, implying that Odin’s explanations should complement existing informal financial socialization.”

**Limits of relevance:**

- Sample is students (not employed young professionals) from a single institution in Mindanao, not Metro Manila.
- Study measures self‑reported literacy and behavior, not actual transaction data or PFMS usage.
- No evaluation of digital financial tools or mobile app contexts.

### Limitations

- Single‑institution sample in Mindanao limits generalizability to Metro Manila young professionals.
- Cross‑sectional design cannot establish causation between education and financial behavior. [unacknowledged]
- Self‑reported Likert responses may overstate actual financial skills (social desirability bias). [unacknowledged]
- No measure of income or employment status, so findings may not reflect spending patterns of working adults.
- Study does not assess how literacy translates to real‑world financial decisions under pressure.

---

## Source: `1.C/L--Espelita_et-al_2025_summarized.md`

**Title:** Understanding Monetary Policy: Student Awareness, Perceptions, and Financial Behaviors in the Philippine Context

### TL;DR

Filipino students have moderate monetary policy awareness; graduate and business/economics students score higher, and awareness predicts saving and investing but not spending.

### Findings

1. Overall monetary policy awareness is moderate (M ~3.2/5); graduate students (M=3.75) and business/economics students (M=3.48) scored **significantly higher** than senior high (M=2.80) and non‑business peers (M=3.02–3.16).
2. Age and educational level predict awareness (F=14.62 and 47.83, both p<.001); gender shows no significant difference.
3. Awareness correlates positively with saving (r=0.31, p<.001) and investing (r=0.24, p=.001) but not with spending (r=−0.07, p=.310).
4. Regression: awareness + perceptions explain 22% of saving variance and 15% of investment variance, but only 4% of spending variance.
5. Students view monetary policy as effective for controlling inflation but are more cautious about its impact on employment and long‑term growth.

### Relevance to Odin

**Topics:**

1.C — Financial Behavior of Filipino Young Professionals

5.A — Financial Behavioral Profiles in Personal Finance Systems

**Contribution to Odin:**

This paper provides empirical evidence on how demographic factors (age, education, academic program) and awareness of economic policy influence saving, investing, and spending behaviors among Filipino students — directly applicable to Odin’s user profiling and behavioral prediction modules. The finding that awareness predicts saving and investing but not spending justifies Odin’s design choice to prioritize long‑term financial goal tracking (savings, investments) over short‑term consumption nudges. The documented disparities by educational background and program of study underscore the need for adaptive user models that adjust for users’ financial literacy levels, which Odin’s classification module can leverage to personalize budget recommendations.

**Directly justifies:**

- “Monetary policy awareness is positively correlated with saving behavior (r=0.31, p<.001) and investment behavior (r=0.24, p=.001) among Filipino students, but shows no significant relationship with spending behavior (r=−0.07, p=.310).”
- “Graduate students and business/economics majors exhibit significantly higher economic literacy than senior high and non‑business peers, indicating that educational exposure shapes financial awareness.”
- “Awareness and perceptions together explain 22% of the variance in saving behavior and 15% of investment behavior, supporting the TRA/TPB chain from knowledge to attitude to action.”
- “Age (F=14.62, p<.001) and educational level (F=47.83, p<.001) are stronger predictors of monetary policy awareness than gender (t=0.31, p=.756), suggesting that life experience and coursework matter more than sex.”

**Limits of relevance:**

- The study measures monetary policy awareness, not personal finance system usage or budgeting behavior; direct extrapolation to Odin’s budget recommendation algorithm is indirect.
- Sample includes senior high and graduate students, whereas Odin targets young professionals (20–40); however, the 19–22 and 23–30 age brackets overlap with the target.
- Financial behaviors are self‑reported and may not reflect actual transaction‑level actions in a mobile app.
- No evaluation of how awareness translates into digital financial tool adoption or retention.

### Limitations

- Cross‑sectional design prevents causal inference; directionality between awareness and behavior is assumed but not proven.
- Sample drawn from selected institutions in the Philippines may not be nationally representative. [unacknowledged]
- Reliance on self‑reported financial behaviors introduces recall and social desirability biases.
- The study does not measure income levels or actual disposable income, which could confound saving and investment behaviors.
- No longitudinal tracking to see if awareness changes over time or if behaviors shift with policy interventions. [unacknowledged]

---

## Source: `1.C/L--Espiritu_2026_summarized.md`

**Title:** The Relationship Between the Online Banking Usage and Financial Decision-Making Processes among Financial Management Students in Rural Areas

### TL;DR

Among rural Filipino financial management students, higher online banking transaction diversity and trust/security perceptions correlate strongly with better budgeting, saving, and spending behaviors, though overall usage frequency remains low.

### Findings

1. Overall online banking frequency mean = 2.04 (“Rarely”); transaction diversity mean = 3.05 (“Agree”); trust/security mean = 3.02 (“Agree”).
2. Financial decision-making means: budgeting 3.01, saving 3.03, spending 2.98 (all “Agree”).
3. Frequency of use showed significant moderate negative correlations with all three decision-making dimensions (rs = -.276 to -.282, p = .000).
4. Transaction diversity showed strong positive correlations (rs = .657 to .702, p = .000).
5. **Trust and security showed very strong positive correlations** (rs = .753 to .823, p = .000), with saving behavior having the highest (rs = .823).

- Students expressed confidence in platform security but acknowledged that hacking/fraud concerns influence engagement.

### Relevance to Odin

**Topics:**

1.C — Financial Behavior of Filipino Young Professionals

5.A — Financial Behavioral Profiles in Personal Finance

10.B — User Trust in Personal Finance Systems

11.A — Engagement Dynamics in Personal Finance Applications

**Contribution to Odin:**

This paper’s very strong positive correlation between trust/security perceptions and financial decision-making (rs up to .823) directly justifies Odin’s emphasis on privacy-by-design and transparent security features as core engagement drivers. The finding that transaction diversity (not just frequency) predicts better budgeting and saving behaviors informs Odin’s design to encourage varied transactional use (transfers, bill payments, purchases) rather than passive balance checking. Although the study focuses on rural students, its results on convenience-induced spending (mean 3.02 agreement that convenience encourages spending) provide evidence for Odin’s anomaly detection module to distinguish between habitual vs. impulsive spending. The moderate negative correlation between frequency of use and decision-making (rs = -.276 to -.282) is counterintuitive but suggests that infrequent users have weaker financial habits, supporting Odin’s goal of sustaining regular engagement to build financial capability.

**Directly justifies:**

- “Perceived trust and security in online banking correlates very strongly with saving behavior (rs = .823, p = .000) and spending behavior (rs = .814, p = .000) among rural Filipino students.”
- “Online banking transaction diversity (transfers, bill payments, purchases) has strong positive correlations (rs = .657 to .702) with budgeting, saving, and spending engagement.”
- “Frequency of online banking use is low (mean 2.04/4) among rural financial management students, and lower frequency is associated with weaker financial decision-making (rs = -.276 to -.282).”
- “Students agree that online banking convenience can encourage more frequent spending (mean 3.02), but reviewing transactions helps avoid impulse purchases (mean 2.90).”

**Limits of relevance:**

- Sample limited to rural financial management students; results may not generalize to urban young professionals or non-business students.
- Correlational design cannot infer causality; direction of relationships (trust → behavior or behavior → trust) is unknown.
- Trust and security measured as perceptions, not objective security metrics; may not reflect actual platform vulnerability.
- No longitudinal data; relationship dynamics over time (e.g., cold-start vs. experienced users) are not examined.

### Limitations

- Sample drawn from a single rural institution, limiting generalizability to other geographic or demographic contexts.
- Self-reported survey data may introduce recall and social desirability bias.
- Study does not control for prior financial literacy or digital literacy levels, which could confound observed correlations. [unacknowledged]
- No qualitative component to explain why frequency of use is low despite positive perceptions of trust.
- The negative correlation between frequency and decision-making is not experimentally explained; reverse causality possible.

---

## Source: `1.C/L--Jumawan-Powao_et-al_2024_summarized.md`

**Title:** Family Income in Relation to Budgeting of Accounting Students in A University

### TL;DR

Lower family income and allowance correlate with better budgeting practices among Filipino accounting students, who prioritize savings over flexible expenses.

### Findings

1. Overall budgeting literacy mean = 2.92/4.00 (“Often” — students budget 51–75% of the time).
2. **No significant difference in budgeting by sex** (Mann‑Whitney p = 0.709).
3. Significant inverse relationship between allowance and budgeting: lower allowance → more budgeting (Spearman Rho p = 0.001).
4. Significant inverse relationship between family income and budgeting (Spearman Rho p = 0.001).
5. Family income positively correlates with weekly allowance (Pearson p = 0.001).

- Students prioritize savings (mean 2.93) over flexible expenses (mean 2.63), deviating from the typical 50-30-20 rule.

### Relevance to Odin

**Topics:**

1.C — Financial Behavior of Filipino Young Professionals

7.A — Budgeting Strategies as Domain Knowledge

**Contribution to Odin:**

This paper directly informs Odin’s understanding of how income level affects budgeting discipline among Filipinos — a key input for behavioral profiling and budget recommendation. The finding that lower income drives stronger budgeting behavior suggests Odin’s algorithm should not assume higher income leads to better financial management; instead, lower‑income users may need less aggressive budgeting nudges. The documented deviation from the 50-30-20 rule (students prioritize savings over wants) provides empirical grounding for Odin’s default allocation logic, especially for younger Filipino users. The absence of sex‑based differences simplifies Odin’s user model, indicating that gender may not require separate handling in core budgeting modules.

**Directly justifies:**

- “Filipino accounting students with lower family income exhibit significantly better budgeting skills than those with higher income (Spearman Rho p = 0.001).”
- “Allowance amount is inversely related to budgeting behavior: students with lower allowances budget more actively (p = 0.001).”
- “No significant difference in budgeting practices exists between male and female Filipino students (p = 0.709), suggesting gender is not a moderating factor.”
- “Filipino students prioritize savings (mean 2.93) over flexible expenses (mean 2.63), deviating from the standard 50-30-20 rule.”
- “Family income positively correlates with weekly allowance amount (Pearson p = 0.001), meaning allowance largely reflects household financial capacity.”

**Limits of relevance:**

- Study population is university accounting students, not young professionals — financial behavior may differ after entering the workforce.
- Sample drawn from a single university in Dapitan City (Mindanao) — may not represent Metro Manila young professionals.
- No AI/ML methods or system design evaluation — only correlational statistics.
- Cross‑sectional design; cannot infer causality between income and budgeting.
- Accounting students likely have higher financial literacy than general population, limiting generalizability.

### Limitations

- Sample limited to accounting students in one university — results may not generalize to non‑accounting students or other regions. [unacknowledged]
- Cross‑sectional design cannot establish causality between family income and budgeting practices.
- Self‑reported Likert scale data subject to social desirability bias (students may overreport good budgeting).
- No measurement of actual spending vs. budget adherence — only perceived budgeting frequency.
- The paper’s reported statistical direction (positive Spearman Rho vs. stated inverse relationship) is internally inconsistent, weakening the reliability of the finding.

---

## Source: `1.C/L--Polinar_et-al_2023_summarized.md`

**Title:** Knowledge and Practice of Personal Finance of Non-Teaching Staff in a Private University in Cebu City

### TL;DR

Non-teaching staff have moderate personal finance knowledge and practice, but emergency fund and investment behaviors are weak, and knowledge does not correlate with practice for emergency funds or debt management.

### Findings

1. Grand mean knowledge = 3.10 (moderately knowledgeable); budgeting (3.29) and saving/spending (3.32) were “highly knowledgeable.”
2. **Grand mean practice = 2.71 (moderately practiced)**; emergency fund (2.42) and investment (2.20) were “less practiced.”
3. Significant positive correlations (p < 0.05): budgeting (r=0.939), saving/spending (r=0.839), insurance (r=0.969), investment (r=0.973).
4. No significant correlation for emergency fund (p=0.052) or debt management (p=0.053) – knowledge does not predict practice.
5. Investment knowledge (2.56) is higher than practice (2.20), indicating a notable gap.

### Relevance to Odin

**Topics:**

1.C — Financial Behavior of Filipino Young Professionals

5.A — Financial Behavioral Profiles in Personal Finance

7.A — Budgeting Strategies as Domain Knowledge

**Contribution to Odin:**

This paper provides empirical baseline data on the knowledge-practice gap among Filipino non-teaching staff, directly informing Odin’s user profiling and behavioral classification modules. The finding that emergency fund and investment practices are weakest (means 2.42 and 2.20) despite moderate knowledge justifies Odin’s design to include explicit, structured nudges for these behaviors rather than relying on literacy alone. The significant correlation between budgeting knowledge and practice (r=0.939) supports Odin’s educational component as a lever for behavior change, while the non-significant correlation for debt management (p=0.053) warns that knowledge interventions may be insufficient – Odin must incorporate action-oriented tools.

**Directly justifies:**

- “Filipino non-teaching staff have moderate personal finance knowledge (grand mean 3.10/4) but lower practice (2.71/4), with emergency fund and investment practice falling below the moderate threshold.”
- “Knowledge of budgeting correlates strongly with budgeting practice (r=0.939, p=0.002) – literacy interventions can improve practice for some domains.”
- “No significant correlation between knowledge and practice for emergency funds (p=0.052) and debt management (p=0.053), indicating that knowledge alone does not drive these behaviors.”
- “Investment knowledge is moderate (2.56) but practice is low (2.20) – a gap that requires structured goal-setting or automated allocation in a PFMS.”

**Limits of relevance:**

- Respondents are non-teaching staff from a single private university, not specifically the 20–40 young professional demographic – but likely overlapping in income and obligations.
- Self-reported Likert scales, not objective transaction data – Odin would measure actual behaviors, not perceptions.
- No algorithm or system design evaluated – descriptive only, cannot justify specific ML choices.
- Geography is Cebu City, Philippines – culturally similar to Metro Manila but not identical.

### Limitations

- Small sample size (n=50) from one university – limits generalizability to other institutions or regions. [unacknowledged]
- Self-reported knowledge and practice may suffer from social desirability bias – respondents may overstate good behaviors.
- No longitudinal data – causal direction between knowledge and practice cannot be established.
- Survey was adapted from a study on teachers – may not be fully validated for non-teaching staff roles.
- Does not measure actual financial outcomes (e.g., savings amounts, debt levels) – only perceived practice.

---

## Source: `1.C/L--Sarmiento_et-al_2025_summarized.md`

**Title:** Financial Edutainment: The Effect of Social Media Usage on the Financial Literacy of Students in Bulacan

### TL;DR

Heavy social media use among Filipino students positively affects financial literacy, explaining 69% of its variance, with TikTok and Facebook as primary sources.

### Findings

1. Social media usage has a **statistically significant positive effect** on overall financial literacy (β = 0.882, p < 0.001, R² = 0.689) — explaining 68.9% of variance.
2. Budgeting is the most strongly affected component (β = 0.751, R² = 0.667), followed by debt management (β = 0.719, R² = 0.629).
3. Most students (36.33%) spend 5–6 hours daily on social media; 84.35% are aged 19–21.

- TikTok ranked first for financial content (mean = 3.748), then Facebook (3.397), YouTube (2.978), Instagram (2.890).
- Students passively view financial influencer content “several times a month” (27.7%) but actively search only “about once a month” (31.8%) or “never” (17.8%).
- Students agree social media is useful (grand mean = 3.144) and easy to use (3.000), but also acknowledge privacy/security risks (3.116).

### Relevance to Odin

**Topics:**

1.C — Financial Behavior of Filipino Young Professionals

7.A — Budgeting Strategies as Domain Knowledge

10.B — User Trust in Personal Finance Systems

11.A — Engagement Dynamics in Personal Finance Applications

**Contribution to Odin:**

This paper establishes that Filipino students — a demographic adjacent to Odin’s target young professionals — have moderate financial literacy (mean 3.12/4.00) and that passive social media consumption is the dominant mode of financial learning. The finding that 68.9% of literacy variance is explained by social media use directly justifies Odin’s need to incorporate educational components that go beyond passive exposure, because users currently lack active knowledge-seeking behavior. The documented privacy and security concerns among students (mean 3.116 for risks) provide empirical grounding for Odin’s privacy-by-design emphasis, as user trust is shown to be a salient factor even in voluntary financial learning contexts.

**Directly justifies:**

- “Social media usage explains 68.9% of the variance in Filipino students’ financial literacy (β = 0.882, p < 0.001), indicating that digital platforms are the primary channel for informal financial education.”
- “Students are passive consumers of financial content (27.7% view several times a month) but rarely search actively (17.8% never search), suggesting financial apps must design for passive-to-active conversion through nudges or interactive features.”
- “Privacy and security concerns when discussing finances on social media are salient (grand mean 3.116), supporting the inclusion of explicit trust signaling in personal finance systems.”
- “Budgeting is the financial literacy component most strongly influenced by social media (β = 0.751, R² = 0.667), confirming that budget-related content is particularly effective for informal learning.”

**Limits of relevance:**

- Study population is students (mean age ~20), not young professionals aged 20–40; income structures and financial obligations differ.
- The dependent variable is self-perceived financial literacy via Likert scale, not objective knowledge tests or actual financial behavior.
- Context is social media as an educational tool, not a PFMS; causal direction (social media → literacy) may not transfer directly to system-driven learning.
- No distinction between fixed and variable income users; Odin’s forecasting and recommendation modules depend on income typology.

### Limitations

- Purposive sampling limits generalizability to all students in Bulacan; selection bias possible.
- 4-point Likert scale eliminates neutral responses, potentially forcing artificial agreement/disagreement.
- Self-reported financial literacy may overestimate actual knowledge (social desirability bias).
- Causal design with regression cannot fully rule out reverse causality (literate users may seek more financial content). [unacknowledged]
- No validation of financial influencer content quality; assumes positive effect without measuring misinformation exposure.

---

## Source: `2.A/L--Mansueto_et-al_2025_summarized.md`

**Title:** Unraveling the Retirement Spending Habits in Siquijor, Philippines: Promoting Support Policies for Retirees

### TL;DR

Retirees in Siquijor prioritize utilities (3.94) and groceries (3.80) while housing costs stay low due to extended family living, and emergency savings remain inadequate (3.25).

### Findings

1. Utilities (3.94) and groceries (3.80) are the highest basic living expenses; housing ranks lowest (3.02) due to extended family cost‑sharing.
2. Prescription medications (3.60) dominate healthcare spending; preventive care (3.36) and insurance premiums (2.70) are lower.
3. Financial support to adult children or grandchildren averages 3.46 (“often”), but emergency funds (3.25) are only “seldom” maintained.
4. Charitable giving focuses on local communities (2.68) rather than institutional donations (2.39).
5. Recreation and leisure (composite 2.45) and volunteerism (2.80) are rarely funded.

- **Emergency savings (3.25) are inadequate, leaving retirees financially vulnerable.**
- Transportation expenses are modest, with a shift from private vehicles to public transit.

### Relevance to Odin

**Topics:**

2.A — Culturally Specific Financial Practices

3.A — Expense Categorization Frameworks

3.B — Expense Category Design Considerations

**Contribution to Odin:**

This paper provides a validated expense category structure (utilities, groceries, housing, healthcare, transportation, recreation, charitable giving, home maintenance, debt reduction, gifts, insurance, education, gardening, legacy, emergency, volunteerism) that aligns with Philippine household spending realities. The finding that retirees frequently provide financial support to grandchildren (3.46) directly informs Odin’s need for a “family obligations” expense category, a culturally specific item absent from Western budgeting frameworks. Although the sample is retirees, the demonstrated prioritization of utilities and groceries over discretionary spending can inform default budget allocations for young professionals with similar fixed‑income constraints.

**Directly justifies:**

- “Retirees in Siquijor rate financial support to adult children or grandchildren as ‘often’ (3.46), confirming that inter‑family transfers are a recurring expense in Philippine households.”
- “Housing costs rank lowest (3.02) among basic expenses because extended family living arrangements distribute shelter costs across multiple earners.”
- “Emergency savings are rated only 3.25 (‘seldom’), indicating that even with moderate financial awareness, retirees lack a dedicated safety net category.”
- “A 14‑category expense taxonomy (utilities, groceries, healthcare, transportation, recreation, charity, home maintenance, debt, gifts, insurance, education, gardening, legacy, emergency) was field‑tested and can be adapted for personal finance systems.”

**Limits of relevance:**

- Sample is retirees (mean age not reported), not young professionals aged 20–40; spending priorities may shift with age.
- Study location is rural Siquijor; Metro Manila cost structures and income levels differ substantially.
- No algorithm or predictive model is discussed; relevance is limited to category design and cultural behavior description.
- Data are self‑reported Likert scales, not actual transaction logs, so frequency estimates are subjective.

### Limitations

- Purposive sampling may limit generalizability even within Siquijor; no random selection.
- Self‑reported spending frequency is subject to recall and social desirability bias. [unacknowledged]
- No income or wealth data collected, so spending patterns cannot be linked to pension levels or asset holdings.
- Cross‑sectional design cannot track how spending changes over time in retirement.
- Small sample size (n=179) and single province restrict statistical power and external validity.

---

## Source: `2.A/L--Rosario_2025_summarized.md`

**Title:** Personal Financial Management Practices of Average earning households within Indigenous Communities of Mountain Province: Exploring Their Strategies and Challenges

### TL;DR

Indigenous Bontoc households survive income insufficiency by blending strict budgeting with cultural reciprocity systems (og-ogfo, bayanihan, paluwagan), prioritizing community obligations over individual wealth.

### Findings

- Households consistently practice **strict budgeting and expense tracking**, but allocations are heavily shaped by cultural obligations (rituals, weddings, wakes) rather than purely personal goals.
- **All 12 participants reported income insufficiency** against rising costs of food, LPG, electricity, and education — forcing continuous cash‑flow juggling.
- Savings are thin and irregular (coin jars, livestock, stored rice), often depleted by emergencies; formal emergency funds are rare.
- Cultural practices dominate coping: og-ogfo (mutual labor/ aid), bayanihan, paluwagan (rotating savings), and in‑kind contributions (labor, food, livestock) function as informal insurance.
- **Borrowing is secondary** — families first seek kinship support, then cooperatives, and only last resort to formal loans or microfinance.
- Ritualized spending (mangmang, pasup-ok, butchering rites) is treated as non‑negotiable, preserving social identity even when it strains budgets.
- Financial stress manifests as psychological strain, children’s education disruptions, and limited healthcare access — but community solidarity prevents destitution.

### Relevance to Odin

**Topics:**

2.A — Culturally Specific Financial Practices

2.B — Seasonal and Cyclical Spending Patterns

4.B — Limitations and Gaps in Existing Systems

5.A — Financial Behavioral Profiles in Personal Finance

7.A — Budgeting Strategies as Domain Knowledge

8.A — Anomaly Detection in Personal Finance Systems

**Contribution to Odin:**

This paper provides empirical evidence that Filipino households in resource‑limited settings prioritize community obligations (og‑ogfo, rituals) over individual financial goals — a behavioral pattern that must inform Odin’s user profiling and budget recommendation logic. The finding that households use mental accounting and irregular savings (coin jars, livestock) rather than structured emergency funds directly challenges Western financial literacy assumptions and supports Odin’s need for culturally grounded expense categories. Additionally, the paper identifies that unexpected health and schooling costs are the most frequent financial anomalies, guiding Odin’s anomaly detection module to prioritize these categories for alerting.

**Directly justifies:**

- “Indigenous households in Bontoc treat cultural obligations (weddings, wakes, rituals) as non‑negotiable expenses, often delaying utility bills or personal savings to meet them.”
- “Households consistently face income insufficiency, with rising costs of food, LPG, electricity, and education cited by all 12 participants as the primary financial stressor.”
- “Informal risk‑sharing through og‑ogfo and kinship networks is the first‑line coping mechanism, with formal credit accessed only after community resources are exhausted.”
- “Savings take culturally embedded forms (paluwagan, livestock, stored rice) rather than conventional bank accounts, demonstrating that financial resilience is asset‑based and relational, not cash‑centric.”
- “Unexpected health expenses and school enrolment periods are recurrent budget disruptions, causing families to draw down savings or seek kinship aid — a pattern directly informing anomaly detection category weights.”

**Limits of relevance:**

- Study population is rural Indigenous households in Mountain Province, not urban young professionals in Metro Manila — income volatility and cultural obligations may differ significantly.
- No quantitative comparison of coping effectiveness or savings rates; findings are qualitative and not statistically generalizable.
- The study does not evaluate digital finance or mobile app usage, so inferences about user behavior with a PFMS are indirect.
- Reliance on informal reciprocity assumes stable community networks; this may weaken in highly urbanized or transient populations.

### Limitations

- Sample size of 12 participants from a single municipality limits transferability to other Indigenous or non‑Indigenous groups.
- Qualitative design cannot quantify the effectiveness of coping mechanisms or the magnitude of financial stress reduction.
- The paper does not compare Bontoc practices with those of non‑Indigenous low‑income households, leaving uncertainty about which findings are unique to indigeneity. [unacknowledged]
- No longitudinal data — captures financial practices at a point in time, but seasonal and ritual cycles may alter patterns across the year.
- Potential social desirability bias: participants may overstate adherence to cultural norms (og‑ogfo, bayanihan) when interviewed by a local researcher.
