# Comprehensive Report for Subtopic: `12.B`

**Total relevant papers:** 63

This report includes problem/motivation, approach, key findings, support for Odin, and limitations/contradictions.

---


## Proteus: Shapeshifting Desktop Visualizations for Mobile via Multi-level Intelligent Adaptation
**Filename:** `I--Liu-et_al_summarized.md`  
**Authors:** Liu, C.; Cheng, S.; Liang, F.; Jiang, Z.; Huang, L.; Athapaththu, K.; Wang, Y. (2026)  
**ID:** `d2b5c3f1-6a7e-4b8c-9d0f-1e2a3b4c5d6e`  
**Odin Topics:** 9.A, 9.B, 12.A, 12.B  

**TLDR:** Proteus is an LLM-driven multi-agent framework that transforms desktop visualizations into mobile-optimized versions using a novel multi-level design space, outperforming a strong baseline in user studies.

**Problem & Motivation:** Desktop visualizations are ill-suited for mobile screens due to different viewport sizes and interaction paradigms. Direct scaling causes illegible text, information loss, and interaction failures. Existing responsive visualization techniques treat adaptation as a flat layout puzzle lacking semantic understanding and hierarchical constraint propagation.

**Approach (summary):**
- The authors propose a multi-level design space with three layers: Global Topology, Reference Frame, and Visual Elements.
- They develop Proteus, a five-agent LLM system (Semantic Parser, Data Extractor, Design Planner, Frontend Engineer, Visual Critic) that iteratively adapts visualizations.
- The system accepts HTML/SVG source code and renders mobile-optimized components using TypeScript and Recharts.

**Key Findings (selected):**
- num: Proteus achieved 91.8% render success rate on 67 visualizations versus 87.8% for the baseline.
- num: Wilcoxon signed-rank tests showed significant improvements for data fidelity and readability (p < 0.05) and for interaction reasonableness and aesthetics (p < 0.001).
- The multi-level design space enables hierarchical constraint propagation from global topology down to individual visual marks.
- The visual critic agent autonomously evaluates and guides iterative refinement, essential for zero-intervention robustness.

**Supports Odin (direct justifications):**
- Mobile adaptation requires semantic re-authoring rather than simple geometric resizing.
- A multi-level design space with hierarchical constraint propagation improves readability and interaction on small screens.
- LLM-based multi-agent systems can automate visualization adaptation with high fidelity and minimal human intervention.

**Limitations / Contradictions for Odin:**
- High latency for complex SVG/HTML inputs due to large token counts.
- Preserving subtle aesthetic qualities of bespoke visualizations remains difficult.
- No task-oriented evaluation of analytic equivalence between desktop and mobile versions. [unacknowledged]

**Key takeaways:**
- Proteus achieves 91.8% render success on 67 diverse visualizations.
- Multi-level design space outperforms flat geometry-centric heuristics.
- LLM agents with a critic loop enable zero-intervention mobile adaptation.

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


## Predicting student retention: A comparative study of machine learning approach utilizing sociodemographic and academic factors
**Filename:** `LA--Delena-et_al_summarized.md`  
**Authors:** Delen˜a, R. D.; Diab, N. J.; Sacayan, R. R.; Sieras, J. C.; Khalid, S. A.; Macatotong, A. H. T.; Gulam, S. B. (2025)  
**ID:** `10.1016/j.sasc.2025.200352`  
**Odin Topics:** 12.A, 12.B  

**TLDR:** A comparative study of ten machine learning algorithms predicts student retention using sociodemographic and academic data from a Philippine university, with XGBoost achieving highest accuracy.

**Problem & Motivation:** Student dropout is a persistent challenge in higher education, especially in developing regions with limited resources for intervention. Traditional approaches based on subjective assessments are insufficient to capture attrition complexity. There is a need for accurate predictive models using machine learning on institutional data.

**Approach (summary):**
- Data from Mindanao State University (482 students, 146 variables over 2012–2022) was preprocessed using CRISP-DM and Power BI.
- Ten algorithms were evaluated: XGBoost, Gradient Boosting, ANN, Decision Tree, Random Forest, MLP, Logistic Regression, KNN, SVM, and Naïve Bayes.
- Models were assessed with train-test split and 5-fold cross-validation using accuracy, precision, recall, F1, MSE, and log loss.

**Key Findings (selected):**
- num: XGBoost achieved 90.66% cross-validated accuracy and 90.72 F1 score, outperforming all other models.
- num: Gradient Boosting had 89.42% accuracy and the lowest log loss (0.25), while ANN reached 88.39% accuracy and 91.48% recall.
- Naïve Bayes had high recall (97.21%) but excessive false positives (31), limiting practical use.
- Decision Tree overfitted, dropping from 90.34% to 84.44% accuracy after cross-validation.

**Supports Odin (direct justifications):**
- XGBoost achieves higher accuracy (90.66%) than other models on imbalanced tabular data.
- Cross-validation is necessary to avoid overestimation of model performance from single train-test splits.
- Ensemble methods like Gradient Boosting produce more stable generalization than single decision trees.

**Limitations / Contradictions for Odin:**
- Data sourced from a single institution may limit external validity.
- Behavioral and psychosocial dimensions (e.g., LMS engagement, motivation) were not included.
- Model interpretability remains a challenge for deployment in education and finance.

**Key takeaways:**
- XGBoost achieved 90.66% cross-validated accuracy for dropout prediction.
- Ensemble models like Gradient Boosting consistently outperform single classifiers.
- Cross-validation is essential to avoid overfitting in educational data mining.

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
- num: Random forest with ensemble feature selection achieved 99.6% accuracy and 100% precision in credit card fraud detection.
- num: XGBoost consistently outperformed deep neural networks across 10 credit scoring datasets, achieving highest AUC and efficiency.
- num: CNN reduced fraud detection cost of failure by 30% and achieved 87.64% AUC on European dataset.
- num: GCN achieved 94.5% fraud detection accuracy, outperforming CNN (93%) by improving recall by 10% via graph-based user relationship analysis.

**Supports Odin (direct justifications):**
- Random forest with ensemble feature selection achieves 99.6% accuracy for fraud detection, suitable for Odin anomaly detection.
- LSTM improves expense forecasting accuracy by 30% over traditional regression models.
- AI personalization increases user engagement by 27% and retention by 15% in personal finance apps.

**Limitations / Contradictions for Odin:**
- Review primarily cites papers up to 2024; rapid ML/DL advances may render some comparisons outdated. [unacknowledged]
- Performance metrics are aggregated across heterogeneous datasets, making direct apples-to-apples comparisons difficult. [unacknowledged]
- The review does not address computational resource constraints of mobile-first deployment, which is critical for Odin. [unacknowledged]

**Key takeaways:**
- XGBoost outperforms deep learning for credit scoring across 10 datasets.
- Random forest achieves 99.6% fraud detection accuracy with feature selection.
- AI personalization lifts user engagement by 27% and retention by 15%.

---


## Foundations and Innovations in Data Fusion and Ensemble Learning for Effective Consensus
**Filename:** `IA--Du-et_al_summarized.md`  
**Authors:** Du, K.-L.; Zhang, R.; Jiang, B.; Zeng, J.; Lu, J. (2025)  
**ID:** `10.3390/math13040587`  
**Odin Topics:** 3.A, 5.C, 6.A, 6.B, 8.A, 8.B, 12.B  

**TLDR:** Surveys ensemble learning methods including bagging, boosting, random forests, and data fusion, analyzing bias‑variance trade‑offs, margin theory, and computational complexities.

**Problem & Motivation:** No single machine learning method universally outperforms others across all problem domains. Ensemble learning combines multiple models to improve predictive accuracy, robustness, and generalization. This survey addresses the need for a structured understanding of ensemble techniques and their theoretical foundations.

**Approach (summary):**
- Comprehensive literature review of ensemble learning and data fusion techniques.
- Covers bagging, boosting, random forests, stacking, and cascading methods.
- Includes advanced topics: multiclass classification, error‑correcting output codes, Dempster‑Shafer theory, multiple kernel learning, and multiview learning.

**Key Findings (selected):**
- Bagging reduces variance and improves stability, especially for high‑variance models like decision trees.
- Boosting reduces bias by sequentially focusing on misclassified instances but can overfit noisy data.
- Random forests consistently outperform most methods in predictive accuracy and handle missing data effectively.
- The C‑bound provides a more accurate risk indicator for majority voting than the Gibbs classifier's risk.

**Supports Odin (direct justifications):**
- Bagging reduces variance and improves stability for high‑variance models like decision trees.
- Boosting can convert weak learners into strong ones by focusing on misclassified instances.
- Random forests consistently outperform most methods in predictive accuracy and handle missing data effectively.

**Limitations / Contradictions for Odin:**
- Ensemble methods increase computational complexity and storage requirements [acknowledged].
- Dempster’s rule can produce counterintuitive results under high evidence conflict [acknowledged].
- Boosting tends to overfit noisy datasets [acknowledged].

**Key takeaways:**
- Bagging reduces variance by averaging models trained on bootstrap samples.
- Boosting sequentially focuses on misclassified instances to reduce bias.
- Random forests achieve high accuracy and handle missing data effectively.

---


## MACHINE LEARNING TIME SERIES FORECASTING: A COMPREHENSIVE SURVEY AND STOCK MARKET APPLICATION
**Filename:** `IA--Hall_summarized.md`  
**Authors:** Hall, T. (2025)  
**ID:** `d1e2f3a4-b5c6-47d8-9e0f-1a2b3c4d5e6f`  
**Odin Topics:** 6.B, 12.A, 12.B  

**TLDR:** A survey and application demonstrate that LightGBM and recurrent neural networks excel in time series forecasting, with LightGBM offering computational efficiency and a day trading model achieving daily returns 500 times higher than human traders.

**Problem & Motivation:** Existing time series surveys cannot compare models fairly because each study uses different datasets and implementations. Day trading poses exceptional difficulty for human traders due to cognitive biases and slow reaction times. No prior work has applied a unified ML framework to second-by-second trading across all US equities with realistic execution constraints.

**Approach (summary):**
- Survey identified 79 papers from Web of Science (2017-2024) that compare at least one tree-based and one deep learning model under identical experimental conditions.
- Application used two years of second-by-second trade and quote data for all US equities, engineered multi-timeframe technical indicators and stock attributes.
- LightGBM models estimated risk-reward ratios over multiple forward horizons with min-max regularized target and equal weighting.

**Key Findings (selected):**
- num: LightGBM and LSTM/GRU consistently outperform other architectures across time series tasks.
- num: Tree-based methods show a significant computational efficiency advantage over deep learning, often training 10-100x faster.
- num: The best ML day trading model achieved average daily profit of 20,000 basis points with a Sharpe ratio of 15.78 across 999 trades per day.
- num: ML daily returns were more than 500 times higher than top human day traders.

**Supports Odin (direct justifications):**
- LightGBM outperforms deep learning models in computational efficiency for time series forecasting.
- Combining multiple models and diverse features improves forecasting accuracy over any single model.
- High-frequency second-by-second data enables more accurate short-term financial predictions.

**Limitations / Contradictions for Odin:**
- The survey's citation-based selection may bias results toward older, highly cited papers [unacknowledged].
- The day trading model was not tested on out-of-sample periods beyond the two-year window [unacknowledged].
- Human trader benchmark comparisons are approximate, not controlled head-to-head [unacknowledged].

**Key takeaways:**
- LightGBM and LSTM are top performers for time series forecasting.
- Tree-based methods offer major computational speed advantages over deep learning.
- ML day trading model achieved 20,000 bps average daily profit.

---


## Review of Methods and Models for Forecasting Electricity Consumption
**Filename:** `IA--Misiurek-et_al_summarized.md`  
**Authors:** Misiurek, K.; Olkuski, T.; Zysk, J. (2025)  
**ID:** `10.3390/en18154032`  
**Odin Topics:** 6.A, 6.B, 12.A, 12.B  

**TLDR:** A comprehensive review of electricity consumption forecasting methods across four time horizons, comparing classical statistical models with modern machine learning and deep learning techniques.

**Problem & Motivation:** Accurate electricity forecasting is critical for balancing supply and demand, integrating renewable energy, and modernizing grids. Inaccurate forecasts cause significant economic losses, with a 1% increase in error costing an additional USD 10 million annually. Existing methods range from classical ARIMA to advanced deep learning, but no universal approach exists.

**Approach (summary):**
- Reviewed over 100 studies on electricity load forecasting published up to 2024, with emphasis on works from the last 5 years.
- Categorized forecasting horizons into very short-term (30 min), short-term (day to weeks), medium-term (months to years), and long-term (decades).
- Compared classical statistical methods (ARIMA, SARIMA, Holt-Winters, linear regression) against machine learning (ANN, Random Forest) and deep learning (LSTM, CNN-LSTM, Transformer).

**Key Findings (selected):**
- num: LSTM model achieved RMSE improvement of approximately 10-15% over traditional machine learning models in aggregated household forecasting.
- num: Transformer with sparse attention achieved inference up to 5 times faster than RNN methods while maintaining comparable accuracy (sMAPE ≈ 0.18 for 1-day forecast).
- num: ARIMA model outperformed regression (8.1% MAPE) and ANN (5.6% MAPE) with 3.8% MAPE for monthly electricity consumption in Saudi Arabia.
- num: Hybrid SARIMA-ANN model (Khashei & Bijari) achieved lowest RMSE of 0.0792 compared to SARIMA alone at 0.0823 for Turkish electricity.

**Supports Odin (direct justifications):**
- LSTM networks effectively learn complex temporal dependencies and can significantly improve forecasting accuracy over classical methods.
- Hybrid models combining statistical and machine learning outperform single models when linear and nonlinear structures cannot be separated.
- No single universal forecasting method exists; algorithm selection must match data characteristics and forecast horizon.

**Limitations / Contradictions for Odin:**
- Review does not provide original empirical validation; all metrics are cited from primary studies.
- External variables (temperature, GDP) used in models are difficult to predict ex ante for operational forecasting.
- Electricity consumption patterns differ from personal spending; direct transferability to PFMS requires adaptation and validation.

**Key takeaways:**
- LSTM models improve forecasting RMSE by 10-15% over traditional methods.
- Transformer models achieve 5x faster inference than RNNs with comparable accuracy.
- No single universal forecasting method exists for all time horizons.

---


## ARTIFICIAL INTELLIGENCE-DRIVEN PERSONAL FINANCE SOLUTION
**Filename:** `IA--Bashshar-et_al_summarized.md`  
**Authors:** Bashshar, S. A.; Imran, M.; Kumar, P. S.; Goud, E. S.; Venunath, M.; Prasad, M. L. M. (2025)  
**ID:** `a2b8c9d0-e1f2-34a5-b678-90c1d2e3f4a5`  
**Odin Topics:** 3.A, 3.B, 6.A, 6.B, 12.A, 12.B  

**TLDR:** An AI-powered personal finance assistant uses NLP for transaction categorization and ARIMA for expense forecasting, achieving 86% categorization accuracy and MAE of 253.47.

**Problem & Motivation:** Manual tracking fails to provide real-time insights and predictive capabilities, leading to poor budgeting and low savings. Digital payments increase transaction volume, making it hard for individuals to understand spending habits. Existing systems lack automation and forecasting.

**Approach (summary):**
- Data is collected from user-uploaded CSV files containing transaction date, description, amount, and type.
- Preprocessing removes extraneous characters, normalizes fields, and applies tokenization, stopword removal, and lemmatization using NLTK.
- Transaction categorization uses keyword matching against domain-specific dictionaries without manual labeling.

**Key Findings (selected):**
- num: Categorization accuracy of 86.2% with precision 0.88, recall 0.85, F1-score 0.86.
- num: Forecasting MAE of 253.47 and RMSE of 318.91 over 30-day horizon.
- System captures seasonal spending patterns and main spending variations.
- User feedback from ten participants was mostly positive on interface intuitiveness and clarity.

**Supports Odin (direct justifications):**
- NLP with keyword matching achieves 86.2% accuracy for transaction categorization.
- ARIMA model can forecast 30-day expenses with MAE 253.47.
- Automated categorization reduces manual effort and improves financial awareness.

**Limitations / Contradictions for Odin:**
- Small sample size for user feedback (n=10) [unacknowledged]
- Categorization depends on static keyword dictionaries, may not generalize to new transaction types.
- No comparison with deep learning baselines for forecasting [unacknowledged]

**Key takeaways:**
- NLP categorization achieved 86.2% accuracy on real transaction data.
- ARIMA forecasting produced MAE of 253.47 for 30-day expenses.
- Automated expense tracking reduces manual errors and improves awareness.

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


## Deep learning-based time series forecasting
**Filename:** `IA--Song-et_al_summarized.md`  
**Authors:** Song, X.; Deng, L.; Wang, H.; Zhang, Y.; He, Y.; Cao, W. (2025)  
**ID:** `10.1007/s10462-024-10989-8`  
**Odin Topics:** 6.A, 6.B, 8.A, 8.B, 12.A, 12.B  

**TLDR:** A comprehensive review of deep learning-based time series forecasting models from 2014 to 2024, examining their ability to capture temporal dependencies and variable correlations, long-term forecasting optimizations, and loss functions.

**Problem & Motivation:** Traditional time series models like ARIMA fail to capture complex nonlinear correlations and long-term dependencies in real-world data. Deep learning offers potential but the field has rapidly expanded with many architectures. This survey systematically organizes the progress to guide researchers and practitioners.

**Approach (summary):**
- Reviews models from 2014-2024 including RNNs, LSTMs, GRUs, CNNs, TCNs, Transformers, and decomposition-based methods.
- Evaluates models on ETT, Electricity, Exchange, Traffic, and ILI datasets with input lengths 36-192 and output horizons 12-336.
- Uses MAE, MSE, MAPE, and R2 metrics with simple time split and sliding window validation.

**Key Findings (selected):**
- num: DLinear, a simple linear model, often outperforms complex Transformers, reducing MSE by up to 27.30% on ILI dataset compared to NS-Transformer.
- num: PatchTST’s patch attention improves MSE by 85.27% on Exchange dataset over vanilla attention.
- num: Shuffling input sequence degrades DLinear and PatchTST by 93-1092% in MSE, while complex models like TDformer improve, indicating poor use of sequential order.
- num: Fedformer achieves best trend and season prediction on artificial data, with MAE improvements of 26.65% (season) and 3.14% (trend) over second-best.

**Supports Odin (direct justifications):**
- DLinear, a simple linear model, often outperforms complex Transformers on time series forecasting tasks.
- Patch-based attention (PatchTST) significantly reduces memory usage while improving accuracy.
- Frequency-domain seasonal extraction outperforms time-domain methods for periodic spending patterns.

**Limitations / Contradictions for Odin:**
- Survey does not propose a novel algorithm; it synthesizes existing work. [unacknowledged]
- All experiments use public datasets (energy, traffic, exchange rates), not personal finance data. [unacknowledged]
- Does not consider real-time or streaming forecasting scenarios common in PFMS. [unacknowledged]

**Key takeaways:**
- Simple linear models (DLinear) often beat complex Transformers on forecasting accuracy.
- Patch-based attention reduces memory by 10.93% while improving MSE by 85.27% on exchange data.
- Frequency-domain methods extract seasonal spending patterns more accurately than time-domain.

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


## Predict, Optimize, Deliver: Demand Forecasting and Resource Optimization for a Market Research Firm
**Filename:** `LA--Mariano-&-Monreal_summarized.md`  
**Authors:** Mariano, M. T. G.; Monreal, R. N. (2025)  
**ID:** `10.1145/3785171.3785187`  
**Odin Topics:** 6.A, 6.B, 12.A, 12.B  

**TLDR:** Compares ARIMA, Holt-Winters, Prophet, and LSTM for demand forecasting and integrates with Pyomo-based optimization for workforce allocation in a market research firm, with Prophet achieving best balance of accuracy and usability.

**Problem & Motivation:** Professional service firms face demand uncertainty and inefficient manual workforce planning. Existing forecasting-optimization frameworks target product-based contexts, not time-sensitive service environments with high variance. There is a need for an integrated, interpretable pipeline that connects demand forecasting, resource optimization, and visualization.

**Approach (summary):**
- Historical time-tracking data from January 2018 to December 2024 (billable hours) for two clients.
- Compared ARIMA, Holt-Winters Exponential Smoothing, Prophet, and LSTM using MAE, RMSE, and MAPE across multiple train-test splits and a 30-day holdout.
- Weighted error score (0.35 MAE + 0.35 RMSE + 0.30 MAPE) plus interpretability and speed (0.25 each) for model selection.

**Key Findings (selected):**
- Prophet achieved the lowest weighted error for Client1 (13.038) and Client2 (27.786), and the best overall score (10.456) after including interpretability and speed.
- LSTM showed stable performance across training splits but higher complexity and data requirements reduced practical viability.
- ARIMA and Holt-Winters performed worse under noisy, volatile demand patterns.
- num: The optimization model achieved near-zero unmet demand under baseline and RMSE-adjusted scenarios, with occasional overutilization (e.g., 106% for shared resource S2).

**Supports Odin (direct justifications):**
- Prophet offers a robust balance between forecast accuracy and interpretability for short-term planning horizons.
- LSTM maintains stable performance across training sizes but requires more data and computational resources.
- Incorporating prediction intervals from RMSE into optimization improves allocation precision under demand uncertainty.

**Limitations / Contradictions for Odin:**
- Analysis restricted to output-based variables; input-level factors like individual analyst skill were unavailable.
- Forecasting model uses internal historical data only and does not incorporate external economic indicators.
- Long-range forecasting caution: rare high-impact events (e.g., COVID-19 pandemic) not considered.

**Key takeaways:**
- Prophet achieved the lowest weighted error score of 10.456.
- Forecast uncertainty bands from RMSE improve resource allocation resilience.
- The predict-then-optimize framework bridges predictive analytics and operational planning.

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


## Expense tracker management system using machine learning
**Filename:** `IA--Thakur-&-Jadhav_summarized.md`  
**Authors:** Thakur, R. S.; Jadhav, A. (2025)  
**ID:** `10.14744/sigma.2025.00119`  
**Odin Topics:** 6.A, 6.B, 12.A, 12.B  

**TLDR:** Predicts future expenses using machine learning on household transaction data, finding a voting ensemble regressor achieves 78.11% R-squared.

**Problem & Motivation:** Manual expense tracking is time-consuming and error-prone, while existing apps lack predictive capabilities. There is a need for automated expense prediction to help users manage budgets. This paper addresses the gap by applying machine learning to forecast expenses from past spending patterns.

**Approach (summary):**
- {'Dataset': 'Daily Household Transactions (date, mode, category, subcategory, note, amount, income/expense, currency).'}
- {'Preprocessing': 'MinMax scaling, log1p transformation of amount, TF-IDF vectorization of text fields (min_df=3).'}
- {'Models': 'Individual (XGBoost, Random Forest, SVM, MLP, KNN, Decision Tree, Extra Tree, CatBoost) and ensemble (bagging, boosting, stacking, voting, blending).'}

**Key Findings (selected):**
- {'num': 'XGBoost achieves R-squared of 77.89%, highest among individual models.'}
- {'num': 'Voting ensemble regressor achieves highest R-squared of 78.11% and lowest relative absolute error of 0.1765.'}
- Voting ensemble outperforms bagging, boosting, stacking, and blending.
- RAE is the deciding factor due to similar R2 values across models.

**Supports Odin (direct justifications):**
- Voting ensemble regressor outperforms individual models for expense prediction on household transaction data.
- XGBoost achieves 77.89% R-squared for expense forecasting, second only to voting ensemble.
- Relative absolute error of 0.1765 is the lowest among all tested models.

**Limitations / Contradictions for Odin:**
- Manual data entry required, no automatic transaction fetching. [acknowledged]
- Limited to expense prediction; does not provide budget recommendations. [unacknowledged]
- R2 values around 78% leave substantial unexplained variance. [unacknowledged]

**Key takeaways:**
- Voting ensemble regressor achieves 78.11% R-squared for expense prediction.
- XGBoost outperforms other individual models with 77.89% R2.
- Manual expense entry remains a limitation of the system.

---


## Dynamic Model for Budget Allocation in via Multi-Criteria Optimization
**Filename:** `IA--Gulbakyt-et_al_summarized.md`  
**Authors:** Gulbakyt, S.; Almaz, A.; Saule, S.; Suhrab, Y. (2025)  
**ID:** `10.47738/jads.v6i4.935`  
**Odin Topics:** 7.A, 7.B, 7.C, 12.A, 12.B  

**TLDR:** A dynamic multi-criteria optimization framework allocates a constrained regional budget across seven activity areas using SQP and genetic algorithms, achieving fair distribution with a Gini coefficient of 0.223.

**Problem & Motivation:** Regional budget allocation by local councils in Kazakhstan suffers from opacity, insufficient public involvement, and lack of data-driven tools. Socioeconomic disparities and declining public trust demand a transparent, equitable, and efficient allocation method that balances citizen satisfaction, strategic priorities, basic needs, and urbanization.

**Approach (summary):**
- Data from four districts in Almaty region: population, income, urbanization coefficients, and synthetically generated citizen votes.
- Objective function maximizes weighted sum of four criteria: citizen satisfaction (0.2), strategic priorities (0.2), basic needs fulfillment (0.3), and urbanization level (0.3).
- Quadratic programming with Sequential Quadratic Programming (SQP) implemented in MATLAB fmincon solver.

**Key Findings (selected):**
- SQP converged in under 100 iterations to objective value 18,519,864.85 thousand tenge.
- GA achieved objective value 18,520,000.00 thousand tenge after 500 generations.
- num: The difference between methods is 135.15 thousand tenge (0.0007% of total budget).
- Healthcare (22.05%) and transport (21.11%) received largest allocations; education smallest (7.03%).

**Supports Odin (direct justifications):**
- Multi-criteria optimization can balance user satisfaction, savings goals, and spending necessities in personal budget allocation.
- SQP provides fast convergence for well-defined budget constraints, suitable for real-time recommendations.
- Genetic algorithms offer robustness against local optima when user preferences are uncertain or conflicting.

**Limitations / Contradictions for Odin:**
- Synthetic citizen voting data reduces external validity. [unacknowledged]
- Weight coefficients lack systematic sensitivity analysis or stakeholder validation. [unacknowledged]
- Constraint violation persists at convergence (0.47% of budget), though authors acknowledge it as a trade-off.

**Key takeaways:**
- SQP and GA achieved nearly identical optimal budget allocations, differing by only 0.0007%.
- Healthcare and transport received the largest shares (22% and 21%) due to strategic weight.
- Gini coefficient of 0.223 indicates fair distribution across seven activity areas.

---


## Artificial Intelligence vs. Efficient Markets: A Critical Reassessment of Predictive Models in the Big Data Era
**Filename:** `IA--Pagliaro_summarized.md`  
**Authors:** Pagliaro, A. (2025)  
**ID:** `10.3390/electronics14091721`  
**Odin Topics:** 6.A, 10.A, 12.A, 12.B  

**TLDR:** Critically reassesses AI stock market prediction models, finding ensemble methods achieve up to 86% directional accuracy but statistical significance often fails to translate into economic value after transaction costs.

**Problem & Motivation:** Existing reviews focus on taxonomic classification without rigorous cross-regime evaluation or reconciling statistical significance with economic relevance. The gap between theoretical market efficiency and empirical predictability remains inadequately addressed.

**Approach (summary):**
- Synthesizes over 100 studies on stock market prediction from 1988 to 2024 across statistical, machine learning, and deep learning methods.
- Evaluates model performance using both classification metrics (accuracy, precision) and financial metrics (Sharpe ratio, returns after transaction costs).
- Develops a comprehensive evaluation framework incorporating statistical significance, economic relevance, robustness across regimes, and implementation feasibility.

**Key Findings (selected):**
- num: ExtraTreesClassifier achieves 86.1% directional accuracy for 10-day S&P500 predictions, outperforming RandomForest at 73%.
- num: LSTM networks achieve 53.2% directional accuracy with Sharpe ratio 0.77 after transaction costs.
- num: RandomForest achieves 91.27% accuracy on NASDAQ100 using 15-minute intervals.
- num: Models showing statistical significance (p<0.05) often fail to generate economic value; 60-80% of published anomalies fail to replicate under stringent tests.

**Supports Odin (direct justifications):**
- Ensemble methods consistently outperform single classifiers in financial prediction tasks across multiple studies.
- Statistical significance (p<0.05) alone is insufficient; economic relevance after transaction costs is required.
- Models must be evaluated across different market regimes to ensure robustness and generalizability.

**Limitations / Contradictions for Odin:**
- High risk of backtest overfitting due to complex models and numerous hyperparameters.
- Standard k-fold cross-validation fails for financial time series; purged cross-validation required but often omitted. [unacknowledged]
- Publication bias toward positive results leads to overoptimistic performance claims in literature.

**Key takeaways:**
- Ensemble methods achieve up to 86% directional accuracy in financial prediction.
- Statistical significance does not guarantee economic value after transaction costs.
- Evaluation must include out-of-sample testing across different market regimes.

---


## Time-Series Forecasting Using Deep Learning and Data Mining Models
**Filename:** `IA--Scrivano_summarized.md`  
**Authors:** Scrivano, A. (2025)  
**ID:** `c3d5e7f9-1a2b-3c4d-5e6f-7a8b9c0d1e2f`  
**Odin Topics:** 6.B, 8.B, 12.B  

**TLDR:** A review comparing traditional statistical, deep learning (RNN, LSTM, CNN, Transformer), and data mining models for time-series forecasting, finding Transformers and Gradient Boosting Machines achieve superior accuracy across finance, energy, and retail domains.

**Problem & Motivation:** Traditional time-series models like ARIMA fail to capture non-linear dynamics and complex patterns in real-world data. Deep learning and data mining methods offer improved accuracy but require systematic evaluation across domains. This review synthesizes current methodologies to guide model selection.

**Approach (summary):**
- Data collected from stock exchanges, meteorological records, smart grids, and retail transactions.
- Preprocessing included differencing, smoothing, log transforms, feature extraction (lagged variables, moving averages), and normalization.
- {'Model selection based on task': 'RNN/LSTM for temporal dependencies, CNN/TCN for spatial hierarchies, Transformers for attention-based long-range dependencies.'}

**Key Findings (selected):**
- num: LSTM achieved 15% reduction in MAE over conventional methods in web traffic prediction.
- num: TCN attained 20% higher accuracy in early-stage anomaly detection compared to traditional methods.
- num: Transformer reduced MSE by 12% and MAE by 17% over recurrent and convolutional models in retail.
- num: Gradient Boosting Machine outperformed Random Forest with MAE of 170 vs 185 in energy dataset.

**Supports Odin (direct justifications):**
- Transformers reduce forecast error by 12-17% compared to recurrent models in retail data.
- Gradient Boosting Machines achieve MAE of 170 on energy data, outperforming Random Forest.
- TCNs provide 20% higher early-stage anomaly detection accuracy than traditional methods.

**Limitations / Contradictions for Odin:**
- The review lacks specific guidance for personal finance domains; results are from aggregate datasets not individual-level transactions.
- Computational constraints of Transformers may limit deployment on mobile devices [unacknowledged].
- Generalizability to Filipino financial behaviors and spending patterns is untested [unacknowledged].

**Key takeaways:**
- Transformers achieve 12-17% lower forecast errors than recurrent models.
- Gradient Boosting Machines offer strong accuracy with lower computational cost.
- Probabilistic forecasting quantifies uncertainty essential for risk-aware decisions.

---


## A Review of Time Series Prediction Models Based on Deep Learning
**Filename:** `IA--Ao-et_al_summarized.md`  
**Authors:** Ao, X.; Gong, Y.; He, A. (2025)  
**ID:** `10.1109/ACCESS.2025.3602791`  
**Odin Topics:** 6.A, 6.B, 8.A, 8.B, 12.A, 12.B  

**TLDR:** Reviews deep learning models for time series prediction, including CNNs, RNNs/LSTM/GRU, Transformers, GNNs, and hybrids, with a task-driven model selection framework.

**Problem & Motivation:** Traditional time series methods like ARIMA struggle with nonlinear, non-stationary, and seasonal real-world data. Deep learning offers powerful nonlinear modeling and automatic feature extraction, but existing surveys lack practical model selection guidelines, deep cross-comparisons, and systematic coverage of emerging challenges like interpretability and efficiency.

**Approach (summary):**
- Systematically analyzes CNN-based models (TCN, SCINet, Kmeans-CNN) and their trade-offs in long-range dependency capture versus computational cost.
- Reviews RNN family (vanilla RNN, LSTM, GRU) focusing on gating mechanisms that solve vanishing gradients for long sequences.
- Examines Transformer variants (Informer, Autoformer, iTransformer, Conformer, Scaleformer, CrossFormer) with emphasis on self-attention complexity and efficiency innovations.

**Key Findings (selected):**
- {'num': 'ARIMA-RNN hybrid achieved 15% MAE reduction on electricity load dataset compared to standalone models.'}
- {'num': 'ETSformer reduced inference latency by 37% versus Autoformer on ETT data while maintaining accuracy.'}
- {'num': 'PatchTST achieved 23% lower MSE than Informer with 60% less GPU memory consumption.'}
- Transformer variants with ProbSparse attention (Informer) reduce time complexity from O(L^2) to O(L log L).

**Supports Odin (direct justifications):**
- LSTM and GRU are suitable for long-sequence prediction tasks such as power load forecasting.
- Gated Recurrent Units offer lower computational cost than LSTM with comparable performance.
- Transformer variants like Informer achieve O(L log L) complexity for efficient long-sequence processing.

**Limitations / Contradictions for Odin:**
- The paper is a survey, not an empirical study; claims about model performance are aggregated from cited primary research.
- Comparative tables lack statistical significance testing across different datasets. [unacknowledged]
- Real-time performance metrics are discussed qualitatively without standardized benchmarks. [unacknowledged]

**Key takeaways:**
- LSTM and GRU solve vanishing gradients for medium-length sequence forecasting.
- Transformer variants achieve O(L log L) complexity for sequences over 1000 steps.
- PatchTST reduces GPU memory by 60% via sub-series tokenization.

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


## A Predictive Framework for Annual Financial Planning using Deep Learning Models
**Filename:** `IA--Singh-et_al_summarized.md`  
**Authors:** Singh, U.; Anand, U.; Singh, V. (2025)  
**ID:** `5e8f3a2b-1c4d-4e5f-8a9b-0c1d2e3f4a5b`  
**Odin Topics:** 6.A, 6.B, 12.A, 12.B  

**TLDR:** A deep learning framework using LSTM and GRU networks accurately forecasts annual expenses, outperforming traditional statistical methods like ARIMA and linear regression.

**Problem & Motivation:** Traditional forecasting methods (linear regression, ARIMA) fail to capture non-linear and dynamic patterns in financial data, limiting accuracy for long-term annual planning. Deep learning offers potential but lacks comprehensive evaluation for annual expense forecasting. This gap hinders proactive fiscal decision-making.

**Approach (summary):**
- Data from public government expenditure portals and synthetic augmentation using Gaussian/exponential distributions.
- Preprocessing: forward-fill missing values, min-max normalization, sliding window of 12 months to create sequences.
- Models: RNN baseline, LSTM, and GRU implemented in TensorFlow/Keras with grid search for hyperparameters.

**Key Findings (selected):**
- num: LSTM achieved MAE 1872.56, RMSE 2614.32, and MAPE 7.02%, the lowest among all models.
- num: GRU performed slightly worse with MAE 1950.45 and MAPE 7.48%, still outperforming RNN.
- num: RNN had MAE 2450.13 and MAPE 9.85%, showing gradient vanishing issues.
- Deep learning models capture long-term dependencies and seasonal variations better than ARIMA and linear regression.

**Supports Odin (direct justifications):**
- LSTM achieves 7.02% MAPE for annual expense forecasting, outperforming GRU and RNN.
- Deep learning models capture long-term dependencies and seasonal patterns better than ARIMA.
- Sliding window of 12 months is effective for annual expense prediction.

**Limitations / Contradictions for Odin:**
- Dependency on high-quality, complete datasets; incomplete or noisy data may hinder performance. [unacknowledged]
- Performance may vary with different time horizons (e.g., monthly or quarterly). [unacknowledged]
- Models could be sensitive to overfitting on smaller datasets if not carefully tuned.

**Key takeaways:**
- LSTM forecasts annual expenses with 7.02% MAPE, beating GRU and RNN.
- Deep learning outperforms ARIMA and linear regression for non-linear financial patterns.
- Sliding window of 12 months effectively captures seasonal spending cycles.

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


## Evolution of Machine Learning: A Foundation for Intelligent Systems
**Filename:** `IA--Gouni_summarized.md`  
**Authors:** Gouni, M. (2025)  
**ID:** `10.32996/jcsts.2025.7.5.74`  
**Odin Topics:** 8.A, 8.B, 12.A, 12.B, 10.A  

**TLDR:** Machine learning techniques from supervised to deep learning enable adaptive credit card fraud detection by identifying patterns and anomalies, reducing false positives compared to rule-based systems.

**Problem & Motivation:** Traditional rule-based fraud detection systems are static, require constant manual updates, and fail against evolving fraud tactics, leading to high false positives and financial losses. Machine learning offers adaptive, proactive detection capabilities that learn from transaction data without explicit reprogramming.

**Approach (summary):**
- Reviews supervised learning models including logistic regression, decision trees, random forests, gradient boosting, and deep neural networks for fraud classification.
- Examines unsupervised techniques such as k-means clustering, DBSCAN, spectral clustering, and autoencoders for detecting novel fraud patterns without labeled data.
- Analyzes deep learning architectures including RNNs, LSTMs, GRUs, and CNNs for sequential and spatial pattern recognition in transaction monitoring.

**Key Findings (selected):**
- num: Deep learning models significantly outperform traditional methods in detecting sophisticated fraud patterns across multiple studies.
- num: Ensemble methods and advanced neural approaches consistently outperform single-classifier methods on imbalanced fraud datasets.
- Unsupervised autoencoders capture complex non-linear relationships to identify anomalies that distance-based clustering methods miss.
- Sequential models (RNN/LSTM) excel at detecting card-not-present fraud by analyzing transaction sequences rather than isolated events.

**Supports Odin (direct justifications):**
- Machine learning models dynamically learn from transaction data, adapting to new fraud patterns without manual rule updates.
- Unsupervised autoencoders detect anomalies based on reconstruction error, useful for unknown pattern detection in spending behavior.
- Ensemble methods like random forests reduce false positives compared to single classifiers in imbalanced datasets.

**Limitations / Contradictions for Odin:**
- Survey lacks empirical comparison of specific algorithms on a common benchmark dataset.
- Does not address computational cost of deep learning in real-time mobile environments [unacknowledged].
- Focus on credit card fraud rather than general expense anomaly detection for personal finance management.

**Key takeaways:**
- Ensemble models outperform single classifiers in imbalanced fraud data.
- Autoencoders detect non-linear anomalies missed by clustering methods.
- Federated learning enables privacy-preserving collaborative model training.

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


## A Constrained, Data-Driven Budgeting Framework Integrating Macro Demand Forecasting and Marketing Response Modeling
**Filename:** `IA--Lu-et_al_summarized.md`  
**Authors:** Lu, Y.; Zhou, H.; Zhang, Y. (2025)  
**ID:** `10.51903/jtie.v4i3.466`  
**Odin Topics:** 6.A, 6.B, 7.A, 7.B, 7.C, 12.B  

**TLDR:** Integrates macro demand forecasting, marketing response with diminishing returns, and accounting constraints into a budget optimization framework under uncertainty.

**Problem & Motivation:** Budgeting must combine macroeconomic signals, channel-level marketing effectiveness, and hard accounting constraints. Existing approaches treat these components separately and ignore uncertainty, leading to suboptimal or constraint-violating allocations.

**Approach (summary):**
- Uses quarterly PCE components (durable, nondurable, services) from FRED as macro demand proxy.
- Compares seasonal naïve, SARIMAX, gradient boosting, and VAR in rolling backtest (2018Q1-2025Q3).
- Estimates marketing response from Advertising dataset (TV, radio, newspaper) using OLS, ridge, lasso, GBR, and Hill saturation model.

**Key Findings (selected):**
- {'num': 'Multivariate VAR improves aggregate demand accuracy with ≈2.85% MAPE.'}
- {'num': 'Newspaper spend has near-zero marginal ROI; radio saturates quickly, TV saturates slowly.'}
- Optimal marketing spend lies below the SG&A ratio cap due to diminishing returns.
- {'num': 'Spending at the deterministic cap yields ≈40% violation probability under demand uncertainty.'}

**Supports Odin (direct justifications):**
- Optimal budgets may be below ratio caps due to diminishing returns.
- Spending at a deterministic cap yields 40% violation probability under demand uncertainty.
- Multivariate forecasting improves aggregate demand accuracy over univariate baselines.

**Limitations / Contradictions for Odin:**
- Macro PCE and Advertising datasets are not internally consistent; response-to-dollar normalization is arbitrary. [acknowledged]
- No adstock or carryover effects in marketing response, limiting dynamic budgeting. [acknowledged]
- Constraint calibration uses a single firm (Apple); results may not transfer to other sectors. [acknowledged]

**Key takeaways:**
- Optimal budgets often sit below ratio caps due to diminishing returns.
- VAR forecasting achieved 2.85% MAPE for aggregate demand proxy.
- Newspaper spend showed near-zero marginal ROI in the Advertising dataset.

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


## A Survey of Machine Learning Methods for Time Series Prediction
**Filename:** `IA--Hall-&-Rasheed_summarized.md`  
**Authors:** Hall, T.; Rasheed, K. (2025)  
**ID:** `10.3390/app15115957`  
**Odin Topics:** 6.A, 6.B, 8.A, 8.B, 12.A, 12.B  

**TLDR:** A survey of 79 papers comparing tree-based and deep learning methods for time series prediction finds that LightGBM, LSTM, and CatBoost perform best, with tree-based methods offering greater computational efficiency.

**Problem & Motivation:** Existing surveys cannot draw meaningful comparisons between forecasting models due to heterogeneous experimental setups across independent studies. This gap prevents robust conclusions about relative strengths and weaknesses of tree-based versus deep learning approaches. This survey addresses the gap by exclusively reviewing studies that compare both methodologies using identical datasets.

**Approach (summary):**
- Searched Web of Science with query combining TBML and DL terms, yielding 589 papers from 2017-2024.
- Selected top 100 most-cited papers, then applied inclusion criteria requiring direct comparison of TBML and DL on identical datasets.
- Included 79 papers with balanced yearly representation from 2020 to 2024.

**Key Findings (selected):**
- num: TBML models achieve best performance in 54.55% of tasks (FPA) with WRA 0.6910, while DL models achieve 52.70% FPA with WRA 0.6486.
- num: RNN models (LSTM, GRU) are best in 61.36% of studies with WRA 0.7330, followed by SPTB models (XGBoost, LightGBM, CatBoost) at 50% FPA and 0.6328 WRA.
- num: CatBoost achieves highest individual FPA and WRA, but LSTM shows more robust performance (58.97% FPA, 0.7222 WRA over 39 evaluations).
- num: TBML models are on average 126,935% faster to train than DL models, with median advantage of 5,603%.

**Supports Odin (direct justifications):**
- LightGBM and LSTM are among the best-performing algorithms for time series forecasting tasks.
- Tree-based methods are significantly more computationally efficient than deep learning methods (median 5603% faster training).
- On large datasets (>200k samples), tree-based models outperform deep learning models.

**Limitations / Contradictions for Odin:**
- The analysis of task categories has relatively small sample sizes (3.85% to 21.8% of papers), limiting statistical certainty.
- Transformer-based architectures are underrepresented with only five papers, limiting generalizability.
- The paper does not address real-time or streaming time series prediction scenarios. [unacknowledged]

**Key takeaways:**
- LightGBM and LSTM are top performers for time series forecasting.
- Tree-based methods train 5603% faster on average than deep learning.
- Dataset size determines best model: small data favors RNNs, large data favors TBML.

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


## Modelling Concept Drift in Dynamic Data Streams for Recommender Systems
**Filename:** `IA--Caroprese-et_al_summarized.md`  
**Authors:** Caroprese, L.; Pisani, F. S.; Veloso, B. M.; Konig, M.; Manco, G.; Hoos, H.; Gama, J. (2025)  
**ID:** `10.1145/3707693`  
**Odin Topics:** 6.A, 8.A, 12.B  

**TLDR:** Generates synthetic data streams with concept drift by modeling user preferences as dynamic tripartite graphs and learning latent embeddings via matrix factorization.

**Problem & Motivation:** Recommender systems research lacks large public datasets that capture evolving user preferences over time. Existing synthetic data generators ignore concept drift, making it hard to evaluate algorithm robustness in streaming scenarios.

**Approach (summary):**
- Uses Bayesian Personalized Ranking (BPR) matrix factorization to learn user and item embeddings from implicit feedback.
- Models concept drift as changes in the tripartite graph connecting users, features, and items, triggered by performance degradation.
- Detects drift via HDDM_W on loss values; when drift occurs, extends latent dimension and retrains with a penalty on deviation from previous model.

**Key Findings (selected):**
- num: The proposed method generates synthetic item frequency distributions that closely match real data when number of users exceeds items.
- Drift detection identified 6 regimes in Amazon Video Games and 1 in Yoochoose, with performance drops followed by recovery.
- Inverted Amazon dataset (users < items) showed poor synthetic fidelity, confirming need for sufficient preferences per item.
- BPR outperformed VAE in adaptive scenarios with many new items, while VAE performed better on stable news datasets.

**Supports Odin (direct justifications):**
- Adaptive matrix factorization models outperform static models when user preferences drift over time.
- Drift detection based on loss function monitoring can reliably identify distribution shifts in streaming interaction data.
- Synthetic data generation with controlled drifts is necessary for evaluating algorithm robustness in personal finance systems.

**Limitations / Contradictions for Odin:**
- Synthetic data generation quality depends on sufficient item preferences; poor performance when users < items.
- Drift detection using HDDM_W assumes bounded signals; not validated on financial data. [unacknowledged]
- Experiments only on three non-financial datasets; generalization to PFMS untested.

**Key takeaways:**
- BPR matrix factorization with drift detection generates realistic synthetic preference streams.
- Hit rate drops to 0.6 after drift but recovers within a few batches.
- Adaptive models outperform static when user preferences change over time.

---


## A SYSTEMATIC REVIEW OF DEMAND FORECASTING MODELS FOR RETAIL E-COMMERCE ENHANCING ACCURACY IN INVENTORY AND DELIVERY PLANNING
**Filename:** `IA--Chowdury-et_al_summarized.md`  
**Authors:** Chowdhury, A. R.; Paul, R.; Rozony, F. Z. (2025)  
**ID:** `10.63125/mbbfw637`  
**Odin Topics:** 6.A, 6.B, 12.A, 12.B  

**TLDR:** A systematic review of 72 studies finds machine learning and deep learning models outperform traditional statistical methods for demand forecasting in retail e-commerce, especially with volatile data and external variables.

**Problem & Motivation:** Retail e-commerce faces volatile demand and complex logistics, requiring accurate forecasting. Existing literature lacks a comprehensive synthesis of forecasting models for inventory and delivery planning. This review addresses that gap by evaluating 72 studies to guide model selection.

**Approach (summary):**
- Followed PRISMA guidelines for systematic review of 72 peer-reviewed articles from Scopus, Web of Science, IEEE Xplore, and ScienceDirect (2010–2024).
- Used keyword combinations including “demand forecasting,” “retail e-commerce,” “machine learning,” and “deep learning” to identify relevant studies.
- {'Categorized forecasting models into four groups': 'traditional statistical, machine learning, deep learning, and hybrid approaches.'}

**Key Findings (selected):**
- Traditional statistical models (ARIMA, Holt-Winters) remain relevant for stable, seasonal demand but fail under nonlinearity and promotional spikes.
- {'num': 'Machine learning models (random forests, gradient boosting) improve forecast accuracy by up to 20% over statistical methods in high‑SKU environments.'}
- Deep learning models (LSTM, GRU, CNN) capture long‑range dependencies and outperform other methods for erratic and intermittent demand.
- Hybrid ARIMA‑ML/DL models balance interpretability and accuracy, reducing forecasting error during flash sales and disruptions.

**Supports Odin (direct justifications):**
- Machine learning models improve forecasting accuracy by up to 20% over statistical methods in volatile demand environments.
- Integration of external data like weather and social media sentiment enhances demand forecast precision.
- Hybrid ARIMA‑ML models balance interpretability and accuracy for short‑term forecasts.

**Limitations / Contradictions for Odin:**
- The review only includes English‑language peer‑reviewed studies, potentially missing relevant industry reports. [unacknowledged]
- Performance comparisons across studies use different datasets and evaluation protocols, making direct aggregation difficult. [acknowledged in discussion]
- The paper does not address real‑time deployment constraints or inference latency for forecasting models.

**Key takeaways:**
- Forecasting accuracy can reduce inventory costs by up to 25%.
- Machine learning models beat statistical methods by 20% in volatile settings.
- Deep learning captures long‑term spending patterns better than ARIMA.

---


## A Comparative Review of Electricity Load Forecasting Methods Across Temporal Horizons
**Filename:** `IA--Saeedian_summarized.md`  
**Authors:** Saeedian, Z. (2024)  
**ID:** `b7c4e2d1-9a8f-4c3b-8e2d-1f5a7c9b3e6d`  
**Odin Topics:** 6.A, 6.B, 12.A, 12.B  

**TLDR:** Reviews electricity load forecasting methods across short, medium, and long horizons, comparing statistical, machine learning, deep learning, and hybrid models for temporal pattern capture.

**Problem & Motivation:** Accurate load forecasting is critical for grid stability and renewable integration. Existing methods face challenges with nonlinearity, uncertainty, and data availability. A structured comparison across time horizons is missing.

**Approach (summary):**
- Reviews literature on short-term (minutes to 1 week), medium-term (1 week to 1 month), and long-term (beyond 1 month) forecasting.
- Categorizes methods into statistical (ARIMA, SARIMA, regression), machine learning (SVR, tree-based), deep learning (LSTM, Transformer), and hybrid models.
- Evaluates models based on accuracy, interpretability, computational cost, and data requirements.

**Key Findings (selected):**
- num: LSTM achieved MAPE of 2.42% for Turkish electricity consumption, outperforming SARIMA.
- num: XGBoost achieved lowest MAPE of 1.88% for short-term forecasting in Algeria.
- num: Hybrid ETS+RD-LSTM reduced MAPE by up to 25% over standalone models.
- Statistical models like ARIMA work for stable seasonal patterns but fail with nonlinearity.

**Supports Odin (direct justifications):**
- LSTM achieves higher accuracy than SARIMA for electricity consumption forecasting.
- XGBoost outperforms other machine learning models for short-term load forecasting with MAPE of 1.88%.
- Hybrid models combining statistical and deep learning methods reduce forecasting error by up to 25%.

**Limitations / Contradictions for Odin:**
- Based on published literature and benchmark datasets, real-world constraints not modeled.
- Hybrid model performance varies significantly across datasets and implementations.
- Probabilistic forecasting methods were only lightly discussed.

**Key takeaways:**
- LSTM achieves 2.42% MAPE for electricity forecasting.
- XGBoost outperforms other models with 1.88% MAPE.
- Hybrid models reduce error by up to 25%.

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


## Recurrent Neural Networks: A Comprehensive Review of Architectures, Variants, and Applications
**Filename:** `IA--Mienye-et_al-2024_summarized.md`  
**Authors:** Mienye, I. D.; Swart, T. G.; Obaido, G. (2024)  
**ID:** `10.3390/info15090517`  
**Odin Topics:** 3.A, 6.A, 6.B, 8.A, 8.B, 12.B  

**TLDR:** Recurrent neural networks and their variants enable effective processing of sequential data for applications including time series forecasting, anomaly detection, and natural language processing.

**Problem & Motivation:** Previous reviews of RNNs do not fully capture the latest advancements in architectures and applications across a broad range of fields. A comprehensive review is needed to assess theoretical advancements and practical implementations to help shape future research.

**Approach (summary):**
- Surveys foundational RNN architectures including basic RNN, LSTM, and GRU.
- Reviews advanced variants such as bidirectional LSTM, peephole LSTM, echo state networks, and independently recurrent neural networks.
- Examines hybrid models combining RNNs with CNNs, attention mechanisms, and transformers.

**Key Findings (selected):**
- num: LSTM and GRU effectively mitigate vanishing gradient problems in sequential modeling.
- num: Bidirectional RNNs improve context understanding by processing sequences in both directions.
- Hybrid CNN-RNN models outperform standalone RNNs in video analysis and time series forecasting.
- Attention mechanisms integrated with RNNs enhance long-range dependency modeling.

**Supports Odin (direct justifications):**
- Bidirectional RNNs improve context understanding in sequential classification tasks.
- LSTM networks effectively capture long-term dependencies in time series data.
- Attention-enhanced RNNs outperform standard RNNs in anomaly detection.

**Limitations / Contradictions for Odin:**
- Training RNNs on long sequences remains computationally intensive compared to transformer architectures.
- RNNs are often perceived as black-box models with limited interpretability, a challenge acknowledged but not solved.
- Bias in training data can lead to unfair predictions; the review notes this but offers no mitigation for financial applications.

**Key takeaways:**
- LSTM and GRU solve vanishing gradient problems in sequential data.
- Bidirectional processing captures both past and future context.
- Hybrid CNN-RNN models excel at spatiotemporal forecasting.

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


## Machine Learning Approaches in Classifying Income Levels
**Filename:** `LA--Laspinas-&-Murcia_summarized.md`  
**Authors:** Laspiñas, E. L.; Murcia, J. V. B. (2024)  
**ID:** `10.5281/zenodo.10049652`  
**Odin Topics:** 12.A, 12.B  

**TLDR:** Six machine learning classifiers for adult income classification are compared, with RandomForest and Random Tree achieving over 98% accuracy.

**Problem & Motivation:** Conventional econometric models struggle to capture non-linear dynamics of income distribution. Machine learning offers a data-driven alternative to improve income level prediction accuracy. This study addresses the gap by systematically comparing multiple classifiers on a real-world dataset.

**Approach (summary):**
- Used Adult Income Prediction dataset from Kaggle with 16,281 observations and 13 features including age, occupation, education, and capital gain.
- Applied InfoGainAttributeEval and Ranker in Weka for feature selection, identifying 'Relationship' as most predictive.
- Evaluated Logistic, J48 (Decision Tree), RandomForest, Random Tree, IBk (k-NN), and NaiveBayes classifiers.

**Key Findings (selected):**
- num: RandomTree achieved highest accuracy at 98.37%, correctly classifying 16,016 instances.
- num: RandomForest achieved 98.35% accuracy with F-measure of 0.983.
- num: J48 accuracy improved from 87.21% (C=0.25) to 90.84% (C=0.75).
- num: IBk accuracy decreased from 89.11% (k=3) to 85.74% (k=9), contradicting expected improvement with higher k.

**Supports Odin (direct justifications):**
- RandomForest and Random Tree achieve over 98% accuracy in binary classification tasks.
- Increasing confidence factor in J48 improves accuracy but risks overfitting.
- Smaller k values (k=3) yield higher k-NN accuracy for this dataset.

**Limitations / Contradictions for Odin:**
- The study only uses a single dataset (Adult Income) and does not test on Philippine data. [unacknowledged]
- No comparison with deep learning methods like neural networks. [unacknowledged]
- The paper does not address class imbalance or feature engineering beyond information gain. [unacknowledged]

**Key takeaways:**
- RandomTree and RandomForest both exceeded 98% classification accuracy.
- Ensemble methods reduce overfitting and generalize better than single classifiers.
- Parameter tuning (confidence factor, k) significantly alters classifier performance.

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


## Dive into Time-Series Anomaly Detection: A Decade Review
**Filename:** `IA--Boniol-et_al_summarized.md`  
**Authors:** Boniol, P.; Liu, Q.; Huang, M.; Palpanas, T.; Paparrizos, J. (2024)  
**ID:** `d3b4c5a6-7e8f-4a9b-8c0d-1e2f3a4b5c6d`  
**Odin Topics:** 8.A, 8.B, 12.A, 12.B  

**TLDR:** A comprehensive survey categorizing time-series anomaly detection methods into distance-based, density-based, and prediction-based approaches, with a process-centric taxonomy and meta-analysis of trends.

**Problem & Motivation:** Despite decades of research, time-series anomaly detection methods are scattered across disconnected communities using different datasets and evaluation measures, making it impossible to identify best practices. A structured, unified taxonomy is missing to organize existing solutions and guide future research.

**Approach (summary):**
- The survey reviews over 200 papers on time-series anomaly detection published between 1980 and 2023.
- A process-centric taxonomy groups methods into distance-based, density-based, and prediction-based categories, further divided into nine subcategories.
- A meta-analysis examines the evolution of method types, supervision levels, and univariate vs. multivariate capabilities over time.

**Key Findings (selected):**
- num: After 2016, prediction-based methods, especially LSTM and autoencoder, represent nearly 50% of new anomaly detection methods.
- num: 65% of anomaly detection methods proposed between 1980 and 2000 were unsupervised, dropping to 50% between 2012 and 2018.
- Simple time-series classification baselines can improve model selection accuracy by a factor of 2 compared to the best individual anomaly detector.
- Point-adjusted evaluation metrics overestimate performance and even random anomaly scores can yield seemingly good results.

**Supports Odin (direct justifications):**
- No single anomaly detection method performs best on all datasets, requiring model selection or ensembling.
- Prediction-based methods (LSTM, autoencoder) are most effective for semi-supervised settings with anomaly-free training data.
- Point-adjusted evaluation metrics overestimate detection performance and should be avoided for time-series anomalies.

**Limitations / Contradictions for Odin:**
- Benchmark datasets often have trivial anomalies, unrealistic anomaly density, or mislabeled ground truth [unacknowledged].
- Many semi-supervised methods assume anomaly-free training data, which is rarely available in practice [acknowledged].
- The survey does not provide a systematic empirical comparison, making it hard to rank methods [acknowledged].

**Key takeaways:**
- After 2016, deep learning methods represent half of new anomaly detection research.
- Volume Under the Surface (VUS) is the most robust evaluation metric for time-series anomalies.
- Point-adjusted metrics overestimate performance and should not be used.

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


## Forecasting the Future: A Comprehensive Review of Time Series Prediction Techniques
**Filename:** `IA--Kolambe-&-Arora_summarized.md`  
**Authors:** Kolambe, M.; Arora, S. (2024)  
**ID:** `3c5b4f2a-8e6d-4c9a-b1e3-9f7d2c8a5e1b`  
**Odin Topics:** 6.A, 6.B, 12.A, 12.B, 8.A  

**TLDR:** From classical ARIMA to deep learning LSTM, time series forecasting techniques are comprehensively reviewed, including hybrid methods, challenges, and evaluation metrics.

**Problem & Motivation:** Time series forecasting is critical for finance, economics, weather, and industrial processes. Traditional methods struggle with complex patterns and dynamics in real-world data. This review synthesizes key advancements and guides method selection.

**Approach (summary):**
- Surveys classical methods including ARIMA, exponential smoothing, Prophet, and STL decomposition.
- Covers machine learning approaches: regression, decision trees, random forests, SVM, and gradient boosting.
- Reviews deep learning techniques: RNN, LSTM, GRU, and Transformer-based models.

**Key Findings (selected):**
- Classical methods like ARIMA work for simple trends and seasonality but fail on complex patterns.
- LSTM and GRU effectively capture long-term dependencies in time series data.
- Hybrid methods that combine decomposition with deep learning improve forecast accuracy.
- Noisy data, outliers, and missing values remain major challenges for forecasting models.

**Supports Odin (direct justifications):**
- Classical methods like ARIMA fail on complex patterns, motivating deep learning for spending forecasting.
- LSTM networks effectively capture long-term dependencies in sequential data.
- Hybrid models combining decomposition and neural networks improve forecast accuracy.

**Limitations / Contradictions for Odin:**
- Lacks empirical validation of any specific forecasting method on real-world datasets. [unacknowledged]
- Does not address computational efficiency or latency, which are critical for real-time personal finance applications. [unacknowledged]

**Key takeaways:**
- Time series forecasting methods range from classical ARIMA to deep learning LSTM.
- Hybrid models often outperform pure classical or deep learning approaches.
- MAE and RMSE are essential for evaluating forecast accuracy.

---


## Exploring Machine Learning for Credit Card Fraud Detection from a Philippine Perspective
**Filename:** `LA--Blancaflor-et_al_summarized.md`  
**Authors:** Blancaflor, E.; Asuncion, K. D.; Reyes, H. J.; Verzosa, M. (2024)  
**ID:** `10.1145/3698062.3698088`  
**Odin Topics:** 8.A, 8.B, 12.B  

**TLDR:** Evaluates machine learning models (SVM, ANN, k-NN, Naive Bayes, logistic regression) for credit card fraud detection in the Philippines, finding ANN achieves up to 98.44% accuracy.

**Problem & Motivation:** Credit card fraud in the Philippines increased 21% since COVID-19, with traditional fraud prevention systems inadequate due to large data volumes, imbalanced distributions, concept drift, and real-time detection needs. There is a need to customize machine learning algorithms to the Philippine economic, technological, and social context to improve fraud detection effectiveness.

**Approach (summary):**
- {'Data source': 'credit card transaction data from the Philippines (dataset size not specified).'}
- {'Methods evaluated': 'logistic regression, k-Nearest Neighbors, Naive Bayes, Support Vector Machines, and Artificial Neural Networks with GA and SMOTE enhancements.'}
- {'Evaluation metrics': 'accuracy, sensitivity, specificity, precision, Matthews Correlation Coefficient, and balanced classification rate.'}

**Key Findings (selected):**
- num: ANN-SMOTE achieved the best performance with up to 98.44% accuracy.
- num: k-NN achieved 97.69% accuracy and Naive Bayes 97.92% accuracy.
- num: Logistic regression had the lowest accuracy at 54.86%.
- A trade-off exists between model accuracy and explainability; logistic regression is better for regulatory compliance.

**Supports Odin (direct justifications):**
- ANN-SMOTE achieves 98.44% accuracy for fraud detection in the Philippine context.
- Logistic regression offers interpretability at the cost of lower accuracy (54.86%).
- Imbalanced data handling via SMOTE improves detection performance.

**Limitations / Contradictions for Odin:**
- No explicit dataset size or transaction volume provided. [unacknowledged]
- All reported accuracies are from cited secondary sources, not original experiments. [unacknowledged]
- Real-time detection challenges mentioned but no latency or throughput benchmarks given.

**Key takeaways:**
- ANN-SMOTE achieves 98.44% accuracy for fraud detection.
- Imbalanced data handling is critical for anomaly detection.
- Explainability trade-off matters for regulatory compliance.

---


## Use of Boosting Algorithms in Household-Level Poverty Measurement: A Machine Learning Approach to Predict and Classify Household Wealth Quintiles in the Philippines
**Filename:** `LA--Salvador_summarized.md`  
**Authors:** Salvador, E. L. V. (2024)  
**ID:** `8a7b6c5d-4e3f-2a1b-9c8d-7e6f5a4b3c2d`  
**Odin Topics:** 5.C, 6.A, 12.B  

**TLDR:** Boosting algorithms, especially CatBoost, accurately classify household wealth quintiles using Philippine DHS data, with CatBoost achieving 90.93% accuracy.

**Problem & Motivation:** Poverty measurement often oversimplifies multidimensional aspects or relies on limited features. Conventional econometric methods may overlook important data relationships. Machine learning, particularly boosting algorithms, offers advantages in handling high-dimensional data but remains underutilized for poverty prediction in the Philippines.

**Approach (summary):**
- Data from 2022 Philippine DHS, originally 2,099 features and 30,372 households, cleaned to 396 features and 20,679 households.
- Applied five boosting algorithms: AdaBoost, CatBoost, GBM, LightGBM, and XGBoost to classify households into five wealth quintiles.
- Used SMOTE to handle class imbalance, hyperparameter tuning via grid search and manual trial, and 80/20 train-test split with 10% validation.

**Key Findings (selected):**
- num: CatBoost achieved highest accuracy at 90.93%, followed by XGBoost (89.41%), GBM (89.05%), and LightGBM (88.52%).
- num: AdaBoost had lowest accuracy at 80.39% and significantly lower AUC-ROC scores for poorer classes.
- num: CatBoost had longest training time (69.29s) but fastest testing (0.01s); AdaBoost fastest training (4.48s) but slowest testing (0.23s).
- AUC-ROC scores near 0.99-1.00 for CatBoost, GBM, LightGBM, XGBoost across most wealth classes.

**Supports Odin (direct justifications):**
- CatBoost achieves 90.93% accuracy in five-class wealth classification on Philippine household data.
- Boosting algorithms can effectively handle high-dimensional feature sets for poverty prediction.
- LightGBM and XGBoost offer good balance of high performance and computational efficiency.

**Limitations / Contradictions for Odin:**
- Data cleaning removed many features and households, potentially introducing bias.
- Only five boosting algorithms compared; other ML methods not included.
- Hyperparameter tuning may not be optimal across all models.

**Key takeaways:**
- CatBoost achieved 90.93% accuracy for wealth quintile classification.
- LightGBM and XGBoost balance high accuracy with fast training and small model size.
- AdaBoost had lowest accuracy (80.39%) and higher misclassification for poorer classes.

---


## Budgeted Embedding Table For Recommender Systems
**Filename:** `IA--Qu-et_al_summarized.md`  
**Authors:** Qu, Y.; Chen, T.; Nguyen, Q. V. H.; Yin, H. (2024)  
**ID:** `10.1145/3616855.3635778`  
**Odin Topics:** 4.A, 4.B, 7.B, 7.C, 12.B  

**TLDR:** Proposes Budgeted Embedding Table (BET) for efficient embedding size search in recommender systems under strict memory budgets using table-level actions and a fitness predictor.

**Problem & Motivation:** Existing lightweight embedding methods rely on manually tuned trade-off coefficients that fail to strictly meet memory budgets and perform inefficient instance-by-instance search. The implicit memory complexity term cannot guarantee parameter usage caps, and RL-based approaches require costly per-instance optimization. A method is needed that directly enforces memory budgets while scaling to large user/item sets.

**Approach (summary):**
- Uses two real-world datasets, Gowalla and Yelp2018, with up to 1.56M interactions.
- Defines a bounded sampler that draws embedding sizes for all users and items from probabilistic distributions, ensuring total parameter usage is capped.
- Employs a DeepSets-based fitness predictor that evaluates table-level actions without full model retraining.

**Key Findings (selected):**
- num: BET achieves the highest Recall@20 (0.1753) and NDCG@20 (0.1483) on Gowalla with LightGCN at 80% sparsity.
- num: At 95% sparsity on Gowalla with LightGCN, BET obtains 0.0627 Recall@5 and 0.1037 NDCG@5, outperforming CIESS by 22% and 21% respectively.
- num: On Yelp2018 with LightGCN at 80% sparsity, BET reaches 0.0873 Recall@20, exceeding the best baseline by 4%.
- BET guarantees strict memory budget satisfaction, unlike ESAPN and OptEmbed which often exceed target sparsity.

**Supports Odin (direct justifications):**
- A table-level action that sets embedding sizes for all users simultaneously can strictly enforce a memory budget.
- DeepSets-based fitness prediction reduces the number of full model evaluations from O(number of candidates × iterations) to O(iterations).
- Ranking users and items by frequency and allocating larger embeddings to frequent entities improves recommendation quality under sparsity.

**Limitations / Contradictions for Odin:**
- Does not address cold-start users or items; frequency-based ranking fails for new entities. [unacknowledged]
- May not generalize to streaming recommendation where user/item sets grow over time (mentioned as future work).
- Requires a pre-trained full embedding table, which itself may be infeasible for extremely large-scale systems. [unacknowledged]

**Key takeaways:**
- BET guarantees strict memory budget adherence without manual coefficient tuning.
- DeepSets fitness predictor cuts evaluation cost from O(S*T) to O(T) full trainings.
- At 95% sparsity, BET achieves 0.0627 Recall@5 on Gowalla with LightGCN.

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


## A Survey of Time Series Data Forecasting Methods Based on Deep Learning
**Filename:** `IA--Chen-et_al_summarized.md`  
**Authors:** Chen, J.; Chen, T.; Wang, Y.; Wang, L. (2024)  
**ID:** `10.56557/jobari/2024/v30i69014`  
**Odin Topics:** 6.A, 6.B, 12.A, 12.B  

**TLDR:** Surveys deep learning methods for time series forecasting including RNN, LSTM, GRU, and Transformer, and compares their performance on public datasets.

**Problem & Motivation:** Traditional statistical models for time series forecasting require extensive manual feature engineering and struggle with large-scale data. Deep learning offers automatic feature extraction but faces challenges like vanishing gradients and difficulty capturing long-range dependencies. This survey systematically reviews deep learning methods to identify strengths and weaknesses for forecasting tasks.

**Approach (summary):**
- Reviews common time series features, datasets (ETT, ECL, Traffic, Weather, ILI, TE), and evaluation metrics (MSE, MAE, RMSE, MAPE, SMAPE, R²).
- Describes RNN structure and its vanishing/exploding gradient problem.
- Explains LSTM gating mechanism (forget, input, output gates) to address gradient issues.

**Key Findings (selected):**
- num: Transformer achieved best performance on ETTm2 with MSE=3.418, MAE=1.399.
- num: LSTM achieved minimum MAE on Electricity (1.848) and Traffic (0.020).
- num: GRU achieved minimum MSE on Electricity (19.524) and Traffic (0.00110).
- num: RNN achieved best performance on Weather with MSE=0.007, MAE=0.060.

**Supports Odin (direct justifications):**
- Deep learning models can automatically extract temporal features from time series data.
- Transformer self-attention captures long-range dependencies better than RNNs.
- No single model dominates all datasets; model selection depends on data characteristics.

**Limitations / Contradictions for Odin:**
- Survey format; no novel algorithm proposed.
- Univariate experiments may not generalize to multivariate spending data [unacknowledged].
- Excluded datasets with insufficient periodicity, limiting generalizability.

**Key takeaways:**
- Transformer achieved lowest MAE (1.399) on ETTm2 dataset.
- No single deep learning model dominates all time series forecasting tasks.
- Deep learning automates feature extraction but requires large training data.

---


## Single and Multiple Separate LSTM Neural Networks for Multiple Output Feature Purchase Prediction
**Filename:** `IA--Ciric-et_al_summarized.md`  
**Authors:** Ciric, M.; Predic, B.; Stojanovic, D.; Ciric, I. (2023)  
**ID:** `10.3390/electronics12122616`  
**Odin Topics:** 3.A, 6.A, 6.B, 12.A, 12.B  

**TLDR:** Compares single multivariate LSTM against separate LSTM networks for predicting next purchase day and product category from customer transaction data, finding separate networks better for category prediction and single multivariate better for timing.

**Problem & Motivation:** Predicting both the timing and product category of a customer's next purchase from historical transaction data is challenging because input features are multidimensional and outputs are heterogeneous. Existing methods often treat these predictions separately or use single models that underperform on one of the tasks. A systematic comparison of single versus multiple dedicated LSTM architectures for this multi-output problem was missing.

**Approach (summary):**
- Data from a medical device vendor: 7.5M transactions, ~10,100 customers with ≥4 orders, anonymized.
- Product categories defined using GPI (generic product identifier) with 100 drug groups (2‑character tiers) or 16 aggregated categories.
- Input features: time series of days between consecutive purchases and multi-hot encoded vectors of drug groups/categories present in each purchase.

**Key Findings (selected):**
- num: Dedicated LSTM network for drug group/category prediction improved recall for realized purchases by 15–50% across all datasets.
- Single multivariate LSTM network produced better results for next purchase day prediction than a dedicated network.
- Using all 100 drug groups gave higher metrics than using 16 aggregated categories for category prediction.
- For 100+ purchases dataset, a dedicated LSTM correctly predicted at least one purchased drug category for 95.7% of customers.

**Supports Odin (direct justifications):**
- A dedicated LSTM network for spending category prediction achieves 15-50% higher recall than a joint model.
- Single multivariate LSTM for next purchase day prediction outperforms a dedicated day-only network.
- Using fine-grained category labels (100 groups) yields better prediction than aggregated categories (16 groups).

**Limitations / Contradictions for Odin:**
- GPI classification system is specific to medical drugs; not generalizable to all expense categories without adaptation.
- Data comes from B2B medical supply, not young professionals' personal finance. [unacknowledged]
- Does not compare against traditional statistical baselines (ARIMA, exponential smoothing). [unacknowledged]

**Key takeaways:**
- Dedicated LSTM for category prediction improves recall by 15-50% over a joint model.
- Single multivariate LSTM is better for predicting timing of next purchase.
- Fine-grained product categories (100 groups) predict better than aggregated ones.

---


## A Review of ARIMA vs. Machine Learning Approaches for Time Series Forecasting in Data Driven Networks
**Filename:** `IA--Kontopoulou-et_al_summarized.md`  
**Authors:** Kontopoulou, V. I.; Panagopoulos, A. D.; Kakkos, I.; Matsopoulos, G. K. (2023)  
**ID:** `10.3390/fi15080255`  
**Odin Topics:** 6.A, 6.B, 7.A, 7.B, 8.A, 8.B, 12.A, 12.B  

**TLDR:** A review comparing ARIMA statistical models with machine learning and hybrid approaches for time series forecasting across finance, health, weather, utilities, and network applications.

**Problem & Motivation:** The scientific literature lacks an extensive summary comparing ARIMA with machine learning and deep learning time series forecasting methods. Although machine learning models are increasingly used, their claimed superiority over classical statistical methods is not always systematically evaluated. This review addresses that gap by synthesizing comparative studies across multiple application domains.

**Approach (summary):**
- Reviewed published literature comparing ARIMA with SVM, decision tree, deep learning (LSTM, GRU, CNN), and hybrid models.
- {'Organized findings by application domain': 'finance (bitcoin, stocks), healthcare (COVID-19 cases), weather (wind, drought), utilities (energy, water), and network traffic.'}
- Extracted performance metrics including RMSE, MAPE, MAE, MSE, R2, NSE from each comparative study.

**Key Findings (selected):**
- Machine learning and deep learning models generally outperform ARIMA in time series forecasting across most applications reviewed.
- {'num': 'Deep learning models (LSTM, GRU) achieved RMSE values up to 40 times smaller than ARIMA for COVID-19 case forecasting in several countries (Arun Kumar et al., 2022).'}
- {'num': "ARIMA outperforms machine learning models for small datasets, limited value ranges, or strongly linear and seasonal univariate series (e.g., drought forecasting with R2 >0.9 vs. SVM's 0.83)."}
- Hybrid models combining ARIMA with machine learning (e.g., ARIMA-SVM, ARIMA-NARNN, ARIMA-CNN) consistently outperform both individual approaches.

**Supports Odin (direct justifications):**
- Machine learning models generally provide more accurate time series forecasts than ARIMA for non-linear spending data.
- Hybrid ARIMA-ML models consistently outperform pure ARIMA or pure ML models in forecasting tasks.
- ARIMA is preferable for small datasets or when spending patterns are linear and seasonal.

**Limitations / Contradictions for Odin:**
- ARIMA parameter selection depends on forecaster skill and experience.
- Machine learning models require large datasets and higher computational resources. [unacknowledged]
- Review does not cover real-time forecasting requirements for mobile personal finance applications. [unacknowledged]

**Key takeaways:**
- Machine learning outperforms ARIMA for most non-linear time series.
- Hybrid ARIMA-ML models always beat either method alone.
- ARIMA works best for small, linear, or seasonal univariate data.

---


## Continual Deep Learning for Time Series Modeling
**Filename:** `IA--Ao-&-Fayek_summarized.md`  
**Authors:** Ao, S.-I.; Fayek, H. (2023)  
**ID:** `10.3390/s23167167`  
**Odin Topics:** 6.A, 6.B, 8.A, 8.B, 12.A, 12.B  

**TLDR:** Surveys deep learning for sensor time series, highlighting non-stationarity challenges and continual learning methods to mitigate catastrophic forgetting.

**Problem & Motivation:** Real-world time series often exhibit non-stationary distributions, causing deep learning models to suffer catastrophic forgetting. Traditional methods assume stationarity, limiting deployment in dynamic environments. This survey identifies the gap in applying continual learning to time series forecasting and anomaly detection.

**Approach (summary):**
- Conducts systematic review of deep learning for sensor time series from 2018-2023.
- Categorizes methods into deep learning architectures (MLP, RNN, LSTM, CNN, GNN) and preprocessing techniques.
- Evaluates continual learning approaches (regularization, replay, parameter isolation) for time series tasks.

**Key Findings (selected):**
- num: CNN with direct multi-step procedure improved prediction accuracy by 22.6% over seasonal ARIMAX for building load forecasting.
- num: Graph Deviation Network achieved 54% better F-measure than the next best baseline for anomaly detection in water treatment systems.
- num: LSTM achieved mean absolute percentage error of 4.82% for traffic flow forecasting versus 20.97% for ARIMA and 9.06% for BPNN.
- num: Empirical mode decomposition preprocessing improved gesture classification accuracy from 94.22% to 99.73% using CNN.

**Supports Odin (direct justifications):**
- CNN with direct multi-step procedure can improve forecasting accuracy by 22.6% over ARIMAX.
- No single deep learning method fits all time series anomaly detection tasks.
- Simple models with feature engineering can outperform deep learning without preprocessing.

**Limitations / Contradictions for Odin:**
- Survey primarily synthesizes existing literature without new empirical experiments. [unacknowledged]
- Focus on sensor time series limits generalizability to financial transaction sequences. [unacknowledged]
- Computational cost of continual learning on mobile devices is not quantitatively assessed. [unacknowledged]

**Key takeaways:**
- LSTM achieved 4.82% MAPE for traffic forecasting versus 20.97% for ARIMA.
- Empirical mode decomposition preprocessing raised accuracy from 94.22% to 99.73%.
- No single deep learning method works for all anomaly detection tasks.

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
- {'num': 'Deep learning neural network achieved 96.60% accuracy in predicting behavioral intention.'}
- {'num': 'Random forest classifier achieved 94% accuracy at 90:10 train-test split with Gini and best splitter.'}
- Perceived environmental concern (PENC) was the most important factor (100% normalized importance), followed by attitude (96.32%) and perceived behavioral control (94.50%).
- Basic decision tree produced much lower accuracy (max 72.32%) due to random tree generation per iteration.

**Supports Odin (direct justifications):**
- Random forest classifier achieved 94% accuracy in predicting behavioral intentions from 12 latent variables.
- Deep learning neural network with tanh activation outperformed random forest with 96.6% accuracy.
- Perceived environmental concern is the most important predictor (100% normalized importance).

**Limitations / Contradictions for Odin:**
- Limited constructs from adapted questionnaire; self-administered online survey may introduce response bias. [unacknowledged]
- Only drivers with a license and social media presence were sampled, excluding non-digital or non-licensed populations.
- Only two machine learning algorithms (RFC and DLNN) were used; other algorithms like Naïve Bayes or k-NN were not tested.

**Key takeaways:**
- Deep learning achieved 96.6% accuracy for predicting purchase intentions.
- Perceived environmental concern was the most important factor.
- Random forest classifier reached 94% accuracy with Gini and best splitter.

---


## A Recommendation System for Participatory Budgeting
**Filename:** `IA--Leibiker-&-Talmon_summarized.md`  
**Authors:** Leibiker, G.; Talmon, N. (2023)  
**ID:** `f5a3b2c1-4d5e-6f7a-8b9c-0d1e2f3a4b5c`  
**Odin Topics:** 5.B, 6.A, 7.B, 7.C, 11.A, 12.B  

**TLDR:** Machine learning recommendation systems estimate voter preferences from partial ballots in participatory budgeting, improving prediction accuracy and budget allocation.

**Problem & Motivation:** Voters in participatory budgeting face information overload when many projects are considered, leading to low participation and poor decisions. Existing methods require complete ballots, which is cognitively burdensome. A solution using recommendation systems can reduce this burden while maintaining allocation quality.

**Approach (summary):**
- Used ten real-world participatory budgeting datasets from Warsaw, Poland (2020-2023), with 2,614 to 10,424 voters and 67 to 111 projects per instance.
- Defined three sampling settings: random (k projects chosen uniformly), offline (choose k projects by popularity, consensus, or controversy), and online adaptive (iteratively choose most controversial projects).
- Applied prediction modules: Matrix Factorization, Factorization Machines, and binary classification using XGBoost with class weighting for imbalance.

**Key Findings (selected):**
- num: At 10% sample degree, classification-online and offline-popularity setups produced higher FA scores than the sampling method.
- num: Classification-offline-popularity achieved the maximal FA score when collecting half of the votes (sample degree 0.5).
- num: As sample degree increased, FA score increased and Symmetric Distance decreased across most LV degree levels.
- Classification techniques consistently outperformed Matrix Factorization and Factorization Machines in prediction accuracy.

**Supports Odin (direct justifications):**
- Machine learning classification on partial user ballots improves budget allocation accuracy compared to naive sampling.
- Adaptive online preference elicitation reduces information overload without sacrificing prediction quality.
- Fractional Allocation score is an effective metric for evaluating budget recommendation systems with incomplete inputs.

**Limitations / Contradictions for Odin:**
- Experiments conducted only on Warsaw PB datasets; results may not generalize to other cultural or demographic contexts. [unacknowledged]
- Assumes existence of a training set of voters with full ballots (LV group), which may be unavailable in pure cold-start scenarios. [unacknowledged]
- Does not address privacy concerns of collecting partial preferences from all voters. [unacknowledged]

**Key takeaways:**
- Classification online achieves higher FA scores than sampling at 10% data collection.
- Fractional Allocation score increases with more exposed preferences.
- Adaptive controversial selection improves prediction over random sampling.

---


## Review of Family-Level Short-Term Load Forecasting and Its Application in Household Energy Management System
**Filename:** `IA--Ma-et_al_summarized.md`  
**Authors:** Ma, P.; Cui, S.; Chen, M.; Zhou, S.; Wang, K. (2023)  
**ID:** `10.3390/en16155809`  
**Odin Topics:** 6.A, 6.B, 12.B  

**TLDR:** Deep learning methods (LSTM, CNN, hybrid) improve short-term household load forecasting accuracy; probabilistic forecasting addresses uncertainty; these enable home energy management system scheduling.

**Problem & Motivation:** Household electricity consumption is rising and lacks consistent patterns due to human behavior, making system-level forecasting methods inadequate. Accurate short-term load forecasting is essential for home energy management systems to optimize energy use and reduce costs. Existing methods have limitations in accuracy, uncertainty handling, and real-time adaptability.

**Approach (summary):**
- Surveys deep learning models (LSTM, CNN, hybrid) for load forecasting with emphasis on sequence learning and feature extraction.
- Analyzes feature extraction techniques including wavelet decomposition, principal component analysis, and mutual information.
- Discusses adaptive online learning methods to handle dynamic load patterns and concept drift.

**Key Findings (selected):**
- num: SVR-LSTM hybrid achieved correlation coefficient 0.9901, outperforming traditional SVR and LSTM.
- num: CNNGRU with attention mechanism reached 92.06% accuracy in small-range load prediction and reduced prediction time by 75%.
- num: Principal component analysis reduced 12 weather factors to 3 dimensions with 93.93% cumulative contribution rate.
- Bottom-up forecasting by aggregating appliance-level predictions improves accuracy over direct household-level forecasting.

**Supports Odin (direct justifications):**
- LSTM networks effectively capture long-term dependencies in sequential household load data.
- Hybrid CNN-LSTM models improve accuracy over single-model approaches for irregular time series.
- Probabilistic forecasting provides uncertainty intervals essential for robust decision-making under variability.

**Limitations / Contradictions for Odin:**
- Data quality issues (missing values, noise) affect prediction accuracy.
- Deep learning models risk overfitting, especially with small datasets.
- Real-time performance and uncertainty from user behavior remain challenging.

**Key takeaways:**
- LSTM with empirical mode decomposition improves household load prediction accuracy.
- Hybrid CNN-LSTM models outperform single models on irregular time series data.
- Probabilistic forecasting captures uncertainty missed by point forecasts.

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
- num: Bagging ensemble achieved 93% accuracy, precision 0.93, recall 0.94, F1 0.94.
- num: Boosting ensemble achieved 89% accuracy.
- Poor income class had most true positives; Rich class had fewest due to fewer instances.
- Model with >80% accuracy is considered good per literature.

**Supports Odin (direct justifications):**
- Naive Bayes with bagging achieves 93% accuracy on household income prediction.
- Expenditure features like food and transportation are strong predictors of income class.
- Models with accuracy above 80% are acceptable for poverty targeting.

**Limitations / Contradictions for Odin:**
- Dataset only covers 2018, not updated annually. [unacknowledged]
- Feature independence assumption of Naive Bayes may reduce real-world accuracy. [unacknowledged]
- Only two ensemble methods tested; other algorithms not compared.

**Key takeaways:**
- Naive Bayes with bagging yields 93% accuracy for income classification.
- Food expenditure is the strongest predictor of income class.
- Seven income brackets from Poor to Rich are used.

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


## Test-Time Adaptation for Non-stationary Time Series: From Synthetic Regime Shifts to Financial Markets
**Filename:** `IA--Wu_Y.-et_al_summarized.md`  
**Authors:** Wu, Y.; Deng, Q.; Chung, W.; Li, M. (0)  
**ID:** `f81d4fae-7dec-11d0-a765-00a0c91e6bf6`  
**Odin Topics:** 6.A, 6.B, 12.A, 12.B  

**TLDR:** Test-time adaptation using batch-normalization statistics refresh or norm-only affine parameter updates improves or harms forecasting accuracy depending on shift type, with bn_stats as a safe default for financial markets.

**Problem & Motivation:** Real-world time series like financial prices are non-stationary, causing models trained on past data to lose accuracy under distribution shifts. Existing test-time adaptation methods lack causal, parameter-efficient frameworks for streaming forecasting. This paper studies when small-footprint TTA helps or hurts under synthetic and real regime shifts.

**Approach (summary):**
- Freeze backbone and update only normalization affine parameters (γ,β) using unsupervised objectives on recent unlabeled windows.
- For classification: minimize entropy and enforce temporal consistency via weak time-preserving augmentations.
- For regression: minimize prediction variance across augmentations and optionally distill from an EMA teacher.

**Key Findings (selected):**
- num: On SPY directional classification, bn_stats achieves 0.525 accuracy vs no_tta 0.504 and norm_only 0.512.
- num: Under gradual synthetic drift, norm_only reduces MAE to 0.22 (R2 0.31) vs no_tta 0.28 (R2 -0.31).
- num: BN-Stats yields Sharpe ratio 1.930 on SPY and 4.080 on QQQ, higher than no_tta (1.746, 3.205) and norm_only (1.544, 1.349).
- Diebold-Mariano tests show bn_stats significantly better than no_tta on SPY (p=0.0054) and QQQ (p=0.0220).

**Supports Odin (direct justifications):**
- Batch-normalization statistics refresh is a safe default for financial time series forecasting.
- Norm-only adaptation can hurt performance on noisy equity markets and should be used with uncertainty control.
- Uncertainty-triggered fallback prevents harmful gradient updates when entropy or variance is high.

**Limitations / Contradictions for Odin:**
- Synthetic shift generators are stylized and cannot cover all real dynamics [unacknowledged].
- Only one backbone architecture (TCN) is used for main results; findings may not generalize to other backbones [unacknowledged].
- No comparison to online learning or continual learning baselines [unacknowledged].

**Key takeaways:**
- BN statistics refresh improves Sharpe ratio from 1.75 to 1.93 on SPY.
- Norm-only adaptation helps gradual drift but hurts noisy markets.
- Uncertainty fallback prevents harmful updates in high entropy days.

---


## Next.js-Powered AI Platform for Smart Expense Tracking, Budgeting and Insights
**Filename:** `IA--Badiger-et_al_summarized.md`  
**Authors:** Badiger, R.; Robin, R.; Moraas, T.; Naik, V. G.; Karthikeyan, A. N. (0)  
**ID:** `e5c5f2a3-4b5c-6d7e-8f9a-0b1c2d3e4f5a`  
**Odin Topics:** 3.A, 3.B, 6.A, 6.B, 7.A, 7.B, 7.C, 8.A, 8.B, 12.A, 12.B  

**TLDR:** A Next.js-based AI platform integrates XGBoost transaction categorization, Gemini LLM insights, and Prophet forecasting, achieving 91.3% F1-score and reducing manual effort by 78%.

**Problem & Motivation:** Digital payment growth in India produces vast personal financial data, but individuals lack effective tools to interpret and act on it. Traditional budgeting methods fail to provide real-time, context-aware insights. Existing AI-driven systems suffer from limited personalization, opaque recommendations, and poor multi-channel support.

**Approach (summary):**
- System built on Next.js 14 with Clerk authentication, Supabase PostgreSQL, and Prisma ORM.
- XGBoost classifier maps transactions to 18 categories using merchant, amount, and temporal features.
- Gemini LLM generates insights via RAG prompting with user spending summaries and anomaly scores.

**Key Findings (selected):**
- num: Weighted F1-score of 0.913 across 18 spending categories.
- num: Manual expense-logging effort reduced by approximately 78% compared to conventional approaches.
- High-frequency categories (Food & Dining, Transport, Utilities) achieve F1 above 0.95.
- 84% of pilot users found AI-generated insights useful or very useful.

**Supports Odin (direct justifications):**
- XGBoost with temporal features achieves 91.3% weighted F1-score for transaction categorization.
- LLM-generated insights using RAG are rated useful by 84% of users.
- Prophet forecasting requires at least 3 months of historical data for reliable predictions.

**Limitations / Contradictions for Odin:**
- {'Cold-start problem': 'categorization accuracy lower for new users with fewer than 50 transactions.'}
- {'LLM hallucination risk': 'Gemini may generate imprecise guidance despite RAG.'}
- {'Manual data entry dependency': 'users may not maintain complete records without banking API.'}

**Key takeaways:**
- XGBoost achieves 91.3% F1-score for transaction categorization.
- LLM insights rated useful by 84% of pilot users.
- Manual expense logging effort reduced by 78%.

---


## 📌 Note for the Agent

The summaries above contain **essential extracts** – enough to understand the paper's relevance to Odin, including supporting evidence and limitations.
If you need additional details not shown here (e.g., **critical citations, definitions, equations, full methodology, or the complete mapping rationale**),
**ask the user to send the original summary file (`<filename>_summarized.md`) or the converted MarkItDown file(`<filename>_marked.md`)** for the specific paper(s) of interest.
Do not invent missing information. Acknowledge gaps when they exist.