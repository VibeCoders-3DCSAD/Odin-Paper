# Odin Papers - Repository Index

**Project:** Development of Odin: A Personal Budget Management System Using LSTM and Isolation Forest Algorithms  
**Institution:** University of Makati | Group 4, III-DCSAD  
**Last indexed:** 2026-05-31

---

## How to Use This Index

This is the navigation map for the Odin papers workspace. It is not a bibliography registry. The RRL corpus is large and changes often, so this index lists the directory roles, naming conventions, counts, and source-of-truth files instead of trying to hand-maintain a row for every paper.

Start here when opening a new session:

| Need | Go to |
| :--- | :--- |
| Official project title, objectives, scope, deliverables, and references | `Documents/Research-Proposal.md` |
| Current working system concept and module inventory | `BIBLE.md` |
| Chapter 1 purpose, description, and significance draft | `CHAPTER-1/purpose-and-description.md` |
| Data/model training design | `Data/model-training-data-design.md` |
| Synthetic data generation architecture | `Data/data-synthesis-handoff.md` |
| Statistical parameter handoff for synthetic data | `Data/synthetic-data-parameters-handoff.md` |
| RRL topic map and source-search plan | `RRL/topic-outline.md` |
| Fast Q&A summary of Odin | `RRL/odin-app-report.md` |
| Panel feedback and revision requirements | `Documents/Proposal Panel's Comments & Suggestions/Panel-Comments-and-Suggestions.md` |
| Local PDF-to-Markdown utility | `PDF-to-MD/README.md` |

---

## Repository Map

| Path | Purpose |
| :--- | :--- |
| `INDEX.md` | This file. Master navigation index for the workspace. |
| `BIBLE.md` | Broad working bible for Odin's platform, target users, inputs, modules, expense categories, ML components, and paper outline. This is a live planning document, not the formal proposal. |
| `CHAPTER-1/` | Chapter 1 drafting area. Currently contains the purpose, description, and significance draft. |
| `Data/` | Data sources and methodology documents for synthetic data generation and model training. |
| `Documents/` | Formal proposal, pre-survey instrument, panel comments, and meeting/transcription records. |
| `PDF-to-MD/` | Standalone local utility for converting PDFs to Markdown through CLI or browser UI. |
| `RRL/` | Review of Related Literature workspace: source PDFs, converted/marked papers, summaries, compilations, and helper scripts. |
| `.agents/` | Local assistant/runtime directory. Not thesis content. |
| `.codex` | Local assistant placeholder. Not thesis content. |
| `.gitattributes` | Git line-ending normalization. Not thesis content. |
| `.gitignore` | Ignores local assistant files, Claude/Codex guidance, and Office lock/temp files. Not thesis content. |

---

## CHAPTER-1/

| File | Purpose |
| :--- | :--- |
| `purpose-and-description.md` | Current Chapter 1 draft covering the description of the study, purpose of the study, significance of the study, and references. Defines Odin as a web/mobile PBMS for Filipino young professionals in Metro Manila using financial behavioral profiling, LSTM-based spending forecasts, Isolation Forest anomaly alerts, savings tracking, and debt management support. |

---

## Data/

Data sources, handoffs, and design notes for the synthetic data and ML pipeline.

| File | Purpose |
| :--- | :--- |
| `model-training-data-design.md` | Defines the training data shapes, sample rows, inputs, outputs, model connections, and key columns for Random Forest profile classification, LSTM spending forecasting, and Isolation Forest anomaly detection. Use this when designing datasets or explaining how model outputs feed downstream modules. |
| `data-synthesis-handoff.md` | Primary architecture document for the synthetic data/model pipeline. Covers Financial Behavioral Profiles, category hierarchy, data schema, dataset splits, synthetic generation parameters, event/noise design, LSTM architecture, cold-start fallback, and forecasting horizons. |
| `synthetic-data-parameters-handoff.md` | Detailed handoff for statistical parameter sources. Covers values derivable from FIES/BSP aggregate tables, blocked parameters pending PSA microdata, CV-bound workarounds, and self-validation for synthetic data. |
| `BSP-Data-on-Filipinos-in-Metro-Manila.xlsx` | Primary local statistical workbook. Use for NCR income/expenditure aggregates and category shares when grounding synthetic data values. |
| `Family Income and Expenditure.csv` | Old FIES-like microdata CSV. Treat as structural reference only unless separately validated; do not treat as the current NCR ground truth for spending means. Currently untracked. |
| `FIDashboard_1Q2023.pdf` | BSP Financial Inclusion Dashboard. Useful for financial inclusion context; not the main source for category-level spending variability. |
| `archive.zip` | Compressed archive in `Data/`. Contents not indexed. Currently untracked. |
| `.codex` | Local assistant placeholder. Not thesis content. |

---

## Documents/

Formal thesis materials, survey instruments, panel feedback, and meeting records.

| File | Purpose |
| :--- | :--- |
| `Research-Proposal.md` | Formal RP2 proposal. Authoritative source for project title, context, objectives, scope and limitations, deliverables, evaluation plan, and reference list. |
| `PRESURVEY - ODIN.md` | Public user expectations/perception survey instrument for Filipino young professionals in Metro Manila. Covers demographics, financial management behavior, app literacy, budgeting challenges, expectations, trust/privacy, and cultural relevance. |
| `Proposal Panel's Comments & Suggestions/Panel-Comments-and-Suggestions.md` | Organized summary of proposal panel feedback and required responses. |
| `Proposal Panel's Comments & Suggestions/Transcription-of-Comments-and-Suggestions.md` | Verbatim panel-defense Q&A transcription. Use when exact wording matters. |
| `Transcribed Group Sessions/4-24-meeting.md` | Internal group session notes from April 24 covering design decisions and open issues. |

---

## PDF-to-MD/

Standalone local PDF-to-Markdown converter.

| File | Purpose |
| :--- | :--- |
| `README.md` | Usage instructions, requirements, CLI examples, and browser UI instructions. |
| `pdf_to_md.py` | Python CLI converter. Requires Python 3.10+ and `pdftotext` in `PATH`. |
| `pdf_to_md_server.py` | Local web server exposing the browser conversion endpoint. |
| `index.html` | Browser UI shell. |
| `pdf-to-md.js` | Browser-side conversion/upload logic. |
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

RRL is the largest and most active part of the workspace. It now uses the following current structure:

| Path | Current Count | Purpose |
| :--- | ---: | :--- |
| `RRL/00_Bucket/` | 167 files | Raw/candidate PDFs and unused or not-yet-processed literature. Use as the intake pool. |
| `RRL/00_RRL/` | 1,256 files | Topic/subtopic-organized RRL working corpus. Contains topic compilation files, marked conversions, summaries, and a small number of source PDFs. |
| `RRL/01_Papers/` | 135 files | Curated source-paper store: 134 PDFs plus `references.md`. |
| `RRL/02_Reviews/` | 118 files | Structured `_summarized.md` reviews. These are the fastest files to read when evaluating a paper's relevance. |
| `RRL/03_Related Literature/` | 119 files | Converted/usable Markdown literature files for Chapter 2 writing. |
| `RRL/04_Processing/` | 31 files | Active processing scratch area for papers in conversion/marking/summarization. |
| `RRL/.claude/settings.local.json` | 1 file | Local Claude Code permissions/settings for RRL work. Not thesis prose. |

### RRL Root Files

| File | Purpose |
| :--- | :--- |
| `topic-outline.md` | Current RRL topic hierarchy. This is the source of truth for topic/subtopic names, shorthand tags, and search prompts. |
| `odin-app-report.md` | Q&A-style synthesis of Odin from existing repo materials. Useful for onboarding or quick project recall. |
| `discusser.md` | Chapter 2 drafting handoff. Defines how to turn compilation files into dense academic RRL sections. |
| `summarizer.md` | Summary prompt/instructions for turning marked/converted papers into structured summaries. |
| `themizer.md` | Theming or synthesis helper prompt for RRL work. |
| `markify.py` | Converts PDFs in a target directory into `_marked.md` files using `markitdown`, then creates empty `_summarized.md` placeholders. Requires the `markitdown` package. |
| `compilefy.py` | Extracts TL;DR, Findings, Relevance to Odin, and Limitations from `_summarized.md` files in one directory into a `<directory>_Compilation.md` file. |
| `chroniclefy.py` | Aggregates summarized files across subfolders into a root chronicle with optional prefix and keyword filters and duplicate-content detection. |
| `movify.py` | Moves PDFs from allowed RRL folders into `01_Papers/`; refuses to process `0`-prefixed folders. |

### RRL Naming Conventions

Observed source prefixes:

| Prefix | Meaning |
| :--- | :--- |
| `L--` | Local or Philippine-focused source. |
| `I--` | International source. |
| `A--` | Algorithm/system/general technical source. |
| `AI--` | Algorithm/technical source with international designation. |
| `AL--` | Algorithm/technical source with local designation. |

Observed processing suffixes:

| Suffix | Meaning |
| :--- | :--- |
| `.pdf` | Source paper PDF. |
| `_marked.md` | Markdown conversion or marked text extracted from a paper. |
| `_summarized.md` | Structured review/summary for a paper. |
| `_Compilation.md` | Subtopic-level compilation of selected summary sections. |

### RRL/00_RRL/ Subtopic Folders

`RRL/00_RRL/` is organized according to `RRL/topic-outline.md`. Counts below are current file counts inside each subfolder.

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

### RRL Topic Reference

Current major topics from `RRL/topic-outline.md`:

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

### RRL Workflow

Recommended workflow for adding or using literature:

1. Put candidate PDFs in `RRL/00_Bucket/` or the active processing folder.
2. Convert/mark PDFs into Markdown using `RRL/markify.py` or the `PDF-to-MD/` utility.
3. Create or fill the matching `_summarized.md` file using `RRL/summarizer.md`.
4. Place or copy the paper outputs into the relevant `RRL/00_RRL/<topic-subtopic>/` folder.
5. Run `RRL/compilefy.py` inside the relevant topic folder to update that folder's `_Compilation.md`.
6. Draft Chapter 2 sections from compilation files using `RRL/discusser.md`.

Important: older index references to `RRL/README.md`, `RRL/registry.md`, `RRL/01_Reviews/`, `RRL/02_Related Literature/`, `RRL/03_Skills/`, and `RRL/04_Definition of Terms/` are stale. Those paths are not present in the current tree.

---

## Cross-References

| Task | Use |
| :--- | :--- |
| Explain what Odin is officially supposed to build | `Documents/Research-Proposal.md` |
| Reconcile current architecture/module ideas | `BIBLE.md` |
| Write Chapter 1 purpose/significance language | `CHAPTER-1/purpose-and-description.md` |
| Justify or shape synthetic model-training columns | `Data/model-training-data-design.md` |
| Design synthetic data generation | `Data/data-synthesis-handoff.md` and `Data/synthetic-data-parameters-handoff.md` |
| Find local spending/income aggregates | `Data/BSP-Data-on-Filipinos-in-Metro-Manila.xlsx` |
| Use pilot survey wording | `Documents/PRESURVEY - ODIN.md` |
| Address panel comments | `Documents/Proposal Panel's Comments & Suggestions/Panel-Comments-and-Suggestions.md` |
| Draft RRL topic sections | `RRL/topic-outline.md`, relevant `RRL/00_RRL/<topic>/` compilation files, and `RRL/discusser.md` |
| Quickly evaluate one paper's relevance | Matching file in `RRL/02_Reviews/` or `_summarized.md` in `RRL/00_RRL/` |
| Convert a PDF locally | `PDF-to-MD/README.md` or `RRL/markify.py` |
| Move processed PDFs into the paper store | `RRL/movify.py` |

---

## Git/Tracking Notes

Current untracked items observed during this update:

| Path | Note |
| :--- | :--- |
| `Data/Family Income and Expenditure.csv` | Present in workspace but not tracked by git. |
| `Data/archive.zip` | Present in workspace but not tracked by git. |
| `PDF-to-MD/` | Present in workspace but not tracked by git. |

Do not assume untracked files are safe to remove; they may be local research assets or active utilities.
