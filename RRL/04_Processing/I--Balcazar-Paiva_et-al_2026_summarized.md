# Financial Education in the Age of Artificial Intelligence: A Systematic Review, Text Mining, and Natural Language Processing

```yaml
---
paper_id: "10.3390/ijfs14030076"
designation: international
title: "Financial Education in the Age of Artificial Intelligence: A Systematic Review, Text Mining, and Natural Language Processing"
authors: "Balcázar-Paiva, E. S.; Haro-S., A. F.; V.-C., J. A."
year: 2026
venue: "International Journal of Financial Studies"
odin_topics: ["A.1", "H.1"]
shorthand_tags: ["/intelligent-vs-literacy", "/data-sensitivity", "/privacy-by-design"]
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

AI personalizes financial education and boosts short-term comprehension, yet sustained behavioral change remains unproven; privacy and bias are structural conditions for responsible adoption.

## Problem and Motivation

The literature on AI in financial education is fragmented, lacking integrative synthesis and long-term evidence. AI adoption outpaces empirical validation, especially in vulnerable contexts like Latin America.

## Approach

- PRISMA 2020 systematic review covering 2020–2025
- Three databases: Scopus, ScienceDirect, Taylor & Francis (388 initial records → 50 included studies)
- Bibliometric mapping with VOSviewer (keyword co‑occurrence and temporal evolution)
- Sentiment analysis of abstracts using three methods: VADER, TextBlob, and XLM‑RoBERTa transformer
- Combined NLP metrics (sentiment_index, lexical diversity, text_energy) plus descriptive statistics

## Findings

1. Mean sentiment_index = **0.0489** (slightly positive), but transformer‑based neutrality dominates (trf_neu ~0.54)
2. TextBlob polarity trends negative (−0.26), revealing discrepancy: lexicon tools catch caution, transformers catch overall tone
3. Longer abstracts correlate with higher negativity (trf_neg) and lower sentiment_index — length proxies for methodological caveats
4. Greater lexical diversity associates with positive framing and opportunity‑oriented language
5. 50 empirical studies included; no meta‑analysis possible due to heterogeneity

## Key Figures and Tables

- Figure 4: Histogram of sentiment_index → most abstracts cluster near zero (neutral, low affective intensity)
- Figure 5: Correlation matrix → sentiment_index aligns tightly with transformer‑based positivity (trf_pos) and opposes negativity (trf_neg)
- Table 1: Summary statistics → mean word count 218, mean sentence count 9, lexical diversity 0.53

## Key Equations

None.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| AI | Artificial Intelligence — machines performing human‑like cognitive tasks. |
| NLP | Natural Language Processing — teaching computers to understand human language. |
| PRISMA | Preferred Reporting Items for Systematic Reviews and Meta‑Analyses — a standardized reporting guideline. |
| VADER | Valence Aware Dictionary and sEntiment Reasoner — a lexicon‑based sentiment tool (better for English). |
| XLM‑RoBERTa | Multilingual transformer model for sentiment analysis, robust across English and Spanish. |
| SDG | Sustainable Development Goal — UN targets for 2030 (here SDG 4 and SDG 8). |
| Sentiment_index | Continuous measure: P(positive) – P(negative) from transformer, range −1 to +1. |

## Critical Citations

- [Zhu, 2025] — Foundational link between machine learning and financial literacy.
- [Leal & Oliveira, 2024] — Defines hypernudging and adaptive choice architecture in financial AI.
- [Wahyudi et al., 2025] — Documents scarcity of longitudinal studies in AI education research.
- [AL‑Ghuribi et al., 2025] — Emphasizes data privacy and bias as structural conditions.

## Relevance to Odin

**Topics:**

A.1 — Spending and Budgeting Behavior of Filipino Young Professionals

H.1 — Data Privacy, Security, and User Trust in Personal Finance Systems

**Contribution to Odin:**

This systematic review justifies integrating AI into personal finance systems for adaptive, personalized financial education. It provides evidence that AI‑powered nudging and natural language interfaces (e.g., chatbots) can improve short‑term financial comprehension and engagement — directly supporting Odin’s goal of intelligent budgeting assistance. Equally important, the review establishes that data privacy, algorithmic fairness, and transparency are not optional features but structural prerequisites for any AI system handling financial data. These findings inform Odin’s privacy‑by‑design requirements and the need for bias audits in user profiling or recommendation modules.

**Directly justifies:**

- “AI‑based hypernudging can tailor financial advice to individual spending patterns, improving decision‑making without requiring constant user input.”
- “Long‑term behavioral change (e.g., sustained saving) has not been robustly demonstrated; therefore, Odin’s evaluation must include longitudinal metrics, not just short‑term usability.”
- “Privacy and algorithmic bias are structural conditions — Odin must implement explainable models and data‑minimization practices from the start.”
- “The absence of standardized metrics in the literature means Odin should define its own comparable outcome measures for financial literacy and behavior change.”

**Limits of relevance:**

- No Filipino‑specific spending data or cultural validation — findings are general to AI financial education, not localized.
- The review does not address mobile‑first constraints (e.g., on‑device inference, limited bandwidth).
- No empirical comparison of specific algorithms (e.g., LSTM vs. GRU, Isolation Forest vs. autoencoders).
- Sentiment analysis captures discursive tone, not causal effectiveness of AI tools.

## Limitations

- Search restricted to three databases and English/Spanish language — may miss relevant grey literature or other languages.
- No manual reference searching, potentially omitting seminal works outside indexed journals.
- Sentiment analysis tools are calibrated for social media, not academic abstracts; domain shift may affect calibration.
- Lexicon‑based methods (VADER, TextBlob) are less reliable for Spanish texts.
- No meta‑analysis possible due to heterogeneous study designs and missing effect sizes.

## Remember This

- 🔑 **Sentiment_index = +0.049** — slightly positive, but mostly neutral technical tone.
- 💡 Longer abstracts = more caution and negativity (length proxies for risk discussion).
- 📌 **50 studies included** from 388 initial records — large but still fragmented field.
- ⚠️ No sustained behavioral evidence — longitudinal studies are the missing link.
- 🧠 Privacy and bias are structural conditions, not add‑ons — design for them from day one.
