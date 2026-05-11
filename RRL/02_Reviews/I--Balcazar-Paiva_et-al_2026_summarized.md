# Financial Education in the Age of Artificial Intelligence: A Systematic Review with Text Mining and Natural Language Processing

## Metadata

```yaml
---
paper_id: "10.3390/ijfs14030076"
designation: international
title: "Financial Education in the Age of Artificial Intelligence: A Systematic Review with Text Mining and Natural Language Processing"
authors: "Balcazar-Paiva, E. S.; Haro-Sarango, A. F.; Villanueva-Calderón, J. A."
year: 2026
venue: "International Journal of Financial Studies"
odin_topics: ["A.2", "H.1"]
shorthand_tags: ["/pfms-gap", "/user-trust", "/privacy-by-design"]
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

A systematic review of 50 studies (2020–2025) finds AI in financial education is technically framed with slight optimism but lacks longitudinal evidence and standardized metrics for sustained behavioral change.

## Problem and Motivation

The literature on AI integration in financial education is fragmented, with no integrative synthesis unifying findings on effectiveness or robust theoretical frameworks linking pedagogy to technical capabilities. This fragmentation limits evidence-based policy and tool design. Prior reviews had not systematically analyzed both thematic structure and discursive framing (sentiment) in the same corpus.

## Approach

- PRISMA 2020 systematic review of 388 records from Scopus, ScienceDirect, and Taylor & Francis, narrowed to 50 empirical peer-reviewed studies (2020–2025).
- Bibliometric keyword co-occurrence mapping (VOSviewer) to identify thematic clusters and temporal trends.
- Sentiment analysis on abstracts using three tools: VADER, TextBlob, and a multilingual transformer (XLM-RoBERTa).
- Computed a continuous sentiment_index = P(positive) − P(negative) and text_energy (punctuation + word count).
- Quality appraisal adapted to heterogeneous designs (qualitative, quantitative, mixed).

## Findings

1. AI acts as the central organizing keyword, connecting financial literacy, machine learning, education, and ChatGPT.
2. Temporal analysis shows shift from pandemic-driven digitalization (2020–2022) toward generative AI and conversational systems (2023–2025).
3. **Neutral tone dominates (trf_neu mean = 0.54)** ; sentiment_index averages 0.049 (slight positive tilt), but TextBlob polarity is negative (−0.26), revealing method-dependent divergence.
- Longer abstracts correlate with higher negativity – cautionary language expands with length.
- Higher lexical diversity correlates with positive sentiment indices, suggesting opportunity framing uses richer vocabulary.
- Ethics clusters (privacy, bias, fairness) appear as structural conditions, not peripheral concerns.

## Key Figures and Tables

- Figure 2: Keyword co-occurrence map → AI connects education, finance, health, and generative AI in overlapping clusters.
- Figure 3: Temporal overlay → COVID-19 terms (2020–2022) shift to ChatGPT and large language models (2023–2025).
- Figure 4: Sentiment histogram → most abstracts cluster near zero polarity; neutral tone predominates.
- Table 1: Summary statistics → mean sentiment_index = 0.049, mean trf_neu = 0.539, mean abstract length = 218 words.
- Figure 5: Correlation heatmap → length correlates with negativity; lexical diversity correlates with positivity.

## Key Equations

$$sentiment\_index = P(positive) - P(negative)$$
*Bounded measure from transformer probabilities, ranging approximately −1 to +1.*

$$text\_energy = punctuation\_score + normalized(word\_count)$$
*Proxy for rhetorical intensity combining expressive punctuation and abstract length.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| AI | Artificial Intelligence – technologies performing tasks requiring human-like intelligence. |
| NLP | Natural Language Processing – computational analysis of human language. |
| VADER | Valence Aware Dictionary and sEntiment Reasoner – lexicon-based sentiment tool. [think: scores words as positive/negative/neutral] |
| XLM-RoBERTa | Cross-lingual RoBERTa – multilingual transformer model for sentiment classification. |
| sentiment_index | Continuous measure: positive probability minus negative probability from transformer. |
| Hypernudging | Dynamic, AI-personalized recommendations that reshape choice architecture in real time. |

## Critical Citations

- [Page et al., 2021] – PRISMA 2020 statement; the review's methodological backbone.
- [Leal & Oliveira, 2024] – Defines hypernudging and AI-assisted nudging in financial contexts.
- [Zhu, 2025] – Machine learning for financial literacy detection; cited as evidence of AI's diagnostic potential.
- [Wahyudi et al., 2025] – Flags scarcity of longitudinal studies in the field – a core gap this review confirms.

## Relevance to Odin

**Topics:**

A.2 — Existing Personal Finance and Budget Management Systems

H.1 — Data Privacy, Security, and User Trust in Personal Finance Systems

**Contribution to Odin:**

This systematic review contextualizes the broader AI-in-finance landscape, helping Odin's RRL justify the selection of specific algorithms by showing that the field lacks standardized evaluation metrics and longitudinal evidence – a limitation Odin's evaluation plan (ISO 25010 + SUS) directly addresses. The review's finding that ethics clusters (privacy, bias, fairness) are structural conditions, not add-ons, supports Odin's design decision to prioritize data privacy via manual input only (no banking integration). Although focused on financial education rather than budget management, the paper's discussion of AI-mediated decision-making and user trust (e.g., robo-advisor adoption transparency) informs Odin's approach to user-facing explanations of anomaly detection and budget recommendations.

**Directly justifies:**

- "Systematic reviews of AI in financial domains confirm a persistent lack of standardized metrics and longitudinal designs, limiting claims about sustained behavioral impact."
- "Privacy, fairness, and algorithmic bias are not peripheral ethical concerns but structural conditions for responsible AI deployment in personal finance systems."
- "Transparency is a decisive determinant of user adoption for automated financial tools (robo-advisors), reinforcing Odin's need for explainable anomaly and budget recommendation outputs."
- "The literature's discursive neutral-to-positive framing of AI capabilities does not translate into proven long-term effectiveness – a gap that Odin's module-specific algorithm benchmarking can address."

**Limits of relevance:**

- Paper focuses on financial *education*, not personal budget *management* systems; direct analogies to spending forecasting or anomaly detection are indirect.
- All studies reviewed are international (global) with no Philippine-specific data; cultural spending behaviors and digital readiness differ.
- Sentiment analysis on abstracts captures framing, not causal effectiveness; cannot be cited as evidence that any algorithm works in practice.
- Review excludes grey literature and non-peer-reviewed sources; may miss applied industry insights relevant to PBMS design.

## Limitations

- NLP sentiment pipeline does not measure pedagogical or behavioral effectiveness – it only captures discursive tone of abstracts.
- Search limited to three databases (Scopus, ScienceDirect, Taylor & Francis); no manual reference searching or institutional grey literature.
- Quality appraisal used heterogeneous criteria due to design diversity – no single standardized tool applied across all 50 studies.
- Language bias toward English and Spanish; non-English research may be underrepresented. [unacknowledged]
- Temporal window (2020–2025) captures post-pandemic acceleration but excludes foundational pre-2020 AI finance literature.

## Remember This

- 📌 **50 studies, 388 initial records** – field is fragmented, no meta-analysis possible due to heterogeneity.
- 🔑 Sentiment averages near zero (0.049) – AI in finance research is technically neutral, not boosterist.
- ⚠️ Longer abstracts = more caution – length correlates with negativity, not enthusiasm.
- 💡 Ethics (privacy, bias) are *structural conditions* – not optional add-ons for responsible PBMS design.
- 🧠 No longitudinal evidence for sustained financial behavior change – Odin's evaluation must fill this gap.