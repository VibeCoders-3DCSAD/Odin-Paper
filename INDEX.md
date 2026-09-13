# Odin Papers — Repository Index

- **Project:** Development of BUDI: A Personalized Intelligent Finance Management Application for Filipinos Using Classification, Forecasting, Optimization, and Anomaly Detection Models for Improving Savings and Debt
- **Institution:** University of Makati | Group 4, III-DCSAD
- **Last indexed:** 2026-09-13

---

> **Ground truth:** the authoritative versions of the thesis documents live in the Google Drive folder. Copies in this repository are working mirrors and may lag behind the Drive source — verify before citing.

---

## How to Use This Index

| Need | Go to |
| :--- | :--- |
| Formal RP2 proposal, title, objectives, scope | `docs/archive/research-proposal/Research-Proposal.md` |
| System specification (working contract) | `docs/requirements-engineering/system-spec.md` |
| Product requirements (PRD) | `docs/requirements-engineering/product-requirements-document.md` |
| Functional requirements per module | `docs/requirements-engineering/requirements-engineering.md` |
| Chapter 1 draft | `docs/thesis/paper/chapter-1.md` |
| ML model design and training docs | `docs/ml/README.md` |
| Screen descriptions (24 screens) | `docs/design-architecture/screen-descriptions/00-index.md` |
| System architecture and data schema | `docs/design-architecture/system-architecture.md` |
| Survey instrument | `docs/assessment-evaluation/survey/PUEPS.md` |
| RRL corpus, scoring, pipeline | **Odin-Literature** (https://github.com/VibeCoders-3DCSAD/Odin-Literature) |
| Google Drive CLI tool | `scripts/gdrive/README.md` |
| Agent navigation and standards | `AGENTS.md` |

For everything under `docs/`, see **`docs/INDEX.md`** (authoritative for the documentation tree).

---

## Repository Map

| Path | Purpose |
| :--- | :--- |
| `AGENTS.md` | Agent navigation guide, standards, and repository conventions. |
| `INDEX.md` | This file. Master navigation index. |
| `docs/` | Thesis documents, standards, and documentation. See `docs/INDEX.md`. |
| `docs/archive/` | Preserved research proposal, panel comments, and superseded documents. |
| `archived-literature/` | Deprecated RRL working files. See `archived-literature/DEPRECATED.md`. |
| `formats-templates/` | Format and template files for thesis outputs. Includes `chapter-1/Writing Chapter 1.md` (adviser guidelines) and the reference thesis `chapter-1/Reference Thesis (Group 10).docx` (gitignored, local-only benchmark). |
| `google-drive/` | Local mirrors of Drive files. Gitignored. Run `fetch_drive.py` to refresh. |
| `scripts/gdrive/` | Google Drive API CLI tool (local OAuth 2.0). See `scripts/gdrive/README.md`. |
| `skills/` | Agent skills for this repository. |

---

## Source-of-Truth Stack

| Layer | Source | Notes |
| :--- | :--- | :--- |
| Formal research proposal | `docs/archive/research-proposal/Research-Proposal.md` | Authoritative for RP2 framing, objectives, scope. |
| Topical outline | `google-drive/topical-outline/topical-outline.md` | Drive mirror (gitignored). Thesis structure. |
| System specification | `docs/requirements-engineering/system-spec.md` | Working system contract. |
| Product requirements | `docs/requirements-engineering/product-requirements-document.md` | Full-app PRD with user stories and scope. |
| Paper chapters | `docs/thesis/paper/` | Drafts such as `chapter-1.md`. |
| RRL corpus & scoring | **Odin-Literature** | Conversions, summaries, scores, module config. |

---

## Cross-References

| Task | Use |
| :--- | :--- |
| Understand what BUDI proposes to build | `docs/archive/research-proposal/Research-Proposal.md` |
| Topical outline of the thesis | `google-drive/topical-outline/topical-outline.md` |
| Full app product requirements | `docs/requirements-engineering/product-requirements-document.md` |
| Detailed system rules | `docs/requirements-engineering/system-spec.md` |
| Chapter drafts | `docs/thesis/paper/` |
| Plan ML/model implementation | `docs/ml/` (design docs) + **Odin-ML** (code) |
| List/search/download Drive files | `scripts/gdrive/README.md` |
| RRL corpus and scoring | **Odin-Literature** — `scores/index.json` / `scores/report.md` |
| RRL processing workflow | **Odin-Literature** — `docs/standards/rrl-workflow.md` |

---

## archived-literature/ (DEPRECATED)

**This directory is deprecated.** All RRL processing has moved to **Odin-Literature** (https://github.com/VibeCoders-3DCSAD/Odin-Literature).

| Path | Status |
| :--- | :--- |
| `papers/` | Source PDFs (Git LFS). Pending migration to Odin-Literature. |
| `compilations/` | Deprecated. Old taxonomy. Do not use. |
| `scripts/` | Deprecated. All useful scripts moved to Odin-Literature. |
| `skills/` | Deprecated. Not moved. Skills form through demand in Odin-Literature. |
| `DEPRECATED.md` | Full deprecation details. |
| `_MIGRATION.md` | Final migration state. |
