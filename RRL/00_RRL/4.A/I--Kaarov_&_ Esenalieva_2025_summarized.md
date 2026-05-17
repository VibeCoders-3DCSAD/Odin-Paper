# Development of a Platform for Financial Data Analysis and Adaptive Personal Finance Management

## Metadata

```yaml
---
paper_id: "10.20944/preprints202504.2615.v1"
designation: international
title: "Development of a Platform for Financial Data Analysis and Adaptive Personal Finance Management"
authors: "Kaarov, A.; Esenalieva, G."
year: 2025
venue: "Preprints.org"
odin_topics: ["3.A", "4.A", "6.A", "7.B", "7.C", "9.A", "10.A", "11.A"]
shorthand_tags: ["/cat-approaches", "/pfms-intelligent-features", "/temporal-dependency", "/budget-rec-approaches", "/budget-rec-evidence", "/budget-rec-formulation", "/mobile-first-def", "/data-sensitivity", "/security-standards", "/entry-friction"]
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

AI-driven personal finance app TYIYN increased average monthly savings by 12–18% and achieved 85% prediction accuracy for overspending using ML-based recommendations and interactive visualizations.

## Problem and Motivation

Existing personal finance tools lack adaptive, AI-driven personalization and real-time guidance, particularly in developing economies. This leads to poor budgeting behavior, low savings, and reactive financial decisions. No prior platform combined real-time AI recommendations, interactive data visualization, and multilingual support to serve underserved, non-English-speaking populations.

## Approach

- **Tech stack:** Flutter (frontend), Django REST Framework (backend API), PostgreSQL (database), Pandas/Matplotlib (data processing/visualization), Celery/Redis (async tasks), Docker (containerization).
- **AI models:** Machine learning for expense categorization, personalized budget recommendations, and cash flow forecasting; natural language processing (NLP) for transaction labeling.
- **Training data:** Models trained on synthetic data and anonymized real financial data, then fine-tuned.
- **Security:** Multi-factor authentication (MFA), token-based authorization, end-to-end encryption, SQL injection/CSRF defenses.
- **Multilingual support:** Kyrgyz, Russian, and English interfaces to reduce language barriers.
- **Testing:** 100 simulated users over three months; iterative usability testing with prototype versions.
- **Manual input only:** Users manually enter transactions; no banking API integration in current version.

## Findings

1. Users following AI recommendations increased average monthly savings by **12–18%** compared to non-users.
2. Predictive engine achieved **85% accuracy** in detecting potential overspending.
3. Expense distribution among test users: rent 35%, food 25%, transport 15%, entertainment 10%, miscellaneous 15%.
4. Over 60% of users disproportionately spent on discretionary/leisure items; less than 40% consistently saved.

- 45% of users reduced discretionary spending after receiving targeted AI reminders and visual recaps.
- 87% of non-English speakers appreciated Russian/Kyrgyz interfaces, improving usability and confidence.
- System maintained API response times under 200ms; security tests found strong resistance to common threats.

## Key Figures and Tables

None.

## Key Equations

None.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| TYIYN | Name of the proposed personal finance app (no expansion given). |
| AI | Artificial intelligence — computer systems that mimic human decision-making. |
| ML | Machine learning — algorithms that learn patterns from data without explicit programming. |
| NLP | Natural language processing — AI that understands and generates human language. |
| API | Application programming interface — a way for software components to communicate. |
| MFA | Multi-factor authentication — login requires two or more verification methods [think: password + phone code]. |
| CSRF | Cross-Site Request Forgery — an attack that tricks a user into executing unwanted actions on a web app. |
| DRF | Django REST Framework — a toolkit for building web APIs in Django. |

## Critical Citations

- [Tversky & Kahneman, 1979] — Prospect Theory explains how users frame financial outcomes, justifying visual framing in budget interfaces.
- [Zhang & Liu, 2020] — Supervised ML for expenditure forecasting provides baseline for TYIYN's predictive approach.
- [Davis, 1989] — Technology Acceptance Model (TAM) links perceived usefulness/ease of use to FinTech adoption.
- [Anderson, 2019] — Security vulnerabilities in consumer finance apps motivate TYIYN's encryption and MFA design.

## Relevance to Odin

**Topics:**

3.A — Expense Categorization Frameworks

4.A — Landscape of Existing Personal Finance Systems

6.A — Predictive Modeling in Personal Finance Systems

7.B — Budget Recommendation in Personal Finance Systems

7.C — Budget Recommendation Algorithm

9.A — Mobile-First Design Principles and Rationale

10.A — Data Privacy and Security in Personal Finance Systems

11.A — Engagement Dynamics in Personal Finance Applications

**Contribution to Odin:**

This paper provides a complete reference architecture for an AI-powered, mobile-first personal finance system that aligns closely with Odin's functional domains. The TYIYN platform's use of ML for expense categorization, budget recommendations, and spending forecasting directly informs Odin's module design choices. The reported 12–18% savings lift from AI recommendations offers a quantifiable performance benchmark for Odin's budget recommendation module, while the 85% overspending prediction accuracy supports the feasibility of Odin's anomaly detection component. The identification of manual transaction entry as a user friction point is directly applicable to Odin's manual-input-only scope, highlighting the need for intuitive entry interfaces.

**Directly justifies:**

- "AI-based budget recommendations increased average monthly savings by 12–18% compared to users who did not follow recommendations (100 users, 3 months)."
- "Machine learning expense categorization revealed typical spending distribution: rent 35%, food 25%, transport 15% — providing baseline category weights for budget allocation algorithms."
- "The predictive engine achieved 85% accuracy in detecting potential overspending, demonstrating that ML can flag anomalies before they occur."
- "Multilingual support improved usability for 87% of non-English speakers, indicating that language accessibility directly drives adoption in linguistically diverse populations."
- "Manual transaction entry was identified as a significant user adoption friction point, confirming that Odin's manual-input-only scope must prioritize low-friction data entry design."

**Limits of relevance:**

- The study was conducted in Kyrgyzstan, not the Philippines; cultural spending patterns and financial behaviors may differ significantly.
- Testing used only 100 simulated users over three months, not a diverse, real-world user population.
- The paper is a non-peer-reviewed preprint; findings should be validated against peer-reviewed sources before strong claims.
- No formal usability evaluation (e.g., SUS) or ISO 25010 quality assessment is reported.
- The app lacks banking API integration (same as Odin), but the paper acknowledges this as a limitation to be addressed, not a design feature.

## Limitations

- Small test sample (100 simulated users) and short duration (3 months) limit generalizability to real-world long-term behavior. [unacknowledged]
- Manual transaction entry was identified as a friction point; the paper acknowledges this and plans automation via open banking APIs.
- Cold-start performance of the recommendation engine required real-world interaction data to improve; no cold-start evaluation metrics are reported.
- No retention or dropout metrics are provided; engagement claims rely on qualitative feedback and dashboard access frequency. [unacknowledged]
- The paper is a non-peer-reviewed preprint; methodology details (e.g., exact ML algorithms, training splits) are sparse.

## Remember This

- 🔑 **12–18% savings increase** — AI budget recommendations directly boost financial outcomes.
- 📌 **85% overspending prediction accuracy** — supports Odin's anomaly detection feasibility.
- ⚠️ Manual entry is a friction point — Odin must design ultra-simple transaction input.
- 💡 87% of non-English speakers preferred native-language UI — language matters for adoption.
- 🔍 100 users, 3 months — small test; real-world replication needed for Odin's context.
