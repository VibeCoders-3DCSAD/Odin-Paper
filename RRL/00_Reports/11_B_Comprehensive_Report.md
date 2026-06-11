# Comprehensive Report for Subtopic: `11.B`

**Total files:** 8

This report includes problem/motivation, approach, key findings, support for Odin, and limitations/contradictions.

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

**Limitations / Contradictions for Odin:**
- "Synthetic dataset may not generalize to real-world user behavior. [unacknowledged]"
- "No user study or empirical validation of trust or engagement metrics. [unacknowledged]"
- "SHAP computational cost and caching overhead acknowledged but not fully solved."

**Key takeaways:**
- "Explainability is critical for user trust in automated finance."
- "Context-aware triggers (time, location, habits) increase engagement."
- "SHAP provides fair, locally interpretable explanations for nudges."

---


## Systematic review of deep and machine learning for financial modeling
**Filename:** `IA--Zlobin-&-Bazylevych_summarized.md`  
**Authors:** Zlobin, M.; Bazylevych, V. (2025)  
**ID:** `10.25140/2411-5363-2025-1(39)-184-195`  
**Odin Topics:** 6.A, 6.B, 8.A, 8.B, 11.A, 11.B, 12.A, 12.B  

**TLDR:** Systematic review of 41 papers on ML/DL for financial classification and regression tasks including credit scoring, fraud detection, stock prediction, and anomaly detection.

**Problem & Motivation:** Financial institutions face datasets that traditional analytical methods cannot process effectively. ML and DL offer improved predictive accuracy but challenges like model interpretability, data quality, and concept drift remain. A systematic synthesis of state-of-the-art methods is needed to identify gaps and guide future research.

**Approach (summary):**
- Review of 41 peer-reviewed papers on ML/DL applications in finance published up to 2025.
- Focus on classification tasks (credit scoring, fraud detection, customer segmentation) and regression tasks (stock price prediction, volatility forecasting, option pricing).
- Comparative analysis of model performance using metrics such as AUC, RMSE, accuracy, precision, recall, and F1-score.

**Key Findings (selected):**
- "num: Random forest with ensemble feature selection achieved 99.6% accuracy and 100% precision in credit card fraud detection."
- "num: XGBoost consistently outperformed deep neural networks across 10 credit scoring datasets, achieving highest AUC and efficiency."
- "num: CNN reduced fraud detection cost of failure by 30% and achieved 87.64% AUC on European dataset."
- "num: GCN achieved 94.5% fraud detection accuracy, outperforming CNN (93%) by improving recall by 10% via graph-based user relationship analysis."

**Limitations / Contradictions for Odin:**
- "Review primarily cites papers up to 2024; rapid ML/DL advances may render some comparisons outdated. [unacknowledged]"
- "Performance metrics are aggregated across heterogeneous datasets, making direct apples-to-apples comparisons difficult. [unacknowledged]"
- "The review does not address computational resource constraints of mobile-first deployment, which is critical for Odin. [unacknowledged]"

**Key takeaways:**
- "XGBoost outperforms deep learning for credit scoring across 10 datasets."
- "Random forest achieves 99.6% fraud detection accuracy with feature selection."
- "AI personalization lifts user engagement by 27% and retention by 15%."

---


## "DIGITIZATION IN RETAIL BANKING: A REVIEW OF CUSTOMER ENGAGEMENT AND FINANCIAL PRODUCT ADOPTION IN SOUTH ASIA"
**Filename:** `I--Koswar-et_al_summarized.md`  
**Authors:** "Kowsar, M. M.; Islam, S.; Mohiuddin, M.; Siddiqui, N. A." (2025)  
**ID:** `10.63125/cv50rf30`  
**Odin Topics:** 4.A, 4.B, 8.A, 9.A, 9.B, 10.A, 10.B, 11.A, 11.B, 13.A, 13.B  

**TLDR:** "A systematic review of 84 studies finds that mobile infrastructure, AI-driven personalization, and behavioral nudges enhance customer engagement and financial product adoption in South Asian retail banking, though digital divides persist."

**Problem & Motivation:** "Digitization transforms retail banking but region-specific evidence for South Asia is scarce. Understanding how mobile banking and fintech affect customer engagement and product adoption is critical for inclusive financial growth. This review synthesizes fragmented literature to identify drivers and barriers."

**Approach (summary):**
- "Followed PRISMA 2020 systematic review methodology."
- "Searched Scopus, Web of Science, JSTOR, EBSCOhost, ProQuest, Google Scholar, and institutional repositories."
- "Used Boolean keyword combinations on digital banking, engagement, product adoption, and South Asia."

**Key Findings (selected):**
- "num: Mobile phone penetration exceeds 85% and mobile broadband covers over 95% of the population in India and Sri Lanka."
- "num: Digitally engaged customers in India were 2.3 times more likely to open secondary financial products like insurance or investment accounts."
- "num: 34 of 84 reviewed studies directly examined product adoption, collectively cited over 4,200 times."
- "num: 29 articles on infrastructure expansion were cited over 3,400 times, underscoring their foundational impact."

**Limitations / Contradictions for Odin:**
- "Relies on secondary data from published studies; no primary data collection. [unacknowledged]"
- "Geographic scope limited to South Asia; findings may not generalize to Philippines. [unacknowledged]"
- "Does not address algorithmic cold-start or profile dynamics for new users."

**Key takeaways:**
- "85% mobile phone penetration enables digital banking at scale."
- "2.3x higher product adoption for digitally engaged customers."
- "AI nudges and personalization drive user retention and loyalty."

---


## Optimizing Business Decision-Making Through AI-Enhanced Business Intelligence Systems: A Systematic Review of Data-Driven Insights in Financial and Strategic Planning
**Filename:** `IA--Siddiqui_summarized.md`  
**Authors:** Siddiqui, N. A. (2025)  
**ID:** `10.71292/sdmi.v2i01.21`  
**Odin Topics:** 6.A, 6.B, 8.A, 8.B, 10.A, 10.B, 11.A, 11.B, 12.A, 12.B  

**TLDR:** AI-enhanced Business Intelligence systems improve financial forecasting accuracy by 32-45%, reduce fraudulent transactions by 47%, increase customer engagement by 38%, and optimize supply chain efficiency by 23%.

**Problem & Motivation:** Traditional BI systems struggle with real-time processing and unstructured data, limiting predictive capabilities. AI integration offers potential for improved decision-making but lacks systematic synthesis of its impact on financial and strategic planning.

**Approach (summary):**
- This systematic review follows PRISMA guidelines for transparent and rigorous literature analysis.
- Searched Scopus, Web of Science, IEEE Xplore, ScienceDirect, and Google Scholar for 2012-2024.
- Initial pool of 2,450 articles reduced to 98 high-quality peer-reviewed studies after screening.

**Key Findings (selected):**
- "num: 32-45% improvement in financial forecasting accuracy with AI-powered BI"
- "num: 47% decrease in fraudulent transactions and 60% reduction in false positives"
- "num: 38% increase in customer engagement and 22% improvement in conversion rates"
- "num: 23% increase in supply chain operational efficiency and 17% reduction in logistics costs"

**Limitations / Contradictions for Odin:**
- "Data governance complexities and integration issues hinder widespread AI-BI adoption."
- "Algorithmic transparency remains a challenge; many AI models operate as black boxes."
- "Bias in AI models due to skewed training data can reinforce discriminatory outcomes."

**Key takeaways:**
- "AI-enhanced BI improves forecasting accuracy by 32-45%."
- "Fraud detection reduces transactions by 47% with 60% fewer false positives."
- "Customer engagement increases by 38% using AI-driven segmentation."

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


## The Role of Digital Banking Features in Bank Selection: An Analysis of Customer Preferences for Online and Mobile Banking
**Filename:** `I--Faisal-et_al_summarized.md`  
**Authors:** Faisal, N.; Nahar, J.; Waliullah, M.; Borna, R. S. (2024)  
**ID:** `c3e5d6f7-8a9b-4c2d-9e1f-0a1b2c3d4e5f`  
**Odin Topics:** 9.A, 9.B, 10.A, 10.B, 11.A, 11.B  

**TLDR:** A systematic review of 112 articles identifies convenience, security, personalization, competitive innovation, and pandemic resilience as key drivers of digital banking adoption and customer satisfaction.

**Problem & Motivation:** Prior research on digital banking focuses on general adoption drivers but lacks deeper insights into evolving customer expectations across demographics and cultures. Understanding how specific features like usability, security, and personalization influence bank selection is critical for financial institutions to remain competitive. This gap is addressed by synthesizing existing literature to provide actionable guidance for digital banking design.

**Approach (summary):**
- Systematic literature review following PRISMA guidelines.
- Searched Scopus, Web of Science, ProQuest, and Google Scholar using keyword combinations like "digital banking" AND "customer preferences".
- Initial identification of 3,284 articles, screened to 112 peer-reviewed studies published between 2012 and 2023.

**Key Findings (selected):**
- "num: 47 out of 112 articles emphasize convenience (ease of use, 24/7 availability, fast transactions) as primary adoption driver."
- "num: 42 articles highlight security and privacy (encryption, MFA, fraud detection) as critical for customer trust."
- "num: 36 articles identify personalization (AI-driven recommendations, tailored interfaces) as transformative for satisfaction and loyalty."
- "num: 29 articles show competitive pressure drives adoption of blockchain, AI, and biometrics to differentiate offerings."

**Limitations / Contradictions for Odin:**
- "Limited focus on elderly users and rural populations with low digital literacy [acknowledged]."
- "Lack of empirical evidence linking emerging technologies (AI, blockchain) to long-term customer loyalty and profitability [acknowledged]."
- "Underexplored ethical implications of data-driven personalization and privacy trade-offs [acknowledged]."

**Key takeaways:**
- "47 studies confirm convenience as the top driver of digital banking adoption."
- "Security features like MFA and encryption are essential for customer trust."
- "Personalization via AI increases satisfaction but raises privacy concerns."

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


## Note for the Agent

The summaries above contain **essential extracts** – enough to understand each paper's relevance to Odin, including supporting evidence and limitations.
If you need additional details not shown here (e.g., **critical citations, definitions, equations, full methodology, or the complete mapping rationale**),
**ask the user to send the original summary file (`<filename>_summarized.md`) or the converted MarkItDown file(`<filename>_marked.md`)** for the specific paper(s) of interest.
Do not invent missing information. Acknowledge gaps when they exist.