```markdown
# AI-Based Personal Finance Manager (AI)

## Metadata

```yaml
---
paper_id: "f7d8a9b2-3c4e-5f6a-789b-cd0e1f2a3b4c"
designation: international
title: "AI-Based Personal Finance Manager (AI)"
authors: "Sireesha, B.; Kumar, K. K.; Lavanya, O.; Keshan, S.; Ramsai, N.; Kumar, K. L."
year: 2026
venue: "International Journal of AI Electronics and Nexus Energy"
odin_topics: ["A.2", "C.1", "C.2", "D.1", "D.2", "E.1", "E.2", "F.1", "F.2", "G.1", "I.1", "J.1"]
shorthand_tags: ["/budget-rec-algorithms", "/lstm-spending-applied", "/isolation-forest-applied", "/classifier-candidates", "/cat-approaches", "/eval-pfms-applied", "/anomaly-approaches", "/forecasting-methods"]
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

AI-based system combining Random Forest (93–96% accuracy) and LSTM (4.7% MAE) automates expense categorization, forecasting, anomaly detection, and budget recommendations, boosting user financial control.

## Problem and Motivation

Users struggle to monitor spending, manage budgets, and forecast savings due to lack of time, financial literacy, and analytical tools amid growing digital transaction volumes. Traditional finance apps rely on static rules, offering limited personalization and failing to adapt to individual spending patterns. Prior systems lacked an integrated AI framework that combines classification, forecasting, anomaly detection, and adaptive recommendations in a single platform.

## Approach

- Data source: Transaction logs from digital wallets, online banking statements, and user-provided receipts (no public dataset size specified).
- Preprocessing: Data cleaning, normalization, tokenization of merchant names, and mapping to standardized categories.
- Expense classification: Random Forest and Gradient Boosting Machines achieve 93–96% accuracy, outperforming rule-based systems (75–80%).
- Financial forecasting: LSTM network predicts monthly expenditures and recurring payments with 4.7% Mean Absolute Error (MAE).
- Anomaly detection: Isolation Forest flags suspicious transactions with 92% precision.
- User profiling: K-Means clustering identifies spending personas (budget-conscious, impulsive spender, balanced planner).
- Recommendation engine: Hybrid model combining rule-based logic, supervised ML, and reinforcement learning to refine suggestions from user feedback.
- Usability study: 50 participants used the system for one month; post-study surveys measured awareness and savings control.

## Findings

1. Expense classifier achieved **93–96% accuracy** — significantly above rule-based systems (75–80%).
2. LSTM forecasting MAE = 4.7% for monthly expenditure prediction.
3. Anomaly detection precision = 92% for unusual transaction flagging.
4. 84% of users reported better awareness of spending after one month.
5. 78% of users claimed increased control over savings.
- K-Means clustering successfully generated three distinct financial personas.
- Real-time alerts helped users avoid unnecessary spending.
- Younger users benefited more from automated budgeting; older users valued predictive features.

## Key Figures and Tables

None.

## Key Equations

None.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| LSTM | Long Short-Term Memory — a deep learning model that remembers patterns over time [think: memory cell with forget gate]. |
| MAE | Mean Absolute Error — average prediction error in same units as the data. |
| Random Forest | An ensemble of decision trees that votes on the final classification. |
| Isolation Forest | Anomaly detection algorithm that isolates outliers instead of profiling normal points. |
| K-Means | Clustering algorithm that groups users by spending similarity. |
| Reinforcement learning | An AI that learns optimal actions through trial and error from user feedback. |

## Critical Citations

- [Patel & Kumar, 2022] — Foundational AI-driven personal finance automation framework.
- [Chen et al., 2022] — Systematic review of deep learning for financial forecasting.
- [Zhao, 2021] — Established Isolation Forest for financial transaction anomaly detection.
- [Singh & Sharma, 2021] — Prior LSTM application to personal expense prediction.

## Relevance to Odin

**Topics:**

A.2 — Existing Personal Finance and Budget Management Systems

C.1 — Budgeting Strategies and Budget Recommendation

C.2 — Budget Recommendation Algorithm

D.1 — Predictive Modeling in Personal Finance Systems

D.2 — LSTM as the Spending Forecasting Algorithm

E.1 — Anomaly Detection in Personal Finance Systems

E.2 — Anomaly Detection Algorithm

F.1 — User Behavioral Profiling in Filipino Personal Finance Contexts

F.2 — Profile Classification Algorithm

G.1 — Expense Categorization in Filipino Personal Finance Contexts

I.1 — User Retention and Engagement in Personal Finance Systems

J.1 — System Evaluation

**Contribution to Odin:**

This paper validates Odin's proposed algorithm stack by demonstrating that Random Forest achieves 93–96% expense categorization accuracy, directly supporting the choice of supervised ML over rule-based approaches for Odin's categorization module. The LSTM forecasting result (4.7% MAE) provides a performance benchmark for Odin's spending forecasting module, especially for predicting recurring payments like rent and utilities. The use of Isolation Forest for anomaly detection (92% precision) justifies its inclusion in Odin's anomaly detection module, while K-Means clustering for user profiling offers a practical method for Odin's profile classification module. The usability study findings (84% better awareness, 78% increased savings control) show that AI-driven personalization drives engagement — supporting Odin's value-driven retention strategy over gamification.

**Directly justifies:**

- "Random Forest expense classification achieves 93–96% accuracy on personal transaction data, outperforming rule-based systems that plateau at 75–80%."
- "LSTM-based spending forecasting produces a Mean Absolute Error of 4.7% for monthly expenditures and accurately predicts recurring payments such as rent and subscriptions."
- "Isolation Forest detects anomalous financial transactions with 92% precision without requiring labeled training data."
- "K-Means clustering on spending patterns generates three distinct financial personas: budget-conscious, impulsive spender, and balanced planner."
- "Users of an AI-powered personal finance system reported 84% better spending awareness and 78% increased savings control after one month of use."

**Limits of relevance:**

- Study population is Indian, not Filipino; income volatility and cultural spending priorities may differ.
- System assumes banking API integration; Odin uses manual input only, which may affect data completeness and model performance.
- No cold-start evaluation: results assume historical transaction data is available for each user.
- Usability study used only 50 participants over one month, limiting generalizability to long-term retention.
- Paper does not address privacy-preserving techniques like federated learning, which Odin may require.

## Limitations

- Small usability sample size (n=50) and short duration (one month) limit statistical power and longitudinal insight.
- No comparison of different ML algorithms on the same dataset (e.g., LSTM vs. GRU). [unacknowledged]
- Dataset size and composition not disclosed; reproducibility is limited.
- No explicit evaluation of cold-start performance for new users with no transaction history. [unacknowledged]
- Paper does not discuss data privacy or security measures, which are critical for personal finance systems. [unacknowledged]

## Remember This

- 🔑 **93–96% expense classification** — Random Forest beats rule‑based systems by 15+ points.
- 📌 LSTM forecasts spending with **4.7% MAE** — strong baseline for Odin's forecasting module.
- 💡 Isolation Forest hits **92% anomaly precision** — usable without labeled fraud data.
- 📊 K‑Means splits users into 3 personas — profiles drive personalized budget recommendations.
- ⚠️ No cold‑start data — unknown if these results hold for new Odin users with zero history.
```