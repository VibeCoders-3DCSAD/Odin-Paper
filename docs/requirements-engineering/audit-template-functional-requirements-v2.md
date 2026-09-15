---
type: audit-template
subtype: functional-requirements
title: Functional Requirements Engineering Audit Template
version: 1.1
date: 2026-09-05
status: active
scope: Functional requirements in the audited deliverable are checked against the approved feature-module baseline and functional-requirements writing guide.
basis: feature-modules.md
writing_guide: |-
  Rules and Instructions for Creating Functional Requirements, version 1.1  
  audit_target: reqs-eng_v2.md
scoring: 100-point weighted checklist with applicability normalization and mandatory gates
---
# ---- Fill these per audit run ----

# file_audited: <path or title>

# file_audited_baseline: <version, date, or repository commit>

# feature_modules_baseline: <version, date, or repository commit>

# writing_guide_baseline: <version, date, or repository commit>

# audit_control_number: <ACN-YYYY-NNN>

# audit_date: <YYYY-MM-DD>

# audit_time: <HH:MM and time zone>

# auditor: <name>

# result: <pass | conditional | fail | not-completed>

# score: <0-100 or not-calculated>

# implementation_ready: <yes | no | not-assessed>

---

# Functional Requirements Engineering Audit Template

## 1. Purpose

This audit determines whether the generated functional requirements:

- Completely represent the approved, in-scope content of `feature-modules.md`.
- Follow the functional-requirements writing guide.
- Contain no unsupported product behavior.
- Are clear, atomic, consistent, traceable, and independently verifiable.
- Correctly represent fields, placeholders, rules, calculations, states, messages, and interactions.
- Identify missing specifications instead of silently inventing behavior.
- Meet the required document structure and HTML/Joplin format.
- Are sufficiently resolved and approved for implementation.

The audit evaluates both **document conformance** and **specification readiness**. A well-written document may still be unready for implementation because its authoritative source contains unresolved gaps.

A score alone does not establish acceptance. Mandatory gates and unresolved findings also determine the result.

## 2. Required Audit Inputs

|Input|File or reference|Baseline/version|Available?|
|---|---|---|---|
|Functional requirements deliverable||||
|`feature-modules.md`||||
|Functional-requirements writing guide||||
|Applicable approved supporting documents||||
|Traceability register or equivalent embedded mapping||||
|Specification-gap and applicability records||||
|Change history and approval records||||
|Verification/test references, when available||||

### Input rules

- Use `feature-modules.md` consistently; do not substitute an unapproved file or similarly named document.
- Identify the exact baselines being compared.
- Supporting documents are authoritative only within their approved scope.
- Do not assume that a missing register means no gaps, changes, or exceptions exist.
- Registers may be embedded in the deliverable or maintained separately, provided their references are available.
- If a core input cannot be accessed or its baseline cannot be established, mark the audit **Not completed**. Record the limitation and do not issue a final score or Pass result.
- If a required artifact is confirmed absent, rather than merely inaccessible, record a non-conformance.

## 3. Audit Method

### 3.1 Establish the source inventory

Before scoring, identify all approved, in-scope:

- Modules and capabilities.
- Actors and roles.
- Child components.
- Input fields and UI text.
- Business and validation rules.
- States and transitions.
- Calculations and derived values.
- Cross-module and external interactions.
- Functional safeguards and related constraints.

Do not use a hard-coded module list as a substitute for inspecting the approved source.

Any scope exclusion shall have an approval reference. An unapproved omission is not an acceptable exclusion.

### 3.2 Perform bidirectional checks

Check:

1. **Source → requirements:** every source-defined obligation is represented.
2. **Requirements → source:** every normative statement has an approved basis.
3. **Hierarchy:** each detailed statement belongs to a child row, and each child row maps to a lettered parent component.
4. **Requirements → verification:** each detailed statement has an identifiable verification method and objective expected outcome.
5. **Changes → affected artifacts:** approved changes are reflected consistently where applicable.

A full-conformance audit requires complete coverage. Automated checks may assist, but they do not replace semantic review.

A sampled review shall be labeled as limited and shall not be reported as full compliance with this template.

### 3.3 Record evidence

For each checklist item, provide:

- Applicable FR identifiers.
- Detailed-statement identifiers where relevant.
- Source sections or stable source element identifiers.
- Supporting document references, when applicable.
- Finding, gap, applicability, or verification references.
- The basis for any partial score.

Evidence may reference a linked evidence register instead of listing every occurrence in the checklist.

Use the canonical identifiers:

- Parent: `FR01`
- Child row: `FR01-AA01`
- Detailed statement: `FR01-AA01-01`

### 3.4 Distinguish omissions from source gaps

- **Requirement omission:** approved source behavior exists but is absent from the deliverable.
- **Unsupported addition:** the deliverable introduces behavior without an approved source.
- **Source gap:** needed behavior is missing, ambiguous, or contradictory in the source.
- **Applicability decision:** a reviewed case does not apply, with a documented reason.

Correctly recording a source gap satisfies the relevant gap-management check. It does not resolve the missing behavior or establish implementation readiness.

## 4. Status and Scoring Rules

### 4.1 Checklist status

|Status|Meaning|Scoring treatment|
|---|---|---|
|P — Pass|All applicable checks for the item are satisfied.|Full applicable points.|
|F — Fail|One or more applicable checks are not satisfied.|Zero or evidence-based partial points.|
|N/A|The entire item is inapplicable, with an accepted rationale.|Excluded from applicable maximum.|

**Observation (Obs)** is a finding type, not a scoring status. Record observations separately; do not use them to conceal a failed requirement.

### 4.2 Partial credit

Where an item has multiple applicable checks:

> Item score = item weight × passed applicable checks ÷ total applicable checks.

Define and record the checks being counted. For example, the unit may be a field, detailed statement, state transition, or explicit subcriterion.

- Each check is passed or failed; do not assign unsupported subjective percentages.
- If any applicable check fails, the item status is **F**, even when partial points are awarded.
- A partially applicable item retains its weight and is evaluated using its applicable checks.
- Use **N/A** only when the entire item is inapplicable.
- Missing evidence is not N/A.
- Source ambiguity is not N/A.
- Do not change counting units after review merely to improve the score.

Retain calculation precision and round only the final normalized score to two decimal places.

### 4.3 Normalized score

> Final score = 100 × total awarded points ÷ total applicable maximum points.

If all items apply, the applicable maximum is 100.

Record every N/A decision and its rationale. Source coverage, identifiers, traceability, clarity, and required output-format checks are not N/A for a nonempty FR deliverable.

## 5. Weighted Sections

|Section|Weight|
|---|---|
|A. Source Coverage and Scope Fidelity|30|
|B. Verifiability and Testability|15|
|C. Clarity, Atomicity, and Normative Language|15|
|D. Consistency, Structure, and Traceability|15|
|E. Correctness of Specified Behavior|15|
|F. Gap Management, Governance, and Delivery Readiness|10|
|**Total**|**100**|

## A. Source Coverage and Scope Fidelity — 30 Points

Evaluate whether approved source content is represented. Detailed correctness is evaluated in Section E.

|No.|Check|Pts|Status|Document evidence|Source evidence|Score / finding|
|---|---|---|---|---|---|---|
|A1|Every parent, child row, and detailed normative statement has an approved functional basis in `feature-modules.md`, including explicitly approved references incorporated by that source.|4|||||
|A2|Every approved, in-scope module and capability in the source inventory is represented. Exclusions have explicit approval references.|4|||||
|A3|No unsupported capability, UI behavior, safeguard, retry policy, implementation choice, or template-derived default has been introduced as mandatory behavior.|2|||||
|A4|Every child row maps to a specific lettered parent component; every detailed statement belongs to its identified child row; no source-defined child component is omitted.|3|||||
|A5|All source-defined fields are represented, including applicable labels, control types, required/optional status, values, defaults, placeholders, constraints, visibility, and editability.|3|||||
|A6|All source-defined validation rules are represented, including applicable required, format, range, matching, uniqueness, dependency, timing, and blocking rules.|3|||||
|A7|Successful end-to-end flows and all source-defined initial, empty, loading, error, success, offline/stale, blocked, and alternative states are represented.|3|||||
|A8|All source-defined placeholders and user-facing messages are represented, including applicable validation, error, notice, confirmation, progress, empty-state, blocked, network-required, and success text.|3|||||
|A9|All source-defined calculations, derived values, data effects, and recalculation triggers are represented.|3|||||
|A10|All source-defined cross-module and external-system flows are represented, including relevant roles, exchanged information, dependencies, responses, and failure behavior.|2|||||
||**Section A total**|**30**|||||

## B. Verifiability and Testability — 15 Points

|No.|Check|Pts|Status|Evidence|Score / finding|
|---|---|---|---|---|---|
|B1|Every detailed statement specifies an objectively observable behavior or constraint. Necessary actors, preconditions, triggers, and outcomes are explicit or unambiguously referenced.|3||||
|B2|Each detailed statement has an identifiable verification method and objective expected outcome without unstated assumptions. Test or verification references are linked when available; parent summaries are verified through their children.|3||||
|B3|Applicable numeric limits, inclusive/exclusive boundaries, formats, units, currencies, periods, time zones, formulas, precision, and rounding are sufficiently defined for deterministic verification.|3||||
|B4|Exact-text assertions are possible for source-defined messages and placeholders. Dynamic tokens, formatting rules, applicable locales, and approved localized references are identifiable where relevant.|3||||
|B5|States, allowed and prohibited transitions, persistence effects, failure outcomes, and recovery behavior are sufficiently specific to test where applicable. Successful completion can be verified beyond a success message alone.|3||||
||**Section B total**|**15**||||

## C. Clarity, Atomicity, and Normative Language — 15 Points

|No.|Check|Pts|Status|Evidence|Score / finding|
|---|---|---|---|---|---|
|C1|Statements use clear language; necessary domain terms, actors, references, and shared conditions are defined. Pronouns and scope are unambiguous.|3||||
|C2|Each detailed statement expresses one independently verifiable behavior or constraint. Independently testable responses are separated and linked to their common trigger where necessary.|3||||
|C3|No undefined subjective terms, open-ended lists, ambiguous “and/or,” or unclear qualifiers remain in normative statements.|3||||
|C4|Terminology, role names, field names, state names, and module names are consistent with the source and across the deliverable.|3||||
|C5|Mandatory behavior uses “shall.” Recommendations, permissions, rationale, notes, assumptions, and proposals are clearly distinguished from mandatory requirements. The requirements can be understood without oral clarification.|3||||
||**Section C total**|**15**||||

## D. Consistency, Structure, and Traceability — 15 Points

|No.|Check|Pts|Status|Evidence|Score / finding|
|---|---|---|---|---|---|
|D1|Identifiers use the canonical `FR01`, `FR01-AA01`, and `FR01-AA01-01` formats; are unique; and remain stable across available revisions. Retired identifiers are not reassigned to unrelated requirements.|3||||
|D2|Requirements are grouped by module. Each parent contains one summary followed by lettered components. Child rows appear separately in the same table. Every detailed normative statement has a stable identifier. Source references and notes are outside numbered normative statements.|3||||
|D3|No duplicate obligations, contradictory statements, or ambiguous overlaps exist. Parent summaries aggregate child obligations rather than creating independent duplicate acceptance obligations.|3||||
|D4|Requirements are consistent with source definitions and applicable approved supporting documents. Source conflicts and related interface or non-functional obligations are explicitly resolved or tracked; interface contracts are referenced rather than inconsistently duplicated.|3||||
|D5|Bidirectional source-to-requirement traceability is demonstrable. Parent and child rows contain explicit source references; statement-specific references exist when row-level references do not identify the basis adequately.|3||||
||**Section D total**|**15**||||

## E. Correctness of Specified Behavior — 15 Points

Evaluate source-defined behavior and identify relevant unresolved gaps. Do not award correctness credit for invented behavior.

|No.|Check|Pts|Status|Evidence|Score / finding|
|---|---|---|---|---|---|
|E1|Field and validation behavior matches the source: labels, control types, required/optional status, allowed values, defaults, boundaries, whitespace/case/null handling, uniqueness, dependencies, timing, blocking, input preservation/clearing, and feedback removal where defined. Placeholders are not treated as substitutes for labels or accessible names.|3||||
|E2|Rendered placeholders and messages match approved source text verbatim, including capitalization, punctuation, spacing, and symbols. Dynamic patterns and locale-specific text match their approved definitions. No unsupported messages or translations are added.|3||||
|E3|State names, semantics, transitions, actor permissions, successful outcomes, persisted changes, unchanged data, partial completion, duplicate effects, concurrent-update handling, and related-module visibility match the source where defined.|3||||
|E4|Formulas, input sources, units, currencies, dates, periods, precision, rounding, exceptional-input handling, recalculation triggers, and displayed/stored results match the source. Examples do not replace or contradict general rules.|3||||
|E5|Applicable empty, loading, service-failure, timeout, offline, cached/stale, blocked, cancellation, retry, recovery, and destructive-action handling matches the source. Cross-module and external interactions preserve defined sequencing, data exchange, responses, and failure behavior. No unsupported safeguard or connectivity assumption is imposed.|3||||
||**Section E total**|**15**||||

## F. Gap Management, Governance, and Delivery Readiness — 10 Points

|No.|Check|Pts|Status|Evidence|Score / finding|
|---|---|---|---|---|---|
|F1|Each capability has a documented applicability assessment covering relevant happy-path, alternative, boundary, empty, loading, failure, offline/stale, authorization, duplicate/concurrent, cancellation/recovery, and destructive-action cases. Each case is Specified, N/A with rationale, or Gap.|2||||
|F2|Missing, ambiguous, contradictory, or insufficient specifications are recorded with source references, affected FRs, owner, status, and resolution where available. TBD/TBC are used appropriately; assumptions and proposals are not presented as approved behavior.|2||||
|F3|Source and deliverable baselines are recorded. Applicable changes have reasons, decisions, approvals, impact assessments, and consistent updates to affected sources, FRs, interfaces, messages, tests, and data-related behavior. Retired requirements remain traceable.|2||||
|F4|Related functional and non-functional obligations are correctly classified and cross-referenced without omission. Feasibility concerns and required stakeholder reviews are recorded. Implementation readiness is not asserted while critical gaps or required approvals remain unresolved.|2||||
|F5|Every module/feature table uses the required HTML/Joplin wrapper, required columns, and one continuous block with no line breaks inside the wrapper. HTML encoding preserves exact rendered text. No unresolved template placeholders remain in content marked approved.|2||||
||**Section F total**|**10**||||

## 6. Mandatory Acceptance Gates

Evaluate these separately from the weighted score.

|Gate|Mandatory condition|Status: Met / Not met / Not assessed|Evidence / finding|
|---|---|---|---|
|G1 — Auditable baseline|Core inputs are accessible and their approved baselines are identifiable.|||
|G2 — Scope fidelity|No unresolved unsupported mandatory behavior or unapproved scope exclusion remains.|||
|G3 — Essential coverage|No unresolved major omission or contradiction affects a source-defined capability, successful flow, or applicable failure behavior.|||
|G4 — Critical correctness|No unresolved critical defect affects permissions, destructive actions, data integrity, or business-rule/calculation outcomes.|||
|G5 — Readiness integrity|No critical source gap or unapproved assumption remains in requirements claimed to be implementation-ready.|||
|G6 — Deliverable integrity|Required identifier hierarchy, independent statement references, and HTML/Joplin output structure are satisfied.|||
|G7 — Review and approval|Reviews and approvals required for the declared lifecycle stage are recorded.|||

Rules:

- Any gate marked **Not met** prevents a Pass result.
- An inability to assess a gate because evidence is inaccessible prevents a completed acceptance decision.
- Missing required artifacts or confirmed unmet obligations are findings, not merely “Not assessed.”
- Critical or major findings result in **Fail**, regardless of numeric score.
- Gate failures involving only minor corrections may result in **Conditional**, subject to the result rules below.

## 7. Source Coverage and Traceability Register

Use this register or an equivalent linked artifact.

|Source baseline and element|Capability / obligation|Parent ID|Child ID|Statement ID(s)|Verification method/reference|Coverage status|Gap/finding|
|---|---|---|---|---|---|---|---|
|||||||||

Coverage status:

- **Covered**
- **Partially covered**
- **Missing**
- **Approved exclusion**

For unsupported requirement statements, record the FR identifiers in the non-conformance register because no valid source element exists.

## 8. Capability and State Applicability Register

Create entries for each relevant capability and assessed case.

|Capability / source reference|Case assessed|Classification: Specified / N/A / Gap|FR statement(s)|Rationale or gap reference|
|---|---|---|---|---|
||Successful flow||||
||Initial/default state||||
||Missing/invalid/boundary input||||
||Empty result||||
||Loading/in-progress||||
||Service failure/timeout||||
||Offline/cached/stale data||||
||Unauthenticated/unauthorized access||||
||Blocked/unavailable action||||
||Duplicate submission||||
||Concurrent/conflicting update||||
||Cancellation/retry/recovery||||
||Destructive/irreversible action||||

An N/A rationale shall explain why the case does not apply. “Not mentioned in the source” is not, by itself, an adequate rationale.

## 9. Specification-Gap Register

Source gaps and requirement defects shall remain distinguishable, even if tracked in one system.

|Gap ID|Source reference|Missing/ambiguous/conflicting specification|Affected FRs|Criticality|Owner|Status|Resolution and approval|
|---|---|---|---|---|---|---|---|
|||||||||

A gap may be correctly documented while still blocking implementation readiness.

Do not resolve a gap by silently adding assumed behavior to the audited document.

## 10. Non-Conformance and Observation Register

### Severity definitions

|Severity|Definition|
|---|---|
|Critical|A defect or unresolved issue could cause unauthorized access, irreversible unintended data loss, materially incorrect business outcomes, or similarly severe consequences.|
|Major|A substantive obligation is missing, unsupported, contradictory, untestable, or insufficiently traceable, preventing reliable implementation or verification of the affected behavior.|
|Minor|A localized conformance defect does not materially alter behavior or prevent reliable implementation and testing.|
|Observation|An improvement opportunity with no demonstrated violation of an applicable obligation.|

Severity shall reflect impact, not merely the number of affected rows.

|Finding ID|Checklist/gate reference|FR reference|Source/evidence|Finding|Origin: Deliverable / Source / Process|Severity|Required correction|Owner|Due date|Status / retest evidence|
|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||

Rules:

- Link every failed checklist item to one or more findings.
- One finding may affect several checklist items; cross-reference it rather than creating inconsistent duplicates.
- Cite specific evidence for each deficiency.
- Do not classify a known violation as an observation.
- Close findings only after correction evidence has been reviewed.
- Update affected scores and gates after re-audit.

## 11. Scoring Summary

|Section|Nominal weight|Applicable maximum|Awarded points|Open finding references|
|---|---|---|---|---|
|A. Source Coverage and Scope Fidelity|30||||
|B. Verifiability and Testability|15||||
|C. Clarity, Atomicity, and Normative Language|15||||
|D. Consistency, Structure, and Traceability|15||||
|E. Correctness of Specified Behavior|15||||
|F. Gap Management, Governance, and Delivery Readiness|10||||
|**Total**|**100**||||

**Normalized score:** __________ / 100

**N/A items and rationale references:** ____________________

**Open findings:** Critical ___ / Major ___ / Minor ___ / Observations ___

**Unresolved critical source gaps:** __________

**Mandatory gates not met:** ____________________

### Result classification

Apply these rules in order:

1. **Not completed**
    
    - Core inputs or necessary evidence cannot be assessed.
    - The audit is incomplete or limited to sampling.
    - Any calculated partial score shall be labeled provisional, not final.
2. **Fail**
    
    - At least one critical or major finding remains unresolved; or
    - A critical source gap blocks specification readiness; or
    - The completed normalized score is below 60.
3. **Conditional**
    
    - The completed score is at least 60;
    - No critical or major findings or critical source gaps remain;
    - Minor corrections, minor gate failures, or outstanding required approval steps remain.
    - Corrective actions require owners, deadlines, and re-audit.
4. **Pass**
    
    - The completed score is at least 80;
    - All mandatory gates are met;
    - No non-conformances remain open;
    - Any remaining observations do not represent unmet obligations.

A score of 80 or more does not override an unresolved finding or failed gate.

A Pass confirms conformance for the audited baseline and declared scope. It does not establish that the product itself has passed implementation testing.

## 12. Implementation-Readiness Decision

Record this decision separately from the audit score.

|Readiness check|Yes / No / N/A|Evidence|
|---|---|---|
|Applicable behavior is sufficiently defined for implementation and verification.|||
|Critical gaps and unapproved assumptions are resolved.|||
|No critical or major requirement defects remain.|||
|Source, hierarchy, and verification traceability are established.|||
|Feasibility concerns have been reviewed and resolved or formally dispositioned.|||
|Required stakeholder reviews and approvals are complete.|||

**Implementation-ready:** Yes / No / Not assessed

**Conditions or limitations:** ______________________________________

## 13. Writing-Guide Coverage Map

|Writing-guide rule or topic|Primary audit checks|
|---|---|
|R1 — Approved-source derivation|A1–A4, D4–D5, F2|
|R2 — Fields and placeholders|A5, A8, B4, E1–E2|
|R3 — Successful flow|A7, B1–B2, B5, E3|
|R4 — Alternative, failure, and state behavior|A7–A8, B5, E3, E5, F1–F2|
|R5 — Conditions, triggers, and outcomes|B1–B2, C1–C2, C5|
|R6 — Validation and data boundaries|A6, B3, E1|
|R7 — Calculations and derived values|A9, B3, E4|
|R8 — State changes and data integrity|B5, E3, E5|
|R9 — Cross-module and external interactions|A10, D4, E5|
|R10 — Approved messages and UI text|A8, B4, E2|
|R11 — Functional behavior and related constraints|A3, D4, F4|
|Writing style|C1–C5|
|Hierarchy and stable identifiers|A4, D1–D3|
|Traceability and verification|B2, D5|
|Gaps, assumptions, and applicability|F1–F2, G5|
|HTML/Joplin structure and template use|A3, D2, F5, G6|
|Versioning and change control|D1, F3|
|Feasibility, reviews, and readiness|F4, G7, Section 12|

## 14. Audit Conclusion

**Audited deliverable and baseline:** ____________________

**Source baseline:** ____________________

**Final result:** Pass / Conditional / Fail / Not completed

**Final score:** ____________________

**Implementation-ready:** Yes / No / Not assessed

**Summary of coverage and conformance:**

---

**Principal findings and unresolved source gaps:**

---

**Required corrections and re-audit scope:**

---

**Audit limitations:**