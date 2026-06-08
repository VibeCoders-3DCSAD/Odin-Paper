# Recommendation system for financial decision-making using Artificial intelligence

## Metadata

```yaml
---
paper_id: "10.15276/aait.07.2024.24"
designation: algorithm-specific
title: "Recommendation system for financial decision-making using Artificial intelligence"
authors: "Shuryhin, K. A.; Zinovatna, S. L."
year: 2024
venue: "Applied Aspects of Information Technology"
odin_topics: ["A.2", "C.1", "C.2", "D.1", "D.2", "E.1", "E.2", "F.1", "H.1"]
shorthand_tags: ["/pfms-typology", "/budget-rec-algorithms", "/budget-rec-formulation", "/spending-time-series", "/lstm-spending-applied", "/anomaly-approaches", "/isolation-forest-applied", "/profiling-role", "/privacy-by-design"]
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

A system that combines Isolation Forest for anomaly detection, ARIMA and LSTM for budget forecasting, and a large language model to generate personalized, ethically-grounded financial recommendations.

## Problem and Motivation

Cognitive biases (loss aversion, framing) cause consumers to make irrational spending decisions, a problem amplified by AI‑driven marketing that can manipulate behavior. Helping users overcome these biases is critical for financial well‑being and autonomy. Prior work lacked an integrated architecture that combines anomaly detection, multi‑horizon forecasting, and LLM‑based personalized advice while explicitly addressing ethical transparency.

## Approach

- Detects atypical expenses using Isolation Forest; anomalies are identified by short path lengths in randomly‑constructed binary trees.
- Forecasts future spending with ARIMA (short‑term, handles seasonality) and LSTM (long‑term, captures extended dependencies).
- Combines ARIMA and LSTM forecasts using a weighted average: `^y_t = α·^y_t(ARIMA) + (1‑α)·^y_t(LSTM)`.
- Feeds transaction history, forecasted expenses, and anomaly information into a large language model (e.g., LLaMa 3.1) to generate personalized financial advice.
- The LLM forms context from user’s financial status, then evaluates recommendations against user‑specific risk level, financial goals, and preferences.
- System architecture event‑driven and modular (AI Module, Budget Module, API Gateway) using AWS SageMaker, OAuth 2.0, and a React.js frontend.

## Findings

- Isolation Forest effectively isolates atypical financial actions by measuring path lengths; shorter paths indicate anomalies.
- ARIMA captures seasonal fluctuations and short‑term dependencies, while LSTM models long‑term dependencies in time series data.
- Combining ARIMA and LSTM via a weighted average improves forecast stability by balancing short‑ and long‑term trends.
- An LLM can integrate anomaly flags and forecasts to produce actionable, non‑judgmental financial advice tailored to income level and goals.
- Ethical design (privacy, fairness, transparency) preserves user autonomy and promotes rational spending without manipulation.

## Key Figures and Tables

- Figure 1: Request diagram to LLM for personalized recommendation → shows input (forecasts, anomalies, goals) and output flow.
- Figure 2: Example LLM response based on context → structured advice with rationale and potential consequences.
- Figure 3: Interaction of AI components within the system → data preprocessing → forecasting/anomaly → LLM → user interface.
- Figure 4: ERD for the recommendation system → entities: users, transactions, budgets, goals, subscriptions, categories.
- Figure 5: Main page of the developed system → dashboard showing budget, transactions, and AI insights.
- Figure 6: Use of AI models for anomaly detection → UI highlighting detected atypical expenses.

## Key Equations

$$E(h(x)) = c(n) + \frac{2\log(n-1) - \frac{2(n-1)}{n}}{n}$$
*Expected path length for Isolation Forest; shorter paths indicate anomalies.*

$$y_t = c + \phi_1 y_{t-1} + \dots + \phi_p y_{t-p} + \theta_1 \epsilon_{t-1} + \dots + \theta_q \epsilon_{t-q} + \epsilon_t$$
*ARIMA(p,d,q) models dependencies on past values and past errors.*

$$f_t = \sigma(W_f \cdot [h_{t-1}, x_t] + b_f)$$
*Forget gate in LSTM – decides what past information to discard.*

$$\hat{y}_t = \alpha \cdot \hat{y}_t^{ARIMA} + (1-\alpha) \cdot \hat{y}_t^{LSTM}$$
*Weighted average combining short‑term (ARIMA) and long‑term (LSTM) forecasts.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| Isolation Forest | Anomaly detection algorithm that isolates outliers by randomly splitting data. |
| ARIMA | AutoRegressive Integrated Moving Average – a time‑series model for short‑term forecasting. |
| LSTM | Long Short‑Term Memory – a recurrent neural network that remembers patterns over long sequences. |
| LLM | Large Language Model – a neural network trained on vast text to generate human‑like advice. |
| Cognitive bias | Systematic pattern of deviation from rational judgment (e.g., loss aversion). |
| Robo‑advisor | Automated software that provides financial advice with minimal human interaction. |

## Critical Citations

- [Lu et al., 2020] – Foundational work on intelligent information systems and recommendation system theory.
- [Milano et al., 2020] – Framework for ethical challenges in recommender systems, used to motivate system transparency.
- [Verma & Sharma, 2020] – Broad overview of AI‑based recommendation systems across domains.
- [Zibriczky, 2016] – Literature review of recommender systems applied to finance, including contextual spending recommendations.

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

H.1 — Data Privacy, Security, and User Trust in Personal Finance Systems

**Contribution to Odin:**

This paper directly validates Odin’s design choice to use Isolation Forest for anomaly detection, as the algorithm requires no labeled training data – a critical advantage for cold‑start users. The hybrid ARIMA+LSTM forecasting approach offers a justified alternative to pure LSTM: ARIMA captures short‑term seasonality (e.g., weekly spending cycles) while LSTM handles irregular long‑term patterns, directly applicable to Odin’s spending forecasting module. The integration of an LLM to generate personalized, non‑judgmental advice informs Odin’s budget recommendation module, particularly the requirement to explain recommendations and respect user autonomy. Finally, the explicit discussion of ethical principles (privacy, fairness, transparency) provides a framework for Odin’s data privacy and user trust requirements, including the use of OAuth 2.0 and privacy‑by‑design.

**Directly justifies:**

- "Isolation Forest detects financial anomalies without requiring labeled training data, making it suitable for cold‑start user profiles where no historical anomaly examples exist."
- "Combining ARIMA (short‑term) and LSTM (long‑term) forecasts via a weighted average captures both seasonal fluctuations and long‑term dependencies, improving forecast stability over either model alone."
- "Large language models can generate personalized financial recommendations by integrating transaction history, forecasted expenses, anomaly flags, and user‑specified risk tolerance and goals."
- "Ethically‑designed recommendation systems must balance AI influence with user autonomy, avoiding manipulation and supporting rational decision‑making through transparent, non‑judgmental advice."
- "OAuth 2.0 and privacy‑by‑design principles (e.g., OWASP Top 10) are essential for securing user financial data and maintaining trust in AI‑powered personal finance systems."

**Limits of relevance:**

- Study is a system design proposal with no empirical evaluation – no accuracy, retention, or usability metrics are reported.
- Population and geography are not specific to the Philippines; spending patterns and financial infrastructure differ.
- The system assumes integration with banking APIs for transaction data; Odin uses manual input only, which may affect data availability and forecast quality.
- The architecture relies on cloud services (AWS SageMaker, SQS) that may not be feasible for a purely mobile‑first, offline‑capable system like Odin.
- No comparison of LLM‑based advice against rule‑based or simpler recommendation methods is provided.

## Limitations

- No quantitative results or user studies; claims are architectural and conceptual, not empirically validated.
- Does not address cold‑start performance for new users with no transaction history. [unacknowledged]
- ARIMA and LSTM combination weight (`α`) is not optimized or evaluated; performance may vary across different spending patterns.
- System assumes continuous cloud connectivity and low‑latency API access, which may not hold for mobile users in all Metro Manila conditions. [unacknowledged]
- Ethical safeguards are described but not implemented or tested for real‑world manipulation resistance.

## Remember This

- 🔑 **Isolation Forest** – no labeled data needed for anomaly detection; ideal for cold‑start Odin users.
- 💡 **ARIMA + LSTM** – hybrid forecast captures both short‑term patterns (ARIMA) and long‑term memory (LSTM) in spending data.
- 📌 **LLM advice** – integrates forecasts + anomalies + user goals to generate personalized, non‑judgmental recommendations.
- ⚠️ **No empirical results** – paper is a design proposal, not a validated system; cite as architecture reference only.
- 🔍 **Ethics by design** – privacy (OAuth 2.0) and user autonomy must be built into any AI financial advisor.
