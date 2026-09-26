# BUDI-Base — Repository Index

- **Project:** Development of BUDGIE: A Personal Financial Management App Using SARIMA to Improve Financial Planning
- **Institution:** University of Makati | Group 4, III-DCSAD
- **Last indexed:** 2026-09-26

---

> **Ground truth:** the authoritative versions of the thesis documents live in the Google Drive folder. Copies in this repository are working mirrors and may lag behind the Drive source — verify before citing.
>
> **Outline update (2026-09-26):** the project identity is now **BUDGIE** — "Development
> of BUDGIE: A Personal Financial Management App Using SARIMA to Improve Financial
> Planning". Topical Outline V4 (09.26) and Chapter 2 V3 (09.26) both use BUDGIE and
> agree with each other. V4 is a full rewrite: the savings/debt subtypes, TAM/UTAUT, and
> the SVM classifier are gone, replaced by a **rule-based** saver/borrower classifier,
> seasonal expense forecasting, budget creation by constraint optimization, and unusual
> expense detection. `TAYA`, named in the 09.24 technical specification, is superseded.
>
> **Chapter 1 is only half-renamed.** Drive Chapter 1 V6 (09.24) carries BUDGIE on its
> title page and introduction, but its Scope and Limitations still says BUDI and still
> uses SVM. Do not treat it as settled on identity or algorithms.
>
> **Spec update (2026-09-24):** the Drive *Technical Specification V1 (09.24.2026)* is
> still ground truth for system, module, and implementation detail. Its canonical mirror
> is `docs/requirements-engineering/technical-specification.md`. The algorithm set it
> states still holds (rule-based classifier, SARIMA forecaster on FIES 2023 + HFCE
> 2022 Q1–2026 Q2, LP/HiGHS solver, IQR detector around a central **Financial Plan**
> artifact); its project name does not.
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
| Topical outline | `google-drive/topical-outline/GROUP4 - TOPICAL OUTLINE - V4 - 09.26.26.docx` | Drive mirror (gitignored). Authoritative thesis structure. |
| Technical specification | `docs/requirements-engineering/technical-specification.md` | Ground truth for system/module detail (Drive mirror). Names the project TAYA, which V4 supersedes. |
| Product requirements | `docs/requirements-engineering/product-requirements-document.md` | Full-app PRD with user stories and scope. |
| Model methodologies | `BUDI-ML/training/docs/model-methodologies/` | Adopted new-scope designs; override spec algorithm column. |
| Paper chapters | `thesis/paper/` | `chapter-1.md` (local mirror is V5; Drive V6 newer and half-renamed), `chapter-2.md` (**V3.0**, current), `chapter-2-evidence-map.md`. |
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
| Chapter drafts | `thesis/paper/` (Chapter 2 is current at V3.0) |
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
