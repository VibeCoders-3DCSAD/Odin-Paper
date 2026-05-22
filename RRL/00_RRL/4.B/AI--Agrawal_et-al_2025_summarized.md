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
odin_topics: ["4.A", "4.B", "5.A", "5.C", "6.A", "12.B"]
shorthand_tags: ["/pfms-intelligent-features", "/pfms-limitations", "/profiling-role", "/classification-vs-clustering", "/classifier-candidates", "/classifier-eval-metrics", "/forecast-algo-candidates", "/forecast-algo-comparison", "/eval-ml-design"]
member_checklist:
  - name: "Gabion, Stefanie S."
    status: "[ ]"
  - name: "Guevarra, Joaquin Luis T."
    status: "[X]"
  - name: "San Jose, Alexa Joanne Paula G."
    status: "[ ]"
  - name: "Togle, Charles Nathaniel B."
    status: "[ ]"
---
```

## TL;DR

K-Means clustering segments credit card users by card type, and an optimized reward formula achieves **R² = 0.99** in predicting reward points.

## Problem and Motivation

Credit card reward programs in India use static, one-size-fits-all structures that fail to incentivize high-value discretionary spending (luxury, travel) or retain affluent customers. Traditional models lack personalization and real-time adaptability, causing missed engagement opportunities during peak spending seasons. No prior work combined clustering-based user segmentation with a multi‑factor reward formula validated by machine learning regression.

## Approach

- **Original dataset** from Kaggle (83M active cards context) lacked user IDs, outdated dates, and insufficient features.
- **Synthetic dataset** generated with Python’s Faker, adding 15 features: User ID, Card Promotion Date, Expense Type, Income Category, Attrition Risk, etc.
- **Clustering** compared K-Means, DBSCAN, and GMM on 4 card types (Silver, Gold, Platinum, Signature) using monthly spend, transaction frequency, credit utilization.
- **Reward formula** (synthetic): `Scored Points = RCT + CPD + ET + IC + NoC + AR`, then `(Scored Points × Amount Spent)/500`. RCT = card type multiplier (0.5–2.0), ET = expense bonus (0–3.0).
- **Models** Linear Regression, XGBoost, Random Forest predict reward points; evaluation metrics: R², RMSE, MAE.

## Findings

1. **K-Means achieved the highest silhouette score (0.42)** for card‑type based segmentation, outperforming DBSCAN and GMM.
2. **Random Forest achieved R² = 0.99** with lowest RMSE and MAE, beating Linear Regression and XGBoost.
3. Synthetic dataset reward points ranged **0–3500**, whereas original‑dataset‑based rewards capped at 1000.
- Clusters cleanly separated Platinum (high luxury/travel spend) from Silver (low essential spend).
- Expense‑type bonuses (travel +3, luxury +2) drove higher rewards for discretionary categories.
- Card Promotion Date (+2) and Income Category (+1) further personalized allocations.

## Key Figures and Tables

- Figure 2: Original dataset EDA → missing user‑level identifiers and outdated dates limit personalization.
- Figure 3: Synthetic dataset monthly spending trends → festive peaks (Diwali, Christmas) validate seasonal reward targeting.
- Figure 4: Clustering performance scores → K-Means silhouette = 0.42, DB index <1.
- Figure 6: Reward point distribution → synthetic data spreads 0–3500 vs original capped at 1000.
- Figure 8: Model performance comparison → Random Forest R²=0.99, lowest error.

## Key Equations

$$Reward\ Points\ (Synthetic) = \frac{Scored\ Points \times Amount\ Spent}{500}$$
*Total reward points scale linearly with monthly spend after computing scored points from six factors.*

$$Scored\ Points = RCT + CPD + ET + IC + NoC + AR$$
*Each factor (card type, promotion, expense type, income, card count penalty, attrition risk) adds or subtracts points.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| K-Means | Clustering algorithm that groups users into K segments based on spending similarity. |
| Silhouette Score | Metric (−1 to +1) measuring how well a point fits its own cluster vs others; >0.4 indicates meaningful segmentation. |
| Davies-Bouldin Index (DBI) | Lower values mean clusters are compact and well‑separated. |
| R² | Proportion of variance in reward points explained by the model; 0.99 means nearly perfect prediction. |
| RCT | Base multiplier for card type (e.g., Platinum = 2.0, Silver = 0.5). |
| ET | Expense type bonus: travel (+3), luxury (+2), entertainment (+1), groceries/bills (+0.5). |
| Attrition Risk (AR) | Bonus (+1.0) for customers likely to churn, designed to retain them. |

## Critical Citations

- [Cheema & Van der Stede, 2019] — Showed reward programs tailored to luxury/travel spending increase engagement; lacked dynamic adaptation.
- [Li, Ngai, & Hu, 2021] — Surveyed K‑Means, Random Forest, Gradient Boosting for consumer segmentation; static and not real‑time.
- [Gan et al., 2021] — Used XGBoost/LightGBM for high‑value spending prediction; prone to overfitting on high‑dimensional data.
- [Sadat Akash, 2024] — “Credit Card Transaction Dataset” widely used but not aligned with targeted reward structures.

## Relevance to Odin

**Topics:**

4.A — Landscape of Existing Personal Finance Systems

4.B — Limitations and Gaps in Existing Systems

5.A — Financial Behavioral Profiles in Personal Finance

5.C — Financial Behavioral Profile Classification Algorithm

6.A — Predictive Modeling in Personal Finance Systems

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This paper directly justifies Odin’s choice of K‑Means for user segmentation in the financial behavioral profiling module, demonstrating that card‑type (a proxy for spending tier) produces interpretable clusters with silhouette score 0.42. The multi‑factor reward formula (RCT, ET, IC, NoC, AR) provides a template for Odin’s budget recommendation algorithm — weights can be repurposed as budget allocation coefficients. The finding that Random Forest achieves R²=0.99 with low error supports using ensemble regression for any prediction task in Odin (e.g., spending forecasting or reward points). Although the domain is credit card rewards, the method of clustering users based on spending patterns and validating with regression is transferable to cold‑start profile classification.

**Directly justifies:**

- “K‑Means clustering achieves a silhouette score of 0.42 for segmenting users by spending behavior, outperforming DBSCAN and GMM in financial transaction data.”
- “Random Forest regression achieves R²=0.99 for predicting reward points, with lower RMSE and MAE than XGBoost or Linear Regression.”
- “A multi‑factor scoring function (RCT, ET, IC, NoC, AR) personalizes allocations; expense type bonuses (e.g., travel +3) incentivize discretionary spending.”
- “Synthetic data with rich features (income category, attrition risk, card promotion date) yields wider reward distribution (0–3500) than sparse original data (capped at 1000).”

**Limits of relevance:**

- Study uses Indian credit card data; Filipino young professional spending patterns may differ (e.g., lower luxury spend, higher remittance/family obligations).
- Reward optimization domain differs from budget recommendation; the formula weights are suggestive, not directly adoptable without re‑calibration.
- Synthetic dataset (not real transaction logs) limits external validity for real‑world performance.
- No evaluation of temporal drift or seasonal adaptation beyond festive peak observations.

## Limitations

- Original dataset lacked user‑level identifiers and had outdated dates; synthetic generation may not capture real‑world noise. [unacknowledged]
- Clustering was validated only on card type as ground truth; no external behavioral outcome (e.g., retention) measured.
- Reward formula weights (e.g., RCT = 2.0 for Platinum) are arbitrary and not optimized via user feedback.
- Real‑time adaptability claimed but not demonstrated — system still batch‑based.
- No comparison with deep learning or transformer‑based sequence models for spending prediction.

## Remember This

- 🔑 **R² = 0.99** — Random Forest predicts reward points almost perfectly from engineered features.
- 📌 K‑Means silhouette 0.42 beats DBSCAN/GMM — card type is a clean proxy for spending tier.
- 💡 Expense bonuses work: travel +3, luxury +2 drive discretionary spending — apply to Odin’s budget incentives.
- ⚠️ Synthetic data only — real transaction logs may degrade performance; validate before production.
- 🔍 Multi‑factor formula (RCT+ET+IC+NoC+AR) personalizes — a template for Odin’s budget allocation logic.
