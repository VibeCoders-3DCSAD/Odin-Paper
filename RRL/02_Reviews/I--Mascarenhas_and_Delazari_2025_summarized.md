# WebGIS UFPR CampusMap mobile first proposition

## Metadata

```yaml
---
paper_id: "10.1590/s1982-21702025000100007"
designation: international
title: "WebGIS UFPR CampusMap mobile first proposition"
authors: "Mascarenhas, T. L.; Delazari, L. S."
year: 2025
venue: "Bulletin of Geodetic Sciences"
odin_topics: []
shorthand_tags: []
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

Mobile-first redesign of a university campus WebGIS using iterative requirements engineering and design thinking produced a high-fidelity prototype prioritized for smartphone constraints.

## Problem and Motivation

Existing web-based campus maps designed for desktop devices perform poorly on mobile, frustrating users. Poor mobile UX undermines adoption even though most users access the web via phones. Prior work documented usability issues on the UFPR CampusMap mobile version but no mobile-first redesign had been attempted.

## Approach

- Requirements reuse from prior desktop-focused versions (Lima, 2020; Martins, 2021), filtered for mobile suitability.
- Two brainstorming sessions with seven and two participants (interns, professors, researchers) to elicit needs.
- Proto-personas created from brainstorming outputs to represent internal (frequent) and external (sporadic) users.
- User stories written in "As a ... I want ... so that ..." format, organized by location, search, and route needs.
- Use case diagram identifying three actors: users, registered users, administrators.
- Low-fidelity wireframes (pencil/paper) of four home-screen designs presented to 14 participants via online form (two stages: without and with explanations).
- High-fidelity interactive prototype built in Figma based on the winning wireframe (Prototype 3).

## Findings

- Prototype 3 (search bar prominent at top, action buttons at bottom, map area uncluttered) was preferred in both survey stages, without and with explanations.
- Participants favored familiarity with Google Maps‑style layout, citing ease of use and reduced learning curve.
- Reusing desktop requirements saved time but introduced mobile‑unsuitable features that needed filtering.
- Users proposed features mimicking commercial apps (e.g., Google Maps); expert filtering was required to avoid scope creep.
- Proto‑personas enabled rapid requirement identification but remain hypothesis‑driven without real‑user validation.

## Key Figures and Tables

- Figure 1: Research methodology scheme → three steps: elicitation, specification, validation with iterative feedback.
- Figure 2: Four proto-persona profiles → internal vs. external users with different visit frequencies.
- Figure 3: Use case diagram → actors and their actions (search, locate, route, login, suggest updates).
- Figure 4: Four low-fidelity wireframe proposals → Prototype 3 won for clean map area and familiar layout.
- Figure 5: Hand-drawn wireframe → initial concept for home screen before digital prototyping.
- Figure 6: High-fidelity Figma prototype screens → final interactive design with bottom navigation and search bar.

## Key Equations

None.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| WebGIS | Web‑based Geographic Information System — a map application accessible via browser. |
| Mobile-first | Design strategy that starts with the smallest screen (mobile) then scales up to larger devices. |
| Requirements engineering | Systematic process of capturing what a system must do (functional) and how well (non‑functional). |
| Proto-persona | Fictional user profile created from team knowledge, not from direct user research. |
| Wireframe | Low-fidelity layout sketch showing structure without visual design details. |
| High-fidelity prototype | Interactive, polished simulation that looks and behaves like the final product. |

## Critical Citations

- [Wroblewski, 2011] — Introduced the mobile-first concept with three core rationales (prevalence, screen constraints, device sensors).
- [Roth, 2019] — Defined mobile-first cartographic design in terms of UX optimization for mobile device limitations.
- [Martins, 2021] — Provided prior usability evaluation of UCM on desktop vs. mobile, identifying the gap this paper addresses.

## Relevance to Odin

**Topics:**

None — contextual only.

**Contribution to Odin:**

This paper does not address personal finance systems, AI/ML models for spending, or any of Odin’s five modules. It describes a campus navigation WebGIS with no transferable method or finding for budget management, spending forecasting, anomaly detection, user profiling, or expense categorization.

**Directly justifies:**

None.

**Limits of relevance:**

- Domain is geographic campus navigation, not personal finance or budgeting.
- User population is Brazilian university affiliates, not Filipino young professionals.
- No algorithmic or behavioral findings applicable to spending patterns or financial decision-making.
- No evaluation using ISO 25010 or SUS — only proposed as future work.

## Limitations

- Proto-personas were hypothesis‑driven, not validated with real users through surveys or interviews [unacknowledged].
- Requirements reuse from desktop version risked retaining specifications unsuitable for mobile (e.g., complex geometry tools).
- User feedback uncritically mirrored commercial apps (Google Maps), potentially biasing design toward familiarity rather than domain-specific needs.
- High-fidelity prototype could not simulate all interactions (e.g., zoom, editing tools).
- No usability testing was conducted; the prototype remains unvalidated for effectiveness or efficiency.

## Remember This

- 🔑 Mobile‑first prioritizes constrained screens before scaling up — core to any mobile app design.
- 📌 Prototype 3 won because it looked like Google Maps — users prefer familiar patterns.
- ⚠️ Reusing desktop requirements without filtering adds mobile‑unsuitable features — filter critically.
- 💡 Proto‑personas are fast but not real data — validate with actual users when possible.
- 🔍 Usability testing is the next step — this paper only proposes, not proves, improvement.
