# Optimizing Banking Application Interfaces: A User-Centric Perspective on Consent Management in Digital Banking Environments

## Metadata

```yaml
---
paper_id: "6ba7b810-9dad-51d1-80b4-00c04fd430c8"
designation: international
title: "Optimizing Banking Application Interfaces: A User-Centric Perspective on Consent Management in Digital Banking Environments"
authors: "Pakarinen, O."
year: 2025
venue: "Jyväskylä University of Applied Sciences"
odin_topics: ["B.1", "H.1", "I.1"]
shorthand_tags: ["/mobile-first-def", "/mobile-ux-entry", "/user-trust", "/privacy-by-design", "/value-driven-retention"]
member_checklist:
  - name: "Gabion, Stefanie S."
    status: "[ ]"
  - name: "Guevarra, Joaquin Luis T."
    status: "[x]"
  - name: "San Jose, Alexa Joanne Paula G."
    status: "[ ]"
  - name: "Togle, Charles Nathaniel B."
    status: "[ ]"
---
```

## TL;DR

Two-layer consent management (category overview + detailed permissions) improved user understanding and perceived control over data-sharing decisions in digital banking usability tests.

## Problem and Motivation

Digital banking consent screens rely on long legal text and dense layouts, causing users to skim or ignore information and feel uncertain about their choices. Poor consent design undermines trust and informed decision-making, yet no prior work had systematically tested a layered, user-centered consent interface in banking. Existing solutions prioritize compliance over usability, leaving a gap between legal requirements and actual user comprehension.

## Approach

- Initial exploratory survey (n=6) and literature review to identify consent pain points in banking apps.
- Designed a two-level prototype in Figma: category-based overview (icons, status badges) and detailed permission view per category.
- Built a functional MEAN stack prototype (MongoDB, Express.js, Angular, Node.js) storing auditable consent records.
- Two rounds of usability testing with think-aloud, measuring task completion, hesitation, errors, and semi-structured interviews.
- Iterative improvements after round 1: shortened text, clearer labels, repositioned tooltips, added icons.

## Findings

1. In round 1, users ignored long consent descriptions and struggled to map consent items to categories; **task completion time dropped by an unspecified but notable margin** in round 2 after simplification.
2. Layered structure (overview then detail) helped users orient faster; visual badges (green = all accepted, yellow = partial) improved status recognition.
3. Participants reported higher confidence and perceived control when tooltips were positioned beside relevant options and labels used plain language.

- Icons and short headers reduced cognitive load; users opened tooltips without prompting after repositioning.
- Some terminology (e.g., “Payments” category) remained confusing; final consent overview still needed clearer descriptions.

## Key Figures and Tables

- Figure 6.1: Revolut privacy settings (category-based toggles) → Categorized consent reduces clutter.
- Figure 6.5: Barclays push notification settings → Dense text with limited interaction causes disengagement.
- Figure 7.1: Prototype consent flow diagram → Two-layer structure from snapshot to detailed view.
- Table (implicit in findings): Round 1 vs. round 2 task completion time → Simplification reduced hesitation.

## Key Equations

None.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| Consent management | System for users to accept, decline, and review how their personal data is processed. |
| GDPR | General Data Protection Regulation (EU law) — *requires clear, informed consent.* |
| CCPA | California Consumer Privacy Act (US law) — *similar to GDPR but for California residents.* |
| MEAN stack | MongoDB, Express.js, Angular, Node.js — a full‑JavaScript web development toolkit. |
| Two‑layer consent | Overview screen (categories) + detail screen (individual permissions) — *like a table of contents then pages.* |
| Cognitive load | Mental effort needed to use an interface — *high load = confusion, skimming.* |

## Critical Citations

- [EDPB, 2020] — Defines legal standards for clear, accessible consent interfaces under GDPR.
- [Nouwens et al., 2020] — Demonstrates that dark patterns and dense text undermine informed consent.
- [Kyi et al., 2024] — Shows that long consent blocks lead to disengagement and poor understanding.
- [Montes, 2024] — ING Spain case study: unified consent platform improved user engagement.

## Relevance to Odin

**Topics:**

B.1 — Mobile-First Design in Personal Finance Systems

H.1 — Data Privacy, Security, and User Trust in Personal Finance Systems

I.1 — User Retention and Engagement in Personal Finance Systems

**Contribution to Odin:**

This paper directly informs Odin’s approach to data privacy and user trust by demonstrating that a two‑layer consent interface (category overview + detailed permissions) increases users’ perceived control and confidence. Odin, as a mobile‑first personal budget manager handling sensitive financial data, must present consent choices clearly to avoid user skimming and mistrust. The finding that visual badges (e.g., green/yellow for consent states) and progressive disclosure reduce cognitive load justifies similar design decisions in Odin’s own consent or data‑sharing settings. Although the study focuses on banking, the same user‑centered principles apply to any financial app that requests permission to store or analyze spending data.

**Directly justifies:**

- “Two‑layer consent management (category overview then detailed permissions) improves user confidence and perceived control compared to dense, single‑screen legal text.”
- “Visual status badges (green = all accepted, yellow = partial) help users quickly assess their consent state without reading every item.”
- “Users ignore long consent descriptions; concise, labelled categories with on‑demand tooltips reduce cognitive load and increase engagement.”
- “Usability testing with iterative simplification reduced task completion time and hesitation in consent management flows.”

**Limits of relevance:**

- Study population is not Filipino; banking customer behavior in Finland/Europe may differ from Filipino young professionals.
- Prototype tested in a controlled environment, not a live banking app with real financial consequences.
- No evaluation of long‑term trust or retention effects beyond immediate usability metrics.
- Consent management for data sharing is not identical to Odin’s core budgeting features, but the UI principles transfer.

## Limitations

- Small sample size (n=6 for survey, smaller for each usability round) limits generalizability.
- Tests conducted in a controlled environment, not integrated with a real banking backend. [unacknowledged]
- Prototype simplified many real‑world banking complexities (e.g., third‑party API consent, regulatory audit trails).
- No longitudinal data on whether improved confidence leads to sustained user retention.
- Some technical terms (e.g., “Payments” category) remained confusing even after iteration.

## Remember This

- 🔑 Two‑layer consent (overview + details) cuts cognitive load — users found categories faster and felt more in control.
- 📌 Visual status badges (green ✔ / yellow ⚠️) let users grasp consent state at a glance, no dense text required.
- 💡 Users ignore long legal paragraphs — concise labels + hover tooltips drive actual reading and confidence.
- ⚠️ Findings are from a controlled prototype with small sample; real‑banking integration may reveal new friction points.
