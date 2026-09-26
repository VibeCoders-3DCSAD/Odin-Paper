# Chapter 1 – Evidence Map (Claim → Citation → Finding)

Audit companion to `chapter-1.md` (**Finalized V5**). Purpose: let the adviser and the team verify that **every citation placed in Chapter 1 is aligned with the scope and genuinely supported by the cited source**, and to track which claims still need `VERIFY` work.

## Policy

- Citation pool is **only** the curated intake in `BUDI-Literature/literature/papers/` (PDFs) plus the study's own PUEPS instrument.
- APA 7th edition.
- **No-stretch rule:** a claim is cited only if the source directly supports it. Claims without direct support remain uncited and are flagged with `<!-- VERIFY: ... -->`.
- **Versioning (team decision):** repo drafts that follow the Drive V5 file are numbered **5.x** (this is 5.0, the finalized revision); Drafts 4.1–4.3 were the candidate-open rewrites of the Drive V4 file. Draft 4.1 was the former V5 (committed `a179f9a`); Draft 4.2 was the former V6; Draft 4.3 (reconciled against the refreshed V4 docx, 2026-09-14) was the last revision that listed candidate algorithms with final selection deferred to Specific Objective 4. This audit covers Finalized V5.
- **V5 (final, 2026-09-21) is reconciled against two documents re-fetched from Drive the same day:** `GROUP4 - CHAPTER 1 - V5 - 09.19.26.docx` (Drives's V5, whose inline comments this draft resolves) and `GROUP4 - TECHNICAL SPECIFICATION - V1 - 09.20.2026.docx` (the authoritative scope snapshot: users **18–59 in the NCR**, single-user Android app, offline-first core + server-side intelligent modules, one selected algorithm per module).
- **⚠️ 2026-09-24 supersession:** the Drive *Technical Specification V1 (09.24.2026)* replaces the 09.20 scope this V5 was reconciled against — project renamed **TAYA**, profile classification is **rule-based** (SVM/PFP no longer the named model), and forecasting is SARIMA with FIES 2023 + HFCE 2022 Q1–2026 Q2 temporal disaggregation. Every claim pinned to the 09.20 spec (SVM, budget-optimizer naming, data sources) must be re-verified against 09.24 before this map is used as the current audit.
- **Team decisions (2026-09-21) reflected in this draft:** (1) the paper **names the selected models** — SVM profile classification, SARIMA forecasting, LP-based budgeting, IQR anomaly detection — and no longer presents candidate-algorithm comparisons or any "best performing" framing (resolves the V5 inline comments on the algorithm paragraph, SO2, and the technical scope); (2) the V5 cover title's "Rule-Based Classification" is treated as a stale leftover — SVM is restored per V5 SO4, the tech-spec models table, and the trained `tier3_svm.joblib` artifact; (3) **single-user mobile application** — no admin, system-admin, or web-management roles (carried from Drafts 4.x); (4) target band is **18–59 living or working in the NCR** (revised from 20–40, resolving the V5 "(check if the report is still applicable for individuals aged 18-59)" comment); (5) the savings-and-obligations sentence in II-P3 no longer relies on third parties to justify the outcome link ("(how exactly?)" resolved by anchoring to the PUEPS savings-allocation findings).
- **New citations** (classification → optimization → anomaly) come from the BUDI-Literature batch-7 intake (2026-09-07); those sources are mid-migration and exist only as `_marked.md` conversions for now (see source key notes).
- **Structure benchmark:** section order, heading navigation, and prose discipline follow the reference thesis `formats-templates/chapter-1/Reference Thesis (Group 10).docx` (Ch. I: Introduction → Project Context → Purpose and Description → General Objectives → Specific Objectives → Scope and Limitations → Definition of Terms).

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
| D'Souza et al., 2026 | `A--DSouza-2026_marked.md` † | P.E.S. Modern College of Engineering manuscript, 2026 |
| Laspiñas & Murcia, 2024 | `L--LaspinasMurcia-2024_marked.md` † | TWIST 19(2), 2024 |
| Lu et al., 2025 | `A--Lu-2025_marked.md` † | JTIE 4(3), 2025 |
| Pratama & Putri, 2024 | `A--Pratama-2024_marked.md` † | IJAIM 4(4), 2024 |
| Reyes et al., 2024 | `L--Reyes-2024_marked.md` † | IJAMC 1(1), 2024 |
| Salvador, 2024 | `L--Salvador-2024_marked.md` † | Research manuscript (PH wealth quintiles), 2024 |
| Sonkavde et al., 2023 | `A--Sonkavde-2023_marked.md` † | Int. J. Financial Studies 11(3), 2023 |
| Zhang et al., 2023 | `A--ZhangEtAl-2023_marked.md` † | PVLDB 16(11), 2023 |
| Zhong, 2025 | `A--Zhong-2025_marked.md` † | University of Chicago MS thesis, 2025 |
| PUEPS, 2026 | (own instrument) `docs/assessment-evaluation/survey/PUEPS-findings.md` + `PUEPS-responses.csv` | 2026 |

> † **Batch-7 intake (2026-09-07).** Mid-migration: only the `BUDI-Literature/literature/conversions/*_marked.md` conversions exist yet; each PDF lands in `BUDI-Literature/literature/papers/` when the scoring-migration finishes.

Not cited from the intake (kept out per the no-stretch rule): `Andresen et al., 2025.pdf` (household pooling), `Rane et al., 2024.pdf` (AI acceptance), and batch-7 `A--Sappa-2024`, `A--ZhangHou-2026`, `I--Awaluddin-2023` (portfolio optimization, financial-agent studies, cost-of-living analysis). None has a claim in the current draft that it directly supports; re-evaluate later if a fitting claim emerges.

## Claim-by-claim mapping

### I. Introduction

| # | Location | Claim (abridged) | In-text citation | What the source supports | Residual verify |
|---|---|---|---|---|---|
| 1 | I-P1 | PFM evolved from manual methods to a digital discipline of budgeting apps and finance software | (El Hajj & Hammoud, 2023; Yadav et al., 2026) | El Hajj & Hammoud: AI/ML transforming financial operations; Yadav et al.: fintech/AI paradigm change in personal finance management | **Citation-support stretch:** neither source addresses the historical manual-methods claim ("mental accounting") — see Open Item #13 |
| 2 | I-P2 | Many individuals find financial management difficult; unmaintained budgets → struggle to save, reliance on debt, vulnerability and stress | (Ganong et al., 2025; Danahy et al., 2024; Wang-Ly & Newell, 2023) | Ganong: earnings instability → financial fragility; Danahy: debt + no emergency savings → stress; Wang-Ly & Newell: income volatility affects saving decisions | None |
| 3 | I-P3 | Mobile apps consolidate financial info, automate tracking, present summaries; ML estimates future expenses, flags unusual transactions, proposes allocations; reviews organize these techniques for intelligent PFM systems | (Yadav et al., 2026; Chen et al., 2024; Chen & Tan, 2025; A. Huang et al., 2025; D'Souza et al., 2026) | Yadav: IPFMS aggregates transactions and gives predictive budgeting; Chen et al.: deep-learning time-series forecasting; Chen & Tan: behavior prediction; A. Huang: threshold calibration for anomaly detection; D'Souza et al.: review of ML techniques for intelligent PFM systems | None |
| 4 | I-P4 | Savings as buffer; poorly managed debt → income loss, stress, fewer opportunities; Filipino workers struggle to save while servicing obligations | (Danahy et al., 2024; Yeo et al., 2023; Yoganandham, 2025; Abila & Ulibas, 2026) | Danahy/Yeo/Yoganandham: savings buffer, planning resilience, budget/debt → stability; Abila & Ulibas: Filipino freelancers' savings/resilience amid obligations | **Citation covers online freelancers in Laguna only** — cross-supported by PUEPS figures in Project Context |
| 5 | I-P5 | Need for personalized intelligent PFM for Filipinos | No citation (self-authored synthesis of previous paragraphs) | — | None |

### II. Project Context

| # | Location | Claim (abridged) | In-text citation | What the source supports | Residual verify |
|---|---|---|---|---|---|
| 6 | II-P1 | NCR young adults manage finances manually (38% mental, 28% spreadsheet, 28% notebook, 19% no tracking); 40% use a mobile budgeting app | (PUEPS, 2026) | Own instrument; figures re-transcribed and confirmed 2026-09-13 against `PUEPS-responses.csv` | None |
| 7 | II-P1 | Informal practices (paluwagan, ambag, family support, gov contributions) not captured by commercial apps | No citation (study context) | — | Could be anchored to PUEPS open-ended items or a BSP CES figure if needed |
| 8 | II-P1 | Age band **18–59** (NCR) adopted because BSP data show digitally connected Filipino workers among the most active mobile/digital finance users | (Bangko Sentral ng Pilipinas, 2026) | BSP CES 2Q 2026 as the recommended consumer/primer source | **Confirm the specific digital-finance uptake figure from the cited BSP report** — applicable to 18–59 as a working band (V5 revised the band from 20–40 to match the technical spec scope). |
| 9 | II-P1 | PUEPS used purposive sampling among working young adults in NCR; respondents drawn primarily from Taguig, Pasay, Manila, and Makati | (PUEPS, 2026) | Findings file Study Design: Taguig 30%, Pasay 17%, Manila 13%, Makati 11%, QC 9% | None (note the four cities are "primarily" — Honest description) |
| 10 | II-P2 | Survey confirmations: 95.7% (45/47) finances challenging; 85.1% (40/47) monitor spending difficulty; 66.0% (31/47) / 80.9% (38/47) where money goes; 72.3% (34/47) / 97.9% (46/47) unexpected obligations; 68.1% (32/47) tools too complex; 89.4% (42/47) not Filipino-context; 89.4% (42/47) limited insights; 83.0% (39/47) privacy | (PUEPS, 2026) | Re-transcribed and confirmed 2026-09-13 against `PUEPS-responses.csv` (see Appendix note below) | None (figures recomputed from raw CSV) |
| 11 | II-P3 | Unmonitored unusual spending strains budgets; debt vs savings tension → defer savings / higher-cost debt; reduces financial resilience | (PUEPS, 2026; Danahy et al., 2024; Ganong et al., 2025; Wang-Ly & Newell, 2023; Yeo et al., 2023) | Savings-allocation pattern from PUEPS (68.1% every-salary/or often; ~1/3 sometimes/rarely/never); Danahy: debt-stress; Ganong/Wang-Ly/Yeo: volatility and planning → resilience | Generalization from college-debt findings (#11 stress mechanism) |
| 12 | II-P4 | BUDI problem→feature mapping; every major function tied to an identified problem | (PUEPS, 2026) (feature-preference figures P5) | PUEPS feature expectations: forecasts helpful 94%, alerts 98%, personalized suggestions 100% | None |
| 13 | II-P5 | Four model families with explicit input/output; models must stay reliable as behavior evolves | (Abdullahi et al., 2025) | Abdullahi: concept drift degrades time-series/classification performance | Applicability of concept-drift findings to personal-finance profile classification |

### III. Purpose and Description of the Study

| # | Location | Claim (abridged) | In-text citation | What the source supports | Residual verify |
|---|---|---|---|---|---|
| 14 | III-P1 | Purpose, intended users, and the three concerns the study addresses | Self-authored description | — | None |
| 15 | III-P2 | BUDI described (Android + Expo/React Native, offline-first, single-user — no admin/system-admin/web roles, Filipino-context categories, privacy, DPA 2012) | Self-authored description (DPA reference is legal naming, not a research claim) | — | None |
| 16 | III-P3 | Selected algorithms (one per module) and how each functions on its key feature (SVM classification, SARIMA forecasting, LP optimization, IQR anomaly); outputs are decision-support subject to user approval | (Laspiñas & Murcia, 2024; Reyes et al., 2024; Pratama & Putri, 2024; Salvador, 2024; Sonkavde et al., 2023; Hu et al., 2023; Lu et al., 2025; Zhang et al., 2023; Zhong, 2025) | Classification: PH income-level/wealth classification (Laspiñas & Murcia; Salvador), finance ML model comparison (Reyes et al.), plus clustering-based transaction-pattern user segmentation as the profiling feature basis (Pratama & Putri); Forecasting: statistical + ML/DL survey for financial forecasting (Sonkavde et al.); Optimization: predict-then-optimize MILP (Hu et al.) and constrained data-driven budgeting (Lu et al.); Anomaly: time-series anomaly-detection benchmark (Zhang et al.) and adaptive-threshold calibration (Zhong) | **Salvador (2024) is a research manuscript — confirm venue before final submission**. No candidate-comparison framing anywhere (V5 team decision). |
| 17 | III-P4 | Savings/debt improvement measured via in-app indicators (savings rate, goal growth, alert reduction, repayment progress); respondent preference figures; savings rate treats debt principal and own-account transfers as allocations, not expenses | (PUEPS, 2026) | PUEPS feature expectations 94%/98%/100% | None |
| 18 | III-P5 | Expected contribution; SDG 1 & 8 alignment | No citation + `<!-- VERIFY -->` on SDG wording | — | **Confirm claim alignment against the UN SDG framework wording** |
| 19 | GO | General objective mirrors the title, naming the models the study uses (SVM profile classification, SARIMA forecasting, LP-based budgeting, IQR anomaly detection) — no candidate framing | Self-authored | — | None |
| 20 | SO3 | Data from BSP CFS, PSA FIES, synthetic personas; public microdata via PSADA; consent for direct survey | Self-authored methodology | — | PSADA access specifics to confirm (see Scope #22) |

### IV. Scope and Limitations

| # | Location | Claim (abridged) | In-text citation | What the source supports | Residual verify |
|---|---|---|---|---|---|
| 21 | Scope-Locale | NCR locale; users **18–59**; purposive sampling; respondent cities | (Bangko Sentral ng Pilipinas, 2026; PUEPS, 2026) | BSP CES context; PUEPS sample design | None (V5 revised 20–40 to 18–59). |
| 22 | Scope-Tech | Public PH datasets (BSP, PSA/PSADA) are household-level/aggregate → synthetic data for training | (Bangko Sentral ng Pilipinas, 2026) + PSA `<!-- VERIFY -->` | BSP CES as an aggregate household survey example | **Confirm exact FIES/PSADA dataset years and access date** |
| 23 | Scope-Tech | Forecasting limited to periods/categories with sufficient history; alerts from recorded baseline; outputs subject to user approval | Self-authored | — | None |
| 24 | Limitations | Each limitation mapped to an objective/feature (sampling→SO1, data→SO3, manual entry→SO5, model limits→SO4, Android-only→SO8, concept drift→II-P5, cold-start→SO5.14/15, non-advice→III) | (Abdullahi et al., 2025) | Drift evidence only | None |

### V. Operational Definition of Terms

No citations required (terms defined operationally for this study). Per adviser annotations, `Time-Series Data` (flagged "not part") and `Transaction Data` (flagged "general") were removed; `Category-Level Spending Forecast` and `Purposive Sampling` added; `Recurring Transaction` retained with its V4 scope.

## Adviser feedback log (Drive V4 → Draft 4.3 action)

### Comments (comments.xml)

| # | Source / date | Comment | 4.3 action |
|---|---|---|---|
| c0 | Gannaban 09-02 | "how do you plan to measure users improvement in savings and debt?" | III-P4 defines measurable indicators (savings rate, goal growth, alert reduction, repayment progress). |
| c1 | Gannaban 09-04 | "why specifically for young adults? can we say individuals who wants to learn financial freedom?" | II-P1 adds the BSP-based rationale for the 20–40 band (`VERIFY` flagged); locale justification from the group's topic defense retained. |
| c2 | Guevarra 09-04 | (reply to c1) BSP-derived justification | Incorporated into II-P1. |
| c3 | Gannaban 09-04 | "do you plan to collect information and approval from them?" (BSP/PSA) | SO3 + Scope-Tech state public-reports/microdata approach (PSADA) and informed consent for direct survey data. |
| c4 | Guevarra 09-04 | (reply to c3) public info; PSADA microdata (Jul–Dec) for synthetic seeding | Incorporated into SO3 and Scope-Tech. |
| c5 | Gannaban 09-04 | "what are the category level?" | New term `Category-Level Spending Forecast`; forecasting language (II-P5, III-P3, SO5.15) now defines category-level estimates. |
| c6 | Gannaban 09-04 | "can we limit it to makati only then lets make it purposive sampling because ncr is too big to consider" | **Team decision 09-13:** NCR locale retained (defense-approved; PUEPS sample spans 4+ NCR cities) with purposive sampling made explicit and respondent distribution stated in II-P1 and Scope-Locale. |
| c7 | Gannaban 09-04 | "are these algorithms ? software tools?" | Scope-Tech splits the model/data scope from the software toolchain (React/Expo/Node/Supabase/SQLite). |

### Inline annotations in the Drive Google Doc

| Annotation | 4.3 action |
|---|---|
| (TODO: Verify if all the core features are included here.) | II-P4 feature sentence rewritten and synchronized with SO5. |
| `[[organized]]` "this is a system characteristic" | Replaced with "structured transaction, income, and obligation records." |
| (discuss how models will function on the key features) | III-P3 explains how each candidate algorithm functions on its feature. |
| (Add: The researchers will utilize and discuss how it will function on its key feature) | III-P3 opening sentence added. |
| (what algo/ model do you plan to use) | **4.3:** SO4 listed candidate algorithms per family, winner deferred to SO4 metrics. **V5 (2026-09-21):** superseded — the paper names the selected models (SVM/SARIMA/LP/IQR) and no longer compares candidates. |
| (needs revision, since the new scope will use one model/algorithm per intelligent module) [Drive V5, algorithm paragraph] | **V5:** III-P3 names exactly one selected algorithm per module. |
| (revise or remove since we are shifting away from explicitly stating that we're tackling multiple models/algorithms) [Drive V5, SO2] | **V5:** SO2 reworded to "explore existing systems… to identify gaps", dropping the multi-model lead. |
| (revise since it uses the candidate algos) [Drive V5, technical scope] | **V5:** Scope defines SVM/SARIMA/LP/IQR as the selected models, with no candidate list. |
| (check if the report is still applicable for individuals aged 18-59) [Drive V5, BSP age-band] | **V5:** scope revised to 18–59 NCR; BSP claim re-scoped to "Filipino workers" with `VERIFY` retained. |
| (only include actual operational terms… time-series data, transaction data and recurring transaction here) [Drive V5, definitions intro] | **V5:** Section V keeps only operational terms; `Time-Series Data` and `Transaction Data` excluded. |
| (System Admin Module) | **Team decision 09-14:** removed. SO5 is now a single User Module (Mobile) feature list; functional scope and III-P2 state single-user with no admin/system-admin/web roles. |
| (Add user account management) | New SO5.3 User Account Management; Scope functional list matches. |
| (what are the recurring transactions?) | SO5.6 defines recurring income/expenses/savings/debt; term kept in Section V. |
| (how do you plan to monitor these?) (financial accounts) | SO5.9 states accounts are monitored via recorded transactions and balances, without API integration. |
| (how do you plan to do this / breakthrough feature) (debt repayment strategies) | SO5.12 describes snowball/avalanche comparison with payoff projection. |
| (Add: usability sub-characteristics) | **V5:** SO7 added Usability sub-characteristics. **Finalized V5 (2026-09-21):** superseded — SO7 now follows the Drive `ISO 25010 - V1 - 09.15.2026` questionnaire, which delegates usability to SUS; the ISO list covers Functional Suitability, Performance Efficiency, Reliability, Security, and Maintainability. |
| (Replace "Reliability…" with "usability") | **V5:** SO7 kept both Usability and Reliability. **Finalized V5:** reliability sub-characteristics updated to the Drive ISO instrument's set (faultlessness, availability, fault tolerance, recoverability). |
| (you can check counterpart ng playstore) | SO8 names the Google Play Store as the deployment target. |
| (please match this to your specific objectives) (functional scope) | Scope functional list enumerates exactly the SO5 features. |
| (what is technical scope?) | Scope-Tech now defines technical scope explicitly (Section III `Scope`). |
| (Please review your limitation match it to your objectives, project context and purpose) | Limitations reorganized to map each limitation to its objective/feature. |
| (not part) on Time-Series Data / (general) on Transaction Data | Both terms removed from Section V. |

## Appendix — PUEPS re-transcription (2026-09-13)

Raw `PUEPS-responses.csv` (47 rows) recomputed for every figure quoted in Chapter 1:

- Challenging (agree+strongly agree): 45/47 = 95.7%
- Difficulty monitoring spending (A+SA): 40/47 = 85.1%
- Where the money goes (frequently+very frequently): 31/47 = 66.0%; at least occasionally: 38/47 = 80.9%
- Unexpected obligations affect budgeting (freq+vfreq): 34/47 = 72.3%; at least occasionally: 46/47 = 97.9%
- Tools too complex/time-consuming (A+SA): 32/47 = 68.1%
- Do not reflect Filipino realities (A+SA): 42/47 = 89.4%
- Limited insights (A+SA): 42/47 = 89.4%
- Privacy/security concerns (A+SA): 39/47 = 83.0%
- Saving allocation: every salary period (20/47) + often (12/47) = 32/47 = 68.1%; sometimes/rarely/never = 15/47 = 31.9%
- Tracking methods: mental 38% (18/47), spreadsheet 28% (13/47), notebook 28% (13/47), no tracking 19% (9/47), mobile app 40% (19/47) (multi-select)

> Note: `PUEPS-findings.md` formerly reported "Regularly allocate income to savings … 26%". That row was mislabeled; the same item yields 68.1% on "every salary period + often" (32/47). The findings file has been corrected (2026-09-13). All body figures follow the raw CSV.

## Open items for the team

1. **BSP digital-finance uptake** for the 18–59 justification (II-P1, `#8`) — pull the specific figure from the cited BSP CES/CFS report or soften the claim.
2. **PSA FIES / PSADA & household financial characteristics** — add verified references: **PSA FIES**, **PSA HFCI/HFCE (confirm exact dataset name — Drive and tech spec alternate between "HFCI" and "HFCE" — plus year and version)**, and **BSP CFIS/CFS** are **not yet indexed** in `BUDI-Literature/literature/papers/`; each body claim carries a `<!-- VERIFY -->` marker until the reference lands (`#22`, SO3).
3. **SDG wording** — confirm the SDG 1/8 alignment phrasing against the UN framework (`#18`).
4. **Generalization flag `#11`** — the debt→stress mechanism cites Danahy et al. (college-student context); decide whether a qualifying clause suffices or a stronger source is needed.
5. **Andresen et al. (2025)**, **Rane et al. (2024)**, and batch-7 **Sappa (2024)**, **Zhang & Hou (2026)**, **Awaluddin (2023)** remain in the intake uncited; confirm they are reserved for Chapters 2–3.
6. **Locale framing** — team decision keeps NCR + purposive sampling; keep the Drive doc and this chapter consistent when the adviser re-checks.
7. **Salvador (2024) venue** (`#16`) — cited as a research manuscript; confirm the final venue (or reclassify) before submission.
8. **Drive copy refresh (V5)** — the Drive `V5` docx and the `09.20` tech spec were re-fetched 2026-09-21 to write this draft; the Drive docx should be updated from this finalized draft so the source of truth matches (V5 cover title still says "Rule-Based Classification"; keep SVM as in V5 SO4 / the tech-spec models table).
9. **Batch-7 migration** — the 9 new citations (source key) exist only as `_marked.md` conversions; confirm each PDF lands in `BUDI-Literature/literature/papers/` so the citation pool completes.
10. **Profile label taxonomy & ground truth** (SO4.1) — finalize the profile label set and its supervised ground-truth scheme in the ML modeling phase; the FIES/BSP household-level sources do not provide individual-level profile labels as-is.
11. **Anomaly ground truth** (SO4.4) — define the labeled-anomaly scheme (e.g., synthetic labels or rule-based flags) that backs the precision/recall metrics.
12. **"Sufficient data" threshold** — quantify the minimum transaction history (periods/categories) that activates forecasting and anomaly baselines, resolving the cold-start behavior.
13. **Mental-accounting citation** (I-P1, `#1`) — the historical claim cites El Hajj & Hammoud (AI/ML in markets) and Yadav et al. (IPFMS); neither supports that sentence's manual-methods history — re-cite or trim.
14. **Improvement attribution** (III-P4) — the in-app indicators measure change, not attribution; define the baseline/timeframe (or a limitation) for claiming savings/debt improvement results from using BUDI.
15. **Clean the Drive evaluation instruments (SO6/SO7)** — the Drive `ISO 25010 - V1 - 09.15.2026` doc is a template with residual placeholder content (stray "User Error Protection"/"User Assistance" rows under Performance Efficiency; questions still reference the source project's subject matter) and the Drive `SUS - V1 - 09.15.2026` doc prints a 1–4 scale while the scoring guide uses 5-point arithmetic. Finalize both questionnaires so the instruments match this chapter's SO7 wording before deployment.