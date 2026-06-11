# Comprehensive Report for Subtopic: `13.A`

**Total relevant papers:** 68

This report includes problem/motivation, approach, key findings, support for Odin, and limitations/contradictions.

---


## Psychology and Development: Applications from Cognitive and Social Psychology
**Filename:** `I--Breza-&-Kaur_summarized.md`  
**Authors:** Breza, E.; Kaur, S. (2026)  
**ID:** `a1b2c3d4-e5f6-4a7b-8c9d-0e1f2a3b4c5d`  
**Odin Topics:** 5.A, 5.C, 6.A, 6.B, 7.A, 7.B, 8.A, 11.A, 13.A, 13.B  

**TLDR:** Reviews how psychological constraints like self-control and limited cognition affect financial behaviors, and argues that missing markets for behavioral aids amplify poverty, informing personal finance system design.

**Problem & Motivation:** Development economics has focused on external constraints like missing markets, but internal psychological constraints also impede escaping poverty. These biases are amplified in developing countries due to proximity to subsistence, high volatility, weak institutions, and reliance on social ties. The paper reviews evidence across self-control, cognition, mental health, self-beliefs, and social norms to outline a research agenda for behavioral development economics.

**Approach (summary):**
- Provides a conceptual framework using missing markets to explain why behavioral aids are undersupplied.
- Identifies five key features of poverty that amplify psychological constraints: subsistence proximity, volatility, market failures, weak institutions, social ties.
- Reviews field experiments on self-control, including hard commitment (e.g., savings accounts) and soft commitment (e.g., lockboxes, reminders).

**Key Findings (selected):**
- num: 81% increase in total savings from a commitment savings account in the Philippines (Ashraf et al., 2006).
- num: Adding a social monitor increased savings by 36% in rural India (Breza and Chandrasekhar, 2019).
- num: 97.7% of farmers intend to use fertilizer but only 36.4% actually do (Duflo et al., 2011).
- num: 86% of individuals overpredict their savings, with average forecast error of 80% (Augenblick et al., 2023).

**Supports Odin (direct justifications):**
- People systematically underestimate irregular future expenses, leading to overconsumption and savings failures.
- Small transaction costs or physical actions (e.g., unlocking a lockbox) can effectively reduce temptation spending.
- Social observability of savings goals increases actual savings by 36% via reputation concerns.

**Limitations / Contradictions for Odin:**
- The literature on psychology of poverty has mixed replication, especially for priming manipulations.
- Most studies are short-term; long-run welfare effects of commitment devices remain unclear. [unacknowledged]
- The review does not provide precise meta-analytic estimates, limiting quantification of effect sizes.

**Key takeaways:**
- Commitment savings accounts increased savings by 81% in a Philippine field experiment.
- Soft commitment like lockboxes can be as effective as hard financial penalties.
- Financial concerns reduce cognitive performance and worker productivity by 7%.

---


## Beyond the Beach: Micro-Entrepreneurship Survival in Philippine Tourism Enclaves
**Filename:** `L--Lopez_summarized.md`  
**Authors:** Lopez, A. (2026)  
**ID:** `f5c9e6a2-3b4d-4a7e-9c8f-1d2e3f4a5b6c`  
**Odin Topics:** 2.A, 2.B, 13.A, 13.B  

**TLDR:** Micro-entrepreneurs in Philippine tourism enclaves deploy culturally embedded survival strategies including operational contraction, social capital activation, and diversification, but face a resilience trap excluding the most vulnerable from transformative adaptation.

**Problem & Motivation:** The survival strategies of micro-entrepreneurs in Philippine tourism enclaves during economic disruptions remain underexplored despite their critical role in local tourism economies. Recurring disruptions from pandemics, natural disasters, and policy interventions progressively deplete their adaptive capacity. A systematic analysis of survival strategies across disruption types and structural conditions is missing from Philippine scholarship.

**Approach (summary):**
- Qualitative secondary data analysis (QSDA) of peer-reviewed literature, government reports, and institutional studies from 2013 to 2024.
- Interpretivist paradigm with thematic analysis following Braun and Clarke's six-phase framework.
- Cross-case synthesis organized by disruption type, geographic context, and enterprise sector.

**Key Findings (selected):**
- num: International arrivals fell 82% in 2020, with 5.7 million tourism jobs affected.
- num: Only 38% of tourism micro-enterprises in enclave destinations held valid business permits.
- Social capital mechanisms (utang na loob, bayanihan, paluwagan) are the primary survival asset for vulnerable operators.
- A four-quadrant typology reveals a resilience trap: short-term strategies accessible, long-term transformative strategies inaccessible to most vulnerable.

**Supports Odin (direct justifications):**
- Social capital activation through paluwagan is the primary survival mechanism for vulnerable micro-entrepreneurs.
- Only 38% of tourism micro-entrepreneurs held valid business permits during COVID-19.
- Compound disruptions progressively deplete adaptive capacity, requiring multi-cycle resilience planning.

**Limitations / Contradictions for Odin:**
- Secondary data quality varies across government and institutional sources. [unacknowledged]
- No primary data on gender dynamics despite its policy importance. [unacknowledged]
- Rapidly evolving post-pandemic policy landscape may supersede some findings.

**Key takeaways:**
- Only 38% of tourism micro-entrepreneurs held valid permits during COVID-19.
- Utang na loob, bayanihan, and paluwagan are primary survival mechanisms.
- Compound disruptions progressively deplete adaptive capacity over successive shocks.

---


## AI-BASED PERSONAL FINANCE MANAGER (AI)
**Filename:** `IA--Sireesha-et_al_summarized.md`  
**Authors:** Sireesha, B.; Kiran Kumar, K.; Lavanya, O.; Keshan, S.; Ramsai, N.; Latheesh Kumar, K. (2026)  
**ID:** `a8b9c0d1-e2f3-4a5b-8c9d-0e1f2a3b4c5d`  
**Odin Topics:** 3.A, 3.B, 5.A, 5.C, 6.A, 6.B, 7.A, 7.B, 7.C, 8.A, 8.B, 12.A, 12.B, 13.A  

**TLDR:** An AI-based personal finance manager using machine learning, deep learning, and reinforcement learning automates expense categorization, spending forecasting, anomaly detection, and personalized budget recommendations.

**Problem & Motivation:** Users struggle to monitor spending, manage budgets, and make informed decisions due to lack of time, financial literacy, or analytical tools. Traditional finance management tools rely on static rules, offering limited personalization and predictive capabilities. An AI-powered solution is needed to automate data analysis, provide personalized insights, and adapt to dynamic user behavior.

**Approach (summary):**
- Data is collected from banking statements, e-commerce receipts, and user inputs then preprocessed via cleaning, normalization, tokenization, and category mapping.
- Random Forest, Gradient Boosting, SVM, and neural networks classify expenses into categories like food, transport, rent, and utilities.
- An LSTM model forecasts monthly expenditures and revenue streams, achieving a Mean Absolute Error of 4.7%.

**Key Findings (selected):**
- {'num': 'Random Forest expense classifier achieved 93-96% accuracy, outperforming rule-based systems (75-80%).'}
- {'num': 'LSTM forecasting produced a Mean Absolute Error of 4.7% for monthly expenditure prediction.'}
- {'num': 'Isolation Forest anomaly detection achieved 92% precision.'}
- {'num': '84% of users reported better spending awareness and 78% claimed increased savings control after one month.'}

**Supports Odin (direct justifications):**
- Random Forest achieves 93-96% accuracy for expense categorization, outperforming rule-based systems.
- LSTM forecasting reduces mean absolute error to 4.7% for monthly spending prediction.
- Isolation Forest detects anomalous transactions with 92% precision.

**Limitations / Contradictions for Odin:**
- Usability study limited to 50 participants, may not generalize. [unacknowledged]
- Long-term retention and engagement not evaluated. [unacknowledged]
- Data privacy and security not experimentally validated. [unacknowledged]

**Key takeaways:**
- Random Forest categorizes expenses with 93-96% accuracy.
- LSTM forecasts monthly spending with 4.7% MAE.
- 84% of users report better spending awareness after using the system.

---


## Consumer Expectations Survey Report 1st Quarter 2026
**Filename:** `L--Bangko_Sentral_ng_Pilipinas-2026_summarized.md`  
**Authors:** Bangko Sentral ng Pilipinas (2026)  
**ID:** `b3e5c6d7-8a9f-4b2c-9d1e-2f3a4b5c6d7e`  
**Odin Topics:** 1.C, 2.B, 6.B, 13.A, 13.B  

**TLDR:** Consumer sentiment improved in Q1 2026 with less pessimistic outlook, but year-ahead confidence decreased due to concerns over corruption, inflation, and government policies.

**Problem & Motivation:** Understanding consumer expectations is crucial for economic forecasting and policy formulation. The BSP conducts quarterly surveys to capture sentiment on income, spending, savings, and debt. Prior data showed pessimistic trends, requiring timely assessment of shifts in confidence.

**Approach (summary):**
- Data from 5,358 Philippine households (NCR and AONCR) surveyed 22 January to 5 February 2026.
- Sample drawn from PSA 2023 Geo-Enabled Master Sample using stratified multi-stage probability sampling.
- Confidence index computed as percentage of optimistic minus pessimistic responses.

**Key Findings (selected):**
- num: Overall confidence index improved from -22.2% to -15.8% in Q1 2026.
- num: Year-ahead confidence index decreased from 11.8% to 9.6%.
- num: Saving intention index increased from 4.6% to 12.4%.
- num: Borrowing intention index for next quarter improved from -71.7% to -69.5%.

**Supports Odin (direct justifications):**
- Consumer confidence improved by 6.4 percentage points from Q4 2025 to Q1 2026.
- Saving intention index rose from 4.6% to 12.4% in one quarter.
- Only 26.1% of saving households set aside at least 10% of monthly income.

**Limitations / Contradictions for Odin:**
- Survey conducted before the US-Israel-Iran conflict onset in February 2026 (acknowledged).
- Sample excludes individuals without stable address [unacknowledged].
- Only 5,358 households, may not fully represent young professionals [unacknowledged].

**Key takeaways:**
- Consumer sentiment less pessimistic in Q1 2026 but year-ahead outlook weakened.
- Saving intention index jumped to 12.4%, highest since 2021.
- Majority of households (58.6%) target housing under ₱450,000.

---


## Determinants of Saving Behavior Among Filipino University Students: A Psychological and Social Perspective
**Filename:** `L--Claros-et_al_summarized.md`  
**Authors:** Claros, J. R.; Gaza, J. A.; Villaverde, Z. A.; Angeles, I. T. (2026)  
**ID:** `10.5281/ZENODO.18884267`  
**Odin Topics:** 1.C, 5.A, 13.A  

**TLDR:** Financial literacy and parental influence positively predict saving behavior among Filipino university students, while peer influence is insignificant and self-control shows a negative effect.

**Problem & Motivation:** University students face increasing financial pressure and low savings rates despite formal financial education. Few studies examine psychological and social determinants of saving behavior in the Philippine university context. There is a gap in understanding how financial literacy, parental influence, peer influence, and self-control contribute to intentional saving among Filipino young adults.

**Approach (summary):**
- Quantitative explanatory design using Partial Least Squares Structural Equation Modeling (PLS-SEM) with 377 university students aged 18-25 from private and public universities across the Philippines.
- Non-probability purposive sampling targeting enrolled students managing personal allowances or income sources.
- Structured questionnaire with validated six-point Likert scales measuring financial literacy, parental influence, peer influence, self-control, and saving behavior.

**Key Findings (selected):**
- Financial literacy has the strongest positive effect on saving behavior (β=0.684, p<.001).
- Parental influence shows a significant positive effect on saving behavior (β=0.284, p<.001).
- Peer influence does not significantly affect saving behavior (β=-0.041, p=0.423).
- Self-control exhibits a significant negative effect on saving behavior (β=-0.201, p<.001), contradicting conventional assumptions.

**Supports Odin (direct justifications):**
- Financial literacy is the strongest predictor of saving behavior among university students (β=0.684).
- Parental influence positively affects saving behavior (β=0.284), justifying family-centered financial features.
- Peer influence does not significantly affect saving behavior among Filipino university students.

**Limitations / Contradictions for Odin:**
- Lack of demographic data like age and gender in the survey instrument limits subgroup analysis.
- Sample includes emerging adults who rely on parental allowance, but demographic controls needed for generalizability.
- Self-control's negative effect may be suppressed by financial literacy, requiring further research. [unacknowledged]

**Key takeaways:**
- Financial literacy is the strongest predictor of student saving behavior.
- Parental influence shapes saving habits more than peer influence.
- Higher self-control unexpectedly reduces saving behavior in this sample.

---


## Reimagining social protection: financialised futures among ageing migrant domestic workers in Asia
**Filename:** `I--Amrith_summarized.md`  
**Authors:** Amrith, M. (2026)  
**ID:** `10.1080/1369183X.2025.2542769`  
**Odin Topics:** 2.A, 5.A, 7.A, 13.A, 13.B  

**TLDR:** Financial literacy courses for ageing Filipino migrant domestic workers in Singapore and Hong Kong promote self-responsibility and financialised futures as alternatives to limited state protection and uncertain kinship care.

**Problem & Motivation:** Migrant domestic workers face precarious futures after decades of remittances due to limited state-based social protection and ambivalence about reliance on kin. Financial education courses have emerged to address this gap, but their implications are understudied.

**Approach (summary):**
- Ethnographic fieldwork (2018-2022) with Filipino domestic workers aged 45-65 in Singapore and Hong Kong.
- Over 50 in-depth interviews plus observations in financial literacy courses, social spaces, and online.
- Focus on three organisations: a Singapore NGO, a Hong Kong NGO, and a Filipino-led cooperative.

**Key Findings (selected):**
- Migrant women undergo a transformation narrative from 'breadwinner' to 'financially-smart' self.
- num: Only 5% of overseas Filipinos in Singapore contributed to the state pension system.
- Financial education varies from basic budgeting to corporate insurance and real-estate seminars.
- Participation fosters new communities and purpose but also individualises responsibility for future security.

**Supports Odin (direct justifications):**
- Migrant domestic workers struggle to refuse family requests for money due to emotional pressure.
- Financial education courses promote self-responsibility as a solution to precarious futures.
- Only a small minority of overseas Filipinos contribute to formal pension systems.

**Limitations / Contradictions for Odin:**
- Focus on Filipino migrants limits cross-national comparison. [unacknowledged]
- Does not quantify the long-term effectiveness of financial education. [unacknowledged]
- Potential selection bias as participants are self-selected into courses.

**Key takeaways:**
- num: Only 5% of overseas Filipinos pay into state pension system.
- Financial literacy courses transform breadwinners into self-reliant investors.
- Financialisation coexists with activist and faith-based alternatives.

---


## Financial Literacy of Public Secondary School Teachers in San Francisco District, Camotes Island, Cebu, Philippines
**Filename:** `L--Montuerto-&-Ferrater-Gimena_summarized.md`  
**Authors:** Montuerto, J. E.; Ferrater-Gimena, J. A. O. (2026)  
**ID:** `10.5281/zenodo.18438866`  
**Odin Topics:** 1.C, 3.A, 7.A, 13.A, 13.B  

**TLDR:** Public secondary school teachers in San Francisco District, Camotes Island demonstrate moderate financial literacy in budgeting, spending, and credit management, but low literacy in savings and investing.

**Problem & Motivation:** Public school teachers in the Philippines face financial difficulties including budget deficits, debt cycles, and reliance on loans. Financial literacy is essential for personal financial management and effective teaching of financial education, yet limited research exists on rural public school teachers' financial literacy.

**Approach (summary):**
- Descriptive-correlational design with 150 teachers from three national high schools.
- {'Researcher-made survey with two parts': 'demographic profile and financial literacy items (budgeting, savings, investing, spending, credit/debt).'}
- Cronbach's alpha of 0.885 confirmed reliability.

**Key Findings (selected):**
- num: 42% of respondents were aged 24-32 years (mean 36.11), 78.67% female, 68% married, 74% had no other income sources.
- num: Budgeting aggregate mean 2.96 (moderate), savings 2.42 (low), investing 1.98 (low), spending 3.17 (moderate), credit/debt 3.05 (moderate).
- num: Age significantly related to budgeting (p=0.004), savings (p=0.001), investing (p=0.0001), and credit/debt (p=0.001).
- num: Educational attainment significantly related to savings (p=0.038) and credit/debt (p=0.001).

**Supports Odin (direct justifications):**
- Public school teachers allocate earnings primarily to essential household commodities (weighted mean 3.39).
- Teachers save only 20% of earnings for emergencies (weighted mean 2.79) and show low savings account use (2.44).
- Teachers lack correct investment knowledge (2.21) and avoid Bitcoin/online investments (1.70).

**Limitations / Contradictions for Odin:**
- Small sample from one rural district; may not represent urban teachers. [unacknowledged]
- Cross-sectional design; causality cannot be inferred. [unacknowledged]
- Self-reported survey data may overstate financial literacy due to social desirability bias. [unacknowledged]

**Key takeaways:**
- Teachers showed low financial literacy in savings (2.42) and investing (1.98).
- Age significantly correlates with budgeting, savings, investing, and debt management.
- Most teachers (74%) have no other income sources beyond salary.

---


## Effect of Subscription Culture on Consumer Spending Patterns
**Filename:** `I--Reena-&-Murugesan_summarized.md`  
**Authors:** Reena, R.; Murugesan, Sudeshna (2026)  
**ID:** `f47ac10b-58cc-4372-a567-0e02b2c3d479`  
**Odin Topics:** 2.B, 5.A, 7.A, 8.A, 10.B, 13.A  

**TLDR:** Subscription culture encourages recurring spending, often leading to unnoticed cumulative costs, unexpected auto-renewal charges, and budgeting challenges among young consumers.

**Problem & Motivation:** The rapid growth of subscription-based services has transformed consumer purchasing from one-time ownership to recurring access, yet limited understanding exists of how these models influence spending patterns and financial management. Despite the convenience and flexibility of subscriptions, consumers often underestimate cumulative costs and face unexpected charges from automatic renewals. This gap motivates research into subscription culture's effect on consumer spending behavior.

**Approach (summary):**
- Collected primary data from 100 respondents using a structured questionnaire distributed via Google Forms.
- Applied descriptive research design and convenience sampling technique.
- Used percentage analysis, one-way ANOVA, and correlation analysis to identify patterns and relationships.

**Key Findings (selected):**
- Young consumers aged 18-23 show higher tendency to subscribe to multiple services due to digital familiarity and convenience.
- Convenience and exclusive access are primary reasons for choosing subscription services.
- Many consumers sometimes forget their total monthly subscription spending.
- Unexpected charges due to automatic renewals are common among users.

**Supports Odin (direct justifications):**
- Subscription services lead to unnoticed cumulative monthly spending.
- Automatic renewals often cause unexpected charges for consumers.
- Young consumers aged 18-23 are more likely to hold multiple subscriptions.

**Limitations / Contradictions for Odin:**
- Small sample size of 100 respondents limits generalizability. [unacknowledged]
- Convenience sampling may introduce selection bias. [unacknowledged]
- Sample predominantly consists of students aged 18-23, not representative of all consumers. [unacknowledged]

**Key takeaways:**
- Subscription culture increases recurring spending and budgeting challenges.
- Auto-renewal systems often cause unexpected charges for consumers.
- Young consumers frequently underestimate cumulative subscription costs.

---


## NURSING CAREER TOWARDS FINANCIAL INDEPENDENCE
**Filename:** `L--Nduka-&-Benedicto_summarized.md`  
**Authors:** Nduka, P.; Benedicto, E.G. (2026)  
**ID:** `8c4a3b2d-1e5f-4a6b-9d7c-8e0f1a2b3c4d`  
**Odin Topics:** 1.C, 13.A, 13.B  

**TLDR:** Nurses in the Philippines experience a mismatch between income and expenses, with most unable to save, perceiving financial independence as essential for personal security, job satisfaction, and family obligations.

**Problem & Motivation:** Filipino nurses face financial insecurity due to low wages and rising living costs, yet limited research focuses specifically on their financial independence. This gap affects workforce retention and healthcare system stability.

**Approach (summary):**
- Qualitative phenomenological study conducted with 28 registered nurses from three government Level III specialty hospitals in Metro Manila.
- Data collected via semi-structured interviews lasting 40-60 minutes, audio-recorded and transcribed verbatim.
- Interview guide validated using Aiken’s V (0.8 to 1.0), ensuring content validity.

**Key Findings (selected):**
- num: 64.29% of nurse participants are female, 35.71% male.
- num: 53.57% aged 33-39 years, 28.57% aged 26-32 years.
- num: 50.0% hold government salary grades 2-6, only 17.85% reach grades 7-10.
- num: 53.57% have master’s degrees, 10.71% doctorates, but financial returns remain limited.

**Supports Odin (direct justifications):**
- Single nurses living alone can cover basic needs but cannot accumulate savings for long-term security.
- Financial independence reduces work-related stress and improves job satisfaction among professionals.
- Nurses with four or more dependents experience monthly deficits and psychological strain.

**Limitations / Contradictions for Odin:**
- Small sample size (n=28) limits generalizability.
- No longitudinal data; financial status reported cross-sectionally.
- Potential social desirability bias in self-reported financial perceptions. [unacknowledged]

**Key takeaways:**
- 64.29% of nurse participants are female.
- 53.57% support four or more dependents.
- Most nurses cannot save due to monthly deficits.

---


## Budgeting Practices and Challenges of Micro-Entrepreneurs in Maria Aurora Public Market: Toward a Strategic Management Plan
**Filename:** `L--Delos_Santos-et_al_summarized.md`  
**Authors:** Delos Santos, D.T.; Austria, M.G.P.; Candelario, C.C.; Garcia, L.E.B.; Gonaranao, B.S. (2026)  
**ID:** `10.4898/jener.v2i3.a32`  
**Odin Topics:** 3.A, 3.B, 7.A, 13.A, 13.B  

**TLDR:** Micro-entrepreneurs in Maria Aurora Public Market exhibit high financial discipline in income utilization, expense tracking, savings, and financial planning but face major challenges from debt burdens, inflation, and irregular income.

**Problem & Motivation:** Micro-entrepreneurs in rural Philippine public markets often lack structured budgeting systems, hindering their sustainability and growth despite being economic backbones. Existing research does not focus specifically on Maria Aurora's vendors, leaving a gap in localized understanding of their financial practices and barriers.

**Approach (summary):**
- Descriptive quantitative design with 68 micro-entrepreneurs sampled via simple random lottery from a population of 82 stall owners, food vendors, and retailers.
- Self-constructed Likert-scale survey covering four budgeting dimensions (income utilization, expense tracking, savings, financial planning) and two challenge dimensions (financial liability, income generation).
- Data analyzed using frequency counts, average weighted means (AWM), and verbal interpretation scales (Never to Always for practices; Not a Challenge to Major Challenge for obstacles).

**Key Findings (selected):**
- num: Overall income utilization AWM=3.63 (Always), expense tracking AWM=3.48 (Always), savings AWM=3.49 (Always), financial planning AWM=3.57 (Always).
- num: Financial liability AWM=3.27 (Major Challenge), income generation AWM=3.40 (Major Challenge).
- num: Highest-ranked practice: setting financial goals (AWM=3.77).
- num: Lowest-ranked practice: categorizing expenses into fixed vs variable costs (AWM=3.20).

**Supports Odin (direct justifications):**
- Micro-entrepreneurs struggle to categorize expenses into fixed and variable costs, justifying automated expense categorization in Odin.
- High debt repayment pressure reduces capital for business needs, supporting a debt management module with repayment planning.
- Low tendency to deposit savings in banks (AWM=3.22) indicates Odin should facilitate micro-savings accounts with low barriers.

**Limitations / Contradictions for Odin:**
- Single-site study (Maria Aurora Public Market) limits external validity.
- Reliance on self-reported Likert scales may introduce social desirability and recall bias. [unacknowledged]
- Mixed methods promised in introduction but only quantitative data collected; no qualitative triangulation. [unacknowledged]

**Key takeaways:**
- Income utilization discipline is high with AWM=3.63 (Always).
- Managing multiple debts is the top financial liability challenge (AWM=3.42).
- Only 3.22 AWM for depositing savings in banks shows low formal integration.

---


## The Relationship Between the Online Banking Usage and Financial Decision-Making Processes among Financial Management Students in Rural Areas
**Filename:** `L--Espiritu-2026_summarized.md`  
**Authors:** Espiritu, Mark Jay M. (2026)  
**ID:** `https://doi.org/10.65339/ijsair.V2.I1.31`  
**Odin Topics:** 1.A, 1.C, 7.A, 10.A, 10.B, 13.A  

**TLDR:** Online banking usage among rural Filipino financial management students shows low frequency but high transaction diversity and trust, which correlate positively with budgeting, saving, and spending practices.

**Problem & Motivation:** Rural financial management students face unique economic conditions, yet little is known about how their online banking usage relates to financial decision-making. Existing literature links digital literacy and trust to adoption but does not clarify these relationships in rural student populations. This gap matters for designing educational and institutional supports for responsible digital finance.

**Approach (summary):**
- A descriptive-correlational quantitative design was used with 242 purposively selected BSBA Financial Management students from a rural Philippine area.
- Data were collected via an online structured questionnaire measuring online banking utilization (frequency, transaction type, trust/security) and financial decision-making (budgeting, saving, spending).
- Pilot testing with 30 participants showed strong internal consistency (Cronbach's alpha .835 to .970) across all subscales.

**Key Findings (selected):**
- num: Overall frequency of online banking use was low (mean=2.04, 'Rarely'), while transaction diversity (mean=3.05) and trust/security (mean=3.02) were rated 'Agree'.
- num: Frequency of use showed moderate negative correlations with budgeting (rs=-.276), saving (rs=-.274), and spending (rs=-.282), all p=.000.
- num: Transaction diversity had strong positive correlations with budgeting (rs=.702), saving (rs=.677), and spending (rs=.657), p=.000.
- num: Trust and security had very strong positive correlations with budgeting (rs=.753), saving (rs=.823), and spending (rs=.814), p=.000.

**Supports Odin (direct justifications):**
- Trust and security perceptions have very strong positive correlations (rs=.753 to .823) with budgeting, saving, and spending behaviors among rural students.
- Using online banking for diverse transactions (e.g., transfers, bill pay, purchases) is strongly associated (rs=.657 to .702) with better financial decision-making.
- Low frequency of online banking use is moderately associated (rs=-.276 to -.282) with weaker budgeting, saving, and spending practices.

**Limitations / Contradictions for Odin:**
- Descriptive-correlational design limits causal inference.
- Single rural setting and specific student population limit generalizability.
- Self-reported data may contain response bias.

**Key takeaways:**
- Trust and security perceptions show the strongest correlation (rs=.823) with saving behavior.
- Low frequency of online banking use is linked to weaker financial practices.
- Using diverse online banking transactions strongly predicts better budgeting and saving.

---


## How reinforcement learning can drive personalized financial wellness
**Filename:** `IA--Pandey-&-Awasthi_summarized.md`  
**Authors:** Pandey, V.; Awasthi, V. (2025)  
**ID:** `10.30574/ijsra.2025.15.1.1244`  
**Odin Topics:** 4.B, 5.A, 5.B, 5.C, 7.A, 7.B, 7.C, 11.A, 12.A, 12.B, 13.A  

**TLDR:** Reinforcement learning with DQN, user persona clustering, and GPT-based conversation produces personalized financial recommendations that improve savings outcomes in a simulated environment.

**Problem & Motivation:** Financial wellness is a pervasive challenge; many individuals struggle with saving, investing, and budgeting effectively. Traditional budgeting tools and robo-advisors provide generic advice that fails to account for individual behavior and needs. This gap motivates an integrated framework combining RL, behavioral analytics, and NLP to deliver real-time personalized guidance.

**Approach (summary):**
- Synthetic dataset of 300 users with income and saving rate generated to simulate diverse financial behaviors.
- K-means clustering (k=3) creates interpretable personas: low-income low-saver, mid-income moderate-saver, high-income high-saver.
- Personal finance management formulated as Markov Decision Process with state (month, savings) and 6 discrete saving actions ($0 to $50).

**Key Findings (selected):**
- num: Learned policy achieved average final savings of $450 across simulations, compared to baseline 2 (always save $50) at $564 and baseline 1 negative.
- RL agent learns to save aggressively near year-end and after shocks to recover from debt.
- K-means clustering produces well-separated personas that can inform policy specialization.
- GPT-4 generates empathetic, personalized responses that incorporate persona context and RL recommendations.

**Supports Odin (direct justifications):**
- Reinforcement learning can learn personalized saving policies that outperform static baselines.
- User persona clustering via K-means enables initial policy customization for different financial behaviors.
- Conversational AI can translate quantitative RL recommendations into empathetic, context-aware advice.

**Limitations / Contradictions for Odin:**
- Synthetic data limits external validity.
- Action space limited to saving amounts, excluding debt and investment choices.
- No real-world deployment or user study. [unacknowledged]

**Key takeaways:**
- DQN agent achieved $450 average savings in simulation.
- K-means clusters users by income and saving rate into three personas.
- Conversational GPT explains RL recommendations naturally.

---


## Explainable and Context-Aware Financial Nudges via Event-Driven Microservices
**Filename:** `IA--Mandaleeka_summarized.md`  
**Authors:** Mandaleeka, A. P. (2025)  
**ID:** `10.63282/3050-922X.ICRCEDA25-143`  
**Odin Topics:** 7.A, 8.A, 10.A, 10.B, 11.A, 11.B, 13.A  

**TLDR:** An event-driven microservices framework uses SHAP-based explainability to deliver context-aware financial nudges, improving user trust and engagement.

**Problem & Motivation:** Generic financial alerts lack context and transparency, leading users to ignore or distrust them. Financial decisions directly affect well-being, making explainability essential for automated advice. Existing systems fail to integrate real-time context, interpretable AI, and modular architecture in a privacy-preserving way.

**Approach (summary):**
- Data consists of synthetic and anonymized financial datasets simulating diverse user behaviors.
- Kafka-based microservices include Data Ingestor, Context Processor, Nudge Decision Engine (rule-based or ML), XAI module with SHAP, and Notification Service.
- Context is enriched with transaction history, geolocation, behavioral signals, and temporal patterns like pay cycles.

**Key Findings (selected):**
- Contextual triggers such as time, location, and prior habits increase user engagement.
- Explainability boosts users' perceived relevance and trust in the system.
- SHAP provides local interpretability for individual nudge decisions with formal fairness guarantees.
- Modular event-driven architecture enables scalability, fault isolation, and auditability for financial applications.

**Supports Odin (direct justifications):**
- Explainable AI increases user trust and behavioral compliance in financial nudging systems.
- Contextual triggers such as time, location, and prior habits increase user engagement.
- SHAP provides local interpretability for individual nudge decisions with formal guarantees.

**Limitations / Contradictions for Odin:**
- Synthetic dataset may not generalize to real-world user behavior. [unacknowledged]
- No user study or empirical validation of trust or engagement metrics. [unacknowledged]
- SHAP computational cost and caching overhead acknowledged but not fully solved.

**Key takeaways:**
- Explainability is critical for user trust in automated finance.
- Context-aware triggers (time, location, habits) increase engagement.
- SHAP provides fair, locally interpretable explanations for nudges.

---


## Financial Literacy and Financial Health of Public Junior High School Teachers
**Filename:** `L--Garcia_summarized.md`  
**Authors:** Garcia, E. (2025)  
**ID:** `10.69569/jip.2025.324`  
**Odin Topics:** 1.C, 5.A, 7.A, 13.A, 13.B  

**TLDR:** Public junior high school teachers in Quezon City show high financial literacy but are financially coping, with gaps in emergency savings, debt management, and long-term planning.

**Problem & Motivation:** Public school teachers face financial insecurity due to low wages and rising costs, yet localized research on their financial literacy and health is scarce. This study addresses that gap by assessing these factors among teachers in District VI, Quezon City.

**Approach (summary):**
- A quantitative-descriptive design was used with a validated questionnaire adapted from the Financial Health Network and Surendar & Subramanya Sarma.
- Data were collected from 241 randomly selected public junior high school teachers across five schools in Quezon City.
- Financial literacy was measured across nine dimensions (knowledge, behavior, attitude, budgeting, liquidity, large purchases, insurance, investment, retirement).

**Key Findings (selected):**
- num: Overall financial literacy mean was 4.02 (High), with retirement planning scoring lowest (3.75) and financial knowledge highest (4.24).
- num: Overall financial health mean was 61.2, categorizing respondents as 'Financially Coping' (spending 63.17, saving 51.87, borrowing 72.40, planning 60.22).
- num: Only 39.00% of respondents had money remaining at month end (Financially Vulnerable), and emergency fund preparedness scored 3.72.
- Significant differences in financial literacy were found for sex, age, number of children, income, education, teaching position, years of experience, and specialization.

**Supports Odin (direct justifications):**
- Public junior high school teachers have a mean financial health score of 61.2, categorized as Financially Coping.
- Female teachers exhibit significantly higher overall financial literacy than male teachers (p=0.017).
- Teachers allocate 78.44% of monthly income to debt repayment, limiting surplus for savings.

**Limitations / Contradictions for Odin:**
- The study does not compare teachers to other professions, so findings may reflect public sector constraints rather than teacher‑specific traits.
- Self‑reported data may overstate financial literacy due to social desirability bias. [unacknowledged]
- The financial health scoring (0-100) lacks external validation against actual default or bankruptcy rates. [unacknowledged]

**Key takeaways:**
- Teachers have high literacy but are financially coping, not thriving.
- Only 39% have any money left at month end.
- Retirement planning literacy is the lowest at 3.75.

---


## How do young people perceive financial literacy, and what role do they believe it plays in their future success?
**Filename:** `I--Nasih-&-Adam_summarized.md`  
**Authors:** Nasih, M.; Adam, A. S. (2025)  
**ID:** `c8c9e9b8-4c3a-4b2a-9a1a-2b3c4d5e6f7a`  
**Odin Topics:** 1.C, 2.A, 5.A, 11.A, 13.A  

**TLDR:** Young adults universally recognize financial literacy as important for future success but exhibit an awareness-confidence paradox, overestimating their competence while acknowledging knowledge gaps.

**Problem & Motivation:** Despite extensive research on youth financial knowledge, limited systematic evidence exists on how young people perceive financial literacy and its role in future success, particularly in developing countries. Understanding these perceptions is critical because they shape engagement with financial education and subsequent financial behaviors.

**Approach (summary):**
- Systematic literature review following PRISMA 2020 guidelines across seven databases (JSTOR, ERIC, Scopus, Google Scholar, OECD iLibrary, World Bank, ProQuest).
- Included 47 peer-reviewed empirical studies from 25 countries published 2015-2025, with participants aged 18-30 (total n>250,000).
- {'Used thematic synthesis with three-stage approach': 'line-by-line coding, descriptive theme development, and analytical theme generation.'}

**Key Findings (selected):**
- num: 78% of university students rated financial knowledge as good/excellent but only 34% could answer basic literacy questions (Germany).
- num: Pandemic experiences increased financial literacy awareness scores by 28% (US longitudinal study).
- num: Young women 40% more likely to respond 'don't know' to financial questions despite equal knowledge (15-country study).
- Family financial socialization dominates formal education, with open family discussions correlating with 45% higher financial confidence.

**Supports Odin (direct justifications):**
- Financial literacy perceptions among young adults are characterized by an awareness-confidence paradox where knowledge gaps coexist with overconfidence.
- Family financial socialization has stronger influence on youth financial capability than formal education.
- Gender stereotypes widen financial confidence gaps, with young women 40% more likely to respond 'don't know' despite equal knowledge.

**Limitations / Contradictions for Odin:**
- English-language publication bias may exclude relevant research from non-English speaking countries. [unacknowledged]
- Heterogeneity in financial literacy measures across studies limits comparability. [acknowledged]
- Rapid digital financial innovation may outdate some findings. [unacknowledged]

**Key takeaways:**
- Young adults show an awareness-confidence paradox: high self-rated but low actual financial literacy.
- Family discussions about money increase financial confidence by 45% regardless of parents' knowledge.
- Only 15-20% of youth who plan to learn about finances actually take action within a year.

---


## Teachers’ Financial Literacy Management and their Performance in the Workplace
**Filename:** `L--Manatad-&-Labitad_summarized.md`  
**Authors:** Manatad, W. C. V.; Labitad, G. F. (2025)  
**ID:** `b3c4d5e6-f7a8-49b0-9c1d-2e3f4a5b6c7d`  
**Odin Topics:** 1.C, 5.A, 7.A, 13.A, 13.B  

**TLDR:** Public school teachers in Cagayan de Oro demonstrate literate financial literacy, highest in debt management, and very satisfactory workplace performance, with significant positive relationships between financial literacy and instructional planning, classroom management, and task management.

**Problem & Motivation:** Financial difficulties among public school teachers due to limited salaries and rising living costs may impair job focus and productivity. Prior studies show financial instability correlates with lower job satisfaction and increased stress. However, the direct link between teachers' financial literacy management and specific workplace performance dimensions remains underexplored.

**Approach (summary):**
- Data from 303 public elementary teachers in South District, Cagayan de Oro City using universal sampling.
- Researcher-developed survey measured financial literacy (budgeting, savings, debt, investment) and workplace performance (student outcomes, instructional planning, classroom management, delivery, task management).
- Descriptive statistics (mean, SD) and Pearson correlation analyzed relationships.

**Key Findings (selected):**
- num: Overall financial literacy mean 3.14 (SD 0.81) interpreted as Literate.
- num: Debt management had highest mean 3.22, budgeting the lowest 3.05.
- num: Workplace performance overall mean 3.33 (Very Satisfactory), with classroom management highest at 3.42.
- Significant positive relationship between financial literacy and instructional planning (p=0.0442), classroom management (p=0.0442), and task management (p=0.0091).

**Supports Odin (direct justifications):**
- Teachers with higher debt management scores show significantly better classroom management and task organization.
- Financially literate teachers exhibit very satisfactory workplace performance, especially in classroom management.
- Budgeting and financial planning is the lowest literacy area among teachers, requiring intervention.

**Limitations / Contradictions for Odin:**
- Sample limited to one district in Cagayan de Oro City (N=303).
- Self-reported survey data may have social desirability bias [unacknowledged].
- Cross-sectional design cannot establish causality [unacknowledged].

**Key takeaways:**
- Debt management is the strongest financial literacy area among teachers.
- Classroom management performance is rated very satisfactory.
- Financial literacy significantly improves task management in the workplace.

---


## Financial Literacy of Department of Education Teachers in the Philippines
**Filename:** `L--Vidal-Sarahina_summarized.md`  
**Authors:** Vidal-Sarahina, M. E. (2025)  
**ID:** `10.69569/jip.2025.483`  
**Odin Topics:** 1.C, 2.A, 5.A, 13.A, 13.B  

**TLDR:** Examines financial knowledge, attitudes, and behaviors of 30 Filipino public school teachers, finding a significant gap between knowledge and practice due to economic pressures, cultural obligations, and behavioral biases.

**Problem & Motivation:** Teachers face financial instability despite their critical role. Existing financial literacy programs focus on knowledge acquisition but fail to address socio-economic, cultural, and behavioral barriers. Limited research exists on the financial literacy of DepEd teachers in Guihulngan City.

**Approach (summary):**
- Mixed-methods study with 30 quantitative survey respondents and 10 qualitative interview participants from DepEd teachers in Guihulngan City, Philippines.
- Measured financial knowledge, attitude, and behavior using a Likert-scale questionnaire, analyzed with weighted means and Spearman correlation.
- Qualitative data analyzed using reflexive thematic analysis to identify barriers such as cultural obligations, economic constraints, and behavioral biases.

**Key Findings (selected):**
- num: Mean financial knowledge score 2.15 (moderate), attitude 3.02 (positive), behavior 2.80 (moderately acceptable).
- num: No significant correlation between knowledge and behavior (r=0.01, p=0.96).
- num: Very weak correlation between knowledge and attitude (r=0.09, p=0.62).
- Qualitative themes: Knowledge-Action Gap, Cultural and Familial Expectations, Economic Realities, Behavioral Biases.

**Supports Odin (direct justifications):**
- Financial knowledge does not significantly correlate with financial behavior among Filipino teachers (r=0.01, p=0.96).
- Cultural obligation of utang na loob drives financial decisions that prioritize family over personal savings.
- Behavioral biases such as impulsive spending and overconfidence lead to inconsistent financial actions.

**Limitations / Contradictions for Odin:**
- Sample size of 30 is small for quantitative correlation analysis [unacknowledged].
- Purposive sampling may introduce selection bias [unacknowledged].
- Findings may not generalize beyond Guihulngan City [unacknowledged].

**Key takeaways:**
- Financial knowledge does not predict financial behavior among Filipino teachers.
- Cultural obligation utang na loob overrides personal savings goals.
- Low salaries and loan dependence trap teachers in debt cycles.

---


## The Mediating Role of Financial Well-Being in the Relationship between Financial Behavior and Stress Among Irregular Income Workers
**Filename:** `I--Nurkhalida-&-Renanita_summarized.md`  
**Authors:** Nurkhalida, K.; Renanita, T. (2025)  
**ID:** `10.20885/psikologika.vol30.iss2.art5`  
**Odin Topics:** 5.A, 7.A, 13.A  

**TLDR:** Financial well-being fully mediates the relationship between financial behavior and stress among irregular income workers aged 20-40 in Indonesia.

**Problem & Motivation:** Irregular income workers face high stress due to financial instability. Understanding how financial behavior affects stress is important for mental health. The mediating role of financial well-being has not been examined in this vulnerable population.

**Approach (summary):**
- Data collected from 266 irregular income workers aged 20-40 in Indonesia using purposive sampling.
- Instruments included DASS-21 stress scale, Financial Management Behavior Scale, and Financial Well-being Scale.
- Validation study with 200 participants used CFA to confirm factor structures.

**Key Findings (selected):**
- num: Financial well-being fully mediated the effect of financial behavior on stress (indirect effect = -0.5045, 95% CI [-0.6070, -0.4119]).
- Financial behavior positively correlated with financial well-being (β = 0.6566, p < .001).
- Financial well-being negatively correlated with stress (β = -0.6761, p < .001).
- Direct effect of financial behavior on stress was non-significant (β = -0.1039, p = .0564).

**Supports Odin (direct justifications):**
- Improving financial behavior alone does not reduce stress without increasing financial well-being.
- Financial well-being negatively correlates with stress among irregular income workers.
- Each unit increase in financial behavior increases financial well-being by 0.66 standard deviations.

**Limitations / Contradictions for Odin:**
- Online questionnaire may have introduced sampling bias (acknowledged).
- Scope confined to internal variables, excluding external factors like social support (acknowledged).
- Cross-sectional design cannot establish causality [unacknowledged].

**Key takeaways:**
- Financial well-being fully mediates the behavior-stress link.
- Indirect effect of -0.5045 shows strong mediation.
- Good financial behavior improves well-being but not directly reduces stress.

---


## Financial literacy among young college students: Advancements and future directions
**Filename:** `L--Rodriguez-Correa-et_al_summarized.md`  
**Authors:** Rodríguez-Correa, P. A.; Arias García, S.; Bermeo-Giraldo, M. C.; Valencia-Arias, A.; Martínez Rojas, E.; Aurora Vigo, E. F.; Gallegos, A. (2025)  
**ID:** `10.12688/f1000research.159085.3`  
**Odin Topics:** 1.C, 2.C, 5.A, 7.A, 13.A, 13.B  

**TLDR:** A systematic review of 44 studies finds that financial literacy research on college students focuses on financial knowledge and behavior, while budgeting, credit, debt, and digital tools remain underexplored.

**Problem & Motivation:** Young college students face increasing financial responsibilities but lack adequate financial education. Poor financial decision-making can lead to long-term negative outcomes. Existing literature on financial literacy among this population is fragmented and lacks structured guidance on underexplored subtopics.

**Approach (summary):**
- Searched Scopus and Web of Science using title terms 'Financ* literacy', 'Financ* education' with 'University student*' or 'College student*'.
- Applied inclusion criteria: studies on higher education students with quantitative measures of financial literacy analyzed via statistical methods.
- Used PRISMA 2020 methodology to screen 350 records down to 44 peer-reviewed studies from 2003-2023.

**Key Findings (selected):**
- num: 34% of studies use regression analysis, 20% factor analysis, and 18% structural equation modeling.
- Financial literacy and financial knowledge are the most frequently assessed constructs, but the terms are often used interchangeably without clear definition.
- Budgeting is considered a core skill, yet globally students show the least interest in budgeting processes.
- Few studies analyze psychological and behavioral effects of credit card use and student loans on college students.

**Supports Odin (direct justifications):**
- College students lack adequate budgeting skills and show low interest in budgeting processes.
- Financial knowledge alone is insufficient; financial attitude and self-efficacy moderate behavior.
- Credit card use and student debt among young adults require psychological and behavioral analysis.

**Limitations / Contradictions for Odin:**
- Search restricted to title fields only, not abstracts, potentially missing relevant studies.
- Only Scopus and Web of Science databases used; other databases may contain relevant research.
- Non-English publications were excluded, potentially biasing geographic coverage.

**Key takeaways:**
- Financial literacy and knowledge are often used interchangeably in research.
- Budgeting skills are critically low among college students globally.
- num: 34% of studies use regression analysis as primary method.

---


## Financial Management and Commitment to Sending Remittances of Filipina Wives in Virginia, United States
**Filename:** `L--Dimaranan-&-Dy_summarized.md`  
**Authors:** Dimaranan, C. F. D.; Dy, M. F. R. (2025)  
**ID:** `10.29244/jfs.v10i1.62925`  
**Odin Topics:** 1.C, 2.A, 2.B, 7.A, 13.A  

**TLDR:** Filipina wives in Virginia manage household finances through budgeting and savings while regularly sending remittances to families in the Philippines, though emergency requests strain budgets.

**Problem & Motivation:** Limited research exists on how Filipina wives living overseas manage finances for their own families while also remitting to relatives in the Philippines. Understanding this dual financial obligation is critical given the cultural importance of family support and the potential for budget disruption.

**Approach (summary):**
- Qualitative case study of nine Filipina wives residing in Virginia, USA, selected via purposive and snowball sampling.
- Face-to-face in-depth interviews conducted from 2018-2020 covering household income, expenditures, budgeting, financial decision-making, and remittance practices.
- Thematic analysis using description-focused and interpretation-focused coding strategies, with within-case and cross-case analysis.

**Key Findings (selected):**
- num: Monthly household incomes ranged from $5,000 to $22,500, with all households having sufficient income to cover expenses and savings.
- num: Monthly remittances sent to the Philippines ranged from $100 to $500, plus occasional emergency amounts.
- {'All households practice financial management': 'clear goals, monthly budgets (mostly mental), proactive decision-making, and regular savings.'}
- Husbands are primary budget holders in American‑Filipina couple‑led households; Filipina wives hold the budget in Filipino couple‑led households.

**Supports Odin (direct justifications):**
- Filipina wives prioritize savings for children's education, emergencies, and retirement.
- Emergency remittance requests create budget strain and risk savings depletion.
- Husbands are primary budget holders in American‑Filipina households, while wives manage in Filipino couples.

**Limitations / Contradictions for Odin:**
- Small sample size (n=9) limits generalizability to all Filipina wives in the US.
- Numerical data based on participant estimations, not actual financial records.
- Did not include perspectives of husbands or remittance recipients.

**Key takeaways:**
- Monthly remittances range from $100 to $500.
- Emergency requests disrupt budgets and savings.
- Husbands control finances in American-Filipina couples.

---


## Relationship between family resources, financial stress, with financial management among Filipino millennials
**Filename:** `I--Lambert-et_al_summarized.md`  
**Authors:** Lambert, M. J. C. M.; Jusoh, Z. M.; Zainudin, N. (2025)  
**ID:** `f7c3e1a0-2b5d-4a8f-9c6e-1d2b3a4c5d6e`  
**Odin Topics:** 1.A, 1.C, 5.A, 7.A, 13.A, 13.B  

**TLDR:** Financial stress negatively affects financial management among Filipino millennials (β = -0.724), while millennial characteristics positively influence it (β = 0.480).

**Problem & Motivation:** Financial well-being among Filipinos is low despite economic growth, with high financial stress and limited literacy. Millennials face additional pressures from job instability, rising costs, and family obligations. Existing research lacks an integrated understanding of how family resources and financial stress jointly shape financial management in this population.

**Approach (summary):**
- Quantitative correlational design with cross-sectional survey of 400 Filipino millennials in Eastern Visayas, Philippines.
- Multistage random sampling from three cities (Tacloban, Ormoc, Baybay) with Slovin's formula for sample size.
- Online self-administered questionnaire adapted from Pew surveys, Frufonga’s financial stress scale, and Rajnah’s financial management instrument.

**Key Findings (selected):**
- num: Financial stress has a strong negative effect on financial management (β = -0.724, p < .001).
- num: Millennial characteristics have a positive effect on financial management (β = 0.480, p < .001).
- Higher millennial traits (adaptability, collaboration, tech-savviness) are associated with better budgeting, bill payment, and saving practices.
- Financial stress leads to poorer cash management, credit management, retirement planning, and emergency fund behavior.

**Supports Odin (direct justifications):**
- Financial stress reduces financial management effectiveness by 0.724 standardized units per unit increase in stress.
- Millennial characteristics such as digital literacy and adaptability improve financial management by 0.480 standardized units.
- Debt and housing affordability are central stressors requiring policy and product interventions.

**Limitations / Contradictions for Odin:**
- Sample from only three cities in Eastern Visayas limits generalizability.
- Cross-sectional design cannot establish causality between stress and financial management.
- Potential common method bias from single-source self-report surveys.

**Key takeaways:**
- Financial stress reduces financial management by 0.724 standardized units.
- Millennial traits improve financial management by 0.480 standardized units.
- Debt and housing cost are primary stressors for Filipino millennials.

---


## Personal Financial Information Presentation and Consumer Spending
**Filename:** `I--Levi_summarized.md`  
**Authors:** Levi, Y. (2025)  
**ID:** `9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d`  
**Odin Topics:** 5.A, 7.A, 7.B, 11.A, 13.A  

**TLDR:** Presenting net worth as a monthly cash flow under a consumption frame with a salient spending comparison reduces discretionary spending by 15% in a field experiment.

**Problem & Motivation:** Consumers exhibit strong spending habits and inertia, yet existing savings tools like financial education and tax subsidies are costly or benefit only the wealthy. It is unclear whether simple changes in information presentation within online financial apps can influence spending without altering economic variables.

**Approach (summary):**
- Randomized field experiment with 3,138 users of an online account aggregation app over 25 months.
- Users received a personalized index converting net worth to inflation-protected lifetime monthly cash flow.
- Treatments varied index framing (Financial Sustainability Index with fear appeal vs. neutral Life Annuity Index) and salience (context plot comparing index to historical spending vs. no plot).

**Key Findings (selected):**
- num: Users exposed to consumption frame (FSI) and context plot reduced discretionary spending by 15% relative to control.
- num: Effect persisted for 8 months after experiment removal, with gradual convergence after 9 months.
- num: Restaurant spending fell 14%, clothing 20%, entertainment 14%, travel 24%, and cash withdrawals 25%.
- No significant change in non-discretionary categories (gas, groceries, utilities).

**Supports Odin (direct justifications):**
- Presenting net worth as monthly cash flow under a consumption frame reduces discretionary spending by 15%.
- A salient comparison between the index and past spending is necessary for the framing effect to work.
- The spending reduction persists for months after the treatment is removed.

**Limitations / Contradictions for Odin:**
- Data may not include all consumer accounts, potentially offsetting spending changes in unobserved accounts.
- Net worth estimation omits real estate and some retirement or debt accounts, biasing the personalized index.
- Sample is wealthier than average U.S. population, limiting generalizability to lower-income users.

**Key takeaways:**
- A 15% reduction in discretionary spending lasted 8 months after treatment removal.
- Consumption frame and salient context together drive behavior change.
- Effect strongest on tempting categories like restaurants and clothing.

---


## The Effect of Online Buying Decision on Personal Budget of Business Administration Students
**Filename:** `L--Cervantes-et_al_summarized.md`  
**Authors:** Cervantes, J. Z.; Custora, J. M. G.; Duguran, J. C. C.; Malacaya, A. S.; Mendoza, J.; Panga, R. B.; Waminal, E. D. (2025)  
**ID:** `10.61424/rjbe.v3.i3.569`  
**Odin Topics:** 1.C, 5.A, 7.A, 13.A  

**TLDR:** Online buying decisions driven by social media and instant gratification significantly correlate with poor budget management among business administration students.

**Problem & Motivation:** Students have limited financial resources yet face constant online marketing and social pressure to buy impulsively. Existing literature shows online shopping disrupts personal budgets, but evidence specific to Filipino business students is sparse. Understanding this relationship is essential for promoting financial discipline and digital consumer literacy.

**Approach (summary):**
- Used descriptive-correlational design with 153 randomly selected business administration students from Bukidnon State University.
- Adapted a validated questionnaire measuring online buying behavior and budgeting practices on a four-point Likert scale.
- Analyzed data using SPSS with descriptive statistics (frequencies, means, standard deviations).

**Key Findings (selected):**
- num: Pearson r = 0.612 (p < 0.05) indicates a strong positive relationship between online buying decisions and poor budget management.
- num: 83% of respondents were aged 18-24, and 62% were female, a group highly responsive to digital trends.
- num: Mean score for online buying decisions was 3.02 (Agree/High), with social media influence highest at 3.05.
- num: Mean personal budget score was 3.15 (Agree/High), but necessary expenses scored 3.32 (Very High).

**Supports Odin (direct justifications):**
- Online buying decisions driven by social media have a strong positive correlation (r=0.612) with poor budget management.
- Age and civil status significantly affect students' allowance, spending, and savings behaviors.
- Instant gratification motives (stress relief, mood improvement) lead to frequent impulsive unplanned purchases.

**Limitations / Contradictions for Odin:**
- The study focused only on one degree program (Business Administration) at one campus. [unacknowledged]
- Data collection was inside the university premises; results not applicable to non-students.
- The outcome applies only to the 153 randomly selected respondents and cannot be generalized beyond this population.

**Key takeaways:**
- r=0.612 strong correlation between online buying and poor budget management.
- Social media likes and influencer ads most strongly drive impulsive spending.
- Age and civil status affect savings; sex affects savings but not allowance.

---


## The Gig Economy: Financial Challenges and Opportunities Faced by Freelancers
**Filename:** `L--Casalhay-et_al_summarized.md`  
**Authors:** Casalhay, S. F.; Guevarra, C. M.; Bragas, C. M. (2025)  
**ID:** `10.55248/gengpi.6.0525.1716`  
**Odin Topics:** 1.C, 4.B, 5.A, 7.A, 13.A  

**TLDR:** Freelancers in the gig economy face income volatility, lack of benefits, and barriers to financial services, relying on budgeting and savings strategies that are often insufficient for long-term security.

**Problem & Motivation:** Traditional employment models provide stability and benefits, but freelancers in the gig economy lack these protections, leading to financial insecurity. Existing research focuses on the growth of gig work rather than the specific financial behaviors and coping mechanisms of freelancers. This gap hinders the development of tailored financial products and policies to support gig workers.

**Approach (summary):**
- Qualitative study using semi-structured interviews with 50 freelancers in Metro Manila across writing, design, virtual assistance, and software development.
- Participants had at least six months of gig experience; purposive and snowball sampling were used.
- Data were transcribed and analyzed using thematic analysis with NVivo software.

**Key Findings (selected):**
- num: 50 freelancers reported income instability as a primary challenge due to seasonal fluctuations and irregular client payments.
- num: Many freelancers allocate 30% to savings and 70% to expenses when possible, and save 10% of earnings into emergency funds.
- Freelancers lack access to employer-sponsored health insurance, retirement plans, and paid leave, increasing financial burden.
- Financial institutions view freelancers as high-risk borrowers, denying loans and credit due to irregular income.

**Supports Odin (direct justifications):**
- Freelancers experience income volatility due to seasonal fluctuations and irregular client payments.
- Many freelancers lack access to traditional benefits like health insurance and retirement plans.
- Budgeting apps and tracking tools are widely used but insufficient for long-term financial security.

**Limitations / Contradictions for Odin:**
- Small sample size (n=50) and geographic restriction to Metro Manila limit external validity [unacknowledged].
- No comparison group of traditionally employed workers to benchmark financial outcomes.
- The study does not test causal relationships between coping strategies and financial stability [unacknowledged].

**Key takeaways:**
- num: 50 freelancers report income volatility as a primary challenge.
- Budgeting and emergency savings are common but insufficient for long-term security.
- Freelancers lack access to loans, credit, and employer-sponsored benefits.

---


## Financial Literacy and its Effect on the Economic Conditions of Households in Barangay Imbatug
**Filename:** `L--Teh-et_al_summarized.md`  
**Authors:** Teh, C. R.; Caralde, R. T.; Bengado, R. B.; Puclawan, J. C.; Rapirap, A. N.; Salvo, F. L. (2025)  
**ID:** `10.61424/rjbe.v3.i3.564`  
**Odin Topics:** 1.C, 7.A, 13.A, 13.B  

**TLDR:** Financial literacy among 188 households in Barangay Imbatug shows moderate correlation (r=0.50068) with economic condition, though not statistically significant (p>0.05).

**Problem & Motivation:** Households face daily financial difficulties and lack financial knowledge to make sound decisions. The community has common problems with debt and living paycheck to paycheck. Understanding the relationship between financial literacy and economic conditions can inform targeted interventions.

**Approach (summary):**
- Quantitative study using structured questionnaires and face-to-face surveys.
- Simple random sampling selected 188 respondents from three puroks of Barangay Imbatug.
- Instrument measured financial literacy (budgeting, savings, investing, debt, retirement) and economic condition (income, education) on a four-point Likert scale.

**Key Findings (selected):**
- Overall mean financial literacy score was 2.99 (High) and economic condition mean was 3.02 (High).
- {'num': 'Correlation coefficient of 0.50068 indicates a moderate relationship between financial literacy and economic condition.'}
- {'num': 'p-value >0.05, therefore the relationship is not statistically significant.'}
- {'num': '52% of respondents earn ₱10,000-₱15,000 monthly; 30% are aged 18-25 and 45-50 each.'}

**Supports Odin (direct justifications):**
- Households in Barangay Imbatug have high financial literacy (mean 2.99) but only moderate correlation with economic conditions.
- Debt management literacy is very high (mean 3.33) among respondents.
- No statistically significant relationship exists between financial literacy and economic condition (p>0.05).

**Limitations / Contradictions for Odin:**
- Study focused only on three puroks of Barangay Imbatug. [unacknowledged]
- Financial literacy considered only in terms of budgeting, saving, investing, debt management, and retirement planning.
- No longitudinal data to assess changes over time. [unacknowledged]

**Key takeaways:**
- Financial literacy mean score was 2.99 (High) on a 4-point scale.
- Correlation between literacy and economic condition is moderate (r=0.50) but not significant.
- Debt management showed the highest literacy (mean 3.33).

---


## Consumer Autonomy or Illusion? Rethinking Consumer Agency in the Age of Algorithms
**Filename:** `IA--Nokhiz-&-Ruwanpathirana_summarized.md`  
**Authors:** Nokhiz, P.; Ruwanpathirana, A. K. (2025)  
**ID:** `10.23919/JSC.2025.0015`  
**Odin Topics:** 3.A, 5.A, 7.A, 7.B, 13.A  

**TLDR:** Formal analysis shows that obligatory consumption, algorithmic persuasion, and unstable work schedules lead rational consumers to early financial ruin despite utility-maximizing behavior.

**Problem & Motivation:** Consumer agency in digital ecosystems is eroded by systemic barriers like obligatory subscriptions, algorithmic manipulation (e.g., BNPL, personalized ads), and unpredictable work schedules. The authenticity of consumer choices is questioned as external pressures undermine financial autonomy. Existing models lack formal treatment of how limited agency impacts long-term financial stability.

**Approach (summary):**
- Constructs discounted utility models with constraints representing obligatory consumption (fixed amount), impulsive consumption (minimum subsistence plus discretionary spending), and income uncertainty from unstable work schedules.
- Assumes rational utility-maximizing agents with concave utility functions (CRRA) and no borrowing.
- Defines financial ruin as assets reaching zero within finite time.

**Key Findings (selected):**
- {'num': 'Rational consumers with fixed obligatory consumption will go to ruin regardless of utility function concavity.'}
- {'num': 'With impulsive consumption and minimum subsistence, probability of avoiding ruin decays exponentially as exp(-cT) for sufficiently large T.'}
- {'num': 'Lookahead of k steps yields utility advantage of Ω(k) over no lookahead under bounded income.'}
- Algorithmic persuasion and obligatory consumption create value capture, where consumers adopt externally imposed values without critical reflection.

**Supports Odin (direct justifications):**
- Consumers with fixed obligatory expenses face guaranteed ruin under rational utility maximization.
- Algorithmic impulse triggers increase ruin probability exponentially over time.
- Workers with advance schedule notice (lookahead) achieve Ω(k) higher utility than those without.

**Limitations / Contradictions for Odin:**
- Model uses simple intertemporal consumption framework without debt or liabilities.
- Does not incorporate behavioral economics insights like present bias or loss aversion.
- Macroeconomic factors like inflation and recessions not modeled.

**Key takeaways:**
- Fixed obligatory consumption guarantees financial ruin even for rational agents.
- Algorithmic impulse triggers make ruin exponentially more likely over time.
- Knowing work schedules 2 weeks ahead yields significantly higher utility.

---


## Bridging AI and Emotion: Enhanced Models for Personal Finance Manager Applications
**Filename:** `IA--Bader-&-Haraty_summarized.md`  
**Authors:** Bader, S.; Haraty, R. A. (2025)  
**ID:** `10.12785/ijcds/1571107231`  
**Odin Topics:** 3.A, 5.A, 6.A, 6.B, 7.A, 7.B, 8.A, 8.B, 12.B, 13.A  

**TLDR:** An AI-driven financial advisor application integrates anomaly detection, sentiment analysis, and deep learning forecasting (Transformer, TCN, N-BEATS) to provide personalized budgeting, fraud detection, and merchant recommendations.

**Problem & Motivation:** Traditional financial apps rely on static rules and ignore user emotions and unstructured data, leading to poor recommendations and low engagement. There is a gap in leveraging AI to analyze both quantitative transactions and qualitative sentiment for adaptive financial advice.

**Approach (summary):**
- System architecture uses .NET Core 6 backend with Python TensorFlow/Keras for AI modules.
- Data sources: bank transaction logs, MCC merchant codes, account balances, and user profiles.
- Anomaly detection implements Isolation Forest, Local Outlier Factor (LOF), and One-Class SVM models.

**Key Findings (selected):**
- num: Mean Absolute Percentage Error (MAPE) improved from 10.5% to 7.8% when sentiment analysis was incorporated.
- num: Anomaly detection achieved 90% precision, 85% recall, and 0.93 ROC-AUC.
- num: Predictive accuracy within a 90% confidence interval reached 88% alignment with actual user behavior.
- num: Sentiment analysis reduced prediction error by 25% compared to rule-based budgeting systems.

**Supports Odin (direct justifications):**
- Anomaly detection using Isolation Forest and One-Class SVM achieves 90% precision and 85% recall on financial transactions.
- Incorporating sentiment analysis reduces MAPE from 10.5% to 7.8% in spending forecasting.
- Transformer, TCN, and N-BEATS models forecast spending patterns with 88% accuracy within a 90% confidence interval.

**Limitations / Contradictions for Odin:**
- Generalization across diverse financial behaviors and demographics not validated.
- Computational resources required for deep learning models may limit real-time deployment [unacknowledged].
- User trust and human-AI interaction in financial decision-making not studied [unacknowledged].

**Key takeaways:**
- Sentiment analysis improved MAPE from 10.5% to 7.8%.
- Anomaly detection achieved 90% precision and 85% recall.
- Transformer, TCN, and N-BEATS enable personalized spending forecasts.

---


## Development of a Platform for Financial Data Analysis and Adaptive Personal Finance Management
**Filename:** `IA--Kaarov-&- Esenalieva_summarized.md`  
**Authors:** Kaarov, A.; Esenalieva, G. (2025)  
**ID:** `10.20944/preprints202504.2615.v1`  
**Odin Topics:** 3.A, 7.B, 9.A, 9.B, 10.A, 13.A  

**TLDR:** TYIYN is a multilingual mobile app using AI to provide adaptive budgeting, expense categorization, and cash flow estimation with a Flutter-Django stack.

**Problem & Motivation:** Many individuals lack intelligent tools to monitor expenses and receive context-appropriate financial advice, especially in developing economies. Financial ignorance and lack of guidance lead to poor spending, saving, and reactive budgeting. AI-powered finance apps can improve user outcomes through behavior-based recommendations.

**Approach (summary):**
- The app uses Flutter for cross-platform frontend, Django REST Framework for backend API, and PostgreSQL for data storage.
- AI algorithms provide personalized budget advice, expense categorization, and cash flow estimation using Pandas and Matplotlib for analysis.
- Asynchronous tasks (notifications, sync) are handled by Celery and Redis.

**Key Findings (selected):**
- {'num': 'Users who followed AI recommendations increased average monthly savings by 12–18%.'}
- {'num': '45% of users reduced discretionary spending on non-essential items.'}
- {'num': 'Overspending prediction engine achieved approximately 85% precision.'}
- {'num': 'API response times under 200 ms provided a responsive user experience.'}

**Supports Odin (direct justifications):**
- AI-driven personalized financial advice increases average monthly savings by 12–18%.
- Multilingual support improves usability for 87% of non-English speaking users.
- Interactive dashboards lead to more frequent engagement than static reports.

**Limitations / Contradictions for Odin:**
- Manual transaction entry creates user adoption friction.
- Lacks direct banking integration, planned for future using open banking APIs.
- Initial recommendation engine performance required real-world data to improve [unacknowledged].

**Key takeaways:**
- AI recommendations increased savings by 12-18% for active users.
- Multilingual support boosted usability for 87% of non-English speakers.
- Interactive dashboards drive more frequent financial engagement.

---


## FINANCIAL LITERACY AMONG PHILIPPINE NATIONAL POLICE FORCE
**Filename:** `L--Hurley-et_al_summarized.md`  
**Authors:** Hurley, R. Z.; Gonzales, D. T.; Hurley III, R. V.; Zaratan, M. K. P. (2025)  
**ID:** `f47ac10b-58cc-4372-a567-0e02b2c3d479`  
**Odin Topics:** 1.C, 7.A, 13.A, 13.B  

**TLDR:** Financial literacy among Dagupan City police officers is assessed, revealing gaps in budgeting, saving, and investing despite adequate knowledge in some areas, with recommendations for integrating financial education into PNP training.

**Problem & Motivation:** Police officers face irregular income and high-stress conditions, yet PNP training lacks formal personal finance education. This gap leaves officers vulnerable to financial insecurity, negatively impacting job performance and community relations.

**Approach (summary):**
- Mixed-methods study with surveys and interviews of 50 PNP officers in Dagupan City.
- Quantitative analysis of survey data using descriptive statistics and Likert scales.
- Qualitative insights from interviews, focus groups, and case studies.

**Key Findings (selected):**
- num: 42% of officers are aged 31-40, the largest age group.
- num: 60% of respondents are male, 40% female.
- num: 92% are married, indicating shared financial responsibilities.
- num: 42% of participants are Police Staff Sergeants (PSSG), the most engaged rank.

**Supports Odin (direct justifications):**
- Officers with extended financial responsibilities are more likely to seek financial education.
- Most officers create a monthly budget to manage finances.
- Salary loans are the most common form of debt among police officers.

**Limitations / Contradictions for Odin:**
- Small sample size (n=50) limits generalizability to all PNP personnel.
- Self-reported financial literacy may be inflated due to social desirability [unacknowledged].
- Cross-sectional design cannot establish causality between financial literacy and job performance.

**Key takeaways:**
- 42% of officers are ages 31-40 and handle major financial obligations.
- 60% use salary loans, indicating reliance on debt for cash flow.
- Officers agree on budgeting but are neutral on investing in stocks.

---


## DIGITIZATION IN RETAIL BANKING: A REVIEW OF CUSTOMER ENGAGEMENT AND FINANCIAL PRODUCT ADOPTION IN SOUTH ASIA
**Filename:** `I--Koswar-et_al_summarized.md`  
**Authors:** Kowsar, M. M.; Islam, S.; Mohiuddin, M.; Siddiqui, N. A. (2025)  
**ID:** `10.63125/cv50rf30`  
**Odin Topics:** 4.A, 4.B, 8.A, 9.A, 9.B, 10.A, 10.B, 11.A, 11.B, 13.A, 13.B  

**TLDR:** A systematic review of 84 studies finds that mobile infrastructure, AI-driven personalization, and behavioral nudges enhance customer engagement and financial product adoption in South Asian retail banking, though digital divides persist.

**Problem & Motivation:** Digitization transforms retail banking but region-specific evidence for South Asia is scarce. Understanding how mobile banking and fintech affect customer engagement and product adoption is critical for inclusive financial growth. This review synthesizes fragmented literature to identify drivers and barriers.

**Approach (summary):**
- Followed PRISMA 2020 systematic review methodology.
- Searched Scopus, Web of Science, JSTOR, EBSCOhost, ProQuest, Google Scholar, and institutional repositories.
- Used Boolean keyword combinations on digital banking, engagement, product adoption, and South Asia.

**Key Findings (selected):**
- num: Mobile phone penetration exceeds 85% and mobile broadband covers over 95% of the population in India and Sri Lanka.
- num: Digitally engaged customers in India were 2.3 times more likely to open secondary financial products like insurance or investment accounts.
- num: 34 of 84 reviewed studies directly examined product adoption, collectively cited over 4,200 times.
- num: 29 articles on infrastructure expansion were cited over 3,400 times, underscoring their foundational impact.

**Supports Odin (direct justifications):**
- Digitally engaged customers are 2.3 times more likely to adopt secondary financial products.
- Mobile-first interfaces with personalized prompts and goal-setting increase user retention.
- AI-based fraud detection enhances user trust in digital banking environments.

**Limitations / Contradictions for Odin:**
- Relies on secondary data from published studies; no primary data collection. [unacknowledged]
- Geographic scope limited to South Asia; findings may not generalize to Philippines. [unacknowledged]
- Does not address algorithmic cold-start or profile dynamics for new users.

**Key takeaways:**
- 85% mobile phone penetration enables digital banking at scale.
- 2.3x higher product adoption for digitally engaged customers.
- AI nudges and personalization drive user retention and loyalty.

---


## Enhancing Financial Literacy in Young Adults: An Android-Based Personal Finance Management Tool
**Filename:** `I--Imawan-et_al_summarized.md`  
**Authors:** Imawan, R.; Putra, W. P.; Alqahtani, R.; Milakis, E. D.; Dumchykov, M. (2025)  
**ID:** `10.58536/j-hytel.166`  
**Odin Topics:** 3.A, 3.B, 9.A, 9.B, 11.A, 11.B, 12.A, 13.A  

**TLDR:** An Android-based personal finance management app for young adults features income/expense tracking, budgeting, goal setting, and notifications, achieving a 4.6/5 usability score.

**Problem & Motivation:** Young adults face unique financial challenges including limited experience and high online loan usage. Existing financial tools overlook the interactive, mobile-first needs of this demographic. Without targeted intervention, financial illiteracy may perpetuate debt and instability.

**Approach (summary):**
- Waterfall model used for systematic development with phases: requirements analysis, design, implementation, testing, deployment.
- Requirements gathered via interviews and surveys with Indonesian higher education students to identify key processes like income/expense tracking and budget projection.
- Application built with Laravel backend, Flutter frontend, and local SQLite database for offline functionality.

**Key Findings (selected):**
- num: Overall application satisfaction score of 4.6/5, rated 'Excellent'.
- num: 78% of users rated likelihood of continued use at 4 or 5 on Likert scale.
- num: Usability aspect scored 4.72, engagement 4.74, and functionality 4.70.
- Users praised intuitive design, accurate tracking, and motivational reminders for consistent engagement.

**Supports Odin (direct justifications):**
- Mobile-first design with intuitive navigation achieves excellent usability scores (4.6/5).
- Automated notifications encourage consistent financial tracking and habit formation.
- Progress bars on financial goals motivate users to set and achieve savings targets.

**Limitations / Contradictions for Odin:**
- Short two-week evaluation period limits assessment of long-term habit formation.
- Sample of 50 Indonesian university students may not represent all young adult populations.
- No control group to isolate app effects from other factors [unacknowledged].

**Key takeaways:**
- Overall user satisfaction score of 4.6 out of 5.
- Automated notifications reinforce consistent financial tracking habits.
- Progress bars on financial goals increase user motivation.

---


## Financial literacy and sustainable planning assessment among Filipino millennials
**Filename:** `L--Dimaunahan-et_al_summarized.md`  
**Authors:** Dimaunahan, D. S. F.; Santiago, A. F. B.; Eusebio, M. C. C.; Loteriña, S. M. M.; Ong, A. K. S.; Chavez, J. X. S. (2025)  
**ID:** `10.1016/j.actpsy.2025.105334`  
**Odin Topics:** 1.C, 13.A  

**TLDR:** Financial literacy among Filipino millennials is low and does not directly affect financial planning, but monthly income, occupation, and monthly expenses significantly influence planning via goal setting theory constructs.

**Problem & Motivation:** Filipino millennials exhibit low financial literacy and poor financial decision-making, yet no recent studies have assessed their financial literacy and planning. Understanding these factors is crucial for improving financial inclusion and sustainable planning in the Philippines.

**Approach (summary):**
- Data were collected from 400 Filipino millennials in Makati City via online and in-person surveys.
- Financial literacy was measured using Lusardi and Mitchell's "Big Three" questions on interest compounding, inflation, and risk diversification.
- {'Financial planning was operationalized through goal setting theory constructs': 'goal commitment, specificity, acceptance, and difficulty.'}

**Key Findings (selected):**
- num: Mean correct scores were 0.545 for interest compounding, 0.388 for inflation, and 0.338 for risk diversification.
- num: Financial literacy had no significant direct effect on financial planning (β=0.077, p=0.153).
- num: Monthly expenses (β=0.205, p=0.001) and monthly income (β=0.180, p=0.003) showed significant effects on financial planning.
- num: Goal acceptance (β=0.924) and goal commitment (β=0.809) were the strongest predictors of financial planning among goal setting constructs.

**Supports Odin (direct justifications):**
- Financial literacy does not directly affect financial planning among Filipino millennials.
- Monthly income and expenses are significant determinants of financial planning behavior.
- Goal acceptance and goal commitment are strong predictors of financial planning in this demographic.

**Limitations / Contradictions for Odin:**
- Only Makati City residents were surveyed, limiting generalizability.
- Only millennials were included; older generations may differ.
- Only 'The Big Three' questions measured financial literacy; other dimensions omitted.

**Key takeaways:**
- Only 0.545 mean correct on interest compounding, 0.388 on inflation, 0.338 on risk diversification.
- Financial literacy had no significant effect on financial planning (p=0.153).
- Monthly expenses and income were stronger predictors than financial literacy.

---


## Financial literacy and financial wellbeing of youth entrepreneurs: The mediating role of financial behaviour
**Filename:** `I--Isaga_summarized.md`  
**Authors:** Isaga, N. (2025)  
**ID:** `10.20525/ijrbs.v14i7.4383`  
**Odin Topics:** 5.A, 7.A, 13.A, 13.B  

**TLDR:** Financial literacy positively affects financial well-being of youth entrepreneurs in Tanzania, with financial behaviour partially mediating this relationship.

**Problem & Motivation:** The relationship between financial literacy and financial well-being is well established, but the mediating role of financial behaviour among youth entrepreneurs in developing economies remains underexplored. Understanding this mediation is crucial for designing effective financial interventions. This study addresses that gap by focusing on Tanzanian youth entrepreneurs.

**Approach (summary):**
- A cross-sectional design was used with 455 youth entrepreneurs in urban Tanzania.
- Data were collected via structured questionnaires measuring financial literacy, financial behaviour, and financial well-being.
- Structural Equation Modelling (SEM) was employed to test direct and indirect relationships.

**Key Findings (selected):**
- Financial literacy has a significant positive direct effect on financial well-being.
- Financial literacy significantly influences financial behaviour.
- Financial behaviour partially mediates the relationship between financial literacy and financial well-being.

**Supports Odin (direct justifications):**
- Financial literacy significantly improves financial behaviour among youth entrepreneurs.
- Financial behaviour partially mediates the relationship between financial literacy and financial well-being.
- Improving financial behaviour leads to better financial well-being beyond the effect of literacy alone.

**Limitations / Contradictions for Odin:**
- Cross-sectional design cannot establish causality.
- Sample from Tanzania only, not representative of Filipino young professionals. [unacknowledged]
- No objective measures of financial behaviour; reliance on self-reports.

**Key takeaways:**
- Financial literacy alone is insufficient without positive financial behaviour.
- Budgeting, saving, and debt management mediate financial well-being.
- Partial mediation means literacy has both direct and indirect effects.

---


## The Influence of Financial Literacy on the Budgeting Practices among College Students in a Private Catholic School: Input for Student Literacy Program
**Filename:** `L--Templa-et_al_summarized.md`  
**Authors:** Templa, E. L.; Andea, R. J. B.; Bagahansol, J. D. M.; Carreon, R. B.; Comendador, L. G.; Labrador, J. G.; Miscreola, D. J. V.; Tapay, A. J. D.; Uson, P. G. R. A. (2025)  
**ID:** `10.70838/pemj.380810`  
**Odin Topics:** 1.C, 7.A, 13.A  

**TLDR:** Higher financial literacy correlates strongly with better budgeting practices among Filipino college students, explaining 75% of variance in budgeting behavior.

**Problem & Motivation:** College students face financial responsibilities affecting their studies and well-being, yet many lack effective budgeting skills. Prior research shows financial literacy gaps persist globally and in the Philippines. However, few studies examine this relationship in private Catholic schools with unique socioeconomic contexts.

**Approach (summary):**
- Quantitative descriptive-correlational design with 225 randomly selected college students from a private Catholic school in Davao City.
- Validated survey instrument measured five financial literacy dimensions (awareness, attitudes, risk management, culture, knowledge/skills) and four budgeting dimensions (goal setting, financial control, decision-making, financial behavior).
- Pearson correlation and linear regression analysis used to assess relationship and influence between financial literacy and budgeting practices.

**Key Findings (selected):**
- num: Strong positive correlation (r = 0.85, p < 0.001) between financial literacy and budgeting practices.
- num: Financial literacy accounts for approximately 75% of variance in budgeting behavior (R² = 0.723).
- Students demonstrate high financial literacy (mean 3.95/5) with strongest dimension being attitudes towards finance (4.03).
- Budgeting practices also high (mean 3.91/5) with decision-making strongest (4.03) and financial control lowest (3.77).

**Supports Odin (direct justifications):**
- Financial literacy accounts for 75% of variance in budgeting practices among Filipino college students.
- Students with higher financial literacy demonstrate stronger goal setting, financial control, and decision-making in budgeting.
- Managing financial risk is the lowest literacy dimension, indicating a gap for PFMS to address.

**Limitations / Contradictions for Odin:**
- Self-reported data may introduce bias in respondents' assessments. [unacknowledged]
- Study does not account for external factors like socioeconomic background or prior financial education.
- Sample limited to one private Catholic school in Davao City, limiting generalizability. [unacknowledged]

**Key takeaways:**
- Financial literacy explains 75% of budgeting behavior variance.
- Decision-making is the strongest budgeting skill among students.
- Financial risk management is the weakest literacy area.

---


## Does Technology Reduce or Amplify Financial Stress? A Cognitive-Behavioral Perspective on Nigerian Postgraduate Students
**Filename:** `I--Yusuf-et_al_summarized.md`  
**Authors:** Yusuf, J.; Bolaji, H. O.; Ahmed, M. S.; Abdulkareem, H. B. (2025)  
**ID:** `10.23887/jet.v9i4.103004`  
**Odin Topics:** 5.A, 13.A, 13.B  

**TLDR:** Digital financial technologies have a dual role in financial stress among Nigerian postgraduate students, reducing or amplifying it depending on cognitive-behavioral skills and financial literacy.

**Problem & Motivation:** The psychological impact of fintech adoption on student financial stress is understudied, especially in developing countries. Existing literature emphasizes structural economic factors but neglects cognitive and behavioral mechanisms. An integrated perspective is needed to understand whether technology alleviates or worsens financial distress.

**Approach (summary):**
- Conceptual and analytical research design with a qualitative, theory-driven approach grounded in Cognitive-Behavioral Theory (CBT).
- {'Data from secondary sources': 'approximately 70 peer-reviewed articles, policy documents, and empirical studies (2015–2024).'}
- Sources retrieved from Scopus, Web of Science, Google Scholar, and JSTOR using keywords such as financial stress, fintech adoption, and CBT.

**Key Findings (selected):**
- {'Digital financial technologies play a dual role': 'budgeting apps and savings platforms enhance financial awareness and self-efficacy, while impulsive borrowing and fraud exposure trigger cognitive distortions.'}
- Financial stress is shaped more by students’ cognitive interpretations and coping strategies than by technology itself.
- Catastrophizing financial difficulties and negative self-evaluation lead to avoidance behaviors and impulsive borrowing, increasing vulnerability.
- Fintech lending applications encourage rapid credit access, which may lead to unsustainable debt accumulation when used without financial literacy.

**Supports Odin (direct justifications):**
- Digital financial technologies reduce financial stress only when accompanied by adequate cognitive-behavioral skills and financial literacy.
- Misuse of fintech services and impulsive digital borrowing trigger cognitive distortions that exacerbate anxiety and maladaptive financial behaviors.
- Financial stress is shaped more by students’ cognitive interpretations and coping strategies than by technology itself.

**Limitations / Contradictions for Odin:**
- Conceptual and literature-based methodology limits direct measurement of student experiences.
- Evidence synthesized reflects existing literature patterns, not primary data. [unacknowledged]
- Rapid fintech changes may introduce behaviors not yet documented in current research.

**Key takeaways:**
- Digital financial technologies reduce or amplify financial stress depending on user skills.
- Cognitive distortions like catastrophizing intensify financial anxiety.
- Financial literacy alone insufficient; cognitive-behavioral skills are needed.

---


## A Systematic Literature Review on Personal Financial Management Practices: Budgeting, Investment, Debt, and Saving
**Filename:** `I--Elliyana-et_al_summarized.md`  
**Authors:** Elliyana, E.; Maricar, R.; Toalib, R. (2025)  
**ID:** `04e5b9d2-6c3f-5a9e-8b1d-2f4c7a9e6b3d`  
**Odin Topics:** 5.A, 7.A, 13.A, 13.B  

**TLDR:** Financial literacy strongly correlates with better budgeting, saving, investment, and debt management, but behavioral biases and digital tool risks require integrated interventions.

**Problem & Motivation:** Economic uncertainty, digital transformation, and persistently low financial literacy create widespread financial vulnerability. Despite abundant research on discrete PFM behaviors, a unified synthesis tying budgeting, saving, investing, and debt management together is missing. This gap hinders the design of holistic interventions for diverse populations.

**Approach (summary):**
- Systematic literature review following PRISMA 2020 protocol.
- Searched Scopus, Web of Science, Google Scholar, MDPI, and DOAJ for 2018–2024 peer-reviewed open-access studies.
- Used search terms combining financial literacy, budgeting, saving, investment, and debt with personal or household finance.

**Key Findings (selected):**
- num: Only 44% of U.S. adults have sufficient savings to cover a $1,000 emergency expense.
- num: Indonesia's financial literacy index is 49.7% while financial inclusion reaches 85.1%.
- num: Financial education programs explained 26% of the variance in saving behavior in Malaysia.
- Financial literacy alone is insufficient; self-efficacy and behavioral intention mediate the link between knowledge and action.

**Supports Odin (direct justifications):**
- Financial literacy alone does not change behavior without self-efficacy and behavioral intention.
- Budgeting is the foundational PFM behavior that enables saving, investing, and debt reduction.
- Digital financial tools increase user participation but risk harm when literacy is low.

**Limitations / Contradictions for Odin:**
- The review relies on cross-sectional studies; causal relationships cannot be established.
- Grey literature and non-English studies were excluded, potentially missing regional insights.
- The 47-study sample, while systematically selected, may not represent all PFM contexts globally.

**Key takeaways:**
- Financial literacy explains 26% of saving behavior variance.
- Indonesia has 49.7% literacy but 85.1% financial inclusion.
- Budgeting is the foundation for all other PFM behaviors.

---


## PERSONAL FINANCIAL MANAGEMENT BEHAVIOR AND FINANCIAL PLANNING AS KEY DRIVERS OF RETIREMENT PREPAREDNESS AMONG LGU's CONTRACTUAL PERSONNEL
**Filename:** `L--Tambuli-&-Villarba_summarized.md`  
**Authors:** Tambuli, A. P.; Villarba, L. O. (2025)  
**ID:** `f47ac10b-58cc-5372-a567-0e02b2c3d479`  
**Odin Topics:** 1.C, 5.A, 7.A, 13.A  

**TLDR:** Personal financial management behavior and financial planning significantly drive retirement preparedness among LGU contractual personnel in Nabunturan, Philippines.

**Problem & Motivation:** Contractual LGU employees face unstable income and limited savings opportunities, yet no prior study examines how their personal financial management behavior and financial planning drive retirement preparedness.

**Approach (summary):**
- Data from 200 LGU contractual employees in Nabunturan using a simple random sample and a validated survey questionnaire.
- Descriptive-correlational design with mean, standard deviation, Pearson r, and multiple regression analysis.
- Variables measured: retirement preparedness (asset acquisition, budgeting, decision making), personal financial management behavior (cash, credit, savings/investment), and financial planning (retirement savings, abilities).

**Key Findings (selected):**
- num: Personal financial management behavior correlates with retirement preparedness at r = 0.701 (p < .001).
- num: Financial planning correlates with retirement preparedness at r = 0.739 (p < .001).
- num: Combined model explains 61.5% of variance in retirement preparedness (R² = 0.615).
- Retirement savings indicator was only moderately evident (mean 3.37) among contractual employees.

**Supports Odin (direct justifications):**
- Personal financial management behavior has a strong positive correlation with retirement preparedness (r = 0.701).
- Financial planning behavior has a strong positive correlation with retirement preparedness (r = 0.739).
- Personal financial management behavior and financial planning together explain 61.5% of variance in retirement preparedness.

**Limitations / Contradictions for Odin:**
- Cross-sectional design limits causal inference. [unacknowledged]
- Sample restricted to one LGU in Nabunturan, Davao de Oro. [unacknowledged]
- Retirement savings domain showed only moderate evidence (mean 3.37), indicating weak translation of planning to action.

**Key takeaways:**
- Personal financial management behavior correlates strongly with retirement preparedness (r=0.70).
- Financial planning is an even stronger driver (r=0.74) of retirement preparedness.
- Contractual employees have high financial planning abilities but only moderate actual retirement savings.

---


## Understanding Monetary Policy: Student Awareness, Perceptions, and Financial Behaviors in the Philippine Context
**Filename:** `L--Espelita-et-al_summarized.md`  
**Authors:** Atento, R. G.; Espelita, C. A. M.; Rao, L.; Tian, Y. (2025)  
**ID:** `3c6e0b8a-9c1d-5f2a-9e3b-4d7f8a9b0c1d`  
**Odin Topics:** 1.C, 13.A  

**TLDR:** Filipino students show moderate monetary policy awareness, with graduate and business students more knowledgeable; awareness correlates positively with saving and investment but not spending.

**Problem & Motivation:** Limited research examines how young Filipinos understand monetary policy despite its critical role in economic stability and personal financial decisions. Students, as future economic stewards, need literacy to navigate policy impacts on saving, investing, and spending. Without this understanding, policy effectiveness may be undermined and financial behaviors misaligned.

**Approach (summary):**
- Descriptive-correlational survey of 200 Filipino senior high, undergraduate, and graduate students using stratified random sampling.
- Instrument measured monetary policy awareness (10 items), perceptions (10 items), and financial behaviors (saving, investing, spending) on 5-point Likert scales.
- Data analyzed with ANOVA, t-tests, Pearson correlations, and multiple regression using Jamovi and SPSS.

**Key Findings (selected):**
- num: Awareness correlates moderately with perception of policy effectiveness (r = 0.48, p < .001).
- num: Awareness positively correlated with saving behavior (r = 0.31, p < .001) and investment behavior (r = 0.24, p = .001).
- num: Awareness not significantly correlated with spending behavior (r = -0.07, p = .310).
- num: Regression shows awareness and perceptions predict saving (R² = .22) and investment (R² = .15) but not spending (R² = .04).

**Supports Odin (direct justifications):**
- Monetary policy awareness positively correlates with saving behavior (r=0.31, p<.001).
- Graduate students have higher awareness than senior high students (M=3.75 vs 2.80).
- Business and economics students are more aware of monetary policy than non-business peers.

**Limitations / Contradictions for Odin:**
- Cross-sectional design prevents causal inference.
- Self-reported data may introduce social desirability bias.
- Sampling restricted to selected Philippine HEIs and senior high schools, limiting generalizability to all Filipino students.

**Key takeaways:**
- Awareness correlates with saving (r=0.31) but not spending.
- Graduate students show highest monetary policy knowledge.
- Business students more aware than non-business peers.

---


## Financial Management Practices of Employees at Bureau Of Internal Revenue
**Filename:** `L--Cabiles_summarized.md`  
**Authors:** Cabiles, S. L. (2025)  
**ID:** `a0b1c2d3-e4f5-4678-89ab-c0d1e2f3a4b5`  
**Odin Topics:** 13.A, 13.B  

**TLDR:** A survey of BIR employees in Sorsogon City finds strong budgeting and saving but inconsistent spending and investing, with debt accumulation and low interest rate awareness as key challenges, leading to proposed financial literacy programs.

**Problem & Motivation:** Employees face financial management challenges that affect their well-being and productivity. The study addresses gaps in understanding the financial practices of government employees in the Philippines. It aims to identify specific needs for targeted financial literacy interventions.

**Approach (summary):**
- Surveyed permanent employees of BIR RDO 068, Sorsogon City using a Likert-scale questionnaire.
- Measured financial practices across budgeting, spending, saving, and investing domains.
- Collected qualitative data on challenges through open-ended questions.

**Key Findings (selected):**
- num: Employees frequently set up emergency funds (mean 4.32) and track expenses (mean 4.03).
- num: Spending practices show quality prioritization (mean 4.10) but impulse buying occurs sometimes (mean 3.20).
- num: Saving practices are strongest (overall mean 3.87), but higher-risk saving investments are low (mean 2.66).
- num: Investing practices are inconsistent (mean 3.47) with a value-action gap.

**Supports Odin (direct justifications):**
- Employees frequently maintain emergency funds (mean 4.32), justifying automated saving features.
- Debt accumulation is the top challenge, supporting debt tracking and education tools.
- Financial literacy activities improve perceived financial decision-making (mean 4.54).

**Limitations / Contradictions for Odin:**
- Sample limited to one BIR office in Sorsogon City [unacknowledged].
- Self-reported data may be biased [unacknowledged].
- No causal inference due to cross-sectional design [unacknowledged].

**Key takeaways:**
- Employees save well but struggle with consistent investing.
- Debt accumulation and low interest rate awareness are top financial challenges.
- Financial literacy programs are perceived as helpful but knowledge application lags.

---


## MASTERING ECONOMIC AND FINANCIAL SOURCES WITH REFERENCE TO BUDGETING, SAVINGS, EARLY INVESTING, DEBT MANAGEMENT AND THE POWER OF FINANCIAL PLANNING - A COMPREHENSIVE ANALYSIS
**Filename:** `I--Yoganandham_summarized.md`  
**Authors:** Yoganandham, G. (2025)  
**ID:** `7c9e6679-7425-40de-944b-e07fc1f90ae7`  
**Odin Topics:** 7.A, 13.A, 13.B  

**TLDR:** Mastering budgeting, savings, early investing, debt management, and financial planning enables long-term financial stability and independence.

**Problem & Motivation:** Many individuals lack the skills and discipline to manage finances effectively, leading to financial instability and stress. Financial illiteracy, impulsive spending, and delayed investing hinder wealth accumulation and emergency preparedness. Limited awareness of comprehensive financial planning prevents optimal resource allocation and risk mitigation.

**Approach (summary):**
- The study employs a descriptive and diagnostic methodology relying on secondary data.
- Data sources include academic journals, books, expert analyses, official records, and websites.
- Statistical tools and established theoretical frameworks are used to examine key concepts.

**Key Findings (selected):**
- Budgeting using the 50/30/20 rule (50% needs, 30% wants, 20% savings/debt) promotes financial discipline.
- Emergency funds covering three to six months of expenses provide a critical safety net against income shocks.
- Early investing leverages compound growth to turn small contributions into substantial long-term wealth.
- Prioritizing high-interest debt repayment (avalanche or snowball method) reduces financial strain and interest costs.

**Supports Odin (direct justifications):**
- Budgeting that prioritizes needs over wants reduces impulsive spending and financial strain.
- An emergency fund covering 3-6 months of expenses prevents reliance on high-interest debt during crises.
- Starting investments early harnesses compound growth to build long-term wealth with smaller contributions.

**Limitations / Contradictions for Odin:**
- No quantitative evaluation of the proposed strategies. [unacknowledged]
- The paper does not address cultural or demographic variations in financial behavior. [unacknowledged]
- Lacks discussion of digital tools or PFMS-specific implementation challenges. [unacknowledged]

**Key takeaways:**
- Budgeting with the 50/30/20 rule aligns spending with long-term goals.
- A 3-6 month emergency fund is the first savings priority before investing.
- Starting investments early leverages compound growth for wealth accumulation.

---


## AI: Proactive Workforce and Financial Guardians – Transforming Enterprise Systems from Reactive to Predictive
**Filename:** `IA--Pahuja_summarized.md`  
**Authors:** Pahuja, H. (2025)  
**ID:** `10.5281/zenodo.16628566`  
**Odin Topics:** 6.A, 6.B, 8.A, 13.A, 10.A, 10.B, 12.A  

**TLDR:** Proposes an architectural framework using Generative AI and agentic AI to transform reactive enterprise HR and financial systems into predictive, proactive platforms with digital assistants and financial guardianship.

**Problem & Motivation:** Traditional HR and FinTech platforms operate in silos, requiring manual intervention and providing retrospective insights. This fragmentation delays responses and impedes employee satisfaction and financial decision-making. Organizations need predictive AI systems that anticipate needs and deliver personalized guidance.

**Approach (summary):**
- The framework is derived from qualitative analysis of enterprise AI implementations across industries and assessment of performance metrics.
- Digital HR assistants leverage Generative AI, NLP, sentiment analysis, and privacy-preserving architectures for query resolution and onboarding.
- Agentic AI for financial services uses predictive analytics, reinforcement learning for micro-savings, and cash flow forecasting.

**Key Findings (selected):**
- Digital HR assistants reduce administrative burden and enable HR professionals to focus on strategic initiatives.
- Agentic AI with reinforcement learning generates more accumulated savings than fixed rule-based methodologies.
- Proactive financial interventions substantially reduce overdraft incidents and late payment penalties.
- Phased deployment models significantly outperform all-at-once approaches for AI implementation.

**Supports Odin (direct justifications):**
- Reinforcement learning-based savings automation generates more accumulated savings than fixed rule-based methods (Pandey & Awasthi, 2025).
- Proactive financial monitoring substantially reduces overdraft incidents and late payment penalties (Abikoye et al., 2024).
- Phased deployment with continuous ROI tracking improves AI implementation success rates (Bashir, 2024).

**Limitations / Contradictions for Odin:**
- No empirical validation of the proposed framework with real-world user data. [unacknowledged]
- Assumes enterprise-scale infrastructure not applicable to lightweight PFMS. [unacknowledged]
- Does not consider cultural or behavioral differences specific to Filipino users. [unacknowledged]

**Key takeaways:**
- Agentic AI enables micro-savings automation that adapts to user behavior.
- Predictive cash flow models can prevent overdraft fees through timely interventions.
- Phased deployment with ROI tracking increases AI adoption success.

---


## AI-Based Wealth Advisory System using Machine Learning and Predictive Analytics for Personalized Budget Planning
**Filename:** `IA--Bhavana-et_al_summarized.md`  
**Authors:** Bhavana, B. R.; Pavan, D.; Darshan, T. H. Guru (2025)  
**ID:** `10.15662/IJARCST.2025.0805004`  
**Odin Topics:** 3.A, 3.B, 6.A, 6.B, 7.A, 7.B, 7.C, 8.A, 8.B, 10.A, 10.B, 12.A, 12.B, 13.A  

**TLDR:** An AI wealth advisory system integrates classification, forecasting, anomaly detection, and explainable AI to deliver personalized budget planning, achieving 95% anomaly detection accuracy and a 22% improvement in savings.

**Problem & Motivation:** Most personal finance applications are reactive, limited to expense tracking without proactive wealth management or personalized AI-driven advice. A gap exists in consumer-centric financial advisory systems that are both predictive and interpretable, particularly for users with low financial literacy. This paper addresses the need for an intelligent system that combines forecasting, anomaly detection, and explainable recommendations to improve financial outcomes.

**Approach (summary):**
- Data sources include transaction logs, household expenditure surveys, and macroeconomic indicators from World Bank/IMF.
- Preprocessing involves cleaning, normalization, NLP-based categorization (BERT), anonymization, and KNN imputation.
- Classification uses XGBoost, Random Forest, and BERT; forecasting uses ARIMA, Prophet, LSTM, and Transformers in an ensemble.

**Key Findings (selected):**
- num: 95% anomaly detection accuracy achieved in pilot testing.
- num: 22% improvement in savings among participants.
- num: 78% of participants reported enhanced financial literacy.
- num: Expense classification achieved 91% F1-score.

**Supports Odin (direct justifications):**
- AI-based wealth advisory systems can achieve 95% anomaly detection accuracy on personal transaction data.
- Explainable AI methods like SHAP and LIME enhance user trust in personal finance systems.
- Personalized budget recommendations using contextual bandits achieve 41% user adoption rate.

**Limitations / Contradictions for Odin:**
- Small pilot sample (100 users) limits statistical power and generalizability. [unacknowledged]
- Paper does not specify the exact composition of transaction datasets, raising reproducibility concerns. [unacknowledged]
- Potential bias in recommendation algorithms mentioned but not empirically mitigated. [acknowledged]

**Key takeaways:**
- Anomaly detection accuracy reached 95% in pilot testing.
- Savings improved by 22% among system users.
- Expense classification achieved 91% F1-score.

---


## The Effectiveness of Financial Literacy Program on Financial Management Skills of Millennial Teachers
**Filename:** `L--Remonde_summarized.md`  
**Authors:** Remonde, E. A. (2025)  
**ID:** `f47ac10b-58cc-4372-a567-0e02b2c3d479`  
**Odin Topics:** 1.C, 7.A, 13.A, 13.B  

**TLDR:** A financial literacy program significantly improved financial management skills of millennial teachers in Digos City, increasing overall proficiency from approaching proficient to advanced.

**Problem & Motivation:** Millennial teachers lack basic financial literacy, leading to difficulties in budgeting, saving, investing, and debt management. Little research addresses their specific financial challenges in the local context of Digos City. This study assesses a targeted financial literacy program to equip them with necessary skills.

**Approach (summary):**
- A descriptive pre-experimental design with pre-test and post-test surveys was used.
- Participants were 36 millennial teachers from Senior High Schools in Digos City, selected via purposive sampling.
- {'The financial literacy program covered ten areas': 'savings, budgeting, investing, debt management, emergency funds, insurance, loan management, expenditure management, tax planning, and retirement planning.'}

**Key Findings (selected):**
- Pre-test overall mean score was 32.22 (approaching proficient), with lowest in investing skill (3.14).
- Post-test overall mean score increased to 43.19 (advanced), with all areas reaching advanced level.
- {'num': 'Paired t-test showed a statistically significant improvement (p < .001).'}
- Debt management had the highest post-test mean (4.00) and investing skill the lowest (4.28) among advanced scores.

**Supports Odin (direct justifications):**
- Financial literacy programs significantly improve budgeting skills among millennial teachers.
- Debt management skills increase substantially after targeted financial education.
- Investment knowledge remains the lowest area even after training, indicating need for focused content.

**Limitations / Contradictions for Odin:**
- No control group, so improvements could be due to maturation or testing effects.
- Small sample size from a single geographic area limits external validity.
- Reliance on self-reported multiple-choice tests may not capture actual financial behavior change.

**Key takeaways:**
- Financial literacy program raised overall proficiency from 32.22 to 43.19.
- Investing skills remained the weakest area even after training.
- Debt management showed the highest post-test mean score.

---


## Financial Edutainment: The Effect of Social Media Usage on the Financial Literacy of Students in Bulacan
**Filename:** `L--Sarmiento-et_al_summarized.md`  
**Authors:** Sarmiento, A. G.; Rivera, L. M.; Cortez, W. (2025)  
**ID:** `10.69569/jip.2025.630`  
**Odin Topics:** 1.A, 1.C, 13.A, 13.B  

**TLDR:** Social media usage positively affects financial literacy of Bulacan students, explaining 68.9% of variance in literacy scores.

**Problem & Motivation:** Filipino students increasingly rely on unverified social media financial content due to gaps in formal financial education. Only 25% of Filipino youth aged 15-24 demonstrate adequate financial literacy. It is unclear whether financial edutainment supplements learning or fosters confusion and poor financial decisions.

**Approach (summary):**
- Survey of 556 students in Bulacan using purposive sampling.
- Instruments adapted from Cabral et al. (2024) for financial literacy and Cao et al. (2020) for social media usage.
- 4-point Likert scale validated with Cronbach's alpha of 0.89 (literacy) and 0.82 (social media usage).

**Key Findings (selected):**
- num: Social media usage explains 68.9% of variance in overall financial literacy (R²=0.689, p<0.001).
- num: Budgeting shows the strongest relationship (β=0.751, R²=0.667), followed by debt management (β=0.719, R²=0.629).
- num: TikTok is the most used platform for financial content (mean=3.748), then Facebook (mean=3.397).
- Students passively view financial influencer content several times a month (27.7%) but rarely seek it actively (31.8% search once a month).

**Supports Odin (direct justifications):**
- Social media usage explains 68.9% of variance in financial literacy among students.
- TikTok is the most used platform for financial content with mean score 3.748.
- Students are more motivated to save by social media than to learn new saving techniques.

**Limitations / Contradictions for Odin:**
- Purposive sampling may introduce selection bias [unacknowledged].
- Regression analysis does not prove causation despite causal design claim [unacknowledged].
- No actual behavioral measures (e.g., savings history, app usage) were collected; only self-reports.

**Key takeaways:**
- Social media explains 68.9% of financial literacy variance.
- TikTok is the top platform for financial content among students.
- Students passively consume financial content several times monthly.

---


## Mental Accounting Through Two-stage Budgeting Under Bounded Rationality
**Filename:** `IA--Pretnar-et_al_summarized.md`  
**Authors:** Pretnar, N.; Olivola, C. Y.; Montgomery, A. (2025)  
**ID:** `10.21203/rs.3.rs-7730348/v1`  
**Odin Topics:** 5.A, 5.C, 6.A, 6.B, 7.A, 13.A, 13.B  

**TLDR:** A model of two-stage budgeting with cognitive constraints shows consumers exhibit heterogeneous bounded rationality, updating only half of budgets weekly, with mental accounting affecting spending and savings.

**Problem & Motivation:** Classical two-stage budgeting assumes perfect fungibility and ex-post budget adherence. Behavioral evidence suggests consumers use mental accounting and sticky budgets, but field evidence is lacking. This paper quantifies how cognitive constraints and budget rigidities explain observed expenditure patterns.

**Approach (summary):**
- Builds a dynamic model with planner/doer structure, mental accounting state variable, and sparse budget updates.
- Uses weekly agent-level expenditure data from 2,509 low-income prepaid debit card users spanning September 2013 to January 2016.
- Estimates structural parameters via Bayesian MCMC with latent change-point inference, sampling over four million parameters.

**Key Findings (selected):**
- num: Consumers update only 2.48 budgets per week on average (out of 4 categories) in baseline, 2.11 with $1 numeracy threshold.
- num: 68% of consumers do not benefit from forced weekly full budget updates; 3.3% go bankrupt under forced attention in $1-threshold model.
- Ex-ante most consumers (79%) are budget prioritizers (mental accounting), but ex-post a plurality (43-47%) are spendthrifts who increase spending regardless of prior over/under-spending.
- {'Heterogeneous rationality': 'most consumers are neither fully rational (always update all budgets) nor fully bounded (never update).'}

**Supports Odin (direct justifications):**
- Consumers update only a subset of budgets each period due to cognitive constraints.
- Forcing full budget attention reduces welfare for 68% of consumers.
- Bankrupt consumers exhibit stickier budgets and planning fallacy syndrome.

**Limitations / Contradictions for Odin:**
- Data limited to low-income prepaid debit card users, not generalizable. [unacknowledged]
- Model assumes strong separability and Stone-Geary utility, potentially unrealistic. [unacknowledged]
- Latent budgeting inference is model-dependent and lacks direct validation. [acknowledged]

**Key takeaways:**
- 2.11 average weekly budget updates under $1 numeracy threshold.
- 68% of users worse off with full budget attention.
- Bankrupt consumers have only 1.25 updates per week.

---


## How does financial literacy affect financial behavior over the life cycle? Evidence from Filipino households
**Filename:** `L--Cacnio-&-Romarate_summarized.md`  
**Authors:** Cacnio, F. Q.; Romarate, M. E. G. (2024)  
**ID:** `3f2a1b4c-5d6e-7f8a-9b0c-1d2e3f4a5b6c`  
**Odin Topics:** 1.C, 5.A, 7.A, 13.A, 13.B  

**TLDR:** Financial literacy, particularly financial aptitude, positively correlates with having retirement plans and insurance, while higher financial attitude improves loan timeliness; young adults show higher literacy than older cohorts.

**Problem & Motivation:** Prior studies focus on developed countries, leaving a gap in developing country contexts. The Philippines has low financial literacy, yet no research examines age-dependent effects on short- and long-term behaviors. Understanding this link can inform targeted financial education programs.

**Approach (summary):**
- Data from 2018 BSP Consumer Finance Survey covers 7,084 Filipino households with annual income ≥₱10,000 and expenditure ≥₱1,000.
- Financial literacy index combines financial attitude (spending attitude, risk attitude, time discounting) and financial aptitude (loan, deposit, surplus scores), each equally weighted.
- OLS regression identifies determinants of financial literacy including age, gender, income, education, children, and remittances.

**Key Findings (selected):**
- num: Young adults have mean financial literacy index 0.392, higher than middle-aged (0.387) and seniors (0.370).
- num: Higher financial attitude increases likelihood of paying loans on time (odds ratio 4.011, p<0.05).
- num: Higher financial aptitude strongly predicts having pension/retirement plan (OR 85.478) and insurance (OR 46.808).
- Higher financial literacy (both attitude and aptitude) is associated with lower likelihood of spending within income (OR 0.435 and 0.051 respectively).

**Supports Odin (direct justifications):**
- Young adults have higher financial literacy than middle-aged and senior Filipinos.
- Higher financial attitude scores increase the probability of paying loans on time.
- Financial aptitude is a strong predictor of having a retirement or pension plan.

**Limitations / Contradictions for Odin:**
- Financial literacy index excludes knowledge questions due to survey constraints. [unacknowledged]
- Data from 2018 may not reflect post-pandemic financial behavior. [unacknowledged]
- Small sample for loan payment regression (n=1,743) limits statistical power.

**Key takeaways:**
- Young adults in the Philippines have higher financial literacy than older cohorts.
- Financial aptitude is a far stronger predictor of retirement plans than financial attitude.
- Higher financial literacy correlates with spending beyond income, possibly due to higher consumption.

---


## Harmonizing Work and Higher Education: Analysis of the Circular Flow of Income in the Philippine Setting
**Filename:** `L--Easdown-et_al_summarized.md`  
**Authors:** Easdown, D. M. P.; Manlongat, M. C.; Abante, M. V.; Caisip, A.; Vigonte, F. G. (2024)  
**ID:** `c9a3b7d4-2f1e-5a6b-8c9d-0e1f2a3b4c5d`  
**Odin Topics:** 1.A, 1.C, 2.A, 13.A  

**TLDR:** Higher education investments by Filipino working professionals enhance individual financial stability and economic engagement, strengthening the circular flow of income and reducing inequality.

**Problem & Motivation:** Research on higher education's economic impact largely focuses on macro-level growth, neglecting how working professionals' educational investments affect personal financial behaviors and the circular flow of income in the Philippine setting. The gap is critical because understanding these microeconomic dynamics can inform policies that leverage education to reduce income inequality and boost national resilience.

**Approach (summary):**
- Systematic literature review following PRISMA methodology to ensure transparent and reproducible selection.
- Searched Google Scholar and SSRN using keywords 'economic growth', 'income distribution', and 'professional development'.
- Included studies from 2017 onward, prioritizing local Philippine publications and English-language articles.

**Key Findings (selected):**
- Higher education correlates with increased income, job security, and socio-economic mobility for Filipino professionals.
- Educated professionals exhibit advanced financial literacy and engage in diversified economic activities, producing a multiplier effect.
- Income inequality restricts household spending to basic necessities, reducing discretionary spending and economic dynamism.
- Graduate degree programs, such as MBA, enhance job performance and promotion prospects, motivating educational investment.

**Supports Odin (direct justifications):**
- Higher educational attainment correlates with higher income and job security for Filipino professionals.
- Educated professionals increase consumption, savings, and investments, enhancing the circular flow of income.
- Outcomes-Based Education improves student skills for entrepreneurship and economic participation.

**Limitations / Contradictions for Odin:**
- Systematic review may miss recent unpublished studies or grey literature. [unacknowledged]
- Exclusion of non-English and international studies limits generalizability of findings. [unacknowledged]
- No empirical validation; relies on secondary sources that may have inherent biases. [unacknowledged]

**Key takeaways:**
- Higher education boosts income and financial engagement for Filipinos.
- Educated professionals drive economic growth through savings and investment.
- OBTL curriculum prepares students for entrepreneurship and leadership.

---


## EMPOWERING YOUNG ADULTS THROUGH FINANCIAL MANAGEMENT: IMPLICATIONS FOR ACHIEVING THE SDGS AMONG INDONESIAN STUDENTS IN THE PHILIPPINES
**Filename:** `I--Kusumaningsih-et_al_summarized.md`  
**Authors:** Kusumaningsih, A.; Mariana; Handayani, S. (2024)  
**ID:** `f47ac10b-58cc-4372-a567-0e02b2c3d479`  
**Odin Topics:** 1.C, 3.A, 7.A, 13.A  

**TLDR:** Indonesian students in the Philippines prioritize long-term savings and use digital tools for budgeting but face uncontrolled spending and peer pressure, revealing gaps between financial knowledge and practice.

**Problem & Motivation:** International students encounter unique financial challenges such as currency fluctuations, unfamiliar banking systems, and social pressures that hinder effective money management. Poor financial handling can lead to stress and academic difficulties, yet tailored interventions for this demographic are lacking. Understanding these factors is essential to support financial well-being and contribute to poverty reduction and responsible consumption (SDGs).

**Approach (summary):**
- Qualitative descriptive design using online surveys and semi-structured interviews with Indonesian students enrolled in Philippine universities.
- Purposive sampling captured diversity in age, gender, and academic background; 88% of respondents aged 18-24, 65% female.
- Surveys included closed and open questions on budgeting, saving, investment, and technology use; interviews explored personal financial philosophies and challenges.

**Key Findings (selected):**
- num: 92% of students have long-term financial goals (savings 31.6%, investment 22.8%, further education 19.3%).
- num: Only 26.9% stick to their budget despite 85% rating financial planning as very important.
- num: 46.2% save 10% of monthly income, and 42.3% have tried investing, but 61.5% have not invested further.
- num: 63.9% use digital tools for financial management, yet only 23.1% rate them as very effective.

**Supports Odin (direct justifications):**
- Only 26.9% of young adults stick to their budget despite 85% acknowledging its importance.
- Peer influence affects 23.4% of students' spending decisions, often overriding financial plans.
- 63.9% use digital tools but only 23.1% find them very effective, indicating a usability and literacy gap.

**Limitations / Contradictions for Odin:**
- Qualitative design with limited sample size; findings may not be statistically representative. [unacknowledged]
- No longitudinal data to assess whether financial behaviors change over time. [unacknowledged]
- Relies on self‑reported data, which may be subject to social desirability bias. [unacknowledged]

**Key takeaways:**
- Only 26.9% of young adults follow their budget.
- Peer pressure is a top barrier for 23.4% of students.
- Digital tool effectiveness is perceived as low at 23.1%.

---


## The Traditional Way of Saving Money Versus the Modern Style of Investment: The Financial Management Styles of Sorsogon State University (Sorsu) Bulan Campus Faculty Members
**Filename:** `L--Bongalonta-et_al_summarized.md`  
**Authors:** Bongalonta, M. B.; Bongalonta, M. M.; Gigantoca, S. E. (2024)  
**ID:** `10.11594/ijmaber.05.08.32`  
**Odin Topics:** 1.C, 2.A, 7.A, 13.A, 13.B  

**TLDR:** Faculty members of Sorsogon State University Bulan Campus adopt both traditional saving methods and modern investments, but face challenges including rising costs, low financial literacy, poor debt management, and delayed salaries.

**Problem & Motivation:** Faculty members experience financial difficulties despite government salaries, often resorting to borrowing and facing insolvency. There is a need to understand their financial management styles to enhance saving capacity. This study identifies practices, problems, and formulates a financial model.

**Approach (summary):**
- Mixed design using survey and focus group discussions with 40 faculty members from Sorsogon State University Bulan Campus.
- Quantitative survey collected profile data on age, gender, salary, expenses, savings percentage, and saving modalities.
- Qualitative FGDs were transcribed and coded using open coding to identify themes on saving practices and problems.

**Key Findings (selected):**
- num: 60% of faculty respondents save 15% or less of their income.
- num: 62.5% earn P40,001–P50,000 monthly, while 82.5% have monthly expenses above P12,000.
- Budgeting, paluwagan, piggy banks, bank deposits, and stock investments are common saving practices.
- Increasing utility costs, unexpected expenses, lack of financial literacy, poor debt management, and low/delayed salaries are key problems.

**Supports Odin (direct justifications):**
- Faculty members save only 0-15% of income, indicating low savings capacity.
- Paluwagan participation often leads to debt instead of savings.
- Low and delayed salaries are primary barriers to saving for non-permanent faculty.

**Limitations / Contradictions for Odin:**
- Small sample size (N=40) from a single campus. [unacknowledged]
- Self-reported survey and FGD data may introduce social desirability bias. [unacknowledged]
- No statistical inference or hypothesis testing performed. [acknowledged as descriptive]

**Key takeaways:**
- 60% of faculty save 15% or less of their income.
- Paluwagan often leads to debt rather than savings.
- Budgeting is the most common saving practice.

---


## AI-Powered Financial Insights Platform
**Filename:** `IA--Reddy-et_al_summarized.md`  
**Authors:** Reddy, S. T.; C., S.; G., T.; BG, D.; Gupta, S. (2024)  
**ID:** `c3b5c3d0-8f3a-5a1c-9e2a-4f7b8c9d0e1f`  
**Odin Topics:** 3.A, 3.B, 6.A, 6.B, 7.B, 7.C, 10.A, 10.B, 12.A, 12.B, 13.A, 13.B  

**TLDR:** A full-stack AI personal finance platform with conversational CA advisor, receipt scanner, portfolio tracker, EMI calculator, and LSTM spending forecast.

**Problem & Motivation:** Indian working-class and students lack affordable, personalized financial advisory. Existing apps like Mint are US-only, and Indian investment platforms lack budgeting and AI advice. No unified system covers budgeting, investment, EMI, tax planning with user-specific data.

**Approach (summary):**
- Built Next.js 15 full-stack with PostgreSQL, Prisma, and Clerk authentication.
- Conversational AI uses Groq LLAMA 3.1 8B/70B for intent parsing, investment advice, and CA Arjun persona.
- Receipt scanner uses Google Gemini 1.5 Flash with multimodal prompt extracting amount, merchant, category.

**Key Findings (selected):**
- num: Dashboard initial load 420ms to first meaningful content.
- num: Receipt scan average 2.1 seconds with >92% accuracy (citing prior research).
- num: Live portfolio fetch for 10 holdings in 1.4 seconds.
- num: EMI schedule creation for 60 months takes 180ms DB round-trip.

**Supports Odin (direct justifications):**
- Multi-modal transformer models like Gemini achieve >92% OCR accuracy for receipts.
- LSTM networks can forecast cash flow trajectories in personal finance apps.
- LLAMA 3.1 70B with structured JSON prompts reduces hallucination for investment recommendations.

**Limitations / Contradictions for Odin:**
- Geographical and regulatory focus on India limits external validity. [unacknowledged]
- Dependency on third-party APIs (Yahoo Finance, MFAPI.in) introduces failure risk. [acknowledged]
- Requires 3 months of user financial context for AI to provide accurate advice (cold-start). [acknowledged]

**Key takeaways:**
- Receipt scanner achieves sub-2.1s processing with >92% accuracy.
- LLAMA 3.1 8B delivers sub-200ms intent classification.
- Dashboard initial load at 420ms using SSR and Suspense.

---


## Navigating Financial Struggle: The Ripple Effect of Inflation Rates on Working Students
**Filename:** `L--D._et-al_summarized.md`  
**Authors:** D, Althea Grace; R, Valerie Mae; G, Lazaro Bryan Louis (2024)  
**ID:** `10.62225/2583049X.2024.4.3.2862`  
**Odin Topics:** 1.C, 7.A, 13.A  

**TLDR:** Inflation increases financial strain on working students, forcing budget adjustments, prioritizing necessities, and seeking government aid.

**Problem & Motivation:** Rising inflation rates disproportionately burden working students who balance academic and financial obligations. Limited research examines how this demographic navigates escalating costs and what coping strategies they employ. Understanding these dynamics is essential for designing targeted support systems.

**Approach (summary):**
- Qualitative phenomenological study with 6 interviewees and 10 quantitative participants.
- Convenience sampling of working students from Noveleta Senior High School, Philippines.
- Data collected via open-ended questionnaires to explore financial struggles and coping mechanisms.

**Key Findings (selected):**
- Working students experience disqualification or slot shortages when accessing government financial aid.
- Budgeting and prioritizing necessities (food, bills, tuition) are primary coping strategies.
- Students pack lunch or eat at carinderia to save money.
- Inflation reduces purchasing power and increases stress, forcing students to work more hours.

**Supports Odin (direct justifications):**
- Inflation forces working students to reduce discretionary spending and prioritize essentials like food and tuition.
- Accessing government financial aid is hindered by bureaucratic barriers and limited slots.
- Balancing work and study during inflation reduces academic time and increases stress.

**Limitations / Contradictions for Odin:**
- Qualitative design with small sample size limits statistical generalizability. [unacknowledged]
- No comparison group of non-working students to isolate inflation effects. [unacknowledged]
- Convenience sampling may introduce selection bias. [unacknowledged]

**Key takeaways:**
- Inflation forces working students to prioritize essentials over wants.
- Budgeting and packing lunch are common coping strategies.
- Accessing government financial aid faces bureaucratic barriers.

---


## Essays on the Causes and Consequences of Employment Uncertainty
**Filename:** `I--Ramos-2024b_summarized.md`  
**Authors:** Ramos, Vincent Jerald R. (2024)  
**ID:** `fc5e6d7c-8b9a-4a1e-9f2d-3c4b5a6d7e8f`  
**Odin Topics:** 1.C, 5.A, 13.A  

**TLDR:** Employment uncertainty, operationalized through informal work, fixed-term contracts, recession entry, social class, and caregiving, has persistent negative effects on fertility behavior and intentions across the Philippines and Germany.

**Problem & Motivation:** Employment uncertainty is a global phenomenon with profound demographic consequences, yet its multiple dimensions and causal effects on fertility are understudied. Prior research lacks integration of various uncertainty types and robust causal identification. This dissertation examines how different forms of employment uncertainty affect fertility decisions across contexts.

**Approach (summary):**
- Chapter 2 uses difference-in-differences on Philippine Labor Force Surveys (2016-2020) to estimate extreme lockdown effects on informal employment.
- Chapter 3 uses optimal full matching and Cox PH models on German SOEP to analyze fixed-term and recession entry effects on first birth hazards within 10 years.
- Chapter 4 uses piecewise constant event history and cure fraction models on SOEP to assess social class and second birth rates.

**Key Findings (selected):**
- num: Extreme lockdowns increased informal employment probability by 1.7 percentage points for women but not for men.
- num: Female fixed-term labor market entrants had a 19% lower first birth hazard within 10 years.
- num: Male recession entrants had a 23% lower first birth hazard within 10 years.
- Upper service class members have strongly elevated second birth rates compared to semi-/unskilled workers.

**Supports Odin (direct justifications):**
- Extreme lockdowns increase informal employment probability for women by 1.7 percentage points.
- Female fixed-term labor market entrants have 19% lower first birth hazard within a decade.
- Male recession entrants have 23% lower first birth hazard within a decade.

**Limitations / Contradictions for Odin:**
- LFS data undercounts informal employment, potentially underestimating lockdown effects.
- Analysis in Chapter 3 limited to first 10 years post-entry due to sample attrition.
- Vignette experiment measures ascribed intentions, not actual fertility behavior. [unacknowledged]

**Key takeaways:**
- Extreme lockdowns increased women's informal employment by 1.7 percentage points.
- Fixed-term entry reduces first birth hazard for women by 19% over 10 years.
- Male recession entrants have 23% lower first birth hazard within a decade.

---


## Exploring the Influence of Financial Literacy and Lifestyle Choices on Financial Management Practices among Young Workers in Batam City's Urban Landscape
**Filename:** `I--Raya_summarized.md`  
**Authors:** Raya, S. I. (2024)  
**ID:** `d9e8f7a6-5b4c-3d2e-1f0a-9b8c7d6e5f4a`  
**Odin Topics:** 1.C, 2.C, 5.A, 7.A, 13.A, 13.B  

**TLDR:** Higher financial literacy correlates with better financial management among young workers in Batam City, while urban lifestyle choices and peer influence negatively affect spending and debt practices.

**Problem & Motivation:** Young workers in Batam City face financial challenges from rising living costs and diverse lifestyle options. Limited financial literacy exacerbates inadequate planning, debt accumulation, and insufficient savings. The interplay between lifestyle choices and financial literacy lacks comprehensive research, necessitating this study.

**Approach (summary):**
- Mixed-methods design combining quantitative surveys and qualitative semi-structured interviews/focus groups.
- Purposive sample of young workers across diverse ages, education levels, and employment sectors in Batam City.
- Survey collected demographics, lifestyle choices, financial literacy levels, and financial management practices.

**Key Findings (selected):**
- Positive correlation between higher financial literacy and more robust savings habits.
- Urban lifestyle associated with greater challenges in debt management.
- Lifestyle preferences for entertainment and discretionary spending correlate with conservative investment approaches.
- Discrepancy exists between theoretical financial knowledge and practical application in daily decisions.

**Supports Odin (direct justifications):**
- Higher financial literacy positively correlates with consistent savings habits among young workers.
- Urban lifestyle increases challenges in debt management for young professionals.
- Peer influence significantly shapes spending patterns in urban social circles.

**Limitations / Contradictions for Odin:**
- Sample size constraints limit generalizability beyond Batam City.
- Self-reporting biases in survey responses may affect validity.
- Subjective nature of qualitative data introduces potential interpretation bias.

**Key takeaways:**
- Financial literacy alone does not guarantee prudent financial decisions due to lifestyle pressures.
- Urban living and peer influence are key determinants of young workers' financial behaviors.
- Tailored financial education should bridge theory and practical application.

---


## Financial Practices among Foundation University Employees: Basis for Financial Plan
**Filename:** `L--Paghasian_summarized.md`  
**Authors:** Paghasian, M. F. (2024)  
**ID:** `10.69569/jip.2024.0198`  
**Odin Topics:** 1.C, 3.A, 5.A, 13.A, 13.B  

**TLDR:** Foundation University employees demonstrate strong financial practices in income management, expenditure tracking, and saving, but lack emergency funds; positive practices correlate with higher investment levels.

**Problem & Motivation:** Employees' financial practices impact well-being and job satisfaction, yet many lack adequate financial literacy and emergency funds. Understanding these practices is needed to design effective financial wellness programs.

**Approach (summary):**
- Survey of 191 regular and probationary employees at Foundation University using a validated questionnaire.
- Measured financial practices across income, expenditure, saving, and investment domains using Likert scales.
- Used weighted means, multiple linear regression, Kruskal-Wallis, and Mann-Whitney U tests for analysis.

**Key Findings (selected):**
- Employees agree on prudent income management (mean 3.81) including budgeting and avoiding debt.
- Employees lack emergency funds (mean 3.40, only moderately agree).
- Expenditure practices are strong (mean 3.83) with use of discounts and avoiding impulse buys.
- Saving practices are sound (mean 3.84) prioritizing debt reduction before saving.

**Supports Odin (direct justifications):**
- Employees with strong saving patterns allocate more to monthly investments (coef 6594.35, p=0.040).
- Only moderate agreement on seeking financial advisor advice (mean 3.17) indicates opportunity for automated guidance.
- 61.26% of employees use regular savings accounts, suggesting preference for low-risk liquid investments.

**Limitations / Contradictions for Odin:**
- Only regular and probationary employees included, not all staff.
- Confidentiality concerns led to some withheld income and investment data.
- Busy schedules caused delays and missing responses.

**Key takeaways:**
- Employees lack emergency funds despite strong other practices.
- Saving and investment practices positively predict monthly investment levels.
- Expenditure discipline negatively correlates with investment amounts.

---


## UNDERSTANDING FINANCIAL BEHAVIOR: AN ANALYSIS OF PERSONAL FINANCIAL MANAGEMENT AMONG WORKING PROFESSIONALS AMIDST THE GLOBAL INFLATION SURGE
**Filename:** `L--Natal-et_al_summarized.md`  
**Authors:** Natal, T. M.; Bentulan, K. K.; Del Rosario, R. J.; Olazo, C. B.; Mangarin, J. A. (2024)  
**ID:** `10.5281/zenodo.10892981`  
**Odin Topics:** 1.A, 1.C, 13.A  

**TLDR:** Working professionals aged 24-35 in Balayan, Batangas prioritize saving and reduce spending during inflation, with no demographic differences in saving or buying behavior.

**Problem & Motivation:** Personal financial management among single working professionals in Balayan, Batangas during the global inflation surge remains unexplored. Inflation erodes purchasing power and strains household budgets, yet no prior research examined how this demographic adjusts saving and spending. Understanding these behaviors is essential for designing targeted financial support.

**Approach (summary):**
- Mixed-methods design with quantitative survey (n=75) using a 4-point Likert scale and qualitative semi-structured interviews (n=25, five per industry).
- Participants were single working professionals aged 24-35 from education, finance, government, healthcare, and retail industries in Balayan, Batangas.
- Quantitative analysis used frequency distribution, mean scores, and Pearson Chi-square tests for demographic relationships.

**Key Findings (selected):**
- num: General weighted mean for saving habits was 3.56 (Strongly Agree), with highest item 'save for secure future' at 3.69.
- num: General weighted mean for buying behavior was 3.35 (Strongly Agree), with 'assess practical value' highest at 3.59.
- num: Chi-square tests showed no significant relationship between age (p=0.62), gender (p=0.224), industry (p=0.244), employment type (p=0.598), or income (p=0.241) and saving habits.
- num: No significant relationship between any demographic variable and buying behavior (all p > 0.05).

**Supports Odin (direct justifications):**
- Demographic characteristics (age, gender, income, industry) do not predict saving habits during inflation.
- Professionals consistently prioritize saving over non-essential purchases with mean 3.54 out of 4.
- Tracking monthly expenditures is the lowest-ranked saving habit, suggesting need for automated tracking in PFMS.

**Limitations / Contradictions for Odin:**
- Single municipality and narrow age range limit external validity. [unacknowledged]
- Self-reported Likert scale data subject to social desirability bias. [unacknowledged]
- No control for prior financial literacy levels or debt status.

**Key takeaways:**
- Saving habits mean 3.56 out of 4 during inflation surge.
- No demographic factor significantly predicts saving or buying behavior.
- Professionals save for a secure financial future as top priority.

---


## A qualitative investigation of financial decision-making and enabling factors among ethnic minority young adults in Hong Kong
**Filename:** `I--Cho_summarized.md`  
**Authors:** Cho, Esther Y.-N. (2024)  
**ID:** `10.1057/s41599-024-03605-1`  
**Odin Topics:** 1.C, 2.A, 5.A, 7.A, 13.A, 13.B  

**TLDR:** Ethnic minority young adults in Hong Kong employ diverse budgeting strategies, save about one-third of their income, use informal borrowing and credit cards, face fraud risks, and are enabled by family capital, self-discipline, peer support, and financial knowledge.

**Problem & Motivation:** Current understanding of financial decision-making among racial/ethnic minority young adults is limited because day-to-day decisions are underexamined, younger minorities receive little attention, studies are mainly Western, and research is predominantly quantitative. Addressing this gap is important for designing tailored financial literacy education.

**Approach (summary):**
- Semi-structured individual interviews were conducted with 53 Pakistani, Indian, Nepalese, and Filipino participants aged 18 to 29 in Hong Kong.
- Participants were recruited through NGOs and university international offices using purposive sampling.
- Interview questions covered personal budgeting, spending, financial planning, use of financial products, debt management, and fraud detection.

**Key Findings (selected):**
- {'num': 'Many participants saved at least 30% of their monthly salary or pocket money.'}
- Participants used saving-centric or spending-centric budgeting approaches, aided by digital apps, parental monitoring, and mental bucketing.
- Spending was modest, with basic needs prioritized; strategies included deferred purchase, bargain shopping, and one-time lump-sum payments.
- Spending philosophies included differentiating needs from wants, using spending as work incentive, and YOLO enjoyment.

**Supports Odin (direct justifications):**
- Many young adults save at least 30% of monthly income, a benchmark for savings recommendations.
- Informal borrowing from family is common and often interest-free, reducing demand for formal credit products.
- Credit card users sometimes pay only the minimum due due to ignorance of interest charges.

**Limitations / Contradictions for Odin:**
- Sample was generally well-educated (half had bachelor's degree) and English-proficient, limiting generalizability to less educated or non-English-speaking ethnic minorities. [unacknowledged]
- Small qualitative sample size (n=53) does not allow broad generalization.
- Ethnic Chinese young adults were not included, preventing comparison.

**Key takeaways:**
- Many young adults saved at least 30% of monthly income.
- Family social capital strongly influences financial habits through monitoring and role modeling.
- Informal borrowing from family and friends is common and often interest-free.

---


## The Impact of AUP-CES Livelihood Initiatives, Leadership and Management in Buklod Bahayan
**Filename:** `L--Carpizo-et_al_summarized.md`  
**Authors:** Carpizo, E. M.; Balitar, J. E.; Balila, J. S. (2024)  
**ID:** `c5b2a8f0-3d4e-4a1b-9c6d-7e8f9a0b1c2d`  
**Odin Topics:** 13.A, 13.B  

**TLDR:** Community cooperatives provide economic benefits (dividends, loans, discounts), social benefits (camaraderie, security), and organizational benefits (leadership and accounting skills) from AUP-CES training.

**Problem & Motivation:** Poverty persists in the Philippines, limiting economic opportunities for marginalized communities. Community cooperatives offer alternative income sources but require effective leadership and management to succeed. The impact of structured training on cooperative sustainability remains underexplored.

**Approach (summary):**
- Qualitative study using Focus Group Discussions (FGDs) and individual interviews with cooperative members from Buklod Bahayan Subdivision.
- Three guiding questions were validated by research consultants and translated into Filipino for participant responses.
- Participants were selected based on availability and willingness; no random sampling was used.

**Key Findings (selected):**
- Members receive dividends on share investments, e.g., Php 5,580 on an initial Php 3,300 share.
- {'num': 'The cooperative grew from 5 to 20 members over ten years after reorganizing.'}
- Members access loans up to Php 10,000 payable within a year, providing emergency financial security.
- Social benefits include camaraderie, mutual help, and a sense of security during crises.

**Supports Odin (direct justifications):**
- Community cooperatives provide dividend returns on member shares (e.g., Php 5,580 on Php 3,300).
- Cooperative members gain financial security during emergencies through loan access.
- Leadership and management seminars equip members with accounting skills for cooperative sustainability.

**Limitations / Contradictions for Odin:**
- Small sample size from single community limits generalizability. [unacknowledged]
- Lack of control group for training impact prevents causal inference. [unacknowledged]
- Qualitative findings may be subject to recall bias. [unacknowledged]

**Key takeaways:**
- Member received Php 5,580 dividend on Php 3,300 share investment.
- Leadership training enabled cooperative to survive 10 years after initial failure.
- Cooperatives provide emergency loans and social support during crises.

---


## Scaling the Frame of Mind: Money Attitude and Financial Well-Being of Generation Zoomers (Gen-Zs) in Rizal Province
**Filename:** `L--Razalan_summarized.md`  
**Authors:** Razalan, D. (2024)  
**ID:** `f7c9e5d3-1a2b-4c3d-8e9f-0a1b2c3d4e5f`  
**Odin Topics:** 1.C, 5.A, 13.A, 13.B  

**TLDR:** Gen-Zs in Rizal Province show a great extent of positive money attitudes in power-prestige and retention-time dimensions, which significantly correlate with their financial well-being across autonomy, competence, and relatedness.

**Problem & Motivation:** Gen-Zs face unique financial challenges and low financial literacy, yet limited research examines their money attitudes and financial well-being in the Philippine education sector. Understanding these attitudes is crucial for developing targeted financial education.

**Approach (summary):**
- Mixed methods with quantitative survey of 364 Gen-Z teaching and non-teaching personnel from public and private schools in Rizal Province.
- Used Money Attitude Scale (MAS) measuring power-prestige, retention-time, distrust, anxiety and financial well-being based on Self-Determination Theory (autonomy, competence, relatedness).
- Qualitative interviews and focus group discussions to identify financial challenges and coping strategies.

**Key Findings (selected):**
- num: Significant positive correlation between overall money attitudes and overall financial well-being (r=0.679, p<0.05).
- num: Highest correlation observed between controlling finances (anxiety dimension) and competence (r=0.631).
- Gen-Zs exhibit great extent in power-prestige (spending and saving), retention-time (financial planning), and anxiety (financial protection and control).
- Gen-Zs show moderate extent in financial education (mean 3.35/5) and distrust dimensions (borrowing mean 3.21/5, donations mean 3.30/5).

**Supports Odin (direct justifications):**
- Positive money attitudes significantly correlate with higher financial well-being among Gen-Zs (r=0.679).
- Gen-Zs with strong financial planning attitudes exhibit greater financial competence and autonomy.
- Anxiety about financial protection is mitigated by awareness of scams and cybersecurity measures.

**Limitations / Contradictions for Odin:**
- Sample limited to education sector in one province, reducing generalizability [unacknowledged].
- No causal inference due to cross-sectional design.
- Potential self-report bias in financial attitude and well-being measures.

**Key takeaways:**
- Money attitudes correlate strongly with financial well-being (r=0.679).
- Gen-Zs prioritize paying bills on time and saving for specific goals.
- Financial education among Gen-Zs is only moderate in extent.

---


## THE IMPACT OF PSYCHOLOGICAL, ECONOMIC, SOCIAL ASPECTS, AND INTEREST RATE VARIATIONS ON WORKING MILLENNIALS' SAVING PATTERNS THROUGH DIGITAL BANKING
**Filename:** `L--Ataza-et_al_summarized.md`  
**Authors:** Ataza, C.; Porcel, M.; Resabal, L.; Sandoval, A.; Bragas, C. (2024)  
**ID:** `d1c9f8e7-6a5b-4c3d-2e1f-0a9b8c7d6e5f`  
**Odin Topics:** 1.C, 5.A, 13.A  

**TLDR:** Psychological aspects and interest rate variations positively affect working millennials' saving patterns through digital banking, while social aspects have a negative effect.

**Problem & Motivation:** Understanding the saving patterns of working millennials in the Philippines through digital banking is limited. Psychological, economic, social, and interest rate factors may interact in complex ways. This gap hinders banks from optimizing personalized offers and promoting financial literacy.

**Approach (summary):**
- Data collected from 51 working millennials aged 26-42 in Metro Manila with digital bank accounts.
- Questionnaire measured psychological, economic, social aspects and interest rate variations using 5-point Likert scale.
- Cronbach's alpha values ranged from 0.804 to 0.926 indicating good internal consistency.

**Key Findings (selected):**
- num: Psychological aspects had a positive effect on saving patterns (Beta=0.430, p<0.05).
- num: Interest rate variations showed the strongest positive effect (Beta=0.878, p<0.05).
- num: Social aspects had a negative effect (Beta=-0.182, p<0.05).
- num: The full model explained 75.34% of variance in saving patterns (R²=0.7534).

**Supports Odin (direct justifications):**
- Psychological aspects positively affect saving patterns of working millennials through digital banking.
- Interest rate variations are the strongest predictor of saving behavior in digital banking.
- Social aspects have a negative effect on saving patterns via digital banking.

**Limitations / Contradictions for Odin:**
- Potential sample bias due to purposive sampling.
- Dynamic nature of digital banking may affect future applicability.
- Sample size of 51 is relatively small [unacknowledged].

**Key takeaways:**
- Interest rate variations have the strongest positive effect on saving patterns (Beta=0.878).
- Psychological aspects positively influence saving behavior through digital banking.
- Social aspects negatively affect saving patterns, unlike psychological factors.

---


## EXPLORING TWO DECADES OF PERSONAL FINANCIAL PLANNING: A SYSTEMATIC LITERATURE REVIEW
**Filename:** `I--Pande-et_al_summarized.md`  
**Authors:** Pande, S.; Mazhar, S. S.; Khan, F. S.; Khan, B. A.; Haque, E.; Mir, M. A. (2024)  
**ID:** `10.55643/fcaptp.4.57.2024.4470`  
**Odin Topics:** 1.C, 4.A, 4.B, 13.A, 13.B  

**TLDR:** A systematic literature review of personal financial planning research from 2004 to 2024 reveals growing scholarly interest, prominent journals, diverse institutional contributions, and global geographic representation, with key themes including behavioral finance, digital tools, and financial literacy.

**Problem & Motivation:** Despite increased attention to personal financial planning after the 2008 financial crisis, no comprehensive systematic review has mapped trends and gaps over two decades. Understanding these patterns is crucial for policymakers, practitioners, and researchers to address financial insecurity and improve financial well-being.

**Approach (summary):**
- Conducted a systematic literature review following the PRISMA framework.
- Searched Scopus database using keywords 'Personal Financial Planning', 'Personal Wealth Management', 'Financial Wellness', or 'Personal Financial Management'.
- Included 158 documents published between 2004 and 2024 in English, covering subjects like Economics, Finance, Business, and Social Sciences.

**Key Findings (selected):**
- num: Publication volume grew from under 5 per year (2004-2009) to peaks in 2017, 2019, 2020, and 2023.
- The Journal of Financial Counselling and Planning contributed the most documents (17).
- Kansas State University produced the most publications (9), followed by Ohio State University (8).
- United States led with 62 publications, followed by India (19) and Malaysia (18).

**Supports Odin (direct justifications):**
- Increasing scholarly interest in personal financial planning since 2010 justifies Odin's market entry timing.
- Journal of Financial Counselling and Planning is a key source for financial behavior research.
- United States leads but India and Malaysia show growing output, suggesting Asian relevance.

**Limitations / Contradictions for Odin:**
- Search limited to Scopus database, may miss relevant publications. [unacknowledged]
- Potential bias in paper selection and interpretation acknowledged by authors.
- Findings may not generalize to all populations due to sample representation issues. [unacknowledged]

**Key takeaways:**
- Personal finance publications grew from under 5 to peaks after 2016.
- US leads research output, but India and Malaysia show strong growth.
- Behavioral finance and FinTech are dominant themes in recent literature.

---


## Robo-Advice: Transforming Households into Rational Economic Agents
**Filename:** `IA--D'Acunto-&-Rossi_summarized.md`  
**Authors:** D'Acunto, F.; Rossi, A.G. (2023)  
**ID:** `10.1146/annurev-financial-110921-013217`  
**Odin Topics:** 5.A, 13.A, 13.B, 10.B  

**TLDR:** Robo-advice reduces information frictions, corrects distorted beliefs, and lowers transaction costs to transform households into rational economic agents across consumption, saving, debt, and investment decisions.

**Problem & Motivation:** Households make suboptimal financial decisions due to limited information, systematic biases, and high transaction costs, leading to wealth inequalities and dampened policy effectiveness. Traditional human advice is expensive and not scalable, while nudges lack personalization. Robo-advice offers a third, scalable solution using big data and automation to align household choices with neoclassical benchmarks.

**Approach (summary):**
- Synthesizes research on household finance puzzles including suboptimal consumption, saving, investment, and debt choices.
- Defines robo-advice's three unique features: using big open data to inform households, managing beliefs toward rational expectations, and reducing monetary, cognitive, and psychological transaction costs.
- Reviews empirical studies on income aggregators (Olafsson & Pagel 2018), goal setting (Gargano & Rossi 2020), peer information (D'Acunto, Rossi & Weber 2019), and debt management (Chak et al. 2022).

**Key Findings (selected):**
- num: 95% of users linked all checking accounts, over 93% linked savings, and 91% linked credit cards to an income aggregator.
- num: Goal setting increased savings by €20 per month intention-to-treat and €60 per month local average treatment effect.
- num: Overspending messages cut daily spending by approximately 5% more for recipients.
- num: 41% of users with access to goal setting used it continuously.

**Supports Odin (direct justifications):**
- Goal setting via robo-advice increases savings by €60 per month for users with €1,200 average income.
- Providing aggregated balance sheet information reduces non-durable spending, especially on eating out and travel.
- Overspending messages cut daily spending by approximately 5% for recipients.

**Limitations / Contradictions for Odin:**
- Lack of long-term data on robo-advice effects beyond short time horizons.
- Potential for ostrich effect to reduce engagement over time, especially for vulnerable households.
- Algorithmic aversion may limit adoption and exacerbate inequalities.

**Key takeaways:**
- Robo-advice increases savings by €60 per month for low-income users via goal setting.
- Providing peer spending information reduces overspending by 5% more than control.
- Algorithmic aversion is the main predictor of robo-adoption, varying by age and wealth.

---


## Understanding financial professionals' perceptions of their clients' financial behaviors
**Filename:** `I--Morris-et_al_summarized.md`  
**Authors:** Morris, T.; Kamano, L.; Maillet, S. (2023)  
**ID:** `10.1108/IJBM-07-2022-0298`  
**Odin Topics:** 5.A, 13.A, 13.B  

**TLDR:** Financial professionals perceive clients' problematic financial behaviors as driven by psychological factors like instant gratification and bias, financial habits such as lack of discipline and planning, and system flexibility, especially in debt, savings, and investment decisions.

**Problem & Motivation:** Despite financial knowledge, many individuals exhibit suboptimal debt, savings, and investment behaviors that harm financial well-being. Prior research focuses on financial literacy but yields mixed results on intervention effectiveness. Understanding financial professionals' perspectives can reveal underlying behavioral drivers often missed by quantitative studies.

**Approach (summary):**
- Qualitative study with 26 semi-structured interviews of financial professionals in New Brunswick, Canada.
- Participants included loan managers, advisers, branch managers, accountants, and brokers from depository institutions, investment services, and insurance companies.
- Interviews covered clients' financial management, challenges, habits, and credit relationships, averaging 60 minutes.

**Key Findings (selected):**
- Professionals report clients abuse credit by maximizing limits and borrowing beyond needs, often driven by instant gratification and lack of budgeting.
- Clients insist on credit extensions even when advised against it, threatening to switch institutions, and some use multiple credit cards to circumvent limits.
- Many clients make only minimum credit card payments and fail to synchronize loan terms with asset life, leading to negative equity.
- Clients lack savings, start saving too late, and use revolving credit instead of emergency funds; only 10% save adequately for retirement.

**Supports Odin (direct justifications):**
- Financial professionals observe that clients abuse credit by maximizing limits beyond needs and borrowing for non-asset purchases.
- Many clients make only minimum credit card payments, increasing long-term debt costs and delaying repayment.
- Lack of savings habit and starting late lead to financial insecurity and reliance on credit for emergencies.

**Limitations / Contradictions for Odin:**
- Did not obtain opinions of clients, only professionals' perceptions. [unacknowledged]
- Professionals from different positions (e.g., loan managers vs. investment advisers) may have divergent perspectives due to different clientele.
- Qualitative methodology does not allow generalization of results.

**Key takeaways:**
- Psychological factors like instant gratification drive poor financial behaviors.
- Financial habits such as lack of discipline matter more than knowledge for debt and savings.
- num: Only 10% of clients save adequately for retirement per professionals.

---


## Passionate Online Shoppers
**Filename:** `L--Pagobo-et_al_summarized.md`  
**Authors:** Pagobo, M. C. P.; Sumicad, R. P.; Arciete, D. C.; Salve, J. D.; Marabiles, K.; Rivera, C. (2023)  
**ID:** `10.32996/ijaas.2023.2.2.1`  
**Odin Topics:** 1.C, 13.A, 13.B  

**TLDR:** Online shopping addiction among Filipino college students is driven by psychological, marketing, social, and convenience factors, leading to overspending, financial problems, and distraction, with self-assessment, budgeting, and app uninstallation as coping mechanisms.

**Problem & Motivation:** The rapid growth of e-commerce and promotional offers have increased online shopping addiction, yet research on passionate online shoppers' experiences, challenges, and coping strategies among Filipino college students remains limited. Understanding these factors is important for addressing financial and psychological consequences.

**Approach (summary):**
- Qualitative phenomenological study with 16 Filipino college students from University of Cebu Main Campus.
- Participants screened using Bergen Shopping Addiction Scale (BSAS) to identify passionate online shoppers.
- Semi-structured open-ended interviews conducted face-to-face after obtaining informed consent.

**Key Findings (selected):**
- Four influencing factor themes: psychological (motivation, attitude, positive emotions, perception, escape), marketing (appearance, promotional offers), social (family, friends), and convenience.
- Three challenge themes: overspending, financial problems (including debt and borrowing), and distraction from duties.
- Three coping mechanism themes: self-assessment (checking emotions and deservingness), budgeting (separating money for shopping vs savings), and temporarily uninstalling shopping apps.
- Participants experienced regret, worry, and stress after online purchases, consistent with prior research.

**Supports Odin (direct justifications):**
- Psychological factors like positive emotions and escape from stress drive online spending among Filipino young adults.
- Promotional offers (discounts, free shipping) trigger impulse purchases and overspending.
- Passionate online shoppers experience financial problems including borrowing money to pay for orders.

**Limitations / Contradictions for Odin:**
- Small sample size (16 participants) from one university limits generalizability. [unacknowledged]
- Qualitative design without quantitative validation of coping effectiveness. [unacknowledged]
- Contradictory statement about gender focus: claims both genders but conclusion says exclusively female. [acknowledged in paper as limitation]

**Key takeaways:**
- Promotional offers triple daily shopping frequency among passionate online shoppers.
- Sixteen Filipino college students reported overspending and debt from online shopping addiction.
- Self-assessment before purchasing reduces impulsive online spending.

---


## Financial literacy in the digital age — A research agenda
**Filename:** `I--Koskelainen-et_al_summarized.md`  
**Authors:** Koskelainen, T.; Kalmi, P.; Scornavacca, E.; Vartiainen, T. (2023)  
**ID:** `10.1111/joca.12510`  
**Odin Topics:** 5.A, 10.A, 10.B, 13.A, 13.B  

**TLDR:** Digitalization transforms financial services and consumer behavior, requiring updated financial literacy to address new risks like data privacy and digital nudging.

**Problem & Motivation:** Digital finance offers convenience but also risks that traditional financial literacy does not cover. There is limited understanding of how digitalization affects financial literacy and capability. This gap motivated a systematic review to propose a research agenda.

**Approach (summary):**
- Applied an integrative literature review to explore how digitalization affects financial literacy and capability.
- Searched ProQuest, EBSCO, ACM Digital Library, and Google Scholar using terms like “financial literacy” AND “digital”.
- Initial screening of 603 papers, narrowed to 29 peer-reviewed papers after excluding off-topic or analog-only studies.

**Key Findings (selected):**
- {'“num': '80% of millennial smartphone owners use their device for transactional financial purposes.”'}
- Smartphone apps that track spending and compare loan interest improve financial resilience after shocks.
- Digital nudging via mobile apps can increase salience of credit card transactions and reduce spending.
- Financial literacy helps mitigate the effect of mobile payment use on account overdrafts.

**Supports Odin (direct justifications):**
- Digital payment methods increase spending due to loss of tangibility compared to cash.
- Smartphone apps that compare loan interest and track spending improve financial resilience.
- Digital nudging can reduce credit card spending by increasing transaction salience.

**Limitations / Contradictions for Odin:**
- Only peer-reviewed journal articles from finance, economics, and IS disciplines were included.
- Conference proceedings, which may contain emerging technologies, were excluded. [unacknowledged]
- The review may miss newer digital finance developments published after 2020.

**Key takeaways:**
- 80% of millennials use smartphones for transactional financial tasks.
- Digital nudging can reduce credit card spending through salience.
- Loss of cash tangibility increases spending in digital payments.

---


## Financial Literacy and Financial Well-Being of Nurses of a First-Class Province in the Philippines
**Filename:** `L--Gerzon-et_al_summarized.md`  
**Authors:** Gerzon, R. A.; Lopena, G. L. (2023)  
**ID:** `10.52006/main.v6i2.752`  
**Odin Topics:** 1.C, 5.A, 7.A, 13.A, 13.B  

**TLDR:** Financial literacy of public health nurses in a Philippine province is high, and financial well-being is great, with a strong positive correlation between them.

**Problem & Motivation:** Filipino nurses face low pay and financial stress, yet little is known about their financial literacy and well-being. Understanding these factors is crucial for improving their financial health and work performance. This study addresses the gap by assessing literacy and well-being among public health nurses.

**Approach (summary):**
- Data from 178 randomly stratified public health nurses in a first-class Philippine province.
- Descriptive-correlational design using a researcher-made 52-item questionnaire with four-point Likert scale.
- Financial literacy measured via financial knowledge and behavior; financial well-being via discipline, security, and resiliency.

**Key Findings (selected):**
- num: Overall financial literacy was high (M=3.22, SD=0.39) and financial well-being great (M=3.03, SD=0.46).
- num: Monthly income significantly correlated with financial literacy (r=0.223, p=0.003).
- num: Strong positive correlation between financial literacy and financial well-being (rs=0.660, p=0.000).
- Age, sex, civil status, and number of dependents showed no significant relationship with financial literacy or well-being.

**Supports Odin (direct justifications):**
- Financial literacy and financial well-being are strongly correlated among Filipino public health nurses (rs=0.660).
- Monthly income is a significant predictor of financial literacy in this population (r=0.223).
- Demographic factors like age, sex, and marital status do not significantly affect financial literacy among Filipino nurses.

**Limitations / Contradictions for Odin:**
- Sample size is limited (n=178) and restricted to one province.
- Only nurses were surveyed; results may not generalize to other Filipino young professionals.
- Quantitative design limits depth of insight into financial behaviors.

**Key takeaways:**
- Higher monthly income is linked to better financial literacy among nurses.
- Financial literacy strongly predicts financial well-being (rs=0.66).
- Nurses show great financial discipline but lower financial resilience (M=2.88).

---


## Consumer Finance Survey 2021
**Filename:** `L--Bangko_Sentral_ng_Pilipinas-2021_summarized.md`  
**Authors:** Bangko Sentral ng Pilipinas (2021)  
**ID:** `f47ac10b-58cc-4372-a567-0e02b2c3d479`  
**Odin Topics:** 1.A, 1.B, 1.C, 2.A, 2.C, 3.A, 4.A, 4.B, 5.A, 10.B, 13.A, 13.B  

**TLDR:** The 2021 Consumer Finance Survey by the Bangko Sentral ng Pilipinas provides comprehensive data on income, expenditure, assets, liabilities, and demographics of Filipino households, revealing trends in financial inclusion, digital adoption, and debt during the COVID-19 pandemic.

**Problem & Motivation:** There were significant data gaps on household wealth and indebtedness in the Philippines, as existing surveys like FIES and APIS had limited coverage of assets and liabilities. Collecting detailed financial condition data was necessary to inform evidence-based socio-economic policies and monetary decisions. The survey aimed to provide a comprehensive picture of household balance sheets, income sources, spending patterns, and demographic characteristics.

**Approach (summary):**
- Sample of 18,000 households drawn from PSA's 2013 Master Sample (two-stage cluster sampling) covering all regions including BARMM.
- Face-to-face interviews using structured CAPI questionnaire, translated into six major languages, conducted from March to December 2022.
- Reference period for income and expenditure was calendar year 2021; assets and liabilities as of interview date.

**Key Findings (selected):**
- num: 91.5% of households had wage income in 2021, up from 73.7% in 2018.
- num: Only 29.3% of households carried any debt, down from 40.4% in 2018.
- num: 35.3% owned deposit accounts, significantly up from 9.7% in 2018.
- num: 24.3% owned electronic money accounts, up from 0.3% in 2018.

**Supports Odin (direct justifications):**
- Filipino households spend 55.4% of their budget on food at home.
- Only 35.3% of households have a formal deposit account.
- E-money account ownership reached 24.3% during the pandemic.

**Limitations / Contradictions for Odin:**
- Estimates with coefficients of variation above 20 percent should be interpreted with caution.
- Recall bias may affect income and expenditure values reported for the previous year.
- Non-sampling errors from intentional under-reporting of assets and liabilities. [unacknowledged]

**Key takeaways:**
- Wage income source increased to 91.5% of households during the pandemic.
- Debt prevalence dropped to 29.3% as households reduced borrowing.
- Digital financial assets grew rapidly: e-money accounts up to 24.3%.

---


## AI Wealth Navigator: An Integrated Platform for Smart Budgeting, Financial Learning, and Personalized Policy Guidance
**Filename:** `IA--Yadav-et_al_summarized.md`  
**Authors:** Yadav, A.; Prakash, R. S.; Iqubal, S. M.; Gebremicahea, M. G. (0)  
**ID:** `f5c8d3e6-9a4b-4c7d-8e2f-1a3b5c7d9e0f`  
**Odin Topics:** 3.A, 3.B, 7.B, 7.C, 9.A, 9.B, 10.A, 10.B, 11.A, 11.B, 13.A  

**TLDR:** AI Wealth Navigator integrates adaptive financial learning, AI-driven budget tracking with receipt scanning, and personalized government policy recommendations using LLMs into a single platform.

**Problem & Motivation:** Personal finance apps remain fragmented, separating budgeting, education, and policy navigation. Users lack cohesive tools to maximize financial well-being, especially in regions with low financial literacy like India. Existing solutions fail to provide personalized, integrated guidance across all three domains.

**Approach (summary):**
- Built a web platform using Next.js, Supabase, Prisma, Inngest, and Arcjet for secure, scalable performance.
- Integrated Gemini LLM for personalized financial recommendations and adaptive learning roadmaps based on user literacy and progress.
- Developed an AI-powered budget tracker with receipt OCR (94% accuracy) and real-time visual insights.

**Key Findings (selected):**
- num: Receipt scanner achieved 94% accuracy on digital and physical receipts.
- num: Over 70% of users discovered previously unknown government programs tailored to their profiles.
- User ratings: budgeting insights 4.8/5, policy recommendations 4.7/5, learning roadmap 4.6/5.
- Arcjet blocked all simulated security threats, ensuring data protection.

**Supports Odin (direct justifications):**
- Receipt scanning with AI achieves 94% accuracy, reducing manual entry errors.
- Personalized policy recommendations increase user discovery of relevant government schemes by over 70%.
- Integrating financial learning, budgeting, and policy guidance into one platform reduces fragmentation.

**Limitations / Contradictions for Odin:**
- Small sample size (50 users) for human evaluation, limiting generalizability.
- No longitudinal study to measure retention or sustained behavior change.
- Reliance on full user profiles for policy matching may raise privacy concerns (acknowledged as minor drawback by authors).

**Key takeaways:**
- Receipt OCR achieved 94% accuracy on digital and physical receipts.
- Over 70% of users found new government schemes via policy engine.
- Unified platform integrates budgeting, learning, and policy recommendations.

---


## A Descriptive-Correlational Analysis of Social Media Usage and Personal Finance Competencies Among University Students
**Filename:** `L--Cadayunan-et_al_summarized.md`  
**Authors:** Cadayunan, A. M. G.; Fabe, A. C. M.; Tingabngab, G. T.; Bagtong, S. M. D. (0)  
**ID:** `7c9e6679-7425-40de-944b-e07fc1f90ae7`  
**Odin Topics:** 1.A, 1.C, 2.C, 5.A, 13.A, 13.B  

**TLDR:** High social media use correlates moderately with financial literacy and decision-making among Filipino university students, but a knowledge-action gap persists.

**Problem & Motivation:** Social media's influence on financial competencies among Filipino university students is understudied. While digital platforms can disseminate financial information, they also introduce behavioral risks. This gap hinders efforts to promote practical financial literacy within university settings.

**Approach (summary):**
- Descriptive-correlational design with stratified random sampling of 173 BSBA students from Bukidnon State University Talisayan Campus.
- Survey measured social media usage (platforms, frequency) and personal finance competencies (financial literacy and decision-making abilities).
- Pearson correlation coefficient and two-tailed significance test used to analyze relationships.

**Key Findings (selected):**
- Social media usage is high, with Facebook and TikTok as most preferred platforms.
- Financial literacy reported as high, but practical application (budget adherence, regular saving) is lower.
- Decision-making abilities rated as moderate, with difficulty resisting impulse purchases.
- {'num': 'Moderate positive correlation between social media frequency and financial literacy (r=0.359, p<0.001).'}

**Supports Odin (direct justifications):**
- Social media frequency is positively associated with self-reported financial literacy (r=0.359).
- Students with high financial literacy still struggle with budget adherence and regular saving.
- Difficulty resisting impulse purchases is a significant barrier to sound financial decision-making.

**Limitations / Contradictions for Odin:**
- Correlational design prevents causal inference.
- Self-reported financial literacy may not reflect objective competence.
- Sample limited to business students at one campus, not representative of all Filipino young professionals.

**Key takeaways:**
- Social media use correlates moderately with financial literacy (r=0.359).
- High knowledge does not guarantee good financial behavior.
- Impulse buying is a major barrier to sound decisions.

---


## 📌 Note for the Agent

The summaries above contain **essential extracts** – enough to understand the paper's relevance to Odin, including supporting evidence and limitations.
If you need additional details not shown here (e.g., **critical citations, definitions, equations, full methodology, or the complete mapping rationale**),
**ask the user to send the original summary file (`<filename>_summarized.md`) or the converted MarkItDown file(`<filename>_marked.md`)** for the specific paper(s) of interest.
Do not invent missing information. Acknowledge gaps when they exist.