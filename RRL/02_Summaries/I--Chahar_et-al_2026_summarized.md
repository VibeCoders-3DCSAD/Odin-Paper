# Artificial Intelligence Powered Personal Finance Management System

## Metadata

```yaml
---
paper_id: "8e5b7c9d-4a2f-4b3e-9d1c-2f3a4b5c6d7e"
designation: international
title: "Artificial Intelligence Powered Personal Finance Management System"
authors: "Chahar, P.; Vishwakarma, Y.; Mishra, R.; Paliwal, G."
year: 2026
venue: "Unknown"
odin_topics: ["A.2", "C.1", "C.2", "D.1", "D.2", "E.1", "F.1", "G.1", "H.1", "J.1"]
shorthand_tags: ["/pfms-typology", "/pfms-limitations", "/budget-rec-algorithms", "/forecasting-methods", "/lstm-spending-applied", "/anomaly-approaches", "/cat-approaches", "/security-standards", "/eval-pfms-applied"]
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

AI-powered personal finance assistant with machine learning and NLP achieved 4.4/5 user satisfaction, 4.5/5 ease of use, and 4.2/5 transaction categorization accuracy.

## Problem and Motivation

Existing personal finance tools rely on static budgeting and generic advice, lacking adaptability to individual spending patterns. This leads to poor savings, increased debt, and low financial literacy. No prior system integrated machine learning, natural language processing, and educational content into a unified adaptive assistant.

## Approach

- Data aggregated via bank APIs or manual CSV uploads, then preprocessed (normalization, missing values, text cleaning)
- Expense classification using Random Forest, SVM, and LSTM with TF‑IDF and word embeddings
- Predictive analytics using time series forecasting (ARIMA, LSTM) for future expenses and income
- Recommendation system using collaborative filtering and content‑based methods for personalized saving tips
- NLP chatbot interface for user queries and real‑time financial advice
- Security layer with end‑to‑end encryption, role‑based access, and GDPR compliance
- Web prototype built with React.js, Flask, MongoDB, and Firebase
- Evaluation via user satisfaction survey (no sample size reported)

## Findings

1. Overall user satisfaction scored **4.4/5**.
2. Ease of use scored 4.5/5.
3. Goal‑setting functionality scored 4.3/5.
4. Transaction categorization accuracy scored 4.2/5.

- Users highly valued customizable budgets based on spending habits.
- Classification accuracy suffered for ambiguous or vendor‑specific transactions.
- Spending predictions for variable or non‑recurring expenses (e.g., meals) need improvement.

## Key Figures and Tables

None.

## Key Equations

None.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| AI | Artificial Intelligence — machines simulating human intelligence. |
| ML | Machine Learning — algorithms that learn from data without explicit programming. |
| NLP | Natural Language Processing — enabling computers to understand human language. |
| LSTM | Long Short‑Term Memory [think: remembers patterns over long sequences, forgets irrelevant noise] |
| SVM | Support Vector Machine — a classifier that finds the best boundary between categories. |
| TF‑IDF | Term Frequency‑Inverse Document Frequency — a score that highlights important words in a transaction description. |
| GDPR | General Data Protection Regulation — EU privacy law setting strict data handling rules. |
| API | Application Programming Interface — a way for software to talk to banks automatically. |
| CSV | Comma‑Separated Values — a simple file format for spreadsheets. |
| UI | User Interface — the screen and controls a person interacts with. |
| MAE | Mean Absolute Error — average size of prediction mistakes. |
| F1‑score | A balanced measure of precision and recall, useful for uneven data. |

## Critical Citations

- [Siami‑Namini et al., 2018] — Foundational comparison of ARIMA and LSTM for time series forecasting in finance.
- [Galperti, 2019] — Theoretic model of personal budgeting linking consumption‑saving biases to budgeting strategies.
- [Zhang et al., 2007] — Decision tree SVM method for classification tasks applied to financial data.

## Relevance to Odin

**Topics:**

A.2 — Existing Personal Finance and Budget Management Systems

C.1 — Budgeting Strategies and Budget Recommendation

C.2 — Budget Recommendation Algorithm

D.1 — Predictive Modeling in Personal Finance Systems

D.2 — LSTM as the Spending Forecasting Algorithm

E.1 — Anomaly Detection in Personal Finance Systems

F.1 — User Behavioral Profiling in Filipino Personal Finance Contexts

G.1 — Expense Categorization in Filipino Personal Finance Contexts

H.1 — Data Privacy, Security, and User Trust in Personal Finance Systems

J.1 — System Evaluation

**Contribution to Odin:**

This paper provides a modular AI system design (classification, forecasting, recommendation, NLP) that directly parallels Odin’s five‑module architecture, offering a validated precedent for combining multiple ML techniques in a personal finance app. The user satisfaction results (4.4/5 overall, 4.5/5 ease of use) establish benchmark targets for Odin’s ISO/IEC 25010 and SUS evaluations. The explicit discussion of challenges with irregular income and variable expenses reinforces Odin’s need to handle income volatility common among Filipino young professionals. The paper’s security and privacy layer (encryption, GDPR) justifies Odin’s data protection requirements even without banking integration.

**Directly justifies:**

- “Automated expense classification using Random Forest, SVM, and LSTM achieved user‑rated accuracy of 4.2/5 in a prototype personal finance system.”
- “Predictive analytics for spending forecasting are feasible with time series models (ARIMA, LSTM), but accuracy degrades for users with irregular income patterns.”
- “User satisfaction surveys in AI‑powered PFMS reported ease of use (4.5/5) and goal‑setting functionality (4.3/5) as strong drivers of engagement.”
- “End‑to‑end encryption and role‑based access control are essential security measures for user trust in AI‑driven personal finance tools.”
- “Supervised ML models for expense categorization require large labeled datasets, which may not be available during cold‑start for new users.”

**Limits of relevance:**

- Study population is Indian university‑affiliated, not Filipino young professionals; spending behavior and income typology may differ.
- Evaluation uses subjective satisfaction ratings (4‑point scale) rather than objective metrics like MAE or F1‑score for algorithm performance.
- No comparison against baseline (non‑AI) tools; claims of improvement over static budgeting are unsupported by comparative data.
- Prototype relies on bank API integration; Odin’s manual‑only input model may alter classification and forecasting dynamics.
- Sample size and demographic breakdown of survey participants not reported, limiting generalizability.

## Limitations

- Data quality and completeness directly affect prediction accuracy — a limitation the paper acknowledges.
- Models performed well for stable income but struggled with variable income users [unacknowledged as a limitation in the evaluation section, though mentioned in discussion].
- Survey‑based evaluation lacks objective financial outcome measures (e.g., savings rate increase, debt reduction).
- No longitudinal study; retention and long‑term behavior change not assessed [unacknowledged].
- Security and privacy claims (GDPR compliance, encryption) are design statements, not validated through penetration testing or user trust metrics.

## Remember This

- 🔑 **4.4/5 user satisfaction** — AI personal finance prototype was well‑received overall.
- 📌 Ease of use scored 4.5/5 — simple UI matters more than advanced features.
- ⚠️ Variable income breaks predictions — Odin must address this directly.
- 💡 Customizable budgets (based on spending habits) were users’ favorite feature.
- 🔍 No baseline comparison — the reported 4.2/5 accuracy has no non‑AI control.
