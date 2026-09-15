---
type: guide
subtype: functional-requirements-writing
title: Rules and Instructions for Creating Functional Requirements
version: 1.1
date: 2026-09-05
status: active
applies_to: reqs-eng_v2.md
basis: feature-modules.md
audit_template: audit-template-functional-requirements.md
---

# Rules and Instructions for Creating Functional Requirements

## Purpose

This guide defines how functional requirements (FRs) are derived, written, reviewed, and maintained in `reqs-eng_v2.md`. Functional requirements shall be based on approved content in `feature-modules.md`. They shall be audited against that source using `audit-template-functional-requirements.md`. The objective is to produce requirements that are:

- Complete relative to the approved source and scope.
- Clear, consistent, and individually traceable.
- Observable and verifiable.
- Sufficiently detailed for implementation and testing.
- Free from unsupported assumptions, duplicate obligations, and contradictions.

This guide establishes project-specific writing and formatting conventions. Following it does not, by itself, establish compliance with an external requirements engineering standard.

## Source Authority and Scope

For this deliverable, `feature-modules.md` is the authoritative functional source. Other approved documents may define relevant business rules, interfaces, security obligations, accessibility obligations, or quality constraints. When these affect functional behavior:

1. Record the relevant document and section.
2. Identify any missing or conflicting content in `feature-modules.md`.
3. Obtain an approved resolution.
4. Update or explicitly reference the authoritative source before baselining the affected requirements.

A template, common industry practice, or writer preference is not an approved source of product behavior.

## Requirement Levels and Identifiers

Use the following hierarchy consistently:

| Level                 | Identifier  | Purpose                                                          |
| --------------------- | ----------- | ---------------------------------------------------------------- |
| Parent requirement    | `FR01`      | Summarizes a capability and lists its child components.          |
| Child requirement row | `FR01-AA01` | Specifies a child component in a separate table row.             |
| Detailed statement    | `N/A`       | Identifies an individual normative statement within a child row. |

Rules:

- Use the canonical identifier format without spaces around hyphens.
- Each numbered normative statement in a child row shall have a stable detailed-statement identifier.
- Each detailed statement shall express one independently verifiable behavior or constraint.
- Each child row shall map to a lettered component in its parent.
- A lettered component may map to multiple child rows when decomposition is needed.
- Parent summaries are aggregate requirements verified through their children, not separate copies of the same detailed obligations.
- Identifiers shall remain stable across revisions.
- Retired identifiers shall not be reassigned to unrelated requirements.

## Mandatory Writing Rules

### R1. Derive Every Requirement from Approved Source Content

Every parent requirement, child row, and detailed statement shall trace to one or more capabilities, fields, business rules, validations, states, messages, or interactions defined in `feature-modules.md`.

- Represent every defined capability through one or more traceable requirements.
- Decompose broad capabilities into testable behaviors without adding unsupported behavior.
- Include an explicit source reference in every parent and child row.
- A child-row reference may apply to all statements in that row. Add statement-specific references when different statements derive from different source elements.
- Use stable section identifiers or headings rather than line numbers alone.
- Do not add behavior solely because it appears in a template.
- Do not silently omit source-defined behavior because it is difficult to specify or implement.

When source content is missing, ambiguous, contradictory, or insufficient for deterministic testing, record a specification gap. Proposed enhancements shall remain separate from approved requirements until approved and incorporated into, or explicitly referenced by, the authoritative source.

### R2. Specify Input Fields and Approved Placeholders

Every input field defined in the feature module shall be represented in the requirements. For each field, specify or reference the source-defined:

- Label and purpose.
- Control type.
- Required or optional status.
- Allowed values and format.
- Minimum and maximum values or lengths.
- Default value, if applicable.
- Placeholder, if applicable.
- Validation behavior and associated messages.
- Conditional visibility or editability, if applicable.

Where the feature module defines a placeholder:

- Copy it verbatim.
- Enclose it in quotation marks.
- Preserve capitalization, punctuation, spacing, and symbols.

Example:

> The system shall display the email field with the placeholder "you@example.com".

Do not invent a placeholder when the source does not define one. If the source requires a placeholder but omits its text, record a specification gap. Placeholders shall not be treated as substitutes for persistent labels or accessible names. Input types that do not support placeholders shall be assessed accordingly.

### R3. Cover the Successful Flow

For every functional capability, specify the successful end-to-end flow through individually testable statements. Cover, where applicable:

1. The authorized actor and required preconditions.
2. Valid input or a valid initiating event.
3. The permitted action.
4. The resulting state or data change.
5. The observable result available to the user or calling system.
6. Any source-defined success feedback or cross-module update.

A success message is required only when the source defines one. A successful outcome may instead be demonstrated by navigation, a changed status, a saved record, updated data, or an interface response. Do not treat a success message alone as proof that the underlying operation completed correctly.

### R4. Assess Alternative, Failure, and State Behavior

For each capability, assess the applicability of:

- Initial and default states.
- Missing, malformed, mismatched, or out-of-range input.
- Boundary values.
- Empty results.
- Loading and in-progress states.
- Service failures and timeouts.
- Offline operation and stale or cached data.
- Unauthenticated or unauthorized access.
- Blocked or unavailable actions.
- Duplicate submissions.
- Conflicting or concurrent updates.
- Cancellation, retry, and recovery.
- Destructive or irreversible actions.

For each applicable, source-defined case, specify:

1. The triggering condition.
2. Whether the action is allowed, blocked, rejected, or interrupted.
3. The resulting system and data state.
4. The user or external-system feedback.
5. Available recovery actions, if defined.

Classify each assessed case as:

- **Specified:** behavior is defined and represented in the requirements.
- **N/A:** the case does not apply; record the reason.
- **Gap:** the case applies, but required behavior is missing or unclear.

Do not invent error messages, retry policies, offline behavior, or loading indicators to satisfy the checklist. For potentially destructive actions, specify the source-defined safeguard, such as confirmation, undo, or recoverable deletion. If an appropriate safeguard is not defined, flag the issue for review rather than automatically prescribing a confirmation dialog.

### R5. State Conditions, Triggers, and Outcomes Clearly

Each detailed statement shall identify the elements necessary to remove ambiguity:

- **Actor:** the user role or external system involved.
- **Precondition:** what must already be true.
- **Trigger:** the event or action initiating the behavior.
- **Response:** what the system shall do.
- **Postcondition:** the resulting observable state.

Preferred patterns:

> When [trigger], the system shall [observable response].
> If [condition], the system shall [observable response].
> While [state applies], the system shall [observable behavior].

Not every statement needs all elements. Shared preconditions may be defined once and referenced, provided their scope is explicit. Avoid combining several independently testable responses in one statement. Separate them and link them to the same triggering condition.

### R6. Define Validation and Data Boundaries Precisely

Where applicable and source-defined, specify:

- Inclusive or exclusive minimum and maximum boundaries.
- Length limits and how length is measured.
- Permitted characters and formats.
- Treatment of whitespace and case.
- Treatment of missing, null, and empty values.
- Uniqueness and duplicate-handling rules.
- Cross-field dependencies and matching rules.
- Validation timing, such as during entry, on field exit, or on submission.
- Whether invalid input blocks an action.
- Whether values are preserved, cleared, or transformed.
- When validation feedback appears or disappears.

Do not infer these rules from field names or sample values. If a source uses a term such as “valid email,” “strong password,” or “acceptable amount” without sufficient definition for consistent testing, record a gap or reference the approved rule that defines it.

### R7. Specify Calculations and Derived Values

For every source-defined calculation, specify or reference:

- The formula or algorithmic business rule.
- Input values and their sources.
- Units and currency.
- Relevant dates, time zones, and periods.
- Precision and rounding rules.
- Treatment of missing, zero, negative, or invalid inputs.
- Recalculation triggers.
- The displayed or stored result.

Use boundary examples or worked examples where they clarify the rule, but do not use examples as a substitute for the rule itself. Undefined calculation details that could produce different valid implementations shall be recorded as specification gaps.

### R8. Specify State Changes and Data Integrity

For state-changing actions, make the approved before-and-after behavior clear. Where applicable, specify:

- Permitted and prohibited state transitions.
- Records or values that change.
- Relevant records or values that must remain unchanged.
- When changes are persisted.
- Behavior if processing fails after it begins.
- Whether partial completion is possible.
- Whether repeated requests can create duplicate effects.
- When related views or modules reflect the change.

Do not assume that an error means no data changed. Where partial completion, rollback, or uncertain outcomes are possible but unspecified, record a gap for resolution.

### R9. Specify Cross-Module and External Interactions

For each source-defined cross-module or external-system flow, specify or reference:

- The initiating event.
- The sending and receiving components.
- The information exchanged.
- Relevant sequencing or dependencies.
- The expected response or observable result.
- Failure and recovery behavior.
- Related interface specifications, where available.

Avoid duplicating detailed interface contracts across multiple FRs. Reference the approved contract and specify the functional behavior that depends on it. Do not invent protocols, endpoints, payload fields, or integration mechanisms absent from the approved source.

### R10. Preserve Approved Messages and UI Text

Every source-defined validation, error, unavailable, blocked, network-required, empty-state, or success message shall be represented where the associated behavior is specified.

- Copy approved text verbatim.
- Preserve capitalization, punctuation, spacing, and symbols.
- Do not paraphrase text that a tester must compare exactly.
- Distinguish exact UI text from explanatory requirement prose.

For dynamic messages:

- Preserve the approved message pattern.
- Identify variable tokens and their source-defined formatting.
- Do not substitute an example value for the general message requirement.

For localized products:

- Identify the applicable locale.
- Use stable message identifiers where available.
- Reference the approved localized text source rather than inventing translations.

If source messages conflict or are missing for a state that requires a message, record a gap.

### R11. Keep Functional Behavior Distinct from Related Constraints

Functional requirements describe required system behavior. Related performance, availability, accessibility, security, legal, or other quality constraints shall be maintained in the appropriate requirement category and cross-referenced where relevant.

Examples:

- Rejecting an unauthorized operation is functional behavior.
- Completing an operation within a defined duration is a performance requirement.
- Recording a specified audit event is functional behavior.
- Meeting an accessibility conformance target is a quality or compliance requirement.

Do not omit an approved obligation merely because it belongs outside the functional requirements table. Specify observable behavior rather than implementation details unless the implementation constraint is explicitly approved.

## Writing Style Rules

Each detailed normative statement shall be:

- **Verifiable:** an objective check can determine whether it is satisfied.
- **Clear:** terms and conditions have an identifiable meaning.
- **Atomic:** it expresses one independently verifiable behavior or constraint.
- **Consistent:** terminology, roles, field names, states, and identifiers agree with the approved source.
- **Necessary:** it has a documented source and purpose.
- **Feasible:** unresolved implementation concerns are flagged for review.
- **Traceable:** its source and place in the requirement hierarchy are explicit.

Use **“shall”** for mandatory system behavior. Avoid:

- Vague terms such as “fast,” “intuitive,” “user-friendly,” or “appropriate.”
- Undefined qualifiers such as “normally” or “where necessary.”
- Open-ended lists ending in “etc.”
- Ambiguous pronouns or unspecified actors.
- “And/or” when the intended alternatives can be stated explicitly.
- Mixing rationale, proposals, and mandatory behavior in the same statement.

Use “should” or “may” only when nonmandatory guidance or permission is intentional and clearly distinguished from mandatory requirements.

## Traceability and Verification

Maintain bidirectional traceability:

- From each source capability to the requirements that represent it.
- From each detailed requirement back to its approved source.
- From each detailed requirement to verification checks or test cases when available.

A traceability register may use the following fields:

| Source baseline and reference | Parent ID | Child ID | Statement ID | Verification reference | Status |
|---|---|---|---|---|---|

For each detailed statement, the intended verification method shall be identifiable, such as:

- Test.
- Inspection.
- Demonstration.
- Analysis.

Detailed test procedures may be maintained separately. Requirements shall still contain enough information to determine the expected outcome without relying on unstated assumptions.

## Specification Gaps, Assumptions, and Applicability

Maintain a separate gap register for incomplete or conflicting specifications.

| Gap ID | Source reference | Issue or question | Affected FRs | Owner | Status | Resolution |
|---|---|---|---|---|---|---|

Use:

- **TBD:** information has not yet been determined.
- **TBC:** information is awaiting confirmation.
- **N/A:** an assessed item does not apply, with a recorded reason.

Rules:

- Do not present unresolved assumptions as approved requirements.
- Keep proposed behavior separate from normative statements.
- Record the decision and approval that resolve a gap.
- Update affected source content, requirements, and verification references after resolution.
- Do not mark affected requirements implementation-ready while critical gaps remain unresolved.

## Structure and Output Rules

### Content Structure

- Group requirements by module.
- Each parent row shall contain one summary requirement followed by lettered child components.
- Each child row shall appear separately in the same table.
- Each detailed normative statement shall have a stable statement identifier.
- Include source references in parent and child rows.
- Keep rationale, notes, and source references outside the numbered normative statements.

### Table Format

Use the compact HTML/Joplin format required by `reqs-eng_v2.md`: `<div class="joplin-table-wrapper"><table>...</table></div>`

Each module or feature-block table shall be one continuous block with no line breaks inside the wrapper.

Use the columns:

1. **No.**
2. **Components**
3. **Functional Requirements**

HTML/Joplin serialization is a deliverable-format requirement, not a substitute for requirements-quality review. Encode reserved HTML characters where necessary so that the **rendered text** matches the approved source exactly.

## Template

Replace all bracketed placeholders before approval. Template statements are illustrative structures, not approved product behavior. Include only statements supported by the approved source. Do not automatically add input preservation, immediate error clearing, success messages, retries, offline handling, or destructive-action confirmation.

```html
<div class="joplin-table-wrapper"><table><thead><tr><th colspan="3"><p><strong>[Module Name] Module</strong></p></th></tr><tr><th><p>No.</p></th><th><p>Components</p></th><th><p>Functional Requirements</p></th></tr></thead><tbody><tr><td><p>FR01</p></td><td><p>[Parent Component]</p></td><td><p><strong>Source:</strong> feature-modules.md — [section identifier or heading]</p><ol><li>The system shall [summary capability].<ol type="a"><li>[Child component a]</li><li>[Child component b]</li></ol></li></ol></td></tr><tr><td><p>FR01-AA01</p></td><td><p>[Child component a]</p></td><td><p><strong>Source:</strong> feature-modules.md — [specific source reference]</p><p><strong>Parent component:</strong> FR01(a)</p><ol><li><strong>FR01-AA01-01:</strong> The system shall display the [field name] field with the placeholder "[exact source-defined placeholder]".</li><li><strong>FR01-AA01-02:</strong> When [source-defined invalid condition], the system shall prevent [action].</li><li><strong>FR01-AA01-03:</strong> When [same source-defined invalid condition], the system shall display "[exact source-defined validation message]".</li></ol></td></tr><tr><td><p>FR01-AA02</p></td><td><p>[Child component b]</p></td><td><p><strong>Source:</strong> feature-modules.md — [specific source reference]</p><p><strong>Parent component:</strong> FR01(b)</p><ol><li><strong>FR01-AA02-01:</strong> When [valid trigger and required conditions], the system shall [single observable successful outcome].</li><li><strong>FR01-AA02-02:</strong> When [source-defined failure condition], the system shall [single source-defined failure response].</li></ol></td></tr></tbody></table></div>
```

## Review Checklist

Use this checklist alongside `audit-template-functional-requirements.md`. Audit references below retain the mappings stated in this guide; additional checks supplement the audit template.

### Source Coverage and Traceability

- [ ] Every defined capability maps to one or more requirements (A1, A3).
- [ ] Every parent and child row has an explicit source reference.
- [ ] Every child row traces to a parent child component (A4).
- [ ] Every detailed statement traces to approved source content.
- [ ] The source baseline is recorded.
- [ ] No unsupported capability or behavior has been introduced.

### Fields, Rules, and Calculations

- [ ] All source-defined form fields are specified (A5).
- [ ] Applicable placeholders are quoted exactly (B4).
- [ ] Validation rules and blocking behavior are specified (A6, E1).
- [ ] Applicable boundaries, units, formats, and dependencies are defined.
- [ ] Calculations, precision, and rounding match the source (A9, E4).

### Flows, States, and Messages

- [ ] Successful end-to-end behavior is covered (R3).
- [ ] Failure and alternative behavior have been assessed (R4, E5).
- [ ] All source-defined applicable states are specified (A7).
- [ ] Inapplicable cases are marked N/A with a reason.
- [ ] Applicable but undefined behavior is recorded as a gap.
- [ ] All source-defined messages are quoted verbatim (A8, E2).
- [ ] Relevant failed-action data outcomes are defined.
- [ ] Cross-module flows are specified (A10).

### Requirement Quality and Structure

- [ ] Each detailed statement expresses one independently verifiable obligation.
- [ ] Actors, conditions, triggers, and outcomes are clear where necessary.
- [ ] Statements use mandatory wording consistently.
- [ ] No vague or ambiguous language remains (C1–C3).
- [ ] Terminology is consistent (C4).
- [ ] Identifiers and parent-child relationships are consistent (D1–D2).
- [ ] No duplicate or contradictory requirements remain (D3).
- [ ] Related interface and non-functional requirements are cross-referenced.
- [ ] Output complies with the compact HTML/Joplin format.

### Readiness

- [ ] Verification methods or checks are identifiable.
- [ ] Critical gaps and unapproved assumptions are resolved.
- [ ] Feasibility concerns have been reviewed.
- [ ] Required stakeholder reviews and approvals are recorded.

## Versioning and Change Control

Record the version, date, or repository commit of `feature-modules.md` used to produce the requirements. For each proposed change:

1. Identify the affected source content and requirement identifiers.
2. Assess impacts on related modules, interfaces, UI text, calculations, and tests.
3. Assess impacts on existing behavior or data where relevant.
4. Record the reason, decision, and approval status.
5. Update the source, requirements, traceability records, and verification references consistently.
6. Retain a record of retired or superseded requirements.

A requirement set is ready for implementation only when its applicable behavior is sufficiently defined, its traceability is established, and critical unresolved gaps have been closed.

## Self-Check Example

Assume `feature-modules.md` defines **“Log in with email and password”** and gives the email placeholder as `you@example.com`. The requirement set shall cover:

1. A parent summary for the login capability.
2. The source-defined email and password fields.
3. The exact email placeholder: "you@example.com".
4. Source-defined validation rules and associated messages.
5. Successful authentication and its specified observable outcome.
6. Source-defined rejection and failure behavior.
7. Applicable loading, connectivity, and recovery behavior where defined.
8. Traceability to the relevant source sections.

If the source does not define a password placeholder, do not invent one. If a relevant network-failure case is identified but its handling is absent, record a gap. If the source defines a rejection message, copy it verbatim and specify the associated rejected or blocked behavior separately.

The goal is not to produce a fixed number of rows. The goal is complete, source-grounded, independently verifiable coverage.
