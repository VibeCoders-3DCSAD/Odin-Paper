# Comprehensive Report for Subtopic: `9.B`

**Total files:** 11

This report includes problem/motivation, approach, key findings, support for Odin, and limitations/contradictions.

---


## "Proteus: Shapeshifting Desktop Visualizations for Mobile via Multi-level Intelligent Adaptation"
**Filename:** `I--Liu-et_al_summarized.md`  
**Authors:** "Liu, C.; Cheng, S.; Liang, F.; Jiang, Z.; Huang, L.; Athapaththu, K.; Wang, Y." (2026)  
**ID:** `d2b5c3f1-6a7e-4b8c-9d0f-1e2a3b4c5d6e`  
**Odin Topics:** 9.A, 9.B, 12.A, 12.B  

**TLDR:** "Proteus is an LLM-driven multi-agent framework that transforms desktop visualizations into mobile-optimized versions using a novel multi-level design space, outperforming a strong baseline in user studies."

**Problem & Motivation:** "Desktop visualizations are ill-suited for mobile screens due to different viewport sizes and interaction paradigms. Direct scaling causes illegible text, information loss, and interaction failures. Existing responsive visualization techniques treat adaptation as a flat layout puzzle lacking semantic understanding and hierarchical constraint propagation."

**Approach (summary):**
- "The authors propose a multi-level design space with three layers: Global Topology, Reference Frame, and Visual Elements."
- "They develop Proteus, a five-agent LLM system (Semantic Parser, Data Extractor, Design Planner, Frontend Engineer, Visual Critic) that iteratively adapts visualizations."
- "The system accepts HTML/SVG source code and renders mobile-optimized components using TypeScript and Recharts."

**Key Findings (selected):**
- "num: Proteus achieved 91.8% render success rate on 67 visualizations versus 87.8% for the baseline."
- "num: Wilcoxon signed-rank tests showed significant improvements for data fidelity and readability (p < 0.05) and for interaction reasonableness and aesthetics (p < 0.001)."
- "The multi-level design space enables hierarchical constraint propagation from global topology down to individual visual marks."
- "The visual critic agent autonomously evaluates and guides iterative refinement, essential for zero-intervention robustness."

**Limitations / Contradictions for Odin:**
- "High latency for complex SVG/HTML inputs due to large token counts."
- "Preserving subtle aesthetic qualities of bespoke visualizations remains difficult."
- "No task-oriented evaluation of analytic equivalence between desktop and mobile versions. [unacknowledged]"

**Key takeaways:**
- "Proteus achieves 91.8% render success on 67 diverse visualizations."
- "Multi-level design space outperforms flat geometry-centric heuristics."
- "LLM agents with a critic loop enable zero-intervention mobile adaptation."

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
- num: Users who followed AI recommendations increased average monthly savings by 12–18%.
- num: 45% of users reduced discretionary spending on non-essential items.
- num: Overspending prediction engine achieved approximately 85% precision.
- num: API response times under 200 ms provided a responsive user experience.

**Limitations / Contradictions for Odin:**
- "Manual transaction entry creates user adoption friction."
- "Lacks direct banking integration, planned for future using open banking APIs."
- "Initial recommendation engine performance required real-world data to improve [unacknowledged]."

**Key takeaways:**
- "AI recommendations increased savings by 12-18% for active users."
- "Multilingual support boosted usability for 87% of non-English speakers."
- "Interactive dashboards drive more frequent financial engagement."

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


## Development and Evaluation of My Money Manager: An Intelligent Mobile App for Personalized Financial Insight
**Filename:** `I--Parameswaran-&-Saad_summarized.md`  
**Authors:** Parameswaran, S.; Saad, S. Z. (2025)  
**ID:** `10.32890/jdsd2025.3.2.9`  
**Odin Topics:** 3.A, 3.B, 8.A, 9.A, 9.B, 12.A, 13.A  

**TLDR:** My Money Manager mobile app uses algorithmic expense categorization and 90-day spending analysis to provide personalized savings recommendations and anomaly detection, with a usability study showing high effectiveness in tracking and habit improvement.

**Problem & Motivation:** Existing personal finance apps lack intelligent analysis and personalized guidance, often offering generic one-size-fits-all advice that fails to account for individual spending patterns. Most apps do not differentiate fixed versus variable expenses or detect abnormal spending behaviors, leading to irrelevant recommendations.

**Approach (summary):**
- Iterative and incremental development methodology with agile principles and user-centered design.
- Android app following Model-View-Controller pattern and Material Design guidelines.
- Key calculations: monthly income, expenses, savings, income/expense ratio, budget status, category expense, and category percentage.

**Key Findings (selected):**
- "num: 82.8% of users confirmed income and expense tracking was efficient and reliable."
- "num: 74.3% reported the app encouraged them to manage finances more effectively."
- "num: 71.4% agreed that financial insights helped guide their financial decision-making."
- "num: 77.1% rated navigation, adding entries, and setting budgets as very easy (strongly agree)."

**Limitations / Contradictions for Odin:**
- "Small sample size (n=35) limits statistical power and generalizability."
- "No longitudinal follow-up to assess sustained behavior change or retention."
- "Financial insights comprehension was problematic for 14.3% of users, but no redesign was tested. [unacknowledged]"

**Key takeaways:**
- "82.8% of users found income and expense tracking reliable."
- "74.3% reported improved financial management habits."
- "Only 37.1% strongly agreed financial insights were easy to understand."

---


## Optimizing Banking Application Interfaces: A User-Centric Perspective on Consent Management in Digital Banking Environments
**Filename:** `I--Pakarinen_summarized.md`  
**Authors:** Pakarinen, O. (2025)  
**ID:** `a3b7c9d1-4e5f-4a6b-8c7d-9e0f1a2b3c4d`  
**Odin Topics:** 9.A, 9.B, 10.A, 10.B  

**TLDR:** A two-level consent management prototype with category-based overview and granular controls improved user understanding and confidence in digital banking interfaces.

**Problem & Motivation:** Existing consent screens in banking apps use lengthy legal text and complex layouts, causing users to skim and feel unsure about their decisions. There is a gap between regulatory compliance and usable consent interfaces that support informed choice. A user-centric design is needed to make consent transparent, accessible, and controllable.

**Approach (summary):**
- Mixed-methods approach including an exploratory survey (n=6), two rounds of usability testing, and semi-structured interviews.
- Prototype designed with two layers: category-based consent overview and detailed granular consent view with tooltips.
- Full-stack implementation using MEAN stack (MongoDB, Express.js, Angular, Node.js) with auditable consent records.

**Key Findings (selected):**
- Lengthy, complex consent language impairs users’ understanding and leads to disengagement.
- Concise, clear steps and explicit labels improve users’ perception of control and confidence when giving consent.
- Category-based overview with visible consent state (green/yellow badges) helps users orient faster.
- Tooltips with brief explanations reduce confusion about technical terms.

**Limitations / Contradictions for Odin:**
- "Limited user group and small sample size reduce generalizability of findings."
- "Controlled environment testing, not integrated into a live banking system."
- "Prototype simplified; real-world technical integration challenges not fully addressed."

**Key takeaways:**
- Two-level consent structure (category overview + granular view) reduces cognitive load.
- Visible consent state badges improve user orientation and decision confidence.
- Progressive disclosure and tooltips outperform dense legal text blocks.

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


## Making maps & visualizations for mobile devices: A research agenda for mobile-first and responsive cartographic design
**Filename:** `I--Roth-et_al_summarized.md`  
**Authors:** Roth, R. E.; Çöltekin, A.; Delazari, L.; Denney, B.; Mendonça, A.; Ricker, B. A.; Shen, J.; Stachoň, Z.; Wu, M. (2024)  
**ID:** `10.1080/17489725.2023.2251423`  
**Odin Topics:** 9.A, 9.B  

**TLDR:** A research agenda for mobile-first and responsive cartographic design presents 20 challenges across scale, projections, symbolization, toponymy, and user interaction to adapt cartographic canon for mobile devices.

**Problem & Motivation:** Most maps are viewed on mobile devices, yet cartographic design principles were established for print maps and rarely consider mobile constraints. Mobile devices impose small screens, limited bandwidth, battery life, and touch interaction, but also enable new possibilities like location-based services and egocentric views. A comprehensive reevaluation of the cartographic design space is needed to support mobile-first and responsive maps.

**Approach (summary):**
- Conducted a two-day workshop with 70 scholars from nine countries to identify research challenges.
- Reviewed existing literature on mobile cartography constraints, enablements, and consequences.
- Organized challenges into five design dimensions: scale/generalization, projections, symbolization/visual hierarchy, toponymy/typography, and user interaction.

**Key Findings (selected):**
- Mobile generalization should consider speed or cost rather than scale alone.
- Egocentric oblique projections require renewed research on pitch, bearing, and depth cues.
- Energy-aware color schemes can reduce carbon footprint but conventional schemes fail under dimming.
- Gaze-contingent displays offer potential for adaptive labeling on mobile devices.

**Limitations / Contradictions for Odin:**
- The research agenda is conceptual and lacks empirical validation of specific design recommendations.
- Focuses on cartographic maps rather than financial data visualizations common in PFMS. [unacknowledged]
- Does not consider low-end mobile devices prevalent in developing economies. [unacknowledged]

**Key takeaways:**
- Annual global energy for Google Maps is 820.9 million kWh.
- Mobile-first design prioritizes most constrained user experience first.
- Generalization should depend on travel speed not just scale.

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


## Localized Expansion Strategy Framework for Fintech Products Scaling from African to Western User Markets
**Filename:** `I--Uzoka-et_al_summarized.md`  
**Authors:** Uzoka, A. C.; Olinmah, F. I.; Okolo, C. H.; Omotayo, K. V.; Adanigbo, O. S. (2023)  
**ID:** `d41d8cd9-8f00-320b-a8b0-4f7b0b6d8f5a`  
**Odin Topics:** 9.A, 9.B, 10.A, 10.B  

**TLDR:** A framework guides African fintechs in scaling to Western markets by balancing core innovations with localization of regulation, UX, and trust.

**Problem & Motivation:** African fintechs have developed innovative mobile-first and alternative credit scoring products, but lack structured guidance for expanding into Western markets with different regulatory, cultural, and user expectations. Existing frameworks focus on Western startups entering emerging markets, leaving a gap for reverse expansion. This paper provides a framework to address that gap.

**Approach (summary):**
- Literature review of fintech globalization, localization theory, and gaps in existing frameworks.
- Four foundational principles: contextual product adaptation, regulatory integration, trust and brand repositioning, user-centric innovation.
- Three-phase strategy: internal readiness and product audit, localization and regulatory embedding, market entry and iterative scaling.

**Key Findings (selected):**
- num: Framework offers structured phases without quantitative performance metrics.
- African fintech core innovations include mobile-first design and alternative credit scoring based on mobile usage data.
- Western markets demand GDPR, PSD2, stringent KYC/AML, requiring embedded compliance.
- Trust rebuilding requires transparent communication, local partnerships, and third-party certifications.

**Limitations / Contradictions for Odin:**
- No empirical validation of the framework. [unacknowledged]
- Limited discussion of cost implications for fintechs.
- Assumes Western markets are homogeneous, ignoring intra-regional differences. [unacknowledged]

**Key takeaways:**
- Mobile-first design from African fintechs offers lessons for PFMS in low-resource settings.
- Regulatory compliance must be embedded from the start, not retrofitted.
- User trust in finance apps requires transparent privacy policies and certifications.

---


## The Psychology of Colors in UI/UX Design
**Filename:** `IA--Khandelwal-&-Chaudhary_summarized.md`  
**Authors:** Khandelwal, P.; Chaudhary, N. (2023)  
**ID:** `f6d5c4b3-a2e1-4d3c-8b7a-6f5e4d3c2b1a`  
**Odin Topics:** 9.A, 9.B, 11.A  

**TLDR:** Color psychology in UI/UX design influences user behavior, emotion, and satisfaction through strategic color choices that create visual hierarchy, emotional resonance, and navigational cues.

**Problem & Motivation:** UI/UX design lacks systematic integration of color psychology principles despite colors' proven impact on user emotion and behavior. The growing role of digital interfaces in daily life demands evidence-based color strategies to improve user satisfaction and engagement. Existing guidelines are fragmented and often ignore cultural and contextual factors.

**Approach (summary):**
- Conducted a systematic review and analysis of 10 case studies from academic journals, blogs, and websites.
- Selected case studies across domains including e-commerce, banking, health, education, and gaming.
- Evaluated case studies for relevance, validity, and reliability based on predefined criteria.

**Key Findings (selected):**
- Color psychology plays a significant role in UI/UX design, affecting user behavior, emotion, and satisfaction.
- Red evokes excitement and urgency; blue evokes calmness and trust; green evokes growth and harmony.
- Context, culture, and individual differences moderate how colors are perceived and effective.
- Common challenges include difficulty measuring color effects, lack of universal standards, and ethical concerns.

**Limitations / Contradictions for Odin:**
- "Difficulty measuring and quantifying color psychology effects."
- "Lack of universal color standards and guidelines for UI/UX design."
- "Ethical and social implications of color manipulation and persuasion are noted but not explored in depth."

**Key takeaways:**
- "Color psychology significantly affects user satisfaction and behavior."
- "Red evokes urgency, blue evokes trust, green evokes growth."
- "Context and culture moderate color meaning and impact."

---


## What UK Fintechs Can Learn From African Mobile Money Models
**Filename:** `I--Chepkutwo_summarized.md`  
**Authors:** Chepkutwo, D. (0)  
**ID:** `f7d3c2b1-5a4e-4d3c-8b2a-1c0d9e8f7a6b`  
**Odin Topics:** 4.B, 9.A, 9.B, 10.B, 11.A, 13.A  

**TLDR:** African mobile money models offer UK fintechs lessons in community-centered design, agent networks, frugal innovation, and trust-building to improve financial inclusion.

**Problem & Motivation:** UK fintechs struggle with digital exclusion and low trust among vulnerable populations. African mobile money systems have successfully addressed similar constraints through community-led design and frugal approaches. This paper argues that the innovation flow should reverse, with developed markets learning from Africa.

**Approach (summary):**
- Draws on case studies of M-Pesa in Kenya, MTN MoMo, and Airtel Money across Africa.
- Compares African mobile money design principles with UK fintech approaches to identify transferable lessons.
- Analyzes agent network models, USSD technology, and community-based saving mechanisms.

**Key Findings (selected):**
- "num: More than 80% of adults in Kenya have access to mobile money services as of 2024."
- "num: Approximately 7 million adults in the UK are digitally excluded or under-connected."
- "num: M-Pesa operates over 180,000 agent networks across Kenya."
- African mobile money succeeded by designing for communal needs like sending money to family and paying school fees.

**Limitations / Contradictions for Odin:**
- Lacks quantitative evaluation of proposed UK adaptations. [unacknowledged]
- Does not consider Philippine-specific financial behaviors or cultural context. [unacknowledged]
- Overgeneralizes African mobile money as a homogeneous model. [unacknowledged]

**Key takeaways:**
- More than 80% of Kenyan adults use mobile money, showing scalability of constraint-driven design.
- Agent networks of over 180,000 agents in Kenya act as human trust anchors.
- Building for the margins first leads to inclusive and resilient fintech products.

---


## Note for the Agent

The summaries above contain **essential extracts** – enough to understand each paper's relevance to Odin, including supporting evidence and limitations.
If you need additional details not shown here (e.g., **critical citations, definitions, equations, full methodology, or the complete mapping rationale**),
**ask the user to send the original summary file (`<filename>_summarized.md`) or the converted MarkItDown file(`<filename>_marked.md`)** for the specific paper(s) of interest.
Do not invent missing information. Acknowledge gaps when they exist.