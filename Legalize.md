# Skill: Legal‑Style Technical Specification

**Purpose:** To produce consistent, unified, clean technical or legal documents using a legal‑style framework. This skill defines rules for numbering, language, defined terms, cross‑references, and document structure. Apply these rules to any specification, contract, or policy document.

**Markdown flavor:** GitHub Flavored Markdown.

---

## 1. Document Header and Metadata

Every document begins with a title, version, date, and author(s). Use a simple list (not a table).

Example:

```
# Master Services Agreement

**Version:** 2.1
**Date:** 2026-06-05
**Author:** Legal Department
```

## 2. Definitions of Terms

Place the Definitions section immediately after the header, before any other content.

- Format: `**Term:** Complete sentence definition.`
- Define each term once. After definition, always use the exact capitalized term. Do not replace the term with “it”, “they”, or other pronouns.
- List terms in alphabetical order.

Example:

```
# Definitions of Terms

**Available Balance:** The sum of a specific Account’s starting balance plus all Income Transactions minus all Expense Transactions minus all Savings contributions minus all Debt payments.

**System:** The software application described in this document.
```

## 3. Heading Hierarchy

Use the following heading levels exclusively. Do not skip levels.

| Level | Markdown | Usage |
|-------|----------|-------|
| Title | `# Title` | Overall document title. |
| Major Part | `## Part 1: Name` | Optional, for grouping articles (e.g., Part 1: System Specification). |
| Article | `## Article 1: Name` | Major topic (Heading 2). If Parts are used, then Article becomes Heading 3? Actually the user specified: Heading 1 for specification types (System and Paper). Articles use Heading 2. So for the Odin document, the two main sections are `# System Specification` and `# Paper Specification`. Then articles inside are `## Article 1: ...`. That overrides the generic rule. For generic documents, use: Title (H1) → Part (H2) → Article (H3) → Section (H4) etc. But to keep it simple, we define a flexible rule: The highest heading after the title is H2 for articles; if you need a grouping level, use H2 for the group name and H3 for articles. We'll state: "Use Heading 1 for the overall document title. Use Heading 2 for major divisions (such as 'System Specification' or 'Part 1'). Use Heading 3 for articles. Use Heading 4 for sections. Use Heading 5 for subsections."

Yes, that is clearer. Let me rewrite the heading rule to be generic:

- `#` Document title.
- `##` Major division (e.g., Part 1, System Specification).
- `###` Article (e.g., Article 1: Platform).
- `####` Section (e.g., 1.1. Platform Requirements).
- `#####` Subsection (e.g., 1.1.1. Mobile-First Requirement).

This works for any document. The user's Odin document would use `# System Specification` (H1) and then `## Article 1` (H2). But that conflicts with the generic rule. To avoid confusion, we will present two patterns: one for Odin specifically, and one for general use. However, the user asked for a skill document, not an Odin‑specific guide. So we will provide a flexible rule: The highest heading after the title should indicate the document's primary sections; articles are one level below that. We'll illustrate with examples.

**Simpler approach:** Define the hierarchy as:

- `#` Document title.
- `##` Main section (e.g., Part, Specification type).
- `###` Article.
- `####` Section.
- `#####` Subsection.

That is clear and works for all documents. We'll adopt that.

Thus:

```
# Service Level Agreement

## Part 1: General Provisions

### Article 1: Definitions

#### 1.1. Defined Terms

##### 1.1.1. Capitalization Rule
```

Now the user's Odin document would have `# Odin Specification`, then `## System Specification`, then `### Article 1: Platform`. That matches the user's intent (H1 for spec types, H2 for articles? No – H2 for spec types, H3 for articles. But the user said "Heading 1 should be used for the two specification types (System and Paper). Articles should use Heading 2." That would be `# System Specification` (H1) then `## Article 1` (H2). That is a different pattern. To avoid confusion, we will present the generic rule as the default, but note that the user may adapt heading levels as needed. Since this is a skill document, we should prescribe one consistent rule.

Given the complexity, I will assume the generic rule is: H1 = document title, H2 = major part (e.g., System Specification), H3 = article, H4 = section, H5 = subsection. That is clean and avoids special cases. The user can adjust for their Odin document if they wish. I'll mention that as a note.

Let me write the final heading rule:

```
## 3. Heading Hierarchy

Use the following heading levels in sequence:

- `#` Document title (only once).
- `##` Major division (e.g., "Part 1", "System Specification").
- `###` Article (e.g., "### Article 1: Platform and Target Users").
- `####` Section (e.g., "#### 1.1. Platform Requirements").
- `#####` Subsection (e.g., "##### 1.1.1. Mobile-First Requirement").

Do not skip levels. Number sections using decimal notation (1.1, 1.2, 1.2.1, etc.). The article number is the first digit, section number is the second, etc.
```

I will incorporate this.

Now, I will write the final skill document in full. I will include all the rules we discussed, plus the common mistakes section and a short example.

---# Skill: Legal‑Style Technical Specification

**Version:** 1.0  
**Date:** 2026-06-05  
**Purpose:** To produce consistent, unified, clean technical or legal documents using a legal‑style framework. This skill defines rules for numbering, language, defined terms, cross‑references, and document structure.

**Markdown flavor:** GitHub Flavored Markdown.

---

## Table of Contents

1. [Document Header and Metadata](#1-document-header-and-metadata)
2. [Definitions of Terms](#2-definitions-of-terms)
3. [Heading Hierarchy](#3-heading-hierarchy)
4. [Numbering Style](#4-numbering-style)
5. [Language Rules](#5-language-rules)
6. [Cross‑References](#6-crossreferences)
7. [Callouts for Open Items](#7-callouts-for-open-items)
8. [Module Dependencies Block](#8-module-dependencies-block)
9. [Tables](#9-tables)
10. [Version History and Amendment Tracking](#10-version-history-and-amendment-tracking)
11. [Appendices](#11-appendices)
12. [Common Mistakes and Corrections](#12-common-mistakes-and-corrections)
13. [Example: A Fully Formatted Article](#13-example-a-fully-formatted-article)

---

## 1. Document Header and Metadata

Every document begins with a title, version, date, and author(s). Use a simple list (not a table).

**Example:**

```markdown
# Master Services Agreement

**Version:** 2.1
**Date:** 2026-06-05
**Author:** Legal Department
```

Optional fields: Status (Draft, Final), Reviewer, Document ID.

---

## 2. Definitions of Terms

Place the Definitions section immediately after the header, before any other content.

**Format:** `**Term:** Complete sentence definition.`

- Define each term once. After definition, always use the exact capitalized term. Do not replace the term with “it”, “they”, or other pronouns.
- List terms in alphabetical order.
- The first letter of each defined term is capitalized throughout the document.

**Example:**

```markdown
# Definitions of Terms

**Available Balance:** The sum of a specific Account’s starting balance plus all Income Transactions minus all Expense Transactions minus all Savings contributions minus all Debt payments.

**System:** The software application described in this document.
```

**Usage in body:** “The System calculates the Available Balance. The Available Balance may become negative.” (Not “It may become negative.”)

---

## 3. Heading Hierarchy

Use the following heading levels in sequence. Do not skip levels.

| Level | Markdown | Usage |
|-------|----------|-------|
| 1 | `# Title` | Document title (only once) |
| 2 | `## Part 1: Name` | Major division (e.g., “System Specification”) |
| 3 | `### Article 1: Name` | Article (major topic) |
| 4 | `#### 1.1. Section Title` | Section within an article |
| 5 | `##### 1.1.1. Subsection Title` | Subsection (rare) |

**Example:**

```markdown
# Service Level Agreement

## Part 1: General Provisions

### Article 1: Definitions

#### 1.1. Defined Terms

##### 1.1.1. Capitalization Rule
```

**Note for Odin document:** To match the user’s requirement, use `# System Specification` (H1) and `## Article 1: Platform` (H2) – that is a valid adaptation. The generic rule above uses H2 for major divisions and H3 for articles; either is acceptable as long as the hierarchy is consistent.

---

## 4. Numbering Style

Use **decimal numbering** only. No Roman numerals (I, II) or letters (A, B) for section numbers.

- Article number: `### Article 3: Title` – the article number is 3.
- Section number: `#### 3.1. Section Title` – first digit is article number, second is section number.
- Subsection: `##### 3.1.1. Subsection Title` – third digit.

**Within a section, for numbered lists:**

Use `1.`, `2.`, `3.` for sequential steps or prioritized items. For sub‑clauses, use `(a)`, `(b)`, `(c)` with indentation. Avoid deeper nesting than `(i)`.

**Example:**

```
The System performs three validations in sequence:

1. Validate the amount is greater than zero.
2. Validate the Available Balance is sufficient.
   (a) If insufficient, display a warning.
   (b) If the User confirms, proceed.
3. Store the Transaction.
```

---

## 5. Language Rules

### 5.1. Tense and Modality

Write in **present tense declarative**. The word “shall” is omitted. The obligation is implied by the declarative form.

- Correct: “The System accepts manual transaction entry.”
- Incorrect: “The System shall accept manual transaction entry.”

Use “must” only in callouts for strong warnings or requirements that override default behavior.

### 5.2. Defined Terms

After definition, always use the exact capitalized term. Do not use “it”, “they”, “the system”, or “the user” as a substitute.

- Correct: “The System calculates the Available Balance. The Available Balance may become negative.”
- Incorrect: “The System calculates the Available Balance. It may become negative.”

### 5.3. Prose Style

Write in **complete sentences and paragraphs**. Avoid bullet points unless listing items that are truly parallel and benefit from vertical presentation.

**When using bullet points:**

- Start each bullet with a capital letter.
- End each bullet with a period if it is a complete sentence; no period if a phrase.
- Maintain parallel grammatical structure across all bullets.

**Example of good bullet list:**

```
The System rejects a Transaction if:
- The amount is less than or equal to zero.
- The category is not selected.
- The date is in the future.
```

### 5.4. Numbers and Units

- Spell out numbers one through nine; use numerals for 10 and above.
- For percentages, use numerals followed by the percent sign (e.g., 5%).
- For currency, use PHP followed by a space and the numeral (e.g., PHP 1,000).
- For ranges, use “to” rather than dashes in prose (e.g., “from 10 to 20 days”).

---

## 6. Cross‑References

Use explicit section numbers. Do not write “see Definitions” – assume the reader knows where the Definitions are located.

- Correct: “The User may edit any Transaction (see 3.2.1).”
- Incorrect: “The User may edit any Transaction (see above).”
- Incorrect: “The User may edit any Transaction (see Definitions).”

If a reference is made to an appendix, write “(see Appendix B)”.

---

## 7. Callouts for Open Items

Use blockquotes with a bold label to indicate unresolved items, notes, or future work. Place the callout immediately after the sentence or paragraph it refers to, indented at the same level.

**Labels:**

- `> **NOTE:**` – Clarification, example, or non‑normative guidance.
- `> **OPEN:**` – A decision not yet finalized. Include a deadline or responsible party if possible.
- `> **RRL NEEDED:**` – A placeholder requiring literature or survey validation.
- `> **FUTURE WORK:**` – A feature or capability deferred beyond the current scope.

**Example:**

```
The threshold for income stability is a Coefficient of Variation of 0.25.

> **OPEN:** This threshold is provisional. It must be validated through analysis of BSP Consumer Finance Survey data. The threshold remains configurable.
```

---

## 8. Module Dependencies Block

At the end of each major article or module, add a prose paragraph that describes dependencies. Do not use bold labels or tables.

**Format:** Write one or two complete sentences that state what the module depends on and what modules depend on it.

**Example:**

```
### Module Dependencies

The Budget Recommendation Module depends on the Forecasting Module (Article 7) for income and expense forecasts, and on the Classification Module (Article 3) for the User's Financial Behavioral Profile. The Budget Recommendation Module is used by the Alerts Module (Article 11) for overspending notifications.
```

---

## 9. Tables

**Avoid Markdown tables for most content.** Use prose lists or structured paragraphs instead.

Only use a table when presenting **dense, columnar data** that would be harder to read as a list. Examples: metric thresholds with multiple columns, category mapping with more than 15 rows, or comparison matrices.

If a table is used:

- Keep column headers short.
- Do not merge cells.
- Do not use tables for sequential steps (use numbered list) or for prose comparisons (use bullet list).

**Example of acceptable table use:**

```
| Metric | Acceptable Threshold | Evaluation Method |
|--------|----------------------|-------------------|
| MAE | < 15% | Walk‑forward validation |
| sMAPE | < 25% | Synthetic test set |
```

---

## 10. Version History and Amendment Tracking

At the end of the document (before appendices), include a bullet list of version changes.

**Format:** `- **Version X.Y** (Date): Summary of changes.`

**Example:**

```
## Version History

- **3.0** (2026-06-04): Resolved contradictions; added decision log.
- **2.0** (2026-06-03): Full refactored specification.
- **1.0** (2026-05-01): Initial draft.
```

---

## 11. Appendices

Use Heading 1 for each appendix title to separate them from the main body. Appendices are lettered (A, B, C, etc.).

**Example:**

```
# Appendix A: Onboarding Questionnaire

The User answers the following questions during account creation.

1. What is your typical monthly income (in PHP)?
2. Is your monthly income roughly the same each month?
...
```

Do not include appendices in the main decimal numbering system.

---

## 12. Common Mistakes and Corrections

| Mistake | Correction |
|---------|------------|
| “The System shall accept…” | “The System accepts…” |
| “It then calculates the balance.” | “The System then calculates the Available Balance.” |
| “See Section 3.2 above.” | “(see 3.2)” |
| Using a table for a simple list of three items | Use a bullet list instead. |
| “The user” (lowercase after definition) | “The User” (capitalized) |
| “1. First step. A. Substep.” | “1. First step. (a) Substep.” |
| “The System depends on the Forecasting Module. It also depends on Classification.” | “The System depends on the Forecasting Module and the Classification Module.” |
| Omitting the period at the end of a bullet that is a complete sentence | Add a period. |
| Using “i.e.,” or “e.g.,” without italicizing | Either italicize or use plain text; be consistent. |

---

## 13. Example: A Fully Formatted Article

Below is a short example applying all the rules.

```markdown
### Article 3: User Classification

#### 3.1. Income Stability Thresholds

##### 3.1.1. Coefficient of Variation Calculation

The System determines Income Stability using the Coefficient of Variation (CV) of monthly net income over the preceding ninety (90) days. The CV equals the standard deviation divided by the mean.

##### 3.1.2. Classification Rule

- The System classifies a User as **Stable** if the CV is less than 0.25.
- The System classifies a User as **Variable** if the CV is 0.25 or greater.

> **OPEN:** The threshold of 0.25 is provisional. It must be validated through analysis of BSP Consumer Finance Survey data.

##### 3.1.3. Cold-Start Classification

During the first seven (7) days of Transaction history, the System estimates Income Stability using the Onboarding Questionnaire (see 3.6). The System does not compute the CV until the User has recorded at least five Income Transactions.

**Module Dependencies**

The Classification Module depends on the Onboarding Questionnaire (3.6) for initial cold‑start values. The Classification Module is used by the Budget Recommendation Module (Article 6) and the Forecasting Module (Article 7).
```

---

**End of Skill Document**