[WARNING]: Outdated.

# Odin RRL Working Directory

---

## Table of Contents

- [Odin RRL Working Directory](#odin-rrl-working-directory)
  - [Table of Contents](#table-of-contents)
  - [1. Directory Structure](#1-directory-structure)
  - [2. The Three Core Documents](#2-the-three-core-documents)
    - [`topic-outline.md`](#topic-outlinemd)
    - [`registry.md`](#registrymd)
    - [`Papers/<paper_id>-summary.md`](#paperspaper_id-summarymd)
  - [3. The Two Skills](#3-the-two-skills)
    - [`converter.md` — PDF to Markdown](#convertermd--pdf-to-markdown)
    - [`summarizer.md` — Converted Markdown to Summary](#summarizermd--converted-markdown-to-summary)
  - [4. Source Quota](#4-source-quota)
  - [5. Full Paper Pipeline](#5-full-paper-pipeline)
  - [6. The Registry](#6-the-registry)
    - [Column Reference](#column-reference)
  - [7. Finding Papers](#7-finding-papers)
    - [Starting from a topic](#starting-from-a-topic)
    - [Starting from a topic](#starting-from-a-topic-1)
    - [Checking quota gaps](#checking-quota-gaps)
    - [Searching for a specific shorthand](#searching-for-a-specific-shorthand)
  - [8. The Topic System](#8-the-topic-system)
  - [9. Designation Rules](#9-designation-rules)
  - [10. Citation Recency Rules](#10-citation-recency-rules)
  - [11. Member Checklist Workflow](#11-member-checklist-workflow)
  - [12. Quick Reference](#12-quick-reference)
    - [Add a new paper (command sequence)](#add-a-new-paper-command-sequence)
    - [Topic-to-outline cross-reference](#topic-to-outline-cross-reference)
    - [Quota status](#quota-status)
    - [File naming](#file-naming)
    - [Shorthand tags](#shorthand-tags)

---

## 1. Directory Structure

```
rrl/
│
├── README.md                       ← this file
├── registry.md                     ← one-row-per-paper master index
├── topic-outline.md                ← mind map of all RRL territory + Scholar queries
│
├── Skills/
│   ├── converter.md                ← PDF → Markdown conversion skill (for Claude)
│   └── summarizer.md               ← Markdown → Summary skill (for Claude)
│
└── Papers/
    ├── <paper_id>.pdf              ← raw paper
    ├── <paper_id>.md     ← converted markdown (converter output)
    └── <paper_id>-summary.md       ← structured summary (summarizer output)
```

**All papers, whether in PDF or MD format, live in one flat `Papers/` folder.** There are no subfolders by topic or topic. Cross-topic relevance is tracked in each summary's YAML and in `registry.md` — not by file location. See [Section 6](#6-the-registry) for why.

The `<paper_id>` in filenames is the paper's permanent identifier: the DOI (with slashes replaced by underscores) if available, or a UUID v4 if not. Example:

```
10.1016_j.eswa.2023.119872.pdf
10.1016_j.eswa.2023.119872-converted.md
10.1016_j.eswa.2023.119872-summary.md
```

---

## 2. The Three Core Documents

### `topic-outline.md`
The mind map of the entire RRL. It organizes all research territory the thesis must cover into a hierarchy:

```
Topic (A–J)
  └── Subtopic (A.1, A.2, ...)       ← maps to an RRL topic
        └── Sub-subtopic (bullet)    ← specific claim literature must establish
              └── Scholar query      ← paste directly into Google Scholar Labs
```

Every node has a `[/shorthand]` tag. These are used as search terms when filtering the registry — not as folder names. 
For example, when you want all papers relevant to LSTM, search `registry.md` for `/lstm` in the `topics_covered` column.

### `registry.md`
The master index of every paper that has been processed. One row per paper. Updated every time a new paper completes the pipeline. See [Section 6](#6-the-registry) for full column reference.

### `Papers/<paper_id>-summary.md`
The file the team actually reads. Produced by the summarizer skill. Contains the TL;DR, findings, definitions, and critically, the **Relevance to Odin** section — which states exactly what each paper justifies in Odin's design and RRL.

---

## 3. The Two Skills

Both skills are prompt files given to a language model when processing a paper. They are **not** run automatically — a team member must invoke them manually.

### `converter.md` — PDF to Markdown

**Input:** A PDF research paper.
**Output:** `<paper_id>.md` — a clean, fully structured Markdown representation of the paper, optimized for AI reading.

**What it produces in YAML:**
```yaml
paper_id:       # DOI or UUID — permanent ID
designation:    # local | international | algorithm-specific
title:          # exact paper title
authors:        # Last, F.; Last, F.
year:           # YYYY
venue:          # full journal or conference name
```

**When to use it:** Every time a new PDF is added to the pipeline. Always before the summarizer.

**How to invoke:**
1. Open a new conversation in any language model. It is important that they have file uploading, text-reading/OCR, and thinking features.
2. Paste the contents of `converter.md` as the first message, or use it as a system prompt if on API.
3. Upload the PDF.
4. The language model will output the converted Markdown. Save it as `<paper_id>.md` in `Papers/`.

> **Note on `paper_id`:** If the paper has a DOI (usually found on the first page or in the header), use it as the ID with `/` replaced by `_`. Example: DOI `10.1016/j.eswa.2023.119872` → ID `10.1016_j.eswa.2023.119872`. If no DOI, generate a UUID v4 at [uuidgenerator.net](https://www.uuidgenerator.net) and use that.

---

### `summarizer.md` — Converted Markdown to Summary

**Input:** A `<paper_id>.md` file.
**Output:** `<paper_id>-summary.md` — a human-optimized structured summary.

**What it produces in YAML:**
```yaml
paper_id:           # copied from converter output
odin_topics:       # [1, 5, 6] — list of topic numbers this paper supports
member_checklist:   # four team members, each with "[ ]" status
```

**When to use it:** Immediately after conversion, before adding the paper to the registry.

**How to invoke:**
1. Open a new conversation in any language model. It is important that they have file uploading, text-reading/OCR, and thinking features.
2. Paste the contents of `summarizer.md` as the first message.
3. Paste or upload the `<paper_id>.md` file.
4. The language model will output the summary. Save it as `<paper_id>-summary.md` in `Papers/`.

**Mandatory sections in every summary:**

| Section | Purpose |
|---|---|
| TL;DR | One sentence, ≤30 words |
| Problem and Motivation | The gap the paper addresses |
| Approach | Compact method bullets |
| Findings | Numbered results |
| Key Figures and Tables | Condensed visual takeaways |
| Key Equations | 1–3 central equations with plain-English meaning |
| Definitions | All terms and acronyms in a table |
| Critical Citations | ≤3 foundational references |
| **Relevance to Odin** | **The most important section — see below** |
| Limitations | Up to 4 caveats |
| Remember This | 3 emoji bullets for recall |

The **Relevance to Odin** section is the reason the summary exists. It answers four questions:
- Which topics does this paper support?
- What specifically does it contribute to Odin's design or RRL?
- What exact claims can this paper be cited for?
- What are the limits of how strongly it can be used?

---

## 4. Source Quota

The department requires exactly **50 sources**, split as follows:

| Designation | Target | Meaning |
|---|---|---|
| `local` | 25 | Published in the Philippines |
| `international` | 25 | Published outside the Philippines |
| `algorithm-specific` | Not tracked; any amount | Primarily describes an algorithm or model |

**Critical rule:** `algorithm-specific` is the highest-priority designation and **overrides** local/international. A paper from the Philippines that primarily describes LSTM architecture is `algorithm-specific`, not `local`.

Track current counts in the summary row of `registry.md`. See [Section 9](#9-designation-rules) for full designation logic.

---

## 5. Full Paper Pipeline

Every paper goes through these steps in order. No step is skippable.

```
Step 1 — FIND
  Use topic-outline.md Scholar queries to identify candidate papers.
  Confirm the paper is 2023–2026 (or an exempted source — see Section 10).
  Download the PDF.

Step 2 — ASSIGN ID
  Check for a DOI on the paper. If present: replace "/" with "_" → paper_id.
  If absent: generate UUID v4 → paper_id.

Step 3 — CONVERT
  Run converter skill on the PDF.
  Save output as Papers/<paper_id>.md.

Step 4 — SUMMARIZE
  Run summarizer skill on the converted file.
  Save output as Papers/<paper_id>-summary.md.

Step 5 — READ
  The assigned team member reads the summary (and optionally the full paper).
  They check off their name in the member_checklist in the summary YAML:
    status: "[x]"

Step 6 — REGISTER
  Add one row to registry.md using the YAML fields from the summary.
  Update the quota tally row at the bottom of the registry.

Step 7 — DONE
  Paper is now citable. Use paper_id to find the summary when writing RRL.
```

---

## 6. The Registry

`registry.md` is the master index. Every processed paper has exactly one row. It is the authoritative source for:
- Quota tracking (are we at 25/25?)
- Cross-topic lookup (which papers cover topic 6?)
- Checklist status (has everyone read this?)
- Finding a paper by title or author without opening every summary file

### Column Reference

| Column | Source | Description |
|---|---|---|
| `paper_id` | converter YAML | Permanent ID. DOI (slashes → underscores) or UUID v4. |
| `designation` | converter YAML | `local`, `international`, or `algorithm-specific`. |
| `year` | converter YAML | Four-digit publication year. |
| `authors` | converter YAML | Last, F. format. First author only if list is long; append "et al." |
| `title` | converter YAML | Exact paper title. Truncate at 60 chars with `…` if needed. |
| `venue` | converter YAML | Full journal or conference name. |
| `topics` | summarizer YAML `odin_topics` | Comma-separated topic numbers. E.g. `1, 5, 6`. |
| `shorthand_tags` | manually from outline | Relevant `[/shorthand]` tags from the outline. E.g. `/lstm, /lstm-mobile`. |
| `checklist` | summarizer YAML | `G` Gabion · `J` Guevarra · `A` San Jose · `C` Togle. Mark `✓` when read. |
| `notes` | manual | One-line note on the paper's primary Odin contribution. Optional but recommended. |

---

## 7. Finding Papers

### Starting from a topic
1. Open `topic-outline.md`.
2. Navigate to the relevant subtopic.
3. Copy a Scholar query from beneath a sub-subtopic bullet.
4. Paste into Google Scholar Labs.
5. Filter results to 2023–2026.

### Starting from a topic
1. Open `registry.md`.
2. Search the `topics` column for the topic number.
3. Each matching row links to a `paper_id` whose summary file has the full Relevance to Odin section.

### Checking quota gaps
1. Open `registry.md`.
2. Look at the tally row at the bottom.
3. The designation with the lowest count is where to prioritize next.

### Searching for a specific shorthand
1. Open `registry.md`.
2. Search the `shorthand_tags` column for the tag (e.g. `/concept-drift`).
3. All papers tagged to that sub-subtopic will appear.

---

## 8. The Topic System

The 15 RRL topics map directly to the subtopics in `topic-outline.md`. Every summary's `odin_topics` YAML field uses these numbers. Every registry row's `topics` column uses these numbers.

| Topic | Name | Outline Node |
|---|---|---|
| 1 | Spending and Budgeting Behavior of Filipino Young Professionals | A.1 |
| 2 | Existing Personal Finance and Budget Management Systems | A.2 |
| 3 | Mobile-First Design in Personal Finance Systems | B.1 |
| 4 | Budgeting Strategies and Budget Recommendation | C.1 |
| 5 | Budget Recommendation Algorithm | C.2 |
| 6 | Predictive Modeling in Personal Finance Systems | D.1 |
| 7 | LSTM as the Spending Forecasting Algorithm | D.2 |
| 8 | Anomaly Detection in Personal Finance Systems | E.1 |
| 9 | Anomaly Detection Algorithm | E.2 |
| 10 | User Behavioral Profiling in Filipino Personal Finance Contexts | F.1 |
| 11 | Profile Classification Algorithm | F.2 |
| 12 | Expense Categorization in Filipino Personal Finance Contexts | G.1 |
| 13 | Data Privacy, Security, and User Trust in Personal Finance Systems | H.1 |
| 14 | User Retention and Engagement in Personal Finance Systems | I.1 |
| 15 | System Evaluation | J.1 |

---

## 9. Designation Rules

Apply in strict priority order. Stop at the first match.

**1. `algorithm-specific` (highest priority)**
The document primarily describes a specific algorithm, model, or computational method. This applies regardless of where the paper was published. Covers: original algorithm papers, comparative benchmarks, applied ML papers where the algorithm is the primary subject, architecture overviews.

Examples that qualify: LSTM for time-series forecasting, Isolation Forest for anomaly detection, a classifier comparison study, a quantization method for mobile ML inference.

Examples that do not qualify: a study on Filipino spending behavior that happens to use regression as a tool; a PFMS evaluation that uses SUS as the instrument.

**2. `local`**
Published in or by a Philippine institution, and not algorithm-specific. Covers: Philippine journals, theses from Philippine universities, PSA/BSP/NPC publications, conference papers with Philippine lead authors at Philippine institutions.

**3. `international`**
Published outside the Philippines, and not algorithm-specific. This is the residual category — if it does not qualify as algorithm-specific or local, it is international.

---

## 10. Citation Recency Rules

The department requires all sources to be **2023–2026**, with these specific exceptions:

| Exception | Rule |
|---|---|
| **Laws and statutes** | Any year. Cite by Republic Act number and full title. |
| **ISO standards** | Any year. Always cite the specific edition (e.g., ISO/IEC 25010:2023). |
| **Foundational algorithm papers** | The original paper (e.g., Hochreiter & Schmidhuber 1997 for LSTM) may be cited **only through a recent applied work** that itself cites it. Do not cite the original directly. |
| **PSA/BSP institutional data** | The most recent available release of FIES, BSP CFS, or similar. Cite the data release year, not the institution's founding year. |

**If a paper is pre-2023 and does not fall into an exception above, do not use it.**

When in doubt: check the publication date in the converter YAML `year` field before adding to the registry.

---

## 11. Member Checklist Workflow

Every summary file has this block in its YAML:

```yaml
member_checklist:
  - name: "Gabion, Stefanie S."
    status: "[ ]"
  - name: "Guevarra, Joaquin Luis T."
    status: "[ ]"
  - name: "San Jose, Alexa Joanne Paula G."
    status: "[ ]"
  - name: "Togle, Charles Nathaniel B."
    status: "[ ]"
```

When a team member has read the summary, they change their `status` from `"[ ]"` to `"[x]"`. The registry `checklist` column uses initials (G · J · A · C) with ✓ marks to show the same status at a glance.

**Reading the summary is the minimum.** Members should read the full converted paper only if the Relevance to Odin section directly concerns a module they are building.

---

## 12. Quick Reference

### Add a new paper (command sequence)
```
1. Find paper via topic-outline.md Scholar query
2. Check year ≥ 2023 (or exemption applies)
3. Assign paper_id (DOI with / → _ , or UUID v4)
4. Run converter → save as Papers/<paper_id>.md
5. Run summarizer → save as Papers/<paper_id>-summary.md
6. Read summary → check off your name in member_checklist
7. Add row to registry.md → update tally
```

### Topic-to-outline cross-reference
Search `topic-outline.md` for `[/shorthand]` or heading text. Each subtopic heading corresponds to one topic number in the table above.

### Quota status
Look at the last row of `registry.md` (the tally row). Three numbers: local / international / algorithm-specific. Target is 25 / 25 / 25 = 75 total.

### File naming
```
Papers/<paper_id>.md
Papers/<paper_id>-summary.md
```
Where `<paper_id>` = DOI with `/` replaced by `_`, or UUID v4 if no DOI.

### Shorthand tags
Every node in `topic-outline.md` has a `[/shorthand]` tag. Use these in the `shorthand_tags` column of the registry to link papers to specific sub-subtopics, not just topics. This enables fine-grained lookup later when writing the RRL chapter.

---

*Last updated: 2026-04-28 | Team Aesir, Group 4*