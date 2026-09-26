# BUDI ML — Documentation Index

Study-level index for the four BUDI intelligent modules. **Implementation, code, and
the adopted new-scope methodologies live in `BUDI-ML`** — this directory only mirrors
the study-level design history.

> **Spec update (2026-09-24):** the Drive *Technical Specification V1 (09.24.2026)*
> now states the title algorithms natively (rule-based saver/borrower classifier,
> SARIMA forecaster with FIES 2023 + HFCE 2022 Q1–2026 Q2 temporal disaggregation,
> LP/HiGHS solver, IQR detector) under the **TAYA** project identity, so the prior
> "override" framing no longer applies. BUDI-ML docs still use the legacy v2 names;
> naming realignment is tracked in `docs/requirements-engineering/tbd-register-resolution.md`.
> Reference documents (current mapping):
>
> | Module (09.24 spec) | Adopted methodology (BUDI-ML) | Contract spec (BUDI-ML) |
> | :--- | :--- | :--- |
> | Rule-Based Classifier | `training/docs/model-methodologies/financial-classification-v2-methodology.md` | `docs/models/classification-v2.md` |
> | IQR Detector (unusual expense) | `training/docs/model-methodologies/anomaly-alerts-v2-methodology.md` | `docs/models/anomaly-alerts-v2.md` |
> | LP Solver / Budget Creation | `training/docs/model-methodologies/budget-optimizer-methodology.md` | `docs/models/budget-optimizer.md` |
> | SARIMA Forecaster | `docs/models/forecaster-v2.md` | served artifact `BUDI-ML/models/forecaster_v2/` |

## Status Summary (new scope)

| Module | Approach | Needs training? | Evaluation metrics |
| :--- | :--- | :---: | :--- |
| Financial classification v2 | Rule-based: EFC (<3 / ≥3 mo), DSTI (≤40% / >40%), Financial Margin (≥0 / <0), Credit-card behavior (transactor / light / heavy) | No | Accuracy, Precision, Recall, F1-score (one-vs-rest macro for 3-class) on reference-labeled synthetic sets |
| Expense forecasting | Pooled SARIMA (served `forecaster_v2`; v3 gated on external validation) | Yes | MAE, SMAPE, MDA, RMSE |
| Anomaly alerts v2 | Personalized dual-channel IQR: transaction-level IQR + forecast-residual IQR, `OR` combination | No (statistical bounds) | Accuracy, Precision, Recall, F1-score |
| Budget optimizer v2 | Hierarchical LP (Essentials → Emergency → Debt → Savings → Other), strict + partial-allocation solves | No | Constraint Satisfaction Rate, Budget Utilization Rate, Deviation from User Preferences |

## Superseded Training-Era Docs

The `problem-statement/`, `data-collection/`, `data-preprocessing/`,
`exploratory-data-analysis/`, `dimension-threshold-discovery/`, `feature-engineering/`,
and `model-training/` folders document the **superseded training-era scope** (trained
PFP SVM tiers, trained forecaster candidates, IF/AE anomaly detectors). They are kept
for historical reference only and are **not** the current designs. See `_SUPERSEDED.md`
below.

## Documentation Structure

```
ml/
├─ README.md                # This file — new-scope index
├─ _SUPERSEDED.md           # Scope-change notice for the training-era docs below
├─ problem-statement/       # Phase 1: MDD, feature sets, module integration, deployment (superseded scope)
├─ data-collection/         # Phase 2: FIES/BSP data source documentation (superseded scope)
├─ data-preprocessing/      # Phase 3: preprocessing pipeline documentation (superseded scope)
├─ exploratory-data-analysis/# Phase 4: EDA guide (superseded scope)
├─ dimension-threshold-discovery/ # Phase 4.5: PFP dimension & threshold discovery (superseded scope)
├─ feature-engineering/     # Phase 5: feature engineering pipeline documentation (superseded scope)
└─ model-training/          # Phase 6: trained PFP/Forecaster/Anomaly candidates (superseded scope)
```

## Data Sources (unchanged)

| Source | Year | Scope | Use |
|--------|------|-------|-----|
| **PSA 2023 FIES NCR** | 2023 | 41,380 households, 87 columns | Income/expenditure baselines, synthetic household generation |
| **PSA HFCE** | quarterly | Aggregate | Temporal calibration of synthetic monthly expenditure |
| **BSP CFIS / CFS / CES** | 2025 / 2021 / — | Nationwide | Contextual financial-inclusion and behavior patterns |
| **PUEPS** | 2026 | NCR (47 respondents) | User expectations, preliminary investigation |

## Pipeline Execution Order (superseded scope; forecasting still uses this path)

The trained-forecaster pipeline still follows `BUDI-ML/README.md`:

```
collector.py → preprocessor.py → feature_engineering.py
  → feature_engineering_forecaster.py → train_forecaster.py
  Serves via BUDI-ML.models/forecaster_v2/tier3_sarima.joblib
```

See `BUDI-ML/README.md` and `BUDI-ML/docs/models/` for the authoritative pipeline and runbooks.

## Canonical Artifact Home

Final model artifacts + `metadata.json` per family live in **`BUDI-ML/models/`**.
Training lives in `BUDI-ML/training/` (scripts + docs only; large matrices gitignored).
See `BUDI-ML/models/README.md` and `BUDI-ML/training/docs/phases/`.