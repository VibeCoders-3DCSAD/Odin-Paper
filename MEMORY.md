# BUDI-Base — Session Memory

- **2026-09-24 — TBD resolution register created.** `docs/requirements-engineering/tbd-register-resolution.md`
  maps all 27 spec TBDs (owner tabs Models/System/Paper) to repo evidence and recommended decisions.
  Key findings: temporal disaggregation #1 is RESOLVED as proportional benchmarking (FIES-anchored,
  HFCE-calibrated) — the spec's Chow-Lin/Denton/Litterman list is unused; classifier #4 formulas
  (EFC/DSTI/FM/CC `financial_rules_v1`) specified in BUDI-ML but the saver/borrower profile-composition
  rule is not; cold-start anomaly #9 is RESOLVED (alerts disabled until `n_u≥N_min`, no population
  fallback — spec limitation wording should be tightened); SARIMA blend + `N_min` (#6) and IQR fence
  calibration (#8) are OPEN pending experiments; System items 10–20 are DECISION items with draft
  recommendations; Paper 21–27 are drafted/pending (theoretical-framework is still a placeholder).
  Endpoint mismatch: spec 09.24 proposes new routes (`/api/v1/profile/*`, `/budget/optimize`) that do
  not match served routes (`/classification/v2`, `/budget/recommend`) — adoption decision pending (#15).
- **2026-09-24 — Technical Specification V1 (09.24.2026) fetched & re-mirrored.** The
  Drive doc (same ID `1v8hqqlsHuiEAugGe3or3BCG2F8zQ3aWCCyox--oMm6E`, renamed from
  V1 09.20.2026, last modified 2026-09-24 07:51Z) is now the ground truth. Mirror
  regenerated at `docs/requirements-engineering/technical-specification.md`; the 09.20
  docx in `google-drive/technical-specification/` was replaced. The 09.24 revision is a
  **substantial rewrite**: project identity is now **TAYA** ("Development of TAYA: A
  Personal Financial Management App Using SARIMA-Based Seasonal Expense Forecasting
  for Budget, Savings, and Debt Planning"; acronym words still TBD). It restructures
  into four specs (Project / Paper / System / Models) with a formal Project TBD
  Register (owner tabs: Models, System, Paper). Title algorithms stated natively:
  rule-based saver/borrower classifier, SARIMA forecaster with temporal
  disaggregation (FIES 2023 + HFCE 2022 Q1–2026 Q2), LP/HiGHS solver, IQR detector;
  central Financial Plan artifact. Endpoints now under `/taya/api/` (sync) and
  `/api/v1/profile|forecast|anomaly|budget/*`. The prior 09.21 "v2 methodology
  overrides" note is superseded. `BUDI-ML/docs/models/*` and
  `training/docs/model-methodologies/*` still use v2/legacy naming — flag for
  realignment when filling the models TBDs.
- **2026-09-21 — New-scope realignment (SUPERSEDED by 09.24 fetch).** The Drive *Technical Specification V1
  (09.20.2026)* was the ground truth for systems, paper, and models (mirror:
  `docs/requirements-engineering/technical-specification.md`). The adopted model
  methodologies (financial classification v2 — rule-based EFC/DSTI/FM/credit-card;
  anomaly alerts v2 — dual-channel IQR; budget optimizer v2 — hierarchical LP)
  **override the spec's title-algorithm column**. Methodology documents were injected
  from the temporary `updates/` staging folder into `BUDI-ML/training/docs/model-methodologies/`
  and the staging folder removed. `updates/` is not a permanent home for new docs.
- **Repo naming:** repositories are now `BUDI-Base`, `BUDI-App`, `BUDI-ML`,
  `BUDI-Literature` (workspace root uses these names, not `Odin-*`).
- **Title in use:** "Development of BUDI: A Personalized Intelligent Finance
  Management Application for Filipinos Using Classification, Forecasting,
  Optimization, and Anomaly Detection Models for Improving Savings and Debt".
  (The 09.20 spec's "MULTI-MODEL ARCHITECTURE" title is not used.)
- **Pending reminder (user):** fix the spec title in GDrive and align the spec's
  model/algorithm table once Phase 2 lands.