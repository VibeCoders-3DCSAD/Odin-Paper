# Comprehensive Report for Subtopic: `10.B`

**Total relevant papers:** 31

This report includes problem/motivation, approach, key findings, support for Odin, and limitations/contradictions.

---


## AI-Enabled NLP Framework for Automated Expense Management and Financial Analysis
**Filename:** `IA--Jayaprakashnarayan-et_al_summarized.md`  
**Authors:** Jayaprakashnarayan, N.; Sakthivel, M.; Sachidhanandam, P.; Kanjana Devi, N.; Manivel Mughilan, T.S. (2026)  
**ID:** `10.15662/IJEETR.2026.0802073`  
**Odin Topics:** 3.A, 3.B, 8.A, 8.B, 10.A, 10.B, 12.A, 12.B  

**TLDR:** An AI-enabled NLP framework using transformer-based models and multi-task learning automates transaction extraction (96.8% accuracy) and categorization (94.3% merchant precision) from financial SMS messages with on-device privacy.

**Problem & Motivation:** Digital payments generate overwhelming transaction data, making personal finance management complex and error-prone. Existing rule-based or supervised systems are brittle, unable to adapt to changing message formats or evolving fraud patterns. There is a need for a self-adaptive, privacy-preserving NLP framework that operates on mobile devices.

**Approach (summary):**
- Curated dataset of 124,583 financial SMS messages from 250 Indian participants across 42 banks and 18 UPI apps, annotated with transaction entities and 14 expense categories.
- Hybrid architecture combining MuRIL transformer encoder (12 layers, 768 hidden) with rule-based verification for entity extraction and multi-task learning for classification.
- Multi-task objective jointly optimizes token-level CRF for entities and sequence-level softmax for expense categories, with dynamic loss weights (0.7/0.3).

**Key Findings (selected):**
- num: 96.8% overall F1-score for transaction entity extraction (proposed MuRIL multi-task vs 94.0% for FinBERT).
- num: 94.3% precision in merchant identification across code-mixed and varied formats.
- num: 91.7% sensitivity and 3.8% false positive rate for ensemble fraud detection (AUC-ROC 0.956).
- num: 85.6% reduction in manual expense tracking effort based on user-reported time savings.

**Supports Odin (direct justifications):**
- The proposed NLP framework achieves 96.8% accuracy in extracting transaction entities from financial SMS messages.
- Multi-task learning improves transaction classification F1 by 1.2% over single-task fine-tuning.
- Ensemble fraud detection achieves 91.7% sensitivity with only 3.8% false positives, suitable for user-facing alerts.

**Limitations / Contradictions for Odin:**
- Geographic generalizability not evaluated; results may not transfer to non-Indian payment ecosystems. [unacknowledged]
- On-device model quantization causes 1.3% accuracy loss compared to full-precision model, affecting millions of transactions.
- Battery impact of 2% per hour on low-end devices may reduce user adoption for high-volume users (300+ daily transactions).

**Key takeaways:**
- Transaction extraction achieves 96.8% F1 using transformer multi-task learning on Indian financial SMS.
- Ensemble fraud detection yields 91.7% sensitivity with only 3.8% false positives.
- On-device processing reduces manual expense tracking effort by 85.6% while preserving privacy.

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


## Enhancing Financial Literacy and Personal Investment Decisions Through AI and Machine Learning
**Filename:** `IA--Praveen-et_al_summarized.md`  
**Authors:** Praveen, R. V. S.; Vemuri, H. K.; Peri, S. S. S. R. G.; Sista, S.; Saxena, V.; Saxena, P. (2025)  
**ID:** `c4a8b6d2-f3e5-4a7c-9b1d-2e3f4a5b6c7d`  
**Odin Topics:** 4.A, 4.B, 10.A, 10.B, 11.A, 12.A  

**TLDR:** AI and ML tools significantly improve financial literacy and investment confidence, with higher engagement and usage frequency yielding greater gains.

**Problem & Motivation:** A substantial portion of the global population lacks basic financial literacy, making them vulnerable to poor investment choices. Traditional financial education methods fail to produce lasting behavioral change. AI and ML offer personalized, adaptive solutions, but their integration into personal finance faces gaps in explainability, trust, and ethical design.

**Approach (summary):**
- {'Mixed-methods design with three phases': 'tool analysis of 20 AI-driven financial platforms, survey of 524 users (aged 18-50, minimum 3 months usage), and semi-structured interviews with 33 participants.'}
- Quantitative measures included pre/post financial literacy scores (OECD/INFE framework), investment confidence (5-point Likert), and AI engagement scores.
- {'Analytical techniques': 'paired t-tests, Pearson correlation, regression, and cluster analysis using SPSS and Python.'}

**Key Findings (selected):**
- {'num': 'Mean financial literacy score increased 1.1 points (from 5.5 to 6.6, p < 0.01) after AI tool use.'}
- {'num': 'Over 65% of users reported high investment confidence (levels 4 or 5) post-intervention.'}
- {'num': 'Correlation between AI engagement and literacy gain was r = 0.31 (moderate positive).'}
- {'num': 'Users with >5 weekly sessions achieved the highest literacy gain of 1.46 points.'}

**Supports Odin (direct justifications):**
- Higher AI engagement leads to greater financial literacy improvement (r = 0.31).
- Users who interact with AI tools more than five times per week show the highest knowledge gains (1.46 points).
- Over 65% of users report high investment confidence after using AI-driven financial tools.

**Limitations / Contradictions for Odin:**
- Sample bias toward digitally literate users, limiting generalizability to older or tech-averse populations. [unacknowledged]
- Short-term measurement of literacy and confidence; no longitudinal assessment of retention or real-world behavior.
- Self-reported metrics (confidence, usage frequency) may introduce response bias.

**Key takeaways:**
- AI tools improved financial literacy scores by 1.1 points on average.
- Higher usage frequency (5+ sessions/week) yields 1.46 point literacy gain.
- Over 65% of users reported high investment confidence post-intervention.

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


## Detection of Fraudulent Transaction Issues in the Payment Card Industry using Machine Learning: A Comprehensive Survey
**Filename:** `IA--Kalideen_summarized.md`  
**Authors:** Kalideen, M. R. (2025)  
**ID:** `d8f3a2c1-6b7a-4e9d-8f2c-1a2b3c4d5e6f`  
**Odin Topics:** 8.A, 8.B, 10.A, 10.B, 12.A, 12.B  

**TLDR:** A comprehensive survey of machine learning techniques for payment card fraud detection, covering supervised, unsupervised, deep learning, and ensemble methods, along with challenges like imbalanced data and emerging trends such as explainable AI and privacy-preserving machine learning.

**Problem & Motivation:** Traditional rule-based fraud detection systems are static, inflexible, and prone to high false positives, struggling to keep pace with evolving fraud tactics. The exponential growth of digital payments has increased fraud, causing financial losses and eroding trust. A systematic review of ML-based solutions is needed to identify effective, adaptable, and scalable approaches.

**Approach (summary):**
- Conducted a systematic literature search in IEEE Xplore, Scopus, and PubMed using keywords related to credit card fraud detection and machine learning.
- Included English studies published between 2010 and 2024; initial 500 studies reduced to 49 after duplicate removal, abstract screening, and full-text assessment.
- Classified ML techniques into supervised learning (logistic regression, SVM, decision trees, random forests, neural networks), unsupervised learning (clustering, anomaly detection, PCA), and semi-supervised/hybrid methods.

**Key Findings (selected):**
- num: Less than 1% of all transactions are fraudulent, creating extreme class imbalance that biases models toward the majority class.
- num: Of 500 initial studies, 49 met inclusion criteria, most published within the last five years.
- Supervised learning achieves high accuracy when trained on sufficient labeled data but requires costly labeling and may not generalize to new fraud patterns.
- Unsupervised learning can uncover unknown fraud patterns without labels but results can be difficult to interpret and evaluate.

**Supports Odin (direct justifications):**
- Imbalanced datasets cause models to bias toward legitimate transactions, requiring sampling or cost-sensitive learning.
- Explainable AI is necessary for regulatory compliance and user trust in automated fraud detection.
- Federated learning enables training on distributed data without sharing sensitive financial information.

**Limitations / Contradictions for Odin:**
- Imbalanced datasets remain a fundamental challenge; oversampling can cause overfitting, undersampling can lose information.
- Model interpretability is limited for deep learning 'black boxes', hindering trust and regulatory acceptance.
- Scalability and real-time detection require distributed computing and model optimization not yet fully solved.

**Key takeaways:**
- Less than 1% of transactions are fraudulent, causing extreme class imbalance.
- Ensemble methods like random forests handle imbalanced data better than single classifiers.
- Explainable AI is essential for trust and compliance in financial fraud detection.

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


## Toward Transparent Optimization: A Systematic Review of Explainable AI in Decision-Making Systems
**Filename:** `IA--Danach-et_al_summarized.md`  
**Authors:** Danach, K.; Aly, W. H. F.; Tarhini, A.; Laouadi, S. (2025)  
**ID:** `10.29020/nybg.ejpam.v18i4.6707`  
**Odin Topics:** 6.A, 6.B, 7.B, 7.C, 8.A, 8.B, 10.A, 10.B, 12.A, 12.B  

**TLDR:** A systematic review synthesizes the integration of explainable AI (XAI) with optimization methods across healthcare, finance, logistics, and energy, proposing a taxonomy and highlighting trade-offs between performance and interpretability.

**Problem & Motivation:** Optimization-driven AI systems often operate as black boxes, undermining trust, regulatory compliance, and human-AI collaboration in high-stakes decisions. Despite advances in XAI, systematic integration with optimization frameworks remains fragmented and lacks unified taxonomies. This gap hinders the development of transparent, accountable intelligent systems.

**Approach (summary):**
- Conducted a systematic literature search across Scopus, Web of Science, IEEE Xplore, and ACM Digital Library for 2010-2024, retrieving 642 records and including 112 peer-reviewed studies after screening.
- Proposed a structured taxonomy categorizing XAI-optimization integration by explainability level, optimization complexity, and domain specificity.
- Analyzed integration strategies including post-hoc explanations (SHAP, LIME), interpretable models (decision trees, MILP), certificate-based verification, and data-driven frameworks like EXALT.

**Key Findings (selected):**
- num: EXALT framework reduces explanation generation time by 72% compared to post-hoc methods while maintaining 98% solution optimality.
- num: Explainable optimization approaches achieve error reduction rates of 41-68% compared to black-box optimization in healthcare logistics and derivatives pricing.
- Explainability constraints can enhance solution quality by acting as regularizers that embed domain knowledge.
- The trade-off between optimality and interpretability can be favorable, with explainable path constraints increasing solution cost by only a small margin.

**Supports Odin (direct justifications):**
- XAI methods can explain optimization-driven decisions without sacrificing near-optimal performance.
- Explainability constraints can be embedded as multi-objective optimization objectives.
- Certificate-based verification provides formal guarantees for solution properties like feasibility and stability.

**Limitations / Contradictions for Odin:**
- Scalability to large-scale industrial problems remains a significant challenge [unacknowledged].
- Standardization of explainability metrics and evaluation frameworks is lacking [acknowledged].
- Integration with existing enterprise systems and workflows has received limited research attention [unacknowledged].

**Key takeaways:**
- Explainable optimization reduces explanation time by 72% while preserving 98% optimality.
- XAI methods can turn black-box optimizers into transparent, auditable systems.
- The performance-interpretability trade-off is often favorable in practice.

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


## Development of Budget Management System Using Visual Basic .NET and MySQL Database: A Desktop Application for Personal Financial Tracking
**Filename:** `I--Janobe_summarized.md`  
**Authors:** Janobe, J. (2025)  
**ID:** `10.59431/jda.v4i1.660`  
**Odin Topics:** 3.A, 3.B, 4.A, 4.B, 10.A, 10.B  

**TLDR:** A desktop budget management system using Visual Basic .NET and MySQL enables offline income/expense tracking, automatic balance calculation, and local data storage for privacy.

**Problem & Motivation:** Many individuals struggle with financial discipline due to limited access to reliable, private, and offline tools. Existing cloud-based solutions raise privacy concerns and require internet connectivity, while manual methods are error-prone. There is a need for a simple, secure, desktop-based budget management system that operates offline and respects user autonomy.

**Approach (summary):**
- The system was developed following the Software Development Life Cycle (SDLC) with Visual Basic .NET 2015 and MySQL 5.7.
- It uses a two-tier client-server architecture with ADO.NET for database connectivity and the MySQL Connector/NET driver.
- The database schema (db_budget) includes a transactions table with amount, transaction_type (Received/Expense), remarks, and transaction_date fields.

**Key Findings (selected):**
- num: Performance tests showed transaction operations under 0.5 seconds and data retrieval under 1 second for up to 5,000 entries.
- The system accurately distinguishes income from expenses and calculates current balance with color-coded feedback (green for surplus, red for deficit).
- Usability testing confirmed users of varying technical backgrounds completed all tasks successfully with minimal guidance.
- The system operates fully offline, storing all data locally without internet dependency or subscription costs.

**Supports Odin (direct justifications):**
- Offline financial tracking systems can operate reliably without internet connectivity (Janobe, 2025).
- Local data storage eliminates risks of cloud-based data breaches (Janobe, 2025).
- Simple income/expense categorization with remarks suffices for basic personal finance tracking (Janobe, 2025).

**Limitations / Contradictions for Odin:**
- Manual installation process requires technical knowledge to configure MySQL via XAMPP [unacknowledged].
- Single-user design prevents collaborative household budgeting (acknowledged).
- No automated backup or export features (acknowledged).

**Key takeaways:**
- Offline operation with local storage preserves financial data privacy.
- System processes 5,000 transactions with under 1 second retrieval time.
- Simple income/expense tracking suffices for many users seeking control.

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


## A Review of Machine Learning and Deep Learning Approaches for Fraud Detection Across Financial and Supply Chain Domains
**Filename:** `IA--Martinez_summarized.md`  
**Authors:** Martínez, Ó.; Sánchez, P.; Alcaraz, E. (2025)  
**ID:** `10.21203/rs.3.rs-7893661/v1`  
**Odin Topics:** 8.A, 8.B, 12.A, 12.B, 10.A, 10.B  

**TLDR:** A systematic review of machine learning and deep learning approaches for fraud detection across financial and supply chain domains, evaluating ensemble, deep, and semi-supervised methods on benchmark datasets.

**Problem & Motivation:** Digital fraud schemes are increasingly sophisticated, and traditional rule-based systems are inadequate. While machine learning offers promise, fragmented research across financial and supply chain domains lacks comprehensive comparison. This review synthesizes methodologies to guide algorithm selection and address challenges like class imbalance and concept drift.

**Approach (summary):**
- Systematic literature review following PRISMA guidelines with searches across IEEE Xplore, ACM, ScienceDirect, Springer, arXiv, and Google Scholar covering 2015-2025.
- Initial search yielded 1,847 publications; after deduplication and screening, 97 high-quality studies were selected for analysis.
- Methodologies categorized into traditional ML (logistic regression, random forest, SVM), deep learning (CNN, LSTM, autoencoders), ensemble (XGBoost, LightGBM, stacking), semi-supervised, and emerging technologies.

**Key Findings (selected):**
- num: Ensemble methods achieve AUC-ROC 0.90-0.93 on IEEE-CIS dataset, with stacking improving over single models by 2-5%.
- num: Random forest achieves 99.95% accuracy on European credit card dataset, and XGBoost/LightGBM show comparable top-tier performance.
- num: Autoencoders trained only on legitimate transactions achieve 94.2% accuracy for unsupervised fraud detection.
- num: A two-phase semi-supervised framework (Isolation Forest + self-training SVM) achieves F1-score 0.817 with false positive rate below 3.0% using only 1.2% labeled data.

**Supports Odin (direct justifications):**
- Ensemble methods, particularly XGBoost and LightGBM, achieve state-of-the-art performance on imbalanced fraud data.
- Two-phase semi-supervised learning (Isolation Forest pre-filtering plus self-training SVM) achieves high recall with limited labeled data.
- Autoencoders trained on legitimate transactions only can detect fraud without labeled examples.

**Limitations / Contradictions for Odin:**
- Extreme class imbalance remains a fundamental challenge despite sampling and cost-sensitive techniques.
- Concept drift detection and adaptation are incomplete, with label delay causing lag in response.
- Interpretability-accuracy trade-off forces compromise between regulatory compliance and performance.

**Key takeaways:**
- Ensemble methods like XGBoost and LightGBM consistently outperform other approaches for fraud detection.
- Borderline-SMOTE improves fraud recall by 10-15% compared to standard oversampling.
- Two-phase semi-supervised learning achieves 94% fraud capture with only 1.2% labeled data.

---


## An Introduction to Machine Learning Methods for Fraud Detection
**Filename:** `IA--Compagnino-et_al_summarized.md`  
**Authors:** Compagnino, A. A.; Maruccia, Y.; Cavuoti, S.; Riccio, G.; Tutone, A.; Crupi, R.; Pagliaro, A. (2025)  
**ID:** `10.3390/app15211787`  
**Odin Topics:** 8.A, 8.B, 12.A, 12.B, 10.A, 10.B  

**TLDR:** Reviews machine learning for financial fraud detection, covering supervised, unsupervised, and deep learning approaches, datasets, performance metrics, and case studies highlighting class imbalance and recall challenges.

**Problem & Motivation:** Financial fraud causes severe economic and social damage, with 56% of companies experiencing fraud. Traditional detection methods are increasingly inadequate against evolving fraudulent activities. A systematic analysis of ML techniques bridging academic research and operational reality is missing.

**Approach (summary):**
- Systematic literature search across Scopus, IEEE Xplore, ACM Digital Library, and Web of Science for articles published 2014-2023.
- Classification of fraud types into external (credit card, loan, insurance) and internal (financial statement, money laundering, tax, asset misappropriation).
- Review of supervised methods (Random Forest, XGBoost, SVM, etc.), unsupervised methods (Isolation Forest, Autoencoders, K-Means), and deep learning (LSTM, CNN, RNN, GAN).

**Key Findings (selected):**
- num: Random Forest achieved AUPRC of 0.619 on banking test set (prevalence 2.37%) but fraud recall was only 0.34.
- num: XGBoost on ULB2013 dataset achieved AUPRC of 0.867, outperforming Logistic Regression (0.724) and KNN (0.585).
- num: Class_weight='balanced' and 'balanced_subsample' did not improve recall (stuck at 0.36) compared to default on bank transfer dataset.
- num: Recall@0.5% for Random Forest was 0.202, capturing about 24 of 119 frauds when screening top 0.5% of transactions.

**Supports Odin (direct justifications):**
- Fraudulent transactions typically constitute less than 1% of all transactions, making class imbalance a fundamental challenge.
- Accuracy is misleading for imbalanced data; AUPRC is the preferred metric for comparing anomaly detectors.
- Even with class_weight adjustments, Random Forest recall on fraud class was only 0.34 in a real banking dataset.

**Limitations / Contradictions for Odin:**
- The review does not propose a novel algorithm or system, only synthesizes existing literature.
- Case studies use tree-based ensembles only; deep learning and hybrid methods were not empirically tested. [unacknowledged]
- The low recall achieved (0.34-0.36) suggests standard supervised models are insufficient, but the paper does not implement or evaluate the recommended hybrid solutions.

**Key takeaways:**
- Random Forest achieved AUPRC 0.619 but fraud recall only 0.34 on real banking data.
- Class_weight adjustments did not improve recall beyond 0.36 in imbalanced fraud detection.
- AUPRC is preferred over ROC for evaluating models on imbalanced datasets.

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


## Intelligent UI’s: Revolutionizing Financial Transaction Systems Through AI and Event-Driven Architecture
**Filename:** `I--Musunuri_summarized.md`  
**Authors:** Musunuri, H. (2025)  
**ID:** `3a0b1c2d-4e5f-6a7b-8c9d-0e1f2a3b4c5d`  
**Odin Topics:** 4.A, 4.B, 6.A, 8.A, 8.B, 10.A, 10.B, 11.A, 11.B, 12.A  

**TLDR:** Intelligent UI architectures using AI and event-driven patterns improve financial transaction systems by enhancing fraud detection, reducing processing times, and personalizing user experiences without compromising security.

**Problem & Motivation:** Traditional financial interfaces struggle with linear processing workflows, reactive security measures, and one-size-fits-all designs. These limitations create trade-offs between security and usability, leading to transaction abandonment and fraud vulnerabilities. Modern intelligent UIs aim to transcend these trade-offs through adaptive and event-driven approaches.

**Approach (summary):**
- Paper reviews existing literature and industry implementations of AI-driven and event-driven financial interfaces.
- Analyzes case studies of financial institutions implementing behavioral biometrics, predictive adaptation, and zero-trust models.
- Evaluates performance metrics including fraud detection accuracy, transaction processing times, and completion rates from 127 institutions.

**Key Findings (selected):**
- num: Institutions implementing behavioral biometric monitoring achieved 43.2% improvement in fraud detection accuracy and 37.8% reduction in false positives.
- num: Event-driven architectures reduced transaction processing times by 53.7% for standard transactions and 61.2% for complex transactions.
- num: Context-aware component selection improved task completion rates by 41.6% and reduced time-on-task by 36.2%.
- num: Phased implementation approaches showed 3.7 times higher success rates and 42% lower budget overruns than big-bang replacements.

**Supports Odin (direct justifications):**
- Event-driven architectures reduce transaction processing latency by 53-61% compared to request-response models.
- Behavioral biometrics achieve 97.6% user identification accuracy after 14 seconds of interaction.
- Context-aware component selection improves task completion rates by 41.6%.

**Limitations / Contradictions for Odin:**
- Primarily synthesizes existing literature rather than presenting novel empirical data [unacknowledged].
- Does not address implementation challenges of AI bias in financial interfaces [unacknowledged].
- Lacks specific guidance for small financial institutions with limited resources [unacknowledged].

**Key takeaways:**
- Intelligent UIs improve fraud detection by 43.2% while reducing false positives by 37.8%.
- Event-driven architectures cut transaction processing time by over 50%.
- Phased migrations are 3.7 times more successful than big-bang replacements.

---


## Data-Driven Decision Making in Scholarship Programs: Leveraging Decision Trees and Clustering Algorithms
**Filename:** `LA--Espiritu-et_al_summarized.md`  
**Authors:** Espiritu, F. V.; Natividad, M. C. B.; Velasco, R. A. (2024)  
**ID:** `123e4567-e89b-12d3-a456-426614174000`  
**Odin Topics:** 5.C, 10.A, 10.B, 12.B  

**TLDR:** Integrates decision trees and clustering algorithms with an online system to improve scholarship application processing, achieving 31% higher success rates.

**Problem & Motivation:** Scholarship programs face inefficiencies from manual application review, especially with a 541.1% surge in applications. The BRO-Ed program lacks a systematic data-driven approach to evaluate applicants. This leads to missed opportunities and suboptimal resource allocation.

**Approach (summary):**
- Used historical scholarship data from Isabela province (58,892 initial entries) as the dataset.
- Preprocessed data by handling missing values, outliers, duplicates, and normalization.
- Implemented C4.5 decision tree algorithm for identifying key success factors and K-means clustering for grouping similar applications.

**Key Findings (selected):**
- num: Online registration system achieved 31% higher success rate than traditional methods.
- num: Decision tree predictive accuracy was 80% for successful applications and 70% for failures.
- num: Data completeness reached 95% and accuracy 95% after preprocessing.
- num: Removed 3,100 duplicate entries from original 58,892 records.

**Supports Odin (direct justifications):**
- Online registration systems can achieve 31% higher success rates than traditional methods.
- Decision trees achieve 80% predictive accuracy for scholarship success classification.
- Data anonymization and RA 10173 compliance are essential for user trust in applicant systems.

**Limitations / Contradictions for Odin:**
- Sample limited to Isabela province's BRO-Ed scholarship program.
- No longitudinal validation of applicant success after scholarship award.
- Potential bias in historical data not fully addressed. [unacknowledged]

**Key takeaways:**
- 31% higher success rate from online system over traditional methods.
- Decision trees achieved 80% predictive accuracy for scholarship success.
- Data privacy included anonymization and RA 10173 compliance.

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


## A User-Centric Exploration of Axiomatic Explainable AI in Participatory Budgeting.
**Filename:** `IA--Hashemi-et_al_summarized.md`  
**Authors:** Hashemi, M.; Darejeh, A.; Cruz, F. (2024)  
**ID:** `10.1145/3675094.3677599`  
**Odin Topics:** 7.B, 7.C, 10.B, 12.A, 12.B  

**TLDR:** Using axioms as linear constraints, an integer linear programming approach generates explanations for participatory budgeting outcomes, improving user understanding and perceived fairness but not consistently affecting trust.

**Problem & Motivation:** Participatory budgeting mechanisms lack transparency despite satisfying desirable axioms. Existing voting rules are complex, making outcomes difficult for users to understand. There is a need for explainable AI approaches that justify budget allocations using axiomatic properties.

**Approach (summary):**
- Proposes an integer linear programming (ILP) formulation where axioms (feasibility, exhaustiveness, utilitarian welfare) serve as constraints.
- Uses Gurobi optimizer to enumerate all allocations satisfying the constraints, then explains why a specific outcome was chosen or rejected.
- Evaluates the approach with a pilot user study of 26 participants via Mechanical Turk.

**Key Findings (selected):**
- num: 72.4% of participants found explanations extremely or very helpful for understanding the system's decision.
- num: 63.3% of participants preferred general explanations over counterfactual explanations.
- num: 30% reported a positive impact on perceived fairness of the system after explanations; none reported a negative impact.
- num: Trust increased in 27% of cases, decreased in 20%, and remained unchanged in 50% after receiving explanations.

**Supports Odin (direct justifications):**
- Providing axiomatic explanations improves user understanding of budget allocation decisions.
- General explanations are preferred over counterfactual explanations in participatory budgeting.
- Explanations based on axioms positively impact perceived fairness of the system.

**Limitations / Contradictions for Odin:**
- Small sample size (N=26) limits generalizability of user findings.
- Study only used two simple cases with three projects and greedy rule; complex scenarios may yield different results.
- Could not draw definitive conclusions about trust due to mixed and inconclusive results [unacknowledged].

**Key takeaways:**
- 72.4% of users found axiomatic explanations helpful for understanding budget decisions.
- Explanations improved perceived fairness in participatory budgeting.
- User trust was inconsistently affected by explanations, with 20% reporting decreased trust.

---


## Examining Mobile-First Database Solutions for East African Markets in Detail
**Filename:** `I--Arinze_summarized.md`  
**Authors:** Arinze, E. D. (2024)  
**ID:** `5a6b7c8d-9e0f-1a2b-3c4d-5e6f7a8b9c0d`  
**Odin Topics:** 9.A, 9.B, 10.A, 10.B, 11.A, 11.B  

**TLDR:** Mobile-first database solutions enhance accessibility and scalability in East African markets but face challenges in connectivity, data privacy, and regulatory compliance.

**Problem & Motivation:** Traditional database systems are not optimized for mobile-centric environments like East Africa, where high mobile penetration and limited desktop infrastructure create a need for accessible, scalable solutions. Existing approaches often fail to address bandwidth constraints, offline usage, and local data protection regulations. Without mobile-first design, organizations risk low user adoption and poor service delivery in remote or underserved areas.

**Approach (summary):**
- Literature review of published statistics (2004–2014) from multiple reliable databases on mobile technology adoption in Kenya, Tanzania, Uganda, Rwanda, and Ethiopia.
- Analysis of technical foundations including cloud computing, offline storage with caching and conflict resolution, and real-time synchronization using WebSocket, MQTT, or HTTP long polling.
- Examination of data security measures: TLS encryption, end-to-end encryption (E2EE), at-rest encryption, and authentication (biometric, MFA, OAuth) with RBAC.

**Key Findings (selected):**
- Mobile-first database solutions increase user engagement, adoption, and retention by providing seamless offline and real-time synchronization capabilities.
- Data security requires transport encryption, at-rest encryption, strong authentication, and role-based access control to build user trust.
- Bandwidth limitations and intermittent connectivity remain major barriers, mitigated by compression, CDNs, and local caching.
- Regulatory compliance (e.g., GDPR, Data Protection Act) and legal ambiguity pose challenges that demand privacy-by-design and cross-border cooperation.

**Supports Odin (direct justifications):**
- Mobile-first database solutions increase user acceptance and retention by providing a seamless and intuitive mobile experience.
- Offline capabilities with local storage and conflict resolution ensure data consistency and availability in low-connectivity environments.
- Encryption (TLS, E2EE) and role-based access control are necessary to prevent unauthorized access and build user trust.

**Limitations / Contradictions for Odin:**
- Relies on secondary data from 2004–2014, potentially outdated for current mobile technology trends. [unacknowledged]
- Does not provide quantitative metrics for engagement or retention improvements, making it difficult to benchmark against other designs. [unacknowledged]
- Connectivity and bandwidth challenges are identified, but no specific solution for very low-bandwidth (2G) environments is tested.

**Key takeaways:**
- Mobile-first design with offline sync boosts user engagement in low-connectivity settings.
- End-to-end encryption and role-based access control are essential for user trust.
- Bandwidth constraints demand compression, caching, and CDNs for acceptable performance.

---


## Recommendation system for financial decision-making using Artificial intelligence
**Filename:** `IA--Shuryhin-&-Zinovatna_summarized.md`  
**Authors:** Shuryhin, K. A.; Zinovatna, S. L. (2024)  
**ID:** `10.15276/aait.07.2024.24`  
**Odin Topics:** 2.C, 6.A, 6.B, 7.B, 7.C, 8.A, 8.B, 10.A, 10.B  

**TLDR:** Combines Isolation Forest for anomaly detection, ARIMA and LSTM for budget forecasting, and large language models to generate personalized financial recommendations while addressing ethical concerns like privacy and user autonomy.

**Problem & Motivation:** Cognitive biases lead to irrational financial decisions, and AI-enhanced marketing can manipulate consumer behavior. Existing recommendation systems in finance often lack personalization, fail to account for user autonomy, or ignore ethical considerations. There is a need for an intelligent system that provides unbiased, personalized financial advice without manipulation.

**Approach (summary):**
- Input data includes user transaction history, spending anomalies, budget forecasts, and user parameters like risk tolerance and financial goals.
- Isolation Forest isolates anomalies by building binary trees and calculating path lengths; anomaly score near 1 indicates anomalous expense.
- ARIMA(p,d,q) models short-term dependencies with autoregressive and moving average components after differencing for stationarity.

**Key Findings (selected):**
- Isolation Forest effectively identifies atypical financial actions by isolating deviations from normal spending patterns.
- Combining ARIMA (short-term) and LSTM (long-term) improves budget forecast stability and accuracy.
- LLM-generated recommendations adapt to different income levels and user-specific risk levels, goals, and preferences.
- The system promotes responsible financial behavior without imposing decisions, enhancing user awareness and autonomy.

**Supports Odin (direct justifications):**
- Isolation Forest can identify atypical financial transactions by isolating deviations from normal behavior.
- Weighted combination of ARIMA and LSTM improves budget forecast accuracy over either model alone.
- LLMs can generate personalized financial recommendations that adapt to user income level and risk tolerance.

**Limitations / Contradictions for Odin:**
- No quantitative validation of forecasting or anomaly detection accuracy. [unacknowledged]
- The system's LLM component is described only conceptually; no ablation study or comparison with rule-based baselines. [unacknowledged]
- Ethical claims are not operationalized or measured (e.g., how to verify user autonomy). [unacknowledged]

**Key takeaways:**
- Anomaly detection uses Isolation Forest with path length scoring.
- Forecasts combine ARIMA for short-term and LSTM for long-term trends.
- Large language model generates personalized financial advice from transaction and forecast data.

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


## Localized Expansion Strategy Framework for Fintech Products Scaling from African to Western User Markets
**Filename:** `I--Uzoka-et_al_summarized.md`  
**Authors:** Uzoka, A. C.; Olinmah, F. I.; Okolo, C. H.; Omotayo, K. V.; Adanigbo, O. S. (2023)  
**ID:** `d41d8cd9-8f00-320b-a8b0-4f7b0b6d8f5a`  
**Odin Topics:** 9.A, 9.B, 10.A, 10.B  

**TLDR:** A framework guides African fintechs in scaling to Western markets by balancing core innovations with localization of regulation, UX, and trust.

**Problem & Motivation:** African fintechs have developed innovative mobile-first and alternative credit scoring products, but lack structured guidance for expanding into Western markets with different regulatory, cultural, and user expectations. Existing frameworks focus on Western startups entering emerging markets, leaving a gap for reverse expansion. This paper provides a framework to address that gap.

**Approach (summary):**
- Literature review of fintech globalization, localization theory, and gaps in existing frameworks.
- {'Four foundational principles': 'contextual product adaptation, regulatory integration, trust and brand repositioning, user-centric innovation.'}
- {'Three-phase strategy': 'internal readiness and product audit, localization and regulatory embedding, market entry and iterative scaling.'}

**Key Findings (selected):**
- {'num': 'Framework offers structured phases without quantitative performance metrics.'}
- African fintech core innovations include mobile-first design and alternative credit scoring based on mobile usage data.
- Western markets demand GDPR, PSD2, stringent KYC/AML, requiring embedded compliance.
- Trust rebuilding requires transparent communication, local partnerships, and third-party certifications.

**Supports Odin (direct justifications):**
- Mobile-first design is a key innovation from African fintechs that can be transferred to other markets.
- Regulatory compliance must be embedded early in product architecture, not added later.
- User trust in Western markets depends on transparent privacy policies and third-party certifications.

**Limitations / Contradictions for Odin:**
- No empirical validation of the framework. [unacknowledged]
- Limited discussion of cost implications for fintechs.
- Assumes Western markets are homogeneous, ignoring intra-regional differences. [unacknowledged]

**Key takeaways:**
- Mobile-first design from African fintechs offers lessons for PFMS in low-resource settings.
- Regulatory compliance must be embedded from the start, not retrofitted.
- User trust in finance apps requires transparent privacy policies and certifications.

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


## 📌 Note for the Agent

The summaries above contain **essential extracts** – enough to understand the paper's relevance to Odin, including supporting evidence and limitations.
If you need additional details not shown here (e.g., **critical citations, definitions, equations, full methodology, or the complete mapping rationale**),
**ask the user to send the original summary file (`<filename>_summarized.md`) or the converted MarkItDown file(`<filename>_marked.md`)** for the specific paper(s) of interest.
Do not invent missing information. Acknowledge gaps when they exist.