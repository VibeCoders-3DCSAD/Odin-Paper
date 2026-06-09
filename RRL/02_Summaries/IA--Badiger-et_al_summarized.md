```yaml
paper_id: e5c5f2a3-4b5c-6d7e-8f9a-0b1c2d3e4f5a
designation: algorithm-specific
title: Next.js-Powered AI Platform for Smart Expense Tracking, Budgeting and Insights
authors: Badiger, R.; Robin, R.; Moraas, T.; Naik, V. G.; Karthikeyan, A. N.
year: 0
venue: Unknown
odin_topics:
  - 3.A
  - 3.B
  - 6.A
  - 6.B
  - 7.A
  - 7.B
  - 7.C
  - 8.A
  - 8.B
  - 12.A
  - 12.B
shorthand_tags:
  - /ml-categorization
  - /time-series-forecast
  - /llm-budget-insights
  - /anomaly-detection
  - /system-evaluation
tldr: A Next.js-based AI platform integrates XGBoost transaction categorization, Gemini LLM insights, and Prophet forecasting, achieving 91.3% F1-score and reducing manual effort by 78%.
problem_and_motivation: Digital payment growth in India produces vast personal financial data, but individuals lack effective tools to interpret and act on it. Traditional budgeting methods fail to provide real-time, context-aware insights. Existing AI-driven systems suffer from limited personalization, opaque recommendations, and poor multi-channel support.
approach:
  - System built on Next.js 14 with Clerk authentication, Supabase PostgreSQL, and Prisma ORM.
  - XGBoost classifier maps transactions to 18 categories using merchant, amount, and temporal features.
  - Gemini LLM generates insights via RAG prompting with user spending summaries and anomaly scores.
  - Prophet time-series model forecasts monthly expenses by category with 90% credible intervals.
  - Evaluation on 4,200 transactions achieving 0.913 weighted F1-score and 78% reduction in manual logging effort.
findings:
  - "num: Weighted F1-score of 0.913 across 18 spending categories."
  - "num: Manual expense-logging effort reduced by approximately 78% compared to conventional approaches."
  - High-frequency categories (Food & Dining, Transport, Utilities) achieve F1 above 0.95.
  - 84% of pilot users found AI-generated insights useful or very useful.
  - Server dashboard loads average 420ms, AI insight generation adds 800-1400ms.
key_figures_tables:
  - "Figure 1: End-to-end user workflow of Spend AI → Shows stages from authentication to alerts."
  - "Figure 2: Five-layer system architecture → Presentation, business, AI, data, authentication layers."
  - "Figure 3: Technology stack overview → Next.js, Prisma, Supabase, Clerk, Gemini, XGBoost, Prophet."
  - "Figure 4: AI insight generation pipeline using RAG → Structured prompts with user data to Gemini."
  - "Figure 5: XGBoost transaction categorization F1-scores → Weighted F1=0.913, misc category lower."
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: LLM
    definition: Large language model for text generation.
  - term: UPI
    definition: Unified Payments Interface, India's real-time payment system.
  - term: XGBoost
    definition: Gradient-boosted tree ensemble algorithm.
  - term: RAG
    definition: Retrieval-augmented generation, grounding LLM outputs in retrieved data.
  - term: ORM
    definition: Object-relational mapping for database access.
  - term: RLS
    definition: Row-level security, database-level access control.
critical_citations:
  - "[Hean et al., 2025] — Gemini competitive for personal finance."
  - "[Kotios et al., 2022] — Hybrid deep learning with XAI."
  - "[Pancholi et al., 2026] — Multi-agent AI for personal finance."
  - "[Verma et al., 2024] — Next.js finance tracker without AI."
  - "[Aishwarya and Hemalatha, 2024] — ML expense tracking."
relevance:
  topics:
    - code: 3.A
      name: Expense Categorization Frameworks
      justification: Presents XGBoost-based transaction categorization achieving 91.3% F1.
    - code: 3.B
      name: Expense Category Design Considerations
      justification: Defines 18 spending categories with user override feedback.
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      justification: Uses Prophet time-series for monthly expense forecasting.
    - code: 6.B
      name: Spending Forecasting Algorithm
      justification: Implements Prophet with trend, seasonality, holiday decomposition.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      justification: Provides budget alerts at 80% and 100% thresholds.
    - code: 7.B
      name: Budget Recommendation in Personal Finance Systems
      justification: Gemini LLM generates personalized budget tips.
    - code: 7.C
      name: Budget Recommendation Algorithm
      justification: RAG prompting with user aggregates for budget recommendations.
    - code: 8.A
      name: Anomaly Detection in Personal Finance Systems
      justification: Detects transactions exceeding 2.5 standard deviations.
    - code: 8.B
      name: Anomaly Detection Algorithm
      justification: Statistical anomaly scoring per category.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      justification: Evaluates with F1-score and user feedback (84% useful).
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      justification: Benchmarks XGBoost categorization and system response times.
  contribution: Spend AI contributes an end-to-end AI pipeline combining ML categorization, LLM-generated insights, and time-series forecasting in a production-grade web platform. The system's modular architecture with Next.js Server Actions and Supabase RLS demonstrates how to build secure, scalable personal finance management for multi-channel Indian payment data. The evaluation provides benchmarks for XGBoost categorization (91.3% F1) and user-perceived usefulness of LLM insights, directly informing Odin's expense categorization and budget recommendation modules.
  directly_justifies:
    - XGBoost with temporal features achieves 91.3% weighted F1-score for transaction categorization.
    - LLM-generated insights using RAG are rated useful by 84% of users.
    - Prophet forecasting requires at least 3 months of historical data for reliable predictions.
    - Manual expense-logging effort reduces by 78% compared to conventional methods.
  limits:
    - Cold-start problem: categorization accuracy lower for new users with fewer than 50 transactions.
    - LLM hallucination risk: Gemini may generate imprecise guidance despite RAG.
    - Manual data entry dependency: users may not maintain complete records without banking API.
    - Privacy and regulatory compliance (DPDP Act) require further attention.
    - Forecasting requires at least 3 months of historical data for reliable predictions.
  mapping_rationale: This paper was screened against Odin's functional domains. It directly contributes to Expense Categorization (3.A, 3.B) through its XGBoost classifier and category design. Spending Forecasting (6.A, 6.B) via Prophet time-series model. Budget Recommendation (7.A, 7.B, 7.C) through threshold alerts and Gemini LLM prompts. Anomaly Detection (8.A, 8.B) via statistical outlier detection. System Evaluation (12.A, 12.B) via F1 scores and user feedback. Topics related to behavioral profiling (5.A-C) were rejected as the paper does not model user financial profiles. Mobile-first design (9.A-B) and data privacy (10.A-B) were mentioned but not central contributions. User retention (11.A-B) and savings/debt (13.A-B) are absent. The paper's algorithm-specific nature (XGBoost, Prophet, Gemini) justifies algorithm-specific designation.
limitations:
  - Cold-start problem: categorization accuracy lower for new users with fewer than 50 transactions.
  - LLM hallucination risk: Gemini may generate imprecise guidance despite RAG.
  - Manual data entry dependency: users may not maintain complete records without banking API.
  - Privacy and regulatory compliance (DPDP Act) require further attention.
  - Forecasting requires at least 3 months of historical data for reliable predictions.
remember_this:
  - XGBoost achieves 91.3% F1-score for transaction categorization.
  - LLM insights rated useful by 84% of pilot users.
  - Manual expense logging effort reduced by 78%.
  - Cold-start requires at least 50 transactions for good accuracy.
```