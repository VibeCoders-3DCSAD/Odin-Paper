# Odin Papers - Repository Index

- **Project:** Development of Odin: A Personal Budget Management System Using LSTM and Isolation Forest Algorithms
- **Institution:** University of Makati | Group 4, III-DCSAD
- **Repository root:** `Papers/`
- **Last indexed:** 2026-06-11
- **Indexing scope:** Bounded repo-intake over 1,746 text-like candidates from `git ls-files -co --exclude-standard`. Binary research assets such as PDFs, XLSX files, and ZIP archives were counted but not content-indexed.

---

## How to Use This Index

This is the navigation map for the Odin papers workspace. It is not a row-by-row bibliography registry; the RRL corpus is too large for that to stay accurate by hand. Use this index to find source-of-truth documents, folder roles, current counts, naming conventions, and known stale references.

| Need | Go to |
| :--- | :--- |
| Formal RP2 proposal, title, objectives, scope, deliverables, and references | `Documents/Research-Proposal.md` |
| Current detailed technical and paper specification | `Specification.md` |
| Product-facing app scope, user stories, confirmed screens, testing decisions | `Documents/PRD-Full-Odin-App.md` |
| Gap analysis between PRD and specification | `Documents/Specification-PRD-Alignment-Report.md` |
| Concrete checklist for revising `Specification.md` from the PRD | `Documents/Specification-Revision-Points-Based-on-PRD.md` |
| Model and algorithm implementation plan | `Documents/Model-&-Algorithm-Plan.md` |
| Open specification issues and validation work | `Open-Items.md` |
| RRL topic hierarchy and source-search plan | `Topic-Outline.md` |
| Chapter 1 purpose/description/significance draft | `CHAPTER-1/purpose-and-description.md` |
| Survey instrument and survey cleanup notes | `Survey/` |
| Data synthesis and model training handoffs | `Data/` |
| Local PDF-to-Markdown utility | `PDF-to-MD/README.md` |
| RRL source store, summaries, conversions, and compilations | `RRL/` |

---

## Repository Map

| Path | Purpose |
| :--- | :--- |
| `INDEX.md` | This file. Master navigation index for the papers workspace. |
| `Specification.md` | Detailed legal-style system and paper specification. Treat as the main technical contract, but reconcile with the PRD alignment reports before final submission. |
| `Topic-Outline.md` | Current RRL topic map. Defines 13 major topics and subtopic codes used by summaries, compilations, and drafting prompts. |
| `Legalize.md` | Legal-style technical specification writing guide. Use when normalizing structure, numbering, definitions, and cross-references. |
| `Open-Items.md` | Open validation items and unresolved specification decisions. |
| `CHAPTER-1/` | Chapter 1 drafting area. |
| `Data/` | Data sources, synthetic-data design, and model-training data handoffs. |
| `Documents/` | Proposal, PRD, model plan, alignment reports, panel feedback, screen descriptions, and meeting records. |
| `PDF-to-MD/` | Standalone local PDF-to-Markdown converter. |
| `RRL/` | Review of Related Literature workspace: PDFs, conversions, summaries, compilations, and helper scripts. |
| `Survey/` | Presurvey instrument and notes for adding/removing questions. |
| `.agents/` | Local assistant/runtime directory. Not thesis content. |
| `.codex` | Local assistant placeholder. Not thesis content. |
| `.gitattributes` | Git line-ending normalization. Not thesis content. |
| `.gitignore` | Ignores local assistant files, Claude/Codex guidance, Office lock/temp files, and local utility state. |

---

## Source-of-Truth Stack

| Layer | Source | Notes |
| :--- | :--- | :--- |
| Formal research proposal | `Documents/Research-Proposal.md` | Authoritative for RP2 framing, objectives, scope, deliverables, and reference list. |
| Product scope | `Documents/PRD-Full-Odin-App.md` | Current full-app PRD with 85 user stories, 16 confirmed primary screens, implementation decisions, and testing decisions. |
| Technical contract | `Specification.md` | Detailed system and paper specification. Contains unresolved notes and some PRD mismatches. |
| Reconciliation | `Documents/Specification-PRD-Alignment-Report.md` | Identifies critical/major/moderate/minor gaps between PRD and specification. |
| Revision plan | `Documents/Specification-Revision-Points-Based-on-PRD.md` | Editing checklist for bringing `Specification.md` into alignment with the PRD. |
| Issue list | `Open-Items.md` | Older/parallel list of RRL validation needs, definitions, threshold justifications, and cleanup items. |
| RRL map | `Topic-Outline.md` | Current topic taxonomy. Note: it now includes Topic 13, while `Specification.md` still references "the twelve topics" in places. |

---

## Top-Level Documents

| File | Purpose |
| :--- | :--- |
| `Specification.md` | Version 3.1 technical specification for Odin as a mobile-first/web-accessible personal finance management system for Filipino working young adults. Covers platform, transactions, profiles, categories, financial flows, budgeting, forecasting, anomaly detection, savings, debt, alerts, explainability, evaluation, privacy, scope, definitions, paper specification, timeline, and appendices. |
| `Topic-Outline.md` | RRL topic hierarchy and search prompts. Current topics cover Filipino young professionals, Filipino cultural finance, categorization, existing systems, profiling, forecasting, budget recommendation, anomaly detection, mobile-first design, privacy/trust, retention, evaluation, and savings/debt management. |
| `Legalize.md` | Writing/style guide for legal-style technical specifications. Useful for rewriting `Specification.md` sections consistently. |
| `Open-Items.md` | Actionable open items by specification article, including RRL validation needs, missing definitions, evaluation-threshold support, duplicate privacy text, and paper-spec corrections. |

---

## CHAPTER-1/

| File | Purpose |
| :--- | :--- |
| `purpose-and-description.md` | Current Chapter 1 draft covering description of the study, purpose of the study, significance of the study, and references. |

---

## Data/

Data sources, handoffs, and design notes for synthetic data generation and model training.

| File | Purpose |
| :--- | :--- |
| `data-synthesis-handoff.md` | Primary synthetic-data/model handoff. Covers Financial Behavioral Profiles, category hierarchy, schemas, dataset splits, synthetic generation, noise/event design, LSTM architecture, cold-start fallback, forecast horizons, and evaluation. |
| `model-training-data-design.md` | Defines training data shapes, sample rows, inputs/outputs, downstream connections, and key columns for Random Forest profile classification, LSTM spending forecasting, and Isolation Forest anomaly detection. |
| `synthetic-data-parameters-handoff.md` | Statistical parameter source handoff. Covers FIES/BSP aggregate tables, NCR 2023 reference values, blocked microdata-dependent parameters, generation pipeline, FBP parameterization, category allocation, and validation loops. |
| `2020-Philippine-Classification-of Individual-Consumption-According-to-Purpose.xlsx` | PCOICOP category reference workbook. Binary asset; not content-indexed. |
| `BSP-Data-on-Filipinos-in-Metro-Manila.xlsx` | BSP/NCR statistical workbook used for local income/expenditure grounding. Binary asset; not content-indexed. |
| `FIDashboard_1Q2023.pdf` | BSP Financial Inclusion Dashboard PDF. Binary asset; not content-indexed. |
| `Family Income and Expenditure.csv` | FIES-like CSV data source. Treat as data input/reference material, not prose. |
| `archive.zip` | Compressed data archive. Binary asset; contents not indexed. |
| `.codex` | Local assistant placeholder. Not thesis content. |

---

## Documents/

Formal thesis materials, product planning, specification reconciliation, screen descriptions, panel feedback, and meeting records.

| File or Folder | Purpose |
| :--- | :--- |
| `Research-Proposal.md` | Formal RP2 proposal. Authoritative for official project framing, objectives, scope, deliverables, and references. |
| `PRD-Full-Odin-App.md` | Full app PRD. Defines the product problem, solution, user stories, implementation decisions, testing decisions, out-of-scope list, and further notes. |
| `Specification-PRD-Alignment-Report.md` | Gap analysis comparing `Specification.md` and `PRD-Full-Odin-App.md`; flags conflicts around protected categories, smart defaults, reports, authentication, offline transaction entry, and model/retraining language. |
| `Specification-Revision-Points-Based-on-PRD.md` | Concrete revision checklist for updating `Specification.md`; highest priorities include protected categories, reports, authentication, offline-tolerant entry, onboarding alignment, frozen-model wording, ISO 25010 alignment, CSV/export cleanup, and unresolved-note cleanup. |
| `Model-&-Algorithm-Plan.md` | Module-by-module implementation plan for Financial Behavioral Profile classification, spending forecasting, budget recommendation, anomaly detection, cross-module integration, cloud inference, asynchronous updates, and open decisions. |
| `SCREEN-DESCRIPTIONS/` | Sixteen user-facing screen description files that match the PRD route map. |
| `Proposal Panel's Comments & Suggestions/Panel-Comments-and-Suggestions.md` | Organized summary of panel comments and required responses. |
| `Proposal Panel's Comments & Suggestions/Transcription-of-Comments-and-Suggestions.md` | Verbatim panel-defense Q&A transcription. Use when exact wording matters. |
| `Transcribed Group Sessions/4-24-meeting.md` | Internal group session notes from April 24. |

### Screen Descriptions

| File | Screen |
| :--- | :--- |
| `01-login-register.md` | Login / Register |
| `02-onboarding-questionnaire.md` | Onboarding Questionnaire |
| `03-profile-result.md` | Profile Result / Financial Behavioral Profile |
| `04-dashboard-overview.md` | Dashboard / Overview |
| `05-add-transaction.md` | Add Transaction |
| `06-transactions-history.md` | Transactions List / History |
| `07-recurring-transactions.md` | Recurring Transactions |
| `08-categories-settings.md` | Categories / Category Settings |
| `09-budget-setup.md` | Budget Setup |
| `10-budget-recommendation.md` | Budget Recommendation |
| `11-forecast-dashboard.md` | Forecast Dashboard |
| `12-alerts-anomaly-review.md` | Alerts / Anomaly Review |
| `13-savings-goals.md` | Savings Goals |
| `14-debt-accounts.md` | Debt Accounts |
| `15-reports-analytics.md` | Reports / Analytics |
| `16-settings-privacy-account.md` | Settings / Privacy / Account |

---

## Survey/

| File | Purpose |
| :--- | :--- |
| `PRESURVEY - ODIN.md` | Presurvey instrument for Filipino working young adults. Covers demographics, financial behavior, app literacy, budgeting challenges, user expectations, privacy/trust, cultural relevance, budgeting processes, desired outcomes, and open-ended expectations. |
| `presurvey-pdf-with-removal-notes.md` | Version of the presurvey with inline removal notes and final removal summary. |
| `Additional-Topics-To-Add.md` | Short list of additional survey topics, including device models for testing and anomaly alert sensitivity/alert fatigue. |

---

## PDF-to-MD/

Standalone local PDF-to-Markdown converter.

| File | Purpose |
| :--- | :--- |
| `README.md` | Usage instructions, requirements, CLI examples, browser UI instructions, and conversion limitations. |
| `pdf_to_md.py` | Python CLI converter. Requires Python 3.10+ and `pdftotext` in `PATH`. |
| `pdf_to_md_server.py` | Local web server exposing the browser conversion endpoint. |
| `index.html` | Browser UI shell. |
| `pdf-to-md.js` | Browser-side upload/conversion logic. |
| `markdown-preview.js` | Browser-side Markdown preview logic. |
| `styles.css` | Browser UI styling. |
| `.gitignore` | Ignore rules scoped to this utility. |

Typical usage:

```bash
python3 PDF-to-MD/pdf_to_md.py input.pdf -o output.md
python3 PDF-to-MD/pdf_to_md_server.py
```

The server UI runs at `http://127.0.0.1:8000` by default.

---

## RRL/

RRL is the largest and most active part of the workspace. The index lists folder roles and counts, not every paper.

| Path | Current Count | Purpose |
| :--- | ---: | :--- |
| `RRL/00_Bucket/` | 58 files | Raw/candidate PDF intake pool. All current files are PDFs. |
| `RRL/00_RRL/` | 1,256 files | Topic/subtopic-organized working corpus containing compilation files, marked conversions, summaries, and a small number of source PDFs. |
| `RRL/01_Papers/` | 223 files | Curated source-paper store: 222 PDFs plus `references.md`. |
| `RRL/02_Summaries/` | 222 files | Structured `_summarized.md` paper summaries. Fastest place to evaluate one paper's relevance. |
| `RRL/03_Conversions/` | 222 files | `_marked.md` Markdown conversions from source papers. |
| `RRL/04_Processing/` | 4 files | Active processing scripts/prompts for converting, summarizing, and moving papers. |
| `RRL/.claude/settings.local.json` | 1 file | Local Claude Code permissions/settings for RRL work. Not thesis prose. |

### RRL Root Files

| File | Purpose |
| :--- | :--- |
| `odin-app-report.md` | Q&A-style synthesis of Odin from repo materials. Useful for quick project recall. |
| `discusser.md` | Chapter 2 drafting handoff. Defines how to turn compilation files into dense academic RRL sections. |
| `themizer.md` | Thematic review table prompt for extracting theme-focused RRL tables from chronicles. |
| `compilefy.py` | Compiles sections from `_summarized.md` files into a folder-level `_Compilation.md`. |
| `chroniclefy.py` | Aggregates summarized files across subfolders into `chronicle.md`, with optional prefix and keyword filtering plus duplicate-content detection. |

### RRL/04_Processing Files

| File | Purpose |
| :--- | :--- |
| `Z_Marker.py` | Converts PDFs in a target directory into `_marked.md` files using `markitdown`, optionally creating empty `_summarized.md` files. |
| `Z_Mover.py` | Moves processed PDFs, `_marked.md`, and `_summarized.md` files from `04_Processing` into `01_Papers`, `03_Conversions`, and `02_Summaries`. |
| `0_Summarizer.md` | Machine-optimized YAML summary prompt for AI agents. |
| `Z_Summarizer.md` | Additional summarization prompt/instructions for RRL processing. |

### RRL Naming Conventions

Observed source prefixes:

| Prefix | Meaning |
| :--- | :--- |
| `L--` | Local or Philippine-focused source. |
| `I--` | International source. |
| `A--` | Algorithm/system/general technical source. |
| `AI--`, `IA--` | Algorithm/technical source with international designation. Prefix order is inconsistent across legacy files. |
| `AL--`, `LA--` | Algorithm/technical source with local designation. Prefix order is inconsistent across legacy files. |

Observed processing suffixes:

| Suffix | Meaning |
| :--- | :--- |
| `.pdf` | Source paper PDF. |
| `_marked.md` | Markdown conversion or marked text extracted from a paper. |
| `_summarized.md` | Structured review/summary for a paper. |
| `_Compilation.md` | Subtopic-level compilation of selected summary sections. |

### RRL Topic Reference

Current major topics from `Topic-Outline.md`:

| # | Topic |
| :---: | :--- |
| 1 | Filipino Young Professionals and the Financial Problem |
| 2 | Filipino Cultural Context in Personal Finance |
| 3 | Expense Categorization in Personal Finance Systems |
| 4 | Existing Personal Finance and Budget Management Systems |
| 5 | Financial Behavioral Profiling |
| 6 | Spending Forecasting |
| 7 | Budget Recommendation |
| 8 | Anomalous Spending Detection |
| 9 | Mobile-First Design |
| 10 | Data Privacy, Security, and User Trust |
| 11 | User Retention and Engagement |
| 12 | System Evaluation |
| 13 | Savings and Debt Management Algorithms |

### RRL/00_RRL/ Subtopic Folders

`RRL/00_RRL/` is organized according to `Topic-Outline.md`. Counts below are current file counts inside each subfolder.

| Folder | Files | Topic / Subtopic |
| :--- | ---: | :--- |
| `01_Irrelevant/` | 33 | Processed sources judged irrelevant or not useful. |
| `1.A/` | 35 | Filipino Young Professionals as a Demographic |
| `1.B/` | 35 | Financial Structure of Filipino Young Professionals |
| `1.C/` | 89 | Financial Behavior of Filipino Young Professionals |
| `2.A/` | 37 | Culturally Specific Financial Practices |
| `2.B/` | 13 | Seasonal and Cyclical Spending Patterns |
| `2.C/` | 3 | User-Declared Financial Preferences |
| `3.A/` | 27 | Expense Categorization Frameworks |
| `3.B/` | 11 | Expense Category Design Considerations |
| `4.A/` | 57 | Landscape of Existing Systems |
| `4.B/` | 55 | Limitations and Gaps in Existing Systems |
| `5.A/` | 113 | Financial Behavioral Profiles in Personal Finance |
| `5.B/` | 17 | Profile Dynamics and the Cold-Start Problem |
| `5.C/` | 99 | Financial Behavioral Profile Classification Algorithm |
| `6.A/` | 97 | Predictive Modeling in Personal Finance Systems |
| `6.B/` | 71 | Spending Forecasting Algorithm |
| `7.A/` | 41 | Budgeting Strategies as Domain Knowledge |
| `7.B/` | 41 | Budget Recommendation in Personal Finance Systems |
| `7.C/` | 21 | Budget Recommendation Algorithm |
| `8.A/` | 87 | Anomaly Detection in Personal Finance Systems |
| `8.B/` | 55 | Anomaly Detection Algorithm |
| `9.A/` | 11 | Mobile-First Design Principles and Rationale |
| `9.B/` | 0 | Mobile UX Design for Personal Finance. No folder currently present. |
| `10.A/` | 33 | Data Privacy and Security in Personal Finance Systems |
| `10.B/` | 29 | User Trust in Personal Finance Systems |
| `11.A/` | 15 | Engagement Dynamics in Personal Finance Applications |
| `11.B/` | 7 | Retention Mechanisms and Engagement Design |
| `12.A/` | 31 | Evaluation Frameworks for Personal Finance Systems |
| `12.B/` | 93 | Evaluation of Algorithmic Modules |
| `13.A/` | 0 | Savings Goal Management in PFMS. No folder currently present. |
| `13.B/` | 0 | Debt Management in PFMS. No folder currently present. |

### RRL Workflow

Recommended workflow for adding or using literature:

1. Put candidate PDFs in `RRL/00_Bucket/` or `RRL/04_Processing/`.
2. Convert PDFs with `RRL/04_Processing/Z_Marker.py` or the `PDF-to-MD/` utility.
3. Fill the matching `_summarized.md` file using `RRL/04_Processing/0_Summarizer.md` or `RRL/04_Processing/Z_Summarizer.md`.
4. Move processed files from `RRL/04_Processing/` into the curated stores using `RRL/04_Processing/Z_Mover.py`.
5. Copy or place relevant `_marked.md`, `_summarized.md`, and `_Compilation.md` files into the matching `RRL/00_RRL/<topic-subtopic>/` folder.
6. Run `RRL/compilefy.py` for the relevant topic folder to update that folder's `_Compilation.md`.
7. Draft Chapter 2 topic sections from compilation files using `RRL/discusser.md`.

Important stale references from older notes: `RRL/topic-outline.md`, `RRL/markify.py`, `RRL/movify.py`, `RRL/summarizer.md`, `RRL/02_Reviews/`, and `RRL/03_Related Literature/` are not present in the current tree. Use `Topic-Outline.md`, `RRL/04_Processing/Z_Marker.py`, `RRL/04_Processing/Z_Mover.py`, `RRL/02_Summaries/`, and `RRL/03_Conversions/` instead.

---

## Cross-References

| Task | Use |
| :--- | :--- |
| Explain what Odin officially proposes to build | `Documents/Research-Proposal.md` |
| Understand full app product requirements | `Documents/PRD-Full-Odin-App.md` |
| Implement or defend detailed system rules | `Specification.md` |
| Fix specification/PRD mismatches | `Documents/Specification-PRD-Alignment-Report.md` and `Documents/Specification-Revision-Points-Based-on-PRD.md` |
| Review unresolved validation items | `Open-Items.md` |
| Plan ML/model implementation | `Documents/Model-&-Algorithm-Plan.md`, `Data/model-training-data-design.md`, and `Data/data-synthesis-handoff.md` |
| Ground synthetic data parameters | `Data/synthetic-data-parameters-handoff.md` and local data workbooks in `Data/` |
| Use or revise the survey | `Survey/PRESURVEY - ODIN.md`, `Survey/presurvey-pdf-with-removal-notes.md`, and `Survey/Additional-Topics-To-Add.md` |
| Draft RRL topic sections | `Topic-Outline.md`, relevant `RRL/00_RRL/<topic>/` compilation files, and `RRL/discusser.md` |
| Quickly evaluate one paper's relevance | Matching file in `RRL/02_Summaries/` or `_summarized.md` in `RRL/00_RRL/` |
| Convert a PDF locally | `PDF-to-MD/README.md` or `RRL/04_Processing/Z_Marker.py` |
| Move processed PDFs/conversions/summaries into curated RRL stores | `RRL/04_Processing/Z_Mover.py` |

---

## Git/Tracking Notes

Current working tree items observed during this update:

| Path | Status |
| :--- | :--- |
| `Documents/PRD-Full-Odin-App.md` | Modified before this index update. Not changed by this update. |
| `Documents/Specification-PRD-Alignment-Report.md` | Untracked before this index update. Indexed here as an active repo document. |
| `Documents/Specification-Revision-Points-Based-on-PRD.md` | Untracked before this index update. Indexed here as an active repo document. |

Do not assume untracked files are safe to remove; they may be active research or planning artifacts.
