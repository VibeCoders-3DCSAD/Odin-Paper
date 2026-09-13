# Odin-Paper — Documentation Index

- **Project:** Development of BUDI: A Personalized Intelligent Finance Management Application for Filipinos Using Classification, Forecasting, Optimization, and Anomaly Detection Models for Improving Savings and Debt
- **Institution:** University of Makati | Group 4, III-DCSAD
- **Last indexed:** 2026-09-13

---

> **Ground truth:** the authoritative versions of the thesis documents live in the Google Drive folder. Copies in this repository are working mirrors and may lag behind the Drive source — verify before citing.

---

## How to Use This Index

| Need | Go to |
| :--- | :--- |
| Formal research proposal, objectives, scope | `archive/research-proposal/Research-Proposal.md` |
| System specification (working contract) | `requirements-engineering/system-spec.md` |
| Product requirements (PRD) | `requirements-engineering/product-requirements-document.md` |
| Functional requirements per module | `requirements-engineering/requirements-engineering.md` |
| Chapter drafts | `thesis/paper/chapter-1.md` |
| ML model design and training docs | `ml/README.md` |
| Screen descriptions (24 screens) | `design-architecture/screen-descriptions/00-index.md` |
| System architecture and data schema | `design-architecture/system-architecture.md` |
| RRL benchmarks | `rrl/benchmarks.md` |
| Survey instrument | `assessment-evaluation/survey/PUEPS.md` |
| Git commit and documentation standards | `standards/` |
| RRL corpus and scoring | **Odin-Literature** |
| ML service and training pipeline | **Odin-ML** |

---

## Repository Map

| Path | Purpose |
| :--- | :--- |
| `assessment-evaluation/` | Survey instruments and evaluation materials. |
| `archive/` | Preserved research proposal, panel comments, and superseded documents. |
| `design-architecture/` | System architecture, data schema, and screen descriptions. |
| `ml/` | ML model design, data analysis, and training documentation. |
| `planning-management/` | Roadmap and meeting transcripts. |
| `requirements-engineering/` | System spec, PRD, and functional requirements. |
| `rrl/` | RRL benchmarks, literature matrix, and theoretical framework. |
| `standards/` | Documentation, versioning, and git commit standards. |
| `thesis/` | Thesis paper drafts. |

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

Model design, data analysis, and training documentation. See `ml/README.md` for the phase-by-phase index.

| Path | Purpose |
| :--- | :--- |
| `ml/1_problem-statement/` | MDDs, feature sets, module integration, deployment, synthetic data rules. |
| `ml/2_data-collection/` | FIES/BSP data source documentation. |
| `ml/3_data-preprocessing/` | Preprocessing pipeline documentation. |
| `ml/4_eda/` | Exploratory data analysis guide. |
| `ml/4.5_dimension-threshold-discovery/` | PFP dimension and threshold discovery. |
| `ml/5_feature-engineering/` | Feature engineering pipeline documentation. |
| `ml/6_model-training/` | PFP, Forecaster, and Anomaly training documentation. |
| `ml/README.md` | ML documentation index. |
| `ml/TODO.md` | Known gaps and follow-up tasks. |

---

## planning-management/

| File | Purpose |
| :--- | :--- |
| `roadmap.md` | Milestones, timeline, and Gantt references. |
| `transcripts/4-24-meeting.md` | Group session notes. |

---

## requirements-engineering/

| File | Purpose |
| :--- | :--- |
| `system-spec.md` | System specification (working contract). |
| `product-requirements-document.md` | Product requirements document. |
| `requirements-engineering.md` | Functional requirements per module. |

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
| `documentation-discipline.md` | Rules for maintaining thesis documentation. |
| `documentation-format.md` | Shared formatting rules (metadata, headings, references). |
| `git-commit-standards.md` | Git commit message format and scopes. |
| `versioning.md` | Semantic versioning policy. |
| `rrl-naming-conventions.md` | **Deprecated.** RRL naming rules now live in Odin-Literature. |
| `rrl-workflow.md` | **Deprecated.** RRL workflow now lives in Odin-Literature. |
| `summary-format.md` | **Deprecated.** RRL summary schema now lives in Odin-Literature. |

---

## thesis/

| File | Purpose |
| :--- | :--- |
| `paper/chapter-1.md` | Chapter 1 draft (Introduction). |
| `paper/chapter-1-evidence-map.md` | Claim-by-claim citation audit for Chapter 1. |

---

## Cross-References

| Task | Use |
| :--- | :--- |
| Understand what BUDI proposes to build | `archive/research-proposal/Research-Proposal.md` |
| Full app product requirements | `requirements-engineering/product-requirements-document.md` |
| Detailed system rules | `requirements-engineering/system-spec.md` |
| Model implementation | `ml/` (design docs) + **Odin-ML** (code) |
| RRL corpus and scoring | **Odin-Literature** |
