# Chapter 1 – Evidence Map (Claim → Citation → Finding)

Audit companion to `chapter-1.md` (Draft V5). Purpose: let the adviser and the team verify that **every citation placed in Chapter 1 is aligned with the scope and genuinely supported by the cited source**, and to track which claims still need `VERIFY` work.

## Policy

- Citation pool is **only** the curated intake in `Odin-Literature/literature/papers/` (PDFs) plus the study's own PUEPS instrument.
- APA 7th edition.
- **No-stretch rule:** a claim is cited only if the source directly supports it. Claims without direct support remain uncited and are flagged with `<!-- VERIFY: ... -->`.
- V5 is reconciled against the Drive `GROUP4 - CHAPTER 1 - V4 - 09.13.26.docx`, which carries the adviser's comments (Era Marie Gannaban, 2026-09-04) and the group's inline annotations.
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
| PUEPS, 2026 | (own instrument) `docs/assessment-evaluation/survey/PUEPS-findings.md` + `PUEPS-responses.csv` | 2026 |

Not cited from the intake (kept out per the no-stretch rule): `Andresen et al., 2025.pdf` (household pooling), `Rane et al., 2024.pdf` (AI acceptance). Neither has a claim in the current draft that they directly support; re-evaluate later if a fitting claim emerges.

## Claim-by-claim mapping

### I. Introduction

| # | Location | Claim (abridged) | In-text citation | What the source supports | Residual verify |
|---|---|---|---|---|---|
| 1 | I-P1 | PFM evolved from manual methods to a digital discipline of budgeting apps and finance software | (El Hajj & Hammoud, 2023; Yadav et al., 2026) | El Hajj & Hammoud: AI/ML transforming financial operations; Yadav et al.: fintech/AI paradigm change in personal finance management | None |
| 2 | I-P2 | Many individuals find financial management difficult; unmaintained budgets → struggle to save, reliance on debt, vulnerability and stress | (Ganong et al., 2025; Danahy et al., 2024; Wang-Ly & Newell, 2023) | Ganong: earnings instability → financial fragility; Danahy: debt + no emergency savings → stress; Wang-Ly & Newell: income volatility affects saving decisions | None |
| 3 | I-P3 | Mobile apps consolidate financial info, automate tracking, present summaries; ML estimates future expenses, flags unusual transactions, proposes allocations | (Yadav et al., 2026; Chen et al., 2024; Chen & Tan, 2025; A. Huang et al., 2025) | Yadav: IPFMS aggregates transactions and gives predictive budgeting; Chen et al.: deep-learning time-series forecasting; Chen & Tan: behavior prediction; A. Huang: threshold calibration for anomaly detection | None |
| 4 | I-P4 | Savings as buffer; poorly managed debt → income loss, stress, fewer opportunities; Filipino workers struggle to save while servicing obligations | (Danahy et al., 2024; Yeo et al., 2023; Yoganandham, 2025; Abila & Ulibas, 2026) | Danahy/Yeo/Yoganandham: savings buffer, planning resilience, budget/debt → stability; Abila & Ulibas: Filipino freelancers' savings/resilience amid obligations | **Citation covers online freelancers in Laguna only** — cross-supported by PUEPS figures in Project Context |
| 5 | I-P5 | Need for personalized intelligent PFM for Filipinos | No citation (self-authored synthesis of previous paragraphs) | — | None |

### II. Project Context

| # | Location | Claim (abridged) | In-text citation | What the source supports | Residual verify |
|---|---|---|---|---|---|
| 6 | II-P1 | NCR young adults manage finances manually (38% mental, 28% spreadsheet, 28% notebook, 19% no tracking); 40% use a mobile budgeting app | (PUEPS, 2026) | Own instrument; figures re-transcribed and confirmed 2026-09-13 against `PUEPS-responses.csv` | None |
| 7 | II-P1 | Informal practices (paluwagan, ambag, family support, gov contributions) not captured by commercial apps | No citation (study context) | — | Could be anchored to PUEPS open-ended items or a BSP CES figure if needed |
| 8 | II-P1 | Age band 20–40 adopted because BSP data show younger digitally connected Filipino workers are among the most active users of mobile/digital finance services | (Bangko Sentral ng Pilipinas, 2026) | BSP CES 2Q 2026 as the recommended consumer/primer source | **Confirm the specific digital-finance uptake figure from the cited BSP report** |
| 9 | II-P1 | PUEPS used purposive sampling among working young adults in NCR; respondents drawn primarily from Taguig, Pasay, Manila, and Makati | (PUEPS, 2026) | Findings file Study Design: Taguig 30%, Pasay 17%, Manila 13%, Makati 11%, QC 9% | None (note the four cities are "primarily" — Honest description) |
| 10 | II-P2 | Survey confirmations: 95.7% (45/47) finances challenging; 85.1% (40/47) monitor spending difficulty; 66.0% (31/47) / 80.9% (38/47) where money goes; 72.3% (34/47) / 97.9% (46/47) unexpected obligations; 68.1% (32/47) tools too complex; 89.4% (42/47) not Filipino-context; 89.4% (42/47) limited insights; 83.0% (39/47) privacy | (PUEPS, 2026) | Re-transcribed and confirmed 2026-09-13 against `PUEPS-responses.csv` (see Appendix note below) | None (figures recomputed from raw CSV) |
| 11 | II-P3 | Unmonitored unusual spending strains budgets; debt vs savings tension → defer savings / higher-cost debt; reduces financial resilience | (PUEPS, 2026; Danahy et al., 2024; Ganong et al., 2025; Wang-Ly & Newell, 2023; Yeo et al., 2023) | Savings-allocation pattern from PUEPS (68.1% every-salary/or often; ~1/3 sometimes/rarely/never); Danahy: debt-stress; Ganong/Wang-Ly/Yeo: volatility and planning → resilience | Generalization from college-debt findings (#11 stress mechanism) |
| 12 | II-P4 | BUDI problem→feature mapping; every major function tied to an identified problem | (PUEPS, 2026) (feature-preference figures P5) | PUEPS feature expectations: forecasts helpful 94%, alerts 98%, personalized suggestions 100% | None |
| 13 | II-P5 | Four model families with explicit input/output; models must stay reliable as behavior evolves | (Abdullahi et al., 2025) | Abdullahi: concept drift degrades time-series/classification performance | Applicability of concept-drift findings to personal-finance profile classification |

### III. Purpose and Description of the Study

| # | Location | Claim (abridged) | In-text citation | What the source supports | Residual verify |
|---|---|---|---|---|---|
| 14 | III-P1 | Purpose, intended users, and the three concerns the study addresses | Self-authored description | — | None |
| 15 | III-P2 | BUDI described (Android + React for Web, offline-first, Filipino-context categories, privacy, DPA 2012) | Self-authored description (DPA reference is legal naming, not a research claim) | — | None |
| 16 | III-P3 | Candidate algorithms and how each functions on its key feature (SVM, SARIMA, LP/HiGHS, IQR); final selection by comparative evaluation | No research citation (methodology); concept-drift support only in II-P5 | — | None |
| 17 | III-P4 | Savings/debt improvement measured via in-app indicators (savings rate, goal growth, alert reduction, repayment progress); respondent preference figures | (PUEPS, 2026) | PUEPS feature expectations 94%/98%/100% | None |
| 18 | III-P5 | Expected contribution; SDG 1 & 8 alignment | No citation + `<!-- VERIFY -->` on SDG wording | — | **Confirm claim alignment against the UN SDG framework wording** |
| 19 | GO | General objective mirrors the official four-model title | Self-authored | — | None |
| 20 | SO3 | Data from BSP CFS, PSA FIES, synthetic personas; public microdata via PSADA; consent for direct survey | Self-authored methodology | — | PSADA access specifics to confirm (see Scope #22) |

### IV. Scope and Limitations

| # | Location | Claim (abridged) | In-text citation | What the source supports | Residual verify |
|---|---|---|---|---|---|
| 21 | Scope-Locale | NCR locale; users 20–40; purposive sampling; respondent cities | (Bangko Sentral ng Pilipinas, 2026; PUEPS, 2026) | BSP CES context; PUEPS sample design | None (adviser comment #6 resolved via team decision — see log) |
| 22 | Scope-Tech | Public PH datasets (BSP, PSA/PSADA) are household-level/aggregate → synthetic data for training | (Bangko Sentral ng Pilipinas, 2026) + PSA `<!-- VERIFY -->` | BSP CES as an aggregate household survey example | **Confirm exact FIES/PSADA dataset years and access date** |
| 23 | Scope-Tech | Forecasting limited to periods/categories with sufficient history; alerts from recorded baseline; outputs subject to user approval | Self-authored | — | None |
| 24 | Limitations | Each limitation mapped to an objective/feature (sampling→SO1, data→SO3, manual entry→SO5, model limits→SO4, Android-only→SO8, concept drift→II-P5, non-advice→III) | (Abdullahi et al., 2025) | Drift evidence only | None |

### V. Operational Definition of Terms

No citations required (terms defined operationally for this study). Per adviser annotations, `Time-Series Data` (flagged "not part") and `Transaction Data` (flagged "general") were removed; `Category-Level Spending Forecast` and `Purposive Sampling` added; `Recurring Transaction` retained with its V4 scope.

## Adviser feedback log (Drive V4 → V5 action)

### Comments (comments.xml)

| # | Source / date | Comment | V5 action |
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

| Annotation | V5 action |
|---|---|
| (TODO: Verify if all the core features are included here.) | II-P4 feature sentence rewritten and synchronized with SO5. |
| `[[organized]]` "this is a system characteristic" | Replaced with "structured transaction, income, and obligation records." |
| (discuss how models will function on the key features) | III-P3 explains how each candidate algorithm functions on its feature. |
| (Add: The researchers will utilize and discuss how it will function on its key feature) | III-P3 opening sentence added. |
| (what algo/ model do you plan to use) | SO4 names candidate algorithms per family; selection kept open pending SO4 metrics. |
| (Add user account management) | New SO5.3 User Account Management; Scope functional list matches. |
| (what are the recurring transactions?) | SO5.6 defines recurring income/expenses/savings/debt; term kept in Section V. |
| (how do you plan to monitor these?) (financial accounts) | SO5.9 states accounts are monitored via recorded transactions and balances, without API integration. |
| (how do you plan to do this / breakthrough feature) (debt repayment strategies) | SO5.12 describes snowball/avalanche comparison with payoff projection. |
| (Add: usability sub-characteristics) | SO7 adds Usability: recognizability, learnability, user error protection, UI aesthetics, accessibility. |
| (Replace "Reliability…" with "usability") | SO7 includes Usability; Reliability retained per PRD `product-requirements-document.md`. |
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

1. **BSP digital-finance uptake** for the 20–40 justification (II-P1, `#8`) — pull the specific figure from the cited BSP CES/CFS report or soften the claim.
2. **PSA FIES / PSADA** — add a verified reference (official report) and exact dataset years/access date (`#22`).
3. **SDG wording** — confirm the SDG 1/8 alignment phrasing against the UN framework (`#18`).
4. **Generalization flag `#11`** — the debt→stress mechanism cites Danahy et al. (college-student context); decide whether a qualifying clause suffices or a stronger source is needed.
5. **Andresen et al. (2025)** and **Rane et al. (2024)** remain in the intake uncited; confirm they are reserved for Chapters 2–3.
6. **Locale framing** — team decision keeps NCR + purposive sampling; keep the Drive doc and this chapter consistent when the adviser re-checks.