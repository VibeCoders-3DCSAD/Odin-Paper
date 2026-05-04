# Odin Papers — Repository Index

**Project:** Development of Odin: A Personal Budget Management System Using LSTM and Isolation Forest Algorithms
**Institution:** University of Makati | Group 4, III-DCSAD
**Last indexed:** 2026-05-04

---

## How to Use This Index

Every file and directory in this repository is listed here with its purpose. Use this as the first document to read when starting a new session. Files marked `[OUTDATED]` contain a warning in their content — verify before relying on them.

---

## Root

| File / Dir | Purpose |
| :--- | :--- |
| `INDEX.md` | This file. Master navigation index for all agents and team members. |
| `algorithm-approach-comparison.md` | Documents the decision between a multi-ML design (Option A) vs. a single-ML design (Option B). Concludes that LSTM is the only ML model; all other system functions (profile assignment, overage detection, budget recommendation) are rule-based. Use this when justifying the algorithm architecture in Chapter 3 or in panel responses. |
| `.gitattributes` | Git line-ending config. Not thesis content. |
| `.gitignore` | Ignores `.codex`, `.claude`, `AGENTS.md`, `CLAUDE.md`, and Office temp/lock files (`~$*`, `.~lock.*#`). Means AI assistant state files and Claude Code settings are never committed. Not thesis content. |
| `.codex` | Empty placeholder. No content. |

---

## CHAPTER-1/

Working directory for Chapter 1 (Introduction) content.

| File | Purpose |
| :--- | :--- |
| `definition-of-terms-guide.md` | Standards and rules for writing narrative-style Definition of Terms. Covers the two definition types (conceptual vs. operational), formatting rules, common mistakes, and a template. Read this before drafting any definition. |
| `definition-of-terms-list.md` | The ordered working list of all 18 terms to be defined (plus 3 under discussion). Contains draft definitions, citation status, and gaps marked `NO DIRECT REFERENCE`. This is the active drafting document for the Definition of Terms section. |
| `Scratch/scratch.md` | Scaffold for all Chapter 1 sections with placeholder text. Contains the current in-progress draft of the Definition of Terms section including rough definitions for terms 1–16. This is the actual chapter draft — write Chapter 1 content here. |

---

## Data/

All datasets, handoff documents, and reference files for synthetic data generation and model training.

| File | Purpose |
| :--- | :--- |
| `data-synthesis-handoff.md` | **Primary architecture document for the data and model pipeline.** Covers: Financial Behavioral Profiles (FBPs), category hierarchy (2nd node), data schema, dataset splits, synthetic data generation parameters, noise event design (BSP/legally verified), LSTM model architecture, cold-start fallback logic, and forecasting horizons. Start here when working on the ML pipeline, Chapter 3 methodology, or synthetic data generation. |
| `synthetic-data-parameters-handoff.md` | Detailed breakdown of statistical parameter sources. Covers what can be computed from FIES aggregate tables (mu per category, CV total expenditure), what is blocked pending PSA microdata (sigma per category, median, skewness), the workaround using CV bounds from FBP design, and the full synthetic data generation pipeline with self-validation loop. Use alongside `data-synthesis-handoff.md` when generating or justifying the synthetic dataset. |
| `BSP-Data-on-Filipinos-in-Metro-Manila.xlsx` | **Primary statistical source.** BSP FIES aggregate tables (Tables 1-7) for 2018, 2021, and 2023 NCR data. Use Table 2 for average annual expenditure (divide by 12 for monthly mu), Table 7 for category share breakdowns, Table 1 for income ranges per decile. This is the ground truth for mu values. |
| `Family Income and Expenditure.csv` | Old Kaggle FIES microdata (~2015 vintage), national scope, 41,544 rows (NCR subset = 4,130 rows). **Do not use for mu values — data is too old and not NCR-specific.** May be used only for structural reference (column names, category labels). |
| `FIDashboard_1Q2023.pdf` | BSP Financial Inclusion Dashboard Q1 2023. Contains access, savings, and credit metrics for the Philippines. **Not useful for spending variability or CV values.** Useful only for financial inclusion statistics cited in the project context. |
| `archive.zip` | Untracked compressed archive. Contents unknown. Not part of the thesis pipeline. |
| `.codex` | Empty placeholder. No content. |

---

## Documents/

Meeting records, panel defense outputs, and the formal research proposal.

| File | Purpose |
| :--- | :--- |
| `Research-Proposal.md` | **Full formal research proposal (RP2 format).** Contains the complete project context, objectives (general and specific), scope and limitations, deliverables, and all references. This is the authoritative statement of what the study is, what it will build, and what it will evaluate. Use as the source of truth for objectives and scope when writing any chapter. |
| `Panel-Comments-and-Suggestions.md` | Organized, clean summary of all panel defense feedback from the three panelists (Baccay Plan, Congzon, Dellosa). Records the panel's requirements and the group's responses. Key outcomes: panel requires a clustering or classification algorithm for profile assignment; panel requires profile change tracking over time. Use this when addressing panel revisions. |
| `Transcription-of-Comments-and-Suggestions.md` | **Verbatim transcription** of the panel defense Q&A session. Same content as `Panel-Comments-and-Suggestions.md` but in raw dialogue form. Use when the exact wording of a panel question or response matters. |
| `Transcribed Group Sessions/4-24-meeting.md` | Notes from the internal group session on April 24. Covers design decisions on LSTM/Isolation Forest interaction, budgeting feature logic, fixed expense tracking, behavioral profiling dimensions, and data requirements. Use when reconciling internal design discussions against the formal proposal. |

---

## RRL/

Review of Related Literature working directory. Full pipeline documentation is in `RRL/README.md`.

| File / Dir | Purpose |
| :--- | :--- |
| `README.md` | `[OUTDATED]` Full documentation of the RRL system: the 7-step paper pipeline, topic system (15 topics), designation rules (local / international / algorithm-specific), citation recency rules (2023-2026), member checklist workflow, and quota rules (25 local + 25 international = 50 total). Read this to understand how the RRL directory works before adding or searching for papers. |
| `registry.md` | `[OUTDATED]` Master one-row-per-paper index. Contains all processed papers with paper ID, designation, year, authors, title, venue, topics covered, shorthand tags, and notes. Also tracks quota status (local / international / algorithm-specific counts). Search this by topic number or shorthand tag to find relevant papers when writing RRL sections. |
| `Registry.ods` | LibreOffice Calc version of the registry. May be more current than `registry.md`. Use to cross-check quota counts. |
| `topic-outline.md` | `[OUTDATED]` Hierarchical mind map of all 15 RRL topics (A through J) with specific sub-subtopics and ready-to-paste Google Scholar queries. Use when searching for new papers on a specific claim. Each node has a `[/shorthand]` tag used in the registry's `shorthand_tags` column. |
| `odin-app-report.md` | Q&A-style report answering 10 questions about Odin (purpose, modules, architecture, etc.) by synthesizing materials already in the repo. Each answer includes links to source documents. Useful as a fast onboarding document for agents or team members starting a new session without prior context. |
| `.claude/settings.local.json` | Claude Code permission settings scoped to the RRL subdirectory. Grants WebSearch and WebFetch access to: `sciencedirect.com`, `papers.ssrn.com`, `researchgate.net`, `bsp.gov.ph`, `link.springer.com`. Allows agents to fetch papers from these domains when running the RRL pipeline. |

### RRL/00_Bucket/

Raw PDFs of candidate papers not yet processed through the pipeline. These are unreviewed sources — they have no converted MD, no summary, and no registry entry. File naming convention: plain `Author.pdf` or `Author_et-al.pdf`.

| File | Notes |
| :--- | :--- |
| `Alvarina_et-al.pdf` | Pending pipeline |
| `Asi_et-al.pdf` | Pending pipeline (converted MD already exists in `02_Related Literature/`) |
| `Ataza_et-al.pdf` | Pending pipeline |
| `Bayangos_Lubangco.pdf` | Pending pipeline |
| `Bongado_et-al.pdf` | Pending pipeline |
| `Bongalonta_et-al.pdf` | Pending pipeline |
| `BSP-(2026).pdf` | Pending pipeline |
| `Canalog_et-al.pdf` | Pending pipeline |
| `Casalhay_et-al.pdf` | Pending pipeline |
| `Co_Centeno.pdf` | Pending pipeline |
| `D.-A.-G._et-al.pdf` | Pending pipeline |
| `Dela-Torre_et-al.pdf` | Pending pipeline |
| `Domingo.pdf` | Pending pipeline |
| `Elliyana.pdf` | Pending pipeline |
| `Espiritu.pdf` | Pending pipeline |
| `Estorba_et-al.pdf` | Pending pipeline |
| `Flores.pdf` | Pending pipeline |
| `Gabatin_et-al.pdf` | Pending pipeline |
| `Garcia.pdf` | Pending pipeline |
| `Gavino_et-al.pdf` | Pending pipeline |
| `Gonzales_Campos.pdf` | Pending pipeline |
| `Hurley_et-al.pdf` | Pending pipeline |
| `Jandoc_et-al.pdf` | Pending pipeline |
| `Jumawan-Powao_et-al.pdf` | Pending pipeline |
| `Kusumaningsih_et-al.pdf` | Pending pipeline |
| `Lambert_et-al.pdf` | Pending pipeline |
| `Lim_Cordova.pdf` | Pending pipeline |
| `Lusardi_Mitchell.pdf` | Pending pipeline |
| `Machireddy.pdf` | Pending pipeline |
| `Mamadiyarov_et-al.pdf` | Pending pipeline |
| `Manatad_Labitad.pdf` | Pending pipeline |
| `Manlongat_et-al.pdf` | Pending pipeline |
| `Maria.pdf` | Pending pipeline |
| `Maruf_et-al.pdf` | Pending pipeline |
| `M.-D.-Mercado_et-al.pdf` | Pending pipeline |
| `Montuerto_Gimena.pdf` | Pending pipeline |
| `Nasih_Adam.pdf` | Pending pipeline |
| `Natal_et-al.pdf` | Pending pipeline |
| `Navarro_Bantulo.pdf` | Pending pipeline |
| `Nourallah_et-al.pdf` | Pending pipeline |
| `Paghasian.pdf` | Pending pipeline |
| `Pagobo_et-al.pdf` | Pending pipeline |
| `Palada_et-al.pdf` | Pending pipeline |
| `Philippine-Statistics-Authority.pdf` | Pending pipeline |
| `Pinca_et-al.pdf` | Pending pipeline |
| `Quindoza_et-al.pdf` | Pending pipeline |
| `Raya.pdf` | Pending pipeline |
| `Razalan.pdf` | Pending pipeline |
| `Remonde.pdf` | Pending pipeline |
| `Rodriguez-Correa_et-al.pdf` | Pending pipeline |
| `Rodriguez_et-al.pdf` | Pending pipeline |
| `Romero.pdf` | Pending pipeline |
| `R.-T.-Mercado_et-al.pdf` | Pending pipeline |
| `Sabri_et-al.pdf` | Pending pipeline |
| `Sarmiento_et-al.pdf` | Pending pipeline |
| `Sinnewe_Nicholson.pdf` | Pending pipeline |
| `Somera.pdf` | Pending pipeline |
| `Teh_et-al.pdf` | Pending pipeline |
| `Templa_et-al.pdf` | Pending pipeline |
| `Torres_et-al.pdf` | Pending pipeline |
| `Vega_et-al.pdf` | Pending pipeline |
| `Velez.pdf` | Pending pipeline |
| `V.-J.-Ramos-(2024a).pdf` | Pending pipeline |
| `V.-J.-Ramos-(2024b).pdf` | Pending pipeline |
| `Zambrano_et-al.pdf` | Pending pipeline |

To process any of these: run `converter.md` skill on the PDF, then `summarizer.md` on the output, then add a row to `registry.md`. See `RRL/README.md` Section 5 for the full pipeline.

### RRL/01_Reviews/

AI-generated structured summaries for processed papers. Each file is the output of the `summarizer.md` skill. These are the files the team actually reads — they contain the TL;DR, findings, and critically, the **Relevance to Odin** section.

| File | Paper |
| :--- | :--- |
| `Albert_et-al_summarized.md` | Albert et al. — Wealth Creation for Expanding the Middle Class in the Philippines |
| `Amado_summarized.md` | Amado — The plight of teachers on the twice-a-month salary release: Financial literacy and survival |
| `Ama_summarized.md` | Ama — Analysis of the Food and Income Expenditure Survey 2023 Among Filipino Households |
| `Am-Una_summarized.md` | Am-Una — Beyond Awareness: Examining Financial Behaviors Among Public School Teachers in the Philippines |
| `Apao_et-al_summarized.md` | Apao et al. — Maritime Students' Financial Knowledge, Attitude, and Behavior |
| `Asi_et-al_summarized.md` | Asi et al. — Peer Influence and Adolescent Spending: Insights into High School Students' Buying Behavior |
| `Bai_summarized.md` | Bai — Impact of Financial Literacy, Mental Budgeting, and Self-Control on Financial Well-Being |
| `Bangko-Sentral-ng-Pilipinas-(2021)_summarized.md` | BSP — 2021 Consumer Finance Survey (CFS) |
| `Cabiles_summarized.md` | Cabiles — Financial Management Practices of Employees at Bureau of Internal Revenue |
| `Cacnio_Romarate_summarized.md` | Cacnio & Romarate — How does financial literacy affect financial behavior over the life cycle? Evidence from Filipino households |
| `Casilan_Baclagan_summarized.md` | Casilan & Baclagan — Exploring Parental Expectations on Children Helping Parents out in Lower Middle-Income Families |
| `Casiño_et-al_summarized.md` | Casiño et al. — Revisiting the Filipino Value Utang na Loob: Contextual Perceptions, Implications and Inputs to Sustaining the Filipino Psychology Discussions |
| `Cervantes_et-al_summarized.md` | Cervantes et al. — The Effect of Online Buying Decision on Personal Budget of Business Administration Students |
| `Cho_summarized.md` | Cho — A qualitative investigation of financial decisionmaking and enabling factors among ethnic minority young adults in Hong Kong |
| `Dimaunahan_et-al_summarized.md` | Dimaunahan et al. — Financial literacy and sustainable planning assessment among Filipino millennials |

### RRL/02_Related Literature/

Paired PDF + converted Markdown files for each processed paper. The `.md` file is the converter output (structured Markdown with YAML metadata, optimized for AI reading). The companion `_summarized.md` for each paper lives in `01_Reviews/`. Note: `Asi_et-al.md` has no paired PDF in this directory — its source PDF is in `00_Bucket/`.

| Files | Paper |
| :--- | :--- |
| `Albert_et-al.pdf` + `Albert_et-al.md` | Albert et al. — Wealth Creation for Expanding the Middle Class in the Philippines |
| `Amado.pdf` + `Amado.md` | Amado — The plight of teachers on the twice-a-month salary release: Financial literacy and survival |
| `Ama.pdf` + `Ama.md` | Ama — Analysis of the Food and Income Expenditure Survey 2023 Among Filipino Households |
| `Am-Una.pdf` + `Am-Una.md` | Am-Una — Beyond Awareness: Examining Financial Behaviors Among Public School Teachers in the Philippines |
| `Apao_et-al.pdf` + `Apao_et-al.md` | Apao et al. — Maritime Students' Financial Knowledge, Attitude, and Behavior |
| `Asi_et-al.md` *(no paired PDF here)* | Asi et al. — Peer Influence and Adolescent Spending: Insights into High School Students' Buying Behavior |
| `Bai.pdf` + `Bai.md` | Bai — Impact of Financial Literacy, Mental Budgeting, and Self-Control on Financial Well-Being |
| `Bangko-Sentral-ng-Pilipinas-(2021).pdf` + `Bangko-Sentral-ng-Pilipinas-(2021).md` | BSP — 2021 Consumer Finance Survey (CFS) |
| `Cabiles.pdf` + `Cabiles.md` | Cabiles — Financial Management Practices of Employees at Bureau of Internal Revenue |
| `Cacnio_Romarate.pdf` + `Cacnio_Romarate.md` | Cacnio & Romarate — How does financial literacy affect financial behavior over the life cycle? |
| `Casilan_Baclagan.pdf` + `Casilan_Baclagan.md` | Casilan & Baclagan — Exploring Parental Expectations on Children Helping Parents out in Lower Middle-Income Families |
| `Casiño_et-al.pdf` + `Casiño_et-al.md` | Casiño et al. — Revisiting the Filipino Value Utang na Loob |
| `Cervantes_et-al.pdf` + `Cervantes_et-al.md` | Cervantes et al. — The Effect of Online Buying Decision on Personal Budget of Business Administration Students |
| `Cho.pdf` + `Cho.md` | Cho — A qualitative investigation of financial decisionmaking and enabling factors among ethnic minority young adults in Hong Kong |
| `Dimaunahan_et-al.pdf` + `Dimaunahan_et-al.md` | Dimaunahan et al. — Financial literacy and sustainable planning assessment among Filipino millennials |

### RRL/03_Skills/

Prompt files (skills) used to process papers through the pipeline. These are given to a language model as instructions — they are not run automatically.

| File | Purpose |
| :--- | :--- |
| `converter.md` | Skill prompt for converting a PDF research paper into structured Markdown with YAML metadata. Input: PDF. Output: `<paper_id>.md`. Always run this first, before the summarizer. |
| `summarizer.md` | Skill prompt for generating a human-optimized structured summary from a converted Markdown file. Input: `<paper_id>.md`. Output: `<paper_id>_summarized.md`. Produces TL;DR, findings, definitions, and the Relevance to Odin section. Run after the converter. |

### RRL/04_Definition of Terms/

PDFs collected specifically as citation sources for the Definition of Terms section in Chapter 1. File naming convention: `I--` prefix = international source, `L--` prefix = local (Philippine) source. Papers marked `(NOT USED)` in the filename were considered but rejected.

| File | Notes |
| :--- | :--- |
| `Guide.txt` | Empty placeholder. No content. |
| `I--Dlamini.pdf` | International source — pending use in Definition of Terms |
| `I--Morris_et-al.pdf` | International source — pending use in Definition of Terms |
| `I--YOGANANDHAM.pdf` | International source — pending use in Definition of Terms |
| `L--Bongalonta_et -al.pdf` | Local source — pending use in Definition of Terms |
| `L--Desello_and_Agner-(NOT USED).pdf` | Local source — explicitly marked as not used |
| `L--Tambuli_and_Villarba.pdf` | Local source — pending use in Definition of Terms |

---

## RRL Topic Reference

Quick lookup for the 15 RRL topics used in `registry.md` and paper summaries.

| # | Topic Name |
| :---: | :--- |
| 1 | Spending and Budgeting Behavior of Filipino Young Professionals |
| 2 | Existing Personal Finance and Budget Management Systems |
| 3 | Mobile-First Design in Personal Finance Systems |
| 4 | Budgeting Strategies and Budget Recommendation |
| 5 | Budget Recommendation Algorithm |
| 6 | Predictive Modeling in Personal Finance Systems |
| 7 | LSTM as the Spending Forecasting Algorithm |
| 8 | Anomaly Detection in Personal Finance Systems |
| 9 | Anomaly Detection Algorithm |
| 10 | User Behavioral Profiling in Filipino Personal Finance Contexts |
| 11 | Profile Classification Algorithm |
| 12 | Expense Categorization in Filipino Personal Finance Contexts |
| 13 | Data Privacy, Security, and User Trust in Personal Finance Systems |
| 14 | User Retention and Engagement in Personal Finance Systems |
| 15 | System Evaluation |

---

## Key Cross-References

| Task | Where to Go |
| :--- | :--- |
| Understand the full system architecture | `Data/data-synthesis-handoff.md` |
| Justify LSTM as the only ML model | `algorithm-approach-comparison.md` |
| Find mu values for synthetic data | `Data/BSP-Data-on-Filipinos-in-Metro-Manila.xlsx` (Tables 2 and 7) |
| Understand sigma/CV methodology | `Data/synthetic-data-parameters-handoff.md` Section 4 |
| Write or review a Definition of Terms entry | `CHAPTER-1/definition-of-terms-guide.md` + `CHAPTER-1/Scratch/scratch.md` |
| Check what terms still need definitions | `CHAPTER-1/definition-of-terms-list.md` |
| Find citation sources for Definition of Terms | `RRL/04_Definition of Terms/` |
| Get a fast summary of what Odin is and does | `RRL/odin-app-report.md` |
| Address a panel revision | `Documents/Panel-Comments-and-Suggestions.md` |
| Find papers on a specific RRL topic | Search `RRL/registry.md` by topic number or shorthand tag |
| Add a new paper to the RRL | Follow `RRL/README.md` Section 5 pipeline; use skills in `RRL/03_Skills/` |
| Process a paper in 00_Bucket | Run `converter.md` then `summarizer.md` then add row to `registry.md` |
| Check quota status (local/international counts) | Bottom tally row of `RRL/registry.md` |
