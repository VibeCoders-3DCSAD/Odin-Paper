# Comprehensive Report for Prefix: `LA--`

**Total files:** 16

This report includes problem/motivation, approach, key findings, support for Odin, and limitations/contradictions.

---


## A Decade of Applied Quantitative Analytics for Philippine Policy: Forecasting, Statistical Forensics, and Predictive Modeling Across Education, Energy, Agriculture, Health, and Finance
**Filename:** `LA--Velasco_summarized.md`  
**Authors:** Velasco, A. (2026)  
**ID:** `10.20944/preprints202603.1811.v1`  
**Odin Topics:** 6.A, 6.B, 8.A, 8.B, 12.A, 12.B  

**TLDR:** Reviews 17 Philippine policy analytics studies (2019-2025), showing progression from descriptive statistics and classical forecasting toward machine learning, deep learning, Benford-based anomaly detection, and explainable AI.

**Problem & Motivation:** Government resource allocation under uncertainty requires quantitative analytics, but no systematic review of applied methods in Philippine policy existed. Understanding methodological progress and gaps across education, energy, agriculture, health, and finance is necessary to guide future analytics infrastructure.

**Approach (summary):**
- Structured narrative review of 17 studies from 2019-2025, coded by domain, dataset, modeling approach, validation strategy, and policy contribution.
- Comparison with international literature on dropout research, electricity forecasting, crop-yield analytics, epidemiological surveillance, Benford auditing, and explainable ML.

**Key Findings (selected):**
- Early studies use descriptive statistics and univariate ARIMA/SARIMA/Holt-Winters; later studies adopt comparative machine learning, neural networks, and LSTM.
- Benford-based anomaly detection screens public health and agricultural data quality as a policy tool.
- Validation rigor is uneven: some studies use holdout splits and error metrics, others rely on residual diagnostics due to short samples.
- Interpretability appears via SHAP in diabetes prediction and theory-guided embedding in stock-index forecasting.

**Limitations / Contradictions for Odin:**
- "Corpus is heterogeneous (journal articles, preprints, SSRN papers) with differing data frequencies, sample sizes, and validation maturity."
- "Some study characteristics had to be reconstructed from metadata when full texts were not equally accessible. [unacknowledged]"
- "Direct numerical comparison across sectors is neither appropriate nor intended by the author."

**Key takeaways:**
- "Reviewed 17 Philippine policy analytics studies from 2019 to 2025."
- "Forecasting evolved from ARIMA to machine learning and LSTM."
- "Benford's law detects anomalies in health and agricultural data."

---


## "Predicting student retention: A comparative study of machine learning approach utilizing sociodemographic and academic factors"
**Filename:** `LA--Delena-et_al_summarized.md`  
**Authors:** "Delen˜a, R. D.; Diab, N. J.; Sacayan, R. R.; Sieras, J. C.; Khalid, S. A.; Macatotong, A. H. T.; Gulam, S. B." (2025)  
**ID:** `"10.1016/j.sasc.2025.200352"`  
**Odin Topics:** "12.A", "12.B"  

**TLDR:** "A comparative study of ten machine learning algorithms predicts student retention using sociodemographic and academic data from a Philippine university, with XGBoost achieving highest accuracy."

**Problem & Motivation:** "Student dropout is a persistent challenge in higher education, especially in developing regions with limited resources for intervention. Traditional approaches based on subjective assessments are insufficient to capture attrition complexity. There is a need for accurate predictive models using machine learning on institutional data."

**Approach (summary):**
- "Data from Mindanao State University (482 students, 146 variables over 2012–2022) was preprocessed using CRISP-DM and Power BI."
- "Ten algorithms were evaluated: XGBoost, Gradient Boosting, ANN, Decision Tree, Random Forest, MLP, Logistic Regression, KNN, SVM, and Naïve Bayes."
- "Models were assessed with train-test split and 5-fold cross-validation using accuracy, precision, recall, F1, MSE, and log loss."

**Key Findings (selected):**
- "num: XGBoost achieved 90.66% cross-validated accuracy and 90.72 F1 score, outperforming all other models."
- "num: Gradient Boosting had 89.42% accuracy and the lowest log loss (0.25), while ANN reached 88.39% accuracy and 91.48% recall."
- "Naïve Bayes had high recall (97.21%) but excessive false positives (31), limiting practical use."
- "Decision Tree overfitted, dropping from 90.34% to 84.44% accuracy after cross-validation."

**Limitations / Contradictions for Odin:**
- "Data sourced from a single institution may limit external validity."
- "Behavioral and psychosocial dimensions (e.g., LMS engagement, motivation) were not included."
- "Model interpretability remains a challenge for deployment in education and finance."

**Key takeaways:**
- "XGBoost achieved 90.66% cross-validated accuracy for dropout prediction."
- "Ensemble models like Gradient Boosting consistently outperform single classifiers."
- "Cross-validation is essential to avoid overfitting in educational data mining."

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


## "Predict, Optimize, Deliver: Demand Forecasting and Resource Optimization for a Market Research Firm"
**Filename:** `LA--Mariano-&-Monreal_summarized.md`  
**Authors:** "Mariano, M. T. G.; Monreal, R. N." (2025)  
**ID:** `10.1145/3785171.3785187`  
**Odin Topics:** "6.A", "6.B", "12.A", "12.B"  

**TLDR:** "Compares ARIMA, Holt-Winters, Prophet, and LSTM for demand forecasting and integrates with Pyomo-based optimization for workforce allocation in a market research firm, with Prophet achieving best balance of accuracy and usability."

**Problem & Motivation:** "Professional service firms face demand uncertainty and inefficient manual workforce planning. Existing forecasting-optimization frameworks target product-based contexts, not time-sensitive service environments with high variance. There is a need for an integrated, interpretable pipeline that connects demand forecasting, resource optimization, and visualization."

**Approach (summary):**
- "Historical time-tracking data from January 2018 to December 2024 (billable hours) for two clients."
- "Compared ARIMA, Holt-Winters Exponential Smoothing, Prophet, and LSTM using MAE, RMSE, and MAPE across multiple train-test splits and a 30-day holdout."
- "Weighted error score (0.35 MAE + 0.35 RMSE + 0.30 MAPE) plus interpretability and speed (0.25 each) for model selection."

**Key Findings (selected):**
- "Prophet achieved the lowest weighted error for Client1 (13.038) and Client2 (27.786), and the best overall score (10.456) after including interpretability and speed."
- "LSTM showed stable performance across training splits but higher complexity and data requirements reduced practical viability."
- "ARIMA and Holt-Winters performed worse under noisy, volatile demand patterns."
- "num: The optimization model achieved near-zero unmet demand under baseline and RMSE-adjusted scenarios, with occasional overutilization (e.g., 106% for shared resource S2)."

**Limitations / Contradictions for Odin:**
- "Analysis restricted to output-based variables; input-level factors like individual analyst skill were unavailable."
- "Forecasting model uses internal historical data only and does not incorporate external economic indicators."
- "Long-range forecasting caution: rare high-impact events (e.g., COVID-19 pandemic) not considered."

**Key takeaways:**
- "Prophet achieved the lowest weighted error score of 10.456."
- "Forecast uncertainty bands from RMSE improve resource allocation resilience."
- "The predict-then-optimize framework bridges predictive analytics and operational planning."

---


## Optimized Random Forest Classifier for Students Lifestyle Prediction Using Behavioral Data: A Machine Learning Approach
**Filename:** `LA--Ram-&-Agoylo_summarized.md`  
**Authors:** Ram, M. L.; Agoylo, J. C. Jr. (2025)  
**ID:** `10.54554/jtec.2025.17.02.004`  
**Odin Topics:** 5.C, 12.B  

**TLDR:** Random Forest classifier predicts lifestyle categories from behavioral data with 75.07% accuracy, validated on 93 students.

**Problem & Motivation:** Machine learning for lifestyle classification remains underexplored despite its potential. Balancing accuracy and generalization is a key challenge. Parameter optimization is needed to mitigate overfitting in behavioral analytics.

**Approach (summary):**
- Data source: Half a Million Lifestyle Dataset from Kaggle with 500,000 records.
- Preprocessing removed missing values, selected 9 behavioral features, and encoded gender numerically.
- Random Forest classifier trained with 40 decision trees to balance overfitting and generalizability.

**Key Findings (selected):**
- "num: Accuracy of 75.07% on test data, with precision 75.16%, recall 75.07%, and F1 score 74.40%."
- Training accuracy reaches 100% with 30+ trees, indicating overfitting despite strong memorization.
- Testing accuracy stabilizes around 75% beyond 20 trees, with optimal tree count 30-40.
- Real-world classification of 93 students: 41 Fitness Enthusiast, 50 Health-Conscious, 1 Eco-Friendly, 1 Social Media Influencer.

**Limitations / Contradictions for Odin:**
- "Lifestyle categories are predefined and may not capture the full spectrum of individual behaviors."
- "Self-reported behavioral data introduces potential bias. [unacknowledged]"
- "Real-world test sample of 93 students is small and from a single institution, limiting generalizability. [unacknowledged]"

**Key takeaways:**
- "Random Forest accuracy of 75.07% on lifestyle prediction."
- "Overfitting occurs with more than 30 decision trees."
- "Optimal tree count between 30 and 40 balances accuracy and efficiency."

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


## Predictive Modeling for Loan Eligibility Assessment: A Comparative Study of Logistic Regression, Random Forest, and Support Vector Machine with Detailed Oversampling
**Filename:** `LA--Pandiin-&-Matias_summarized.md`  
**Authors:** Pandiin, J. D.; Matias, J. B. (2025)  
**ID:** `c7b3a1d9-6e5f-4c2a-8b9d-1f3e5a7c9d2b`  
**Odin Topics:** 12.A, 12.B  

**TLDR:** Compares Logistic Regression, Random Forest, and SVM for loan eligibility prediction using oversampling and genetic algorithm feature selection, finding Random Forest most balanced with 85% accuracy.

**Problem & Motivation:** Manual loan approval processes are inefficient and prone to error. Existing machine learning approaches lack robust feature selection and class imbalance handling. A comparative evaluation of optimized classifiers is needed for fair and accurate loan decisions.

**Approach (summary):**
- Data from Kaggle loan dataset with binary target variable Loan_Status.
- Oversampling applied to minority class to address imbalance.
- Feature selection using Correlation, RFE, SelectKBest, Lasso, and Genetic Algorithm optimization.

**Key Findings (selected):**
- Random Forest achieved highest accuracy (85%), precision (86%), recall (84%), F1-score (85%) with Lasso feature selection.
- num: Random Forest cross-validation mean accuracy 92%.
- num: Credit History most important feature (26.8%), followed by Applicant Income (19.7%) and Loan Amount (19.2%).
- SVM achieved 99% recall but low precision (63%), indicating many false positives.

**Limitations / Contradictions for Odin:**
- Only one dataset from Kaggle, limiting generalizability.
- No comparison with deep learning methods.
- Feature selection via GA may overfit to training data [unacknowledged].

**Key takeaways:**
- Random Forest with Lasso feature selection achieved 88.5% accuracy.
- Credit history is the most important predictor at 26.8%.
- SVM has near-perfect recall but high false positives.

---


## "Data-Driven Decision Making in Scholarship Programs: Leveraging Decision Trees and Clustering Algorithms"
**Filename:** `LA--Espiritu-et_al_summarized.md`  
**Authors:** "Espiritu, F. V.; Natividad, M. C. B.; Velasco, R. A." (2024)  
**ID:** `"123e4567-e89b-12d3-a456-426614174000"`  
**Odin Topics:** "5.C", "10.A", "10.B", "12.B"  

**TLDR:** "Integrates decision trees and clustering algorithms with an online system to improve scholarship application processing, achieving 31% higher success rates."

**Problem & Motivation:** "Scholarship programs face inefficiencies from manual application review, especially with a 541.1% surge in applications. The BRO-Ed program lacks a systematic data-driven approach to evaluate applicants. This leads to missed opportunities and suboptimal resource allocation."

**Approach (summary):**
- "Used historical scholarship data from Isabela province (58,892 initial entries) as the dataset."
- "Preprocessed data by handling missing values, outliers, duplicates, and normalization."
- "Implemented C4.5 decision tree algorithm for identifying key success factors and K-means clustering for grouping similar applications."

**Key Findings (selected):**
- "num: Online registration system achieved 31% higher success rate than traditional methods."
- "num: Decision tree predictive accuracy was 80% for successful applications and 70% for failures."
- "num: Data completeness reached 95% and accuracy 95% after preprocessing."
- "num: Removed 3,100 duplicate entries from original 58,892 records."

**Limitations / Contradictions for Odin:**
- "Sample limited to Isabela province's BRO-Ed scholarship program."
- "No longitudinal validation of applicant success after scholarship award."
- "Potential bias in historical data not fully addressed. [unacknowledged]"

**Key takeaways:**
- "31% higher success rate from online system over traditional methods."
- "Decision trees achieved 80% predictive accuracy for scholarship success."
- "Data privacy included anonymization and RA 10173 compliance."

---


## "Machine Learning Approaches in Classifying Income Levels"
**Filename:** `LA--Laspinas-&-Murcia_summarized.md`  
**Authors:** "Laspiñas, E. L.; Murcia, J. V. B." (2024)  
**ID:** `"10.5281/zenodo.10049652"`  
**Odin Topics:** "12.A", "12.B"  

**TLDR:** "Six machine learning classifiers for adult income classification are compared, with RandomForest and Random Tree achieving over 98% accuracy."

**Problem & Motivation:** "Conventional econometric models struggle to capture non-linear dynamics of income distribution. Machine learning offers a data-driven alternative to improve income level prediction accuracy. This study addresses the gap by systematically comparing multiple classifiers on a real-world dataset."

**Approach (summary):**
- "Used Adult Income Prediction dataset from Kaggle with 16,281 observations and 13 features including age, occupation, education, and capital gain."
- "Applied InfoGainAttributeEval and Ranker in Weka for feature selection, identifying 'Relationship' as most predictive."
- "Evaluated Logistic, J48 (Decision Tree), RandomForest, Random Tree, IBk (k-NN), and NaiveBayes classifiers."

**Key Findings (selected):**
- "num: RandomTree achieved highest accuracy at 98.37%, correctly classifying 16,016 instances."
- "num: RandomForest achieved 98.35% accuracy with F-measure of 0.983."
- "num: J48 accuracy improved from 87.21% (C=0.25) to 90.84% (C=0.75)."
- "num: IBk accuracy decreased from 89.11% (k=3) to 85.74% (k=9), contradicting expected improvement with higher k."

**Limitations / Contradictions for Odin:**
- "The study only uses a single dataset (Adult Income) and does not test on Philippine data. [unacknowledged]"
- "No comparison with deep learning methods like neural networks. [unacknowledged]"
- "The paper does not address class imbalance or feature engineering beyond information gain. [unacknowledged]"

**Key takeaways:**
- "RandomTree and RandomForest both exceeded 98% classification accuracy."
- "Ensemble methods reduce overfitting and generalize better than single classifiers."
- "Parameter tuning (confidence factor, k) significantly alters classifier performance."

---


## When machine learning meets econometrics: Can it build a better measure to predict multidimensional poverty and examine unmeasurable economic conditions?
**Filename:** `LA--Onsay-&-Rabajante-2024b_summarized.md`  
**Authors:** Onsay, E. A.; Rabajante, J. F. (2024)  
**ID:** `10.1016/j.sctalk.2024.100387`  
**Odin Topics:** 12.A, 12.B  

**TLDR:** Random forest outperforms econometric and other ML models in predicting multidimensional poverty for indigenous communities in the Philippines, achieving 0.9208 R-squared and 95.94% accuracy.

**Problem & Motivation:** Traditional poverty measurement methods are costly, labor-intensive, and time-consuming, making it difficult for policymakers to target interventions. Indigenous communities face complex, multifaceted socioeconomic conditions that generic poverty research fails to capture. There is a need for disaggregated, cost-effective methods to measure multidimensional poverty.

**Approach (summary):**
- Data comes from a complete census of indigenous communities in Goa, Camarines Sur, Philippines (1,660 indigenous households, 8,022 persons).
- Blends econometric causality tests (logit and probit) with ML models including random forest, LightGBM, XGBoost, SVM, and linear regression.
- Uses 15 multidimensional indicators (health, housing, water, education, income, peace/order) as predictors of poverty.

**Key Findings (selected):**
- "num: Random forest regressor achieved the highest R-square of 0.92075 for impoverished societies."
- "num: Random forest classifier attained 95.94% accuracy in pipeline algorithms and 90.69% at random."
- "num: Random forest had the lowest RMSE (0.3298) compared to LightGBM (0.3642) and XGBoost (0.4001)."
- "num: For indigenous communities, random forest R-square was 0.9208 and MSE 0.5497."

**Limitations / Contradictions for Odin:**
- "Results are specific to rural poverty in the Philippines; generalizability to other domains like personal finance is untested [unacknowledged]."
- "Paper acknowledges time required to build trustworthy datasets but does not discuss real-time prediction constraints."
- "Models rely on census data updated every two years, which may not capture rapid changes in financial behavior [unacknowledged]."

**Key takeaways:**
- Random forest achieved 0.9208 R-square for poverty prediction.
- Random forest classifier accuracy was 95.94% in pipeline algorithms.
- Random forest had the lowest RMSE (0.3298) among regressors.

---


## Exploring Machine Learning for Credit Card Fraud Detection from a Philippine Perspective
**Filename:** `LA--Blancaflor-et_al_summarized.md`  
**Authors:** Blancaflor, E.; Asuncion, K. D.; Reyes, H. J.; Verzosa, M. (2024)  
**ID:** `10.1145/3698062.3698088`  
**Odin Topics:** 8.A, 8.B, 12.B  

**TLDR:** Evaluates machine learning models (SVM, ANN, k-NN, Naive Bayes, logistic regression) for credit card fraud detection in the Philippines, finding ANN achieves up to 98.44% accuracy.

**Problem & Motivation:** Credit card fraud in the Philippines increased 21% since COVID-19, with traditional fraud prevention systems inadequate due to large data volumes, imbalanced distributions, concept drift, and real-time detection needs. There is a need to customize machine learning algorithms to the Philippine economic, technological, and social context to improve fraud detection effectiveness.

**Approach (summary):**
- Data source: credit card transaction data from the Philippines (dataset size not specified).
- Methods evaluated: logistic regression, k-Nearest Neighbors, Naive Bayes, Support Vector Machines, and Artificial Neural Networks with GA and SMOTE enhancements.
- Evaluation metrics: accuracy, sensitivity, specificity, precision, Matthews Correlation Coefficient, and balanced classification rate.

**Key Findings (selected):**
- "num: ANN-SMOTE achieved the best performance with up to 98.44% accuracy."
- "num: k-NN achieved 97.69% accuracy and Naive Bayes 97.92% accuracy."
- "num: Logistic regression had the lowest accuracy at 54.86%."
- A trade-off exists between model accuracy and explainability; logistic regression is better for regulatory compliance.

**Limitations / Contradictions for Odin:**
- "No explicit dataset size or transaction volume provided. [unacknowledged]"
- "All reported accuracies are from cited secondary sources, not original experiments. [unacknowledged]"
- "Real-time detection challenges mentioned but no latency or throughput benchmarks given."

**Key takeaways:**
- "ANN-SMOTE achieves 98.44% accuracy for fraud detection."
- "Imbalanced data handling is critical for anomaly detection."
- "Explainability trade-off matters for regulatory compliance."

---


## "Use of Boosting Algorithms in Household-Level Poverty Measurement: A Machine Learning Approach to Predict and Classify Household Wealth Quintiles in the Philippines"
**Filename:** `LA--Salvador_summarized.md`  
**Authors:** "Salvador, E. L. V." (2024)  
**ID:** `"8a7b6c5d-4e3f-2a1b-9c8d-7e6f5a4b3c2d"`  
**Odin Topics:** "5.C", "6.A", "12.B"  

**TLDR:** "Boosting algorithms, especially CatBoost, accurately classify household wealth quintiles using Philippine DHS data, with CatBoost achieving 90.93% accuracy."

**Problem & Motivation:** "Poverty measurement often oversimplifies multidimensional aspects or relies on limited features. Conventional econometric methods may overlook important data relationships. Machine learning, particularly boosting algorithms, offers advantages in handling high-dimensional data but remains underutilized for poverty prediction in the Philippines."

**Approach (summary):**
- "Data from 2022 Philippine DHS, originally 2,099 features and 30,372 households, cleaned to 396 features and 20,679 households."
- "Applied five boosting algorithms: AdaBoost, CatBoost, GBM, LightGBM, and XGBoost to classify households into five wealth quintiles."
- "Used SMOTE to handle class imbalance, hyperparameter tuning via grid search and manual trial, and 80/20 train-test split with 10% validation."

**Key Findings (selected):**
- "num: CatBoost achieved highest accuracy at 90.93%, followed by XGBoost (89.41%), GBM (89.05%), and LightGBM (88.52%)."
- "num: AdaBoost had lowest accuracy at 80.39% and significantly lower AUC-ROC scores for poorer classes."
- "num: CatBoost had longest training time (69.29s) but fastest testing (0.01s); AdaBoost fastest training (4.48s) but slowest testing (0.23s)."
- "AUC-ROC scores near 0.99-1.00 for CatBoost, GBM, LightGBM, XGBoost across most wealth classes."

**Limitations / Contradictions for Odin:**
- "Data cleaning removed many features and households, potentially introducing bias."
- "Only five boosting algorithms compared; other ML methods not included."
- "Hyperparameter tuning may not be optimal across all models."

**Key takeaways:**
- "CatBoost achieved 90.93% accuracy for wealth quintile classification."
- "LightGBM and XGBoost balance high accuracy with fast training and small model size."
- "AdaBoost had lowest accuracy (80.39%) and higher misclassification for poorer classes."

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


## Purchasing Intentions Analysis of Hybrid Cars Using Random Forest Classifier and Deep Learning
**Filename:** `LA--Ong-et_al_summarized.md`  
**Authors:** Ong, A.K.S.; Cordova, L.N.Z.; Longanilla, F.A.B.; Caprecho, N.L.; Javier, R.A.V.; Borres, R.D.; German, J.D. (2023)  
**ID:** `10.3390/wevj14080227`  
**Odin Topics:** 5.C, 6.A, 12.B  

**TLDR:** Random forest classifier (94% accuracy) and deep learning neural network (96.6% accuracy) predict Filipino drivers’ hybrid car purchase intentions, with perceived environmental concern and attitude as top factors.

**Problem & Motivation:** Hybrid cars are not widely adopted in the Philippines despite their environmental benefits. Limited studies use machine learning to analyze purchasing intentions for hybrid cars in developing countries. Understanding these intentions can guide automakers and support sustainable transportation goals.

**Approach (summary):**
- Surveyed 1048 Filipino drivers with a driver’s license using convenience and snowball sampling.
- Adapted questionnaire from prior hybrid car intention study with 12 latent variables from PEPB and UTAUT2 frameworks.
- Applied Decision Tree, Random Forest Classifier (RFC), and Deep Learning Neural Network (DLNN) to predict behavioral intention.

**Key Findings (selected):**
- num: Deep learning neural network achieved 96.60% accuracy in predicting behavioral intention.
- num: Random forest classifier achieved 94% accuracy at 90:10 train-test split with Gini and best splitter.
- Perceived environmental concern (PENC) was the most important factor (100% normalized importance), followed by attitude (96.32%) and perceived behavioral control (94.50%).
- Basic decision tree produced much lower accuracy (max 72.32%) due to random tree generation per iteration.

**Limitations / Contradictions for Odin:**
- "Limited constructs from adapted questionnaire; self-administered online survey may introduce response bias. [unacknowledged]"
- "Only drivers with a license and social media presence were sampled, excluding non-digital or non-licensed populations."
- "Only two machine learning algorithms (RFC and DLNN) were used; other algorithms like Naïve Bayes or k-NN were not tested."

**Key takeaways:**
- "Deep learning achieved 96.6% accuracy for predicting purchase intentions."
- "Perceived environmental concern was the most important factor."
- "Random forest classifier reached 94% accuracy with Gini and best splitter."

---


## Predicting the Filipino Household Income Using Naive Bayes Classification Algorithm
**Filename:** `LA--Apus-et_al_summarized.md`  
**Authors:** Apus, J. O.; Mantalaba, K. D. V.; Mackno, A. J. B.; Bokingkito, P. B. Jr. (0)  
**ID:** `a1b2c3d4-e5f6-4789-9a8b-7c6d5e4f3a2b`  
**Odin Topics:** 6.A, 12.B  

**TLDR:** Uses Naive Bayes on FIES data to predict Filipino household income classes, achieving 93% accuracy with bagging ensemble.

**Problem & Motivation:** Poverty reduction requires identifying vulnerable households. Existing studies use socio-demographic variables, but household expenditure and income variables remain unexplored for classification. This gap limits targeted interventions.

**Approach (summary):**
- Data from 2018 FIES with 41,545 instances and 60 features.
- Data cleaning handled missing values using mode for categorical, mean/median for numeric.
- Feature selection used univariate chi-squared test, selecting 13 features with highest scores.

**Key Findings (selected):**
- "num: Bagging ensemble achieved 93% accuracy, precision 0.93, recall 0.94, F1 0.94."
- "num: Boosting ensemble achieved 89% accuracy."
- Poor income class had most true positives; Rich class had fewest due to fewer instances.
- Model with >80% accuracy is considered good per literature.

**Limitations / Contradictions for Odin:**
- "Dataset only covers 2018, not updated annually. [unacknowledged]"
- "Feature independence assumption of Naive Bayes may reduce real-world accuracy. [unacknowledged]"
- "Only two ensemble methods tested; other algorithms not compared."

**Key takeaways:**
- "Naive Bayes with bagging yields 93% accuracy for income classification."
- "Food expenditure is the strongest predictor of income class."
- "Seven income brackets from Poor to Rich are used."

---


## Note for the Agent

The summaries above contain **essential extracts** – enough to understand each paper's relevance to Odin, including supporting evidence and limitations.
If you need additional details not shown here (e.g., **critical citations, definitions, equations, full methodology, or the complete mapping rationale**),
**ask the user to send the original summary file (`<filename>_summarized.md`) or the converted MarkItDown file(`<filename>_marked.md`)** for the specific paper(s) of interest.
Do not invent missing information. Acknowledge gaps when they exist.