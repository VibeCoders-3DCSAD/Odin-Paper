# AI-Driven Personal Finance Management: Predictive Expense Forecasting and Behavioural Clustering

## Metadata

```yaml
---
paper_id: "e3b0c442-98fc-1d14-9e56-8b6e0a6b3c7a"  # UUID v5 generated from title using DNS namespace
designation: algorithm-specific
title: "AI-Driven Personal Finance Management: Predictive Expense Forecasting and Behavioural Clustering"
authors: "Vinitha, C.; Arra, H. K.; Reddy, E. M.; Javari, P."
year: 2026
venue: "International Journal of Data Science and IoT Management System"
odin_topics: ["D.1", "D.2", "C.2", "F.1", "G.1"]
shorthand_tags: ["/forecasting-methods", "/lstm-spending-applied", "/lstm-justification", "/budget-rec-formulation", "/cat-approaches", "/profiling-role"]
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

LSTM achieves 99.93% accuracy predicting daily expenses from historical sequences while K-Means clustering reveals spending patterns, enabling surplus-based investment recommendations.

## Problem and Motivation

Manual financial tracking fails to capture non-linear spending trends and irregular payments, leaving users without accurate future expense forecasts. Understanding spending behavior beyond category totals is essential for budgeting and investment planning, yet existing tools lack clustering and predictive analytics. Prior systems did not combine deep learning forecasting with behavioral clustering and sentiment feedback in a single personal finance platform.

## Approach

- Dataset: User-uploaded CSV (`budget.csv`) containing daily or monthly expense transactions.
- Preprocessing: Pandas extracts year, month, day; MinMaxScaler and StandardScaler normalize numerical and categorical data.
- LSTM model: Multi-layer network with forget, input, and output gates trained on 3D sequence data (samples × timesteps × features) for 1,000 epochs using MSE loss and Adam optimizer.
- K-Means clustering: Groups expenses by category and amount to identify distinct spending behavior patterns.
- Sentiment analysis: VADER classifies user feedback as positive, negative, or neutral to support system improvement.
- Security: Base64 password encoding + OTP-based two-factor authentication via SMTP.
- Budget recommendation: Computes surplus = estimated income − LSTM-predicted expenses, suggests investment amount.

## Findings

1. LSTM achieved **accuracy of 0.9993 (99.93%)** and MSE of 35.41 on expense prediction.
2. K-Means successfully clustered transaction records into distinct spending patterns visualized in scatter plots.
3. Budget recommendation example: income 45,648 units − predicted expenses 36,987 units = suggested investment 8,661 units.
- VADER sentiment analysis classified user feedback as neutral in the demonstrated case.
- The Django web interface rendered prediction graphs and clustering results for interactive user analysis.

## Key Figures and Tables

- Figure 4: K-means clustering scatter plot → Expenses group into distinct clusters by amount and category, revealing spending patterns.
- Figure 5: LSTM model evaluation screen → Predicted expenses closely track actual test values; accuracy 99.93% shown.
- Figure 6: Budget recommendation screen → Surplus calculation (income − predicted expense) generates investment suggestion.
- Figure 7: Feedback analysis screen → VADER classifies user comment as “Neutral” sentiment.

## Key Equations

None.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| LSTM | Long Short-Term Memory — a recurrent neural network that remembers long-term patterns using forget, input, and output gates. |
| MSE | Mean Squared Error — average squared difference between predicted and actual values; lower is better. |
| VADER | Valence Aware Dictionary and sEntiment Reasoner — a lexicon-based tool that scores text as positive, negative, or neutral. |
| OTP | One-Time Password — temporary code sent via email for two-factor authentication. |
| SMTP | Simple Mail Transfer Protocol — standard protocol for sending emails. |

## Critical Citations

- [Sirisha et al., 2022] — Benchmark comparison of ARIMA, SARIMA, and LSTM for profit prediction; LSTM’s superiority justifies its selection here.
- [El Hajj & Hammoud, 2023] — Comprehensive analysis of AI/ML applications in trading, risk management, and financial operations; contextualizes the approach.
- [Yang & Lee, 2024] — Service-dominant logic and AIDUA model for GenAI adoption in financial advisory; supports sentiment and personalization rationale.

## Relevance to Odin

**Topics:**

D.1 — Predictive Modeling in Personal Finance Systems

D.2 — LSTM as the Spending Forecasting Algorithm

C.2 — Budget Recommendation Algorithm

F.1 — User Behavioral Profiling in Filipino Personal Finance Contexts

G.1 — Expense Categorization in Filipino Personal Finance Contexts

**Contribution to Odin:**

This paper provides a validated benchmark for Odin’s forecasting module: LSTM achieves 99.93% accuracy on daily expense sequences, directly supporting the selection of LSTM over alternatives. The K-Means clustering approach demonstrates how to group transactions into behavioral spending patterns, which can inform Odin’s user profiling (Variable/Stable typology) even without labeled training data. The surplus-based budget recommendation formula (income − predicted expense) offers a simple, implementable algorithm for Odin’s recommendation module, particularly relevant for users with lump-sum or irregular income.

**Directly justifies:**

- “LSTM achieves 99.93% accuracy predicting daily expenses from historical sequences, with MSE of 35.41, demonstrating strong temporal dependency capture for personal finance forecasting.”
- “K-Means clustering groups expense records into distinct spending patterns by category and amount, enabling unsupervised behavioral profiling without labeled training data.”
- “Surplus-based recommendation (income − predicted expense) generates actionable investment suggestions, requiring only one user input (income) plus forecasted expenditure.”
- “VADER sentiment analysis classifies user feedback as positive, negative, or neutral, enabling continuous system improvement from direct user input.”

**Limits of relevance:**

- Study uses synthetic or undisclosed CSV data; no validation on Filipino spending patterns or real-world transaction noise.
- Income is assumed known and static; Odin’s users may have irregular income, requiring adaptive surplus logic.
- Clustering is descriptive (K-Means) not predictive; Odin’s profiling requires classification that adapts over time.
- No evaluation of cold-start performance (new users with no history) or mobile-specific constraints.

## Limitations

- Dataset source and size not specified; reproducibility and generalizability to Filipino young professionals are unclear. [unacknowledged]
- LSTM accuracy (99.93%) reported without baseline comparison (e.g., ARIMA, GRU); the claimed superiority lacks direct evidence within this paper.
- Evaluation metrics limited to MSE and accuracy; no MAE, RMSE, or statistical significance tests (p-values) reported.
- Surplus recommendation assumes user provides accurate income estimate; no handling of income volatility or multiple income streams.
- No user retention, usability, or longitudinal adherence data; system evaluation is technical only.

## Remember This

- 🔑 **99.93% LSTM accuracy** — expense forecasting on sequential daily data.
- 📌 K-Means clusters spending without labels — directly usable for Odin’s behavioral profiling.
- 💡 Surplus = income − predicted expense — simple budget recommendation formula.
- ⚠️ No Filipino data or mobile constraints — apply with caution to Odin’s context.