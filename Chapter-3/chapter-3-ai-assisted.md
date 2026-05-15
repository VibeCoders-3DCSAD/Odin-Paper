# CHAPTER III

# DESIGN AND METHODOLOGY

This chapter of the paper presents an overview of the proposed study's fundamental theoretical foundations. The research framework is guided by these foundations in order to give substantial results to the research questions at the conclusion of the study. It was also utilized to monitor the progression of the system's workflow.

## Research Design

In this research, a multifaceted research design has been adopted, encompassing developmental, applied, and descriptive evaluative research methodologies. Developmental research is employed to track the progression of the Odin application's development over time, aligning with the research objective of addressing the dynamic budgeting behavior of Filipino young professionals. 

Applied research plays a pivotal role, focusing on the development of a practical web and mobile personal budget management system, effectively addressing real-world financial management challenges faced by users managing variable incomes and cultural obligations.

 Additionally, descriptive research, enriched with evaluative components, allows for a comprehensive examination of the system's effectiveness. This is achieved by combining user surveys to gather practitioner perspectives and detailed testing to assess the accuracy of the integrated machine learning algorithms and the usability of the application. This comprehensive methodology bridges theory and practice, offering both theoretical insights and practical solutions tailored to the financial realities of the target demographic.

## Research Methodology

In this research endeavor, an Agile methodology is conscientiously adopted, providing a dynamic and adaptive framework to navigate the complexities of the study. The methodology encompasses distinct phases, each contributing to the research process in a unique manner.

### Phase 1: Review

The research commences with a comprehensive review and planning phase, mirroring Agile's initial stage. During this phase, the project's objectives are collaboratively defined, outlining the scope of the Odin budget management system and identifying key stakeholders. Open communication and collaboration are pivotal, ensuring that the system is properly tailored to the specific context of Filipino young professionals in Metro Manila. This includes defining non-negotiable expense categories such as culturally obligated spending (*paluwagan*, *utang na loob*, remittances) and establishing the requirement for a mobile-first, privacy-centric design. The iterative review of these requirements fosters a clear understanding of the project goals among the development team, setting a solid foundation for subsequent phases.

### Phase 2: Algorithm Section

Following the establishment of requirements, the algorithm design and model architecture are formulated to align with the research objectives. The core of Odin relies on several distinct machine learning and optimization algorithms designed to accommodate specific financial behaviors. For User Financial Behavioral Profile Classification, XGBoost and LightGBM are implemented to evaluate observed transaction behavior, goal commitment, and income type. To address cold-start scenarios, fuzzy K-means clustering is utilized. For Spending Forecasting, Long Short-Term Memory (LSTM) networks are designed as the primary algorithm to handle longitudinal expenditure data and seasonal spikes, with LightGBM and ARIMA serving as fallbacks for intermittent categories or limited data. The Budget Recommendation module is structured around Goal Programming or Sequential Quadratic Programming (SQP) to maximize savings while strictly protecting culturally obligated expense categories. Lastly, Anomaly Detection utilizes the Isolation Forest algorithm, augmented with a critical cultural-calendar override to prevent the misclassification of legitimate cultural spending spikes as anomalies.

### Phase 3: Data Collection

The data collection strategy is essential for establishing the foundation upon which the system's algorithms are trained and evaluated. This phase involves gathering representative financial data, encompassing demographic factors such as marital status and employment type, alongside longitudinal transaction histories. Because the system relies heavily on manual transaction entry as a privacy-by-design measure, data collection efforts simulate this environment by compiling datasets that reflect real-world manual inputs categorized according to localized frameworks (e.g., extended FIES/PCOICOP categories). The collected data undergoes rigorous cleaning and preprocessing to handle missing values, normalize features, and structure the data into suitable training, validation, and test sets.

### Phase 4: Model Training

The model training process involves the detailed implementation and fine-tuning of the selected algorithms using the prepared datasets. The classification models (XGBoost/LightGBM) are trained to accurately map users to their respective behavioral profiles based on historical data. The LSTM forecasting models are trained using backpropagation through time to predict future expenditure patterns, undergoing hyperparameter tuning via Grid Search or Random Search to optimize network configurations. Similarly, the Isolation Forest model is calibrated to detect structural outliers in transaction streams while integrating the cultural-calendar rules. The performance of these models is evaluated using specific metrics suitable for each domain: AUC-ROC for classification, MAPE and RMSE for forecasting, and VUS-ROC or AUC-PR for anomaly detection. Adjustments and iterative refinements are continuously applied to address challenges such as imbalanced datasets and to minimize false positive rates in anomaly detection.

### Phase 5: Development

After the modeling phase, we proceed to the core development phase, similar to Agile's iterative development cycle. During this phase, the application's core functionalities—such as financial behavioral profile assignment, transaction entry, spending forecasts, anomaly alerts, and budget recommendation support—are developed incrementally. Agile's incremental approach permits the gradual accumulation of insights and improvements as the team integrates the trained models into the system logic. Collaboration remains paramount, with regular review sessions enabling continuous feedback and adjustments to the application's features to ensure they meet the specific needs of the users.

### Application Design

The application design of Odin focuses on delivering a user interface (UI) and user experience (UX) that reduces friction and promotes long-term retention. Recognizing that traditional gamification often fails to retain users in financial contexts, the design relies on automated categorization, visual goal progress bars, and value-driven engagement through clear anomaly alerts and forecasts. The design implements an envelope-based multiple budget approach, providing users with intuitive workflows for managing variable incomes and fixed obligations. Wireframes and high-fidelity mockups visually represent the application's layout, ensuring that complex analytical outputs—such as predictive forecasts and intelligent budget adjustments—are translated into easily understandable, optionally explainable visual elements that enhance rather than detract from perceived user trust.

### Application/Software Development

The software development of Odin encompasses the integration of the front-end interfaces with the back-end machine learning models. Programming languages such as Python are utilized for backend development and model hosting, employing frameworks like Django or Flask to manage API requests and system logic. The front-end leverages modern frameworks (e.g., React Native or Flutter) to deploy a robust, mobile-first application capable of operating effectively even with manual, offline-capable inputs. The application is specifically engineered to interface seamlessly with the LSTM, XGBoost, and Isolation Forest algorithms, ensuring real-time or near-real-time processing of user data for timely recommendations. The development cycle includes rigorous unit testing, integration testing, and system testing. This ensures that the integration of the complex machine learning models into the user-facing application operates seamlessly under various conditions, adhering to Agile principles of iterative improvement, software quality standards (ISO/IEC 25010), and user-centered design.
