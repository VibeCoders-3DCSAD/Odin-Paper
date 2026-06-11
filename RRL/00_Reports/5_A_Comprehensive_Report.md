# Comprehensive Report for Subtopic: `5.A`

**Total files:** 73

This report includes problem/motivation, approach, key findings, support for Odin, and limitations/contradictions.

---


## Digital Finance Usage and Its Impact on Consumer Economic Behavior Based on National Data
**Filename:** `I--Askhiyah_summarized.md`  
**Authors:** Askhiyah, U. M. (2026)  
**ID:** `10.59784/journaljoae.v1i1.37`  
**Odin Topics:** 1.C, 5.A, 7.A, 13.A, 13.B  

**TLDR:** Digital finance adoption increases household consumption by 8.7% and financial literacy by 1.4 points but reduces savings balances by 5.8% and raises debt-to-income ratios, with heterogeneous effects by age and income.

**Problem & Motivation:** The comprehensive impact of digital finance on consumer economic behavior remains inadequately understood despite widespread adoption. Existing research produces mixed findings on whether digital finance promotes prudent behavior or encourages overconsumption and overindebtedness. Robust causal evidence using nationally representative data is needed to inform policy and mitigate risks for vulnerable populations.

**Approach (summary):**
- Data from 45,678 households in a national survey with stratified random sampling.
- Propensity score matching with kernel and radius algorithms to control selection bias.
- Instrumental variable estimation using regional digital infrastructure density as instrument.

**Key Findings (selected):**
- "num: Digital finance users show 8.7% higher consumption expenditure (ATT=742k Rupiah, p<0.001)."
- "num: Savings balances are 5.8% lower for digital finance users despite higher formal savings account ownership."
- "num: Financial literacy scores increase by 1.4 points (on 10-point scale) post-adoption."
- "num: Debt-to-income ratio is 6.4 percentage points higher for digital finance users (34.7% vs 28.3%)."

**Limitations / Contradictions for Odin:**
- "Cross-sectional and short-term panel data (max 24 months) cannot assess long-term wealth effects. [unacknowledged]"
- Self-reported survey data may introduce recall and social desirability bias.
- No direct measurement of impulse spending or self-control mechanisms.

**Key takeaways:**
- Digital finance increases consumption by 8.7% but reduces savings by 5.8%.
- Financial literacy improves by 1.4 points after digital finance adoption.
- Young lower-middle-income users face highest debt and late payment risks.

---


## FINANCIAL HARDSHIPS OF TRICENARIANS EDUCATORS: PREPARING FOR THE FUTURE AMID DEBT CHALLENGES
**Filename:** `L--Navarro-&-Bantulo_summarized.md`  
**Authors:** Navarro, R.; Bantulo, J. (2026)  
**ID:** `10.46827/ejes.v13i5.6659`  
**Odin Topics:** 1.C, 2.A, 5.A, 7.A, 13.A, 13.B  

**TLDR:** Tricenarian Filipino educators face financial strain, mental burden, work disruption, and postponed aspirations, coping through budgeting, emotional outlets, and debt while developing financial discipline and career focus.

**Problem & Motivation:** No localized research exists on how tricenarian educators in Kiamba 1 District manage debt while preparing for future stability. Financial hardship affects teacher well-being, job performance, and retention. The study aims to document lived experiences to inform support mechanisms and policy.

**Approach (summary):**
- Qualitative single case study at Platon Esperanza Taguding Elementary School in Philippines.
- Five purposively selected educators aged 30-39 with 8-15 years teaching experience.
- Semi-structured interviews audio-recorded and transcribed.

**Key Findings (selected):**
- Major challenges: financial strain, mental burden, work distraction, missed career opportunities, emotional distress, postponed aspirations, persistent debt pressure.
- Coping mechanisms include financial planning, controlled spending, emotional release, incurring debt, social support, personal outlets, saving extra income, self-care, budget monitoring.
- Insights: empowered financial decisions, financial growth, aspiring for excellence, thinking before spending, career motivation, long-term planning, debt awareness.

**Limitations / Contradictions for Odin:**
- Small sample size (n=5) limits generalizability.
- Single school setting may not represent all tricenarian educators.
- Self-reported data subject to recall and social desirability bias [unacknowledged].

**Key takeaways:**
- Tricenarian educators use envelope budgeting and expense tracking to cope.
- Debt is both a burden and a survival strategy for Filipino teachers.
- Financial discipline and career focus emerge from hardship.

---


## AI-Driven Personal Finance Management: Predictive Expense Forecasting and Behavioural Clustering
**Filename:** `IA--Vinitha-et_al_summarized.md`  
**Authors:** Vinitha, C.; Krishna, A.H.; Reddy, E.M.; Javari, P. (2026)  
**ID:** `2c3d4e5f-6a7b-8c9d-0e1f-2a3b4c5d6e7f`  
**Odin Topics:** 3.A, 5.A, 5.C, 6.A, 6.B, 7.B, 7.C  

**TLDR:** Combines LSTM for expense forecasting and K-Means for spending behavior clustering with VADER sentiment analysis, achieving 99.93% prediction accuracy.

**Problem & Motivation:** Manual financial tracking is complex, time-consuming, and error-prone. Traditional tools store transactions but lack advanced analytics for future expense prediction. Users struggle to interpret spending patterns and link qualitative feelings to quantitative data.

**Approach (summary):**
- System built with Django, MySQL, and OTP authentication via SMTP for secure access.
- LSTM model with MSE loss and Adam optimizer trained on historical daily expenses over 1000 epochs.
- K-Means clustering groups expenses by category and amount to reveal spending patterns.

**Key Findings (selected):**
- "num: LSTM achieved 99.93% accuracy and MSE of 35.41 on expense prediction."
- K-Means clustering visualizes distinct spending behavior patterns across expense categories.
- Budget recommendation suggests investment amounts from predicted surplus (e.g., 8,661 units surplus).
- VADER sentiment analysis enables continuous system improvement based on user feedback.

**Limitations / Contradictions for Odin:**
- "Evaluation uses only accuracy and MSE; no real-world user study or longitudinal validation. [unacknowledged]"
- "Potential overfitting of LSTM with 1000 epochs on small dataset not discussed. [unacknowledged]"
- "No baseline comparison to traditional statistical methods (e.g., ARIMA). [unacknowledged]"

**Key takeaways:**
- "LSTM predicts daily expenses with 99.93% accuracy."
- "K-Means reveals hidden spending patterns from transaction data."
- "Budget recommendation uses predicted surplus for investment advice."

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
- num: Random Forest expense classifier achieved 93-96% accuracy, outperforming rule-based systems (75-80%).
- num: LSTM forecasting produced a Mean Absolute Error of 4.7% for monthly expenditure prediction.
- num: Isolation Forest anomaly detection achieved 92% precision.
- num: 84% of users reported better spending awareness and 78% claimed increased savings control after one month.

**Limitations / Contradictions for Odin:**
- Usability study limited to 50 participants, may not generalize. [unacknowledged]
- Long-term retention and engagement not evaluated. [unacknowledged]
- Data privacy and security not experimentally validated. [unacknowledged]

**Key takeaways:**
- Random Forest categorizes expenses with 93-96% accuracy.
- LSTM forecasts monthly spending with 4.7% MAE.
- 84% of users report better spending awareness after using the system.

---


## Beyond Awareness: Examining Financial Behaviors Among Public School Teachers in the Philippines
**Filename:** `L--Am-una_summarized.md`  
**Authors:** Am-una, A. (2026)  
**ID:** `10.69569/jip.2026.065`  
**Odin Topics:** 1.C, 2.A, 5.A, 7.A, 13.A, 13.B  

**TLDR:** Public school teachers in Baguio exhibit moderately positive financial behaviors driven by conscious constraint under limited income and heavy debt, with budgeting most difficult despite frequent practice.

**Problem & Motivation:** A knowledge-action gap persists in understanding how financial knowledge translates into everyday behavior, especially under economic constraint. Public school teachers have stable employment but face escalating financial pressures and debt, yet existing studies focus on knowledge rather than behavioral enactment and perceived difficulty. Understanding this gap is critical because teachers serve as financial role models for learners.

**Approach (summary):**
- Explanatory sequential mixed-methods design with quantitative survey (N=335) followed by semi-structured interviews (N=9).
- Participants were regular public school teachers in Baguio City, Philippines, with at least one year of experience.
- Survey measured frequency of financial behaviors (4-point Likert) and perceived difficulty across five domains: budgeting, saving, goals, making ends meet, and choosing products.

**Key Findings (selected):**
- "num: General weighted mean for financial behaviors was 2.69 (moderately positive), with making ends meet highest (M=2.90) and active saving lowest (M=2.43)."
- "num: No significant difference in financial behaviors between teachers who attended financial literacy seminars and those who did not (p=.991)."
- "num: Married teachers had significantly lower financial behavior scores than single teachers (p=.034)."
- "num: Master Teachers scored higher (M=3.00) than non-Master Teachers (M=2.65, p=.002)."

**Limitations / Contradictions for Odin:**
- "Sample limited to one city (Baguio), not representative of all Philippine public school teachers. [unacknowledged]"
- "Cross-sectional design prevents causal inference about seminar attendance or marital status effects. [unacknowledged]"
- "Self-reported financial behavior data may overestimate positive practices due to social desirability. [unacknowledged]"

**Key takeaways:**
- "num: Seminar attendance had zero effect on financial behavior scores (p=.991)."
- "Conscious constraint explains moderate behaviors as endurance, not mastery."
- "Budgeting is most difficult due to scarce resources, not skill deficit."

---


## The plight of teachers on the twice-a-month salary release: Financial literacy and survival
**Filename:** `L--Amado_summarized.md`  
**Authors:** Amado, M. A. (2026)  
**ID:** `10.63498/ijabms2`  
**Odin Topics:** 2.A, 5.A, 7.A, 13.A, 13.B  

**TLDR:** Teachers receiving twice-a-month salaries report improved short-term planning and perceived stability, yet financial stress persists; financial literacy significantly influences their survival strategies and management practices.

**Problem & Motivation:** Literature documents teacher financial difficulties but lacks analysis of how bi-monthly salary cycles structurally determine survival behaviors. Financial literacy is often treated as static, ignoring that mid-month liquidity constraints make conventional budgeting inaccessible. This study addresses the inter-payday period as a stressor dictating resource management.

**Approach (summary):**
- Used descriptive survey design with 115 teachers from Claveria North District (SY 2023–2024).
- Employed validated 5-point Likert scale questionnaire measuring financial well-being, literacy, management, and coping strategies (Cronbach’s α = 0.88).
- Analyzed data using weighted mean and percentage distribution to quantify financial behaviors and perceptions.

**Key Findings (selected):**
- num: Overall perceived impact of twice-a-month salary on well-being was 4.18 (Agree on 5-point scale).
- num: Financial literacy positively influenced financial management under the system (overall mean 4.21).
- Teachers prioritize essential expenses (mean 4.46) and budget strictly (mean 4.32) between pay periods.
- num: Despite advantages (overall 4.23), teachers experience financial stress (mean 3.63) and challenges covering first-half expenses (mean 3.65).

**Limitations / Contradictions for Odin:**
- Cross-sectional design limits causal inference [unacknowledged].
- Sample limited to one district, reducing generalizability [unacknowledged].
- Reliance on self-reported Likert scales may introduce social desirability bias [unacknowledged].

**Key takeaways:**
- Twice-a-month salary release yields perceived stability (4.18 mean) but not stress elimination.
- Financial literacy strongly predicts better handling of unexpected expenses (4.37 mean).
- Teachers employ strict budgeting (4.46) and supplementary income to survive pay gaps.

---


## A Systematic Literature Review: Present Bias versus Financial Literacy as Determinants of Savings Behavior Among Entrepreneurs
**Filename:** `L--Aquino-et_al_summarized.md`  
**Authors:** Aquino, E. J.; Sealmoy, R.; Mandap, O. (2026)  
**ID:** `10.69569/jip.2025.758`  
**Odin Topics:** 5.A, 7.A, 13.A  

**TLDR:** Present bias consistently predicts poor savings behavior among entrepreneurs, while financial literacy’s impact is conditional on self-control.

**Problem & Motivation:** The gap between financial knowledge and actual savings behavior among entrepreneurs is persistent and puzzling. Prior research has not systematically compared the relative influence of financial literacy versus present bias on entrepreneurial savings. This review addresses that gap to inform more effective interventions.

**Approach (summary):**
- A systematic literature review following PRISMA 2020 guidelines.
- Searches conducted in Google Scholar, Scopus, and Web of Science with Boolean keywords.
- Inclusion criteria: peer-reviewed articles in English (2020–2025), Journal Impact Factor ≥1.5, focused on entrepreneurs or SME owners.

**Key Findings (selected):**
- num: Financial literacy’s impact on savings is conditional and often negligible without self-control (Mpaata et al., 2021).
- num: Present bias consistently leads to impulsive spending and reduced savings, even among financially literate individuals.
- Behavioral factors frequently override financial knowledge in shaping entrepreneurial savings.
- num: 78% of reviewed studies used primary data, mostly cross-sectional surveys in Asian contexts.

**Limitations / Contradictions for Odin:**
- The review only includes English-language articles, potentially missing relevant non-English research. [unacknowledged]
- Most primary studies are cross-sectional and focused on Asia, limiting causality and generalizability. [acknowledged]
- The minimum Journal Impact Factor of 1.5 may exclude methodologically sound studies with lower impact. [unacknowledged]

**Key takeaways:**
- Present bias is a stronger savings predictor than financial literacy for entrepreneurs.
- Financial literacy requires high self-control to improve savings.
- 78% of reviewed studies used primary survey data.

---


## Financial Education in the Age of Artificial Intelligence: A Systematic Review with Text Mining and Natural Language Processing
**Filename:** `IA--Balcazar-Paiva-et_al_summarized.md`  
**Authors:** Balcazar-Paiva, E. S.; Haro-Sarango, A. F.; Villanueva-Calderón, J. A. (2026)  
**ID:** `10.3390/ijfs14030076`  
**Odin Topics:** 4.A, 4.B, 5.A, 10.A, 10.B, 11.A, 12.A  

**TLDR:** AI integration in financial education enables personalization and virtual tutoring but lacks longitudinal evidence and standardized metrics, with ethical concerns over privacy and bias.

**Problem & Motivation:** The convergence of AI and financial education lacks integrative synthesis despite rapid growth. Existing literature is fragmented without unifying frameworks articulating pedagogical principles with technical capabilities. Ethical and social implications remain underexplored, especially in vulnerable settings.

**Approach (summary):**
- Systematic review following PRISMA 2020 guidelines.
- Searched Scopus, ScienceDirect, and Taylor & Francis (388 initial records, 50 included).
- Combined bibliometric mapping (VOSviewer) with NLP sentiment analysis.

**Key Findings (selected):**
- "num: 388 initial records reduced to 50 included studies."
- AI acts as central organizing axis connecting education, finance, and health.
- "num: Sentiment analysis shows predominantly neutral technical tone with slight positive tilt (sentiment_index mean 0.049)."
- Longer abstracts correlate with more methodological caution and negativity.

**Limitations / Contradictions for Odin:**
- "Search restricted to three databases, missing gray literature and manual reference searching [acknowledged]."
- "Sentiment analysis tools (VADER, TextBlob) less reliable in Spanish [acknowledged]."
- "Lack of standardized metrics across studies prevents meta-analysis [acknowledged]."

**Key takeaways:**
- "AI in financial education shows neutral technical tone with slight optimism."
- "Longer abstracts include more caution about ethics and risks."
- "Sentiment_index mean 0.049 indicates mild positive framing."

---


## Predictors of Investment Decision among Selected Individuals in Key Cities of Laguna: An Extended Theory of Planned Behavior Approach
**Filename:** `L--Lantin-Magana-et_al_summarized.md`  
**Authors:** Lantin-Magana, L.; Espelita, C. A. M. H.; Calingasan-Habana, C. A.; Atento, A. G. B.; Atento, R. G. O. (2026)  
**ID:** `b9c7a3d4-5e6f-4a7b-8c9d-0e1f2a3b4c5d`  
**Odin Topics:** 5.A  

**TLDR:** Investment decision among individuals in Laguna cities is associated with capital market knowledge and attitude toward investment, with attitude and monthly salary explaining 16.2% of variance.

**Problem & Motivation:** Investment participation in the Philippines remains limited, and decisions to invest are shaped not only by financial capacity but also by evaluative beliefs, risk appraisal, institutional trust, and perceived readiness. An exclusive focus on financial capacity is insufficient for explaining observed differences in investment participation and decision patterns.

**Approach (summary):**
- A descriptive, cross-sectional online survey was administered to 483 respondents from Calamba, Santa Rosa, and Biñan, Laguna.
- Constructs measured risk tolerance, attitude toward capital markets, capital market knowledge (financial literacy), government trust, attitude toward investment, and self-reported investment decision using a six-point scale.
- Descriptive statistics, independent t-tests, ANOVA, Pearson correlations, and stepwise multiple regression were used for analysis.

**Key Findings (selected):**
- num: Attitude toward investment (coefficient 0.345) and monthly salary (0.368) were significant predictors in stepwise regression, with R² = 0.162, p < .001.
- num: Investment decision differed significantly by sex (p = .002) and monthly salary bracket (p < .001).
- num: Capital market knowledge showed the highest correlation with investment decision (r = 0.210, p = .001), followed by attitude toward investment (r = 0.179, p = .003).
- Risk tolerance received the highest mean rating (M = 4.81, SD = 1.19), while government trust received the lowest (M = 3.85, SD = 1.33).

**Limitations / Contradictions for Odin:**
- Cross-sectional design cannot establish causality.
- Purposive and online sampling via Google Forms may exclude individuals with limited digital access. [unacknowledged]
- Self-reported ratings may be influenced by social desirability or response styles.

**Key takeaways:**
- Attitude and salary explain 16.2% of investment decision variance.
- Risk tolerance rated highest (4.81/6), government trust lowest (3.85/6).
- Male respondents had higher investment decision scores than females.

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

**Limitations / Contradictions for Odin:**
- Small sample size of 100 respondents limits generalizability. [unacknowledged]
- Convenience sampling may introduce selection bias. [unacknowledged]
- Sample predominantly consists of students aged 18-23, not representative of all consumers. [unacknowledged]

**Key takeaways:**
- Subscription culture increases recurring spending and budgeting challenges.
- Auto-renewal systems often cause unexpected charges for consumers.
- Young consumers frequently underestimate cumulative subscription costs.

---


## Understanding Millennials' Financial Behavior: The Role of Fintech Adoption, Financial Literacy, and the Mediating Effect of Financial Attitudes in a Crisis-Affected Emerging Economy
**Filename:** `I--Aoun-et_al_summarized.md`  
**Authors:** Aoun, D.; Rahal, R.; Sfeir, L.; AlMaalouf, N. J. (2026)  
**ID:** `10.3390/ijfs14020035`  
**Odin Topics:** 1.C, 5.A, 7.A, 13.A, 13.B  

**TLDR:** Fintech adoption and financial literacy positively influence Lebanese millennials' financial behavior, with financial attitude mediating the literacy-behavior relationship.

**Problem & Motivation:** In crisis-affected emerging economies like Lebanon, traditional financial guidance and institutional support are limited, yet no integrated model examines how FinTech adoption, financial literacy, and financial attitudes jointly shape millennial financial behavior. The persistence of low financial literacy and fragmented FinTech regulation creates an empirical gap in understanding behavioral finance under extreme economic instability.

**Approach (summary):**
- A quantitative survey collected data from 390 Lebanese millennials using a structured questionnaire with five-point Likert scales.
- FinTech adoption (5 items), financial literacy (4 items), financial attitude (4 items), and financial behavior (5 items) were measured using adapted scales.
- Structural equation modeling (SEM) was applied to test direct and mediating effects after confirming validity via KMO, AVE, HTMT, and reliability coefficients.

**Key Findings (selected):**
- "num: Financial literacy has a positive direct effect on financial behavior (β=0.337, p<0.001)."
- "num: FinTech adoption has a positive direct effect on financial behavior (β=0.144, p<0.001)."
- "num: Financial attitude is the strongest predictor of financial behavior (β=0.414, p<0.001)."
- Financial attitude fully mediates the relationship between financial literacy and financial behavior.

**Limitations / Contradictions for Odin:**
- "Cross-sectional design prevents causal inference and temporal tracking of financial behavior change."
- "Self-reported survey data may inflate associations due to common method bias and social desirability."
- "Sample is limited to Lebanese millennials, restricting generalizability to other populations."

**Key takeaways:**
- "Financial attitude mediates the literacy-behavior link."
- "Financial literacy's direct effect on behavior is β=0.337."
- "FinTech adoption has a smaller but significant effect at β=0.144."

---


## The Role of Financial Literacy in Supporting Employee Work-Life Balance
**Filename:** `L--Bancoro-et_al_summarized.md`  
**Authors:** Bancoro, J. C. M.; Barillo, R. M. L.; Buhian, D. L. C. (2025)  
**ID:** `10.69569/jip.2025.015`  
**Odin Topics:** 1.C, 5.A, 13.A  

**TLDR:** Financial literacy among Filipino state university employees is moderately high but does not significantly correlate with work-life balance, though qualitative data suggest it reduces financial stress and supports personal priorities.

**Problem & Motivation:** Balancing work and family responsibilities is difficult due to workplace dynamics and economic factors. Financial stress exacerbates these challenges, but limited empirical research examines how financial literacy directly affects work-life balance. This gap motivates the study to explore the relationship.

**Approach (summary):**
- Descriptive correlational design with quantitative survey (n=140) and qualitative interviews (n=8) at a Philippine state university.
- Survey measured financial knowledge (13 items), attitudes (10 items, 5-point Likert), and behaviors (23 items), plus work-life balance (11 items).
- Cronbach's alpha for attitude (0.83), behavior (0.85), and work-life balance (0.84) indicated high internal consistency.

**Key Findings (selected):**
- num: Mean financial knowledge score 8.35/13 (SD=3.13), indicating moderate knowledge with high variability.
- Employees have positive financial attitudes (M=3.99, SD=0.73) and positive financial behaviors (M=3.94, SD=0.58).
- num: Correlation between financial literacy and work-life balance is weak and not significant (rho=0.11, p=0.191).
- Qualitative findings indicate financial literacy reduces financial stress, improves focus, and enables better time management for personal priorities.

**Limitations / Contradictions for Odin:**
- Reliance on self-reported data may introduce bias [unacknowledged].
- Small qualitative sample (n=8) limits depth of thematic saturation [unacknowledged].
- Cross-sectional design prevents causal inference (acknowledged via correlational analysis).

**Key takeaways:**
- Financial literacy does not significantly predict work-life balance (rho=0.11).
- Employees have positive financial behaviors but struggle with complex concepts.
- Financial literacy reduces stress and supports personal priorities qualitatively.

---


## LSTM-Based Consumer Behavior Prediction Model Research
**Filename:** `IA--Chen-&-Tan_summarized.md`  
**Authors:** Chen, S.; Tan, W. (2025)  
**ID:** `10.1145/3785706.3785906`  
**Odin Topics:** 5.A, 5.C, 6.A, 6.B, 12.B  

**TLDR:** Predicts consumer purchase intentions using a bidirectional LSTM with self-attention, achieving 94.2% accuracy on 80 million e-commerce interactions.

**Problem & Motivation:** Traditional statistical models and simple machine learning methods fail to capture temporal dependencies and high-dimensional patterns in large-scale consumer data. Deep learning offers potential but requires adaptation for sequential behavior prediction. This study addresses the gap by proposing an LSTM-based model for e-commerce purchase intention forecasting.

**Approach (summary):**
- Dataset contains 500,000 users with over 80 million interaction records (browsing, search, cart, purchase) from a major e-commerce platform over 12 months.
- Preprocessing uses Apache Spark distributed framework, 30-day sliding windows with 50% overlap, generating 128-dimensional feature vectors.
- Model architecture: bidirectional LSTM with 512 hidden units, self-attention with 8 heads, adaptive dropout (0.5→0.3), and softmax output for five purchase intention levels.

**Key Findings (selected):**
- num: Proposed LSTM achieves 94.2% accuracy, 93.8% precision, 94.7% recall, and 94.2% F1-score.
- num: Outperforms standard LSTM by 3.0 percentage points and traditional ML by average 10.7 percentage points (p<0.001).
- num: High-frequency users reach 96.1% accuracy, new users 91.8% (23.6% improvement over traditional methods), high-value customers 96.7%.
- Attention weight analysis reveals recency bias (ratio 1.847) and higher importance for behavioral features over demographics.

**Limitations / Contradictions for Odin:**
- Dataset from a single e-commerce platform limits generalizability to PFMS contexts.
- External environmental factors (e.g., economic shocks) are not modeled [unacknowledged].
- Real-time prediction latency and deployment constraints are not evaluated [unacknowledged].

**Key takeaways:**
- LSTM with attention achieves 94.2% accuracy on purchase prediction.
- Behavioral features dominate over demographics (cumulative score 0.521).
- Model generalizes to new users with 91.8% accuracy.

---


## Personal Financial Management Practices of Average earning households within Indigenous Communities of Mountain Province: Exploring Their Strategies and Challenges
**Filename:** `L--Rosario_summarized.md`  
**Authors:** Rosario, E. P. (2025)  
**ID:** `10.64753/jcasc.v10i3.2426`  
**Odin Topics:** 1.C, 2.A, 2.B, 4.B, 5.A, 13.A, 13.B  

**TLDR:** Indigenous households in Bontoc combine modern budgeting with cultural practices like og-ogfo and paluwagan, prioritizing communal obligations over individual financial goals.

**Problem & Motivation:** Mainstream financial models overlook indigenous cultural practices that shape household financial decisions. There is a lack of frameworks recognizing indigenous communities as having structured financial systems rooted in tradition and reciprocity. This gap prevents culturally sensitive financial literacy programs and policy interventions.

**Approach (summary):**
- Qualitative phenomenological study with 12 average-earning Indigenous households in Bontoc, Mountain Province.
- Semi-structured interviews and one focus group discussion conducted in Ilokano and Bontok languages.
- Thematic analysis using Colaizzi’s method, guided by Social Capital Theory, Social Identity Theory, and Behavioral Economics.

**Key Findings (selected):**
- Households practice budgeting and expense tracking but prioritize cultural obligations like ritual contributions over personal savings.
- Savings take indigenous forms including paluwagan, livestock, and stored rice rather than formal accounts.
- Cultural systems such as og-ogfo (mutual aid) and bayanihan function as informal insurance during financial shocks.
- Income insufficiency and rising costs are managed through kinship support, in-kind contributions, and selective borrowing.

**Limitations / Contradictions for Odin:**
- Small sample size (12 participants) from one municipality limits transferability to other indigenous groups.
- Relies on self-reported financial behaviors, which may be subject to social desirability bias.
- Does not quantify the relative frequency of cultural vs. modern financial practices [unacknowledged].

**Key takeaways:**
- Financial resilience in Bontoc is collective and relational, not individual.
- Budgeting serves social preparation, not just personal wealth planning.
- Savings take form of livestock, rice, and paluwagan cycles.

---


## Using Item Personality-Based Profiling in Music Recommender Systems
**Filename:** `LA--de_Goma-et_al_summarized.md`  
**Authors:** de Goma, J.; Anonuevo, J. N.; Pangan, G. N.; Deang, J. J.; Villaluz, A. (2025)  
**ID:** `10.1145/3779657.3779698`  
**Odin Topics:** 5.A, 5.C, 12.B  

**TLDR:** Incorporating Big Five personality profiles into a hybrid LightFM recommender improves music recommendation accuracy over pure collaborative filtering, especially for cold-start users.

**Problem & Motivation:** Music recommender systems struggle with user variability and the cold-start problem. Traditional collaborative filtering fails to capture diverse user preferences. Personality-based profiling offers a potential solution but has accuracy issues.

**Approach (summary):**
- Data collected from 208 Mapua students via survey (10-item BFI, 100 song ratings, top 5 genres) plus Million Song Dataset playcounts.
- LightFM hybrid model with user features (BFI T-scores, genre preferences) and item features (sonic features: acousticness, danceability, energy, etc., and item personality profiles as proportions).
- Item personality profile computed as proportion of users who liked the item with a given Big Five degree.

**Key Findings (selected):**
- num: Hybrid WARP model achieved training precision 0.23, recall 0.75, AUC 0.82; validation precision 0.46, recall 0.64, AUC 0.57.
- Pure CF overfitted (training AUC 1.00, validation AUC 0.56) and performed worse on unseen data.
- Online evaluation: hybrid Model A had mean user satisfaction 4.15 vs pure CF 3.55 (p<0.05).
- Hybrid model achieved precision 0.57, recall 0.62, F1 0.58 on user feedback, outperforming pure CF (0.41/0.46/0.40).

**Limitations / Contradictions for Odin:**
- "Small song dataset (100 songs) limits recommendation variation. [unacknowledged]"
- "Personality data available for less than 20% of users, causing sparsity. [acknowledged]"
- "Online evaluation sample size of 20 new users is small. [unacknowledged]"

**Key takeaways:**
- Hybrid WARP model achieved 0.46 precision and 0.64 recall on validation.
- Personality profiling reduces cold-start problems in recommender systems.
- User satisfaction improved by 0.6 points with personality integration.

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
- "num: Overall financial literacy mean was 4.02 (High), with retirement planning scoring lowest (3.75) and financial knowledge highest (4.24)."
- "num: Overall financial health mean was 61.2, categorizing respondents as 'Financially Coping' (spending 63.17, saving 51.87, borrowing 72.40, planning 60.22)."
- "num: Only 39.00% of respondents had money remaining at month end (Financially Vulnerable), and emergency fund preparedness scored 3.72."
- Significant differences in financial literacy were found for sex, age, number of children, income, education, teaching position, years of experience, and specialization.

**Limitations / Contradictions for Odin:**
- "The study does not compare teachers to other professions, so findings may reflect public sector constraints rather than teacher‑specific traits."
- "Self‑reported data may overstate financial literacy due to social desirability bias. [unacknowledged]"
- "The financial health scoring (0-100) lacks external validation against actual default or bankruptcy rates. [unacknowledged]"

**Key takeaways:**
- "Teachers have high literacy but are financially coping, not thriving."
- "Only 39% have any money left at month end."
- "Retirement planning literacy is the lowest at 3.75."

---


## Exploring the Interplay of Life Attitude and Cognitive Ability in Shaping the Intention to Stock Market Participation Among Young Professionals in the Philippines
**Filename:** `L--Mutuc_summarized.md`  
**Authors:** Mutuc, E. B. (2025)  
**ID:** `10.3390/ijfs13040222`  
**Odin Topics:** 1.A, 1.C, 5.A  

**TLDR:** Life attitude profile positively influences stock market participation intention among Filipino young professionals, with cognitive ability (financial literacy) mediating this relationship.

**Problem & Motivation:** The stock market participation puzzle has been examined through economic, demographic, and cognitive lenses, but the role of broader psychological orientations such as life attitude remains underexplored. Young professionals in emerging economies like the Philippines face unique financial contexts yet lack empirical study. Understanding how life purpose and meaning interact with cognitive ability to shape investment intentions is critical for designing behavioral interventions.

**Approach (summary):**
- A quantitative cross-sectional survey of 195 randomly selected young professionals (aged 20-39, white-collar) in Bulacan, Philippines.
- Life Attitude Profile-Revised (LAP-R) measured seven existential dimensions on a 7-point scale.
- Cognitive ability proxied by financial literacy using van Rooij et al. (2011) 16-item inventory.

**Key Findings (selected):**
- "num: Life attitude profile has a positive direct effect on stock market participation intention (β=0.154, p=0.025)."
- "num: Cognitive ability mediates the relationship between life attitude and participation intention (indirect β=0.051, p=0.032)."
- "num: Death acceptance (β=0.312, p<0.001) and goal seeking (β=0.396, p=0.009) positively predict intention."
- Life purpose negatively predicts stock market intention (β=-0.243, p=0.036).

**Limitations / Contradictions for Odin:**
- "Self-reported data may introduce response and social desirability bias."
- "Cross-sectional design prevents causal conclusions. [unacknowledged]"
- "Sample from Bulacan limits generalizability to other regions."

**Key takeaways:**
- "Life attitude directly affects stock market intention (β=0.154)."
- "Cognitive ability mediates 39% of life attitude's effect on investment."
- "Death acceptance and goal seeking are strong positive predictors of intention."

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
- Used thematic synthesis with three-stage approach: line-by-line coding, descriptive theme development, and analytical theme generation.

**Key Findings (selected):**
- "num: 78% of university students rated financial knowledge as good/excellent but only 34% could answer basic literacy questions (Germany)."
- "num: Pandemic experiences increased financial literacy awareness scores by 28% (US longitudinal study)."
- "num: Young women 40% more likely to respond 'don't know' to financial questions despite equal knowledge (15-country study)."
- Family financial socialization dominates formal education, with open family discussions correlating with 45% higher financial confidence.

**Limitations / Contradictions for Odin:**
- "English-language publication bias may exclude relevant research from non-English speaking countries. [unacknowledged]"
- "Heterogeneity in financial literacy measures across studies limits comparability. [acknowledged]"
- "Rapid digital financial innovation may outdate some findings. [unacknowledged]"

**Key takeaways:**
- "Young adults show an awareness-confidence paradox: high self-rated but low actual financial literacy."
- "Family discussions about money increase financial confidence by 45% regardless of parents' knowledge."
- "Only 15-20% of youth who plan to learn about finances actually take action within a year."

---


## The Moderating Effect of Access to Finance on Myopic Decision-Making and Business Performance of Low-income Household Micro-Enterprises in Manila
**Filename:** `L--Ong-et_al_summarized.md`  
**Authors:** Ong, H. T.; Keh, K. Z. N.; Lui, N. C. J. L.; Santos, A. H. M.; Suarez, E. J. P. (2025)  
**ID:** `d1e2f3a4-b5c6-7d8e-9f0a-1b2c3d4e5f6a`  
**Odin Topics:** 1.C, 5.A  

**TLDR:** Myopic decision-making significantly harms micro-enterprise business performance, but access to finance moderates this negative effect for low-income households in Manila.

**Problem & Motivation:** Low-income household micro-entrepreneurs often prioritize short-term survival over long-term growth due to financial constraints, yet the combined role of myopic decision-making and access to finance on business performance remains underexplored. Understanding this relationship is critical for breaking poverty cycles. No prior study has integrated these three factors simultaneously.

**Approach (summary):**
- Quantitative survey of 100 sari-sari store owners in Manila.
- Measured four myopia dimensions: competitive, cooperative, temporal, and learning.
- Assessed access to finance via barriers, formal lending, and informal credit.

**Key Findings (selected):**
- "num: Myopic decision-making has a significant effect on business performance (p < 0.001)."
- "num: Access to finance has a significant positive effect on business performance (p < 0.001)."
- "num: Access to finance moderates the myopia-performance relationship (p = 0.005)."
- Temporal myopia (mean 2.96) is the highest myopia dimension among micro-entrepreneurs.

**Limitations / Contradictions for Odin:**
- Sample limited to 100 sari-sari store owners in Manila.
- Relies on subjective Likert-scale responses.
- Cross-sectional design prevents causal inference [unacknowledged].

**Key takeaways:**
- Myopic decision-making harms business performance of low-income micro-enterprises.
- Access to finance significantly improves business outcomes (p < 0.001).
- Financial access moderates the negative effect of short-term thinking.

---


## Consumer's Financial Habits on Server-Based Electronic Money as It Affects Their Financial Behavior: Moderated By Monthly Transactions
**Filename:** `L--Torres-et_al-2025a_summarized.md`  
**Authors:** Torres, R. C.; Olaivar, G. M.; Britanico, S. I. (2025)  
**ID:** `10.1145/3785171.3785192`  
**Odin Topics:** 1.C, 5.A, 11.A  

**TLDR:** Saving, spending, donating, and investing habits significantly influence financial behavior among GCash users in the Philippines, with monthly transaction frequency moderating only the spending-behavior relationship.

**Problem & Motivation:** The rapid adoption of e-wallets like GCash in the Philippines has transformed consumer payment behavior, but the specific financial habits (saving, spending, donating, investing, credit) driving overall financial behavior on these platforms remain underexplored. Understanding how transaction frequency moderates these relationships is critical for designing effective financial management tools and promoting responsible digital finance.

**Approach (summary):**
- Quantitative survey of 300 purposively sampled Filipino GCash users aged 18-60.
- Five financial habit predictors (saving, spending, donating, investing, credit/loan) measured via 5‑point Likert scales.
- Multiple regression and moderation analysis using interaction term (spending × monthly transactions) grounded in Theory of Planned Behavior.

**Key Findings (selected):**
- num: Investment habit had the strongest positive effect on financial behavior (β=0.243, p<0.001).
- num: Saving (β=0.178), spending (β=0.115), and donating (β=0.144) habits also significantly influenced financial behavior (p≤0.003).
- Credit/loan habit showed no significant effect (β=-0.003, p=0.955).
- num: Monthly transaction frequency significantly moderated only the spending‑behavior relationship (β=-0.163, p<0.001).

**Limitations / Contradictions for Odin:**
- "Cross‑sectional data; causal claims cannot be made. [unacknowledged]"
- "Purposive sampling may introduce selection bias. [unacknowledged]"
- "Self‑report measures subject to social desirability and recall bias. [unacknowledged]"

**Key takeaways:**
- "Investment habits had the strongest impact on financial behavior (β=0.243)."
- "Monthly transaction frequency intensifies the effect of spending habits on behavior."
- "Credit and loan habits showed no significant influence among GCash users."

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
- "num: Pearson r = 0.612 (p < 0.05) indicates a strong positive relationship between online buying decisions and poor budget management."
- "num: 83% of respondents were aged 18-24, and 62% were female, a group highly responsive to digital trends."
- "num: Mean score for online buying decisions was 3.02 (Agree/High), with social media influence highest at 3.05."
- "num: Mean personal budget score was 3.15 (Agree/High), but necessary expenses scored 3.32 (Very High)."

**Limitations / Contradictions for Odin:**
- "The study focused only on one degree program (Business Administration) at one campus. [unacknowledged]"
- "Data collection was inside the university premises; results not applicable to non-students."
- "The outcome applies only to the 153 randomly selected respondents and cannot be generalized beyond this population."

**Key takeaways:**
- "r=0.612 strong correlation between online buying and poor budget management."
- "Social media likes and influencer ads most strongly drive impulsive spending."
- "Age and civil status affect savings; sex affects savings but not allowance."

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
- num: Rational consumers with fixed obligatory consumption will go to ruin regardless of utility function concavity.
- num: With impulsive consumption and minimum subsistence, probability of avoiding ruin decays exponentially as exp(-cT) for sufficiently large T.
- num: Lookahead of k steps yields utility advantage of Ω(k) over no lookahead under bounded income.
- Algorithmic persuasion and obligatory consumption create value capture, where consumers adopt externally imposed values without critical reflection.

**Limitations / Contradictions for Odin:**
- "Model uses simple intertemporal consumption framework without debt or liabilities."
- "Does not incorporate behavioral economics insights like present bias or loss aversion."
- "Macroeconomic factors like inflation and recessions not modeled."

**Key takeaways:**
- Fixed obligatory consumption guarantees financial ruin even for rational agents.
- Algorithmic impulse triggers make ruin exponentially more likely over time.
- Knowing work schedules 2 weeks ahead yields significantly higher utility.

---


## The Impact of Personal Budgeting Skills on College Students’ Financial Stability
**Filename:** `L--Dela_Torre-et_al_summarized.md`  
**Authors:** Dela Torre, J. M. Y.; Jangao, J. P. P.; Maghilum, J. T.; Man-onan, R. J. H.; Pepito Jr, S. G.; Rapirap Jr, G. P.; Cervantes, J. Z. (2025)  
**ID:** `10.61424/rjbe.v3.i3.574`  
**Odin Topics:** 5.A, 7.A, 13.A  

**TLDR:** Personal budgeting skills in planning, goal setting, and expense tracking strongly correlate with college students' financial stability, reducing stress and increasing savings.

**Problem & Motivation:** College students face rising living costs and economic uncertainties yet many lack adequate financial education, leading to financial stress and poor spending choices. Existing research shows gaps in understanding how specific budgeting practices directly impact financial stability. This study addresses the need to quantify the relationship between budgeting skills and financial outcomes among students.

**Approach (summary):**
- Surveyed 213 randomly selected college students from a Philippine higher education institution using a structured questionnaire.
- Measured budgeting skills across three dimensions: budget planning, financial goal setting, and expense tracking.
- Assessed financial stability via financial stress, savings, and monthly expense management using a four-point Likert scale.

**Key Findings (selected):**
- "num: 0.7247 correlation coefficient (p < 0.01) indicates strong positive relationship between budgeting skills and financial stability."
- Students demonstrated very high levels of budgeting skills (mean 3.45/4.00) and financial stability (mean 3.49/4.00).
- Most students (86%) have monthly allowance below ₱1,000, yet effective budgeting enables savings and reduced financial stress.
- Significant differences in budgeting impact exist across age, year level, program, and monthly allowance.

**Limitations / Contradictions for Odin:**
- Study limited to a single institution in Baungon, Bukidnon; findings may not generalize. [unacknowledged]
- Reliance on self-administered questionnaires may introduce response bias. [acknowledged in paper]
- Cross-sectional design prevents causal inference. [unacknowledged]

**Key takeaways:**
- Budgeting skills correlate strongly (r=0.72) with financial stability.
- Even very low-income students can save through disciplined budgeting.
- Three key skills: planning, goal setting, and expense tracking.

---


## Harnessing artificial intelligence and machine learning for fraud detection and prevention in Nigeria
**Filename:** `IA--Odufisan-et_al_summarized.md`  
**Authors:** Odufisan, O.I.; Abhulimen, O.V.; Ogunti, E.O. (2025)  
**ID:** `10.1016/j.jeconc.2025.100127`  
**Odin Topics:** 5.A, 8.A, 8.B, 10.A, 10.B  

**TLDR:** AI and ML enable real-time anomaly detection, behavior analysis, and risk scoring to combat fraud across Nigeria's banking, e-commerce, healthcare, and education sectors.

**Problem & Motivation:** Traditional fraud detection methods (rule-based, manual) fail to keep pace with evolving fraud schemes and large data volumes, causing economic losses and eroding trust in Nigeria's digital economy. Fraud threatens financial stability, hinders growth, and undermines digital inclusion. A paradigm shift to adaptive, intelligent systems was missing.

**Approach (summary):**
- Literature review of academic publications, industry reports, government records, and global fraud studies.
- Secondary data on fraud trends, technological adoption, and sectoral impacts across banking, e-commerce, healthcare, and education.
- Primary data from unstructured interviews with stakeholders in Nigerian banking, e-commerce, healthcare, and educational sectors.

**Key Findings (selected):**
- "num: 24 commercial banks lost N5.79 billion to fraud in Q2 2023, a 1125% increase from Q1."
- "num: 94.35% of bank fraud losses came from fraudulent loans."
- "num: SVM achieved over 98% accuracy for phishing email detection."
- "num: Feed-forward neural network achieved 97% detection rate for credit card fraud and phishing websites."

**Limitations / Contradictions for Odin:**
- "Primary data limited to unstructured interviews and anecdotal evidence; no large-scale quantitative study. [unacknowledged]"
- "Does not provide a specific, reproducible algorithm for anomaly detection; remains a high-level review. [unacknowledged]"
- "Ethical concerns like algorithmic bias are mentioned but not explored in depth. [unacknowledged]"

**Key takeaways:**
- "Anomaly detection with ML achieved 97% accuracy for credit card fraud."
- "Real-time analysis enables proactive fraud prevention before losses occur."
- "Behavioral profiling reduces false positives by learning user baselines."

---


## "Credit Card Fraud Detection Through Deep Learning and Real-Time Data Streams: A Comparison and New Directions"
**Filename:** `IA--Polytarchos_summarized.md`  
**Authors:** Polytarchos, E. (2025)  
**ID:** `10.47852/bonviewFSI52026108`  
**Odin Topics:** 5.A, 8.A, 8.B, 12.A, 12.B  

**TLDR:** Compares deep learning (LSTM, MLP) and real-time data stream analysis (BEReTiC) for credit card fraud detection, finding deep learning achieves 92% accuracy but slower adaptation, while real-time clustering offers faster detection with lower false positives.

**Problem & Motivation:** Existing fraud detection methods either rely on batch-trained deep learning requiring extensive preprocessing and retraining, or real-time systems with lower initial accuracy. There is a lack of comprehensive empirical comparison between these paradigms on high-volume financial data. This gap prevents system designers from making informed deployment decisions.

**Approach (summary):**
- Used two proprietary datasets: IND (17.5M individual transactions) and SUM (1.2M purchase summaries) with customer demographic and behavioral labels.
- Injected 1000 synthetic fraudulent transactions by assigning average behavioral profiles of one customer to another customer's transactions.
- Deep learning pipeline trained LSTM and MLP models to predict customer labels (e.g., total funds range) and computed Scale of Suspicious Transaction (SST) from ensemble misclassification consensus.

**Key Findings (selected):**
- "num: Deep learning LSTM achieved 92% accuracy predicting total funds range and 86% for age range."
- "num: Deep learning detected 788 of 1000 injected fraudulent transactions with 1340 false positives (0.007% misclassification rate)."
- "num: Real-time clustering detected 619 of 1000 injected frauds with 574 false positives (0.003% misclassification rate)."
- Real-time clustering had lower classification accuracy (e.g., 66% for total funds range) due to cold-start before building customer fingerprints.

**Limitations / Contradictions for Odin:**
- "Real-time clustering suffers from cold-start: initial customer fingerprints are incomplete, lowering early accuracy. [acknowledged]"
- "Dataset is proprietary and not publicly available. [unacknowledged]"
- "No comparison to existing production fraud detection systems or industry benchmarks. [unacknowledged]"

**Key takeaways:**
- "Deep learning LSTM achieved 92% accuracy predicting customer total funds range."
- "Real-time clustering detected 619 of 1000 frauds with only 574 false alarms."
- "Hybrid integration of batch and streaming methods is proposed as future direction."

---


## WEKA-BASED DECISION-TREE MODEL FOR USER SUBSCRIPTION PLAN PREDICTION
**Filename:** `LA--Guban-et_al_summarized.md`  
**Authors:** Guban, J. C. R.; Menderico, C. D. R.; Montalban, D. M. G. (2025)  
**ID:** `a1b2c3d4-e5f6-5123-89ab-cdef01234567`  
**Odin Topics:** 5.A, 5.C, 6.A, 12.A, 12.B  

**TLDR:** A J48 decision tree model predicts streaming subscription plans from user demographics and behaviors, achieving 72% accuracy with country as the strongest predictor.

**Problem & Motivation:** Streaming platforms lack interpretable models to understand how user attributes like age, device, and country jointly influence subscription plan selection. This gap hinders targeted marketing and plan optimization. The study addresses this by developing a transparent decision-tree classifier.

**Approach (summary):**
- Used 2,500 anonymized user records with five attributes: country, age, gender, device type, subscription start month.
- Applied J48 algorithm in WEKA with an 80/20 train-test split.
- Evaluated using accuracy, Kappa statistic, precision, recall, F-measure, and ROC area.

**Key Findings (selected):**
- "num: 72% overall accuracy on the test set."
- "num: Kappa statistic of 0.5797 indicates moderate agreement."
- Country identified as most influential predictor, followed by age and device type.
- Younger smartphone users subscribing later in the year tend to choose Premium plans in the US.

**Limitations / Contradictions for Odin:**
- Dataset limited to five user attributes, excluding behavioral indicators such as watch time or session frequency.
- Only J48 algorithm tested; ensemble methods not explored.
- Model not validated on a different dataset or in a real-time setting.

**Key takeaways:**
- J48 decision tree predicts subscription plans with 72% accuracy.
- Country is the strongest predictor, followed by age and device.
- All United Kingdom users consistently choose Standard plan.

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
- Data from secondary sources: approximately 70 peer-reviewed articles, policy documents, and empirical studies (2015–2024).
- Sources retrieved from Scopus, Web of Science, Google Scholar, and JSTOR using keywords such as financial stress, fintech adoption, and CBT.

**Key Findings (selected):**
- Digital financial technologies play a dual role: budgeting apps and savings platforms enhance financial awareness and self-efficacy, while impulsive borrowing and fraud exposure trigger cognitive distortions.
- Financial stress is shaped more by students’ cognitive interpretations and coping strategies than by technology itself.
- Catastrophizing financial difficulties and negative self-evaluation lead to avoidance behaviors and impulsive borrowing, increasing vulnerability.
- Fintech lending applications encourage rapid credit access, which may lead to unsustainable debt accumulation when used without financial literacy.

**Limitations / Contradictions for Odin:**
- Conceptual and literature-based methodology limits direct measurement of student experiences.
- Evidence synthesized reflects existing literature patterns, not primary data. [unacknowledged]
- Rapid fintech changes may introduce behaviors not yet documented in current research.

**Key takeaways:**
- Digital financial technologies reduce or amplify financial stress depending on user skills.
- Cognitive distortions like catastrophizing intensify financial anxiety.
- Financial literacy alone insufficient; cognitive-behavioral skills are needed.

---


## Simple Financial Management in Housewife Communities: A Qualitative Study on Daily Financial Management Patterns
**Filename:** `I--Efendi-&-Widagdo_summarized.md`  
**Authors:** Efendi, M. I.; Widagdo, C. S. (2025)  
**ID:** `10.59890/ijaeam.v3i3.18`  
**Odin Topics:** 1.C, 2.A, 2.B, 3.A, 5.A, 7.A, 13.A, 13.B  

**TLDR:** Housewives in Salatiga develop adaptive financial strategies including informal recording, expenditure prioritization, community-based savings groups, and risk management despite limited formal literacy.

**Problem & Motivation:** Housewives manage daily household finances but have lower formal financial literacy (36.1% vs 40.6% for men) and face structural disadvantages. Research overlooks their sophisticated adaptive strategies and community-based financial systems.

**Approach (summary):**
- Qualitative case study in Salatiga, Central Java, involving 25 housewives as primary financial managers.
- Data collection through semi-structured interviews (60-90 minutes), non-participant observation of community activities, and document analysis.
- Analysis using ATLAS.ti with open, axial, and selective coding, plus member checking for validation.

**Key Findings (selected):**
- num: 5 of 8 informants perform routine manual expense recording; others use mental envelopes or digital apps inconsistently.
- Housewives prioritize primary needs (food, school fees, bills) over secondary and tertiary needs using mental accounting.
- Strategies include gradual purchasing, cash buffers (e.g., Rp50,000), and informal shop credit for liquidity gaps.
- Income diversification through home-based activities yields Rp300,000–Rp500,000 monthly additional income.

**Limitations / Contradictions for Odin:**
- "Small sample (25 housewives) from one city limits external validity."
- "Self-reported financial practices may suffer from social desirability bias. [unacknowledged]"
- "No longitudinal data to assess stability of adaptive strategies over time. [unacknowledged]"

**Key takeaways:**
- "num: 5 of 8 housewives manually record expenses; others use envelope systems."
- "Community arisan groups act as forced savings with social discipline."
- "Housewives create micro emergency funds of Rp50,000 to Rp200,000."

---


## AI-POWERED PERSONALIZATION IN DIGITAL BANKING: A REVIEW OF CUSTOMER BEHAVIOR ANALYTICS AND ENGAGEMENT
**Filename:** `I--Ashrafuzzaman-et_al_summarized.md`  
**Authors:** Ashrafuzzaman, M.; Parveen, R.; Sumiya, M. A.; Rahman, A. (2025)  
**ID:** `10.63125/z9s39s47`  
**Odin Topics:** 5.A, 6.A, 10.A, 11.A  

**TLDR:** A systematic review of 111 articles finds that AI-powered personalization in digital banking enhances customer engagement through behavior analytics, predictive modeling, and real-time personalization, while facing challenges in measurement, ethics, and cross-cultural adaptation.

**Problem & Motivation:** Digital banking lacks systematic synthesis of how AI personalization, customer behavior analytics, and engagement interact. Financial institutions need coherent frameworks to implement personalized services that build trust and loyalty. Existing literature is fragmented across techniques, outcomes, and governance.

**Approach (summary):**
- Conducted systematic literature review following PRISMA 2020 guidelines.
- Searched Scopus, Web of Science, IEEE Xplore, ScienceDirect, and Google Scholar for articles from 2014-2024.
- Initial pool of 1,248 records reduced to 111 peer-reviewed articles after duplication removal and screening.

**Key Findings (selected):**
- "num: 92 of 111 reviewed articles emphasize AI personalization as integral to digital banking transformation."
- "num: 81 studies identify customer behavior analytics as primary driver of AI personalization."
- "num: 74 articles report positive impact of personalization on customer satisfaction, retention, and lifetime value."
- "num: 63 studies highlight ethical, legal, and governance challenges constraining personalization effectiveness."

**Limitations / Contradictions for Odin:**
- "Most studies use inconsistent definitions and metrics for personalization and engagement, limiting comparability [unacknowledged]."
- "Longitudinal research on AI personalization effectiveness across customer lifecycles is scarce [unacknowledged]."
- "Cross-cultural differences in customer behavior and personalization perception are underexplored, with most studies from Western contexts [unacknowledged]."

**Key takeaways:**
- "AI personalization increases customer retention and lifetime value in digital banking."
- "Behavior analytics drives 81 of 111 studies' personalization strategies."
- "Transparency and consent are critical for user trust in AI banking systems."

---


## "BUY NOW, PAY LATER: SHOPEE ONLINE STORE USERS EXPERIENCES ON SHOPEE PAY LATER FEATURE (SPAY LATER)"
**Filename:** `L--Canalog-et_al_summarized.md`  
**Authors:** "Calanog, V. C.; Paderan, M. J. D.; Adove, R. C. A.; Bathan, C. M. N.; Catibog, D. N.; Rivera, G. R.; Mangarin, J. A." (2025)  
**ID:** `10.5281/zenodo.15031111`  
**Odin Topics:** 1.C, 5.A, 13.B  

**TLDR:** "Shopee Pay Later users employ the feature primarily for essential needs, valuing convenience and flexible repayment, while facing technical issues and requiring disciplined budgeting."

**Problem & Motivation:** "Prior studies on Buy Now, Pay Later focused on either positive or negative impacts but lacked a comprehensive understanding of user motivations and behaviors. This gap prevented a holistic view of how users experience features like Shopee Pay Later. The study addresses the overall experience of Spay Later users, including satisfaction, convenience, financial behavior, and challenges."

**Approach (summary):**
- "Qualitative phenomenological study using semi-structured interviews with 10 Shopee Spay Later users in Balayan, Batangas, Philippines."
- "Participants selected via judgmental sampling: gold or platinum loyalty tier, credit limit ≥5000 PHP, and at least one year of Spay Later use."
- "Thematic analysis applied to interview transcripts to identify patterns in user satisfaction, convenience, financial behavior, and challenges."

**Key Findings (selected):**
- "Three usage patterns emerged: occasional use for necessities, regular monthly use for essentials, and needs-based use during financial constraints."
- "Users primarily purchase everyday household necessities, high-cost essential items during financial constraints, and rarely non-essential items."
- "Motivations include limited budget and financial independence, ability to afford high-cost purchases over time, attractive incentives, and urgent needs."
- "Challenges include transaction errors, unexpected fees, insufficient credit balance, and seller accountability concerns."

**Limitations / Contradictions for Odin:**
- "Small sample size (10 participants) limits generalizability. [unacknowledged]"
- "Qualitative only; no quantitative validation of claimed effects. [unacknowledged]"
- "Participants restricted to gold/platinum tier users with ≥5000 PHP credit limit, excluding lower-tier users. [unacknowledged]"

**Key takeaways:**
- "10 gold/platinum users with 5000 PHP credit limit were interviewed."
- "Three usage patterns: occasional, regular monthly, and needs-based."
- "Spay Later improved budgeting skills and financial flexibility."

---


## Credit Card Customer Profiling Using Self-Supervised Representation Learning on Multi-Source Financial Data
**Filename:** `IA--Yachamaneni-et_al_summarized.md`  
**Authors:** Yachamaneni, T.; Kotadiya, U.; Arora, A. S. (2025)  
**ID:** `10.63282/3050-9262.IJAIDSML-V6I1P118`  
**Odin Topics:** 5.A, 5.C, 6.A, 11.B, 12.B  

**TLDR:** Self-supervised representation learning on multi-source financial data (transactions, demographics, credit, web activity) outperforms K-Means and XGBoost in customer profiling, credit risk prediction, and churn detection.

**Problem & Motivation:** Traditional supervised customer profiling requires costly labeled data and fails to leverage unlabeled multi-source data. Static feature engineering cannot capture temporal dynamics or generalize across behavioral shifts. There is a need for scalable, privacy-friendly profiling that extracts rich representations from heterogeneous financial data without manual labels.

**Approach (summary):**
- A multi-source dataset of 100,000 customers with transaction logs, demographics, credit bureau reports, and web activity was collected.
- Separate encoders handle each modality: temporal encoders for sequences, feedforward layers for static features, and embeddings for categorical variables.
- SSL pretext tasks include masked attribute prediction, temporal order prediction, and augmented view prediction.

**Key Findings (selected):**
- "num: Proposed SSL achieves Silhouette score of 0.56, compared to K-Means (0.35) and XGBoost (0.41)."
- "num: SSL attains AUC of 0.91 for credit risk prediction, outperforming XGBoost (0.84)."
- "num: SSL reaches F1 of 0.81 for churn prediction, versus XGBoost (0.69)."
- "num: Removing temporal encoding causes a 4.2% drop in AUC, the largest decrease among ablated components."

**Limitations / Contradictions for Odin:**
- "Single private bank dataset may not generalize across diverse Filipino young professionals. [unacknowledged]"
- "Interpretability of SSL representations is not addressed, limiting regulatory acceptance. [acknowledged as gap]"
- "No comparison to other SSL methods (e.g., SimCLR, MoCo) on financial data. [unacknowledged]"

**Key takeaways:**
- "SSL outperforms XGBoost by 7 points in AUC for credit risk prediction."
- "Temporal encoding is the most critical component, causing a 4.2% drop."
- "Multi-source data including web activity boosts profiling accuracy by 3.8%."

---


## The Influence of E-Wallets on The Consumptive Behavior Generation Z: Systematic Review
**Filename:** `I--Kuswardhani-et_al_summarized.md`  
**Authors:** Kuswardhani, E. L.; Sari, M. A. N. P.; Yuniawan, A.; Kusumawardhani, A. (2025)  
**ID:** `3c7e3b2a-1f4d-5e6a-8b9c-0d1e2f3a4b5c`  
**Odin Topics:** 1.C, 5.A, 9.B, 11.A  

**TLDR:** E-wallet usage positively correlates with increased consumptive behavior in Generation Z, driven by convenience, promotions, and reduced payment friction.

**Problem & Motivation:** E-wallets offer ease and speed but may foster impulsive spending among Generation Z, a demographic that is digitally native and financially formative. A systematic synthesis of empirical evidence on behavioral triggers and design features was missing. Understanding these effects is critical for balancing digital financial inclusion with long-term financial well-being.

**Approach (summary):**
- Systematic literature review following PRISMA framework, analyzing 28 empirical studies published from 2020 to 2025.
- Search conducted across Scopus, Web of Science, ScienceDirect, ProQuest, and Google Scholar using keywords such as “e-wallet,” “Generation Z,” and “impulsive buying.”
- Synthesis focused on e-wallet features (promotions, notifications, gamification, real‑time transactions) and their effect on spending frequency, impulse buying, and financial awareness.

**Key Findings (selected):**
- "num: 28 studies showed a significant positive correlation between e-wallet usage frequency and increase in consumer spending."
- "num: E-wallet promotions (cashback, discounts, loyalty points) had a significance value of 0.000 (p<0.005) in influencing consumer behavior (Lestari et al., 2021)."
- E-wallets reduce the perceived “pain of paying” due to lack of cash tangibility, leading to unplanned and impulsive purchases.
- Real‑time transactions, push notifications, and gamification elements (spending streaks, loyalty tiers) condition users toward automatic, less deliberate spending habits.

**Limitations / Contradictions for Odin:**
- "Only publications from 2020–2025 were included, potentially missing earlier foundational work."
- "Geographic focus not systematically controlled; results may vary between developed and developing economies [unacknowledged]."
- "The review does not quantitatively meta‑analyze effect sizes across studies [unacknowledged]."

**Key takeaways:**
- "E-wallet usage frequency positively correlates with increased spending across 28 studies."
- "Promotional features like cashback reduce the perceived pain of paying."
- "Most e-wallets lack budgeting tools, leading to financial regret."

---


## Ang tagapagtaguyod na anak for Filipino adults: an exploratory research
**Filename:** `L--Quindoza-et_al_summarized.md`  
**Authors:** Quindoza, T. L. V.; Malcampo, M. C.; Rungduin, T. (2025)  
**ID:** `10.1108/SEAMJ-09-2024-0063`  
**Odin Topics:** 1.A, 1.B, 1.C, 2.A, 5.A  

**TLDR:** Filipino young adults and middle-aged parents perceive the tagapagtaguyod na anak as a family supporter providing financial, emotional, and social support, driven by poverty, parental expectations, and cultural values like utang na loob.

**Problem & Motivation:** The breadwinner role is narrowly viewed as financial provider, lacking a nuanced understanding within Filipino culture. This study explores the broader responsibilities and dynamics of the "tagapagtaguyod na anak" role among Filipino adults.

**Approach (summary):**
- Data collected via semi-structured interviews with 16 Filipino adults from Metro Manila (8 single adults aged 18-29, 8 parents aged 40-60).
- Thematic analysis following Braun and Clarke was used to identify patterns and themes in participants' definitions, characteristics, and factors of the tagapagtaguyod role.
- Pilot testing of interview questions with added sub-questions ensured content validity.

**Key Findings (selected):**
- The tagapagtaguyod na anak provides financial, emotional, and social support, acting as provider, bearer, manager, and lifter of the family.
- Eldest children typically fill the role, but middle children are also seen; any gender can assume it, though women are perceived as more likely.
- Characteristics include being responsible, self-sacrificing, self-sufficient, and excellent.
- Extrinsic factors (poverty, family structure change, parental incapacity, expectations) and intrinsic factors (volition, sense of responsibility, financial independence) drive role adoption.

**Limitations / Contradictions for Odin:**
- "Predominance of female participants may have influenced perceptions of gender."
- "Sample limited to Metro Manila, not generalizable nationwide."
- "Study explores perceptions rather than lived experiences of tagapagtaguyod."

**Key takeaways:**
- "Tagapagtaguyod na anak provides financial, emotional, and social support."
- "Poverty and parental expectations drive this role in Filipino families."
- "Utang na loob (gratitude) is a core cultural motivator."

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
- "num: Consumers update only 2.48 budgets per week on average (out of 4 categories) in baseline, 2.11 with $1 numeracy threshold."
- "num: 68% of consumers do not benefit from forced weekly full budget updates; 3.3% go bankrupt under forced attention in $1-threshold model."
- Ex-ante most consumers (79%) are budget prioritizers (mental accounting), but ex-post a plurality (43-47%) are spendthrifts who increase spending regardless of prior over/under-spending.
- Heterogeneous rationality: most consumers are neither fully rational (always update all budgets) nor fully bounded (never update).

**Limitations / Contradictions for Odin:**
- "Data limited to low-income prepaid debit card users, not generalizable. [unacknowledged]"
- "Model assumes strong separability and Stone-Geary utility, potentially unrealistic. [unacknowledged]"
- "Latent budgeting inference is model-dependent and lacks direct validation. [acknowledged]"

**Key takeaways:**
- "2.11 average weekly budget updates under $1 numeracy threshold."
- "68% of users worse off with full budget attention."
- "Bankrupt consumers have only 1.25 updates per week."

---


## Financial literacy in research and policymaking: the concept at the core
**Filename:** `I--Felbermayr-et_al_summarized.md`  
**Authors:** Zieser, M.; Voith, V.; Lorenz, T.; Anyfantaki, S. (2024)  
**ID:** `8e9f1a2b-3c4d-5e6f-7a8b-9c0d1e2f3a4b`  
**Odin Topics:** 1.C, 5.A, 6.A, 7.A, 12.A  

**TLDR:** Financial literacy lacks consensus on definition, measurement, and empirical relevance; this paper reviews its origins, stakeholders, definitions, measurement approaches, determinants, and impacts, recommending coherent definitions and rigorous methods.

**Problem & Motivation:** The field of financial literacy research and policy is characterized by considerable heterogeneity in definitions and measurement approaches, preventing direct comparison of empirical results and clear conclusions on the effectiveness of financial education. There is little consensus on what financial literacy is, how to measure it, or how empirically relevant it is. This paper aims to provide a structured overview and guide to the concept to enable targeted decisions in defining and quantifying it.

**Approach (summary):**
- Explores six perspectives: historical origins, key stakeholders (OECD, World Bank, national strategies), definitions and theoretical assumptions, measurement approaches (Big Three, ISAFL, PISA, World Bank), determinants (sociodemographic, socioeconomic, macro-level), and effects (financial behavior, resilience, well-being).
- Analyzes discrepancies in measurement by comparing results from the OECD/INFE ISAFL and S&P Global Financial Literacy Survey across 28 countries.
- Reviews literature on determinants including age, gender, education, income, and welfare regime generosity.

**Key Findings (selected):**
- num: Definitions of financial literacy vary across five key aspects: goals, traits considered, inclusion of observable behaviors, thematic focus, and inclusion of environmental context factors.
- num: Correlation between countries' S&P survey percentages and ISAFL knowledge scores is only r = .41, indicating substantial measurement discrepancies.
- Financial knowledge correlates with positive financial behaviors such as saving, retirement planning, and reduced debt, but causal evidence from interventions is limited and mixed.
- Gender, age, education, income, and the generosity of welfare regimes are significant determinants of financial literacy.

**Limitations / Contradictions for Odin:**
- "Focuses primarily on quantitative evaluation methods and English-language literature, omitting qualitative and mixed-method approaches. [unacknowledged]"
- "Does not provide conclusive causal evidence on the effectiveness of financial education for financial well-being. [acknowledged]"
- "Sample of countries and studies reviewed may not fully represent non-OECD contexts, limiting generalizability to the Philippines. [unacknowledged]"

**Key takeaways:**
- "Correlation between two major financial literacy surveys across 28 countries is only r=.41."
- "Financial knowledge correlates with better saving and investment behavior but causal evidence is mixed."
- "Gender gap in financial literacy appears already during adolescence, driven partly by confidence differences."

---


## ENHANCING FINANCIAL SERVICES THROUGH BIG DATA AND AI-DRIVEN CUSTOMER INSIGHTS AND RISK ANALYSIS
**Filename:** `IA--Yang-et_al_summarized.md`  
**Authors:** Yang, T.; Xin, Q.; Zhan, X.; Zhuang, S.; Li, H. (2024)  
**ID:** `10.60087/jklst.vol3.n3.p53-62`  
**Odin Topics:** 5.A, 5.C, 6.A, 8.A, 8.B, 11.A, 11.B, 12.A, 12.B  

**TLDR:** Supervised learning with XGBoost and face recognition enables customer profiling, profit prediction, fraud detection, and churn analysis in financial services.

**Problem & Motivation:** Financial institutions need accurate customer identification and risk analysis to improve loan approval and risk management. Traditional statistical models struggle with massive data and complex financial behaviors. Machine learning offers advantages in processing large datasets and discovering hidden patterns.

**Approach (summary):**
- Constructed six feature systems from customer attributes, debit/credit card transactions, loan applications, trends, and page visit behavior.
- Used supervised learning as basis for AI pricing model to combine man-machine decision making.
- Applied XGBoost for profit modeling at account level, modeling revenue, default probabilities, and loss rates.

**Key Findings (selected):**
- "num: Profit quartile spread across risk ranges increases with risk level, indicating challenge in high-risk areas."
- "num: Learning rate limited to 0.001-0.01 with thousands of trees to prevent overfitting."
- Revenue model and total profit model show poor forecasting performance but better ranking performance.
- Hump-shaped relationship between profit component and risk is retained between predicted and actual curves.

**Limitations / Contradictions for Odin:**
- "Model performance is poor for revenue and total profit forecasting at high risk levels."
- "No discussion of data privacy implications for customer profiling. [unacknowledged]"
- "Lacks validation on non-US or Filipino demographic data. [unacknowledged]"

**Key takeaways:**
- XGBoost profit models outperform risk-only models in ranking profitability.
- Profit and risk have a non-monotonic hump-shaped relationship.
- Community discovery algorithms effectively detect gang fraud in credit data.

---


## Do Remittances Boost Household Spending: New Evidence from Migrants’ Household Survey
**Filename:** `L--Bayangos-&-Lubangco_summarized.md`  
**Authors:** Bayangos, V. B.; Lubangco, C. K. (2024)  
**ID:** `d4f8c2a1-5e6b-4c7d-9a8b-1f2e3d4c5b6a`  
**Odin Topics:** 1.C, 3.A, 5.A, 6.A, 13.A, 13.B  

**TLDR:** Remittances increase household spending in the Philippines, but financial constraints limit welfare gains for poorer households, while macroeconomic factors like exchange rates and transfer costs drive remittance flows.

**Problem & Motivation:** Understanding how remittances affect household consumption and the factors driving remittance flows is critical for maximizing development impact in remittance-dependent economies like the Philippines. Prior research leaves gaps in the nuanced relationship between remittances, consumption patterns, and macroeconomic determinants. This study provides new evidence using household surveys and financial sector data.

**Approach (summary):**
- Analyzed Survey on Overseas Filipinos (SOF) 2007-2022 (nationally representative, 1.96M OFWs in 2022) and Family Income and Expenditure Survey (FIES) 2018/2021.
- Used logistic regressions (odds ratios) to assess determinants of saving vs investing behavior of migrant households.
- Applied propensity score matching (PSM) to estimate average treatment effects of remittances on consumption shares for poor vs non-poor households.

**Key Findings (selected):**
- "num: OFW households allocated 9.9% of cash remittances to savings on average (2008-2022), while 75% allocated nothing to investments."
- "num: 57.2% of cash remittances were sent through banks in 2022; telegraphic transfer fees average 6-7% of remittance value."
- "num: A 1% increase in telegraphic transfer fees reduces cash remittances by approximately 12.5%."
- Poor remittance-receiving households show smaller shifts in expenditure shares (e.g., food reduction -1.28% vs -1.48% for non-poor).

**Limitations / Contradictions for Odin:**
- "Endogeneity between remittances and consumption may bias OLS results, though PSM partially addresses this. [unacknowledged]"
- "The SOF question on remittance allocation only started in 2008 and lacks itemized non-food categories."
- "Small sample of immigrant households (n=522) limits generalizability of comparisons."

**Key takeaways:**
- "OFW households save 9.9% of cash remittances on average, but 50% save nothing."
- "Transfer fees of 6-7% significantly reduce remittance flows."
- "Remittances increase non-food spending only for non-poor households."

---


## Decoding the eco-financial mindset: financial literacy, attitudes, and efficacy measures and the spending behavior of Filipino millennials
**Filename:** `L--Lim-&-Cordova_summarized.md`  
**Authors:** Lim, C. T.; Cordova, W. (2024)  
**ID:** `10.1051/bioconf/20249305010`  
**Odin Topics:** 1.A, 1.C, 5.A  

**TLDR:** Survey of 431 Filipino millennials finds strong positive correlations among financial literacy, attitude, and efficacy, and a negative correlation between spending behavior and financial attitude.

**Problem & Motivation:** Existing literature often examines financial literacy, attitude, and efficacy in isolation or paired combinations, leaving a gap in comprehensive understanding. Filipino millennials face economic uncertainties and lack financial acumen, making them financially vulnerable. A holistic exploration of these variables together is needed to inform targeted interventions.

**Approach (summary):**
- Online survey of 431 millennials in Laguna, Philippines using Google Forms.
- Measured financial literacy (7 items), attitude (8 items), efficacy (10 items), and spending behavior (9 categories) via Likert scales.
- Used Structural Equation Modeling (SEM) and Confirmatory Factor Analysis (CFA) in Jamovi.

**Key Findings (selected):**
- "num: Strong positive correlations: financial efficacy ↔ literacy (β=0.614, p<.001), attitude ↔ literacy (β=0.578, p<.001), attitude ↔ efficacy (β=0.888, p<.001)."
- "num: Negative relationship between spending behavior and financial attitude (β=-0.176, p=0.034)."
- "num: 42% of respondents spend 41% or more of their income (S1)."
- "num: 93.7% spend 10% or less of income on beer and wine (S9, SD=0.521)."

**Limitations / Contradictions for Odin:**
- "Reliance on self-reported Likert scales may introduce bias."
- "Cross-sectional design prevents observation of behavioral changes over time."
- "Sample predominantly from Laguna, limiting geographic generalizability [unacknowledged]."

**Key takeaways:**
- "Financial attitude negatively predicts spending behavior (β=-0.176)."
- "42% of Filipino millennials spend over 41% of their income."
- "Financial literacy and attitude are strongly correlated (β=0.578)."

---


## A User Profile System for the Finance Platform of Commerce
**Filename:** `IA--Hu-et_al_summarized.md`  
**Authors:** Hu, Z.; Qiu, Y.; Hu, S.; Cheng, Z.; Qiu, S. (2024)  
**ID:** `10.1145/3718391.3718436`  
**Odin Topics:** 5.A, 5.C  

**TLDR:** User profiling integrates internal and external data to build a model and system for precise marketing, risk control, and decision-making in financial commerce platforms.

**Problem & Motivation:** Web information is too general to solve individual user needs. Product and service homogeneity reduce customer loyalty and increase churn. Big data enables user profiling to improve satisfaction and competitiveness.

**Approach (summary):**
- Data acquisition combines explicit user input and implicit logging of interactions and behavior patterns.
- Data processing includes word segmentation, filtering, and normalization to produce standardized data.
- Tags are categorized as fact tags (statistical) or model tags (business‑driven) with objective or subjective weighting.

**Key Findings (selected):**
- User profiling enables precise marketing, risk control, and informed decision‑making in financial institutions.
- K‑means clustering can effectively group users with similar characteristics or behaviors for targeted analysis.
- Cross‑industry data integration enriches user profiles, improving accuracy and creating a virtuous cycle for model improvement.

**Limitations / Contradictions for Odin:**
- "No quantitative validation of profiling accuracy or business impact. [unacknowledged]"
- "K‑means assumes spherical clusters and requires choosing K, which may not suit all user data. [unacknowledged]"
- "Data integration across industries raises privacy and consent issues not discussed. [unacknowledged]"

**Key takeaways:**
- "User profiling combines explicit and implicit data for comprehensive insights."
- "Four‑layer architecture separates collection, storage, processing, and visualization."
- "Tag management with fact and model tags enables flexible user segmentation."

---


## Family Income in Relation to Budgeting of Accounting Students in A University
**Filename:** `L--Jumawan-Powao-et_al_summarized.md`  
**Authors:** Jumawan-Powao, A. R.; Tubat, K. T.; Cellero, R. C. L.; Alibangbang, A. D. C.; Capilitan, M. K. T. (2024)  
**ID:** `10.11594/ijmaber.05.08.03`  
**Odin Topics:** 3.A, 5.A, 7.A, 13.A  

**TLDR:** Family income positively correlates with allowance but inversely relates to budgeting among accounting students, with no significant sex difference in budgeting practices.

**Problem & Motivation:** College students face growing financial management challenges, yet the relationship between family income and student budgeting remains underexplored, especially for dependents. Previous studies failed to highlight students as non‑earners while addressing sex differences. This study investigates how family income affects budgeting behavior and whether sex moderates this relationship.

**Approach (summary):**
- Quantitative descriptive‑correlation design with random sampling using Slovin’s formula.
- Sample of 269 accounting students from Jose Rizal Memorial State University.
- Modified survey questionnaire with 4‑point Likert scale measuring budgeting across fixed expenses, flexible expenses, and savings.

**Key Findings (selected):**
- num: Students from lower‑income families demonstrate stronger budgeting practices than those from higher‑income families.
- No significant difference in budgeting between male and female respondents (p = 0.709).
- Allowance amount is significantly related to budgeting behavior, with lower allowance associated with more careful budgeting (p = 0.001).
- Family income shows a significant positive correlation with student allowance (r = 0.265, p = 0.001).

**Limitations / Contradictions for Odin:**
- Sample confined to accounting students, limiting generalizability to non‑accounting majors. [unacknowledged]
- Self‑reported Likert scale data may not reflect actual spending behavior. [unacknowledged]
- No longitudinal tracking of budgeting changes over time.

**Key takeaways:**
- Lower family income correlates with stronger student budgeting.
- Sex does not affect budgeting behavior in this sample.
- Students prioritize savings over flexible spending.

---


## The Mediation of Financial Behavior to Financial Literacy and Spending Habits of Gen Z: An Exploratory Factor Analysis
**Filename:** `L--Rodriguez_summarized.md`  
**Authors:** Rodriguez, J. M. P.; Labong, M. D. C. G.; Palallos, L. Q. (2024)  
**ID:** `10.20944/preprints202409.1696.v1`  
**Odin Topics:** 1.A, 1.C, 5.A  

**TLDR:** Financial literacy directly increases spending habits, and financial behavior partially mediates this relationship among Gen Z in the Philippines.

**Problem & Motivation:** Understanding how financial literacy translates into actual spending is poorly understood for Gen Z. Prior research shows that financial knowledge alone does not guarantee responsible spending. The mediating role of financial behavior remains underexplored in this demographic.

**Approach (summary):**
- Data from 317 Gen Z respondents (aged 18-25) across four barangays in Quezon City, Philippines.
- Structured questionnaire measured financial literacy, financial behavior, and spending habits using validated scales.
- Applied Pearson correlation, regression, mediation analysis (bootstrapped CIs), and Structural Equation Modeling.

**Key Findings (selected):**
- "num: Pearson's r = 0.821 between financial literacy and spending habits (p < .001)."
- "num: Direct effect of financial literacy on spending is 0.642 (p < .001)."
- "num: Indirect mediation effect through financial behavior is 0.180 (p < .001, 95% CI 0.114 to 0.245)."
- Financial literacy explains 51.9% of variance in financial behavior (R²=0.519).

**Limitations / Contradictions for Odin:**
- "Sample size of 317 from only 4 barangays limits generalizability."
- "Cross-sectional design cannot confirm mediation temporally [unacknowledged]."
- "AVE below 0.5 for spending and literacy indicates weak convergent validity [unacknowledged]."

**Key takeaways:**
- "Financial behavior mediates 22% of literacy's effect on spending."
- "Literacy explains 52% of variance in financial behavior among Gen Z."
- "SEM path from behavior to spending is 0.797, larger than direct literacy path 0.642."

---


## ASSESSING THE FINANCIAL LITERACY OF SENIOR HIGH SCHOOL AND COLLEGE STUDENTS: A COMPREHENSIVE ANALYSIS
**Filename:** `L--Dela_Rama-et_al_summarized.md`  
**Authors:** Dela Rama, K. A.; Baylon, F.; Balwet, L. F.; Pullos, K. E.; Durias, R. C.; Cabusca, J. F.; Eguia, A. L.; Cabilin, L. M.; Duran, R.; Mante, J.; Prepecio, D.; Gilongos, C. J.; Rosel, M. (2024)  
**ID:** `f4e5d6c7-b8a9-4c2d-9e1f-3a4b5c6d7e8f`  
**Odin Topics:** 1.A, 1.C, 5.A, 7.A, 13.A, 13.B  

**TLDR:** Senior high school and college students at a Philippine institution show basic financial knowledge but gaps in compound interest and investment, with moderate savings behavior and inconsistent budgeting.

**Problem & Motivation:** Financial literacy among young Filipino students is understudied, yet critical for economic stability. Existing research focuses on adults, leaving gaps in understanding formative financial development. Without targeted assessment, educational policies cannot address practical skill deficiencies.

**Approach (summary):**
- Quantitative survey of 345 randomly stratified students at Colegio de San Francisco Javier during 2023-2024.
- Adapted OECD/INFE questionnaire with 4-point Likert scale measuring financial knowledge and behavior (savings, budgeting, borrowing).
- Data collected online; pilot study yielded Cronbach's alpha of 0.85.

**Key Findings (selected):**
- "num: Total weighted mean financial knowledge score 2.10 for SHS and 2.11 for college on a 4-point scale."
- Less than 30% of respondents could accurately explain compound interest.
- Budgeting practices are less consistent than saving behaviors; few students consider inflation in long-term planning.
- No significant gender differences in financial literacy were found across any dimension.

**Limitations / Contradictions for Odin:**
- "Sample limited to a single private institution in Mindanao; may not represent all Filipino students."
- "Self-reported survey data subject to social desirability bias. [unacknowledged]"
- "No validation of financial literacy measures against actual financial outcomes. [unacknowledged]"

**Key takeaways:**
- "Only 30% of students can explain compound interest."
- "No gender gap in financial literacy among this sample."
- "Budgeting practices are less consistent than saving behaviors."

---


## A Phenomenological Reflection on Ubos-Biyaya and Petsa de Peligro: Capitalism’s Impact on Filipino Attitude of Spending and Church’s Proposition for an Inclusive Economy
**Filename:** `L--Canete-&-Liwanag_summarized.md`  
**Authors:** Canete, J. J. O.; Liwanag, L. A. L. (2024)  
**ID:** `f0e1d2c3-b4a5-6c7d-8e9f-0a1b2c3d4e5f`  
**Odin Topics:** 1.C, 2.A, 2.B, 5.A  

**TLDR:** Ubos-biyaya, the Filipino tendency to spend all resources impulsively, leads to petsa de peligro (pre-payday financial distress) as a consequence of capitalism's planned obsolescence and consumer culture.

**Problem & Motivation:** The paper identifies a gap in understanding the root causes of Filipino spending behaviors ubos-biyaya (resource depletion) and petsa de peligro (pre-payday financial strain). It argues that these are not mere individual failings but preconditioned outcomes of capitalism’s planned obsolescence and consumer culture. The motivation is to advocate for an inclusive economy from a Catholic social teaching perspective.

**Approach (summary):**
- Phenomenological reflection on Filipino spending behaviors using literature review and personal interviews.
- Connects ubos-biyaya to planned obsolescence and cathedrals of consumption via theoretical synthesis.
- Examines Church teachings (Pope Francis, John Paul II) on capitalism and the economy of exclusion.

**Key Findings (selected):**
- "num: 87% of Filipinos buy more than planned compared to 75% of Americans."
- Ubos-biyaya is a preconditioned outcome of planned obsolescence designed by capitalism.
- Petsa de peligro emerges as an upshot of ubos-biyaya and impulsive buying behavior.
- Capitalism creates an economy of exclusion that reduces persons to commodities.

**Limitations / Contradictions for Odin:**
- The paper's phenomenological method lacks generalizable empirical evidence. [unacknowledged]
- It does not address potential individual differences in spending behavior. [unacknowledged]
- The proposed economy of inclusion is not operationalized for practical implementation.

**Key takeaways:**
- 87% of Filipinos exhibit impulsive buying behavior.
- Ubos-biyaya is preconditioned by planned obsolescence.
- Petsa de peligro follows payday spending sprees.

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
- "num: Extreme lockdowns increased informal employment probability by 1.7 percentage points for women but not for men."
- "num: Female fixed-term labor market entrants had a 19% lower first birth hazard within 10 years."
- "num: Male recession entrants had a 23% lower first birth hazard within 10 years."
- "Upper service class members have strongly elevated second birth rates compared to semi-/unskilled workers."

**Limitations / Contradictions for Odin:**
- "LFS data undercounts informal employment, potentially underestimating lockdown effects."
- "Analysis in Chapter 3 limited to first 10 years post-entry due to sample attrition."
- "Vignette experiment measures ascribed intentions, not actual fertility behavior. [unacknowledged]"

**Key takeaways:**
- "Extreme lockdowns increased women's informal employment by 1.7 percentage points."
- "Fixed-term entry reduces first birth hazard for women by 19% over 10 years."
- "Male recession entrants have 23% lower first birth hazard within a decade."

---


## The Mediation of Financial Behavior to Financial Literacy and Spending Habits of Gen Z: An Exploratory Factor Analysis
**Filename:** `L--Rodriguez-et_al_summarized.md`  
**Authors:** Rodriguez, J. M. P.; Labong, M. D. C. G.; Palallos, L. Q. (2024)  
**ID:** `10.20944/preprints202409.1696.v1`  
**Odin Topics:** 1.C, 5.A, 7.A, 13.A  

**TLDR:** Financial behavior mediates the relationship between financial literacy and spending habits among Gen Z, with significant direct and indirect effects.

**Problem & Motivation:** Understanding how financial literacy translates into actual spending behavior remains poorly understood, especially for Gen Z. Existing research shows financial literacy is associated with spending, but the mediating role of financial behavior has been underexplored. This study addresses the gap by examining mediation effects.

**Approach (summary):**
- Data from 317 Gen Z respondents aged 18-25 in Quezon City using stratified random sampling.
- Structured questionnaire measuring financial literacy, financial behavior, and spending habits based on validated scales.
- Pearson correlation, regression analysis, mediation analysis, and Structural Equation Modeling (SEM).

**Key Findings (selected):**
- "num: Pearson correlation r=0.821 (p<0.001) between financial literacy and spending habits."
- "num: Direct effect of financial literacy on spending is 0.642 (p<0.001)."
- "num: Indirect mediation effect through financial behavior is 0.180 (p<0.001)."
- "num: Total effect of financial literacy on spending is 0.821."

**Limitations / Contradictions for Odin:**
- "Sample restricted to Gen Z in Quezon City, limiting generalizability to other regions or age groups."
- "Self-reported questionnaire data may introduce social desirability or recall bias."
- "Reliability for financial literacy construct (Cronbach's α=0.6568) is below the commonly accepted 0.70 threshold. [unacknowledged]"

**Key takeaways:**
- "Financial behavior mediates 18% of literacy's effect on spending."
- "Financial literacy explains 51.9% of variance in financial behavior."
- "Higher financial literacy correlates with more spending (r=0.821)."

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

**Limitations / Contradictions for Odin:**
- Sample size constraints limit generalizability beyond Batam City.
- Self-reporting biases in survey responses may affect validity.
- Subjective nature of qualitative data introduces potential interpretation bias.

**Key takeaways:**
- Financial literacy alone does not guarantee prudent financial decisions due to lifestyle pressures.
- Urban living and peer influence are key determinants of young workers' financial behaviors.
- Tailored financial education should bridge theory and practical application.

---


## User Profiling Based on Financial Transaction Patterns: A Clustering Approach for User Segmentation
**Filename:** `IA--Pratama-&-Putri_summarized.md`  
**Authors:** Pratama, S. F.; Putri, N. A. (2024)  
**ID:** `10.47738/ijaim.v4i4.92`  
**Odin Topics:** 5.A, 5.C  

**TLDR:** K-means clustering on transaction amounts, times, and types identifies three user segments with distinct spending behaviors, achieving a moderate Silhouette Score of 0.33.

**Problem & Motivation:** Traditional user segmentation methods rely on predefined categories or historical data, missing nuanced behavioral patterns. The increasing complexity and diversity of transaction data require advanced techniques to capture hidden patterns. Without such techniques, financial institutions cannot fully personalize services or target marketing effectively.

**Approach (summary):**
- Data source: Simulated financial transaction dataset from Kaggle, generated with Python Faker, containing transaction ID, amount, type, customer ID, and timestamp.
- Preprocessing: Imputed missing numerical values using mean/median, categorical with mode; removed rows with excessive missingness.
- Feature extraction: Derived hour, day of week, and month from transaction_time; scaled amount via Min-Max; encoded transaction_type using one-hot or label encoding.

**Key Findings (selected):**
- num: Silhouette Score of 0.33 indicates moderate cluster separation with some overlap.
- Three clusters identified: Cluster 0 (mean amount 1876.92, purchases, early week, ~11:15 AM), Cluster 1 (mean amount 4147.06, transfers, mid-week, ~1:35 PM), Cluster 2 (mean amount 1970.00, purchases, late week, ~11:20 AM).
- num: Cluster 2 has the highest transaction count (just over 20), followed by Cluster 1 (~17), then Cluster 0 (under 15).
- Transaction day of week distinguishes purchase behavior: Mondays (Cluster 0), Wednesdays (Cluster 1), Fridays (Cluster 2).

**Limitations / Contradictions for Odin:**
- "The dataset is simulated and limited to one month, which may not generalize to real-world multi-year transaction histories. [unacknowledged]"
- "Moderate Silhouette Score (0.33) indicates clusters are not well-separated, but the paper acknowledges this as a limitation."
- "No validation with external criteria (e.g., user survey or downstream task performance) to confirm cluster utility."

**Key takeaways:**
- "K-means clustering achieved a Silhouette Score of 0.33."
- "Cluster 1 had highest mean transaction amount at 4147.06."
- "Transaction day of week distinguishes purchase from transfer behavior."

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
- num: Many participants saved at least 30% of their monthly salary or pocket money.
- Participants used saving-centric or spending-centric budgeting approaches, aided by digital apps, parental monitoring, and mental bucketing.
- Spending was modest, with basic needs prioritized; strategies included deferred purchase, bargain shopping, and one-time lump-sum payments.
- Spending philosophies included differentiating needs from wants, using spending as work incentive, and YOLO enjoyment.

**Limitations / Contradictions for Odin:**
- "Sample was generally well-educated (half had bachelor's degree) and English-proficient, limiting generalizability to less educated or non-English-speaking ethnic minorities. [unacknowledged]"
- "Small qualitative sample size (n=53) does not allow broad generalization."
- "Ethnic Chinese young adults were not included, preventing comparison."

**Key takeaways:**
- "Many young adults saved at least 30% of monthly income."
- "Family social capital strongly influences financial habits through monitoring and role modeling."
- "Informal borrowing from family and friends is common and often interest-free."

---


## Peer Influence and Adolescent Spending: Insights into High School Students' Buying Behavior
**Filename:** `L--Anaya-et_al_summarized.md`  
**Authors:** Anaya, K. K. O.; Piquero, J. R. M.; Romero, C. J. P.; Sales, Y. L. M.; Suñga, P. A. N.; Ibañez, M. M.; Ramos, R. I. A.; Asi, G. M. (2024)  
**ID:** `8a7b6c5d-4e3f-4a2b-9c1d-2e3f4a5b6c7d`  
**Odin Topics:** 5.A  

**TLDR:** Implicit peer pressure correlates weakly with impulsive buying (r=0.273) among Filipino senior high school students, accounting for 7.45% of variance.

**Problem & Motivation:** Limited research directly links implicit peer pressure to impulsive buying among Filipino senior high school students. Foreign studies may not generalize across cultural contexts and age groups. Addressing this gap can inform interventions to improve students' financial decisions.

**Approach (summary):**
- Descriptive-correlational survey of 108 senior high school students from a faith-based institution in Cavite, Philippines.
- Implicit peer pressure measured using Chang et al. (2019) questionnaire; impulsive buying using modified Kim (2003) and Borromeo et al. (2022) scales.
- Data analyzed with Jamovi using means, standard deviations, Pearson correlation, and linear regression.

**Key Findings (selected):**
- "num: Implicit peer pressure level was low (mean 2.24, SD 0.67 on 1-5 scale)."
- "num: Impulsive buying extent was moderate (mean 3.06, SD 0.84)."
- "num: Pearson correlation between implicit peer pressure and impulsive buying was 0.273 (p=.004), a weak positive relationship."
- "num: Implicit peer pressure explained only 7.45% of variance in impulsive buying (R²=0.0745)."

**Limitations / Contradictions for Odin:**
- "Small sample size (n=108) from one faith-based institution limits generalizability to other populations."
- "Self-report questionnaires may be subject to recall and social desirability bias [unacknowledged]."
- "The study did not control for income, parental influence, or digital spending contexts."

**Key takeaways:**
- "Implicit peer pressure correlates weakly (r=0.273) with impulsive buying."
- "Peer pressure explains only 7.45% of impulsive buying variance."
- "Filipino senior high students show low implicit peer pressure (mean 2.24/5)."

---


## Financial technology and financial capability: Study of the European Union
**Filename:** `I--Nourallah-et_al_summarized.md`  
**Authors:** Nourallah, M.; Öhman, P.; Hamati, S. (2024)  
**ID:** `10.1016/j.gfj.2024.101008`  
**Odin Topics:** 5.A, 9.A, 12.A, 13.A, 13.B  

**TLDR:** FinTech positively affects financial capability in EU countries, measured via skills, debt, saving, resilience, and well-being.

**Problem & Motivation:** Household financial capability is important but understudied in the EU, with no standard measurement. Prior measures rely naively on financial access and knowledge. This paper addresses the gap by proposing a multidimensional measure and testing FinTech's role.

**Approach (summary):**
- Three waves (2014, 2017, 2021) of Global Findex and Eurostat panel data for 24 EU countries.
- Financial capability is the arithmetic mean of skills, debt, saving, financial resilience, and financial well-being.
- FinTech is the arithmetic mean of received digital payments, made digital payments, mobile utility payments, and internet use frequency.

**Key Findings (selected):**
- num: FinTech has a significant positive effect on financial capability (coefficient 0.277, p<0.01) in the full fixed-effects model.
- num: Human Development Index positively affects financial capability (coefficient 1.189, p<0.05), while income and financial freedom show no significant effect.
- num: Hungary and Latvia had the highest financial capability growth from 2014-2021 at 34.3% and 25.5%, respectively.
- num: Sweden, Finland, and Estonia top the FinTech rankings in 2021 with scores 0.868, 0.823, and 0.809 out of 1.

**Limitations / Contradictions for Odin:**
- "Cross-country panel data may mask individual-level heterogeneity [unacknowledged]."
- "Three waves (2014-2021) limit dynamic analysis of long-term FinTech effects [acknowledged]."
- "No exploration of socioeconomic variables such as age or education [acknowledged]."

**Key takeaways:**
- FinTech adoption increases financial capability by 0.277 points on a 0-1 scale.
- Financial capability requires five dimensions: skills, debt, saving, resilience, well-being.
- Income alone does not predict financial capability.

---


## Behavioral Factors in Loan Default Prediction: A Literature Review on Psychological and Socioeconomic Risk Indicators
**Filename:** `IA--Maruf-et_al_summarized.md`  
**Authors:** Al Maruf, A.; Kowsar, M. M.; Mohiuddin, M.; Mohna, H. A. (2024)  
**ID:** `10.63125/0jwtbn29`  
**Odin Topics:** 5.A, 5.C, 13.B  

**TLDR:** A systematic review of 67 studies finds that psychological traits like impulsivity and overconfidence, along with socioeconomic vulnerabilities such as income volatility and low financial literacy, significantly predict loan default, challenging traditional credit scoring models.

**Problem & Motivation:** Traditional credit risk models rely on quantitative metrics and neglect behavioral and contextual variables, leading to inaccurate predictions. The 2008 financial crisis highlighted this gap, as widespread defaults were underestimated. A multidimensional framework incorporating psychological and socioeconomic factors is needed for comprehensive credit assessment.

**Approach (summary):**
- Conducted a systematic literature review following PRISMA 2020 guidelines.
- Searched Scopus, Web of Science, PsycINFO, EconLit, ScienceDirect, and Google Scholar for peer-reviewed studies published 2010-2024.
- Included 67 studies examining psychological traits (impulsivity, overconfidence, time inconsistency) or socioeconomic characteristics (income volatility, education, household size) influencing individual loan default.

**Key Findings (selected):**
- "num: 43 of 67 reviewed articles identified psychological traits as significant predictors of loan default."
- "num: 39 of 67 studies found low financial literacy correlated with higher default rates."
- "num: 51 of 67 studies confirmed socioeconomic conditions, especially income volatility, as critical determinants."
- "num: Behavioral interventions (nudges, reminders, financial training) reduced default rates by 12% to 28% in randomized controlled trials."

**Limitations / Contradictions for Odin:**
- "Systematic review may have publication bias toward significant findings."
- "Geographical and cultural diversity of included studies limits generalizability to Filipino young professionals [unacknowledged]."
- "The review does not quantify pooled effect sizes or conduct meta-analysis."

**Key takeaways:**
- "43 of 67 studies link psychological traits to loan default risk."
- "Behavioral nudges cut default rates by 12% to 28%."
- "Income volatility predicts default more strongly than credit scores."

---


## Adaptive Financial Literacy Enhancement through Cloud-Based AI Content Delivery: Effectiveness and Engagement Metrics
**Filename:** `IA--Li-et_al_summarized.md`  
**Authors:** Li, M.; Liu, W.; Chen, C. (2024)  
**ID:** `f47ac10b-58cc-4372-a567-0e02b2c3d479`  
**Odin Topics:** 5.A, 10.A, 10.B, 11.A, 11.B, 12.A, 12.B, 13.A, 13.B  

**TLDR:** Cloud-based AI adaptive learning for financial literacy improves knowledge acquisition (+37.8% vs +19.2%) and financial behaviors like savings (+24.3%) and debt reduction (-18.6%) over 12 months.

**Problem & Motivation:** Financial literacy rates remain persistently low globally, with only 33% of adults classified as financially literate. Traditional content delivery fails to account for individual learning preferences, resulting in suboptimal knowledge transfer and engagement. Limited personalization and rapid knowledge decay necessitate adaptive approaches.

**Approach (summary):**
- Data from 15,000 users across three Southeast Asian countries.
- Recurrent neural networks process temporal user interaction sequences for personalized content delivery.
- Bayesian knowledge tracing and reinforcement learning optimize content sequencing and adaptation.

**Key Findings (selected):**
- "num: Adaptive platform achieved 37.8% knowledge gain vs 19.2% for traditional methods."
- "num: Savings rates increased by 24.3% at 12-month follow-up."
- "num: Investment diversification improved by 31.7% and debt reduced by 18.6%."
- Sequential pattern analysis predicts knowledge acquisition success with 78.3% accuracy.

**Limitations / Contradictions for Odin:**
- No discussion of demographic representativeness. [unacknowledged]
- Potential self-selection bias in user sample. [unacknowledged]
- Absence of cost-benefit analysis for implementation. [unacknowledged]

**Key takeaways:**
- Adaptive AI increased financial knowledge by 37.8% over traditional methods.
- Savings rates rose 24.3% and debt fell 18.6% at 12-month follow-up.
- Engagement profiles predict learning success with 78.3% accuracy.

---


## How and when does a used (vs. unused) account affect consumption behavior?
**Filename:** `I--Yin_summarized.md`  
**Authors:** Yin, S.; Sharif, M. A. (2024)  
**ID:** `10.1037/xge0001541`  
**Odin Topics:** 5.A, 3.A, 7.A  

**TLDR:** Consumers are more likely to spend remaining resources from a used account than from an unused account with the same absolute amount because they value the resources less.

**Problem & Motivation:** No prior research has examined how the mere fact that an account has been used (vs. unused) influences future spending, holding absolute balance constant. Understanding this effect is important for predicting consumer behavior in gift cards, checking accounts, and reward programs. The gap is a lack of empirical evidence on within-account relative comparisons and their behavioral consequences.

**Approach (summary):**
- Seven experimental studies (total N = 8,667) using MTurk and Prolific participants in the US.
- Manipulated used accounts (e.g., $10 left from $100 gift card) versus unused accounts ($10 gift card) across gift cards, checking accounts, and credit card reward points.
- Measured spending likelihood (0-100 scale) and perceived valuation (0-100 scale) as mediator.

**Key Findings (selected):**
- "num: Participants were more likely to spend from a used vs. unused gift card (60.6 vs. 44.8, d = 0.44, p < .001)."
- "num: Valuation significantly mediated the used vs. unused effect on spending (a´b = -0.91, 95% CI [-1.96, -0.025])."
- "num: The effect strengthened as the proportion remaining decreased: spending likelihood dropped 7.99 points per 20% decrease in remaining proportion in used accounts (p < .001)."
- When no original amount was specified, participants spent as if the account was used, not unused.

**Limitations / Contradictions for Odin:**
- "Results may not generalize to non-US cultures or languages. [unacknowledged]"
- "The effect was not tested with very large account sizes (e.g., thousands of dollars). [unacknowledged]"
- "Studies primarily used forced-choice spending scenarios; real-world longitudinal behavior not observed."

**Key takeaways:**
- "Used accounts increase spending likelihood by 15-16 percentage points over unused accounts."
- "Lower perceived valuation of remaining resources mediates the used-account effect."
- "Spending rises as the remaining proportion drops from 60% to 20% in used accounts."

---


## Effects of Filipino Consumers’ Financial Attitudes, Subjective Norms, and Perceived Behavioral Control on Intentions to Formal Banking: Towards Financial Inclusion
**Filename:** `L--Co-&-Centeno_summarized.md`  
**Authors:** Co, M.; Centeno, D.D.G. (2023)  
**ID:** `c5a2e4b7-9d8f-4c3a-8e1b-6f4d2a9c7e3b`  
**Odin Topics:** 1.C, 5.A, 13.A  

**TLDR:** Filipino consumers' intentions to save surplus money in formal banks are significantly predicted by subjective norms and perceived behavioral control, but not by attitudes.

**Problem & Motivation:** Financial exclusion in the Philippines is often attributed to cost and lack of funds, yet attitudinal and psychological factors remain underexplored. Understanding how attitudes, social influences, and perceived control affect banking intentions can improve financial inclusion strategies. This study addresses the gap by applying the Theory of Planned Behavior to a national consumer finance survey.

**Approach (summary):**
- Data from the Bangko Sentral ng Pilipinas Consumer Financial Survey 2014 with 15,503 randomly sampled households.
- Dependent variable is intention to put surplus money in a bank deposit account (binary).
- Independent variables include attitude toward banking, subjective norm (household member with bank account), and perceived behavioral control (two items on earning and saving enough).

**Key Findings (selected):**
- "num: Having a banked household member increases intention probability by 10.16% (p<0.001)."
- "num: Perceived ability to earn enough to save regularly increases intention probability by 1.42% per unit (p=0.024)."
- "num: College graduates have 7.95% higher probability of intention than non-college graduates (p<0.001)."
- "num: Males have 2.02% higher probability of intention than females (p=0.030)."

**Limitations / Contradictions for Odin:**
- "Cross‑sectional design limits causal inference."
- "Data from 2014 may be outdated for current financial behavior."
- "Self‑reported intentions may not translate to actual behavior."

**Key takeaways:**
- "Subjective norms from household members increase banking intention by 10.16%."
- "Perceived ability to earn enough money predicts savings intention."
- "Attitudes alone do not significantly predict banking intentions."

---


## User Cold Start Problem in Recommendation Systems: A Systematic Review
**Filename:** `LA--Yuan-et_al_summarized.md`  
**Authors:** Yuan, H.; Hernandez, A.A. (2023)  
**ID:** `10.1109/ACCESS.2023.3338705`  
**Odin Topics:** 4.B, 5.A, 5.B, 5.C, 6.A, 10.A, 10.B, 11.A, 12.A, 12.B  

**TLDR:** A systematic review of 45 papers (2016-2023) categorizes user cold start solutions into data-driven and method-driven approaches, analyzing evaluation metrics and future directions.

**Problem & Motivation:** Existing systematic reviews on user cold start are scarce, outdated, or fail to distinguish between user and item cold start problems. Solutions for these two problems differ, yet prior work often conflates them. A focused, up-to-date review is needed to guide researchers.

**Approach (summary):**
- Followed systematic literature review guidelines (Kitchenham 2007) with seven steps: research questions, search strings, database selection (IEEE, ACM, Web of Science), inclusion/exclusion criteria, paper search, pre-selection, full reading, and classification.
- Search strings combined terms like "recommendation system", "user cold start", and "cold start".
- 1480 papers initially retrieved; after title/abstract screening and inclusion/exclusion criteria, 45 papers from 2016-2023 were selected for deep analysis.

**Key Findings (selected):**
- num: 45 papers were selected from 1480 initial search results, with the highest number (11) published in 2020.
- Data-driven strategies commonly use cross-domain and social network data to provide additional user information for cold-start users.
- Method-driven strategies increasingly apply meta-learning, deep learning (DNN, GNN, GAN), and attention mechanisms to learn from limited user interactions.
- num: Most literature (over 70% of analyzed papers) uses ranking metrics such as NDCG@K and Hit@K for evaluation, rather than rating prediction metrics.

**Limitations / Contradictions for Odin:**
- "No experimental validation of the surveyed methods. [unacknowledged]"
- "Only 45 papers analyzed; may not capture all recent advances."
- "Does not address domain-specific challenges of personal finance systems. [unacknowledged]"

**Key takeaways:**
- "45 papers from 2016-2023 were analyzed for user cold start."
- "Data-driven and method-driven are the two main solution categories."
- "Meta-learning and deep learning are increasingly applied to cold start."

---


## Rotating savings and credit associations: A scoping review
**Filename:** `I--Zambrano-et_al_summarized.md`  
**Authors:** Zambrano, A.F.; Giraldo, L.F.; Perdomo, M.T.; Hernández, I.D.; Godoy, J.M. (2023)  
**ID:** `10.1016/j.wds.2023.100081`  
**Odin Topics:** 1.C, 2.A, 5.A, 11.A, 13.A, 13.B  

**TLDR:** A scoping review of 96 papers on Rotating Savings and Credit Associations finds financial and non‑financial benefits, risks like defection, and opportunities for technological support and formalization.

**Problem & Motivation:** Despite decades of research on ROSCAs worldwide, no systematic scoping review has synthesized recent findings on their benefits, risks, and operational mechanisms. Understanding these informal financial arrangements is crucial for leveraging them in development and financial inclusion. The lack of a structured overview limits evidence‑based interventions.

**Approach (summary):**
- Used the PRISMA‑ScR protocol to systematically map ROSCA research from January 2000 to July 2022.
- Searched Scopus and Web of Science, screening 227 publications to include 96 peer‑reviewed journal or conference papers in English.
- Extracted data on continent/country of the studied ROSCA, methodological approaches, keywords, and key conclusions.

**Key Findings (selected):**
- num: 96 papers were included in the scoping review.
- Asia and Africa are the most studied continents; South America and Oceania have no primary data studies since 2000.
- ROSCAs provide non‑financial benefits including social capital, health improvements, and women’s empowerment beyond pure financial gains.
- Defection risk is mitigated by social sanctions, reputation mechanisms, and heavy economic penalties; without sanctions, sustainability is theoretically impossible.

**Limitations / Contradictions for Odin:**
- "Only peer‑reviewed articles in English from Scopus and Web of Science were included, potentially missing grey literature or non‑English studies. [unacknowledged]"
- "No primary data from South America or Oceania, limiting generalizability to those regions (acknowledged by authors as a research gap)."
- "Few intervention studies exist; most findings are observational or simulation‑based, reducing actionable causal claims (acknowledged in future directions)."

**Key takeaways:**
- "96 papers on ROSCAs from 2000‑2022 show both financial and social benefits."
- "Social pressure and embarrassment enforce saving discipline better than interest rates."
- "Defection risk is minimized by reputation screening and mobile transparency tools."

---


## Impact of financial literacy, mental budgeting and self control on financial wellbeing: Mediating impact of investment decision making
**Filename:** `I--Bai_summarized.md`  
**Authors:** Bai, R. (2023)  
**ID:** `10.1371/journal.pone.0294466`  
**Odin Topics:** 3.A, 5.A  

**TLDR:** Financial literacy, mental budgeting, and self-control positively affect subjective financial wellbeing, with investment decision making partially mediating these relationships.

**Problem & Motivation:** Financial stress harms mental health and productivity. Understanding cognitive factors like financial literacy, mental budgeting, and self-control that influence subjective financial wellbeing is needed. The mediating role of investment decision making in these relationships has not been fully examined.

**Approach (summary):**
- Data were collected from 449 Chinese university students via convenience sampling using physical and electronic channels.
- The study employed Partial Least Squares Structural Equation Modeling (PLS-SEM) for path analysis and mediation testing.
- Financial literacy was measured with 7 items, mental budgeting with 4 items, and self-control with 5 items from the Brief Self-Control Scale.

**Key Findings (selected):**
- num: Financial literacy has a direct positive effect on financial wellbeing (beta = 0.299, p < 0.001).
- num: Mental budgeting has a direct positive effect on financial wellbeing (beta = 0.102, p < 0.001).
- num: Self-control has a direct positive effect on financial wellbeing (beta = 0.182, p < 0.001).
- num: Investment decision making partially mediates the effect of financial literacy on financial wellbeing (indirect effect = 0.017, p = 0.034).

**Limitations / Contradictions for Odin:**
- Student sample limits generalizability to broader populations.
- Cross-sectional design cannot establish causality.
- Self-reported measures may be subject to social desirability bias.

**Key takeaways:**
- Financial literacy has direct beta 0.299 on financial wellbeing.
- Mental budgeting directly improves financial wellbeing.
- Self-control influences financial wellbeing via investment decisions.

---


## A machine learning ensemble approach to predicting factors affecting the intention and usage behavior towards online groceries applications in the Philippines
**Filename:** `LA--Gumasing-et_al_summarized.md`  
**Authors:** Gumasing, M.J.J.; Ong, A.K.S.; Sy, M.A.P.C.; Prasetyo, Y.T.; Persada, S.F. (2023)  
**ID:** `10.1016/j.heliyon.2023.e20644`  
**Odin Topics:** 1.C, 5.A, 6.A, 11.A, 12.B  

**TLDR:** A machine learning ensemble of random forest and artificial neural network predicts that perceived benefits, perceived vulnerability, behavioral intention, performance expectancy, and perceived severity strongly influence online grocery app usage among Filipino consumers during COVID-19.

**Problem & Motivation:** Despite the rise of online grocery shopping in the Philippines during COVID-19, factors driving consumer intention and usage behavior remain underexplored. Existing studies using traditional statistical methods have limitations in capturing complex, nonlinear relationships. A holistic measurement integrating health concerns and technology acceptance is needed.

**Approach (summary):**
- Data from 373 Filipino online grocery consumers collected via 5-point Likert survey.
- Integrated Protection Motivation Theory (PMT) and Unified Theory of Acceptance and Use of Technology (UTAUT2) with 11 latent variables.
- Used Random Forest Classifier (optimized over 6400 runs with depth 6, 90:10 train-test split, 96% accuracy).

**Key Findings (selected):**
- "num: Random Forest achieved 96% accuracy with 0.00 standard deviation at depth 6."
- "num: Artificial Neural Network achieved 96.63% average testing accuracy."
- Perceived benefit is the most significant factor (importance score 0.270), followed by perceived vulnerability (0.265) and behavioral intention (0.258).
- All ten constructs (performance expectancy, effort expectancy, social influence, hedonic motivation, facilitating conditions, perceived benefit, perceived vulnerability, perceived severity, perceived susceptibility, response efficacy) significantly affect behavioral intention or usage behavior.

**Limitations / Contradictions for Odin:**
- Respondents majorly reside in highly urbanized cities, affecting technological literacy representation.
- Lack of consideration of socio-economic factors for customer segmentation.
- No validation of model generalizability to other types of financial apps [unacknowledged].

**Key takeaways:**
- Perceived benefit is the strongest predictor of app usage behavior at 100% importance.
- Random Forest and ANN both achieved over 96% accuracy in predicting user behavior.
- Integration of health belief model with technology acceptance improves prediction for pandemic contexts.

---


## Financial Inclusion and the Role of Financial Literacy in the Philippines
**Filename:** `L--Deselo-&-Agner_summarized.md`  
**Authors:** Desello, J. M. U.; Agner, M. G. R. (2023)  
**ID:** `10.5539/ijef.v15n6p27`  
**Odin Topics:** 1.C, 5.A  

**TLDR:** Financial literacy positively predicts financial account ownership and use of financial services among Filipinos, with age, gender, income, and household decision-making role as key drivers.

**Problem & Motivation:** Financial inclusion is a national development agenda in the Philippines, but local studies linking financial literacy to inclusion using nationally representative data are scarce. Understanding the drivers of account ownership and service usage is necessary to bridge the inclusion gap and raise financial literacy levels.

**Approach (summary):**
- Data from Bangko Sentral ng Pilipinas 2019 Financial Inclusion Survey (n=1,200).
- Financial literacy measured with three-item quiz (inflation, simple interest, compound interest).
- Dependent variables: ownership of formal accounts (bank, e-money, cooperative, microfinance) and use of financial services (credit, investment, insurance).

**Key Findings (selected):**
- "num: A one-standard-deviation increase in financial literacy raises likelihood of account ownership by 3.7-4.2 percentage points."
- "num: A one-point increase in financial literacy score increases likelihood of availing a financial service by 4.9-6.0 percentage points."
- "num: Financial literacy increases bank account ownership by 2.1 percentage points and investment ownership by 3.7-4.2 percentage points."
- Awareness of BSP financial education programs and being the main household financial decision-maker are strong positive drivers of inclusion.

**Limitations / Contradictions for Odin:**
- "Uses only three financial literacy questions, which may not capture full construct (acknowledged)."
- "Cross-sectional design prevents causal inference [unacknowledged]."
- "Sample of 1,200 may not fully represent all Filipino subgroups [unacknowledged]."

**Key takeaways:**
- "Financial literacy raises account ownership by 3.7-4.2 percentage points."
- "Being main financial decision-maker increases service use by 24-34 percentage points."
- "Awareness of BSP programs strongly predicts bank account ownership."

---


## The Importance of Financial Literacy: Opening a New Field
**Filename:** `I--Lusardi-&-Mitchell_summarized.md`  
**Authors:** Lusardi, A.; Mitchell, O. S. (2023)  
**ID:** `10.1257/jep.37.4.137`  
**Odin Topics:** 5.A, 13.A, 13.B  

**TLDR:** Financial literacy, measured by the “Big Three” questions, is strikingly low globally, varies by demographics, and strongly predicts saving, debt management, and wealth accumulation.

**Problem & Motivation:** People face complex financial decisions at all life stages but often lack basic knowledge of interest, inflation, and risk. No nationally representative dataset measured financial literacy before 2004, leaving a gap in understanding its economic impact. This paper quantifies financial literacy and demonstrates its critical role in financial outcomes and wealth inequality.

**Approach (summary):**
- Designed and fielded the “Big Three” financial literacy questions (interest, inflation, risk diversification) in the 2004 Health and Retirement Study.
- Extended the measure to the “Big Five” and the 28‑question P‑Fin Index, adopted in over 40 countries and 140‑nation S&P Global survey.
- Used median regressions on 2019 Survey of Consumer Finances data (N=5,777) to correlate literacy with net, financial, and non‑financial wealth.

**Key Findings (selected):**
- “num: Only 43% of Americans answer all three Big Three questions correctly.”
- “num: 29% of women vs. 48% of men answer all three correctly; women are more likely to say ‘do not know’.”
- “num: Financial literacy follows a hump‑shaped age pattern, peaking at 50–59 years with ~50% correct, and is lowest among those under 30 (32%).”
- “num: One additional correct answer on the FinLit index is associated with 13% higher median net wealth, 24% higher financial wealth, and a 15% higher wealth/income ratio.”

**Limitations / Contradictions for Odin:**
- "Cross‑sectional data cannot distinguish age vs. cohort effects. [unacknowledged]"
- "Potential reverse causality: wealthier people may acquire more financial literacy. [unacknowledged]"
- "The Big Three may oversimplify financial knowledge, missing numeracy or advanced risk concepts."

**Key takeaways:**
- "Only 43% of US adults answer all three basic financial literacy questions correctly."
- "Financial literacy explains 30‑40% of wealth inequality near retirement."
- "Women and minorities have persistently lower financial literacy scores."

---


## Healthy financial habits in young adults: An exploratory study of the relationship between subjective financial literacy, engagement with finances, and financial decision-making
**Filename:** `I--Sinnewe-&-Nicholson_summarized.md`  
**Authors:** Sinnewe, E.; Nicholson, G. (2023)  
**ID:** `10.1111/joca.12512`  
**Odin Topics:** 1.C, 5.A, 5.B, 13.A, 13.B  

**TLDR:** Social context and financial hardship drive young adults' financial habits more than subjective financial literacy, with romantic partnerships shifting focus to long-term goals.

**Problem & Motivation:** Young adults face rising non-discretionary costs and housing unaffordability, yet evidence that financial education improves behavior is mixed. Understanding how financial habits form during the transition to full-time work is critical for designing effective interventions. Prior work overlooks the role of social context and motivation relative to literacy.

**Approach (summary):**
- Conducted 28 semi-structured interviews with Australian university graduates aged 21-31 who entered full-time work within the last 5 years.
- Used grounded theory with iterative open, axial, and selective coding guided by Theory of Planned Behavior and Family Financial Socialization.
- Interviews lasted 16.1 hours total, transcribed and coded by multiple researchers with debriefing sessions.

**Key Findings (selected):**
- "num: Participants in committed romantic relationships reported future-focused financial goals and formal budgeting, while singles focused on short-term wants."
- "num: Average subjective financial literacy self-rating was 6.4/10, yet literacy had minimal association with daily spending habits; motivation was the primary driver of engagement."
- "num: 21 of 28 participants saved money, 10 used a formal budget, and 21 had investments in shares or property."
- "num: Average financial satisfaction rating was 7.3/10, with satisfaction linked to having a budgeting system."

**Limitations / Contradictions for Odin:**
- "Small sample size (n=28) and homogeneous (university graduates) limit generalizability."
- "Self-selection bias: individuals with poor financial habits or high debt may have declined participation. [unacknowledged]"
- "Subjective financial literacy measure may not correlate strongly with objective literacy. [acknowledged in endnote 1]"

**Key takeaways:**
- "Romantic partnerships shift financial time horizon from present to future."
- "Subjective financial literacy has minimal effect on daily spending habits."
- "Only 10 of 28 young adults use a formal budget."

---


## Knowledge and Practice of Personal Finance of Non-Teaching Staff in a Private University in Cebu City
**Filename:** `L--Polinar-et_al_summarized.md`  
**Authors:** Rico, M. E.; Polinar, M. A. N.; Celada, J. A. (2023)  
**ID:** `10.11594/ijmaber.04.04.16`  
**Odin Topics:** 1.C, 5.A, 7.A, 13.A, 13.B  

**TLDR:** Non-teaching staff at a Philippine private university show moderate knowledge and practice of personal finance, with significant correlations for budgeting, saving, spending, insurance, and investment but not for emergency funds or debt management.

**Problem & Motivation:** The COVID-19 pandemic exposed weak financial resilience in the Philippines, where only 25% of adults understand basic financial concepts. Little research focuses on non-teaching staff’s personal finance knowledge and practice. This study examines their financial behavior to identify gaps and recommend improvements.

**Approach (summary):**
- Survey of 50 non-teaching staff using simple random sampling at a private university in Cebu City.
- Adopted questionnaire from Polinar (2022) measuring knowledge and practice of six indicators on a 4-point Likert scale.
- Indicators: budgeting, saving and spending, emergency fund, debt management, insurance, investment.

**Key Findings (selected):**
- num: Grand mean knowledge 3.10 (moderately knowledgeable) and grand mean practice 2.71 (moderately practiced).
- num: Budgeting knowledge-practice correlation r=0.939, p=0.002 (significant).
- num: Saving and spending correlation r=0.839, p=0.001 (significant).
- num: Insurance correlation r=0.969, p=0.001 (significant).

**Limitations / Contradictions for Odin:**
- "Small sample size (n=50) from a single private university in Cebu City limits generalizability."
- "Self-reported Likert scale data may overstate knowledge and practice due to social desirability bias."
- "Cross-sectional design cannot establish causality between knowledge and practice."

**Key takeaways:**
- "Knowledge-practice correlation is strong for budgeting (r=0.939) but absent for debt."
- "Emergency fund practice is less practiced (mean 2.42 out of 4)."
- "Investment has lowest practice (2.20) and knowledge (2.56)."

---


## "Data Science and Business Analytics Approaches to Financial Wellbeing: Modeling Consumer Habits and Identifying At-Risk Individuals in Financial Services"
**Filename:** `IA--Machireddy_summarized.md`  
**Authors:** "Machireddy, J." (2023)  
**ID:** `a1b2c3d4-e5f6-7890-1234-567890abcdef`  
**Odin Topics:** 5.A, 5.B, 5.C, 6.A, 8.A, 8.B, 10.A, 10.B, 13.B  

**TLDR:** "Data science models using transaction data and digital footprints can profile consumer financial behavior, identify at-risk individuals, and support ethical risk management through explainable AI."

**Problem & Motivation:** "Financial hardship from over-indebtedness and income volatility affects many consumers, leading to defaults and economic instability. Traditional credit scoring uses limited variables and static updates, failing to capture real-time behavioral signals. There is a need for data-driven approaches to model financial habits and detect early warning signs."

**Approach (summary):**
- "Extract behavioral features from transactional data including income volatility, discretionary spending percentage, and liquidity trends."
- "Apply machine learning models such as gradient boosting, hidden Markov models, and autoencoders for risk prediction and anomaly detection."
- "Incorporate psychological traits and contextual factors like life events and economic conditions to enrich consumer profiles."

**Key Findings (selected):**
- "Transactional and digital footprint data enable dynamic financial health portraits that shift in real time."
- "Machine learning models can detect early warning signs of financial distress such as income drops or rising credit reliance before default occurs."
- "Explainable AI techniques improve consumer trust and allow regulators to verify fair decision-making."
- "Consumer segmentation by financial vulnerability allows targeted interventions like debt relief or budgeting tools."

**Limitations / Contradictions for Odin:**
- "No empirical results or quantitative evaluation of proposed models."
- "Does not address the cold-start problem for new users with no transaction history."
- "Real-time streaming infrastructure requirements are assumed but not detailed."

**Key takeaways:**
- "Transaction data alone is insufficient; psychological and contextual factors improve risk models."
- "Explainable AI like SHAP is necessary for regulatory compliance and consumer trust."
- "Consumer segmentation enables targeted interventions such as debt restructuring or coaching."

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
- “num: 80% of millennial smartphone owners use their device for transactional financial purposes.”
- Smartphone apps that track spending and compare loan interest improve financial resilience after shocks.
- Digital nudging via mobile apps can increase salience of credit card transactions and reduce spending.
- Financial literacy helps mitigate the effect of mobile payment use on account overdrafts.

**Limitations / Contradictions for Odin:**
- "Only peer-reviewed journal articles from finance, economics, and IS disciplines were included."
- "Conference proceedings, which may contain emerging technologies, were excluded. [unacknowledged]"
- "The review may miss newer digital finance developments published after 2020."

**Key takeaways:**
- "80% of millennials use smartphones for transactional financial tasks."
- "Digital nudging can reduce credit card spending through salience."
- "Loss of cash tangibility increases spending in digital payments."

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
- "num: Overall financial literacy was high (M=3.22, SD=0.39) and financial well-being great (M=3.03, SD=0.46)."
- "num: Monthly income significantly correlated with financial literacy (r=0.223, p=0.003)."
- "num: Strong positive correlation between financial literacy and financial well-being (rs=0.660, p=0.000)."
- Age, sex, civil status, and number of dependents showed no significant relationship with financial literacy or well-being.

**Limitations / Contradictions for Odin:**
- "Sample size is limited (n=178) and restricted to one province."
- "Only nurses were surveyed; results may not generalize to other Filipino young professionals."
- "Quantitative design limits depth of insight into financial behaviors."

**Key takeaways:**
- "Higher monthly income is linked to better financial literacy among nurses."
- "Financial literacy strongly predicts financial well-being (rs=0.66)."
- "Nurses show great financial discipline but lower financial resilience (M=2.88)."

---


## The ASEAN Access to Digital Finance Study
**Filename:** `I--Ziegler-et_al_summarized.md`  
**Authors:** Ziegler, T.; Suresh, K.; Xie, Z.; Paes, F. F. de C.; Morgan, P. J.; Zhang, B. (2022)  
**ID:** `f47ac10b-58cc-4372-a567-0e02b2c3d479`  
**Odin Topics:** 1.A, 1.C, 4.A, 4.B, 5.A, 11.A, 13.B  

**TLDR:** A survey of 600 digital finance users across five ASEAN countries finds that millennials and MSMEs primarily use fintech for daily expenses and working capital, with fintech complementing traditional banking and low default rates.

**Problem & Motivation:** Digital finance has grown rapidly in ASEAN, but little is known about how fintech platforms engage customers and impact their financial health. Regulators need evidence to balance innovation with consumer protection. This study provides comprehensive data on user demographics, borrowing behavior, and outcomes across five countries.

**Approach (summary):**
- Online survey collected 10,580 responses from users of P2P lending, BNPL, invoice trading, and equity crowdfunding platforms in Indonesia, Malaysia, Philippines, Singapore, Thailand from Feb-Apr 2022.
- Data sanitization removed 16% of entries, resulting in 8,886 cleaned responses; stratified random sampling selected 600 responses (200 from Philippines, 400 from others) for balanced analysis.
- Descriptive and content analysis applied to four research themes: user profile, relationship with traditional finance, financing experience, and post-financing outcomes including COVID-19 impact.

**Key Findings (selected):**
- "num: 44% of P2P consumer lending users aged 25-34; 54% of BNPL users aged 25-34."
- "num: 49% of P2P consumer borrowers used funds for day-to-day expenses; 39% of BNPL for fashion and apparel."
- "num: 1% of P2P consumer borrowers defaulted, compared to >3% average bank NPL in ASEAN (World Bank)."
- "num: 65% of MSMEs reported increased productivity after receiving fintech financing; 59% increased profit."

**Limitations / Contradictions for Odin:**
- "The study does not measure loan quality, price, or diversity of offers. [unacknowledged]"
- "Sample size limitations prevent cross-country comparative analysis."
- "No analysis of herd behavior or anchoring in platform choice. [unacknowledged]"

**Key takeaways:**
- "1% of P2P consumer borrowers default, below regional bank NPL averages."
- "Millennials make up 44% of P2P consumer lending users in ASEAN."
- "Fintech complements banking: 52% of users increased savings account use."

---


## "Consumer Finance Survey 2021"
**Filename:** `L--Bangko_Sentral_ng_Pilipinas-2021_summarized.md`  
**Authors:** "Bangko Sentral ng Pilipinas" (2021)  
**ID:** `f47ac10b-58cc-4372-a567-0e02b2c3d479`  
**Odin Topics:** 1.A, 1.B, 1.C, 2.A, 2.C, 3.A, 4.A, 4.B, 5.A, 10.B, 13.A, 13.B  

**TLDR:** The 2021 Consumer Finance Survey by the Bangko Sentral ng Pilipinas provides comprehensive data on income, expenditure, assets, liabilities, and demographics of Filipino households, revealing trends in financial inclusion, digital adoption, and debt during the COVID-19 pandemic.

**Problem & Motivation:** There were significant data gaps on household wealth and indebtedness in the Philippines, as existing surveys like FIES and APIS had limited coverage of assets and liabilities. Collecting detailed financial condition data was necessary to inform evidence-based socio-economic policies and monetary decisions. The survey aimed to provide a comprehensive picture of household balance sheets, income sources, spending patterns, and demographic characteristics.

**Approach (summary):**
- "Sample of 18,000 households drawn from PSA's 2013 Master Sample (two-stage cluster sampling) covering all regions including BARMM."
- "Face-to-face interviews using structured CAPI questionnaire, translated into six major languages, conducted from March to December 2022."
- "Reference period for income and expenditure was calendar year 2021; assets and liabilities as of interview date."

**Key Findings (selected):**
- "num: 91.5% of households had wage income in 2021, up from 73.7% in 2018."
- "num: Only 29.3% of households carried any debt, down from 40.4% in 2018."
- "num: 35.3% owned deposit accounts, significantly up from 9.7% in 2018."
- "num: 24.3% owned electronic money accounts, up from 0.3% in 2018."

**Limitations / Contradictions for Odin:**
- "Estimates with coefficients of variation above 20 percent should be interpreted with caution."
- "Recall bias may affect income and expenditure values reported for the previous year."
- "Non-sampling errors from intentional under-reporting of assets and liabilities. [unacknowledged]"

**Key takeaways:**
- "Wage income source increased to 91.5% of households during the pandemic."
- "Debt prevalence dropped to 29.3% as households reduced borrowing."
- "Digital financial assets grew rapidly: e-money accounts up to 24.3%."

---


## Consumers semi-intertemporally make intertemporal decisions: insights from the payday effects
**Filename:** `I--Ma-et_al_summarized.md`  
**Authors:** Ma, C.; Gu, Y.; Chong, J. K. (0)  
**ID:** `d9b7a8c6-5f4e-3d2c-1b0a-9e8f7d6c5b4a`  
**Odin Topics:** 1.C, 2.B, 5.A, 7.A, 13.A  

**TLDR:** Analysis of storable product purchase data reveals that consumers self-impose monthly mental budgets, renewing them on paydays, leading to larger expenditures on first post-payday trips and decreasing expenditures over subsequent trips.

**Problem & Motivation:** Consumers are neither fully rational nor completely myopic, yet existing models do not explain how they make intertemporal purchase decisions for storable products without liquidity constraints. The gap is understanding the intrinsic commitment devices like mental budgeting that consumers use to manage spending across pay cycles. This paper provides empirical evidence for monthly mental budgets and the role of payday salience.

**Approach (summary):**
- Analyzed individual-level transaction data from a retail chain selling storable products (cosmetics, personal care) from 2011-2015 in a Southeast Asian country.
- Used regression discontinuity design around paydays (26th of each month) with customer-day and customer-trip level regressions.
- Compared cash users vs credit card users to isolate liquidity constraints vs behavioral effects.

**Key Findings (selected):**
- "num: Expenditures on paydays are 3.3% higher conditional on store visit."
- "num: For credit card users, first trip after payday (non-payday) has 0.726 higher expenditure than later trips."
- "num: Payday effect increases variety seeking by 0.1 varieties for credit card users."
- "num: Probability of purchasing a new variety increases by 0.63% on paydays."

**Limitations / Contradictions for Odin:**
- "Data only covers one retail chain in one country; external validity limited."
- "RD design assumes no other events coinciding with paydays; may be confounded by end-of-month effects."
- "Cannot fully rule out stockpiling as alternative explanation for some findings [unacknowledged]."

**Key takeaways:**
- "Monthly mental budgets renew on paydays, not just on payday itself."
- "Expenditures decrease over trips within a paycheck cycle."
- "Payday salience causes overspending beyond mental budget renewal."

---


## INFLUENCE OF DIGITAL WALLETS ON THE FINANCIAL BEHAVIOR OF HEI’S STUDENTS
**Filename:** `L--Bongado-et_al_summarized.md`  
**Authors:** Bongado, M. B.; Magallanes, A. R.; Semaña, C. M. (0)  
**ID:** `c6a8b9e0-1f2d-4c3a-9e5b-7d8f9a0b1c2d`  
**Odin Topics:** 1.C, 5.A, 7.A  

**TLDR:** Digital wallet usage positively influences financial behavior of HEI students, explaining 45.4% of variance in cash management and budgeting practices.

**Problem & Motivation:** The influence of digital wallet usage on financial behavior among higher education students remains underexplored, particularly in the Philippine context. While digital wallets offer convenience, evidence suggests they may encourage impulsive spending and hinder long-term financial planning. This study addresses the gap by examining determinants of adoption and their effect on cash management and budgeting.

**Approach (summary):**
- Data were collected from 219 randomly selected HEI students at Bukidnon State University – Talisayan Campus using stratified random sampling.
- A quantitative descriptive-correlational design was employed with a validated 4-point Likert scale questionnaire adapted from Belmonte et al. (2024).
- Independent variables were seven TAM-based determinants (e.g., perceived ease of use, trust); dependent variables were cash management and financial planning/budgeting.

**Key Findings (selected):**
- num: Digital wallet usage explains 45.4% of the variance in financial behavior (R²=0.454, F=180.136, p<.001).
- Students agree on all adoption determinants (means 2.91–2.99), with perceived trust showing the highest variability (SD=1.24).
- Financial behavior is generally responsible (overall M=2.99, SD=0.68), with financial planning and budgeting scoring highest (M=3.00).
- Regression beta coefficient (β=0.673, p<.001) indicates a significant positive effect of digital wallet usage on financial behavior.

**Limitations / Contradictions for Odin:**
- "Cross-sectional design cannot infer causation; only association is shown. [unacknowledged]"
- "Reliance on self-reported Likert scales may introduce response bias. [unacknowledged]"
- "The study does not control for income level, digital literacy, or parental influence. [unacknowledged]"

**Key takeaways:**
- "Digital wallet usage explains 45.4% of financial behavior variance."
- "Students agree on all adoption determinants with means from 2.91 to 2.99."
- "Perceived trust shows the widest disagreement (SD=1.24)."

---


## A Comprehensive Review of Machine Learning Techniques for Intelligent Personal Finance Management Systems
**Filename:** `IA--D'Souza-et_al_summarized.md`  
**Authors:** D'Souza, M.; Bhegade, P.; Bhalekar, P.; Bhavsar, Y. (0)  
**ID:** `b9c5f2d1-3a4e-4b5c-8d6e-7f8a9b0c1d2e`  
**Odin Topics:** 5.A, 6.A, 6.B, 7.A, 7.B, 7.C, 8.A, 8.B, 12.A, 12.B  

**TLDR:** Reviews machine learning techniques for intelligent personal finance management across budgeting, forecasting, anomaly detection, and group expense management, highlighting a shift from rule-based to adaptive, data-driven systems.

**Problem & Motivation:** Current research on PFMS is fragmented across budgeting, forecasting, anomaly detection, and group expense management, limiting cohesive intelligent solutions. Most traditional systems lack adaptability and personalization, relying on rigid rules. A systematic review comparing machine learning models across these components is missing.

**Approach (summary):**
- Conducts a qualitative literature survey of personal finance management systems from 1997 to 2021.
- Compares statistical methods (ARIMA, EWMA), machine learning (Isolation Forest, clustering), and deep learning (LSTM, GRU).
- Evaluates techniques across four dimensions: budgeting, forecasting, anomaly detection, and group expense management.

**Key Findings (selected):**
- Rule-based budgeting is transparent but cannot adapt to non-linear spending changes.
- LSTM captures long-term dependencies but requires large historical data and lacks interpretability.
- Isolation Forest efficiently detects anomalies in unlabeled data and scales well.
- Hybrid ARIMA-LSTM models combine linear trend modeling with non-linear residual learning.

**Limitations / Contradictions for Odin:**
- "Qualitative survey without quantitative meta-analysis or statistical significance testing."
- "Lacks systematic search protocol and inclusion/exclusion criteria [unacknowledged]."
- "Does not address data privacy, security, or regulatory compliance in depth [unacknowledged]."

**Key takeaways:**
- "LSTM captures long-term spending patterns but is opaque and data-hungry."
- "Isolation Forest is efficient for unsupervised anomaly detection without labels."
- "Hybrid ARIMA-LSTM models balance linear and non-linear forecasting strengths."

---


## The Role of Big Data Analytics in Behavioral Finance: Understanding Dynamics of Consumer Spending and Saving
**Filename:** `I--Whitaker_summarized.md`  
**Authors:** Whitaker, Kyle (0)  
**ID:** `d0f5e2b6-4c3a-4b8e-9d1f-2a3b4c5d6e7f`  
**Odin Topics:** 2.B, 5.A, 6.A, 6.B, 10.A, 10.B, 11.A, 13.A  

**TLDR:** Big data analytics combined with behavioral finance reveals psychological and social drivers of consumer spending and saving, enabling personalized financial strategies.

**Problem & Motivation:** Traditional financial models overlook psychological biases and contextual influences, limiting personalized financial advice and financial inclusion. Big data offers the scale needed to analyze multidimensional drivers of spending and saving.

**Approach (summary):**
- Reviews existing literature on big data characteristics (volume, velocity, variety) and behavioral finance concepts (cognitive biases, emotional influences).
- Proposes integration of structured transaction data with unstructured digital footprints such as social media and mobile app usage.
- Discusses descriptive, predictive, and prescriptive analytics methods including clustering, regression, and natural language processing.

**Key Findings (selected):**
- Consumer spending is influenced by cognitive biases like loss aversion, overconfidence, and anchoring.
- Predictive analytics using historical transaction data and sentiment analysis can forecast future spending patterns.
- Automated savings programs that analyze spending habits and round up purchases increase customer saving rates.
- Social media sentiment analysis provides context for consumer spending trends and saving motivations.

**Limitations / Contradictions for Odin:**
- Paper lacks empirical data or experimental results. [unacknowledged]
- No discussion of model interpretability or explainability for end users. [unacknowledged]
- Data privacy solutions are mentioned at a high level without technical detail. [acknowledged]

**Key takeaways:**
- Big data reveals psychological drivers beyond rational economic factors.
- Predictive analytics enables personalized financial interventions.
- Ethical safeguards for data privacy are essential for user trust.

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
- num: Moderate positive correlation between social media frequency and financial literacy (r=0.359, p<0.001).

**Limitations / Contradictions for Odin:**
- Correlational design prevents causal inference.
- Self-reported financial literacy may not reflect objective competence.
- Sample limited to business students at one campus, not representative of all Filipino young professionals.

**Key takeaways:**
- Social media use correlates moderately with financial literacy (r=0.359).
- High knowledge does not guarantee good financial behavior.
- Impulse buying is a major barrier to sound decisions.

---


## Leveraging Big Data Analytics in Behavioral Finance: Insights into Consumer Spending and Saving Dynamics
**Filename:** `I--Ying-&-Blaise_summarized.md`  
**Authors:** Ying, H.; Blaise, M. (0)  
**ID:** `5c9a5e3a-8b4a-5c1e-9f2d-4a7b8c9d0e1f`  
**Odin Topics:** 2.B, 3.A, 5.A, 6.A, 10.A, 10.B, 11.A, 13.A  

**TLDR:** Big data analytics combined with behavioral finance reveals how psychological biases and digital footprints influence consumer spending and saving patterns, enabling personalized financial strategies.

**Problem & Motivation:** Traditional financial models assume rational decision-making and overlook psychological, social, and contextual drivers of consumer behavior. This gap limits the ability to design effective personalized financial products and interventions. The paper argues that big data techniques can capture these multidimensional factors at scale to improve financial inclusion and resilience.

**Approach (summary):**
- Reviews the characteristics of big data (volume, velocity, variety, veracity) in financial contexts.
- Identifies data sources: transaction histories, social media, mobile apps, surveys, and web analytics.
- Proposes descriptive, predictive, and prescriptive analytics to uncover spending and saving patterns.

**Key Findings (selected):**
- Big data enables segmentation of consumers based on spending habits and cognitive biases.
- Predictive analytics can forecast future spending behaviors from historical transaction data.
- Social media sentiment analysis provides contextual insights that influence spending decisions.
- Automated savings programs that analyze spending patterns can increase saving rates.

**Limitations / Contradictions for Odin:**
- The paper is a non‑empirical review without original experiments or data.
- No specific machine learning model or evaluation metrics are provided.
- Ethical concerns like algorithmic bias are raised but no mitigation strategies are proposed [unacknowledged].

**Key takeaways:**
- Big data reveals hidden psychological drivers of consumer spending.
- Behavioral segmentation enables personalized financial products and alerts.
- Predictive analytics forecasts spending patterns from transaction history.

---


## Note for the Agent

The summaries above contain **essential extracts** – enough to understand each paper's relevance to Odin, including supporting evidence and limitations.
If you need additional details not shown here (e.g., **critical citations, definitions, equations, full methodology, or the complete mapping rationale**),
**ask the user to send the original summary file (`<filename>_summarized.md`) or the converted MarkItDown file(`<filename>_marked.md`)** for the specific paper(s) of interest.
Do not invent missing information. Acknowledge gaps when they exist.