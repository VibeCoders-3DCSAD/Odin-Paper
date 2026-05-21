# **CHAPTER I** **INTRODUCTION**

| This section discusses what parts or subsections are expected in the first chapter. Commonly, the introduction of a research paper is a critical section that sets the stage for the entire study. vvv |
| ----- |

## **Introduction**

The financial behavior and financial literacy of Filipinos persistently remains low in the modern day, despite a rapidly digitizing economy. National survey data from the Bangko Sentral ng Pilipinas (BSP) and the Philippine Statistics Authority (PSA) prove this consistent claim: only nearly 2% of Filipino adults can correctly answer all six financial literacy assessment items (Cacnio & Romarate, 2024), and a majority of households exhibit irregular savings behavior and high reliance on informal financial mechanisms (BSP, 2021). These patterns are not isolated to low-income groups; Dimauhanan et al. (2025) found that even among Filipino millennials, financial literacy scores remain low and long-term planning is largely absent, while Am-una (2026) observed that awareness of financial concepts among Filipino professionals rarely translates into disciplined financial behavior. This poor financial behavior and literacy are especially pronounced in young professionals aged 20 to 40 in the National Capital Region; this demographic is actively earning income, forming households, and assuming financial obligations, yet they lack structured financial management skills needed to translate income into long-term security for themselves and their households (Albert et al., 2024).

| ^^^ The discussion of financial literacy, behavior, millennials, and professionals should be separated for readability. Revise this paragraph, focusing on the national financial literacy problem in the Philippines. |
| ----- |

Improving financial behavior and literacy among this demographic carries significance primarily for the target user and additionally for their household and the nation as a whole. For the individual user, financial discipline and proper budgeting contributes to wealth building, fund accumulation, and debt mitigation (Bai, 2023; Dela Torre et al., 2025). For the household, especially in the Filipino context where support for dependents and remittances are common, better financial management can reduce financial stress and increase resilience against financial shocks (Bayangos & Lubangco, 2024; Casilan & Baclagan, 2024). At the national level, higher financial literacy and more disciplined financial behavior among citizens can support greater formal savings, investments, and credit health, contributing to overall economic stability (Albert et al., 2024; Akinyemi, 2025). Conversely, poor financial behavior and literacy in young professionals can be detrimental. The consequences are chronic: difficulty covering long-term expenses, borrowing and relying on debt to cover regular expenses, and an inability to allocate money for savings and major goals (Cacnio & Romarate, 2024; Flores, 2025).

| ^^^ This one as well; revise this, focusing on Filipino young professionals in NCR. |
| ----- |

Intelligent personal budgeting systems enhanced with machine learning and algorithms…

| ^^^ Add a transition sentence before introducing intelligent systems. |
| ----- |

…have emerged as a promising solution to these challenges, moving beyond passive transaction entry and statistics toward more predictive and behavior-aware guidance (Bhavana et al., 2025; D'Acunto & Rossi, 2023). Commercially available mobile applications offer basic expense categorization and overspending alerts. However, these applications share a common limitation: they do not integrate intelligent features such as financial behavioral profiles, spending forecasts, and budget recommendations into their systems (Elliyana et al., 2025). Academic literature has demonstrated that the application of Long Short-Term Memory (LSTM) networks for spending forecasting is feasible in financial contexts (Bhavana et al., 2025). The gap is further supported by a pilot survey conducted among the target demographic, which, from a total of 45 respondents, found that 57.8% do not use any application or tool at all, and 22.2% use basic spreadsheet applications or notebooks to log their budgets. The survey also highlighted the numerous challenges the respondents face in personal finance: 60% of respondents believe their income is not enough to cover their expenses, 48.9% believe they lack spending discipline, and 31.1% have difficulty tracking their spending.

To address this gap, this study develops Odin, a mobile and web personal budget management system designed specifically for Filipino working professionals aged 20 to 40 in Metro Manila. Odin combines various intelligent features to provide personalized and adaptive budget guidance. Its key features include financial behavioral profile classification to classify users during onboarding based on income stability and obligation weight, income and spending transaction entry with locally validated spending categories, spending forecasting to show predicted expenditures for the selected time horizon, intelligent budget recommendation designed according to the user's profile, transaction history, and preferences, overspending alerts for transactions exceeding budget thresholds, savings goal tracking, and debt management. By grounding both its predictive models and its advisory logic in the actual income patterns, obligation structures, and behavioral profile of the user, Odin offers a solution that is not merely technically sophisticated, but contextually relevant. Odin can help Filipino young professionals move from reactive spending toward informed financial planning, and further develop their financial discipline and health.

| ^^^ For me, your paragraph contains too many system features in one block, making it difficult to read for the readers of your manuscript. My suggestion is to convert the features into a bullet or numbered format for better presentation. Additionally, explain briefly how the following: 1\. LSTM algorithm handles forecasting 2\. Isolation Forest handles anomaly or overspending detection Currently, Isolation Forest is mentioned in the title but not clearly explained in the introduction. But try to ask your course adviser as well if it's ok to do it in a bullet format. UP: Ma'am Cervantes stated that a bulleted format is not allowed in the Introduction section. She suggested that the key feature list be reduced to only the primary features. |
| ----- |

## **Project Context**

| In the opening paragraph, it is essential to provide an introduction to the broader field of study, setting the stage for your specific research focus. This context establishes the relevance of your research within a larger domain. You may begin by outlining the significance of the overarching topic, discussing its contemporary relevance, and highlighting the key issues or trends. vvv |
| ----- |

The intersection of financial technology and machine learning has reshaped how individuals manage personal finances. Mobile and web-based budgeting applications have moved from passive expense recording toward intelligent systems capable of forecasting future spending and delivering personalized financial guidance (D'Acunto & Rossi, 2023; Ellyana et al., 2025). LSTM has demonstrated strong performance in modeling financial time series data, enabling accurate spending predictions based on historical patterns (Bhavana et al., 2025). Together, these techniques represent an innovative approach to what personal finance and budget management systems can offer.

| In the second paragraph, you can delve deeper into your specific research area within the broader field. Explain why this particular aspect of the topic is worth investigating. Discuss the relevant literature and existing research that has laid the foundation for your research focus. This should help the reader understand why your specific angle on the topic is important and the knowledge gaps or unanswered questions it addresses. vvv |
| ----- |

Within the broader domain of machine learning-driven personal finance and budget management, the specific focus of this study is the application of a classification algorithm, LSTM, and a recommendation algorithm to the digital budgeting needs of Filipino young professionals in Metro Manila. The income structures, spending patterns, financial behavioral profiles, and cultural nuances of Filipino young professionals differ substantially from those of users in foreign countries, for which the aforementioned intelligent budgeting tools were designed (Cho, 2024; Casalhay et al., 2025). This creates a need for a context-specific system that adapts its techniques to local financial realities, including variable freelance income, government contribution requirements, and cultural and religious practices such as padala, donations, and paluwagan (Casino et al., 2025; Donato et al., 2023; Bayangos & Lubangco, 2024).

| ^^^ Add a paragraph specifically explaining: 1\. Why Isolation Forest was selected 2\. Its role in anomaly detection or overspending detection 3\. Related studies using Isolation Forest in finance or fraud detection This is important for the consistency between your title and the proposed system. |
| ----- |

| In the third paragraph, transition to a clear and concise presentation of your main research problem or questions. State your problem in a straightforward manner, emphasizing its significance. This paragraph should provide a seamless transition from the general topic to the specific problem your study seeks to address. vvv |
| ----- |

The core problem that this research aims to address is the absence of a locally-developed, machine learning-driven personal budget management system tailored to Filipino young professionals aged 20 to 40 residing or working in Metro Manila. While commercial budgeting applications and academic prototypes have demonstrated the technical feasibility of LSTM in spending forecasting, none have been designed to accommodate the specific financial behavioral profiles that characterize this demographic. This gap means that Filipino young professionals who wish to benefit from intelligent budgeting tools must either adapt to systems built for foreign financial contexts or forgo such tools entirely.

| To establish the existence of the problem, the fourth paragraph should present evidence or data that supports the claim that the problem you've identified is real and substantial. Cite relevant statistics, studies, or real-world examples that illustrate the issue's prevalence or impact. This evidence not only reinforces the importance of your research but also helps convince the reader of the problem's validity. vvv |
| ----- |

The existence of this problem is substantiated by national financial data, academic research, and the pilot survey conducted among the target demographic. The Bangko Sentral ng Pilipinas reported that while 57.4% of total retail transactions were conducted digitally in 2024, structural gaps in financial management behavior persist (Mesina-Romero et al., 2024). Only 2% of Filipino adults correctly answered all six financial literacy assessment items, and 41% borrow money not for emergencies but to meet regular spending needs (Cacnio & Romarate, 2024). Even among those who engage with digital financial tools, adoption does not necessarily translate into sound financial behavior: Bongado et al. (2025) found that digital wallet usage among Filipino students did not correspond to improved financial discipline, and Calanog et al. (2025) documented the prevalence of impulsive buy-now-pay-later behavior facilitated by digital platforms. The pilot survey of Filipino young professionals in Metro Manila (N=45) found that the majority rely on no formal budgeting tool, with 51% reporting that their income is insufficient to cover expenses and 27% citing difficulty tracking expenses. These findings confirm that the target population not only struggles with basic budgeting, but also lacks access to intelligent digital tools adapted to their financial realities.

| In the fifth paragraph, delve into a discussion of the causes and effects of the main problem. Explain what factors contribute to the problem's existence and why it persists. Discuss the consequences or implications of the problem, both on a broader scale and within specific contexts. This analysis helps the reader grasp the complexity and significance of the issue. vvv |
| ----- |

The persistence of this problem can be attributed to the following factors. The first pertains to a behavioral and attitudinal context: research on financial behavior in Filipinos documents a tendency to prioritize immediate needs over long-term planning, and a reliance on informal saving methods that hinder disciplined budgeting (Am-una, 2026; Flores, 2025; Garcia, 2025). The second pertains to a structural context: the financial obligations of Filipino young professionals go beyond categories captured by most personal financial tools. Examples of such obligations include statutory government contributions (SSS, Pag-IBIG), community collections, religious donations, family remittances, and informal rotating savings arrangements (paluwagan) (Casino et al., 2025; Donato et al., 2023; Domingo, 2026; Bayangos & Lubangco, 2024). These factors cause existing intelligent budgeting systems to produce less relevant and generic forecasts and recommendations, which discourages sustained use. Consequently, young professionals remain trapped in reactive spending cycles, unable to leverage machine learning-driven tools that could otherwise assist in building savings, reducing debt, and achieving financial stability (Ataza et al., 2024; Espiritu, 2025). Addressing this gap through a locally and contextually designed system can potentially improve financial outcomes, not only for individuals but also for their families, communities, and the broader economy (Albert et al., 2024; Akinyemi, 2025).

## **Purpose and Description of the Study**

| In this section, you will introduce the perceived solution to the problem addressed in your research. Explain the strategy or approach that your study will take to address the problem. Additionally, highlight the key system features or components that will be integral to this solution.Start by discussing the identified problem briefly. You have already established this problem's existence and significance in previous sections. Introduce the perceived solution. This could be the development of a specialized system, a novel methodology, or an innovative approach to tackling the problem. Outline the core strategy or methodology you plan to employ. Explain how this strategy aligns with the specific problem you're addressing. This provides context for the reader, helping them understand how your solution is tailored to the problem. Detail the key system features or components that are central to your solution. This can include technology, algorithms, or methods that make your approach unique and effective. These features should directly support the proposed solution. vvv |
| ----- |

In response to the gap between Filipino young professionals' financial management needs and the capabilities of existing budgeting tools, this research proposes the development of Odin, a personal budget management system that integrates a classification algorithm, LSTM, a recommendation algorithm, and a rule-based algorithm. The core strategy of this solution involves: (1) classifying users into financial behavioral profiles based on income stability and obligation weight during onboarding; (2) training the classification model to correctly classify users into the correct financial behavioral profile; (3) training the LSTM model on historical transaction data to predict future spending per category over weekly and monthly horizons; (4) training a recommendation model to construct an accurate and appropriate budget allocation structure based on the user's financial behavioral profile, previous transactions, and user preferences; (5) implementing a rule-based algorithm to flag transactions exceeding their allotted budget size, and; (6) delivering savings goal tracking and debt management guidance aligned with BSP finance competency areas. Key system features include a locally validated spending category structure, financial behavioral profiles, spending forecasting, intelligent budget recommendations, and overspending detection.

| In this section, you will clearly state the primary purpose of your research. Describe what you intend to achieve with your study and how it directly relates to the perceived solution presented in the first paragraph. Begin by explicitly stating the purpose of your study. This purpose should be specific and concise. Connect the purpose to the problem you identified earlier. Explain how achieving this purpose will contribute to addressing the problem or filling a knowledge gap. Highlight the desired outcomes or results that will indicate the successful accomplishment of your study's purpose. vvv |
| ----- |

The primary purpose of this study is to design, develop, and evaluate Odin as a functional mobile and web personal budget management system for Filipino young professionals aged 20 to 40 residing or working in Metro Manila. This purpose directly addresses the absence of a locally developed, machine learning-driven budgeting tool that accounts for the specific financial realities of this demographic, including variable income structures, obligations, and spending categories unique to their financial realities. By achieving this purpose, the study aims to provide Filipino young professionals with an intelligent tool that can provide predictive, behavior-aware financial guidance, thereby improving budgeting discipline and supporting progress towards savings and debt reduction goals.

| In this section, you will emphasize the significance of your research within the larger context of the field or industry it pertains to. Discuss the potential impact and benefits of your study, both theoretically and practically.Start by explaining why your study is significant. What makes it relevant and important? Consider the potential implications for the field, industry, or community. Discuss the practical applications or real-world relevance of your research. How might the findings or outcomes of your study be applied to solve real problems or improve existing systems? Mention any potential contributions to the academic field, such as advancing knowledge or methodologies in a particular area of study. vvv |
| ----- |

This study holds significant implications for both the target users and the broader field of financial technology in the Philippine context. For Filipino young professionals, Odin offers a practical, accessible solution to improve their personal budget management, reduce debt reliance, increase formal savings behavior, and foster long-term financial planning and discipline (Bai, 2023; Dela Torre et al., 2025). For the field of financial technology, this research contributes a reference architecture that combines a classification algorithm, LSTM, a recommendation algorithm, and a rule-based algorithm within a single personal budget management system. This research also contributes a financial behavioral profile framework and locally derived spending category framework grounded in national income and expenditure data, which can be adapted for other Philippine contexts (Ama, 2025). Furthermore, the study's adherence to ISO/IEC 25010:2023 quality standards and its use of the System Usability Scale (SUS) provide a rigorous evaluation framework that may inform future intelligent personal finance system development in emerging economies. Ultimately, this research seeks to bridge the gaps between advances in machine learning-driven techniques, personal finance and budgeting systems, and the everyday budgeting needs of Filipino young professionals, contributing to improved individual financial outcomes and the broader national goal of financial inclusion, literacy, and stability.

| ^^^ I dunno if this is the new format for discussion of the significance of your study. My suggestion is to separate significance into the following: 1\. Users 2\. Researchers 3\. Developers 4\. Financial technology sector But once again, consult it as well with your course adviser. |
| ----- |

## **Objectives**

| Begin your objective with a clear and concise statement of purpose. In this case, the purpose is to create a web-based scoring application for Arnis techniques. Clearly specify what the study aims to cover. In this case, it's basic Arnis striking and blocking techniques. Include the method, algorithm or technology you will use to achieve your objective. Here, it's the HPE algorithm (Human Pose Estimation). State what you expect to achieve by implementing this web-based scoring application. In this case, the expected outcome is the automation of the scoring process and convenience in learning for all entities involved. Use action verbs to convey what you intend to do. In this case, verbs like "design," "develop," and "implement" indicate specific actions. vvv |
| ----- |

The study aims to develop a web and mobile-based intelligent personal budget management system using machine learning algorithms to improve budgeting discipline and financial management among Filipino young professionals. The general objective of the study is to develop a web and mobile-based personal budget management application with financial behavioral profile classification, spending forecasting, budget recommendation, and overspending detection features using a classification algorithm, LSTM, a recommendation algorithm, and a rule-based algorithm, which may improve the budgeting health, spending behavior, and financial discipline of the target users.

| ^^^ The general objective is too long and contains too many embedded ideas. Shorten it and focus on the primary goal only. |
| ----- |

## **Specific Objectives**

In order to fulfill the main objective of this project, the authors constructed the following specific objectives: 

| This objective aims to establish a strong foundational understanding of the key components related to Arnis poses and scoring. Ensure that the objective specifies what aspects of the business process are relevant to your research. If no business understanding is required then this objective may be optional. vvv |
| ----- |

1. Examine and understand Filipino financial behavioral patterns as well as the behavioral profiles and preferences used in categorizing such.

| This objective outlines the need to review and analyze available systems, emphasizing the relevance of benchmarking but keeping it optional. Ensure the scope of relevant systems is defined. vvv |
| ----- |

2. Explore existing systems or applications of predictive modeling algorithms, recommendation algorithms, classification algorithms, and overage detection algorithms that are relevant to the development of a personal budget management system.

| This objective focuses on data preparation, which is crucial for subsequent modeling. It ensures that the data is in a suitable format for algorithm development. vvv |
| ----- |

3. Analyze, understand, and perform preprocessing activities on the data gathered towards the development of a personal budget management system.

| This objective sets clear guidelines for model training and evaluation, emphasizing the use of specific metrics to measure the model's effectiveness. vvv |
| ----- |

4. Train and evaluate the four models and algorithms of the system using the following evaluation metrics:  
   1. LSTM (Spending Forecasting)  
      1. MAE (Mean Absolute Error)  
      2. SMAPE (Symmetric Mean Absolute Percentage Error)  
      3. MDA (Mean Directional Accuracy)  
      4. RMSE (Root Mean Square Error)  
   2. Classification Algorithm (Profile Classification)  
      1. Accuracy  
      2. Precision  
      3. Recall  
      4. F1-Score  
   3. Recommendation Algorithm (Budget Recommendation)  
      1. MAPE (Mean Absolute Percentage Error)  
      2. RMSE (Root Mean Square Error)  
      3. Variance Analysis  
   4. Rule-Based Algorithm (Overage Detection)  
      1. Accuracy  
      2. Precision  
      3. Recall  
      4. F1-Score

| ^^^ Make sure to discuss this in your Chapter 3 (Methodology) or System Architecture section. |
| ----- |

| This objective outlines the specific features the web application should have, ensuring clarity in the development process. vvv |
| ----- |

5. Design and develop a mobile and web-based application with the following key features:

| Use modules (key features) until integration. vvv |
| ----- |

   1. Financial behavioral profile classification into one of the four profiles (Stable-Flexible, Stable-Obligated, Variable-Flexible, Variable-Obligated) during onboarding, with reclassification triggered by changes in income and spending patterns;  
   2. Dashboard with a quick display of spending forecasting; transaction entry, budget plan & health, and overage alerts;  
   3. Manual income and spending transaction entry with predefined spending categories (Essential, Discretionary, Obligatory, Financial), plus scheduled transactions for recurring, automatic logging;  
   4. LSTM-driven spending forecasting, showing the predicted total and per-category spending for the upcoming time horizon (daily, weekly, monthly), plus cold-start fallback forecasting, showing a profile-average baseline forecast derived from pre-trained model priors, triggered when the user's transaction history is insufficient for personalized forecasting, with visible indicator that the forecast is not yet personalized;

| ^^^ Split into two separate objectives: personalized forecasting and cold-start forecasting mechanisms. |
| ----- |

   5. Budget recommendation anchored to the user’s profile, preferences, and transaction history;  
   6. Overage detection that alerts the user whenever spending has exceeded in a category;  
   7. Savings goal tracking, defining savings target and monitoring cumulative progress based on transaction data, with long-term goal projection, and;  
   8. Debt management presenting both the options of Avalanche and Snowball repayment strategies.

| This objective highlights the importance of system testing based on established quality standards, ensuring robust evaluation. Note that testing and test cases may vary depending on the software development methodology chosen by the researchers and developers. vvv |
| ----- |

6. Test the functionality (based on test cases) and non-functionality of the system:  
   1. Functional requirements:  
      1. Financial behavioral profile module;  
      2. Dashboard module;  
      3. Transaction entry module;  
      4. Spending forecasting module;  
      5. Budget recommendation module;  
      6. Overage detection module;  
      7. Savings goal tracking module, and;  
      8. Debt management module.  
   2. Non-functional requirements:  
      1. Response time standards (≤ 2–3 seconds)  
      2. Latency thresholds (≤ 500–800ms delay in normal conditions; ≤ 800–1000ms  delay under load)  
      3. Throughput standards;  
      4. Concurrent users stability under expected peak usage (15–100 concurrent users);  
      5. Load testing and stress testing;  
      6. Error rate standards (0-2%), and;  
      7. Test duration (5–15mins sustained load)

| This objective reinforces the commitment to rigorous evaluation based on internationally recognized standards. vvv |
| ----- |

7. Evaluate the system using a set of metrics based on the ISO/IEC 25010:2023 standards which focuses on:  
   1. Visual layout  
      1. User interface aesthetics  
      2. Accessibility  
      3. Appropriateness recognizability  
   2. Interface element design  
      1. Operability  
      2. User error protection  
      3. Accessibility  
      4. Appropriateness recognizability  
   3. Behavior  
      1. Functional suitability  
      2. Operability  
      3. Performance efficiency  
      4. User error protection

| This objective signifies the culmination of the research, where the system is made ready for real-world application. vvv |
| ----- |

8. Implement and deploy the personal budget management system to the mobile and web platform.

| The "Scope and Limitations" section of your research study is essential for defining the boundaries and constraints within which your work operates. It helps readers understand what your study encompasses and what aspects it does not address. Here's how you can write this section, focusing on the key elements you mentioned: vvv |
| ----- |

## **Scope and Limitations**

| Utilization of the Algorithm \- The primary focus of this research is the utilization of the algorithm for the design and development of an application. The algorithm serves as the foundational technology driving the core functionalities of the application. vvv |
| ----- |

The core focus of this research revolves around the application of a classification algorithm, LSTM, a recommendation algorithm, and a rule-based algorithm to design the modules of a personal budget management system.

| List of System Features: The study discusses system features that the application incorporates to address its intended objectives. While not detailed in this section, these features guide the application's functionality and user experience. vvv |
| ----- |

The study outlines a comprehensive list of system features, which form the functional framework of the application. These features include financial behavioral profile classification, dashboard, income and spending transaction entry and history, spending forecasting, intelligent budget recommendation, overage detection, savings goal tracking, and debt management. While not detailed in this section, they guide the overall functionality and user experience of the application.

| Geographical Scope: The geographical scope of this research extends to \[Specify the geographic region or regions relevant to your study\]. Data collection, testing, and user interaction are expected to occur within this defined geographical region. vvv |
| ----- |

The geographical scope of this research extends to the four districts of the National Capital Region, also known as Metro Manila. Data collection, testing, and user interaction are expected to occur within this defined geographical region.

| Temporal Scope: The study encompasses data collected and system development activities conducted during the period from \[Specify the start date\] to \[Specify the end date\]. vvv |
| ----- |

The study encompasses data collected and system development activities conducted during the period from the start of the 1st Semester, A.Y. 2026-2027 to the end of the 2nd Semester, A.Y. 2026-2027. It acknowledges that technological advancements beyond this temporal scope may not be considered in the study.

| Tools for System Design and Development: The study employs a range of tools and technologies for the design and development of the application. These tools include \[Specify the tools or software used for system design and development\]. vvv |
| ----- |

The study employs a range of tools and technologies for the design and development of the application. These tools include:

| ^^^ The inclusion of exact software versions (e.g., React v19.2.0, Python v3.14.4) may become outdated quickly and is too detailed for Chapter 1\. Write the detailed software versions in the System Design/Implementation chapter and retain only major technologies in Chapter 1\. |
| ----- |

1. React Native v0.83, React v19.2.0, React Native for Web v0.21.0, Expo SDK v55.0.0, as the primary frontend development technologies that will be used to build the application on mobile and web;  
2. TypeScript v5.9.2 as the language for writing the frontend and the main backend;  
3. Node.js v24.15.0 LTS, Express.js v5.1.0, as the primary backend development technology that will be used to develop backend-processes;  
4. FastAPI v0.135.3, as a secondary backend that will be used to develop the microservice for the machine learning;  
5. Python v3.14.4 as the secondary language for writing processes that concern ML;  
6. TensorFlow v2.21.0, scikit-learn v1.8.0, as the machine learning libraries that will be used for development, training, and inference;  
7. PostgreSQL v18.3, Supabase, @supabase/supabase-js v2.57.4, as the database and backend service deployment that will be used for authentication and data storage;  
8. Google Cloud Run, Docker, Uvicorn, as the DevOps and deployment technologies used for containerization, application serving, and cloud deployment of the backend and machine learning services;  
9. NativeWind, Tailwind CSS, @expo/vector-icons, React Native Paper, as the styling, iconography, and component libraries that will be used for designing and development of the application's interface;  
10. Git, GitHub, as the version control and repository management technologies used for tracking source code changes and supporting collaborative development;  
11. Playwright, Jest, React Native Testing Library, Supertest, Pytest, FastAPI Test Client, as primary testing technologies used for end-to-end, unit, component, and API testing across the frontend, backend, and machine learning service.

### **Limitations**

| ^^^ Your limitations discuss LSTM but still lack detailed mention of Isolation Forest limitations. Include limitations of Isolation Forest such as the following: 1\. Possible false positives 2\. Sensitivity to unusual spending patterns 3\. Dependence on transaction quality |
| ----- |

### 

Despite the study's objectives, there are certain limitations that should be acknowledged:

| Algorithm Dependency: This study heavily relies on the specified algorithm for its success. The effectiveness of the application is contingent on the performance and accuracy of this algorithm. Any limitations or constraints of the algorithm may consequently impact the application's performance. vvv |
| ----- |

This study is heavily reliant on the performance of its classification algorithm, LSTM, recommendation algorithm, and rule-based algorithm. LSTM requires a sufficient volume of historical transaction data before spending forecasts become reliable. Users in the early stages of system use will receive the cold-start fallback forecast based on a profile-average baseline until adequate transaction history accumulates. Any inherent limitations of these algorithms directly constrain the system's intelligence.

| Generalization: The findings and outcomes of this research are specific to the context, geographical area, and time frame defined in the scope. The generalizability of the application's performance to other regions or periods may be limited. vvv |
| ----- |

The findings and outcomes of this research are specific to the context, geographical area, and time frame defined in the scope, namely: Filipino young professionals aged 20 to 40 residing or working in Metro Manila. Data collection and system development is conducted from the first semester of Academic Year 2026-2027 through the second semester of Academic Year 2026-2027. The system's financial behavioral profiles based on income stability and obligation weight, locally derived spending categories, and advisory logic may not generalize without modification to other demographics such as high school students, senior citizens, and OFWs, other regions of the Philippines, or other countries with different financial cultures, income structures, and obligation structures.

| External Factors: External factors such as network connectivity, hardware constraints, and user-specific behaviors are beyond the study's control and may influence the application's performance. vvv |
| ----- |

The performance and accessibility of Odin are subject to external conditions beyond the research team. These include network connectivity availability on users' devices, compatibility constraints across Android device models and browser environments, and broader economic or policy changes, such as adjustments to contribution rates for SSS, PhilHealth, and Pag-IBIG, that may affect the accuracy or relevance of the system's spending categories or advisory logic over time. The study does not account for such changes beyond the defined temporal scope.

| Note: Multiple operational definitions of terms is a section where terminologies will be introduced and discussed how it will be used. The terminologies will be in a narrative format where terminologies are italicized. Example is presented below: vvv |
| ----- |

## **Definition of Terms**

Financial Literacy is a dimension in making financial decisions. According to Rodriguez et al. (2024), financial literacy directly affects expenditure through financial behaviors. The better their financial knowledge, the better spending decisions are made while adopting positive financial habits like budgeting and saving. In this study, we will use financial literacy as a measure on how Filipino young professionals will utilize informal financial mechanisms in managing their finances.

Informal Financial Mechanisms is a financial service that is not regulated or supervised by government central banks such as paluwagan and loan or lending. It includes peer-to-peer lending, group savings, and informal money lending. Bongalonta (2024) has stated that the faculty members of SorSU Bulan Campus utilizes this method along with the modern style of investment for saving their finances and have encountered issues regarding the lack of financial literacy. This study takes into account the potential risk of mismanagement in finances from Filipino young professionals using these methods.

Paluwagan is an informal financial mechanism, group saving or money-lending system in the Philippines built and relying on trust and commitment among participants, hence lacking formal regulation and resulting in the occasional misuse of the pooled funds (Bongalonta, 2024). This study analyzes how group spending habits in paluwagan affects the financial behavior of Filipino young professionals. It will also identify how Filipino young professionals will utilize this informal financial mechanism in managing their finances.

Loan or Lending is a financial mechanism that allows individuals to borrow money from each other with agreed-upon terms and interest rates. Bongalonta (2024) states that poor debt management unfavorably affects their finances and savings. There were also issues regarding their liquidity and solvency when it comes to monetary liabilities. This study creates a solution to address the said issues with the use of financial tracking and debt management strategies to help individuals better manage their debts and improve their financial health. 

Financial Obligation partially shares the same concept as Tambuli and Villarba's (2026) Personal Financial Behavior (PFB), where individuals who are more confident in their financial management skills exhibit more predictable and positive financial behaviors. It refers to the extent to which individuals feel prepared to handle their financial commitments and manage various financial responsibilities.

Personal Budget Management System is a system that analyzes the financial data of an individual and provides personalized budget recommendations. It is designed to help individuals track their income and expenses, create budgets, and monitor their progress towards financial goals (Badiger et al., 2026). In the context of this study, it is utilized to analyze the financial data of Filipino young professionals and provide personalized budget recommendations based on their financial behavior, spending habits, cultural influence, and economic status.

Financial Behavioral Profile is a feature in our system that classifies users into one of four profiles (Stable-Obligated, Stable-Flexible, Variable-Obligated, and Variable-Flexible) based on onboarding information to personalize budget guidance. By definition, financial behavior is the study of how individuals make financial decisions and how these decisions affect their financial well-being (Tambuli and Villarba, 2026).

Spending Forecast is a feature in our system that predicts future spending based on historical data. It analyzes previous spending habits and patterns to generate predictions for future spending. The spending forecast covers the next 7 days with the use of the LSTM AI model.

Recurrent Neural Networks (RNNs) is a class of deep learning models that possess the capability to process and forecast sequential data (Mienye et al., 2024). This makes them valuable in modeling complex financial time series patterns, thus being utilized for the Spending Forecast feature of the system.

Long Short-Term Memory (LSTM) is a variant of RNNs. It has long-term dependency and it can selectively remember information. LSTMs are uniquely effective at modeling tasks that require understanding context over long periods (Mienye et. al., 2024).

Cold-Start Fallback is a solution for when the forecasting algorithm does not have enough data to fine-tune results forecasts and budget results for the users. The cold-start problem occurs when an ML model does not have enough data to make accurate predictions (Yuan and Hernandez, 2023). This can happen when a user first joins the platform and does not have enough historical data to train the model.

Recurring Transaction refers to transactions that are repeated on a regular basis such as subscriptions, rent, and loan payments. Our paper assumes potential issues to arise from incorrect management of these transactions, and thus becoming a part of this study's scope. As stated by Reena and Murugesan (2026), recurring payments, automatic renewals, and multiple subscriptions can influence spending habits and financial judgement. Greater financial awareness is needed to avoid certain issues such as unexpected charges, subscription fatigue, and difficulty in cancellation.

Debt Management Strategy is a method used to manage and repay debts. It is critical for maintaining creditworthiness and minimizing financial stress. Strategies such as consolidating high-interest, debts, timely repayments, and avoiding unnecessary borrowing ensures that debt remains manageable (Yoganandham, 2025). Our paper utilizes this concept to create a solution to address the issues of poor debt management encountered by the Filipino young professionals, namely the strategies Avalanche and Snowball.

Avalanche Strategy is a type of debt management method that prioritizes paying off debts with the highest interest rates first to minimize total interest paid, while taking longer to accomplish. This method simplifies repayment by combining high-interest debts into a single loan or refinancing existing ones (Yoganandham, 2025). The system will analyze what kind of debt management strategy the user has based on their historical financial data.

Snowball Strategy is a type of debt management method that prioritizes paying off debts with the smallest balances first to build momentum and motivation, while being the shortest to accomplish. This method creates momentum for larger debts (Yoganandham, 2025). The system will analyze what kind of debt management strategy the user has based on their historical financial data.  
