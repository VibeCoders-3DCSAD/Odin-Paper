# BUDI-Base — Agent Guide

**Thesis**: Development of BUDGIE: A Personal Financial Management App Using SARIMA to Improve Financial Planning (Group 4, III-DCSAD). Earlier drafts named this project BUDI, then TAYA; Outline V4 (09.26) and Chapter 2 V3 (09.26) use **BUDGIE**.
**Group 4, III-DCSAD, University of Makati**

---

## Repository Role

This is the **knowledge base** for the BUDI thesis. It contains thesis documents, specifications, PRDs, and survey instruments. It does **not** contain application code, API servers, or ML model implementations — those live in `BUDI-App/` and `BUDI-ML/` respectively.

The RRL corpus, scoring pipeline, and related tooling live in **BUDI-Literature**.

> **Ground truth:** the authoritative versions of the thesis documents live in the Google Drive folder. Copies in this repository are working mirrors and may lag behind the Drive source — verify before citing.
>
> **Outline update (2026-09-26):** the authoritative topical outline is now
> `google-drive/topical-outline/GROUP4 - TOPICAL OUTLINE - V4 - 09.26.26.docx`, and the
> project identity is now **BUDGIE** — "Development of BUDGIE: A Personal Financial
> Management App Using SARIMA to Improve Financial Planning". V4 is a full rewrite:
> the savings/debt product subtypes, TAM/UTAUT, and the SVM classifier are gone, replaced
> by a **rule-based** saver/borrower classifier, seasonal expense forecasting, budget
> creation by constraint optimization, and unusual expense detection. `TAYA`, named in the
> 09.24 technical specification and still used in its canonical mirror
> `docs/requirements-engineering/technical-specification.md`, is **superseded** and should
> not be used to settle naming questions.
>
> **Chapter 2 V3 (09.26) is the current Chapter 2.** Its canonical mirror is
> `thesis/paper/chapter-2.md` (V3.0). It was written against Outline V4 on the same day,
> so the two are already aligned; see `thesis/paper/chapter-2-evidence-map.md` for the
> citation audit and its open items.
>
> **Chapter 1 is only half-renamed.** `GROUP4 - CHAPTER 1 - V6 - 09.24.26.docx` carries
> BUDGIE on its title page and introduction, but its Scope and Limitations section still
> says BUDI and still uses **SVM** for profile classification, which V4 replaced with
> rule-based. Do not treat Chapter 1 V6 as settled on either identity or algorithms.
>
> **Spec update (2026-09-24):** the Drive *Technical Specification V1 (09.24.2026)* is
> still the ground truth for system, module, and implementation detail, and its canonical
> mirror is `docs/requirements-engineering/technical-specification.md`. The 09.24 revision
> stated the project identity as **TAYA** and the title algorithms as rule-based
> classification, **SARIMA** forecasting (FIES 2023 + HFCE 2022 Q1–2026 Q2 temporal
> disaggregation), **LP (HiGHS)** solving, and **IQR** detection around a central Financial
> Plan artifact. The algorithm set still holds; the name does not. Methodology and
> implementation docs in `BUDI-ML/training/docs/model-methodologies/` and
> `BUDI-ML/docs/models/` use legacy v2 naming that lags both.

---

## Coding Standards

This repository does not contain application code, so backend/frontend coding standards from `BUDI-ML/docs/standards/REPOSITORY-STANDARDS.md` do not apply. The applicable standards are:

| Standard | Location |
|----------|----------|
| Git commit messages | `docs/standards/git-commit-standards.md` |
| Documentation format | `docs/standards/documentation-format.md` |
| Documentation discipline | `docs/standards/documentation-discipline.md` |
| Document versioning | `docs/standards/versioning.md` |

Enforcement: Follow the commit message format for all commits. Keep `INDEX.md` updated when adding or moving files.

> **RRL standards** (naming conventions, summary format, workflow) have moved to **BUDI-Literature**: `BUDI-Literature/docs/standards/`.

---

## Requirements Engineering Documents

- Requirements tables intended for copy-paste into Google Docs must use the compact HTML table syntax used in `docs/requirements-engineering/reqs-eng_v2.md`: one continuous `<div class="joplin-table-wrapper"><table>...</table></div>` block without line breaks inside the table.
- Parent functional requirements must contain one summary requirement followed by lettered child components (`a`, `b`, `c`, and so on).
- Detailed child requirements must use the `FRXX-AAXX` identifier format and appear as separate rows in the same table.

---

## Git Commit Message Standards

```text
<type>(<scope>): <brief message>
```

Always include a scope. Use imperative mood. 50-72 characters.

### Scopes for This Repository

| Scope | Use For |
|-------|---------|
| `model` | Model design documents and data analysis |
| `data` | Data sources, synthetic data, FIES/BSP files |
| `docs` | Thesis documents, specifications, chapter drafts |
| `survey` | Survey instruments and notes |
| `config` | Repo configuration, tooling |
| `standards` | Shared engineering standards and agent guidance |

Full reference: `docs/standards/git-commit-standards.md`

---

## Top-Level Directory Layout

```
BUDI-Base/
  AGENTS.md              # This file — agent navigation and standards
  INDEX.md               # Master navigation index (authoritative)
  docs/                  # Thesis documents and standards
  google-drive/          # Local mirrors of Drive files (gitignored)
  scripts/               # Standalone tooling
  survey/                # Survey instruments
  archived-literature/    # DEPRECATED — see archived-literature/DEPRECATED.md
```

---

## Navigation

See **`INDEX.md`** for the authoritative index. Key documents:

| Document | Purpose |
|----------|---------|
| **`docs/INDEX.md`** | Documentation index for everything under `docs/`. |
| **`docs/requirements-engineering/technical-specification.md`** | Ground-truth technical specification (Drive mirror). The main design contract. |
| **`docs/requirements-engineering/product-requirements-document.md`** | Product requirements. |
| **`docs/requirements-engineering/feature-modules-v2.md`** | Functional requirements per module. |
| **`docs/design-architecture/screen-descriptions/00-index.md`** | Index of the 24 screen descriptions. |
| **`thesis/paper/chapter-1.md`** | Chapter 1 draft (Introduction) — local mirror is V5; Drive V6 (09.24) is newer and is only half-renamed to BUDGIE. |
| **`thesis/paper/chapter-2.md`** | Chapter 2 (RRL) — V3.0, mirroring the 09.26 Drive V3. Current. |
| **`thesis/paper/chapter-2-evidence-map.md`** | Citation audit of Chapter 2 V3 against the RRL corpus, with its open items. |
| **`docs/ml/README.md`** | ML / model methodology index (adopted new-scope designs live in BUDI-ML). |
| **`docs/archive/research-proposal/Research-Proposal.md`** | Formal RP2 proposal (authoritative for objectives/scope). |

---

## Model & Data

- Adopted model methodologies and their evaluation plans are in **BUDI-ML** (`training/docs/model-methodologies/`); condensed service contracts in `BUDI-ML/docs/models/`.
- BUDI-Base `docs/ml/` holds the study-level model index.
- FIES CSV, BSP/PSA data, and synthetic data handoffs are in `BUDI-ML/`.

---

## Python Environment

A `.venv/` exists (gitignored). This repository has no Python dependencies of its own — `requirements.txt` is a legacy artifact. All RRL processing scripts now live in **BUDI-Literature**.

### scripts/gdrive/

A self-contained Google Drive API CLI tool for reading files from the group's Drive. Lives in `scripts/gdrive/` with its own `requirements.txt`. Credentials go in `scripts/gdrive/.env` (gitignored). See `scripts/gdrive/README.md` for usage.

---

## Google Workspace MCP

Use the Google Workspace MCP with account `ctogle.a12345617@umak.edu.ph`.

### Group 4 Drive Folder

- Root folder: [Group 4 Folder](https://drive.google.com/drive/u/2/folders/12__5LoqZMRtzeOGPnFuLaESt3F0BDYuS)
- Root folder ID: `12__5LoqZMRtzeOGPnFuLaESt3F0BDYuS`
- Inventory checked: 2026-09-21
- All listed folders and child items are accessible with the account above.

### Drive Tree

```text
Group 4 Folder/
├── CHANGE REQUEST FORM/ (empty)
├── CHAPTER 1/
│   ├── GROUP4 - CHAPTER 1 - V1 - 08.06.26.docx
│   ├── GROUP4 - CHAPTER 1 - V2 - 08.27.26.docx
│   ├── GROUP4 - CHAPTER 1 - V3 - 08.28.26.docx
│   ├── GROUP4 - CHAPTER 1 - V4 - 09.13.26.docx
│   ├── GROUP4 - CHAPTER 1 - V5 - 09.19.26.docx
│   └── GROUP4 - CHAPTER 1 - V6 - 09.24.26.docx
├── CHAPTER 2/
│   ├── GROUP4 - CHAPTER 2 - V1 - 09.02.26.docx
│   ├── GROUP4 - CHAPTER 2 - V2 - 09.15.26.docx
│   └── GROUP4 - CHAPTER 2 - V3 - 09.26.26.docx
├── CHAPTER 3/
│   └── GROUP4 - CHAPTER 3 - V1 - 09.20.26.docx
├── EMPATHY MAP/
│   └── GROUP4 - EMPATHY MAP - V1 - 09.15.2026 (Google Doc)
├── QUESTIONNAIRES/
│   ├── ISO 25010 (IT EXPERTS)/
│   │   └── GROUP4 - ISO 25010 - V1 - 09.15.2026.docx
│   ├── PRELIMINARY INVESTIGATION SURVEY/
│   │   ├── GROUP4 - PRELIMINARY INVESTIGATION SURVEY - V1 - 09.16.2026 (Google Form)
│   │   └── GROUP4 - PRELIMINARY INVESTIGATION SURVEY - V1 - 09.16.2026 (Google Doc)
│   ├── PRE-SURVEY QUESTIONNAIRE/
│   │   ├── ODIN Public User Expectations and Perception Survey (Google Form)
│   │   └── ODIN Public User Expectations and Perception Survey (Responses) (Google Sheet)
│   └── SYSTEM USABILITY SCALE (SUS for Non-IT Experts)/
│       └── GROUP4 - SYSTEM USABILITY SCALE - V1 - 09.15.2026.docx
├── RECORDINGS/
│   ├── 20260421_142516.aac
│   ├── TA Consultation - 26-08-2026.aac
│   ├── 20260909_134943.aac (duplicate ×2)
│   ├── 20260909_163344.aac (duplicate ×2)
│   └── 20260918_173231.aac
├── USER AND SYSTEM REQUIREMENTS/
│   ├── GROUP4 - USER AND SYSTEM REQUIREMENTS - V1 - 08.31.2026 (Google Doc)
│   └── GROUP4 - USER AND SYSTEM REQUIREMENTS - V2 - 09.24.2026 (Google Doc)
├── SYSTEM DEVELOPMENT/
│   ├── GANTT CHART/
│   │   ├── GROUP4 - GANTT CHART - V1 - 08.15.26 (Google Sheet)
│   │   └── GROUP4 - GANTT CHART - V2 - 08.31.26 (Google Sheet)
│   ├── RESPONSIBILITY MATRIX/
│   │   └── GROUP4 - RESPONSIBILITY MATRIX - V1 - 08.15.26 (Google Sheet)
│   └── TRACEABILITY MATRIX/
│       └── GROUP4 - TRACEABILITY MATRIX - V1 - 08.15.26 (Google Sheet)
├── TECHNICAL SPECIFICATION/
│   └── GROUP4 - TECHNICAL SPECIFICATION - V1 - 09.24.2026 (Google Doc)
├── TEST PLAN/
│   └── GROUP4 - TEST PLAN - V1 - 08.31.2026 (Google Sheet)
├── TOPICAL OUTLINE/
│   ├── GROUP4 - TOPICAL OUTLINE - V1 - 08.05.26.docx
│   ├── GROUP4 - TOPICAL OUTLINE - V2 - 08.25.26.docx
│   ├── GROUP4 - TOPICAL OUTLINE - V3 - 09.15.26.docx
│   └── GROUP4 - TOPICAL OUTLINE - V4 - 09.26.26.docx
└── TRANSCRIPTIONS/
    ├── COURSE ADVISER/ (empty)
    ├── SUBJECT MATTER EXPERT/
    │   └── GROUP4 - SME CONSULTATION LOG - 09.24.2026 (Google Doc; was 09.17.2026, same file ID)
    ├── TECHNICAL ADIVSER/ (Drive spelling preserved)
    │   └── Group 4 - Kick-Off Meetings (Google Doc)
    └── PANEL COMMENTS AND SUGGESTIONS/
        ├── GROUP4 - PANEL COMMENTS AND SUGGESTIONS - 04.21.26.pdf
        └── GROUP4 - SUMMARY OF PANEL COMMENTS AND SUGGESTIONS - 04.21.26 (Google Doc)
```

### Drive Item IDs and Links

| Folder or item | Drive ID | Type | Link |
|---|---|---|---|
| CHANGE REQUEST FORM | `1LCUWOiVRu6Ei0NAf5ocJ9rWueXQJup_5` | Folder | [Open](https://drive.google.com/drive/folders/1LCUWOiVRu6Ei0NAf5ocJ9rWueXQJup_5) |
| CHAPTER 1 | `19QJazfrs3ufWnwSEtRdNgHv-60_bffUw` | Folder | [Open](https://drive.google.com/drive/folders/19QJazfrs3ufWnwSEtRdNgHv-60_bffUw) |
| GROUP4 - CHAPTER 1 - V1 - 08.06.26.docx | `1EO6Hi9mWaV-aLsN9kq2nb9l4zGckUQ4r` | DOCX | [Open](https://docs.google.com/document/d/1EO6Hi9mWaV-aLsN9kq2nb9l4zGckUQ4r/edit) |
| GROUP4 - CHAPTER 1 - V2 - 08.27.26.docx | `15Js77QKmec0rv3JSFo8em_g2h43NcZzz` | DOCX | [Open](https://docs.google.com/document/d/15Js77QKmec0rv3JSFo8em_g2h43NcZzz/edit) |
| GROUP4 - CHAPTER 1 - V3 - 08.28.26.docx | `1fBdmf97ERcDR1l_YRGXMEA8nmUawq3aQ` | DOCX | [Open](https://docs.google.com/document/d/1fBdmf97ERcDR1l_YRGXMEA8nmUawq3aQ/edit) |
| GROUP4 - CHAPTER 1 - V4 - 09.13.26.docx | `15J2p7EDJTF5yzrWQBiFgtR1yuJRMZbdq` | DOCX | [Open](https://docs.google.com/document/d/15J2p7EDJTF5yzrWQBiFgtR1yuJRMZbdq/edit) |
| GROUP4 - CHAPTER 1 - V5 - 09.19.26.docx | `1STLFcymwEnQTFlAxSzF4x-y3swJM5AUd` | DOCX | [Open](https://docs.google.com/document/d/1STLFcymwEnQTFlAxSzF4x-y3swJM5AUd/edit) |
| GROUP4 - CHAPTER 1 - V6 - 09.24.26.docx | `1zF97KyiS6Crsoc0XtKS7tPN0lut40eUb` | DOCX | [Open](https://docs.google.com/document/d/1zF97KyiS6Crsoc0XtKS7tPN0lut40eUb/edit) |
| CHAPTER 2 | `1rgcGoXhRFHaNbaXOCDRSEpoYleKmiiUu` | Folder | [Open](https://drive.google.com/drive/folders/1rgcGoXhRFHaNbaXOCDRSEpoYleKmiiUu) |
| GROUP4 - CHAPTER 2 - V1 - 09.02.26.docx | `1Pk3MIQ5JOogMsqc5vNXAmcVSIXFfYeM2` | DOCX | [Open](https://docs.google.com/document/d/1Pk3MIQ5JOogMsqc5vNXAmcVSIXFfYeM2/edit) |
| GROUP4 - CHAPTER 2 - V2 - 09.15.26.docx | `1D7Nwbddoeg7SVnTK9qJO3DRdJYIvqBco` | DOCX | [Open](https://docs.google.com/document/d/1D7Nwbddoeg7SVnTK9qJO3DRdJYIvqBco/edit) |
| GROUP4 - CHAPTER 2 - V3 - 09.26.26.docx | `1MT-1uzhVS_dZHa6O7YVIPGgA-Vx-IY3q` | DOCX | [Open](https://docs.google.com/document/d/1MT-1uzhVS_dZHa6O7YVIPGgA-Vx-IY3q/edit) |
| CHAPTER 3 | `1t-maI-Vzt5tRot0IFypgkiTVDwHcVjaP` | Folder | [Open](https://drive.google.com/drive/folders/1t-maI-Vzt5tRot0IFypgkiTVDwHcVjaP) |
| GROUP4 - CHAPTER 3 - V1 - 09.20.26.docx | `1bdlyRNfF9I-CkWGLAOsTMsSD5oXrkvMB` | DOCX | [Open](https://docs.google.com/document/d/1bdlyRNfF9I-CkWGLAOsTMsSD5oXrkvMB/edit) |
| EMPATHY MAP | `10FYRQBnCBTAo9pbTuoOGfajMuTVUbUaB` | Folder | [Open](https://drive.google.com/drive/folders/10FYRQBnCBTAo9pbTuoOGfajMuTVUbUaB) |
| GROUP4 - EMPATHY MAP - V1 - 09.15.2026 | `1XcJuEce0XT1SMVXRUxBLRYXVxV-FxA9dKjuSkvFaOto` | Google Doc | [Open](https://docs.google.com/document/d/1XcJuEce0XT1SMVXRUxBLRYXVxV-FxA9dKjuSkvFaOto/edit) |
| QUESTIONNAIRES | `1hGoepFiBWmQ-gwXJA_D5JTyZZQZxVXZt` | Folder | [Open](https://drive.google.com/drive/folders/1hGoepFiBWmQ-gwXJA_D5JTyZZQZxVXZt) |
| ISO 25010 (IT EXPERTS) | `1b4DwUTNYe4iDqyYX0cY8-PkZD_wsisu0` | Folder | [Open](https://drive.google.com/drive/folders/1b4DwUTNYe4iDqyYX0cY8-PkZD_wsisu0) |
| GROUP4 - ISO 25010 - V1 - 09.15.2026.docx | `1rhS0nYvjrIblAOFzFBoXx403SDNkDF7P` | DOCX | [Open](https://docs.google.com/document/d/1rhS0nYvjrIblAOFzFBoXx403SDNkDF7P/edit) |
| PRELIMINARY INVESTIGATION SURVEY | `1zbGcoiMTxBghnML-Og0DuV-uhJdqtpRJ` | Folder | [Open](https://drive.google.com/drive/folders/1zbGcoiMTxBghnML-Og0DuV-uhJdqtpRJ) |
| GROUP4 - PRELIMINARY INVESTIGATION SURVEY - V1 - 09.16.2026 | `1GnyeIL7iXZi8wSg_4eZeez4xkL_3p2zuQyW3TUzt4-w` | Google Doc | [Open](https://docs.google.com/document/d/1GnyeIL7iXZi8wSg_4eZeez4xkL_3p2zuQyW3TUzt4-w/edit) |
| GROUP4 - PRELIMINARY INVESTIGATION SURVEY - V1 - 09.16.2026 | `12mN_kZh_3CCGducNRupwm7KtkWIGSk5foHQkci1lBRU` | Google Form | [Open](https://docs.google.com/forms/d/12mN_kZh_3CCGducNRupwm7KtkWIGSk5foHQkci1lBRU/edit) |
| PRE-SURVEY QUESTIONNAIRE (under QUESTIONNAIRES) | `1ZoG09Stl6RNBQR5GLoVrNVrmjcPRYx-y` | Folder | [Open](https://drive.google.com/drive/folders/1ZoG09Stl6RNBQR5GLoVrNVrmjcPRYx-y) |
| ODIN Public User Expectations and Perception Survey | `11lUJ57mwp1StnyDW37cueQoPulbVdGB0ktgnRknve4Y` | Google Form | [Open](https://docs.google.com/forms/d/11lUJ57mwp1StnyDW37cueQoPulbVdGB0ktgnRknve4Y/edit) |
| ODIN Public User Expectations and Perception Survey (Responses) | `15oqix24YKHG2gfISPr90IujUF4yl0PmlO2wu3-6Kz_A` | Google Sheet | [Open](https://docs.google.com/spreadsheets/d/15oqix24YKHG2gfISPr90IujUF4yl0PmlO2wu3-6Kz_A/edit) |
| SYSTEM USABILITY SCALE (SUS for Non-IT Experts) | `1sJjmgBRhnxc-XTJJLJRnRuCJxHuGC2wa` | Folder | [Open](https://drive.google.com/drive/folders/1sJjmgBRhnxc-XTJJLJRnRuCJxHuGC2wa) |
| GROUP4 - SYSTEM USABILITY SCALE - V1 - 09.15.2026.docx | `1kYgRXxqrYA-95IABBSfEdlcvY9HhHjGF` | DOCX | [Open](https://docs.google.com/document/d/1kYgRXxqrYA-95IABBSfEdlcvY9HhHjGF/edit) |
| RECORDINGS | `1O1uBXs44dma-V7cVk-86TFK4MqYH_QxE` | Folder | [Open](https://drive.google.com/drive/folders/1O1uBXs44dma-V7cVk-86TFK4MqYH_QxE) |
| USER AND SYSTEM REQUIREMENTS (top level; was REQUIREMENTS ENGINEERING) | `1wZvLzJIkKjmkD_0xv9GQI8BH6Do-fvvX` | Folder | [Open](https://drive.google.com/drive/folders/1wZvLzJIkKjmkD_0xv9GQI8BH6Do-fvvX) |

| GROUP4 - USER AND SYSTEM REQUIREMENTS - V1 - 08.31.2026 | `1yxAVRp2SsezUcAuqx-5R3TpP1Q_wg2Sby68YUe4LxYU` | Google Doc | [Open](https://docs.google.com/document/d/1yxAVRp2SsezUcAuqx-5R3TpP1Q_wg2Sby68YUe4LxYU/edit) |
| GROUP4 - USER AND SYSTEM REQUIREMENTS - V2 - 09.24.2026 | `11ISktEsQd4NHCxrb09pn5LOnDzoLwu_TCszmuckEAWE` | Google Doc | [Open](https://docs.google.com/document/d/11ISktEsQd4NHCxrb09pn5LOnDzoLwu_TCszmuckEAWE/edit) |
| SYSTEM DEVELOPMENT | `1p_EtCzgwtBH_UIGFnquUdRXRVr0uUzXt` | Folder | [Open](https://drive.google.com/drive/folders/1p_EtCzgwtBH_UIGFnquUdRXRVr0uUzXt) |
| GANTT CHART (under SYSTEM DEVELOPMENT) | `16IFtAeuUvIP2LRzzPmN3mF4VCN95gcFv` | Folder | [Open](https://drive.google.com/drive/folders/16IFtAeuUvIP2LRzzPmN3mF4VCN95gcFv) |
| GROUP4 - GANTT CHART - V1 - 08.15.26 | `15kgZfwjmO85HY6EK_HrPyvfmcb7-1YC-TBzFQQNcu3k` | Google Sheet | [Open](https://docs.google.com/spreadsheets/d/15kgZfwjmO85HY6EK_HrPyvfmcb7-1YC-TBzFQQNcu3k/edit) |
| GROUP4 - GANTT CHART - V2 - 08.31.26 | `13t2DYOGpGIK6vaK4pxoG6AqN3NsnsoTCjivP_BUMM84` | Google Sheet | [Open](https://docs.google.com/spreadsheets/d/13t2DYOGpGIK6vaK4pxoG6AqN3NsnsoTCjivP_BUMM84/edit) |
| RESPONSIBILITY MATRIX (under SYSTEM DEVELOPMENT) | `1QzaQgS0mF-6HY0cCQ-OeRuaDYUMTh2RT` | Folder | [Open](https://drive.google.com/drive/folders/1QzaQgS0mF-6HY0cCQ-OeRuaDYUMTh2RT) |
| GROUP4 - RESPONSIBILITY MATRIX - V1 - 08.15.26 | `1ZOTt9N1r6KRAUnFlAmfqFzTNXKUDRMYgpKsCcgxEIgM` | Google Sheet | [Open](https://docs.google.com/spreadsheets/d/1ZOTt9N1r6KRAUnFlAmfqFzTNXKUDRMYgpKsCcgxEIgM/edit) |
| TRACEABILITY MATRIX (under SYSTEM DEVELOPMENT) | `1uYshGn_u-Huv0YrmrTD5bXtrO0wQmJyw` | Folder | [Open](https://drive.google.com/drive/folders/1uYshGn_u-Huv0YrmrTD5bXtrO0wQmJyw) |
| GROUP4 - TRACEABILITY MATRIX - V1 - 08.15.26 | `1MFlGZn-OkQzMlq-vk3lPZ6RGndyPo51fmQXlGjozGV4` | Google Sheet | [Open](https://docs.google.com/spreadsheets/d/1MFlGZn-OkQzMlq-vk3lPZ6RGndyPo51fmQXlGjozGV4/edit) |
| TECHNICAL SPECIFICATION | `1dnzS2gz4mzN08rQ9l5O3k6XyVBgb5nQL` | Folder | [Open](https://drive.google.com/drive/folders/1dnzS2gz4mzN08rQ9l5O3k6XyVBgb5nQL) |
| GROUP4 - TECHNICAL SPECIFICATION - V1 - 09.24.2026 | `1v8hqqlsHuiEAugGe3or3BCG2F8zQ3aWCCyox--oMm6E` | Google Doc | [Open](https://docs.google.com/document/d/1v8hqqlsHuiEAugGe3or3BCG2F8zQ3aWCCyox--oMm6E/edit) |
| TEST PLAN | `1myU_uCIUwTeLzmRou2J9FCQBrBwEDJSL` | Folder | [Open](https://drive.google.com/drive/folders/1myU_uCIUwTeLzmRou2J9FCQBrBwEDJSL) |
| GROUP4 - TEST PLAN - V1 - 08.31.2026 | `1SBq-KAIvJNHh12EymJnePa3AGVkE8hPE_mfQHsmDMs4` | Google Sheet | [Open](https://docs.google.com/spreadsheets/d/1SBq-KAIvJNHh12EymJnePa3AGVkE8hPE_mfQHsmDMs4/edit) |
| TOPICAL OUTLINE | `1g87xQAtOP1IfTZxvDrMq7iVV831C0ccv` | Folder | [Open](https://drive.google.com/drive/folders/1g87xQAtOP1IfTZxvDrMq7iVV831C0ccv) |
| GROUP4 - TOPICAL OUTLINE - V1 - 08.05.26.docx | `1lJFfcix2VELN5u0EbOjUHq6F8ds1f5Cb` | DOCX | [Open](https://docs.google.com/document/d/1lJFfcix2VELN5u0EbOjUHq6F8ds1f5Cb/edit) |
| GROUP4 - TOPICAL OUTLINE - V2 - 08.25.26.docx | `1vnIW5BOsuRieQvpIt_nm2H1wEIssRnKI` | DOCX | [Open](https://docs.google.com/document/d/1vnIW5BOsuRieQvpIt_nm2H1wEIssRnKI/edit) |
| GROUP4 - TOPICAL OUTLINE - V3 - 09.15.26.docx | `12kkqhSZIbx0Bsn0yYyqTRrxTCavsS_Hs` | DOCX | [Open](https://docs.google.com/document/d/12kkqhSZIbx0Bsn0yYyqTRrxTCavsS_Hs/edit) |
| GROUP4 - TOPICAL OUTLINE - V4 - 09.26.26.docx | `10H90N72dc2nqeLTl7y7S1BF18uuy8647` | DOCX | [Open](https://docs.google.com/document/d/10H90N72dc2nqeLTl7y7S1BF18uuy8647/edit) |
| TRANSCRIPTIONS | `1YC1IIGMWObiFxNHPNUh-V4mq3fbuXoNp` | Folder | [Open](https://drive.google.com/drive/folders/1YC1IIGMWObiFxNHPNUh-V4mq3fbuXoNp) |
| COURSE ADVISER (under TRANSCRIPTIONS) | `1TeV76BFy9eYUtBsc0DVVyyQTVwkUsYN0` | Folder | [Open](https://drive.google.com/drive/folders/1TeV76BFy9eYUtBsc0DVVyyQTVwkUsYN0) |
| SUBJECT MATTER EXPERT (under TRANSCRIPTIONS) | `1d4i-Eu03xbogJ4fOPdpdKqs3WrQPxOpj` | Folder | [Open](https://drive.google.com/drive/folders/1d4i-Eu03xbogJ4fOPdpdKqs3WrQPxOpj) |
| GROUP4 - SME CONSULTATION LOG - 09.24.2026 (was 09.17.2026) | `1GtrTylHvdOoRqOKfV1gPBj5JST6y4-z5ldkAqCKBz1I` | Google Doc | [Open](https://docs.google.com/document/d/1GtrTylHvdOoRqOKfV1gPBj5JST6y4-z5ldkAqCKBz1I/edit) |
| TECHNICAL ADIVSER (under TRANSCRIPTIONS) | `10k98VHGqXG8ZCq5ijUJfMI8zoN5vJvDb` | Folder | [Open](https://drive.google.com/drive/folders/10k98VHGqXG8ZCq5ijUJfMI8zoN5vJvDb) |
| Group 4 - Kick-Off Meetings | `1_HBHsAEh58o_HsYNvKzc_kiN_jiQtL6OGEbGtWGtMTs` | Google Doc | [Open](https://docs.google.com/document/d/1_HBHsAEh58o_HsYNvKzc_kiN_jiQtL6OGEbGtWGtMTs/edit) |
| PANEL COMMENTS AND SUGGESTIONS (under TRANSCRIPTIONS) | `1NV6uEcBnqoaScpqNlR13U5h6pezTEkkm` | Folder | [Open](https://drive.google.com/drive/folders/1NV6uEcBnqoaScpqNlR13U5h6pezTEkkm) |
| GROUP4 - PANEL COMMENTS AND SUGGESTIONS - 04.21.26.pdf | `1Bt3CY1_XM9qcZqabjfaDdhwWrRuwxlt4` | PDF | [Open](https://drive.google.com/file/d/1Bt3CY1_XM9qcZqabjfaDdhwWrRuwxlt4/view) |
| GROUP4 - SUMMARY OF PANEL COMMENTS AND SUGGESTIONS - 04.21.26 | `1LbK0xd5wP6RkxHfZcc8tiO6oRAgGIkcr72z18DceYrs` | Google Doc | [Open](https://docs.google.com/document/d/1LbK0xd5wP6RkxHfZcc8tiO6oRAgGIkcr72z18DceYrs/edit) |

When locating a Drive item, search by its recorded ID or exact name. When adding or moving files, update this tree and the table in the same change.

---

## Important Gotchas

- **`google-drive/` is gitignored.** It holds local `.docx` mirrors fetched from Drive. Run `python scripts/gdrive/fetch_drive.py` to refresh. Drive is the source of truth.
- The authoritative topical outline is the newest `GROUP4 - TOPICAL OUTLINE - V<N> - *.docx` under `google-drive/topical-outline/` (currently **V4, 09.26.26**). The generated `google-drive/topical-outline/topical-outline.md` is a stale V1-era extraction; do not cite it. See the `TOPICAL OUTLINE` entries in the Drive table.
- `fetch_drive.py` also writes `google-drive/INVENTORY.md` with every item's Drive ID, type, and modified date. AGENTS.md's tree and ID table are still maintained by hand and drift silently; after any fetch that adds, moves, or renames a file, diff the two and copy the changed rows across.
- **Corpus stems name the first author, but the source PDF filename often does not.** Seven corpus stems were wrong for this reason and were corrected on 2026-09-26. Verify a stem against page 1 of the PDF before citing it. `BUDI-Literature/literature/conversions/metadata.json` is the sidecar that records what has actually been verified.
- RRL processing live in **BUDI-Literature**. There are no RRL standards or pipeline scripts here; see `docs/standards/*rrl*` deprecation notices.
- **`archived-literature/` is deprecated.** See `archived-literature/DEPRECATED.md`. All RRL work happens in BUDI-Literature.
