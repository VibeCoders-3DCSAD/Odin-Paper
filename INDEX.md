# BUDI-Base — Repository Index

- **Project:** Development of BUDI: A Personalized Intelligent Finance Management Application for Filipinos Using Classification, Forecasting, Optimization, and Anomaly Detection Models for Improving Savings and Debt
- **Institution:** University of Makati | Group 4, III-DCSAD
- **Last indexed:** 2026-09-24

---

> **Ground truth:** the authoritative versions of the thesis documents live in the Google Drive folder. Copies in this repository are working mirrors and may lag behind the Drive source — verify before citing.
>
> **Spec update (2026-09-24):** the Drive *Technical Specification V1 (09.24.2026)* is
> the ground truth for project, paper, system, and models. Its canonical mirror is
> `docs/requirements-engineering/technical-specification.md`. The 09.24 revision is a
> substantial rewrite: the project identity is now **TAYA** ("Development of TAYA: A
> Personal Financial Management App Using SARIMA-Based Seasonal Expense Forecasting…",
> acronym words still TBD), built on FIES 2023 + HFCE 2022 Q1–2026 Q2 with a
> rule-based classifier, SARIMA forecaster, LP (HiGHS) solver, and IQR detector around
> a central **Financial Plan** artifact. The prior (09.20) "v2 methodology overrides"
> no longer need to be applied — the title algorithms are stated natively.
> Implementation docs live in **BUDI-ML** (`training/docs/model-methodologies/`,
> `docs/models/`) and use legacy v2 naming that may lag this spec.

---

## How to Use This Index

| Need | Go to |
| :--- | :--- |
| Formal RP2 proposal, title, objectives, scope | `docs/archive/research-proposal/Research-Proposal.md` |
| Technical specification (ground truth, Drive mirror) | `docs/requirements-engineering/technical-specification.md` |
| Product requirements (PRD) | `docs/requirements-engineering/product-requirements-document.md` |
| Functional requirements per module | `docs/requirements-engineering/feature-modules-v2.md` |
| Chapter 1 draft | `thesis/paper/chapter-1.md` |
| Model methodologies (adopted new-scope) | `docs/ml/README.md` → **BUDI-ML** `training/docs/model-methodologies/` |
| Screen descriptions (24 screens) | `docs/design-architecture/screen-descriptions/00-index.md` |
| System architecture and data schema | `docs/design-architecture/system-architecture.md` |
| Survey instrument | `docs/assessment-evaluation/survey/PUEPS.md` |
| RRL corpus, scoring, pipeline | **BUDI-Literature** |
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
| Topical outline | `google-drive/topical-outline/GROUP4 - TOPICAL OUTLINE - V3 - 09.15.26.docx` | Drive mirror (gitignored). Authoritative thesis structure. |
| Technical specification | `docs/requirements-engineering/technical-specification.md` | Ground truth (Drive mirror). Scope decisions, systems, models. |
| Product requirements | `docs/requirements-engineering/product-requirements-document.md` | Full-app PRD with user stories and scope. |
| Model methodologies | `BUDI-ML/training/docs/model-methodologies/` | Adopted new-scope designs; override spec algorithm column. |
| Paper chapters | `thesis/paper/` | Drafts: `chapter-1.md`, `chapter-2.md`, plus evidence maps. |
| RRL corpus & scoring | **BUDI-Literature** | Conversions, summaries, scores, module config. |

---

## Cross-References

| Task | Use |
| :--- | :--- |
| Understand what BUDI proposes to build | `docs/archive/research-proposal/Research-Proposal.md` |
| Topical outline of the thesis | `google-drive/topical-outline/GROUP4 - TOPICAL OUTLINE - V3 - 09.15.26.docx` |
| Ground-truth technical/systems scope | `docs/requirements-engineering/technical-specification.md` |
| Full app product requirements | `docs/requirements-engineering/product-requirements-document.md` |
| Adopted model methodologies | **BUDI-ML** — `training/docs/model-methodologies/` and `docs/models/` |
| Chapter drafts | `thesis/paper/` |
| List/search/download Drive files | `scripts/gdrive/README.md` |
| RRL corpus and scoring | **BUDI-Literature** — `scores/index.json` / `scores/report.md` |
| RRL processing workflow | **BUDI-Literature** — `docs/standards/rrl-workflow.md` |

---

## archived-literature/ (DEPRECATED)

**This directory is deprecated.** All RRL processing has moved to **BUDI-Literature**.

| Path | Status |
| :--- | :--- |
| `papers/` | Source PDFs (Git LFS). Pending migration to BUDI-Literature. |
| `compilations/` | **Deleted.** Old taxonomy; superseded by the BUDI-Literature corpus. |
| `scripts/` | **Deleted.** All useful scripts moved to BUDI-Literature. |
| `skills/` | **Deleted.** Superseded by the BUDI-Literature two-phase workflow. |
| `DEPRECATED.md` | Full deprecation details. |
| `_MIGRATION.md` | Final migration state. |
