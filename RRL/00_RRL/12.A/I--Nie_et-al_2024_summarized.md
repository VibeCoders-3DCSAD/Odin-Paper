# A Survey of Large Language Models for Financial Applications: Progress, Prospects and Challenges

## Metadata

```yaml
---
paper_id: "f47ac10b-58cc-4372-a567-0e02b2c3d479"
designation: international
title: "A Survey of Large Language Models for Financial Applications: Progress, Prospects and Challenges"
authors: "Nie, Y.; Kong, Y.; Dong, X.; Mulvey, J. M.; Poor, H. V.; Wen, Q.; Zohren, S."
year: 2024
venue: "Unknown"
odin_topics: ["4.A", "5.A", "5.C", "6.A", "6.B", "7.B", "7.C", "8.A", "8.B", "9.A", "10.A", "10.B", "12.A", "12.B"]
shorthand_tags: ["/pfms-intelligent-features", "/profiling-role", "/classifier-candidates", "/forecasting-methods-survey", "/forecast-algo-candidates", "/budget-rec-approaches", "/anomaly-ml-families", "/mobile-forecast-constraints", "/data-sensitivity", "/explainability-trust", "/eval-frameworks-survey"]
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

LLMs excel at financial sentiment analysis, time series forecasting, and reasoning, but face major challenges in data privacy, interpretability, and computational cost.

## Problem and Motivation

No existing survey provides a holistic, application-driven overview of large language models in finance that bridges academic research and practical implementation. Understanding how LLMs transform financial tasks is critical for both researchers building models and practitioners deploying them. Prior surveys focused narrowly on model architectures or technical benchmarks, lacking deep analysis of real-world challenges like lookahead bias, data pollution, and legal responsibility.

## Approach

- Survey of over 200 papers on LLM applications in finance, organized by task category.
- Categorizes applications into: linguistic tasks (summarization, NER), sentiment analysis, financial time series (forecasting, anomaly detection), financial reasoning (planning, recommendation, decision support), and agent-based modeling.
- Reviews financial domain-specific LLMs (FinBERT, BloombergGPT, FinGPT, Llama variants) and adaptation methods (zero-shot, fine-tuning, LoRA, instruction tuning).
- Compares benchmarks and datasets: FLUE, PIXIU, FinQA, FPB, FiQA, and language-specific benchmarks (Chinese, Japanese, Spanish).
- Identifies major challenges: data pollution, signal decay, future lookahead bias, hallucinations, inference speed/cost, uncertainty estimation, interpretability, and ethical issues.

## Findings

1. **GPT-4 achieved near-perfect financial literacy test scores**, outperforming earlier models on complex reasoning tasks (Niszczota and Abbas, 2023).
2. LLM-based stock prediction strategies generated monthly three-factor **alpha up to 3%** using policy news analysis (Lu et al., 2023).
3. Fine-tuned LLMs for SQL query generation from financial questions reached **95% accuracy** in reconciliation tasks (Yadav et al., 2024).
4. GPT-4 significantly outperformed BERT and traditional methods in predicting stock returns from news headlines, with gains largest for smaller stocks (Lopez-Lira and Tang, 2023).

- LLMs enable zero-shot anomaly detection in financial markets using multi-agent frameworks, reducing manual intervention.
- Instruction-tuned models like FinGPT improve numerical sensitivity and contextual understanding in sentiment analysis.

## Key Figures and Tables

- Figure 1: Paper structure overview → maps models, applications, benchmarks, and challenges as an integrated framework.
- Figure 2: Timeline of financial LLMs (2019–2024) → shows rapid proliferation from BERT variants to Llama 3.
- Table 1: Comparison of related surveys → highlights this survey’s unique coverage of applications and challenges.
- Table 2: Benchmarks of LLMs for financial applications → lists 20+ benchmarks with tasks, modalities, and open-source status.
- Figure 4: Categorization of sentiment analysis papers by data source → social media, news, earnings calls, regulatory filings, policy documents.

## Key Equations

None.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| LLM | Large Language Model – a neural network trained on vast text to understand and generate human-like language. |
| FSA | Financial Sentiment Analysis – quantifying emotions (positive/negative) in financial texts to predict market moves. |
| NER | Named Entity Recognition – extracting specific entities like company names, stock symbols, or monetary values from text. |
| ABM | Agent-Based Modeling – simulating autonomous agents whose interactions produce emergent market behaviors. |
| RAG | Retrieval-Augmented Generation – enhancing LLM prompts with external knowledge retrieved from databases. |
| LoRA | Low-Rank Adaptation – efficient fine-tuning method that updates only a small subset of model parameters. |
| Lookahead bias | Using future information unknowingly in backtesting, inflating apparent model performance. |

## Critical Citations

- [Devlin et al., 2018] — BERT introduced bidirectional transformers, foundation for most financial LLMs.
- [Brown et al., 2020] — GPT-3 demonstrated few-shot learning, enabling zero-shot financial reasoning.
- [Araci, 2019] — FinBERT first domain-specific LLM for financial sentiment analysis.
- [Wu et al., 2023] — BloombergGPT showed training on proprietary financial data yields task-specific gains.
- [Yang et al., 2023] — FinGPT pioneered open-source, accessible financial LLM instruction tuning.

## Relevance to Odin

**Topics:**

4.A — Landscape of Existing Personal Finance Systems

5.A — Financial Behavioral Profiles in Personal Finance

5.C — Financial Behavioral Profile Classification Algorithm

6.A — Predictive Modeling in Personal Finance Systems

6.B — Spending Forecasting Algorithm

7.B — Budget Recommendation in Personal Finance Systems

7.C — Budget Recommendation Algorithm

8.A — Anomaly Detection in Personal Finance Systems

8.B — Anomaly Detection Algorithm

9.A — Mobile-First Design Principles and Rationale

10.A — Data Privacy and Security in Personal Finance Systems

10.B — User Trust in Personal Finance Systems

12.A — Evaluation Frameworks for Personal Finance Systems

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This survey directly informs Odin’s algorithm selection across multiple modules by systematically comparing LLM-based approaches for sentiment analysis, time series forecasting, anomaly detection, and reasoning. The documented success of instruction-tuned models like FinGPT in numerical sensitivity and contextual understanding justifies exploring similar fine-tuning for Odin’s transaction categorization and budget recommendation modules. The survey’s detailed discussion of zero-shot vs. fine-tuning tradeoffs, along with inference cost and privacy constraints, provides essential design guidance for Odin’s mobile-first, manual-input architecture where on-device efficiency and data locality are critical.

**Directly justifies:**

- “Instruction-tuned LLMs (e.g., FinGPT) improve numerical sensitivity and contextual understanding in financial sentiment analysis, directly applicable to Odin’s expense categorization from user-entered transaction descriptions.”
- “LLM-based forecasting models using chain-of-thought reasoning achieve explainable stock predictions, supporting Odin’s requirement for transparent spending forecasts.”
- “Zero-shot anomaly detection with LLM-based multi-agent frameworks reduces manual intervention in identifying irregular spending patterns, applicable to Odin’s cold-start user profiles.”
- “Hybrid inference routing (small model for simple queries, large model for complex ones) reduces LLM inference cost by up to 40%, critical for Odin’s mobile deployment without API reliance.”
- “Lookahead bias in financial backtesting can be mitigated using point-in-time training datasets (TimeMachineGPT), a method Odin can adopt when evaluating forecasting module accuracy with historical user data.”

**Limits of relevance:**

- Survey focuses on institutional finance (trading, risk) more than personal budget management; direct transfer of results requires adaptation.
- Most cited studies use high-frequency or API-connected data; Odin’s manual, sparse transaction logs may reduce LLM effectiveness.
- Computational costs of LLMs remain high for pure mobile deployment; edge deployment or small-model distillation is assumed.
- No Philippine-specific financial behavior or cultural spending data is analyzed; applicability to Filipino young professionals requires validation.

## Limitations

- Survey is not systematic; paper selection and categorization may reflect author bias and omit emerging work. [unacknowledged]
- Rapid evolution of LLMs (e.g., Llama 3, GPT-4 Turbo) makes some comparisons outdated by publication time.
- No quantitative meta-analysis or performance ranking across tasks; claims are qualitative or drawn from disparate studies.
- Ignores low-resource language contexts (e.g., Tagalog, mixed English-Filipino code-switching) prevalent in Philippine mobile finance apps. [unacknowledged]
- Does not address manual transaction entry scenarios; all cited work assumes machine-readable or API-accessible data.

## Remember This

- 🔑 **Up to 3% monthly alpha** from LLM-based stock prediction using policy news (Lu et al., 2023).
- 📌 Zero-shot anomaly detection reduces manual review – critical for Odin’s cold-start users.
- 💡 Hybrid inference cuts LLM cost by 40% – essential for mobile-first, no-API design.
- ⚠️ Lookahead bias can be fixed with point-in-time training (TimeMachineGPT) – use for Odin backtesting.
- 🧠 Instruction-tuned FinGPT boosts numerical sensitivity – directly applicable to expense categorization.
