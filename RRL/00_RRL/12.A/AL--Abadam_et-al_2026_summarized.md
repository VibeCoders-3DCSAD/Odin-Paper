# Development of A Cross-Platform Application Blue-Collar Marketplace with Prescriptive Analytics Using Linear Programming Algorithm

## Metadata

```yaml
---
paper_id: "10.1145/3796315.3796343"
designation: local
title: "Development of A Cross-Platform Application Blue-Collar Marketplace with Prescriptive Analytics Using Linear Programming Algorithm"
authors: "Abadam, J. B.; Acerado, R.; Cuevas, A. C.; Morco, R."
year: 2026
venue: "International Conference on Software Engineering and Information Management (ICSIM 2026)"
odin_topics: ["9.A", "10.B", "12.A"]
shorthand_tags: ["/mobile-first-def", "/user-trust-behavior", "/iso-25010", "/eval-pfms-applied"]
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

A cross-platform job marketplace with linear programming‑based prescriptive pricing achieved a **4.98/6** ISO 25010 rating, demonstrating effective use of optimization and trust features in a Philippine blue‑collar context.

## Problem and Motivation

Persistent unemployment in the Philippines, especially among low‑income individuals, is compounded by a lack of flexible, trusted, and technology‑driven job platforms for blue‑collar workers. Unemployment drives economic hardship and crime, yet existing government programs offer rigid training instead of immediate work, while commercial platforms from developed economies fail to address local trust and pricing gaps. No prior system combined prescriptive analytics, identity verification, and a cross‑platform design specifically for the Philippine blue‑collar short‑term job market.

## Approach

- Development methodology: Rapid Application Development (RAD) with iterative planning, design, construction, and deployment phases.
- System architecture: Three‑tier (presentation in PHP/JavaScript, logic in Python, data in MySQL) supporting mobile and web.
- Prescriptive analytics: Single‑objective Linear Programming (LP) model that recommends a job price to maximize employer value subject to minimum market price, employer budget, and demand‑based constraints.
- LP solution method: Simplex algorithm, producing a feasible optimal price in Philippine Pesos (PHP).
- Trust features: Government‑ID‑based identity verification and a post‑job rating/review system for freelancers.
- Evaluation: ISO/IEC 25010 quality model focusing on functional suitability, performance efficiency, usability, and reliability, with feedback from IT professionals and regular users.

## Findings

1. Overall ISO/IEC 25010 mean rating was **4.98 out of 6** (interpreted as “Agree”), indicating high user satisfaction.
2. Regular users rated functionality at 5.44/6 (“Strongly Agree”), while IT professionals rated usability at 5.13/6 (“Agree”).
3. Performance efficiency and reliability both scored above 5.1/6 from regular users.
- The LP‑based pricing recommendation successfully generated fair, market‑aligned job prices within employer budgets.
- Identity verification and messaging features were cited as trust‑enhancing by both freelancers and employers.

## Key Figures and Tables

- Figure 2: Administrator dashboard → shows total freelancers, employers, job postings, and service‑category distribution charts.
- Table 2: ISO 25010 evaluation results by respondent group → overall 4.98/6; regular users gave higher functionality (5.44) than IT professionals (5.09).

## Key Equations

$$Maximize\ Z = x$$
*Maximize the recommended job price within all constraints.*

$$x \geq P_{min}$$
*Price must not fall below the minimum acceptable market rate.*

$$x \leq P_{max}$$
*Price cannot exceed the employer’s stated maximum budget.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| LP | Linear Programming – an optimization method that finds the best outcome (e.g., highest price) under linear constraints. |
| RAD | Rapid Application Development – an iterative software development model emphasizing prototyping and fast feedback. |
| PESO | Public Employment Service Office – Philippine government agency that connects job seekers to employers. |
| DOLE | Department of Labor and Employment – Philippine government department overseeing labor programs. |
| GIP | Government Internship Program – DOLE program providing short‑term work experience and stipends. |
| PHP | Philippine Peso – the local currency. |
| ISO/IEC 25010 | International standard for software quality evaluation, covering characteristics like functionality, usability, and reliability. |

## Critical Citations

- [Philippine Statistics Authority, 2023] – Provides baseline unemployment figures (2.04 million unemployed Filipinos as of April 2023).
- [Jawadi et al., 2019] – Establishes the causal link between higher unemployment and increased criminality, motivating trust features.
- [United Nations, 2025] – Defines SDG 8 (Decent Work and Economic Growth), which the platform explicitly aims to support.

## Relevance to Odin

**Topics:**

9.A — Mobile-First Design Principles and Rationale

10.B — User Trust in Personal Finance Systems

12.A — Evaluation Frameworks for Personal Finance Systems

**Contribution to Odin:**

This paper provides a concrete, locally‑implemented example of linear programming applied to a constrained optimization problem in a Philippine digital platform, directly supporting Odin’s budget recommendation module which also uses constraint‑based allocation. The successful deployment of ISO/IEC 25010 as an evaluation framework—achieving a 4.98/6 rating—demonstrates that this quality model is practical and well‑received by both IT professionals and regular users in the Philippine context, justifying its use for Odin. Furthermore, the identity verification and rating system’s positive effect on user trust offers empirical grounding for Odin’s privacy‑by‑design and trust‑building features, despite the domain difference (job marketplace vs. personal finance).

**Directly justifies:**

- “Linear programming can provide optimized, fair recommendations under multiple constraints (minimum price, employer budget, demand ceiling) in a Philippine digital platform context.”
- “ISO/IEC 25010 evaluation of a locally‑developed cross‑platform application produced a 4.98/6 mean rating, confirming the framework’s applicability and user acceptance in the Philippines.”
- “Government‑ID‑based identity verification and post‑transaction rating systems improve perceived trust and reduce informal hiring risks in a two‑sided marketplace.”
- “Rapid Application Development (RAD) with iterative user feedback successfully delivered a functional, usable system for Philippine blue‑collar workers and employers.”

**Limits of relevance:**

- Domain mismatch: job price optimization for a marketplace vs. spending budget allocation for personal finance; the objective (maximize price vs. constrain spending) differs.
- User population: blue‑collar freelancers and employers, not young professionals managing personal budgets.
- LP model is extremely simple (single decision variable, no temporal dynamics) compared to Odin’s per‑category forecasting and reclassification needs.
- Evaluation does not include cold‑start scenarios or longitudinal behavioral drift, which are critical for Odin.

## Limitations

- No statistical test reported for the ISO 25010 ratings (e.g., confidence intervals or p‑values), making the 4.98/6 a descriptive average only.
- Evaluation sample size and demographics are not disclosed, limiting generalizability to Odin’s target population of Filipino young professionals. [unacknowledged]
- The LP model’s single variable (price) ignores multidimensional trade‑offs (e.g., quality, urgency, worker reputation) present in real job matching.
- No comparison with alternative algorithms (e.g., rule‑based, regression, or other optimization methods) to justify LP choice.
- The paper does not evaluate system performance under high concurrency or with sparse user activity (cold‑start), both relevant to Odin’s early adoption phase. [unacknowledged]

## Remember This

- 🔑 **4.98/6 ISO 25010 rating** – LP‑based pricing was well‑accepted by Philippine users.
- 📌 Linear programming solves constrained optimization – directly transferable to Odin’s budget recommendation.
- 💡 Identity verification + ratings build trust – empirical support for Odin’s trust modules.
- ⚠️ Domain differs (job pricing vs. spending) – cite the method, not the objective.
