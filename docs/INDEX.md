# BUDI-Base — Documentation Index

- **Project:** Development of BUDGIE: A Personal Financial Management App Using SARIMA to Improve Financial Planning
- **Institution:** University of Makati | Group 4, III-DCSAD
- **Last indexed:** 2026-09-26

---

> **Ground truth:** the authoritative versions of the thesis documents live in the Google Drive folder. Copies in this repository are working mirrors and may lag behind the Drive source — verify before citing.
>
> **Outline update (2026-09-26):** the project is now **BUDGIE** — "Development of
> BUDGIE: A Personal Financial Management App Using SARIMA to Improve Financial Planning".
> Topical Outline V4 and Chapter 2 V3 (both 09.26) use BUDGIE. V4 replaced the SVM
> classifier with a rule-based one and dropped the savings/debt subtypes and TAM/UTAUT.
> `TAYA`, named in the 09.24 technical specification, is superseded. Drive Chapter 1 V6
> is only half-renamed and still says BUDI/SVM in its Scope and Limitations.
>
> **Spec update (2026-09-24):** the Drive *Technical Specification V1 (09.24.2026)* is
> still ground truth for system and module detail (mirror:
> `requirements-engineering/technical-specification.md`). Its algorithm set still holds
> (rule-based classifier, SARIMA with FIES 2023 + HFCE 2022 Q1–2026 Q2 temporal
> disaggregation, LP/HiGHS solver, IQR detector); its project name does not.
> Implementation docs live in **BUDI-ML**.

---

## How to Use This Index

| Need | Go to |
| :--- | :--- |
| Formal research proposal, objectives, scope | `archive/research-proposal/Research-Proposal.md` |
| Technical specification (ground truth, Drive mirror) | `requirements-engineering/technical-specification.md` |
| Product requirements (PRD) | `requirements-engineering/product-requirements-document.md` |
| Functional requirements per module | `requirements-engineering/feature-modules-v2.md` |
| Chapter drafts | `../thesis/paper/chapter-1.md`, `../thesis/paper/chapter-2.md` |
| Model documentation index | `ml/README.md` + **BUDI-ML** `training/docs/model-methodologies/` |
| Screen descriptions (24 screens) | `design-architecture/screen-descriptions/00-index.md` |
| System architecture and data schema | `design-architecture/system-architecture.md` |
| RRL benchmarks | `rrl/benchmarks.md` |
| Survey instrument | `assessment-evaluation/survey/PUEPS.md` |
| Git commit and documentation standards | `standards/` |
| Adviser (Ma'am Era) writing rules & comments | `standards/adviser-writing-rules.md` |
| RRL corpus and scoring | **BUDI-Literature** |
| ML service and training pipeline | **BUDI-ML** |

---

## Repository Map

| Path | Purpose |
| :--- | :--- |
| `assessment-evaluation/` | Survey instruments and evaluation materials. |
| `archive/` | Preserved research proposal, panel comments, and superseded documents. |
| `design-architecture/` | System architecture, data schema, and screen descriptions. |
| `ml/` | Study-level ML/model documentation index (methodologies live in BUDI-ML). |
| `requirements-engineering/` | Technical specification, PRD, and functional requirements. |
| `rrl/` | RRL benchmarks, literature matrix, and theoretical framework. |
| `standards/` | Documentation, versioning, and git commit standards. |
| (root) `thesis/` | Thesis paper drafts. |

---

## assessment-evaluation/

| File | Purpose |
| :--- | :--- |
| `survey/PUEPS.md` | Survey instrument (Public User Expectations and Perception Survey). |
| `survey/PUEPS-with-notes.md` | Survey instrument with notes. |

---

## design-architecture/

| File | Purpose |
| :--- | :--- |
| `system-architecture.md` | High-level system architecture and data flow. |
| `data-schema.md` | Entity Relationship Diagram and data dictionary. |
| `screen-descriptions/00-index.md` | Index of the 24 screen descriptions. |
| `screen-descriptions/01..24-*.md` | One file per user-facing screen/workflow. |

---

## ml/

Study-level model documentation index. The **adopted new-scope methodologies** live in
**BUDI-ML** (`training/docs/model-methodologies/` and `docs/models/`).

| Path | Purpose |
| :--- | :--- |
| `ml/problem-statement/` | MDDs, feature sets, module integration, deployment, synthetic data rules, accountant validation of PFP thresholds. |
| `ml/data-collection/` | FIES/BSP data source documentation. |
| `ml/data-preprocessing/` | Preprocessing pipeline documentation. |
| `ml/exploratory-data-analysis/` | Exploratory data analysis guide. |
| `ml/dimension-threshold-discovery/` | PFP dimension and threshold discovery. |
| `ml/feature-engineering/` | Feature engineering pipeline documentation. |
| `ml/model-training/` | Superseded PFP/Forecaster/Anomaly training docs (kept for reference). |
| `ml/README.md` | ML documentation index. |

---

## requirements-engineering/

| File | Purpose |
| :--- | :--- |
| `technical-specification.md` | Ground-truth technical specification (Drive mirror). The main design contract. |
| `tbd-register-resolution.md` | TBD resolution register — status, evidence, and recommended decisions per spec TBD. |
| `product-requirements-document.md` | Product requirements document. |
| `feature-modules-v2.md` | Functional requirements per module. |
| `feature-modules-v1.md` | Superseded module list (kept for reference). |
| `audit-template-functional-requirements-v2.md` | FR audit templates. |
| `rules-functional-requirements-v2.md` | FR writing rules. |

---

## rrl/

| File | Purpose |
| :--- | :--- |
| `benchmarks.md` | Benchmarking analysis of PFM mobile applications. |
| `literature-matrix.md` | Comparison table of papers, methods, and gaps. |
| `theoretical-framework.md` | Core theoretical models guiding the study. |

---

## standards/

| File | Purpose |
| :--- | :--- |
| `adviser-writing-rules.md` | Adviser (Ma'am Era) writing rules and comments. |
| `documentation-discipline.md` | Rules for maintaining thesis documentation. |
| `documentation-format.md` | Shared formatting rules (metadata, headings, references). |
| `git-commit-standards.md` | Git commit message format and scopes. |
| `versioning.md` | Semantic versioning policy. |

> RRL standards (naming conventions, summary format, workflow) have moved to **BUDI-Literature**.

---

## thesis/ (root-level drafts)

| File | Purpose |
| :--- | :--- |
| `../thesis/paper/chapter-1.md` | Chapter 1 draft (Introduction), Finalized V5. |
| `../thesis/paper/chapter-1-objectively-written.md` | Chapter 1 objective-register variant. |
| `../thesis/paper/chapter-2.md` | Chapter 2 (RRL), **V3.0** — mirrors the 09.26 Drive V3 and covers all 26 Outline V4 leaves. |
| `../thesis/paper/chapter-1-evidence-map.md` | Claim-by-claim citation audit for Chapter 1. |
| `../thesis/paper/chapter-2-evidence-map.md` | Citation audit of Chapter 2 V3 against the RRL corpus, with open items. |

---

## Cross-References

| Task | Use |
| :--- | :--- |
| Understand what BUDI proposes to build | `archive/research-proposal/Research-Proposal.md` |
| Full app product requirements | `requirements-engineering/product-requirements-document.md` |
| Ground-truth systems/paper/models scope | `requirements-engineering/technical-specification.md` |
| Adopted model methodologies & implementation | `ml/` (index) + **BUDI-ML** (code and methodologies) |
| RRL corpus and scoring | **BUDI-Literature** |
