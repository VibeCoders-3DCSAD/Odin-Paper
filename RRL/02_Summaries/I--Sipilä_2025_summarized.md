# Proof of concept of centralized personal finance application

## Metadata

```yaml
---
paper_id: "f47ac10b-58cc-4372-a567-0e02b2c3d479"
designation: international
title: "Proof of concept of centralized personal finance application"
authors: "Sipilä, M."
year: 2025
venue: "Master's Thesis, Aalto University"
odin_topics: ["A.2", "J.1"]
shorthand_tags: ["/pfms-typology", "/pfms-features", "/pfms-limitations", "/pfms-gap", "/eval-pfms-applied"]
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

A centralized personal finance PoC reduced manual effort and improved data reliability by automating asset tracking, cash flow visualization, and report generation, validated through task-based testing with a stakeholder.

## Problem and Motivation

Individuals managing finances across spreadsheets, apps, and manual processes face growing complexity and error risk. Fragmented tools reduce data accuracy and discourage consistent financial review. No existing solution consolidated asset tracking, cash flow, and reporting in a single customizable platform.

## Approach

- Used Design Science Research Methodology (DSRM) with six phases: problem identification, objective definition, design, demonstration, evaluation, communication.
- Gathered stakeholder needs via structured questionnaire on current tools, frequency, challenges, and desired features.
- Prioritized requirements using MoSCoW method (Must/Should/Nice/Optional) for functional and non-functional needs.
- Built cross-platform frontend in Flutter, backend API in ASP.NET Core (C#), and MongoDB for flexible data storage.
- Integrated external data: Google Sheets API for stock prices, HexaRate API for daily exchange rates.
- Evaluated via task-based user testing (4 scenarios), stakeholder questionnaire, baseline comparison, and objective achievement review.

## Findings

1. All four test tasks completed successfully without external guidance; task durations 2–5 minutes.
2. Stakeholder reported **significant reduction in manual work** and improved data reliability compared to Excel-based baseline.
3. Automated PDF report generation replaced multi-step manual quarterly reporting.

- Visualizations (pie charts, bar graphs, net worth timeline) were described as clear and informative.
- Partial automation of stock prices and exchange rates reduced copy-paste errors.

## Key Figures and Tables

- Figure 2: High-level system architecture → Three layers: Flutter UI, .NET API, MongoDB with external API integrations.
- Figure 3: Interactive doughnut chart for share distribution → Clear category breakdown at a glance.
- Figure 5: Net worth over time chart → Automatic historical tracking from daily snapshots.
- Figure 9: Cash flow tracking with monthly comparison → Income vs. expenses visualized alongside categorized pie charts.
- Table 9: Baseline vs. PoC comparison → Automation, centralization, and report generation are key gains.

## Key Equations

None.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| PFM | Personal Finance Management — tools for tracking income, expenses, and assets. |
| PoC | Proof-of-concept — a working prototype to demonstrate feasibility. |
| DSRM | Design Science Research Methodology — a six-phase framework for creating and evaluating IT artifacts. |
| FR | Functional Requirement — what the system must do (e.g., generate reports). |
| QA | Quality Attribute — how well the system performs (e.g., response time). |

## Critical Citations

- [Peffers et al., 2007] — Foundational DSRM process model used to structure the entire thesis.
- [Lusardi & Mitchell, 2014] — Establishes financial literacy's role in wealth accumulation and planning.
- [Cederberg, 2013] — Shows that manual data entry reduces PFM adoption; supports automation rationale.
- [Torno et al., 2021] — Taxonomy revealing most PFM apps lack integrated features, justifying a centralized approach.

## Relevance to Odin

**Topics:**

A.2 — Existing Personal Finance and Budget Management Systems

J.1 — System Evaluation

**Contribution to Odin:**

This paper provides a concrete example of designing and evaluating a PFM system using DSRM, directly applicable to Odin’s own development methodology. The evaluation approach — task-based testing with a single stakeholder plus structured questionnaires — offers a low-cost, high-fidelity validation model for Odin’s PoC phase before user recruitment. Although the system lacks AI/ML algorithms, its focus on automation, data integration, and reporting informs Odin’s non‑algorithmic design decisions, such as dashboard layout and report generation.

**Directly justifies:**

- "Task-based user testing with a single stakeholder successfully validated core PFM functionalities, indicating that small-sample qualitative evaluation is feasible for PoC systems."
- "Automated daily exchange rate fetching and stock price retrieval reduced manual update errors in a multi‑currency asset tracking context."
- "Generating PDF reports from aggregated backend data eliminated a multi‑step manual quarterly reporting process, cutting hours of work per cycle."
- "MongoDB’s flexible schema allowed evolving financial data models without schema migrations — a design insight for Odin’s early development."

**Limits of relevance:**

- Single stakeholder (n=1); findings may not generalize to broader Filipino young professional population.
- No ML/AI components; relevance is limited to system design and evaluation methodology, not algorithmic selection.
- European context (Finnish/Swedish financial APIs, multi‑currency needs) differs from Philippine financial infrastructure.
- No user authentication implemented; security claims are untested.

## Limitations

- User authentication and authorization were not implemented, leaving a critical security gap for any multi‑user deployment. [unacknowledged]
- Full banking/broker API integration was infeasible; stock prices still require a manual Google Sheets setup.
- Evaluation involved only one stakeholder; no external users or statistical significance testing.
- Customizable dashboards (a “nice to have” requirement) were omitted, limiting personalization.
- Mobile UI was not optimized despite Flutter’s cross‑platform capability; testing occurred only on desktop/web.

## Remember This

- 🔑 **All test tasks completed successfully** — single‑user qualitative evaluation can validate core PFM workflows.
- 💡 Automated PDF reports replaced hours of manual quarterly consolidation — a direct retention driver.
- ⚠️ No authentication implemented — a showstopper for multi‑user deployment that Odin must avoid.
- 📌 External API integration (exchange rates, stock prices) reduced copy‑paste errors but still required manual ticker maintenance.
- ✅ DSRM’s six‑phase structure provided a clear, iterative roadmap — recommended for Odin’s development.
