# Chapter 1 – Evidence Map (Claim → Citation → Finding)

Audit companion to `chapter-1.md` (Draft V4). Purpose: let the adviser and the team verify that **every citation placed in Chapter 1 is aligned with the new scope and is genuinely supported by the cited source**, and to track which claims still need `VERIFY` work.

## Policy

- Citation pool is **only** the curated intake in `Odin-Literature/literature/papers/` (17 PDFs) plus the study's own PUEPS instrument.
- APA 7th edition.
- **No-stretch rule:** a claim is cited only if the source directly supports it. Claims without direct support remain uncited and are flagged with `<!-- VERIFY: ... -->`.
- V4 reacts to the V3 reviewer comments from Era Marie Gannaban (2026-09-02); each response is marked `►RESPONSE (reviewer #N)` in the draft.

## Source key (curated intake)

| Key (as cited) | PDF | Venue / Year |
|---|---|---|
| Abdullahi et al., 2025 | `Abdullahi et al., 2025.pdf` | IEEE Access, 2025 |
| Abila & Ulibas, 2026 | `Abila & Ulibas, 2026.pdf` | IJMERI, 2026 |
| A. Huang et al., 2025 | `A. Huang et al., 2025.pdf` | Journal of Global Information Management, 2025 |
| Bangko Sentral ng Pilipinas, 2026 | `Bangko Sentral ng Pilipinas, 2026.pdf` | BSP CES, 2Q 2026 |
| Chen & Tan, 2025 | `S. Chen & Tan, 2025.pdf` | DECS, 2025 |
| Chen et al., 2024 | `J. Chen et al., 2024.pdf` | Journal of Basic and Applied Research International, 2024 |
| Danahy et al., 2024 | `Danahy et al., 2024.pdf` | Journal of Consumer Affairs, 2024 |
| El Hajj & Hammoud, 2023 | `Hajj & Hammoud, 2023.pdf` | Journal of Risk and Financial Management, 2023 |
| Ganong et al., 2025 | `Ganong et al., 2025.pdf` | NBER WP 34227, 2025 |
| Hu et al., 2023 | `Hu et al., 2023.pdf` | NeurIPS 2023 |
| R. Huang et al., 2025 | `R. Huang et al., 2025.pdf` | GAIB, 2025 |
| Wang-Ly & Newell, 2023 | `Wang-Ly & Newell, 2023.pdf` | SSRN 4509925, 2023 |
| Yadav et al., 2026 | `Yadav et al, 2026.pdf` | ISJEM 5(4), 2026 |
| Yeo et al., 2023 | `Yeo et al., 2023.pdf` | Journal of Financial Services Marketing, 2023 (print 2024) |
| Yoganandham, 2025 | `Yoganandham, 2025.pdf` | Degres Journal, 2025 |
| PUEPS, 2026 | (own instrument) `Odin-Paper/docs/assessment-evaluation/survey/PUEPS-findings.md` + `PUEPS-responses.csv` | 2026 |

Not cited from the intake (kept out per the no-stretch rule): `Andresen et al., 2025.pdf` (household pooling), `Rane et al., 2024.pdf` (AI acceptance). Neither has a claim in the current draft that they directly support; re-evaluate later if a fitting claim emerges.

## Claim-by-claim mapping

### I. Introduction

| # | Location | Claim (abridged) | In-text citation | What the source supports | Residual verify |
|---|---|---|---|---|---|
| 1 | I-P1 | PFM evolved from manual methods to a digital discipline of budgeting apps and finance software | (El Hajj & Hammoud, 2023; Yadav et al., 2026) | El Hajj & Hammoud: AI/ML transforming financial operations; Yadav et al.: fintech/AI paradigm change in personal finance management | None |
| 2 | I-P2 | Many individuals find financial management difficult | (Ganong et al., 2025) | Ganong: earnings instability → financial fragility among working individuals | None (kept from V3; note it is earnings-instability evidence used as qualitative support) |
| 3 | I-P2 | Unmaintained budgets → struggle to save, reliance on debt, financial vulnerability and stress | (Danahy et al., 2024; Ganong et al., 2025; Wang-Ly & Newell, 2023) | Danahy: debt + lack of emergency savings → financial stress; Ganong: earnings instability → financial fragility; Wang-Ly & Newell: income volatility affects saving decisions | None |
| 4 | I-P3 | Mobile apps consolidate financial info, automate tracking, present summaries | (Yadav et al., 2026) | Yadav et al.: IPFMS aggregates transactions, real-time snapshot, predictive budgeting recommendations | None |
| 5 | I-P3 | ML estimates future expenses / flags unusual transactions | (Chen et al., 2024; Chen & Tan, 2025; A. Huang et al., 2025) | Chen et al.: deep-learning time-series forecasting survey; Chen & Tan: behavior prediction from historical behavior; A. Huang: threshold calibration for financial anomaly detection | None |
| 6 | I-P4 | Savings as buffer; poorly managed debt → income loss, stress, fewer opportunities | (Danahy et al., 2024; Yeo et al., 2023; Yoganandham, 2025) | Danahy: emergency savings buffer; Yeo: planning behaviour → resilience; Yoganandham: budgeting/savings/debt → long-term stability | None |
| 7 | I-P4 | Many Filipino workers struggle to save while servicing obligations | (Abila & Ulibas, 2026) + `<!-- VERIFY -->` | Abila & Ulibas: Filipino freelancers' savings/resilience amid obligations and income volatility | **Citation covers online freelancers in Laguna only** — V4 now cross-supports incidence with PUEPS findings in Section II |
| 8 | I-P5 | Need for personalized intelligent PFM for Filipinos | (R. Huang et al., 2025; Yadav et al., 2026) | R. Huang: personalized intelligent wealth management; Yadav: intelligent PFM tailored to behavior and goals | None |

### II. Project Context

| # | Location | Claim (abridged) | In-text citation | What the source supports | Residual verify |
|---|---|---|---|---|---|
| 9 | II-P1 | NCR young adults manage finances manually (notebooks, sheets, mental tracking); 19% don't track at all | (PUEPS, 2026) | Own instrument: 38% mental, 28% spreadsheet, 28% notebook, 19% no tracking | Verify figure transcription against `PUEPS-responses.csv` |
| 10 | II-P1 | Informal practices (paluwaluugan, ambag, family support, gov contributions) | `<!-- VERIFY -->` (no citation) | — | Confirm incidence against BSP CES 2026 or PUEPS supplementary items |
| 11 | II-P1 | Generic apps (Western-style, single-account) don't fit local income/expense patterns; 40% use mobile budgeting app such as GCash/Lista | (Abila & Ulibas, 2026; Bangko Sentral ng Pilipinas, 2026; PUEPS, 2026) | Abila & Ulibas: local practices/pressures; BSP: NCR consumer expectations/conditions; PUEPS: 40% mobile budgeting app use | Generalization beyond cited samples — see I-P4 residual |
| 12 | II-P2 | PUEPS as preliminary investigation; **survey results quoted** (96% find financial mgmt challenging, 85% difficulty monitoring, 66% difficulty identifying where money goes, 72% unexpected expenses, 68% apps too complex, 89% not Filipino-context, 89% limited insights, 83% privacy, 53% track regularly, 26% save regularly) | (PUEPS, 2026) | Findings file located: `PUEPS-responses.csv` (2026-09-07 export) → `PUEPS-findings.md` | Verify all percentages against the raw CSV; sample is N=47 |
| 13 | II-P3 | Tension between debt repayment and savings → deferred savings / debt accumulation | (Danahy et al., 2024) + `<!-- VERIFY -->` | Danahy: debt vs emergency savings tension and stress | Generalization beyond college-debt findings |
| 14 | II-P3 | Accumulated conditions reduce financial resilience and goal pursuit | (Ganong et al., 2025; Wang-Ly & Newell, 2023; Yeo et al., 2023) | Volatility/instability → fragility and impaired saving; planning behaviour → resilience | None |
| 15 | II-P4 | BUDI resolves each identified problem (reviewer #4): tracking→monitoring, summaries→where money goes, forecasts→97%/94% preference, budget/savings/debt→obligation tension, alerts→98% welcome | (R. Huang et al., 2025; Yadav et al., 2026; PUEPS, 2026) | Intelligent PFM feature precedents; PUEPS feature-preference figures (94% forecasts, 98% alerts, 100% Filipino categories, 100% personalized suggestions with explanations) | None |
| 16 | II-P5 | Four model families with explicit I/O (reviewer #1): classify financial state, forecast next-period spend, optimize fund allocation, detect unusual spending | (Chen et al., 2024; Hu et al., 2023; A. Huang et al., 2025) | Chen et al.: forecasting; Hu et al.: predict+optimize with constraints; A. Huang: anomaly detection thresholds | None |
| 17 | II-P5 | Models must stay reliable as user behavior evolves | (Abdullahi et al., 2025) + `<!-- VERIFY -->` | Abdullahi: concept drift degrades time-series/classification model performance | Applicability of concept-drift findings to personal-finance profile classification — verify |

### III. Purpose and Description of the Study

| # | Location | Claim (abridged) | In-text citation | What the source supports | Residual verify |
|---|---|---|---|---|---|
| 18 | III-P2 | BUDI described (Android + React for Web, offline-first, Filipino-context categories, privacy) | Self-authored description | — | None |
| 19 | III-P3 | Model inputs→outputs (classified/forecast/optimized/flagged explicitly) | (Chen et al., 2024; Chen & Tan, 2025; Hu et al., 2023; A. Huang et al., 2025) | Same method-family support as #16 | None |
| 20 | III-P4 | Savings/debt improvement measurement (reviewer #2): savings rate, savings goal growth, reduction in unusual-spending alerts, debt repayment progress | Self-authored measurement framework (PUEPS 94% forecasts helpful; 100% personalized suggestions) | Anchored to in-app observable indicators | None |
| 21 | III-P5 | Alignment with UN SDG 1 & 8 | (no citation) + `<!-- VERIFY -->` | — | Confirm claim alignment against the UN SDG framework wording |

### IV. Scope and Limitations

| # | Location | Claim (abridged) | In-text citation | What the source supports | Residual verify |
|---|---|---|---|---|---|
| 22 | IV-P1 | NCR young adults face obligations, savings, debt concerns | (Bangko Sentral ng Pilipinas, 2026; PUEPS, 2026) + `<!-- VERIFY -->` | BSP CES 2Q 2026: NCR + national consumer expectations; PUEPS: NCR-only sample | Specific NCR figures — cite exact DI/percentage when using a number |
| 23 | IV-P3 | Final model selection by evaluation metrics etc. | Self-authored methodology | — | None |
| 24 | IV-P4 | Public PH datasets are household-level/aggregate | (Bangko Sentral ng Pilipinas, 2026) + PSA `<!-- VERIFY -->` | BSP CES as an aggregate household survey example | PSA FIES: confirm exact dataset years and access date (source not in curated intake) |
| 25 | IV-P4 | Savings/debt features subject to PUEPS validation | (PUEPS, 2026) | Own instrument (findings now located) | Field-validation pending |

### V. Operational Definition of Terms

No citations required (terms defined operationally for this study). V4 adds the standard preamble sentence present in the V3 docx.

## Reviewer response log (V3 comments → V4 action)

| # | Reviewer comment (Gannaban, 2026-09-02) | V4 action |
|---|---|---|
| 1 | "what do you plan to classify? forecast? optimize? and identify anomalies?" | Section II-P5 and III-P3 now state the input and output of each of the four model families explicitly. |
| 2 | "how do you plan to measure users improvement in savings and debt?" | New Section III-P4 defines observable in-app indicators: savings rate, savings-goal growth, anomaly-alert reduction, debt repayment progress. |
| 3 | "include discussions on the result of the survey ex: based on the survey savers do this which leads to…" | PUEPS responses located and analyzed (`PUEPS-findings.md`); Section II-P2 now quotes 10 response figures and connects behavior to consequences. |
| 4 | "how do you plan to resolve this" | Section II-P4 adds an explicit problem→feature→response mapping; every identified difficulty is tied to a BUDI function. |

## Open items for the team

1. **PUEPS figure transcription check** — the percentages in §II-P2/P1 were transcribed from `PUEPS-responses.csv`; re-run the analysis script against the raw export before final submission to confirm each percentage.
2. **PSA FIES** — add a verified reference (official report) and exact years, or keep it a named data source only.
3. **BSP CES 2Q 2026** — pull the specific diffusion-index figures (NCR vs national) to underpin any numeric claim.
4. **Generalization flags** (#7, #13, #17) — decide whether the citation stands as qualitative support with a qualifying clause, or whether a stronger source is needed.
5. **Andresen et al. (2025)** and **Rane et al. (2024)** are in the intake but uncited; confirm whether they are reserved for Chapters 2–3.
6. **Scope reconciliation** — V4 keeps System Admin Module (Web) per the V3 reviewer-facing doc and removes the standalone Admin Module; confirm this matches the team's intended scope in the Drive requirements-engineering doc.