# The Role of Artificial Intelligence in Enhancing Financial Decision-Making and Administrative Efficiency: A Systematic Review

## Metadata

```yaml
---
paper_id: "5f9a8e3c-2b1d-4a7e-9c3d-8f6e2a1b4c7d"
designation: international
title: "The Role of Artificial Intelligence in Enhancing Financial Decision-Making and Administrative Efficiency: A Systematic Review"
authors: "Al-E'mari, S.; Sanjalawe, Y.; Al-E'mari, A."
year: 2025
venue: "Al-Basaer Journal of Business Research"
odin_topics: ["A.2", "D.1", "E.1", "H.1", "J.1"]
shorthand_tags: ["/forecasting-methods", "/anomaly-approaches", "/anomaly-ml-families", "/data-sensitivity", "/security-standards", "/eval-frameworks"]
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

AI enhances financial decision-making through predictive analytics and fraud detection, cutting legal review time by 99% at JPMorgan Chase.

## Problem and Motivation

Despite growing AI adoption in finance and administration, no holistic review exists of comprehensive benefits and challenges across both domains. Understanding systemic impacts matters because fragmented knowledge leads to poor integration strategies and overlooked risks. Prior work lacked thorough examination of ethical, regulatory, and security implications of AI-driven decision-making.

## Approach

- Systematic review of peer-reviewed articles from IEEE Xplore, Scopus, Web of Science, and ScienceDirect (2014–2024)
- Search string combined AI terms with financial decision-making, administrative efficiency, and RPA keywords
- Two independent reviewers screened titles, abstracts, and full texts to minimize selection bias
- Structured evaluation framework used KPIs: time savings, cost reductions, error rates, and decision accuracy
- Case study analysis of real-world implementations including JPMorgan Chase, BlackRock, Ant Financial, UiPath, IBM Watson, and Siemens

## Findings

1. JPMorgan Chase's COiN platform reduced legal document review from 360,000 hours/year to under 1,000 hours — **a 99% reduction saving approximately $100 million annually**
2. BlackRock's Aladdin system achieved 20% improvement in forecasting accuracy and 30% reduction in market reaction time
3. Ant Financial's AI fraud detection improved detection rates by 35% over traditional rule-based systems
4. RPA implementation in healthcare billing achieved 80% reduction in processing time and 60% increase in operational efficiency

- AI-powered inventory management for a regional retailer reduced stockouts by 30% and inventory holding costs by 20%
- Healthcare clinic AI scheduling reduced patient wait times by 40% and increased daily appointment capacity by 15%

## Key Figures and Tables

- Figure 1: Efficiency gains from AI in data reporting → time saved, accuracy, and error reduction metrics improve substantially
- Figure 2: Performance impact of AI on decision-making → extensive AI use correlates 0.61 with speed, 0.48 with decision quality
- Figure 3: Comparison of AI case studies → JPMorgan Chase, BlackRock, and Ant Financial show highest quantitative gains

## Key Equations

*No central equations are presented in this systematic review paper.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| RPA | Robotic Process Automation — software bots that mimic human actions for repetitive tasks like data entry |
| PII | Personally Identifiable Information — data like names, addresses, or IDs that can identify a specific person |
| GDPR | General Data Protection Regulation — EU law requiring transparency and consent for personal data use [mnemonic: strict EU privacy rulebook] |
| KYC | Know Your Customer — verification process financial institutions use to confirm client identities |
| AML | Anti-Money Laundering — procedures to detect and prevent illegally obtained funds moving through financial systems |
| XAI | Explainable AI — techniques that make AI decisions understandable to humans [mnemonic: opens the black box] |

## Critical Citations

- [Huang et al., 2022] — Foundational overview of AI ethics frameworks cited throughout the ethics section
- [Bao, Hilary & Ke, 2022] — Establishes AI's role in fraud detection as a core financial application
- [Schuett, 2023] — Risk management framework for AI adoption referenced in compliance discussion

## Relevance to Odin

**Topics:**

A.2 — Existing Personal Finance and Management Systems

D.1 — Predictive Modeling in Personal Finance Systems

E.1 — Anomaly Detection in Personal Finance Systems

H.1 — Data Privacy, Security, and User Trust in Personal Finance Systems

J.1 — System Evaluation

**Contribution to Odin:**

This systematic review provides high-level justification that AI/ML models (predictive analytics, anomaly detection) are effective in financial contexts, supporting Odin's module-level design choices even without algorithm-specific comparisons. The paper's documented efficiency gains from AI automation (e.g., 99% time reduction) can be cited when arguing that Odin's modules should prioritize automation over manual user configuration. The extensive discussion of data privacy challenges (GDPR, PII protection, encryption requirements) directly informs Odin's privacy-by-design requirements for manual transaction data in the Philippine context. The paper's case study analysis framework (KPIs: time savings, error reduction, accuracy) aligns with Odin's planned ISO 25010 evaluation approach.

**Directly justifies:**

- "AI-powered predictive analytics enables forecasting of financial patterns using historical transaction data, supporting per-category spending prediction in personal budget management systems."
- "Machine learning-based anomaly detection systems identify unusual transaction patterns in real-time, outperforming traditional rule-based fraud detection by 35% in financial applications."
- "RPA implementations in administrative functions achieve 50-60% efficiency gains and 40-80% processing time reductions, justifying automation of routine budgeting tasks."
- "Data privacy regulations like GDPR mandate privacy-by-design, anonymization, and encryption for AI systems handling personal financial information — requirements applicable to Philippine personal finance apps."
- "AI-driven financial decision-making requires transparent, explainable models (XAI) to maintain user trust and regulatory compliance, particularly for credit or budget recommendations."

**Limits of relevance:**

- Paper is a systematic review, not a primary study on specific algorithms (LSTM, Isolation Forest) — provides contextual justification but not comparative benchmarks
- Case studies focus on large enterprises (JPMorgan Chase, BlackRock) with resources far beyond Odin's scope
- Geography is Jordan and international; no Filipino-specific financial behavior data
- Administrative efficiency focus (RPA, HR, scheduling) is only partially relevant to Odin's five financial modules
- No evaluation of cold-start performance for new users with minimal transaction history — a core Odin constraint

## Limitations

- Systematic review aggregates findings from heterogeneous studies with varying methodologies and quality levels [unacknowledged]
- Quantitative metrics (e.g., 20% forecasting improvement) lack standardized measurement definitions across cited papers
- No meta-analysis or statistical pooling of effect sizes — claims are directional, not precisely quantified for Odin's context
- Case study selection may favor successful implementations, introducing publication bias [unacknowledged]
- Paper does not distinguish between AI performance on individual vs. institutional financial data — Odin targets individual Filipino users

## Remember This

- 🔑 **99% time reduction** — JPMorgan Chase cut 360,000 hours of legal review to under 1,000 using AI
- 💡 AI fraud detection beats rules by 35% — direct justification for Odin's anomaly detection module
- ⚠️ No primary LSTM or Isolation Forest data — this is a review paper, not an algorithm benchmark
- 📌 Privacy-by-design is mandatory — GDPR-equivalent requirements apply to Odin's manual transaction data
- ✅ RPA cuts processing time 50-80% — justifies automating budget recalculations and categorization
