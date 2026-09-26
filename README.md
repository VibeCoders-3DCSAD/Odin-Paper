# BUDI-Base

Knowledge base for the thesis **"Development of BUDI: A Personalized Intelligent Finance Management Application for Filipinos Using Classification, Forecasting, Optimization, and Anomaly Detection Models for Improving Savings and Debt"** by Group 4, III-DCSAD, University of Makati.

## Purpose

This repository contains thesis documents, specifications, PRDs, and survey instruments. It does **not** contain RRL processing — that lives in **BUDI-Literature**.

> **Ground truth:** the authoritative versions of the thesis documents live in the Google Drive folder. Copies in this repository are working mirrors and may lag behind the Drive source — verify before citing.

## Quick Navigation

| Document | Path |
|----------|------|
| Master index | `INDEX.md` |
| Agent guide | `AGENTS.md` |
| Documentation index | `docs/INDEX.md` |
| Topical outline | `google-drive/topical-outline/GROUP4 - TOPICAL OUTLINE - V3 - 09.15.26.docx` |
| Technical specification (Drive mirror, ground truth) | `docs/requirements-engineering/technical-specification.md` |
| Chapter drafts | `thesis/paper/chapter-1.md`, `thesis/paper/chapter-2.md` |
| Product requirements | `docs/requirements-engineering/product-requirements-document.md` |
| Research proposal | `docs/archive/research-proposal/Research-Proposal.md` |
| RRL corpus & scoring | **BUDI-Literature** |

> **Spec update (2026-09-24):** the Drive *Technical Specification V1 (09.24.2026)* is
> the ground truth. It is a substantial rewrite — project identity is now **TAYA**,
> built on SARIMA with FIES 2023 + HFCE 2022 Q1–2026 Q2 temporal disaggregation and a
> central Financial Plan artifact. See `AGENTS.md` and
> `docs/requirements-engineering/technical-specification.md`.

## Git LFS

Source PDFs in `archived-literature/papers/` are tracked via Git LFS. After cloning:

```bash
git lfs pull
```

These PDFs will be migrated to BUDI-Literature when verified against the new topical outline.
