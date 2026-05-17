# Proof of concept of centralized personal finance application

## Metadata

```yaml
---
paper_id: "8a1b2c3d-4e5f-6a7b-8c9d-0e1f2a3b4c5d"
designation: international
title: "Proof of concept of centralized personal finance application"
authors: "Sipilä, M."
year: 2025
venue: "Unknown"
odin_topics: ["4.A", "4.B", "12.A"]
shorthand_tags: ["/pfms-typology", "/pfms-limitations", "/eval-pfms-applied"]
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

The proof-of-concept application consolidated assets, cash flow, and reporting into a single platform, eliminating the stakeholder’s manual, error-prone Excel workflow.

## Problem and Motivation

The stakeholder’s financial tracking relied on fragmented tools (Spendee, multiple Excel sheets, Google Sheets) requiring frequent manual updates and consolidation. This complexity increased error risk and made quarterly reporting time-consuming, reducing trust in financial data. No existing off-the-shelf solution provided centralized asset tracking, automated price updates, and integrated reporting for the stakeholder’s specific needs.

## Approach

- **Methodology:** Design Science Research Methodology (DSRM) with six phases: problem identification, objective definition, design/development, demonstration, evaluation, communication.
- **Stakeholder engagement:** Structured problem-identification questionnaire, iterative feedback during development, task-based testing, and post-evaluation questionnaire.
- **Technologies:** Flutter (cross-platform UI), ASP.NET Core Web API (backend), MongoDB (NoSQL storage), Google Sheets API (share prices), HexaRate API (exchange rates).
- **Core features:** Asset tracking (shares, cash, real estate), categorized cash flow, daily net worth snapshots, PDF report generation, interactive charts/tables.
- **Evaluation methods:** Task-based user testing, stakeholder questionnaire, baseline comparison, analytical review against design objectives.

## Findings

1. All task-based tests (adding transactions, viewing asset distribution, cash flow, report generation) were completed successfully without external guidance.
2. Stakeholder reported **significant reduction in manual work** and elimination of copy-paste errors compared to the baseline system.
3. **100% of “must have” requirements** were achieved; “should have” features (real-time capital, report generation) were delivered; lower-priority items (authentication, customizable dashboards) deferred.
4. The automated PDF report replaced a previously manual, multi-step quarterly process, described as a major efficiency improvement.
5. Stakeholder expressed increased confidence in data accuracy and trust in the system.

## Key Figures and Tables

- Figure 3: Shares in doughnut chart → real-time visual distribution by category.
- Figure 4: Editable asset tables with summary statistics → centralized, sortable view of holdings.
- Figure 5: Net worth over time line chart → historical trend without manual aggregation.
- Figure 7: Multi-layered share pie charts → breakdown by category, country, and subcategory.
- Table 9: Baseline vs. PoC comparison → automation gains across price updates, reporting, and error reduction.

## Key Equations

None.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| DSRM | Design Science Research Methodology [think: six-step structured process for building and evaluating artifacts] |
| PFM | Personal Finance Management — tools and practices for tracking income, expenses, and assets |
| PoC | Proof-of-concept — a working prototype to demonstrate feasibility |
| API | Application Programming Interface — way for software to talk to other services |
| UI/UX | User Interface / User Experience — how the user interacts with and experiences the application |

## Critical Citations

- [Peffers et al., 2007] — Foundational DSRM process model used to structure the entire development.
- [Lusardi & Mitchell, 2014] — Establishes link between financial literacy and positive financial behaviors, motivating the need for PFM tools.
- [Cederberg, 2013] — Identifies user preferences for automated categorization and minimal manual input, directly informing PoC design decisions.
- [Torno et al., 2021] — Taxonomy showing most PFM apps lack educational content and comprehensive integration, justifying the need for a centralized solution.
- [Hevner et al., 2004] — Defines design science evaluation criteria (utility, quality, efficacy) used in the evaluation phase.

## Relevance to Odin

**Topics:**

4.A — Landscape of Existing Personal Finance Systems

4.B — Limitations and Gaps in Existing Systems

12.A — Evaluation Frameworks for Personal Finance Systems

**Contribution to Odin:**

This thesis provides a validated design science process for building a user-centered PFM artifact, directly applicable to Odin’s development methodology. The stakeholder-driven requirement prioritization (MoSCoW) and iterative feedback loops offer a template for Odin’s own requirement gathering and refinement. The evaluation approach—combining task-based testing, structured questionnaires, and baseline comparison—supports Odin’s planned use of ISO 25010 and SUS by demonstrating how qualitative and quantitative feedback can be collected from a real user.

**Directly justifies:**

- “Fragmented tools (spreadsheets + multiple apps) increase manual effort and error risk, reducing user trust in financial data.”
- “Task-based user testing with a single stakeholder successfully identified usability issues (e.g., tooltip clarity, transaction ordering) before full deployment.”
- “Real-time data integration for exchange rates and stock prices reduces manual copy-paste, a key source of error in spreadsheet-based systems.”
- “Automated PDF reporting replaces a multi-step manual process, improving efficiency and consistency without sacrificing detail.”

**Limits of relevance:**

- Study population is a single Finnish stakeholder with high financial literacy, not representative of Filipino young professionals.
- No mobile-first evaluation; the PoC was tested primarily on desktop, while Odin targets mobile-first deployment.
- System lacks user authentication and banking API integration, both outside the PoC scope but central to Odin’s privacy and data handling concerns.
- No budget recommendation, forecasting, or anomaly detection features—Odin’s core ML modules—so this paper does not inform algorithmic choices.

## Limitations

- Authentication and authorization not implemented, limiting real-world security and multi-user testing.
- Banking/broker API integration not achieved; stock prices rely on manual Google Sheets setup, not seamless automation.
- Evaluation based on a single stakeholder; results may not generalize to other users or demographics.
- No performance or scalability testing under load; the architecture is designed for PoC, not production.
- Cash flow feature purpose (detailed budgeting vs. high-level tracking) remained ambiguous to stakeholder—requires clearer design intent. [unacknowledged]

## Remember This

- 🔑 **Centralized dashboard + automated reporting** eliminated manual Excel consolidation and quarterly report assembly.
- 📌 Task-based testing with **100% success** — no guidance needed for asset, cash flow, or report workflows.
- 💡 Stakeholder reported **“significantly reduced manual work”** and higher trust in data accuracy.
- ⚠️ No authentication or banking APIs — PoC assumes single user with manual transaction entry.
- ✅ DSRM process ensured requirements traceability from problem identification through evaluation.
