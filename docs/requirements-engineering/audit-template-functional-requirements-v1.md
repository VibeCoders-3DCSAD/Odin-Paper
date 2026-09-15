---
type: audit-template
subtype: functional-requirements
title: Functional Requirements Engineering Audit Template
version: 1.0
date: 2026-09-05
status: active
scope: Functional requirements written in the requirements deliverables are checked against Odin's documented feature modules (feature-modules.md).
basis: feature-modules.md
scoring: 100-point weighted checklist
# ---- Fill these per audit run ----
# file_audited: <path or title of the FR document being audited>
# audit_control_number: <ACN-YYYY-NNN>
# audit_date: <YYYY-MM-DD>
# audit_time: <HH:MM>
# auditor: <name>
# result: <pass | fail | conditional>
# score: <0-100>
---

# Functional Requirements Engineering Audit Template

## Instructions

- Audit the **functional requirements document** named in `file_audited`.
- Each Functional Requirement (FR) and its child components must map to a capability, form field, validation rule, state, or message defined in **`features.module.md`**.
- Mark every checklist item `Pass` (P), `Fail` (F), `N/A`, or `Observation` (Obs). An item earns full points at `Pass`; `Fail` earns 0; partial credit is allowed within the item's stated range.
- Record the evidence (the `FRxx` / `FRxx-AAxx` identifier in the audited document and the matching section in `features.module.md`) for each item in the Evidence column.
- Total the awarded points. Maximum is **100**.

## Weighted Sections (total 100)

| Section | Weight |
|---|---|
| A. Completeness / Coverage against feature modules | 30 |
| B. Verifiability & Testability | 15 |
| C. Clarity, Unambiguity & Atomicity | 15 |
| D. Consistency & Traceability | 15 |
| E. Correctness of Rules (validation, states, messages, calculations) | 15 |
| F. Quality Attributes (non-functional coverage as declared) | 10 |
| **Total** | **100** |

---

## A. Completeness / Coverage against feature modules (30 pts)

Every FR must derive from a defined Odin feature-module capability.

| No. | Check                                                                                                                                                                                                                        | Pts    | Doc Evidence | Feature-module Evidence | Score |
| --- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ | ------------ | ----------------------- | ----- |
| A1  | Every functional requirement maps to a feature described in `features.module.md`.                                                                                                                                            | 4      |              |                         |       |
| A2  | All feature modules are represented: Authentication, Onboarding, Dashboard, Accounts, Income Sources, Budgeting, Debt, Savings, Settings, Categories, Obligations, Transactions, Alerts, Forecasting, Reports, Offline Sync. | 4      |              |                         |       |
| A3  | No requirement introduces an out-of-scope capability absent from the feature modules.                                                                                                                                        | 2      |              |                         |       |
| A4  | Every child requirement (FRxx-AAxx) traces to a specific child component of a parent FR.                                                                                                                                     | 3      |              |                         |       |
| A5  | Form fields required by each module (authentication, account, income, budget, debt, savings, obligation, transaction) are all specified.                                                                                     | 3      |              |                         |       |
| A6  | Validation rules for every form and action are specified (required, format, range, match, uniqueness).                                                                                                                       | 3      |              |                         |       |
| A7  | All user-facing states (initial, empty, loading, error, success, offline/stale) are specified.                                                                                                                               | 3      |              |                         |       |
| A8  | All error, validation, notice, confirmation, progress, and success messages are specified.                                                                                                                                   | 3      |              |                         |       |
| A9  | All domain calculations (balance, cash flow, budget health, debt payoff, savings progress, transaction effects) are specified.                                                                                               | 3      |              |                         |       |
| A10 | Cross-module flows (transaction→savings/obligation/debt, credit-card routing, income automation) are specified.                                                                                                              | 2      |              |                         |       |
|     | **Section A total**                                                                                                                                                                                                          | **30** |              |                         |       |

---

## B. Verifiability & Testability (15 pts)

| No. | Check                                                                                                             | Pts    | Evidence | Score |
| --- | ----------------------------------------------------------------------------------------------------------------- | ------ | -------- | ----- |
| B1  | Each requirement states an observable, testable behavior using unambiguous wording (e.g., "the system shall..."). | 3      |          |       |
| B2  | Acceptance criteria or expected outcomes can be derived for each requirement.                                     | 3      |          |       |
| B3  | Numeric values, ranges, and calculations are defined precisely enough to produce deterministic test cases.        | 3      |          |       |
| B4  | Message strings and placeholders are quoted exactly so they can be asserted verbatim in tests.                    | 3      |          |       |
| B5  | States and transitions (e.g., paid, partially paid, overdue, stale) are specific enough to test.                  | 3      |          |       |
|     | **Section B total**                                                                                               | **15** |          |       |

---

## C. Clarity, Unambiguity & Atomicity (15 pts)

| No. | Check                                                                                                       | Pts    | Evidence | Score |
| --- | ----------------------------------------------------------------------------------------------------------- | ------ | -------- | ----- |
| C1  | Each requirement is written in clear, concise language with no undefined domain terms.                      | 3      |          |       |
| C2  | Each requirement expresses a single behavior (atomic), not a list of unrelated behaviors.                   | 3      |          |       |
| C3  | No vague or subjective words (e.g., "fast", "efficient", "user-friendly") that cannot be measured.          | 3      |          |       |
| C4  | Terminology is used consistently across the document (e.g., "account" vs "card", "debt" vs "obligation").   | 3      |          |       |
| C5  | Each requirement is understandable to a developer, QA engineer, and stakeholder without oral clarification. | 3      |          |       |
|     | **Section C total**                                                                                         | **15** |          |       |

---

## D. Consistency & Traceability (15 pts)

| No. | Check                                                                                                                              | Pts    | Evidence | Score |
| --- | ---------------------------------------------------------------------------------------------------------------------------------- | ------ | -------- | ----- |
| D1  | FR identifiers use the `FRxx` / `FRxx-AAxx` format consistently.                                                                   | 3      |          |       |
| D2  | Every FRxx has a summary requirement followed by lettered child components (a, b, c...).                                           | 3      |          |       |
| D3  | No duplicate, contradictory, or overlapping requirements exist.                                                                    | 3      |          |       |
| D4  | Requirements are consistent with other documents (system-spec, PRD, requirements-engineering) and with feature-module definitions. | 3      |          |       |
| D5  | Each requirement maps to a traceability-matrix entry or is traceable to a feature-module capability.                               | 3      |          |       |
|     | **Section D total**                                                                                                                | **15** |          |       |

---

## E. Correctness of Rules (validation, states, messages, calculations) (15 pts)

| No. | Check                                                                                              | Pts    | Evidence | Score |
| --- | -------------------------------------------------------------------------------------------------- | ------ | -------- | ----- |
| E1  | Validation rules match the feature module exactly (required, format, range, matching, uniqueness). | 3      |          |       |
| E2  | Message strings match the feature module verbatim.                                                 | 3      |          |       |
| E3  | State definitions match the feature module (naming and semantics).                                 | 3      |          |       |
| E4  | Calculation rules match the feature module business rules exactly.                                 | 3      |          |       |
| E5  | Empty/error/offline handling is specified for every network-required or data-sourcing action.      | 3      |          |       |
|     | **Section E total**                                                                                | **15** |          |       |

---

## F. Quality Attributes as declared in feature modules (10 pts)

| No. | Check                                                                                                  | Pts    | Evidence | Score |
| --- | ------------------------------------------------------------------------------------------------------ | ------ | -------- | ----- |
| F1  | Offline capability and synchronization requirements are specified.                                     | 2      |          |       |
| F2  | Security (authentication, session, consent, deletion) requirements are specified.                      | 2      |          |       |
| F3  | Privacy and consent (personalization, model training, research evaluation) requirements are specified. | 2      |          |       |
| F4  | Data preservation and audit (archived/deleted/records-preserved) requirements are specified.           | 2      |          |       |
| F5  | Stale-data, cached-data, and freshness requirements are specified.                                     | 2      |          |       |
|     | **Section F total**                                                                                    | **10** |          |       |

---

## Scoring Summary

| Section | Weight | Awarded |
|---|---|---|
| A. Completeness / Coverage | 30 | |
| B. Verifiability & Testability | 15 | |
| C. Clarity, Unambiguity & Atomicity | 15 | |
| D. Consistency & Traceability | 15 | |
| E. Correctness of Rules | 15 | |
| F. Quality Attributes | 10 | |
| **TOTAL** | **100** | |

**Result classification:**
- **Pass:** total ≥ 80
- **Conditional:** total 60–79 (deficiencies must be corrected and re-audited)
- **Fail:** total < 60

---

## Non-Conformance Register

| Item No. | FR Reference | Finding | Severity (Major/Minor/Obs) | Required Correction |
|---|---|---|---|---|
| | | | | |

---

## Audit Sign-off

| Role | Name | Signature | Date |
|---|---|---|---|
| Prepared by (Auditor) | | | |
| Reviewed by (Technical Adviser) | | | |
| Approved by (Project Lead) | | | |
