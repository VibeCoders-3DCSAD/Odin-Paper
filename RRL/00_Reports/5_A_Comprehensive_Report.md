# Comprehensive Report for Subtopic: `5.A`

**Total relevant papers:** 72

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


## Profiling Platform Workers in the Philippines: Evidence from the Jobs and Skills Survey
**Filename:** `L--Jandoc-et_al_summarized.md`  
**Authors:** Jandoc, K. R. L.; Martinez, A.; Bulan, J. A. N.; Molato, R.; Guyos, A. (2026)  
**ID:** `3b5d3c2a-1e4f-4d2e-9a8b-7c6d5e4f3a2b`  
**Odin Topics:** 1.A, 1.B, 1.C, 5.A  

**TLDR:** Platform workers in the Philippines are predominantly young, urban, highly educated, and concentrated in digital services, with flexibility as primary motivation but persistent social protection deficits.

**Problem & Motivation:** The rapid growth of non-traditional platform work in the Philippines has outpaced empirical evidence, leaving gaps in understanding worker profiles, motivations, and job quality. Existing studies rely on small or non-representative samples. This study uses nationally representative data to provide systematic evidence on platform workers to inform policy under the Philippine Development Plan 2023–2028.

**Approach (summary):**
- Data from the 2025 Jobs and Skills Survey (JSS), a nationally representative rider to the Labor Force Survey (LFS), covering ~9,200 employed Filipinos.
- Platform work defined as using online or app-based platforms for paid tasks, including home-based digital work, outside-home services, ride-hailing, and delivery.
- Constructed Routine Task Intensity (RTI) index using task frequency items from JSS Section B.

**Key Findings (selected):**
- num: 8.2% of workers use online platforms, representing approximately 4.1 million Filipinos, with 84.5% as sole job and 42.6 average weekly hours.
- num: Platform workers are 74.0% urban (vs 57.7% national), 69.7% higher education (vs 31.5%), and 82.3% prime working age.
- num: Flexibility is the top motivation (88.9%), but necessity-driven motives are higher for drivers/delivery (18.1% lack other income sources vs 9.3% for home-based).
- num: Platform workers have lower Routine Task Intensity (RTI -0.19) than non-platform workers (RTI +0.56), with home-based workers lowest (-0.73).

**Supports Odin (direct justifications):**
- Platform workers are disproportionately young (mean age 35.9-38.0), urban (74%), and college-educated (69.7%), supporting targeted acquisition for PFMS.
- Flexibility is the primary motivation for 88.9% of platform workers, emphasizing the need for adaptive budgeting and forecasting tools.
- 22.5% of daily platform users report overskilling, indicating potential demand for upskilling financial planning features.

**Limitations / Contradictions for Odin:**
- Cross-sectional design cannot establish causality between platform work and benefit deficits. [unacknowledged]
- Self-reported platform use may misclassify workers, and the survey excludes platform-level earnings or algorithm data. [unacknowledged]
- Potential undercounting of informal platform work due to survey non-response or misclassification.

**Key takeaways:**
- 8.2% of Filipino workers engage in platform work, about 4.1 million people.
- Flexibility is cited by 88.9% of platform workers as a motivation.
- Platform workers have 69.7% higher education but 22.5% overskilling rate.

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


## RFM-Net: A Convolutional Neural Network for Customer Segment Classification
**Filename:** `IA--Balbal-&-Birant_summarized.md`  
**Authors:** Balbal, K. F.; Birant, D. (2026)  
**ID:** `10.3390/app16052223`  
**Odin Topics:** 5.A, 5.C, 11.A  

**TLDR:** RFM-Net integrates Recency, Frequency, Monetary analysis with a lightweight CNN to classify customers into seven strategic segments, achieving 94.33% accuracy on an online retail dataset.

**Problem & Motivation:** Traditional RFM-based segmentation relies on rule-based logic that may miss nonlinear patterns in customer behavior. Clustering and statistical methods often provide static groupings lacking adaptability. A deep learning approach that preserves interpretability while capturing complex relationships is needed.

**Approach (summary):**
- Used the Online Retail dataset (541,909 records) from a UK-based company.
- Computed RFM features (Recency, Frequency, Monetary) per customer and discretized into 1–5 scores using domain thresholds.
- Generated segment labels (Champions, Loyal, etc.) via rule-based logic from RFM scores.

**Key Findings (selected):**
- RFM-Net achieved 94.33% weighted accuracy across 10 folds.
- num: 13.17% relative average increase in accuracy over previously reported methods on the same dataset.
- Recency was the most important feature (importance 0.5358), followed by Frequency (0.4217) and Monetary (0.2642).
- The model performed best on Potential Loyalists (96.9% correct) and Champions (94.3%).

**Supports Odin (direct justifications):**
- A shallow CNN with 6,823 parameters achieves high accuracy on RFM data with minimal overfitting.
- Recency is the strongest predictor of customer engagement, more than frequency or monetary value.
- Seven distinct behavioral segments (Champions to Hibernating) can be derived from RFM scores.

**Limitations / Contradictions for Odin:**
- Dataset consists of UK retail transactions only; may not reflect financial behaviors of Filipino young professionals. [unacknowledged]
- Segment labels are derived from the same RFM scores used as features, creating circular dependency.
- The model only uses three features (R,F,M); additional demographic or cultural factors could improve accuracy.

**Key takeaways:**
- RFM-Net classifies customers with 94.33% accuracy using only three features.
- Recency is the most important predictor of customer engagement.
- A shallow CNN with 6,823 parameters avoids overfitting on tabular data.

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
- {'Model architecture': 'bidirectional LSTM with 512 hidden units, self-attention with 8 heads, adaptive dropout (0.5→0.3), and softmax output for five purchase intention levels.'}

**Key Findings (selected):**
- {'num': 'Proposed LSTM achieves 94.2% accuracy, 93.8% precision, 94.7% recall, and 94.2% F1-score.'}
- {'num': 'Outperforms standard LSTM by 3.0 percentage points and traditional ML by average 10.7 percentage points (p<0.001).'}
- {'num': 'High-frequency users reach 96.1% accuracy, new users 91.8% (23.6% improvement over traditional methods), high-value customers 96.7%.'}
- Attention weight analysis reveals recency bias (ratio 1.847) and higher importance for behavioral features over demographics.

**Supports Odin (direct justifications):**
- LSTM networks with self-attention achieve 94.2% accuracy in predicting purchase intentions.
- Sequential behavioral features (purchase frequency, browsing duration) are more predictive than demographics (cumulative importance 0.521).
- The model maintains >90% accuracy across user segments including new users (91.8%) and high-frequency users (96.1%).

**Limitations / Contradictions for Odin:**
- Dataset from a single e-commerce platform limits generalizability to PFMS contexts.
- External environmental factors (e.g., economic shocks) are not modeled [unacknowledged].
- Real-time prediction latency and deployment constraints are not evaluated [unacknowledged].

**Key takeaways:**
- LSTM with attention achieves 94.2% accuracy on purchase prediction.
- Behavioral features dominate over demographics (cumulative score 0.521).
- Model generalizes to new users with 91.8% accuracy.

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
- {'LightFM hybrid model with user features (BFI T-scores, genre preferences) and item features (sonic features': 'acousticness, danceability, energy, etc., and item personality profiles as proportions).'}
- Item personality profile computed as proportion of users who liked the item with a given Big Five degree.

**Key Findings (selected):**
- {'num': 'Hybrid WARP model achieved training precision 0.23, recall 0.75, AUC 0.82; validation precision 0.46, recall 0.64, AUC 0.57.'}
- Pure CF overfitted (training AUC 1.00, validation AUC 0.56) and performed worse on unseen data.
- {'Online evaluation': 'hybrid Model A had mean user satisfaction 4.15 vs pure CF 3.55 (p<0.05).'}
- Hybrid model achieved precision 0.57, recall 0.62, F1 0.58 on user feedback, outperforming pure CF (0.41/0.46/0.40).

**Supports Odin (direct justifications):**
- Incorporating personality profiles improves recommendation accuracy over pure collaborative filtering.
- Hybrid models using WARP loss generalize better to unseen data than BPR or pure CF.
- User satisfaction is higher for personality-enhanced recommendations (mean 4.15 vs 3.55).

**Limitations / Contradictions for Odin:**
- Small song dataset (100 songs) limits recommendation variation. [unacknowledged]
- Personality data available for less than 20% of users, causing sparsity. [acknowledged]
- Online evaluation sample size of 20 new users is small. [unacknowledged]

**Key takeaways:**
- Hybrid WARP model achieved 0.46 precision and 0.64 recall on validation.
- Personality profiling reduces cold-start problems in recommender systems.
- User satisfaction improved by 0.6 points with personality integration.

---


## Human-AI Collaboration in Customer Behavior Research: Personalizing Financial Services
**Filename:** `I--Duvalla_summarized.md`  
**Authors:** Duvalla, V. R. (2025)  
**ID:** `10.32996/jcsts.2025.7.4.12`  
**Odin Topics:** 5.A, 5.C, 6.A, 10.A, 10.B, 11.A, 11.B  

**TLDR:** Human-AI collaboration in financial services uses machine learning to process transaction data while human experts interpret cultural and socioeconomic factors, enabling personalized segmentation, recommendations, and retention.

**Problem & Motivation:** Financial institutions face data fragmentation, organizational readiness gaps, and regulatory compliance hurdles that impede effective personalization. The disparity between strategic intention and operational execution remains a critical gap. Human-AI collaborative frameworks address these challenges by combining computational pattern recognition with human contextual intelligence.

**Approach (summary):**
- The paper proposes a framework where AI models (clustering, neural networks, temporal pattern mining) process large transactional datasets from millions of accounts.
- Human experts provide interpretive insights on socioeconomic and cultural nuances through human-in-the-loop refinement processes with bidirectional knowledge flows.
- A case study of JP Morgan Chase uses API-based integration, confidence-based escalation, and omnichannel orchestration across mobile, web, ATM, and branches.

**Key Findings (selected):**
- num: Advanced clustering algorithms identify up to 15 distinct behavioral segments versus 4-5 segments with conventional methods.
- num: Omnichannel orchestration yields 59% higher customer satisfaction scores compared to siloed channel-specific approaches.
- num: JP Morgan Chase's human-AI platform achieved 94% higher engagement with financial wellness recommendations than previous approaches.
- Human-in-the-loop refinement improves model prediction accuracy beyond fully automated or purely human-driven systems.

**Supports Odin (direct justifications):**
- Human-guided AI models achieve higher accuracy in predicting customer financial needs than fully automated systems.
- Financial customers express significant concerns about opacity of AI-driven decisions, requiring explainable AI like SHAP and LIME.
- Federated learning achieves predictive accuracy of centralized models while keeping sensitive financial data in local secure environments.

**Limitations / Contradictions for Odin:**
- The paper is a conceptual review without primary empirical validation of its proposed framework. [unacknowledged]
- All quantitative findings are cited from secondary sources, not original experiments. [unacknowledged]
- Implementation costs, latency, and scalability constraints of federated learning in real-time banking are not discussed. [unacknowledged]

**Key takeaways:**
- Human-AI collaboration improves personalization accuracy over pure automation or human-only approaches.
- Advanced clustering identifies up to 15 behavioral segments versus 4-5 conventional methods.
- Federated learning enables privacy-preserving personalization without data centralization.

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
- num: Life attitude profile has a positive direct effect on stock market participation intention (β=0.154, p=0.025).
- num: Cognitive ability mediates the relationship between life attitude and participation intention (indirect β=0.051, p=0.032).
- num: Death acceptance (β=0.312, p<0.001) and goal seeking (β=0.396, p=0.009) positively predict intention.
- Life purpose negatively predicts stock market intention (β=-0.243, p=0.036).

**Supports Odin (direct justifications):**
- Life attitude profile directly influences stock market participation intention among young professionals.
- Cognitive ability mediates the effect of life attitude on investment intention.
- Death acceptance and goal seeking are positively associated with intention to participate in stock markets.

**Limitations / Contradictions for Odin:**
- Self-reported data may introduce response and social desirability bias.
- Cross-sectional design prevents causal conclusions. [unacknowledged]
- Sample from Bulacan limits generalizability to other regions.

**Key takeaways:**
- Life attitude directly affects stock market intention (β=0.154).
- Cognitive ability mediates 39% of life attitude's effect on investment.
- Death acceptance and goal seeking are strong positive predictors of intention.

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


## The Moderating Effect of Access to Finance on Myopic Decision-Making and Business Performance of Low-income Household Micro-Enterprises in Manila
**Filename:** `L--Ong-et_al_summarized.md`  
**Authors:** Ong, H. T.; Keh, K. Z. N.; Lui, N. C. J. L.; Santos, A. H. M.; Suarez, E. J. P. (2025)  
**ID:** `d1e2f3a4-b5c6-7d8e-9f0a-1b2c3d4e5f6a`  
**Odin Topics:** 1.C, 5.A  

**TLDR:** Myopic decision-making significantly harms micro-enterprise business performance, but access to finance moderates this negative effect for low-income households in Manila.

**Problem & Motivation:** Low-income household micro-entrepreneurs often prioritize short-term survival over long-term growth due to financial constraints, yet the combined role of myopic decision-making and access to finance on business performance remains underexplored. Understanding this relationship is critical for breaking poverty cycles. No prior study has integrated these three factors simultaneously.

**Approach (summary):**
- Quantitative survey of 100 sari-sari store owners in Manila.
- {'Measured four myopia dimensions': 'competitive, cooperative, temporal, and learning.'}
- Assessed access to finance via barriers, formal lending, and informal credit.

**Key Findings (selected):**
- num: Myopic decision-making has a significant effect on business performance (p < 0.001).
- num: Access to finance has a significant positive effect on business performance (p < 0.001).
- num: Access to finance moderates the myopia-performance relationship (p = 0.005).
- Temporal myopia (mean 2.96) is the highest myopia dimension among micro-entrepreneurs.

**Supports Odin (direct justifications):**
- Myopic decision-making significantly reduces business performance among micro-enterprises (p < 0.001).
- Access to finance has a significant positive effect on business performance (p < 0.001).
- Access to finance moderates the relationship between myopic decision-making and business performance (p = 0.005).

**Limitations / Contradictions for Odin:**
- Sample limited to 100 sari-sari store owners in Manila.
- Relies on subjective Likert-scale responses.
- Cross-sectional design prevents causal inference [unacknowledged].

**Key takeaways:**
- Myopic decision-making harms business performance of low-income micro-enterprises.
- Access to finance significantly improves business outcomes (p < 0.001).
- Financial access moderates the negative effect of short-term thinking.

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


## Buy-Now-Pay-Later Adoption, Debt Stress, and Repurchase Intention among Filipinos Gen Z Consumers: The Mediating Role of Budgeting Self-Efficacy
**Filename:** `L--Romero_summarized.md`  
**Authors:** Romero, M. A. (2025)  
**ID:** `b3c5d7e9-f1a2-4b6c-8d0e-9f1a2b3c4d5e`  
**Odin Topics:** 1.C, 5.A, 11.A, 11.B, 13.B  

**TLDR:** BNPL adoption among Filipino Gen Z consumers increases repurchase intention but also raises debt stress, while budgeting self-efficacy and transparency mitigate negative outcomes.

**Problem & Motivation:** BNPL services expand rapidly in Southeast Asia but create tension between purchase convenience and consumer welfare risks. Gen Z consumers face high digital shopping frequency and limited financial buffers, yet mechanisms linking BNPL adoption to stress and repurchase are unclear. This study identifies debt stress and budgeting self-efficacy as explanatory pathways for Filipino youth.

**Approach (summary):**
- Survey of 602 Filipino Gen Z BNPL users who had used the service at least twice in three months.
- Constructs measured: perceived convenience, promotional attractiveness, transparency, adoption intensity, budgeting self-efficacy, debt stress, repurchase intention.
- Partial Least Squares Structural Equation Modeling (PLS-SEM) with bootstrapping for mediation analysis.

**Key Findings (selected):**
- Perceived convenience, promotional attractiveness, and transparency are positively associated with BNPL adoption intensity.
- BNPL adoption intensity is positively associated with repurchase intention and also positively associated with debt stress.
- Debt stress is negatively associated with repurchase intention.
- Budgeting self-efficacy reduces debt stress and strengthens repurchase intention.

**Supports Odin (direct justifications):**
- BNPL adoption intensity increases repurchase intention directly but also increases debt stress.
- Budgeting self-efficacy reduces debt stress and strengthens repurchase intention.
- Perceived transparency strengthens budgeting self-efficacy and indirectly reduces debt stress.

**Limitations / Contradictions for Odin:**
- Cross-sectional design restricts temporal inference about how debt stress accumulates over repeated BNPL use. [acknowledged]
- Reliance on self-reported measures may introduce common method bias. [acknowledged]
- No objective transaction data to validate adoption intensity. [acknowledged]

**Key takeaways:**
- Survey of 602 Filipino Gen Z consumers shows BNPL adoption increases repurchase intention and debt stress.
- Budgeting self-efficacy buffers debt stress and supports healthier repurchase behavior.
- Transparency in fees and due dates strengthens self-efficacy and reduces harmful outcomes.

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
- num: 24 commercial banks lost N5.79 billion to fraud in Q2 2023, a 1125% increase from Q1.
- num: 94.35% of bank fraud losses came from fraudulent loans.
- num: SVM achieved over 98% accuracy for phishing email detection.
- num: Feed-forward neural network achieved 97% detection rate for credit card fraud and phishing websites.

**Supports Odin (direct justifications):**
- AI systems reduce false positives by continuously learning from transaction data.
- Anomaly detection algorithms can identify unusual spending in real-time.
- Behavioral profiling with ML establishes user baselines to detect deviations.

**Limitations / Contradictions for Odin:**
- Primary data limited to unstructured interviews and anecdotal evidence; no large-scale quantitative study. [unacknowledged]
- Does not provide a specific, reproducible algorithm for anomaly detection; remains a high-level review. [unacknowledged]
- Ethical concerns like algorithmic bias are mentioned but not explored in depth. [unacknowledged]

**Key takeaways:**
- Anomaly detection with ML achieved 97% accuracy for credit card fraud.
- Real-time analysis enables proactive fraud prevention before losses occur.
- Behavioral profiling reduces false positives by learning user baselines.

---


## Credit Card Fraud Detection Through Deep Learning and Real-Time Data Streams: A Comparison and New Directions
**Filename:** `IA--Polytarchos_summarized.md`  
**Authors:** Polytarchos, E. (2025)  
**ID:** `10.47852/bonviewFSI52026108`  
**Odin Topics:** 5.A, 8.A, 8.B, 12.A, 12.B  

**TLDR:** Compares deep learning (LSTM, MLP) and real-time data stream analysis (BEReTiC) for credit card fraud detection, finding deep learning achieves 92% accuracy but slower adaptation, while real-time clustering offers faster detection with lower false positives.

**Problem & Motivation:** Existing fraud detection methods either rely on batch-trained deep learning requiring extensive preprocessing and retraining, or real-time systems with lower initial accuracy. There is a lack of comprehensive empirical comparison between these paradigms on high-volume financial data. This gap prevents system designers from making informed deployment decisions.

**Approach (summary):**
- {'Used two proprietary datasets': 'IND (17.5M individual transactions) and SUM (1.2M purchase summaries) with customer demographic and behavioral labels.'}
- Injected 1000 synthetic fraudulent transactions by assigning average behavioral profiles of one customer to another customer's transactions.
- Deep learning pipeline trained LSTM and MLP models to predict customer labels (e.g., total funds range) and computed Scale of Suspicious Transaction (SST) from ensemble misclassification consensus.

**Key Findings (selected):**
- num: Deep learning LSTM achieved 92% accuracy predicting total funds range and 86% for age range.
- num: Deep learning detected 788 of 1000 injected fraudulent transactions with 1340 false positives (0.007% misclassification rate).
- num: Real-time clustering detected 619 of 1000 injected frauds with 574 false positives (0.003% misclassification rate).
- Real-time clustering had lower classification accuracy (e.g., 66% for total funds range) due to cold-start before building customer fingerprints.

**Supports Odin (direct justifications):**
- Deep learning models can achieve 92% accuracy in classifying customer financial behavior patterns from transaction history.
- Real-time clustering on raw data streams achieves lower false positive rate (0.003%) than batch deep learning (0.007%) for fraud detection.
- A hybrid model combining offline deep learning with online clustering is proposed for optimal fraud detection performance.

**Limitations / Contradictions for Odin:**
- Real-time clustering suffers from cold-start: initial customer fingerprints are incomplete, lowering early accuracy. [acknowledged]
- Dataset is proprietary and not publicly available. [unacknowledged]
- No comparison to existing production fraud detection systems or industry benchmarks. [unacknowledged]

**Key takeaways:**
- Deep learning LSTM achieved 92% accuracy predicting customer total funds range.
- Real-time clustering detected 619 of 1000 frauds with only 574 false alarms.
- Hybrid integration of batch and streaming methods is proposed as future direction.

---


## WEKA-BASED DECISION-TREE MODEL FOR USER SUBSCRIPTION PLAN PREDICTION
**Filename:** `LA--Guban-et_al_summarized.md`  
**Authors:** Guban, J. C. R.; Menderico, C. D. R.; Montalban, D. M. G. (2025)  
**ID:** `a1b2c3d4-e5f6-5123-89ab-cdef01234567`  
**Odin Topics:** 5.A, 5.C, 6.A, 12.A, 12.B  

**TLDR:** A J48 decision tree model predicts streaming subscription plans from user demographics and behaviors, achieving 72% accuracy with country as the strongest predictor.

**Problem & Motivation:** Streaming platforms lack interpretable models to understand how user attributes like age, device, and country jointly influence subscription plan selection. This gap hinders targeted marketing and plan optimization. The study addresses this by developing a transparent decision-tree classifier.

**Approach (summary):**
- {'Used 2,500 anonymized user records with five attributes': 'country, age, gender, device type, subscription start month.'}
- Applied J48 algorithm in WEKA with an 80/20 train-test split.
- Evaluated using accuracy, Kappa statistic, precision, recall, F-measure, and ROC area.

**Key Findings (selected):**
- num: 72% overall accuracy on the test set.
- num: Kappa statistic of 0.5797 indicates moderate agreement.
- Country identified as most influential predictor, followed by age and device type.
- Younger smartphone users subscribing later in the year tend to choose Premium plans in the US.

**Supports Odin (direct justifications):**
- A decision tree with 72% accuracy can reliably predict subscription plan from five user attributes.
- Country is the strongest predictor of plan choice, explaining most variance.
- Younger smartphone users are more likely to select premium plans when subscribing later in the year.

**Limitations / Contradictions for Odin:**
- Dataset limited to five user attributes, excluding behavioral indicators such as watch time or session frequency.
- Only J48 algorithm tested; ensemble methods not explored.
- Model not validated on a different dataset or in a real-time setting.

**Key takeaways:**
- J48 decision tree predicts subscription plans with 72% accuracy.
- Country is the strongest predictor, followed by age and device.
- All United Kingdom users consistently choose Standard plan.

---


## From Borrowing to Building: A Systematic Literature Review of Data-Driven Strategies for Cultivating Better Money Habits through Consumer Credit
**Filename:** `IA--Oyeyemi-et_al_summarized.md`  
**Authors:** Oyeyemi, D. O.; Moussa, A. H.; Abioye, V. O. (2025)  
**ID:** `10.37502/IJSMR.2025.81004`  
**Odin Topics:** 2.B, 4.A, 4.B, 5.A, 6.A, 10.A, 10.B, 11.A, 13.B  

**TLDR:** A systematic review finds that alternative data and machine learning expand credit access, while behavioral economics and feedback mechanisms improve financial habits, despite privacy and bias concerns.

**Problem & Motivation:** Consumer credit systems have evolved into data-driven platforms, but their potential to cultivate better money habits remains underexplored. The gap involves understanding how alternative data, machine learning, and behavioral insights can be integrated to foster responsible credit use rather than merely expanding access.

**Approach (summary):**
- Systematic literature review across Scopus, Web of Science, IEEE Xplore, and Google Scholar using keywords related to data-driven credit, financial habits, and machine learning.
- Inclusion criteria: peer-reviewed articles, conference papers, book chapters in English addressing data analytics or ML in consumer credit and impact on financial behavior.
- Data extraction using standardized protocol, followed by thematic synthesis of findings across alternative data, behavioral drivers, technological innovations, and information design.

**Key Findings (selected):**
- num: Ensemble machine learning models like XGBoost outperform logistic regression in credit classification tasks, improving predictive accuracy and reducing default rates.
- Alternative data from mobile phone usage, transactional records, and behavioral patterns enables credit scoring for individuals without traditional credit histories.
- Personality traits (conscientiousness, impulsivity), self-control, and financial literacy significantly influence borrowing, repayment, and saving behaviors.
- The 'statement effect' shows that credit card statement receipt temporarily reduces spending, indicating timing-based intervention opportunities.

**Supports Odin (direct justifications):**
- Machine learning models using alternative data predict credit default more accurately than traditional logistic regression.
- Personalized feedback loops and behavioral nudges improve short-term financial behaviors in credit contexts.
- Personality traits like conscientiousness and self-control correlate with responsible credit management.

**Limitations / Contradictions for Odin:**
- The review does not include longitudinal studies tracking long-term habit formation from data-driven interventions.
- Ethical frameworks for mitigating algorithmic bias and ensuring fairness are underdeveloped in the synthesized literature.
- Comparative analysis of different intervention types (financial incentives vs. behavioral nudges) is limited.

**Key takeaways:**
- Ensemble machine learning models outperform logistic regression for credit scoring.
- Behavioral nudges and feedback loops enhance short-term financial habits.
- Alternative data expands credit access but raises privacy and bias concerns.

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


## Analysing community-level spending behaviour contributing to high carbon emissions using stochastic block models
**Filename:** `IA--Simeonov-et_al_summarized.md`  
**Authors:** Simeonov, O.; Restocchi, V.; Goddard, B. D. (2025)  
**ID:** `10.1038/s41598-025-14364-7`  
**Odin Topics:** 5.A, 5.C  

**TLDR:** Stochastic block models on bipartite customer-merchant networks identify consumer groups with similar spending and carbon emission patterns, enabling targeted sustainability interventions.

**Problem & Motivation:** Reducing carbon emissions requires understanding consumer spending behavior at scale. Financial transaction data can estimate emissions, but grouping consumers with similar spending patterns remains challenging for designing effective interventions. Existing clustering methods often rely on demographic data or focus on single categories.

**Approach (summary):**
- Used debit card transaction data from 1,362 UK customers from a sustainable banking FinTech (ekko), filtering to 272 customers with ≥30 transactions across ≥10 MCC categories.
- Constructed bipartite network with customers and merchant categories as nodes, weighted by transaction counts or normalized spending amounts.
- Applied degree-corrected nonparametric hierarchical stochastic block model (SBM) for community detection, running 100 iterations to stabilize entropy.

**Key Findings (selected):**
- num: Weighted SBM produced communities where spending percentages across categories fell within one median absolute deviation of the population median for 71 of 80 clusters.
- num: Unweighted SBM identified clusters with distinct emission profiles; e.g., clusters 17 and 18 had high emissions from taxicabs, while clusters 3,11,12 from service stations.
- num: Logistic regression using age and deprivation index predicted customer retention with AUC 0.744; younger and more deprived customers had higher dropout probability.
- num: Median carbon emission rate was 685 grams per GBP spent, slightly lower than previous studies.

**Supports Odin (direct justifications):**
- Financial transaction data can reliably estimate carbon emissions at individual level.
- Stochastic block models effectively cluster consumers by spending patterns without demographic features.
- Consumer clusters exhibit distinct carbon emission profiles driven by specific merchant categories.

**Limitations / Contradictions for Odin:**
- Dataset represents sustainability-oriented subsample, limiting generalizability. [unacknowledged]
- Utility and subscription payments are underrepresented due to direct debit exclusion. [acknowledged]
- SBM static nature does not capture temporal changes in spending behavior. [acknowledged]

**Key takeaways:**
- Weighted SBM aligns cluster spending with population medians within one MAD.
- Median carbon emission rate is 685 grams per GBP spent.
- Younger and deprived customers have higher dropout probability in paid sustainable banking.

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


## BUY NOW, PAY LATER: SHOPEE ONLINE STORE USERS EXPERIENCES ON SHOPEE PAY LATER FEATURE (SPAY LATER)
**Filename:** `L--Canalog-et_al_summarized.md`  
**Authors:** Calanog, V. C.; Paderan, M. J. D.; Adove, R. C. A.; Bathan, C. M. N.; Catibog, D. N.; Rivera, G. R.; Mangarin, J. A. (2025)  
**ID:** `10.5281/zenodo.15031111`  
**Odin Topics:** 1.C, 5.A, 13.B  

**TLDR:** Shopee Pay Later users employ the feature primarily for essential needs, valuing convenience and flexible repayment, while facing technical issues and requiring disciplined budgeting.

**Problem & Motivation:** Prior studies on Buy Now, Pay Later focused on either positive or negative impacts but lacked a comprehensive understanding of user motivations and behaviors. This gap prevented a holistic view of how users experience features like Shopee Pay Later. The study addresses the overall experience of Spay Later users, including satisfaction, convenience, financial behavior, and challenges.

**Approach (summary):**
- Qualitative phenomenological study using semi-structured interviews with 10 Shopee Spay Later users in Balayan, Batangas, Philippines.
- Participants selected via judgmental sampling: gold or platinum loyalty tier, credit limit ≥5000 PHP, and at least one year of Spay Later use.
- Thematic analysis applied to interview transcripts to identify patterns in user satisfaction, convenience, financial behavior, and challenges.

**Key Findings (selected):**
- Three usage patterns emerged: occasional use for necessities, regular monthly use for essentials, and needs-based use during financial constraints.
- Users primarily purchase everyday household necessities, high-cost essential items during financial constraints, and rarely non-essential items.
- Motivations include limited budget and financial independence, ability to afford high-cost purchases over time, attractive incentives, and urgent needs.
- Challenges include transaction errors, unexpected fees, insufficient credit balance, and seller accountability concerns.

**Supports Odin (direct justifications):**
- Spay Later users primarily make essential purchases rather than discretionary ones.
- Flexible repayment options and low interest rates increase user satisfaction and perceived convenience.
- Pre-payment planning and due date monitoring prevent late fees and promote financial discipline.

**Limitations / Contradictions for Odin:**
- Small sample size (10 participants) limits generalizability. [unacknowledged]
- Qualitative only; no quantitative validation of claimed effects. [unacknowledged]
- Participants restricted to gold/platinum tier users with ≥5000 PHP credit limit, excluding lower-tier users. [unacknowledged]

**Key takeaways:**
- 10 gold/platinum users with 5000 PHP credit limit were interviewed.
- Three usage patterns: occasional, regular monthly, and needs-based.
- Spay Later improved budgeting skills and financial flexibility.

---


## Clustering and Similarity Learning in Financial Markets: A Tutorial for the Practitioners
**Filename:** `IA--Mehta-et_al_summarized.md`  
**Authors:** Mehta, D.; Thompson, J. R. J.; Lee, H.; Lee, Y. (2025)  
**ID:** `b1c2d3e4-f5a6-4b7c-8d9e-0f1a2b3c4d5e`  
**Odin Topics:** 5.A, 8.A, 8.B, 12.A, 12.B  

**TLDR:** Reviews clustering and similarity learning methods for financial markets, covering metric learning, graph methods, and LLMs to build adaptive peer groups for bonds, funds, companies, and investors, with emphasis on operational evaluation and multimodal data fusion.

**Problem & Motivation:** Traditional peer-grouping methods such as industry codes or style boxes provide only coarse and rigid notions of similarity, failing to capture actual risk and thematic exposures. Financial applications require adaptive, data-driven similarity systems that quantify closeness based on real economic attributes. However, similarity has no universal ground truth, making evaluation and governance challenging under regulatory scrutiny.

**Approach (summary):**
- Surveys clustering methods (partitioning, hierarchical, density-based, model-based) and distance metrics for tabular, time-series, text, graph, and image data.
- Reviews similarity learning techniques including metric learning, random forest proximities, Siamese networks, contrastive learning, graph neural networks, and multimodal fusion.
- Presents case studies on corporate bonds (random forest proximities for substitution), municipal bonds (CatBoost), MBS/ABS (hazard models), funds (category reproducibility, open-set recognition), companies (multimodal pipelines), and investors (behavioral clustering).

**Key Findings (selected):**
- Traditional peer-grouping methods (industry codes, style boxes) are coarse and rigid; modern similarity learning enables adaptive, data-driven neighborhoods.
- num: Nearly 20% of U.S. investment-grade bond volume trades in baskets, requiring portfolio similarity metrics like STRAPSim for ETF alignment.
- num: Analysis of 5.5 million households using K-Modes clustering identified five distinct ESG investor types.
- Supervised similarity via random forest proximities improves bond substitution fidelity and fund category reproducibility.

**Supports Odin (direct justifications):**
- Clustering investors by transaction behavior reveals misalignments between self-assessed risk and actual decisions.
- Random forest proximities improve substitution fidelity in bond selection, applicable to expense substitution in PFMS.
- Open-set recognition can detect outlier transactions or categories without retraining.

**Limitations / Contradictions for Odin:**
- Similarity definitions are inherently subjective and depend on task, data modality, and market regime. [unacknowledged]
- Many advanced methods (deep learning) operate as black boxes, complicating accountability and compliance.
- Outputs can shift with parameter choices; stability across time requires careful rolling-window validation.

**Key takeaways:**
- Similarity learning enables adaptive peer groups based on actual risk, not static labels.
- num: Nearly 20% of bond trading volume is in baskets, requiring portfolio similarity metrics.
- Evaluation must prioritize operational validity over academic indices.

---


## Analyzing and Rewarding Credit Card Spending Habits in India: a Machine Learning Approach
**Filename:** `IA--Agrawal-et_al_summarized.md`  
**Authors:** Agrawal, R.; Khanna, A.; Hamdare, S. (2025)  
**ID:** `10.1007/s44196-025-00899-0`  
**Odin Topics:** 3.A, 5.A, 5.C, 11.A, 11.B, 12.B  

**TLDR:** K-Means clustering segments credit card users by spending habits, and a multi-factor reward points formula optimized with Random Forest achieves R2=0.99.

**Problem & Motivation:** Credit card reward programs in India use static, one-size-fits-all structures that fail to incentivize high-value discretionary spending or retain affluent customers. Existing methods lack real-time adaptability and personalization, especially during peak seasons like festivals. A data-driven framework is needed to align rewards with individual spending behaviors.

**Approach (summary):**
- Used original Kaggle dataset and generated synthetic dataset with Faker library to add features like income category, attrition risk, and expense type.
- Applied K-Means clustering to segment users into four clusters (Platinum, Gold, Silver, Signature) based on monthly spend, transaction frequency, and credit utilization.
- Engineered features including card promotion bonus, expense type bonus, income category bonus, and penalties for multiple cards to calculate reward points.

**Key Findings (selected):**
- num: Random Forest achieved R2=0.99, lowest RMSE and MAE among models.
- num: Mean reward points increased to approximately 1000 using synthetic dataset with additional features versus 400 in original.
- K-Means clustering achieved silhouette score 0.42, outperforming DBSCAN, Hierarchical, and GMM.
- Clusters clearly separated Platinum (high spending/luxury/travel) from Silver (low spending/essentials).

**Supports Odin (direct justifications):**
- K-Means clustering effectively segments users by spending behavior with silhouette score 0.42.
- Including expense type bonuses (e.g., +3 for travel) increases reward point distribution range.
- Random Forest achieves R2=0.99 for predicting reward points, minimizing prediction errors.

**Limitations / Contradictions for Odin:**
- Uses synthetic dataset instead of real credit card transaction data. [unacknowledged]
- Reward point multipliers are arbitrary and not calibrated with actual bank policies.
- Temporal analysis limited to 15 months of synthetic data, lacking long-term validation. [unacknowledged]

**Key takeaways:**
- K-Means silhouette score 0.42 outperforms DBSCAN and GMM for spending segmentation.
- Random Forest achieves R2=0.99, nearly perfect reward point prediction accuracy.
- Adding six behavioral factors expands reward range from 0-1000 to 0-3500.

---


## Digital Persona Modeling for Context-Aware Financial Decisioning
**Filename:** `IA--Sanhosh-&-Singh_summarized.md`  
**Authors:** R, Sai Sanhosh; Singh, Ashuosh Kumar (2025)  
**ID:** `c3d4e5f6-7890-4a5b-9cde-f01234567890`  
**Odin Topics:** 5.A, 5.C, 6.A, 7.B, 8.A, 10.A, 12.A, 12.B  

**TLDR:** Digital persona modeling integrates behavioral, contextual, and intent-driven attributes to enable context-aware financial decisioning for personalized budgeting, investment, and fraud detection.

**Problem & Motivation:** Static demographic profiles fail to capture dynamic user behavior and context in digital finance. Existing systems lack real-time adaptability to individual intent and situational factors. A unified framework for digital persona modeling is needed to enable personalized, trustworthy financial guidance.

**Approach (summary):**
- Proposes a five‑layer architecture: data acquisition, context engine, persona builder, decisioning model layer, and decision delivery with feedback.
- Uses a simulated hybrid dataset of transactional logs, mobile contextual logs, user profiles, and feedback labels to mimic mobile banking journeys.
- Implements Random Forest for classification, LSTM for sequential pattern analysis, and K‑Means for persona grouping.

**Key Findings (selected):**
- num: LSTM Neural Net achieved 93.6% accuracy, 94.4% precision, 91.8% recall, and 92.9% F1‑score on the simulated dataset.
- num: Random Forest achieved 91.2% accuracy, 90.4% precision, 89.9% recall, and 90.1% F1‑score.
- num: K‑Means clustering had 75.0% accuracy, showing lower suitability for classification tasks.
- LSTM outperforms other models due to its ability to model temporal dependencies in user behavior and context shifts.

**Supports Odin (direct justifications):**
- LSTM models capture temporal dependencies in financial behavior with 93.6% accuracy.
- Context‑aware risk function can adapt decisions to location, time, and device for fraud detection.
- Federated learning enables privacy‑preserving persona modeling without centralizing user data.

**Limitations / Contradictions for Odin:**
- Data privacy concerns: heavy reliance on sensitive user data increases breach risk. [acknowledged]
- Limited dataset diversity: synthetic data may introduce bias and reduce cross‑population applicability. [acknowledged]
- Model generalizability: LSTM may not generalize to fast‑evolving financial ecosystems. [acknowledged]

**Key takeaways:**
- LSTM achieved 93.6% accuracy for context‑aware financial decisions.
- Digital personas integrate behavioral, contextual, and intent‑driven attributes.
- Federated learning preserves user privacy while enabling personalization.

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
- {'Separate encoders handle each modality': 'temporal encoders for sequences, feedforward layers for static features, and embeddings for categorical variables.'}
- SSL pretext tasks include masked attribute prediction, temporal order prediction, and augmented view prediction.

**Key Findings (selected):**
- num: Proposed SSL achieves Silhouette score of 0.56, compared to K-Means (0.35) and XGBoost (0.41).
- num: SSL attains AUC of 0.91 for credit risk prediction, outperforming XGBoost (0.84).
- num: SSL reaches F1 of 0.81 for churn prediction, versus XGBoost (0.69).
- num: Removing temporal encoding causes a 4.2% drop in AUC, the largest decrease among ablated components.

**Supports Odin (direct justifications):**
- Self-supervised learning on multi-source financial data achieves 0.91 AUC for credit risk prediction.
- Removing temporal encoding reduces predictive performance by 4.2%, indicating its critical role.
- SSL-based representations yield Silhouette score 0.56, demonstrating coherent customer clusters.

**Limitations / Contradictions for Odin:**
- Single private bank dataset may not generalize across diverse Filipino young professionals. [unacknowledged]
- Interpretability of SSL representations is not addressed, limiting regulatory acceptance. [acknowledged as gap]
- No comparison to other SSL methods (e.g., SimCLR, MoCo) on financial data. [unacknowledged]

**Key takeaways:**
- SSL outperforms XGBoost by 7 points in AUC for credit risk prediction.
- Temporal encoding is the most critical component, causing a 4.2% drop.
- Multi-source data including web activity boosts profiling accuracy by 3.8%.

---


## Machine Learning in Financial Risk and Behavior Analysis: Predictive Insights on Bankruptcy, Fraud, and Consumer Trends in the USA
**Filename:** `IA--Begum_summarized.md`  
**Authors:** Begum, M. (2025)  
**ID:** `f47ac10b-58cc-4372-a567-0e02b2c3d479`  
**Odin Topics:** 5.A, 5.C, 6.A, 6.B, 8.A, 8.B  

**TLDR:** Evaluates machine learning models for bankruptcy prediction, fraud detection, and consumer spending forecasting, finding gradient boosting and LSTM outperform traditional methods.

**Problem & Motivation:** Traditional financial risk assessment methods struggle to capture nonlinear patterns, behavioral dynamics, and real-time anomalies. Machine learning offers improvements but faces challenges in generalizability, interpretability, and real-time adaptability. This paper proposes a unified ML framework to address these gaps across bankruptcy, fraud, and consumer behavior domains.

**Approach (summary):**
- For bankruptcy prediction, six models are trained: Logistic Regression, Random Forest, Gradient Boosting (XGBoost, LightGBM), SVM, ANN, and LSTM on financial ratios from SEC EDGAR and Moody's data.
- Fraud detection uses unsupervised Isolation Forest plus supervised classifiers (Logistic Regression, Random Forest, XGBoost) with SMOTE, a stacking ensemble, and a GRU-based RNN for sequential patterns.
- Consumer behavior analysis applies K-Means and DBSCAN clustering for customer segmentation, and ARIMA with LSTM for time-series forecasting of spending.

**Key Findings (selected):**
- num: XGBoost achieves the highest AUC (0.93) for bankruptcy prediction, followed by LSTM (0.92) and LightGBM (0.91).
- num: Stacking ensemble for fraud detection yields F1 of 0.89 and precision of 0.91, outperforming individual classifiers.
- num: LSTM reduces MAE to 2.8 and RMSE to 3.3 for consumer spending forecasting, compared to ARIMA's MAE of 4.2 and RMSE of 5.1.
- num: K-Means clustering produces a silhouette score of 0.68, indicating well-separated customer segments.

**Supports Odin (direct justifications):**
- LSTM achieves lower MAE (2.8) than ARIMA (4.2) for spending forecasting in consumer behavior.
- Stacking ensemble for fraud detection yields F1 of 0.89 and precision of 0.91.
- XGBoost reaches 0.93 AUC for bankruptcy prediction, demonstrating gradient boosting's strength on financial ratios.

**Limitations / Contradictions for Odin:**
- Models were trained on static historical datasets, not on live data streams.
- Real-world deployment would require continuous retraining and monitoring for evolving financial conditions.
- The study does not incorporate macroeconomic indicators or unstructured data (e.g., news, social media).

**Key takeaways:**
- XGBoost achieves 0.93 AUC for bankruptcy prediction.
- Stacking ensemble reaches 0.89 F1 in fraud detection.
- LSTM reduces MAE from 4.2 to 2.8 compared to ARIMA.

---


## Wealth-Voyager: Navigating Intelligent Wealth Management with a Multi-Agent Framework
**Filename:** `IA--Huang-et_al_summarized.md`  
**Authors:** Huang, R.; Zhao, Z.; Chen, S.; Wu, X.; Zhao, J. L. (2025)  
**ID:** `10.1145/3766918.3766944`  
**Odin Topics:** 5.A, 5.C, 10.B, 11.A, 12.A, 12.B  

**TLDR:** A multi-agent framework with behavioral profiling and real-time tactical adjustments outperforms a passive baseline, improving returns and reducing volatility.

**Problem & Motivation:** Traditional wealth advisory models lack scalability, cost-efficiency, and objectivity. Recent AI solutions remain fragmented, focusing on isolated tasks without integrating long-term strategy with behavioral adaptation. A unified framework is missing that combines quantitative rigor with interactive, cognitively-aware guidance.

**Approach (summary):**
- The system coordinates four specialized agents: AssistHub (behavioral profiling via dialogue), NewsCrawler (real-time market data), AlphaForge (constrained mean-variance optimization), and DualAdvisor (BDI-based role-playing simulation).
- A one-month user study with one mid-career participant (retirement goal, RMB 3M capital) was conducted under live market conditions from April 2 to May 2, 2025, including a tariff shock event.
- Strategic Asset Allocation (SAA) sets long-term weights; Tactical Asset Allocation (TAA) dynamically adjusts positions in response to real-time signals. Performance is benchmarked against a passive baseline and an anchored portfolio.

**Key Findings (selected):**
- num: The tactical strategy achieved a cumulative return of 1.86% vs 0.24% for the anchored portfolio over the evaluation period.
- num: Annualized volatility was reduced to 12.10% for tactical vs 13.70% for anchored, and annualized return improved by 2.81 percentage points vs original baseline.
- num: The anchored allocation improved annual return from 3.72% to 6.53% while cutting volatility from 18.08% to 9.42%.
- Qualitative user feedback indicated improved engagement, trust, and understanding due to explainable dialogue and bias exposure.

**Supports Odin (direct justifications):**
- Integrating behavioral bias vectors into user profiles improves risk-adjusted portfolio outcomes.
- Real-time tactical rebalancing triggered by news events outperforms static strategic allocation during market shocks.
- LLM-based role-playing between advisor and user agents surfaces cognitive biases and increases financial self-awareness.

**Limitations / Contradictions for Odin:**
- Evaluation was conducted on a single user with a specific retirement goal, limiting external validity. [unacknowledged]
- The asset universe was restricted to four classes (A-shares, bonds, gold, REITs); performance may differ with broader or different assets.
- System performance depends on the underlying LLM (GPT-4); cost and latency of LLM calls were not analyzed. [unacknowledged]

**Key takeaways:**
- Tactical adjustments added 1.62 percentage points over a passive baseline during a tariff shock.
- Behavioral anchoring alone nearly halved volatility from 18.08% to 9.42%.
- Dual-agent role-playing exposes cognitive biases through explainable dialogue.

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


## Study of an Adaptive Financial Recommendation Algorithm Using Big Data Analysis and User Interest Pattern with Fuzzy K‑Means Algorithm
**Filename:** `IA--Yang_summarized.md`  
**Authors:** Yang, J. (2024)  
**ID:** `10.1007/s44196-024-00719-x`  
**Odin Topics:** 5.A, 5.C, 6.A, 12.A, 12.B  

**TLDR:** An adaptive financial recommendation algorithm combining fuzzy K-means clustering and neural collaborative filtering on Hadoop processes big data to deliver personalized investment suggestions based on user interest patterns.

**Problem & Motivation:** Conventional financial services lack personalization and struggle with incomplete user interest patterns under changing market conditions, leading to suboptimal recommendations.

**Approach (summary):**
- Implements fuzzy K-means clustering on Hadoop with MapReduce for scalable processing of large financial datasets.
- Creates adaptive user profiles using fuzzy logic to handle uncertainty in preferences and cluster users by financial patterns.
- Applies neural collaborative filtering with multi-layer perceptron to predict user interests in financial products.

**Key Findings (selected):**
- num: Highest average silhouette score of 0.690 for cluster 2, indicating well-separated user groups.
- num: Lower MSE than baseline algorithms, demonstrating improved recommendation accuracy.
- num: Precision@k and recall@k consistently outperform existing methods across k values.
- num: Processing time reduced to linear complexity from quadratic in similarity calculations.

**Supports Odin (direct justifications):**
- Fuzzy K-means clustering achieves silhouette scores up to 0.690 for user segmentation.
- Neural collaborative filtering reduces MSE compared to baseline algorithms.
- Processing time complexity improves from quadratic to linear for user similarity calculations.

**Limitations / Contradictions for Odin:**
- Paper does not address cold-start problem for new users [unacknowledged].
- Evaluation uses synthetic or specific dataset; generalizability to other financial domains not proven [unacknowledged].
- Real-time adaptation requires continuous data streams, but latency for large-scale Hadoop jobs may limit true real-time performance [unacknowledged].

**Key takeaways:**
- Fuzzy K-means clustering achieved silhouette score of 0.690 for optimal user grouping.
- Neural collaborative filtering lowered MSE significantly below baseline methods.
- Processing time improved from quadratic to linear complexity.

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
- num: Profit quartile spread across risk ranges increases with risk level, indicating challenge in high-risk areas.
- num: Learning rate limited to 0.001-0.01 with thousands of trees to prevent overfitting.
- Revenue model and total profit model show poor forecasting performance but better ranking performance.
- Hump-shaped relationship between profit component and risk is retained between predicted and actual curves.

**Supports Odin (direct justifications):**
- Supervised learning on debit/credit transactions and loan applications enables accurate customer profiling.
- Profit-based modeling yields higher average profitability than risk-only scoring.
- Community discovery algorithms effectively detect gang fraud in credit applications.

**Limitations / Contradictions for Odin:**
- Model performance is poor for revenue and total profit forecasting at high risk levels.
- No discussion of data privacy implications for customer profiling. [unacknowledged]
- Lacks validation on non-US or Filipino demographic data. [unacknowledged]

**Key takeaways:**
- XGBoost profit models outperform risk-only models in ranking profitability.
- Profit and risk have a non-monotonic hump-shaped relationship.
- Community discovery algorithms effectively detect gang fraud in credit data.

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

**Supports Odin (direct justifications):**
- User profiling enables precise marketing and risk control in financial platforms.
- K‑means clustering groups users with similar characteristics for targeted analysis.
- Tag systems with objective or subjective weighting improve user segmentation.

**Limitations / Contradictions for Odin:**
- No quantitative validation of profiling accuracy or business impact. [unacknowledged]
- K‑means assumes spherical clusters and requires choosing K, which may not suit all user data. [unacknowledged]
- Data integration across industries raises privacy and consent issues not discussed. [unacknowledged]

**Key takeaways:**
- User profiling combines explicit and implicit data for comprehensive insights.
- Four‑layer architecture separates collection, storage, processing, and visualization.
- Tag management with fact and model tags enables flexible user segmentation.

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


## A Survey of Large Language Models for Financial Applications: Progress, Prospects and Challenges
**Filename:** `IA--Nie-et_al_summarized.md`  
**Authors:** Nie, Y.; Kong, Y.; Dong, X.; Mulvey, J. M.; Poor, H. V.; Wen, Q.; Zohren, S. (2024)  
**ID:** `arxiv:2406.11093`  
**Odin Topics:** 5.A, 6.A, 6.B, 7.A, 7.B, 8.A, 8.B, 10.A, 10.B, 12.A, 12.B  

**TLDR:** A survey of large language models applied to finance, covering linguistic tasks, sentiment analysis, time series forecasting, financial reasoning, and agent-based modeling, along with challenges and benchmarks.

**Problem & Motivation:** Financial applications require processing vast unstructured data and complex reasoning. Traditional deep learning methods struggle with long-term dependencies and context understanding. LLMs offer advanced contextual understanding and transfer learning, but a comprehensive overview of their financial applications and challenges is lacking.

**Approach (summary):**
- The survey categorizes existing literature into key application areas: linguistic tasks, sentiment analysis, financial time series analysis, financial reasoning, and agent-based modeling.
- It analyzes domain-specific LLMs (FinBERT, BloombergGPT, etc.) and compares zero-shot vs fine-tuning approaches.
- The paper compiles datasets, benchmarks, and code resources for financial LLM research.

**Key Findings (selected):**
- num: ChatGPT can achieve a monthly three-factor alpha of up to 3% when generating portfolios from policy news.
- FinBERT shows enhanced resilience against adversarial attacks compared to keyword-based sentiment methods.
- LLM-based agents with layered memory (FINMEM) improve trading decisions in volatile financial environments.
- Zero-shot LLMs can forecast time series without explicit training by tokenizing numerical data appropriately.

**Supports Odin (direct justifications):**
- LLMs can forecast stock returns from news headlines with higher Sharpe ratios than traditional models (Lopez-Lira & Tang, 2023).
- Instruction-tuned LLMs enhance financial sentiment analysis numerical sensitivity (Zhang et al., 2023).
- Multi-agent LLM frameworks improve anomaly detection efficiency in financial markets (Park, 2024).

**Limitations / Contradictions for Odin:**
- Lookahead bias in backtesting financial LLMs requires careful data anonymization.
- High computational cost and inference speed limit real-time deployment.
- Lack of standardized evaluation benchmarks for LLM-based trading strategies.

**Key takeaways:**
- LLMs can achieve 3% monthly alpha in portfolio generation from policy news.
- Zero-shot LLMs forecast time series without task-specific training.
- Multi-agent LLM systems enhance anomaly detection and sentiment analysis.

---


## MOTIVATIONAL FACTORS AND BEHAVIORAL INTENTION TO INVEST IN PHILIPPINE STOCK MARKET AMONG MILLENNIAL AND GEN-Z INVESTORS IN CALAMBA CITY
**Filename:** `L--Sanchez_summarized.md`  
**Authors:** Sanchez, M. Q. C. (2024)  
**ID:** `10.5281/zenodo.12730500`  
**Odin Topics:** 1.C, 5.A  

**TLDR:** Examines motivational factors (financial knowledge, well-being, overconfidence bias, investment risk) influencing behavioral intention to invest in Philippine stock market among Millennial and Gen-Z investors in Calamba City.

**Problem & Motivation:** Only 1% of Filipino adults hold equity securities despite rising overall investment ownership. Young Filipinos face job insecurity, perceived high costs, and low trust in providers. Limited research exists on specific motivational factors driving Millennial and Gen-Z stock market participation in the Philippines.

**Approach (summary):**
- Descriptive-correlational survey of 265 Laguna College of Business and Arts graduates (130 Millennials, 130 Gen Z) from Calamba City.
- Used Theory of Planned Behavior (TPB) as framework with four-point Likert scales for motivational factors (financial knowledge, well-being, overconfidence bias, investment risk) and behavioral intention (attitude, subjective norm, perceived behavioral control).
- Adopted validated instruments from Yang et al. (2021) and Schmidt (2010) with Cronbach's alpha >0.86 for all constructs.

**Key Findings (selected):**
- num: Low positive correlation (r=.172 to .372) between motivational factors and behavioral intention across all sub-variables (p<.01).
- num: Significant difference between Millennials and Gen Z in overconfidence bias (p=.048) and investment risk perception (p=.000), but no difference in financial knowledge (p=.195) or financial well-being (p=.075).
- num: Financial well-being indicator 'securing my financial future' had highest mean (3.35), while 'I am behind with my finances' had lowest (2.58), indicating aspiration-reality gap.
- num: Investment risk indicator 'prefer to invest in stocks rather than keep money in bank' scored 3.20 (highest), while 'consider myself a high-risk taker' scored 2.77 (lowest).

**Supports Odin (direct justifications):**
- Low positive correlation (r=.172-.372) exists between motivational factors and behavioral intention to invest.
- Millennial and Gen-Z investors show a gap between financial aspirations and current financial status.
- Overconfidence bias and investment risk perception differ significantly between Millennials and Gen Z.

**Limitations / Contradictions for Odin:**
- Sample restricted to LCBA graduates in Calamba City; findings may not generalize to other regions or educational backgrounds. [unacknowledged]
- Cross-sectional design prevents causal inference between motivational factors and behavioral intention. [unacknowledged]
- No response from original instrument authors for permission to adopt scales, though validity statistics are reported.

**Key takeaways:**
- Low positive correlation (r=.172-.372) links motivation to investment intention.
- Millennials and Gen Z differ in overconfidence and risk perception.
- Financial knowledge shows no generational difference among young Filipinos.

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


## "I deserve this": A phenomenological study toward online impulse buying behavior of service contractors
**Filename:** `L--Somera_summarized.md`  
**Authors:** Somera, K. (2024)  
**ID:** `10.69569/jip.2024.0257`  
**Odin Topics:** 1.A, 1.C, 5.A  

**TLDR:** Online impulse buying among Filipino service contractors serves as a coping mechanism for stress and negative emotions, rewarding hard work, but leads to financial stress and guilt.

**Problem & Motivation:** Research on online impulse buying has focused on other demographics, leaving service contractors' lived experiences unexplored. Understanding their behavior is crucial given the precarious nature of contract work and rising digital marketplace use. The study aims to reveal the meanings behind their 'I deserve this' justification.

**Approach (summary):**
- Qualitative phenomenological study using Interpretative Phenomenological Analysis (IPA) to explore lived experiences.
- Ten Filipino service contractors aged 20-30 from Aurora province participated, selected via high scores (≥31) on the Impulse Buying Scale.
- Semi-structured online interviews were conducted via Google Meet, with questions validated by psychologists and delivered in Filipino.

**Key Findings (selected):**
- Online impulse buying intensified during COVID-19 pandemic as a coping mechanism for loneliness and stress.
- Service contractors use impulse buying to escape negative emotions, achieve immediate gratification, and regulate mood.
- Positive impacts include sense of achievement, stress alleviation, and mood regulation, with participants describing it as therapeutic.
- Negative impacts include financial stress and feelings of guilt and regret, especially when bills accumulate or savings are depleted.

**Supports Odin (direct justifications):**
- Online impulse buying serves as a coping mechanism for work-related stress among Filipino service contractors.
- Impulse buying provides immediate gratification and mood regulation despite leading to financial stress.
- The phrase 'I deserve this' reflects a self-reward justification for unplanned purchases.

**Limitations / Contradictions for Odin:**
- Small sample size (N=10) limits generalizability. [unacknowledged]
- Qualitative design cannot establish causality. [unacknowledged]
- No longitudinal data to assess long-term consequences of impulse buying. [unacknowledged]

**Key takeaways:**
- Impulse buying intensifies as a coping mechanism under stress.
- The 'I deserve this' phrase justifies unplanned spending as self-reward.
- Financial stress and guilt follow initial positive emotions from impulse buying.

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


## Impact of financial behaviour on financial well‑being: evidence among young adults in Malaysia
**Filename:** `I--Sabri-et_al_summarized.md`  
**Authors:** Sabri, M. F.; Anthony, M.; Law, S. H.; Rahim, H. A.; Burhan, N. A. S.; Ithnin, M. (2023)  
**ID:** `10.1057/s41264-023-00234-8`  
**Odin Topics:** 1.C, 5.A  

**TLDR:** Financial behaviour fully mediates the relationship between financial literacy, financial socialisation, self-control, financial technology and financial well-being among young Malaysian adults during COVID-19.

**Problem & Motivation:** Young adults in Malaysia faced income loss, debt, and housing issues during COVID-19, yet prior research on their financial well-being was mostly descriptive. The mediating role of financial behaviour between key determinants and well-being remained underexplored.

**Approach (summary):**
- Survey of 360 young Malaysians aged 18-29 using multi-stage random sampling from five regions.
- Structural equation modelling (SEM) with bootstrapping (1000 samples) to test mediation.
- Measures: financial literacy, financial behaviour, financial socialisation, self-control, financial technology, and financial well-being (CFPB scale).

**Key Findings (selected):**
- num: Financial behaviour fully mediates the effect of financial literacy on financial well-being (indirect β=0.071, p<0.05).
- num: Financial behaviour mediates the effect of financial socialisation (indirect β=0.19, p<0.05), self-control (β=0.05), and financial technology (β=0.01).
- num: Financial behaviour has a direct positive effect on financial well-being (β=0.48, p<0.05).
- Financial literacy alone has no direct effect on financial well-being (β=0.09, p>0.05).

**Supports Odin (direct justifications):**
- Financial behaviour fully mediates the effect of financial literacy on financial well-being.
- Financial technology alone does not improve financial well-being without positive financial behaviour.
- Self-control alone is not sufficient; financial behaviour is the key pathway.

**Limitations / Contradictions for Odin:**
- Sample only from Malaysia, limiting generalizability to Filipinos [unacknowledged].
- Cross-sectional design prevents causal inference; paper acknowledges this.
- No objective financial data, only self-reports.

**Key takeaways:**
- Financial behaviour fully mediates the link from literacy to well-being.
- Fintech alone does not improve well-being without behaviour change.
- Self-control matters only through actual financial actions.

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
- {'Dependent variables': 'ownership of formal accounts (bank, e-money, cooperative, microfinance) and use of financial services (credit, investment, insurance).'}

**Key Findings (selected):**
- num: A one-standard-deviation increase in financial literacy raises likelihood of account ownership by 3.7-4.2 percentage points.
- num: A one-point increase in financial literacy score increases likelihood of availing a financial service by 4.9-6.0 percentage points.
- num: Financial literacy increases bank account ownership by 2.1 percentage points and investment ownership by 3.7-4.2 percentage points.
- Awareness of BSP financial education programs and being the main household financial decision-maker are strong positive drivers of inclusion.

**Supports Odin (direct justifications):**
- Financial literacy increases the probability of owning a bank account by 2.1 percentage points per standard deviation.
- Being the main household financial decision-maker raises likelihood of using financial services by 24-34 percentage points.
- Awareness of financial education programs positively correlates with account ownership and investment uptake.

**Limitations / Contradictions for Odin:**
- Uses only three financial literacy questions, which may not capture full construct (acknowledged).
- Cross-sectional design prevents causal inference [unacknowledged].
- Sample of 1,200 may not fully represent all Filipino subgroups [unacknowledged].

**Key takeaways:**
- Financial literacy raises account ownership by 3.7-4.2 percentage points.
- Being main financial decision-maker increases service use by 24-34 percentage points.
- Awareness of BSP programs strongly predicts bank account ownership.

---


## Impact of Mental Representation on Consumer Behaviors: Implications for Mental Budgeting and Prediction Algorithm Preferences
**Filename:** `I--Fei_summarized.md`  
**Authors:** Fei, L. (2023)  
**ID:** `123e4567-e89b-12d3-a456-426614174000`  
**Odin Topics:** 3.A, 5.A, 6.B, 7.A, 7.C, 12.A  

**TLDR:** Mental representation of expenditures forms a hierarchical taxonomy that predicts spending adjustment based on taxonomic distance, and people prefer prediction algorithms that replicate the event being predicted.

**Problem & Motivation:** Consumers often deviate from budgets, but existing budgeting theories assume single-level categories and cannot explain how people adjust spending across related items. Understanding how mental representation drives spending decisions and algorithm preferences is crucial for improving personal finance systems.

**Approach (summary):**
- Study 1a used successive pile-sort with 27 MTurk participants to elicit hierarchical taxonomies of 38 common expenditures, recovering consensus via Cultural Consensus Model.
- Study 1b tested stability of taxonomies over three months with 50 participants.
- Studies 2a-2c measured self-reported spending adjustment and substitutability/complementarity ratings to isolate taxonomic distance effects.

**Key Findings (selected):**
- num: 27 participants showed consensus in hierarchical expenditure representations (first latent root ratio > 3:1).
- num: Taxonomic distance significantly predicted spending adjustment, with closer items adjusted 31% more than distant items (Study 2a).
- Taxonomic distance effects persisted even after controlling for substitutability and complementarity (Study 2c).
- num: In grocery data, a sale on an item increased spending on taxonomically close items by 12% compared to distant items.

**Supports Odin (direct justifications):**
- Overspending on an item leads to greater spending reduction on taxonomically close items than distant items.
- Users prefer prediction algorithms that replicate the event's generative process over statistical models with equal accuracy.
- Hierarchical expenditure taxonomies are consensual and stable over time, enabling personalization from cold start.

**Limitations / Contradictions for Odin:**
- Lab studies use hypothetical scenarios; real behavior may differ. [unacknowledged]
- Grocery data analysis cannot confirm individual budget tracking; assumes average effects.
- Sample sizes in pile-sort studies (N=27, N=50) are modest for consensus modeling.

**Key takeaways:**
- Taxonomic distance predicts spending adjustment more than substitutability alone.
- Consumers share a consensual hierarchical representation of common expenditures.
- People prefer prediction algorithms that replicate the event's generative process.

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


## Behavior-Driven Personalization Framework to Improve Repeat Usage in Mobile-Enabled Financial Ecosystems
**Filename:** `I--Omotayo-et_al_summarized.md`  
**Authors:** Omotayo, K. V.; Uzoka, A. C.; Okolo, C. H.; Olinmah, F. I.; Adanigbo, O. S. (2023)  
**ID:** `10.62225/2583049X.2023.3.6.4736`  
**Odin Topics:** 5.A, 9.A, 10.A, 10.B, 11.A, 11.B, 12.A  

**TLDR:** A behavior-driven personalization framework using real-time user data, segmentation, and adaptive triggers improves repeat usage in mobile financial apps via continuous learning and ethical nudges.

**Problem & Motivation:** Mobile financial platforms face low repeat usage due to generic, non-responsive experiences. Static personalization fails to capture evolving user behavior. A behaviorally intelligent framework is needed to sustain engagement and support financial goals.

**Approach (summary):**
- The framework comprises three layers: behavioral data capture, dynamic segmentation engine, and personalized trigger system.
- It integrates behavioral science principles like nudges, loss aversion, and choice architecture.
- A continuous feedback loop refines personalization based on user responses.

**Key Findings (selected):**
- Behavior-driven personalization enhances relevance and habit formation compared to static methods.
- Real-time segmentation enables adaptive interventions that align with user intent.
- Continuous learning reduces notification fatigue and cognitive overload.
- Ethical personalization promotes positive financial behaviors and user trust.

**Supports Odin (direct justifications):**
- Behavior-driven personalization increases repeat usage by aligning interventions with real-time user behavior.
- Dynamic segmentation improves the relevance of financial nudges and feature recommendations.
- Continuous learning from user responses reduces notification fatigue and cognitive overload.

**Limitations / Contradictions for Odin:**
- No empirical validation or real-world implementation results. [unacknowledged]
- The framework lacks concrete algorithmic details for segmentation and trigger optimization.
- Ethical safeguards are described at a high level without operational guidelines.

**Key takeaways:**
- Personalization must adapt to evolving user behavior in real time.
- Ethical nudges preserve user autonomy while promoting financial health.
- Continuous feedback loops are essential for reducing notification fatigue.

---


## Data Science and Business Analytics Approaches to Financial Wellbeing: Modeling Consumer Habits and Identifying At-Risk Individuals in Financial Services
**Filename:** `IA--Machireddy_summarized.md`  
**Authors:** Machireddy, J. (2023)  
**ID:** `a1b2c3d4-e5f6-7890-1234-567890abcdef`  
**Odin Topics:** 5.A, 5.B, 5.C, 6.A, 8.A, 8.B, 10.A, 10.B, 13.B  

**TLDR:** Data science models using transaction data and digital footprints can profile consumer financial behavior, identify at-risk individuals, and support ethical risk management through explainable AI.

**Problem & Motivation:** Financial hardship from over-indebtedness and income volatility affects many consumers, leading to defaults and economic instability. Traditional credit scoring uses limited variables and static updates, failing to capture real-time behavioral signals. There is a need for data-driven approaches to model financial habits and detect early warning signs.

**Approach (summary):**
- Extract behavioral features from transactional data including income volatility, discretionary spending percentage, and liquidity trends.
- Apply machine learning models such as gradient boosting, hidden Markov models, and autoencoders for risk prediction and anomaly detection.
- Incorporate psychological traits and contextual factors like life events and economic conditions to enrich consumer profiles.

**Key Findings (selected):**
- Transactional and digital footprint data enable dynamic financial health portraits that shift in real time.
- Machine learning models can detect early warning signs of financial distress such as income drops or rising credit reliance before default occurs.
- Explainable AI techniques improve consumer trust and allow regulators to verify fair decision-making.
- Consumer segmentation by financial vulnerability allows targeted interventions like debt relief or budgeting tools.

**Supports Odin (direct justifications):**
- Transaction history features like income volatility and liquidity trends predict financial distress.
- Unsupervised anomaly detection can identify sudden behavioral changes without labeled data.
- Explainable AI techniques must accompany risk models to maintain consumer trust.

**Limitations / Contradictions for Odin:**
- No empirical results or quantitative evaluation of proposed models.
- Does not address the cold-start problem for new users with no transaction history.
- Real-time streaming infrastructure requirements are assumed but not detailed.

**Key takeaways:**
- Transaction data alone is insufficient; psychological and contextual factors improve risk models.
- Explainable AI like SHAP is necessary for regulatory compliance and consumer trust.
- Consumer segmentation enables targeted interventions such as debt restructuring or coaching.

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


## Influences of mental accounting on consumption decisions: asymmetric effect of a scarcity mindset
**Filename:** `I--Cheng-et_al_summarized.md`  
**Authors:** Cheng, L.; Yu, Y.; Wang, Y.; Zheng, L. (2023)  
**ID:** `10.3389/fpsyg.2023.1162916`  
**Odin Topics:** 1.C, 2.C, 5.A, 7.A  

**TLDR:** Mental accounting influences hedonic vs utilitarian consumption; scarcity mindset asymmetrically reduces hedonic spending from windfall gains but does not affect hard-earning money.

**Problem & Motivation:** Previous research established that mental accounting affects consumption, but the role of a scarcity mindset as a boundary condition remained unclear. Understanding this interaction is important because scarcity mindset alters how consumers process financial resources. The gap is that prior work did not examine asymmetric effects across windfall versus hard-earning gains.

**Approach (summary):**
- Conducted online experiments with two samples: 319 Chinese college students and 294 Chinese adults.
- Used a 2 (mental account: windfall vs hard-earning) × 2 (consumption: hedonic vs utilitarian) between-subjects design.
- Measured scarcity mindset using a three-item self-report scale (Pitesa and Thau, 2018) on a 5-point Likert scale.

**Key Findings (selected):**
- num: Consumers with windfall gains were more likely to choose hedonic consumption (student sample: Cohen's d=0.68, p<0.001; adult sample: d=0.38, p=0.001).
- Scarcity mindset moderated the windfall-to-hedonic effect for students (B=−0.66, p=0.026) and adults (B=−1.28, p<0.001).
- Under high scarcity mindset, windfall gains did not increase hedonic preference; effect was significant only under low scarcity.
- For hard-earning gains, scarcity mindset did not significantly affect utilitarian vs hedonic choices (adult sample p=0.212).

**Supports Odin (direct justifications):**
- Consumers with high scarcity mindset reduce hedonic spending from windfall gains (Cheng et al., 2023).
- Mental accounting leads to non-fungible treatment of money, affecting category-specific budgets.
- Scarcity mindset does not alter utilitarian spending from hard-earning money.

**Limitations / Contradictions for Odin:**
- Self-reported scarcity mindset scale may not capture actual resource constraints. [unacknowledged]
- Only two product types per condition; lacks generalizability to real-world choices. [unacknowledged]
- No manipulation check for mental accounting condition. [unacknowledged]

**Key takeaways:**
- Windfall gains increase hedonic spending; scarcity mindset blocks this effect.
- Hard-earning money consistently drives utilitarian consumption regardless of scarcity.
- num: Scarcity mindset reduced hedonic preference with B=−0.66 (students) and B=−1.28 (adults).

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
- {'Descriptive and content analysis applied to four research themes': 'user profile, relationship with traditional finance, financing experience, and post-financing outcomes including COVID-19 impact.'}

**Key Findings (selected):**
- num: 44% of P2P consumer lending users aged 25-34; 54% of BNPL users aged 25-34.
- num: 49% of P2P consumer borrowers used funds for day-to-day expenses; 39% of BNPL for fashion and apparel.
- num: 1% of P2P consumer borrowers defaulted, compared to >3% average bank NPL in ASEAN (World Bank).
- num: 65% of MSMEs reported increased productivity after receiving fintech financing; 59% increased profit.

**Supports Odin (direct justifications):**
- Fintech platforms serve underbanked populations, with 41% of P2P consumer lending borrowers being female.
- Most MSMEs (65%) report increased productivity after receiving fintech financing.
- Fintech complements traditional banking: over half of borrowers increased use of savings accounts after borrowing.

**Limitations / Contradictions for Odin:**
- The study does not measure loan quality, price, or diversity of offers. [unacknowledged]
- Sample size limitations prevent cross-country comparative analysis.
- No analysis of herd behavior or anchoring in platform choice. [unacknowledged]

**Key takeaways:**
- 1% of P2P consumer borrowers default, below regional bank NPL averages.
- Millennials make up 44% of P2P consumer lending users in ASEAN.
- Fintech complements banking: 52% of users increased savings account use.

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


## Mapping Financial Mindsets: A Two-Stage Unsupervised Framework for Behavioral Profiling Using High-Dimensional Psychometric Data
**Filename:** `IA--Rabinovich-et_al_summarized.md`  
**Authors:** Rabinovich, I.; Rabinovich, R.; Ashburn, N.; DeGeare, M. (0)  
**ID:** `d9e6e8a0-5c7f-5b3a-9f2e-4c8b7a6d5e4f`  
**Odin Topics:** 5.A, 5.B, 5.C, 12.A, 12.B  

**TLDR:** A two-stage unsupervised framework using UMAP and spectral clustering identifies interpretable financial behavioral profiles from psychometric data, validated across two datasets.

**Problem & Motivation:** Traditional financial segmentation relies on spending or demographics, overlooking psychological factors. This limits understanding of financial decision-making and personalized interventions. A method to capture latent behavioral-psychological patterns is needed.

**Approach (summary):**
- Organize survey items into conceptual domains (e.g., motivation, financial behavior).
- Produce unidimensional domain scores via anchor-based projection after UMAP embedding, or weighted averages for binary domains.
- Apply second-stage UMAP to domain scores, then spectral clustering to identify profiles.

**Key Findings (selected):**
- num: Clustering yields silhouette scores of 0.569 (proprietary) and 0.500 (CFPB).
- num: Cluster membership explains 61% variance in perceived financial health (proprietary) and 44% in CFPB.
- num: Demographics alone explain only 9% variance in cluster membership (McFadden pseudo-R²=0.091 proprietary, 0.061 CFPB).
- Profiles are psychologically interpretable and not reducible to a single severity dimension.

**Supports Odin (direct justifications):**
- Unsupervised learning can reveal psychologically meaningful financial profiles not captured by demographics.
- Anchor-based projection produces sample-independent domain scores.
- Cluster membership explains more variance in financial health than income or education.

**Limitations / Contradictions for Odin:**
- All data from US populations; generalizability to other countries unknown. [unacknowledged]
- Self-report measures may not capture actual financial behaviors. [acknowledged]
- Proprietary dataset is modest in size and non-probability sample. [acknowledged]

**Key takeaways:**
- Two-stage UMAP and spectral clustering yields interpretable financial profiles.
- Clusters explain up to 61% of variance in perceived financial health.
- Demographics alone explain less than 10% of cluster membership.

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
- {'num': 'Digital wallet usage explains 45.4% of the variance in financial behavior (R²=0.454, F=180.136, p<.001).'}
- Students agree on all adoption determinants (means 2.91–2.99), with perceived trust showing the highest variability (SD=1.24).
- Financial behavior is generally responsible (overall M=2.99, SD=0.68), with financial planning and budgeting scoring highest (M=3.00).
- Regression beta coefficient (β=0.673, p<.001) indicates a significant positive effect of digital wallet usage on financial behavior.

**Supports Odin (direct justifications):**
- Digital wallet usage significantly predicts financial behavior among students (β=0.673, p<.001).
- Students generally exhibit responsible financial behavior in cash management (M=2.97) and budgeting (M=3.00).
- Perceived trust shows the highest variability (SD=1.24), indicating divided opinions on platform reliability.

**Limitations / Contradictions for Odin:**
- Cross-sectional design cannot infer causation; only association is shown. [unacknowledged]
- Reliance on self-reported Likert scales may introduce response bias. [unacknowledged]
- The study does not control for income level, digital literacy, or parental influence. [unacknowledged]

**Key takeaways:**
- Digital wallet usage explains 45.4% of financial behavior variance.
- Students agree on all adoption determinants with means from 2.91 to 2.99.
- Perceived trust shows the widest disagreement (SD=1.24).

---


## Machine Learning Techniques for Optimizing Recurring Billing and Revenue Collection in SaaS Payment Platforms
**Filename:** `IA--Dlamini_summarized.md`  
**Authors:** Dlamini, A. (0)  
**ID:** `8a7b6c5d-4e3f-2a1b-9c8d-7e6f5a4b3c2d`  
**Odin Topics:** 5.A, 6.A, 6.B, 8.A, 8.B, 11.A, 11.B  

**TLDR:** Machine learning techniques optimize recurring billing, detect anomalies, forecast churn and revenue, and adapt pricing in SaaS payment platforms.

**Problem & Motivation:** Recurring billing in SaaS platforms suffers from payment failures, fraud, and churn due to dynamic user behavior and rigid rule-based systems. Traditional methods lack adaptability to evolving patterns and high-volume transactional data. Machine learning offers scalable solutions for proactive revenue management.

**Approach (summary):**
- Data preprocessing includes cleansing, normalization, missing value imputation, and feature engineering from payment logs and usage metrics.
- Linear and logistic regression with regularization provide interpretable baselines for fraud and churn prediction.
- Ensemble methods like random forests and gradient boosting machines achieve high accuracy by combining multiple weak learners.

**Key Findings (selected):**
- Ensemble methods like gradient boosting achieve high accuracy in fraud detection and churn forecasting.
- Autoencoders effectively detect anomalous transactions by measuring reconstruction error without labeled fraud data.
- Reinforcement learning optimizes dunning schedules and pricing strategies, maximizing revenue while minimizing churn.
- Linear algebra techniques (PCA, SVD) reduce dimensionality, improving computational efficiency and interpretability.

**Supports Odin (direct justifications):**
- Machine learning models can forecast the probability of successful recurring payments.
- Ensemble methods like random forests enhance fraud detection accuracy in payment systems.
- Autoencoders identify anomalous transactions by measuring reconstruction error.

**Limitations / Contradictions for Odin:**
- Lacks quantitative empirical results or benchmark comparisons. [unacknowledged]
- Does not address real-time inference latency constraints for mobile PFMS. [unacknowledged]
- Privacy-preserving methods (federated learning) are mentioned but not evaluated. [unacknowledged]

**Key takeaways:**
- Ensemble tree models often outperform linear baselines for churn and fraud prediction.
- Autoencoders provide unsupervised anomaly detection without labeled fraud data.
- Reinforcement learning dynamically optimizes pricing and dunning strategies.

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