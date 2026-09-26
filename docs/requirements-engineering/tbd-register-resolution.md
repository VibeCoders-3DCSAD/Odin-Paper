# TBD Resolution Register — Technical Specification V1 (09.24.2026)

> **Working document.** Tracks each item in the Drive *Technical Specification V1
> (09.24.2026)* "Project TBD Register" (sections by owner tab: Models, System, Paper).
> For each item: current status, the evidence that resolves or partly resolves it, and
> the recommended decision where one is still needed. Drive remains the source of
> truth; this register is the mirror-side working map used to draft the spec updates.
>
> Status legend: **RESOLVED** (answer exists in repos/docs), **PARTIAL** (direction
> defined, gap remains), **DECISION** (open call; recommended option proposed for team
> confirmation), **OPEN** (no candidate yet / awaiting external input).
>
> Canonical mirror of the spec: `docs/requirements-engineering/technical-specification.md`.

---

## Summary

| # | TBD | Owner | Status | Recommended resolution |
| --- | --- | --- | --- | --- |
| 1 | Temporal disaggregation method | Models | RESOLVED | Proportional benchmarking (FIES-anchored, HFCE-calibrated) — already implemented; not Chow-Lin/Denton/Litterman |
| 2 | Savings and debt categories and primary sources | Models | PARTIAL | Category taxonomy + Filipino categories exist; dataset/persona sources for savings & debt to be pinned |
| 3 | SME validation of thresholds | Models | PARTIAL | Thresholds are literature-published defaults (`financial_rules_v1`); explicit SME sign-off pending |
| 4 | Rule-Based Classifier formulas and dimensions | Models | PARTIAL | EFC/DSTI/FM/CC formulas + `financial_rules_v1` defined; saver/borrower profile composition rule to formalize |
| 5 | Rule-Based Classifier label availability | Models | PARTIAL | No human labels; use rule-derived reference labels + boundary-case test set |
| 6 | SARIMA blending + cold-start threshold | Models | OPEN | Directional design in spec §3.2; blend weight + `N_min` need experiment |
| 7 | Category alignment FIES ↔ HFCE | Models | PARTIAL | Implemented per-category; auditable mapping table to publish |
| 8 | IQR threshold calibration | Models | PARTIAL | Tukey 1.5×IQR fences; `N_min` stability experiment pending |
| 9 | Cold-start anomaly behavior | Models | RESOLVED | Alerts disabled until `n_u ≥ N_min`; explicit insufficient-history state; no population fallback |
| 10 | Financial Planning placement | System | DECISION | Host in api-gateway (no model); no separate container |
| 11 | Event bus selection | System | DECISION | Recommend RabbitMQ (low-volume, per-user events) |
| 12 | Cloud provider | System | OPEN | Supabase (managed) for Postgres + Auth; PaaS container host; team to confirm |
| 13 | Orchestration and infrastructure | System | DECISION | Docker Compose on a single VM (six containers) |
| 14 | NFR numeric targets | System | DECISION | Draft targets proposed (latency/availability/storage) |
| 15 | API contracts, schemas, data dictionary | System | PARTIAL | Contracts exist (BUDI-ML / BUDI-App schema); spec endpoint list needs validation/adoption |
| 16 | Deployment and DevOps | System | DECISION | Docker Compose + GitHub Actions CI |
| 17 | Auth/governance online/offline | System | DECISION | Auth online-only; consent/privacy enforced locally + synced |
| 18 | Data foundation container | System | DECISION | Temporal disaggregation is a batch training step, not a runtime service |
| 19 | Financial Planning container | System | DECISION | See #10 — no separate container |
| 20 | Feedback loop mechanism | System | DECISION | Scheduled/event-driven re-fit into Stage 1 (weekly cadence + on-demand) |
| 21 | KPIs for savings and debt improvement | Paper | DECISION | KPI table proposed (savings rate, goal progress, alert frequency, debt progress) |
| 22 | Portability testing details | Paper | PARTIAL | Android-only; adaptability/installability across OS versions/sizes (+ RNW) |
| 23 | Final research gap definition | Paper | OPEN | Spec §2.3 drafted; pending RRL validation against BUDI-Literature |
| 24 | Research problem wording | Paper | PARTIAL | Spec §2.1 drafted; pending approval |
| 25 | MRQ final wording | Paper | PARTIAL | Spec §3.1 drafted; pending approval |
| 26 | Novelty claim | Paper | OPEN | Pending RRL validation |
| 27 | Theoretical/conceptual framework | Paper | OPEN | `docs/rrl/theoretical-framework.md` is a placeholder; to be written |

---

## Models tab

### 1. Temporal disaggregation method — RESOLVED

**Spec asks:** Chow-Lin, Denton, Litterman, or another approach.

**Evidence:** the implemented and documented method is **"FIES-anchored, HFCE-calibrated
temporal disaggregation with proportional benchmarking"**:

- `BUDI-ML/training/scripts/temporal_disaggregation.py` (calendar-year current-price HFCE load, per-category quarterly weights, annual→month allocation, reconcile-to-annual).
- `BUDI-ML/training/docs/data-collection/fies-hfce-synthetic-data-generation-methodology.md` (§ "Methodology": FIES annual household-category benchmark distributed by PSA HFCE quarterly shares `W_{y,c,q}`; equal monthly thirds within a quarter; 2026 Q1–Q2 only, reconciled to six months).
- Tests: `BUDI-ML/tests/test_temporal_disaggregation.py`, `test_synth_v2_transactions.py`.

**Resolution:** the spec §2.4 should name the adopted method as **proportional benchmarking /
equiproportional disaggregation with reconciliation** (Eurostat-temporal-disaggregation family,
Chow-Lin/Denton/Litterman not used, as those are regression-based and not needed for calibration).
Spec update: remove the un-used candidate list; keep the held-out-quarter and SME-review evaluation
criteria unchanged. The 2026 Q1–Q2 partial-year treatment is already handled (reconcile to six months).

### 2. Savings and debt categories and primary sources — PARTIAL

**Evidence:** the expense category taxonomy and Filipino-context categories exist:
`BUDI-App/schema/seeded-category-taxonomy.json` (envelopes Essentials / Emergency / Debt / Savings /
Other; Filipino-context categories family support, government contributions, paluwagan, ambag).
Savings/debt *primary sources* (which dataset/persona columns or user-entry fields feed the solver)
are not yet documented.

**Proposed completion:** pin savings sources to Income Sources + Savings Goal streams and debt
sources to Debt Manager streams + BSP CFIS (household) definitions; publish as a data dictionary row
in the Models tab. Owner: Models + System (data dictionary).

### 3. SME validation of thresholds — PARTIAL

**Evidence:** `financial_rules_v1` thresholds are **published international defaults**, not invented:
EFC 3 months (Bhutta et al. 2023; Fed 2024), DSTI 40% (He & Zhou 2022), FM 0 (He & Zhou 2022), CC
12-month window (Adams et al. 2022) — see `BUDI-ML/docs/models/classification-v2.md`. Persona roster
was reviewed by a general-finance SME (Asst. Prof. Pamela A. Go) but that was roster validation, not a
threshold sign-off (`BUDI-Base/docs/ml/problem-statement/persona-validation-list-SME-draft.md`,
`BUDI-ML/docs/models/forecaster-v2.md`).

**Proposed completion:** an SME sign-off session on the exact `financial_rules_v1` thresholds (incl.
the probability-of-default-related "40%" boundary semantics) so the spec can mark "validated".

### 4. Rule-Based Classifier formulas and dimensions — PARTIAL

**Evidence:** all four formulas fully specified in `BUDI-ML/docs/models/classification-v2.md`:
EFC (liquid savings / avg monthly essential expenses), DSTI (100 × required debt payments / monthly
disposable income), FM (disposable income − debt payments − basic living costs), CC (revolving-months
count in a 12-month window) with `financial_rules_v1` version tag.

**Gap:** the explicit rule that maps the four financial-condition dimensions to the spec's
**saver / borrower / both / neither** profile is not yet formalized.

**Proposed completion (Models):** add a profile-composition rule table to classification-v2.md, e.g.:
borrower if DSTI > 40% or FM < 0; saver if EFC ≥ 3 months or CC transactor; both when both conditions
hold; neither/holding otherwise — to be confirmed against the primary-sources definition in #2.

### 5. Rule-Based Classifier label availability — PARTIAL

**Evidence:** classification is deterministic; there is no human-labeled ground-truth corpus.

**Proposed completion (Models + Paper):** evaluate via rule-derived reference labels (self-consistency),
a hand-built boundary-case test set (exact-at-40% DSTI, EFC at 3.0, 12-month credit-card window edges),
and SME spot checks — model the evaluation on the anomaly/budget test-case pattern already used in
`BUDI-ML/tests/`. Metrics: Accuracy, Precision, Recall, F1 reported against the reference labels.

### 6. SARIMA blending + cold-start threshold — OPEN

**Evidence:** the spec §3.2 states the directional design (population SARIMA baseline → monthly
multipliers + `(P,D,Q)×12` specification; personal SARIMA with fixed seasonal orders; cold-start
fallback scaling the population baseline). Implementation: served forecaster is a **pooled** SARIMA on
a user-normalized monthly series (`BUDI-ML/docs/models/forecaster-v2.md`: `(1,1,0)(1,0,0,12)`, 24-month
seasonal-identification floor). The **per-user population↔personal blend** is not served; v3 is an
unserved RF research pipeline (`BUDI-ML/docs/models/forecaster-v3.md`).

**Proposed decision:** define `N_min` for personal SARIMA = **24 months** (aligned with the existing
`s=12` identification floor in the training gate). Blend above threshold: weight the personal forecast
linearly from 0→1 as user history goes `N_min`→`2×N_min`, clamping to the population monthly multipliers;
below threshold use the scaled population baseline. Confirm by an offline experiment on the v2/v3 corpus
blending vs personal-only vs population-only (metrics MAE/SMAPE/MDA/RMSE vs seasonal naive).

### 7. Category alignment FIES ↔ HFCE — PARTIAL

**Evidence:** aligned per-category for synthetic generation v2 (FIES annual category benchmark ↔ HFCE
purpose categories; config `BUDI-ML/training/config/hfce_quarterly_indices.json`; methodology
`fies-hfce-synthetic-data-generation-methodology.md`).

**Gap:** no standalone auditable crosswalk table published.

**Proposed completion:** publish the mapping (FIES category → HFCE category → forecast category,
incl. the residual-`other` handling) as a data-collection table in BUDI-ML; cite it in the Models tab.

### 8. IQR threshold calibration — PARTIAL

**Evidence:** fences are **Tukey 1.5×IQR** on log-transformed amounts per personal category, with a
forecast-residual channel; combined as OR (`BUDI-ML/docs/models/anomaly-alerts-v2.md`). The spec asks
for "threshold calibration"; the working doc requires `N_min` and fence stability to be chosen
experimentally across candidate windows 3/6/9/12/18/24 months (not arbitrarily).

**Gap:** the calibration experiment has not been run/published.

**Proposed completion:** run the window-stability experiment (Q1/Q3/IQR/forecast-error stability),
record the selected `N_min` and confirm 1.5× remains appropriate; update the Models tab.

### 9. Cold-start anomaly behavior — RESOLVED

**Evidence:** explicit policy in `BUDI-ML/docs/models/anomaly-alerts-v2.md` §Cold Start Policy: alerts
**disabled** until `n_u ≥ N_min`; return an explicit insufficient-history state; **no** manufactured
alert, normal result, or population-based fallback for the personal anomaly decision.

**Reconciliation note:** the 09.24 spec's *Limitations* say "population-level seasonality partially
mitigates this cold-start condition." For anomaly detection this must be limited to the **forecast
channel's seasonally aware input** (population seasonal input to the forecast), not a population anomaly
fallback — which the methodology forbids. Clarify wording in the Models tab accordingly.

---

## System tab

### 10. Financial Planning placement — DECISION (recommend: api-gateway)

The Financial Planning module composes the Financial Plan with **no model/algorithm** (spec §3.14).
Recommend hosting it **in the api-gateway container (port 8000)** — it already routes/aggregates
(model outputs). No separate container. Team to confirm.

### 11. Event bus selection — DECISION (recommend: RabbitMQ)

Personal-finance event volume is low and per-user; the sync model already needs idempotent message
semantics. Recommend **RabbitMQ** (AMQP: durable queues, per-user routing, simpler ops at this scale).
Kafka only if stream-replay or high fan-out is later required. Team to confirm.

### 12. Cloud provider — OPEN

**Recommendation pending team/university constraints:** keep **Supabase (managed)** for PostgreSQL +
Auth (already in the tech stack), plus a simple container host (Render/Fly.io/GCP Cloud Run) for the six
services; revisit only if cost/region policy requires. Needs a decision input from the team.

### 13. Orchestration and infrastructure — DECISION (recommend: Docker Compose)

Six containers on a single VM via **Docker Compose** with defined health checks and a compose-env for
secrets. Kubernetes is out of proportion at thesis scale. Team to confirm.

### 14. NFR numeric targets — DECISION (draft proposed)

| NFR | Proposed target |
| --- | --- |
| Availability | ≥ 99.5% (services), 100% core offline features |
| API latency | p95 ≤ 500 ms; ML routes (forecast/alert/budget solve) ≤ 2 000 ms |
| LP solve time | ≤ 1 000 ms (HiGHS, per budget period) |
| App cold start | ≤ 3 s on a mid-range Android device |
| Sync queue | ≤ 50 MB retained; push/pull latency p95 ≤ 5 s on 4G |
| Data export | ≤ 60 s for a single user dataset |
| Usability (SUS) | ≥ 68 (acceptable) |
| Security | no plaintext secrets; OWASP top-10 reviewed; RA 10173-aligned export/consent |

Numbers to be confirmed by the team before pushing to the spec.

### 15. API contracts, schemas, data dictionary — PARTIAL

**Evidence:** contracts in `BUDI-ML/docs/models/*.md` (classification-v2 `POST /api/v1/classification/v2`,
forecast `/forecast/predict`, anomaly `/anomaly/detect(+batch)`, budget `/budget/recommend(+batch)`),
schema in `BUDI-App/schema/` (`draft-schema-priority-modules-v3.sql`, `seeded-category-taxonomy.json`,
`erd-create-tables.sql`).

**Gap / action:** the 09.24 spec lists a **new proposed endpoint set**
(`/api/v1/profile/classify`, `/forecast/*`, `/anomaly/*`, `/budget/optimize`) flagged `[TBD: validate
listed endpoints]`. These do **not** match currently served routes. Decision needed: adopt the spec set
as canonical and alias/migrate the service, or revert the spec set to served routes. Recommend adopting
the spec set and migrating (backwards-compatible aliases for `classification/v2`, `budget/recommend`).
Also publish data-dictionary rows from the ERD.

### 16. Deployment and DevOps — DECISION (recommend: Docker Compose + GitHub Actions)

Per-container Dockerfiles, `docker compose up`, GH Actions CI running `ruff check`, `ruff format --check`,
`mypy app`, `pytest`; image build + push on release tags; artifacts from `BUDI-ML/models/` mounted
read-only. Team to confirm.

### 17. Auth and governance online/offline — DECISION (recommend: auth online-only)

- **Authentication online-only:** Google OAuth + email/password with email verification (Supabase Auth);
  offline mode uses the last locally approved, expiring session token.
- **Governance (ownership/consent/privacy):** enforced locally on the device and re-validated remotely
  at next sync — consistent with the sync model ("ownership validation performed both locally and
  remotely").
- Data export / account deletion: initiated online, queued if offline. Team to confirm.

### 18. Data foundation container — DECISION (recommend: batch, not a service)

Temporal disaggregation is a **model-training step** (spec Models §2.4) producing a frozen monthly
estimate artifact. Recommend **batch job** inside the training pipeline (BUDI-ML `training/`), output
consumed as a static artifact by the forecaster — no always-on container. Team to confirm.

### 19. Financial Planning container — DECISION (recommend: none)

Same rationale as #10. Financial Planning lives in the api-gateway (aggregation/composition). Team to
confirm (resolves the "separate container?" open item).

### 20. Feedback loop mechanism — DECISION (draft proposed)

**Mechanism (recommend):**
1. Stage 6 collects user plan approvals/rejections + new transactions + alert acknowledgements.
2. When personal history ≥ `N_min` (see #6), trigger refresh of the personal SARIMA forecast and
   re-run budget optimization; below threshold, refresh the scaled population-baseline forecast.
3. Cadence: **weekly scheduled refresh** plus an on-demand refresh on significant data change
   (e.g., new income/debt/goal or a batch of entered transactions).
4. Updated plan is re-fed into Stage 1 (Expense Forecasting) and presented for approval — closing the loop.
Pure rule-free definition still to be confirmed.

---

## Paper tab

### 21. KPIs for savings and debt improvement — DECISION (draft KPI table)

| KPI | Definition | Source |
| --- | --- | --- |
| Savings rate | monthly savings contributions / monthly income | Savings module + budget solver |
| Savings goal progress | funded weeks/months vs plan for each goal | Savings schedule (LP output) |
| Anomaly alert frequency | unusual-expense alerts per month | IQR detector |
| Debt repayment progress | principal paid vs plan per debt | Debt schedule (LP output) |
| Plan adherence | actual allocation vs recommended allocation | Financial Plan diff |

Aligned with the 09.24 main research question's savings-debt indicators; to be confirmed, then
matched to Models-tab metrics (MAE/SMAPE/MDA/RMSE; constraint-satisfaction rate; budget utilization;
Precision/Recall/F1).

### 22. Portability testing details — PARTIAL

Android-only (iOS out of scope). Approach: adaptability + installability checks across Android OS
versions (emulator matrix) and screen sizes, plus React Native Web for desktop/dev review; report
per ISO/IEC 25010 portability sub-characteristics and the #14 installability target. Confirm scope of
device matrix.

### 23. Final research gap definition — OPEN (drafted, needs RRL validation)

Spec §2.3 gap drafted (Philippine seasonal consumption → personalized expense forecasting → LP plans
under constraints). Validation step: check against `BUDI-Literature` corpus
(`BUDI-Base/docs/rrl/literature-matrix.md`, benchmarks) and reconcile chapter-1 re-rollout (#24/#25).
Owner: Paper + BUDI-Literature.

### 24. Research problem wording — PARTIAL (drafted, unapproved)

Spec §2.1 drafted. Needs: (a) approval, (b) alignment once chapter-1 is re-reconciled to the 09.24
spec (chapter-1 currently reconciled to the superseded 09.20 scope).

### 25. Main research question final wording — PARTIAL (drafted, unapproved)

Spec §3.1 proposed: "How is TAYA developed and evaluated as a seasonality-aware, closed-loop
savings-debt plan pipeline for Filipinos aged 18 to 59 in the National Capital Region?" — pending
approval and chapter-1 consistency.

### 26. Novelty claim — OPEN

Candidate framing: **first integrated PFM that converts Philippine seasonal consumption (HFCE) into
personalized expense forecasts and closed-loop LP-based savings/debt plans under constraints.**
Validation required against RRL; also required for the chapter-2/paradigm narrative. Owner: RRL.

### 27. Theoretical/conceptual framework — OPEN

`BUDI-Base/docs/rrl/theoretical-framework.md` is a TODO placeholder. Needs writing from the selected
RRL corpus (financial-behavior theory + FI theory + seasonality/statistical basis + LP planning), with
the 09.24 spec's Financial Plan pipeline as the conceptual core. Owner: Paper/RRL.

---

## Suggested next actions

1. Push the **RESOLVED** items (1, 9) and the **PARTIAL→RESOLVED** set (4 formulas, 7 mapping, 8
   fences, 2 taxonomy) into the Drive spec statuses/detail, with the evidence citations above.
2. Ask the team to confirm the **DECISION** items (10–14, 16–22) — these are product/ops choices only
   the group can ratify.
3. Run the two calibration experiments that unblock #6 and #8 (blend/personal-SARIMA threshold;
   IQR `N_min` stability) in BUDI-ML.
4. Keep `docs/requirements-engineering/technical-specification.md` and this register in sync with the
   Drive doc as the paper TBDs (23–27) move through RRL validation.