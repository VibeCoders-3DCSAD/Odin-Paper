# Analyzing and Rewarding Credit Card Spending Habits in India: a Machine Learning Approach

## Metadata

```yaml
---
paper_id: "10.1007/s44196-025-00899-0"
designation: algorithm-specific
title: "Analyzing and Rewarding Credit Card Spending Habits in India: a Machine Learning Approach"
authors: "Agrawal, R.; Khanna, A.; Hamdare, S."
year: 2025
venue: "International Journal of Computational Intelligence Systems"
odin_topics: ["3.A", "3.B", "5.A", "5.B", "5.C", "6.A", "6.B", "11.B", "12.B"]
shorthand_tags: ["/cat-approaches", "/cultural-expense-categories", "/profiling-role", "/profile-dimensions", "/profiling-cold-start", "/classification-vs-clustering", "/classifier-candidates", "/classifier-eval-metrics", "/forecasting-methods-survey", "/forecast-algo-candidates", "/forecast-algo-comparison", "/forecast-eval-metrics", "/retention-mechanisms", "/value-driven-retention", "/eval-ml-design"]
member_checklist:
  - name: "Gabion, Stefanie S."
    status: "[ ]"
  - name: "Guevarra, Joaquin Luis T."
    status: "[ ]"
  - name: "San Jose, Alexa Joanne Paula G."
    status: "[ ]"
  - name: "Togle, Charles Nathaniel B."
    status: "[ ]"
---
```

## TL;DR

Machine learning segmentation (K-Means) and regression models (Random Forest, XGBoost) optimize credit card reward points, achieving **R² = 0.99** by aligning higher rewards with luxury and travel spending.

## Problem and Motivation

Traditional credit card reward programs use static, one‑size‑fits‑all structures that fail to personalize incentives for high‑value spenders in categories like luxury and travel. This disconnect reduces customer loyalty and engagement, especially during peak spending seasons such as festivals. Prior ML work on spending prediction either lacked real‑time adaptability or ignored discretionary categories critical for profitable reward allocation.

## Approach

- **Data sources** – Original dataset from Kaggle (“Credit Card Spending Habits in India”) with 83M+ cards context, then a synthetic dataset generated using Python’s Faker library to add features (e.g., income category, attrition risk, card promotion date).
- **Clustering** – K‑Means (k=4) segments users by card type (Silver, Gold, Platinum, Signature) using monthly spend, transaction frequency, credit utilization, and temporal features. Compared with DBSCAN and GMM; Silhouette score = 0.42 (K‑Means best).
- **Reward point formula** – Custom scoring: `ScoredPoints = RCT + CPD + ET + IC + NoC + AR` (base multiplier, promotion, expense type, income, card penalty, attrition risk). Final points = (ScoredPoints × AmountSpent) / 500.
- **Predictive models** – Linear Regression, Random Forest, XGBoost trained to predict reward points from transaction features.
- **Evaluation metrics** – R², RMSE, MAE for regression; Silhouette score and Davies‑Bouldin Index for clustering.

## Findings

1. **Clustering validation** – K‑Means cleanly separated four card‑type clusters, confirming that card type aligns with spending behavior (Platinum: high luxury/travel; Silver: essential groceries).
2. **Model accuracy** – **Random Forest achieved R² = 0.99**, RMSE = 14.2, MAE = 8.5 on synthetic data, outperforming XGBoost (R² = 0.98) and Linear Regression (R² = 0.85).
3. **Reward distribution** – Synthetic dataset with 10+ features produced reward points spanning 0–3500, while the original (5 features) capped at 1000. Mean reward points rose to ≈1000 with additional features.
4. **Seasonal pattern** – Synthetic data showed spending spikes during Diwali, Christmas, and Holi, supporting festive‑season reward adjustments.
- Synthetic data’s correlation matrix identified the most predictive features (monthly spend, expense type, card type), dropping irrelevant ones.

## Key Figures and Tables

- Figure 2a–2d: EDA of original dataset (transaction amounts, gender, card type, expense type) → reveals outdated data (2014–2015) and missing user‑level identifiers.
- Figure 3a: Box plot of spending amount by card type → Platinum and Signature have higher median spends and more outliers.
- Figure 3b: Monthly spending trends over 15 months → festive peaks (Diwali, Christmas, Holi) clearly visible.
- Figure 5: 3D cluster visualization → four card‑type clusters are distinctly separated.
- Table 5: Base multiplier per card type (Platinum: 2.0, Signature: 1.5, Gold: 1.0, Silver: 0.5) → core reward scaling factor.

## Key Equations

$$RewardPoints = \frac{ScoredPoints \times AmountSpent}{500}$$
*Total points scale linearly with monthly spend and composite score.*

$$ScoredPoints = RCT + CPD + ET + IC + NoC + AR$$
*Sum of six weighted factors personalizes each user’s point rate.*

## Definitions

| Term / Acronym | Plain‑English Definition |
| -------------- | ------------------------ |
| K‑Means | Clustering algorithm that groups users into k segments by minimizing within‑cluster distances. |
| RCT | Base multiplier for reward points based on card type (Platinum highest). |
| CPD | Card Promotion Date bonus – extra points when a user upgrades to a higher card tier. |
| ET | Expense Type bonus – higher points for travel/dining (+3.0), lower for groceries/bills (+0.5). |
| IC | Income Category bonus – high‑income users get +1.0, middle +0.5. |
| NoC | Number of Cards penalty – subtract 0.5 for each card beyond the first (discourages multiple cards). |
| AR | Attrition Risk bonus – add +1.0 for users likely to leave (retention incentive). |
| R² | Coefficient of determination – proportion of variance explained by the model (0.99 = almost perfect). |
| RMSE | Root Mean Square Error – average prediction error in original units (lower is better). |
| MAE | Mean Absolute Error – average absolute prediction error (robust to outliers). |
| DBI | Davies‑Bouldin Index – clustering validity measure; lower values (<1) indicate compact, well‑separated clusters. |

## Critical Citations

- [Cheema & Van der Stede, 2019] — Established that category‑specific rewards (luxury/travel) increase engagement and usage frequency.  
- [Li, Ngai & Hu, 2021] — Survey of ML in finance, identifying K‑Means and Random Forest as effective for segmentation.  
- [Gan, Xu & Chen, 2021] — Used XGBoost/LightGBM to predict high‑value spending, informing reward allocation.  
- [Sadat Akash, 2024] — Credit card transaction dataset used as baseline; this paper extends it with synthetic features.

## Relevance to Odin

**Topics:**

3.A — Expense Categorization Frameworks (Paper defines discrete expense types: luxury, travel, groceries, EMIs, entertainment, dining, bills, providing a template for Odin’s category design.)

3.B — Expense Category Design Considerations (Higher rewards for discretionary categories (travel/luxury) vs. essentials (groceries) illustrates how category grouping influences user behavior.)

5.A — Financial Behavioral Profiles in Personal Finance (K‑Means clustering identifies four distinct spending profiles (Platinum, Gold, Silver, Signature) directly analogous to Odin’s required user profiling.)

5.B — Profile Dynamics and the Cold‑Start Problem (Synthetic data generation addresses missing user‑level identifiers and outdated records, informing Odin’s cold‑start strategy for new users.)

5.C — Financial Behavioral Profile Classification Algorithm (Comparison of K‑Means, DBSCAN, GMM with silhouette scores and DBI provides empirical guidance for Odin’s classifier selection.)

6.A — Predictive Modeling in Personal Finance Systems (ML models (Random Forest, XGBoost) predict reward points from spending features, validating the use of supervised learning for financial outcomes.)

6.B — Spending Forecasting Algorithm (Random Forest outperforms XGBoost and Linear Regression on R²=0.99; this benchmark informs Odin’s forecasting algorithm choice.)

11.B — Retention Mechanisms and Engagement Design (Personalized rewards targeting high‑margin categories (travel/luxury) are shown to increase customer loyalty and reduce churn, directly supporting Odin’s retention design.)

12.B — Evaluation of Algorithmic Modules (Use of R², RMSE, MAE for regression and silhouette score, DBI for clustering provides a replicable evaluation framework for Odin’s algorithmic modules.)

**Contribution to Odin:**

This paper justifies Odin’s use of unsupervised clustering (K‑Means) for initial user segmentation before supervised forecasting. The finding that Random Forest achieves R²=0.99 on spending‑derived targets supports Odin’s selection of Random Forest for per‑category spending prediction in Module 6.B. The synthetic data approach for handling sparse or missing transaction histories directly informs Odin’s cold‑start strategy for new users without historical data. Although set in India and focused on credit card rewards, the methodological pipeline (clustering → feature engineering → regression) and evaluation metrics are directly transferable to Odin’s Philippine personal budget context.

**Directly justifies:**

- K‑Means clustering can segment users into distinct spending behavior groups using only monthly spend, transaction frequency, and card type, with a silhouette score of 0.42 validating the grouping.  
- Random Forest achieves higher predictive accuracy (R²=0.99, RMSE=14.2) than XGBoost (R²=0.98) for financial outcome prediction from transaction features.  
- Adding user‑specific factors (income category, attrition risk, promotion status) expands reward point distribution from a maximum of 1000 to 3500, enabling finer personalization.  
- Synthetic data generation using correlation‑based feature selection prevents overfitting and maintains model generalizability (R²=0.99 on unseen synthetic test sets).  
- Higher reward multipliers for discretionary categories (e.g., travel +3.0, luxury +2.0) can shift user spending toward high‑margin categories, improving both engagement and profitability.

**Limits of relevance:**

- Geographic context is India, not the Philippines; spending patterns and festival seasons differ, requiring adaptation of category weights.  
- Focus on credit card rewards, not personal budget management; the objective is maximizing discretionary spending, whereas Odin aims to help users stick to budgets.  
- Uses synthetic data for training; real‑world transaction data may contain different noise distributions and missingness patterns.  
- No evaluation of long‑term user retention or real‑world A/B testing; retention claims are derived from clustering logic, not longitudinal user data.  
- Does not address mobile‑first constraints or offline data handling, which are core Odin requirements.

**Mapping Rationale:**

I screened all 10 Odin functional domains. The paper directly supports *financial behavioral profiling* (clustering users by spending habits, card types), *spending forecasting* (ML models predict reward points derived from spending), *expense categorization* (defines luxury/travel/groceries/EMIs categories), *user retention* (explicitly links personalized rewards to loyalty), and *system evaluation* (reports R², RMSE, MAE, silhouette score, DBI). I rejected *budget recommendation* (paper optimizes rewards, not budget allocation), *anomaly detection* (no outlier detection), *mobile‑first design* (not discussed), *data privacy* (none), and *savings/debt* (none). For each selected topic code: 3.A and 3.B because the paper defines a multi‑category expense taxonomy with bonus weights; 5.A, 5.B, 5.C because K‑Means clustering of card types is a direct profiling method, synthetic data addresses cold‑start, and they compare clustering algorithms; 6.A and 6.B because Random Forest and XGBoost are evaluated on predicting reward points (a function of spending); 11.B because the core argument is that personalized rewards increase retention; 12.B because they provide algorithm evaluation metrics. I considered 4.A (landscape of PFMS) but the paper does not survey existing personal finance systems, only credit card reward programs. I considered 7.B (budget recommendation) but the paper does not recommend budgets, only reward point allocations. Borderline case: the paper mentions “real‑time adaptability” in the introduction but does not implement it; I did not select any real‑time topic codes.

## Limitations

- Original dataset lacked user‑level identifiers and had outdated dates (2014–2015); synthetic data may not fully replicate real transaction distributions.  
- Reward point formula values (e.g., +3.0 for travel, –0.5 per additional card) are arbitrary and not derived from industry data [unacknowledged].  
- No validation on real credit card transaction data from Indian banks; all results are on synthetic data.  
- Clustering evaluation used only internal metrics (silhouette, DBI); no external validation against known user labels.  
- Real‑time adaptability claimed but not tested; the models are batch‑trained, not incrementally updated.

## Remember This

- 🔑 **Random Forest achieves R² = 0.99** predicting reward points – top performer over XGBoost (0.98).  
- ⚠️ Synthetic data with 10+ features expands reward range from 1000 to 3500 – more features enable finer personalization.  
- 💡 K‑Means clustering on card types yields silhouette 0.42 – valid segmentation for spending profiles.  
- 📌 Higher rewards for travel (+3.0) and luxury (+2.0) shift spending to high‑margin categories.  
- 🧠 Paper’s formula `ScoredPoints = RCT + CPD + ET + IC + NoC + AR` can be adapted for Odin’s budget recommendation by replacing reward points with budget adjustments.