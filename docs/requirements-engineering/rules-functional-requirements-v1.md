---
type: guide
subtype: functional-requirements-writing
title: Rules and Instructions for Creating Functional Requirements
version: 1.0
date: 2026-09-05
status: active
applies_to: reqs-eng_v2.md
basis: feature-modules.md
audit_template: audit-template-functional-requirements.md
---

# Rules and Instructions for Creating Functional Requirements

## Purpose

This guide defines how functional requirements (FRs) are written in the requirements deliverable. Functional requirements **shall be created based on `feature-modules.md`** and written into **`reqs-eng_v2.md`**. Requirements are audited against `feature-modules.md` using `audit-template-functional-requirements.md`.

## Mandatory Writing Rules

### R1. Derive every requirement from the feature modules

Every functional requirement and its child components must come from a capability, form field, validation rule, state, or message defined in **`feature-modules.md`**. Do not invent capabilities that are absent from the feature modules; do not omit a defined capability.

- **Action:** For each capability in the feature module, open a matching `FRxx` entry and `FRxx-AAxx` child rows. When in doubt, cite the feature-module section in the FR row.

### R2. Display placeholders for inputs

Every input field required by the feature module must state the **exact placeholder** that appears in the field. Placeholders are part of the requirement, not decoration.

- Use the placeholder text verbatim from the feature module (e.g., `Enter your email`, `Select account type`).
- Quote the placeholder exactly so a tester can assert it verbatim.

### R3. Account for the happy path

For every functional capability, write the requirement that covers the **successful** end-to-end flow: valid input → allowed action → correct result.

- State the observable outcome (e.g., the system authenticates the user and grants access, the balance updates, the goal progress refreshes).

### R4. Account for graceful failure

For every action, write requirements for the **failure, edge, empty, and blocked** cases so the system fails safely and clearly. Graceful failure includes:

- **Validation:** empty required fields, malformed data, out-of-range values, and mismatched entries.
- **Empty states:** no records exist to display.
- **Error states:** a request/service/network action fails.
- **Network-required and offline states:** actions that need connectivity and cached/stale handling.
- **Confirmation:** destructive actions (delete, clear, archive) require user confirmation.
- **Progress / loading states:** long-running actions show progress feedback.

Every error, failure, unavailable, blocked, or network-required state defined in the feature modules **must display its corresponding message** (see `feature-modules.md`).

## Writing Style Rules (from the audit template)

Write so that each requirement passes the audit checklist. Each `FRxx` / `FRxx-AAxx` must be:

- **Verifiable / testable** — observable behavior, deterministic outcomes.
- **Clear and unambiguous** — no vague words ("fast", "user-friendly").
- **Atomic** — one behavior per numbered requirement.
- **Consistent** — terminology and identifiers match across the document and the feature modules.
- **Quoted messages** — copy error/validation/success strings verbatim from the feature module.

## Structure Rules

- Parent functional requirements (FRxx) contain one **summary requirement** followed by lettered child components (`a`, `b`, `c`, ...).
- Detail-level child requirements use the `FRxx-AAXX` identifier and appear as **separate rows** in the same table.
- Output tables use the compact HTML/Joplin format used in `reqs-eng_v2.md`: one continuous `<div class="joplin-table-wrapper"><table>...</table></div>` block with no line breaks inside the table.

## Checklist (aligns with the audit template)

Before finalizing any FR, confirm:

- [ ] Maps to a feature-module capability (A1, A3).
- [ ] Child `FRxx-AAXX` traces to a child component (A4).
- [ ] All required form fields are specified (A5).
- [ ] Placeholders are quoted exactly (B4).
- [ ] Validation rules are specified (A6, E1).
- [ ] All states (initial, empty, loading, error, success, offline/stale) are specified (A7).
- [ ] All messages are quoted verbatim (A8, E2).
- [ ] Happy path is covered (R3).
- [ ] Graceful failure is covered (R4, E5).
- [ ] Calculations match the feature module (A9, E4).
- [ ] Cross-module flows are specified (A10).
- [ ] Single behavior per item, no vague words (C1–C3).
- [ ] Terminology is consistent (C4).
- [ ] `FRxx` / `FRxx-AAXX` identifiers are consistent (D1–D2).
- [ ] No duplicate or contradictory requirements (D3).

## Template

Use this skeleton when adding a new module or feature block to `reqs-eng_v2.md`. Replace the bracketed placeholders.

```html
<div class="joplin-table-wrapper"><table><thead><tr><th colspan="3"><p><strong>[Module Name] Module</strong></p></th></tr><tr><th><p>No.</p></th><th><p>Components</p></th><th><p>Functional Requirements</p></th></tr>

<tr><th><p>FRXX</p></th><th><p>[Parent Component]</p></th><th><ol><li>[Summary requirement describing the feature as a whole.]<ol type="a"><li>[Child component a]</li><li>[Child component b]</li></ol></li></ol></th></tr>

<tr><th><p>FRXX - AA01</p></th><th><p>[Child component name]</p></th><th><ol>
<li>This system feature [allows/lets] the user [clear, atomic behavior].</li>
<li>The system shall display a form with a [field name] field using the placeholder "[exact placeholder verbatim from feature module]".</li>
<li>The system shall prevent submission when the [field name] is blank and display "[empty validation message verbatim]".</li>
<li>The system shall prevent submission when the [field name] contains an invalid value and display "[invalid validation message verbatim]".</li>
<li>The system shall preserve valid input values after an invalid submission and clear the related validation message when the input is corrected.</li>
<li>When the [input] is [valid condition], the system shall [happy-path action] and display "[success message verbatim]".</li>
<li>When [a network/service action fails], the system shall display "[error message verbatim]".</li>
</ol></th></tr>
</table></div>
```

## Self-Check Example

For the feature-module capability **"Log in with email and password"** with placeholder `you@example.com`, the minimum FR rows cover:

1. Summary: the system allows the user to log in with a registered email and password.
2. Happy path: valid credentials authenticate the user and grant access (`R3`).
3. Placeholder: email field uses `you@example.com` (`R2`).
4. Graceful failure: blank email, malformed email, blank password, incorrect credentials, network error — each quoted and blocked/denied (`R4`).
