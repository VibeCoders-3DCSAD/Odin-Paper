# Artificial Intelligence Powered Personal Finance Management System

## Metadata

```yaml
---
paper_id: "9e8d7c6b-5a4f-4e3d-8c7b-2a1b3c4d5e6f"
designation: algorithm-specific
title: "Artificial Intelligence Powered Personal Finance Management System"
authors: "Chahar, P.; Vishwakarma, Y. K.; Mishra, R.; Paliwal, G."
year: 2026
venue: "Unknown"
odin_topics: ["3.A", "4.A", "4.B", "6.A", "6.B", "7.B", "7.C", "8.A", "10.A", "10.B", "12.A", "12.B"]
shorthand_tags: ["/cat-approaches", "/pfms-intelligent-features", "/pfms-limitations", "/forecasting-methods-survey", "/forecast-algo-candidates", "/budget-rec-approaches", "/budget-rec-formulation", "/anomaly-behavioral-evidence", "/data-sensitivity", "/privacy-by-design", "/user-trust-behavior", "/eval-ml-design"]
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

An AI-powered personal finance assistant using ML classification, LSTM forecasting, and NLP achieved user satisfaction of **4.4/5** and transaction categorization correctness of **4.2/5** in a prototype survey.

## Problem and Motivation

Existing personal finance tools rely on static budgeting and generic advice, failing to adapt to individual spending patterns. This leads to poor savings, increased debt, and lack of financial preparedness. No prior system integrated dynamic expense classification, predictive forecasting, personalized recommendations, and conversational AI in a single secure platform.

## Approach

- Data collection via secure bank APIs or CSV uploads; preprocessing includes normalization and text cleaning.
- Expense classification using supervised ML: Random Forest, SVM, and LSTM networks with TF‑IDF or word embeddings.
- Predictive analytics module using ARIMA and LSTM time‑series models to forecast future expenses and cash flow.
- Recommendation system combining collaborative filtering and content‑based methods for personalized saving tips and investment advice.
- NLP‑powered chatbot interface for conversational queries and real‑time financial guidance.
- Security layer with end‑to‑end encryption, role‑based access, anonymization, and GDPR compliance.
- Tech stack: React.js frontend, Flask backend with ML integration, MongoDB, Firebase authentication.

## Findings

1. User satisfaction survey yielded an overall rating of **4.4/5** for the AI‑powered system.
2. Ease of use was rated **4.5/5** – the highest among measured attributes.
3. Goal‑setting functionality received **4.3/5** from users.
4. Transaction categorization correctness was rated **4.2/5**, with ambiguity in vendor‑specific transactions identified as a limitation.

- Users requested improved accuracy for variable or non‑recurring expenses (e.g., dining out).
- The system struggled with irregular income streams and unpredictable spending patterns.
- Survey respondents highly valued the ability to customize budgets based on personal spending habits.

## Key Figures and Tables

- Table 1: AI‑powered finance management tools (Mint, YNAB, Digit, Tally) → compares features, AI techniques, strengths, and limitations.
- Figure 6: Distribution of Expenses across Transaction Types → shows relative spending in food, transport, utilities, etc.
- Figure 5: User engagement growth over time → upward trend but no specific growth rate reported.

## Key Equations

None.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| AI | Artificial Intelligence – systems that simulate human intelligence. |
| ML | Machine Learning – algorithms that learn patterns from data without explicit programming. |
| NLP | Natural Language Processing – enabling computers to understand human language. |
| LSTM | Long Short‑Term Memory [think: recurrent network with memory cells that learn what to forget] – a deep learning model for sequential data like transaction histories. |
| SVM | Support Vector Machine – a classifier that finds the best boundary between categories. |
| ARIMA | AutoRegressive Integrated Moving Average – a statistical model for time‑series forecasting. |
| TF‑IDF | Term Frequency–Inverse Document Frequency – a text vectorization method that weights words by importance. |
| GDPR | General Data Protection Regulation – EU privacy law requiring strict data handling. |

## Critical Citations

- [Siami‑Namini et al., 2018] – Benchmarked ARIMA vs. LSTM for time‑series forecasting, foundational for the predictive analytics module.
- [Zhang et al., 2007] – Decision tree SVM hybrid for classification, cited as basis for expense categorization.
- [Galperti, 2019] – Theoretical model of personal budgeting linking consumption‑saving biases to budgeting behavior.

## Relevance to Odin

**Topics:**

3.A — Expense Categorization Frameworks

4.A — Landscape of Existing Personal Finance Systems

4.B — Limitations and Gaps in Existing Systems

6.A — Predictive Modeling in Personal Finance Systems

6.B — Spending Forecasting Algorithm

7.B — Budget Recommendation in Personal Finance Systems

7.C — Budget Recommendation Algorithm

8.A — Anomaly Detection in Personal Finance Systems

10.A — Data Privacy and Security in Personal Finance Systems

10.B — User Trust in Personal Finance Systems

12.A — Evaluation Frameworks for Personal Finance Systems

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This paper directly informs Odin’s algorithm selection for expense classification (SVM, Random Forest, LSTM) and spending forecasting (LSTM over ARIMA for sequential dependencies). The user satisfaction survey (4.4/5 overall) provides a benchmark for Odin’s expected usability outcomes. The identified limitation – systems struggle with irregular income and variable spending – validates Odin’s requirement to incorporate income typology into its behavioral profiling. The security and privacy measures (encryption, anonymization, GDPR compliance) justify Odin’s privacy‑by‑design approach under Philippine law (RA 10173).

**Directly justifies:**

- “User satisfaction survey of an AI‑powered personal finance prototype yielded an overall rating of 4.4/5 and ease‑of‑use rating of 4.5/5.”
- “Transaction categorization correctness was rated 4.2/5 by users, with ambiguous vendor‑specific transactions as the primary error source.”
- “Predictive models (ARIMA, LSTM) enable proactive budget planning but struggle with irregular income streams common in gig economy workers.”
- “End‑to‑end encryption and GDPR‑compliant anonymization are necessary for user trust in AI‑driven financial tools.”
- “NLP chatbot interfaces reduce barriers for users unfamiliar with financial terminology, improving engagement.”

**Limits of relevance:**

- The study population is not Filipino; spending patterns and cultural financial obligations may differ substantially.
- User survey sample size and demographics are not reported, limiting generalizability to Filipino young professionals.
- The system assumes bank API integration; Odin relies on manual transaction input only, which may change user behavior and data completeness.
- No objective algorithmic performance metrics (e.g., MAE, F1) are reported – only subjective user ratings.
- Evaluation does not use ISO 25010 or SUS, the frameworks adopted for Odin.

## Limitations

- Data quality issues (incomplete or inaccurate transaction records) degrade prediction and recommendation accuracy – acknowledged by the authors.
- Model adaptability is poor for users with irregular income or unpredictable spending patterns – acknowledged as a key limitation.
- The paper does not evaluate cold‑start performance (new users with no transaction history). [unacknowledged]
- No comparison of different ML models (e.g., LSTM vs. GRU, Random Forest vs. XGBoost) on the same dataset. [unacknowledged]
- The survey results lack statistical significance testing or confidence intervals. [unacknowledged]

## Remember This

- 🔑 **4.4/5 user satisfaction** – prototype validated, but no objective accuracy numbers reported.
- 📌 **4.2/5 for categorization** – users liked it, but ambiguous transactions remain a problem.
- ⚠️ **Irregular income breaks predictions** – Odin must treat income typology as a first‑class variable.
- 🧠 **Encryption + GDPR = user trust** – privacy‑by‑design is non‑negotiable for financial apps.
- ✅ **LSTM > ARIMA for sequences** – cited benchmark justifies Odin’s forecasting module choice.
