# BUDI ML — Documentation Index

## ML Development Phases

| Phase | Status | Key Deliverables | Documentation |
| :--- | :---: | :--- | :--- |
| **1. Problem Statement** | Complete | Model Design Document (MDD), 4 module designs, feasibility analysis | `1_problem-statement/README.md` |
| **2. Data Collection** | Complete | FIES 2023 NCR data, PSA/BSP datasets, FIES dictionary | `2_data-collection/`, `BUDI-ML/training/datasets/` |
| **3. Data Preprocessing** | Complete | Preprocessed raw data (train/val/test), temporal fold metadata | `3_data-preprocessing/preprocessing.md` |
| **4. Exploratory Data Analysis** | Complete | EDA report, plots, class balance, correlations, data quality | `4_eda/`, `BUDI-ML/training/docs/4_eda/eda_report.md` |
| **4.5. Dimension & Threshold Discovery** | Complete | Dimension threshold candidates, clustering analysis, binary split validation | `4.5_dimension-threshold-discovery/`, `BUDI-ML/training/datasets/dimension-discovery/` |
| **5. Feature Engineering** | Complete | 17 derived features, cyclical encoding, interaction features, feature selection, PCA | `5_feature-engineering/` |
| **6. Model Training** | Complete | PFP (Tier 0–4), Forecaster (RF selected; PyTorch LSTM/GRU/BiLSTM tiers implemented, not selected), Anomaly (IF + AE) | `6_model-training/` |
| **7. Model Evaluation** | Partial | PFP/Forecaster/Anomaly evaluation JSONs + reports; new-scope runbook in `Odin-ML/training/docs/phases/07-model-evaluation.md` | `6_model-training/`, `Odin-ML/models/*/metadata.json` (new scope) |
| **8. Model Selection & Versioning** | Pending (scaffolded) | Canonical `Odin-ML/models/` artifact home + `metadata.json` schema; runbook `Odin-ML/training/docs/phases/08-*.md` | `Odin-ML/models/README.md` |
| **9. Deployment** | Partial | Serving API + budget optimizer stubbed; containerization/CI-CD pending | `1_problem-statement/deployment-architecture.md` |
| **10. Model Monitoring** | Pending | Drift detection, retraining triggers | `Odin-ML/training/docs/phases/10-model-monitoring.md` |

## Data Sources

| Source | Year | Scope | Use |
|--------|------|-------|-----|
| **PSA 2023 FIES NCR** | 2023 | 41,380 households, 87 columns | Financial numerical baselines (income, expenditure, savings rates) |
| **BSP 2021 Consumer Finance Survey** | 2021 | 267 pages, nationwide | Behavioral/attitudinal patterns (savings behavior, debt patterns, financial inclusion) |

## Documentation Structure

```
ml/
├─ README.md                              # This file — documentation index
├─ TODO.md                                # MDD follow-up tasks and known gaps
├─ 1_problem-statement/
│  ├─ README.md                          # Phase 1 in-depth guide
│  ├─ module-design-document.md          # MDD — PFP, Forecaster, Anomaly, Budget Optimizer
│  ├─ module-integration.md              # Inter-module API contracts (v1.1)
│  ├─ deployment-architecture.md         # Container/k8s/CI-CD design (v1.1)
│  ├─ feature-set.md                     # Complete feature definitions (3 models)
│  ├─ walk-forward-validation.md         # Temporal validation methodology
│  ├─ partial-window-splits.md           # Train/val/test splitting strategy
│  ├─ roc-cutoff-selection.md            # Threshold calibration for PFP
│  ├─ bsp-fies-crosswalk.md              # BSP CFS ↔ FIES NCR field mapping + archetype justification
│  ├─ synthetic-injection-rules.md       # Rules for FIES→Persona→Transaction generation
│  ├─ persona-validation-list.md         # 12 archetypes (A-L) for SME review
│  └─ persona-validation-list-SME-draft.md # SME review draft of the archetype roster
├─ 2_data-collection/
│  └─ README.md                          # Phase 2 in-depth guide (FIES dictionary xlsx + dependency report stay in BUDI-ML)
├─ 3_data-preprocessing/
│  ├─ README.md                          # Phase 3 in-depth guide
│  └─ preprocessing.md                   # Preprocessing pipeline documentation
├─ 4_eda/
│  └─ README.md                          # Phase 4 in-depth guide (generated EDA report stays in BUDI-ML)
├─ 4.5_dimension-threshold-discovery/
│  └─ README.md                          # Phase 4.5: PFP dimension & threshold discovery (generated candidates/JSON stay in BUDI-ML)
├─ 5_feature-engineering/
│  ├─ README.md                          # Phase 5 in-depth guide
│  └─ feature-engineering.md             # Feature engineering pipeline documentation
└─ 6_model-training/
   ├─ README.md                          # Phase 6: PFP Classifier training (Tier 0-4)
   ├─ forecaster-training.md             # Forecaster training (RF + PyTorch LSTM/GRU/BiLSTM)
   └─ anomaly-training.md                # Anomaly Detector training (IF + AE)
```

## Model Candidate Roster

A new-scope model candidate roster mapping each model family to candidate algorithms from the RRL corpus lives in `Odin-ML/docs/models/model-candidate-roster.md`. It incorporates review of the batch-1..6 algorithm screenings and grounds Phase 7–8 candidate selection.

## Scripts

| Script | Purpose | Status |
|--------|---------|--------|
| `BUDI-ML/training/scripts/collector.py` | CSV to Parquet conversion for raw datasets | Complete |
| `BUDI-ML/training/scripts/generate_personas.py` | 12-archetype (A-L) persona generator from FIES data | Complete |
| `BUDI-ML/training/scripts/generate_transactions.py` | 12-month transaction history generator | Complete |
| `BUDI-ML/training/scripts/preprocessor.py` | Synthesis + splitting + raw data export | Complete |
| `BUDI-ML/training/scripts/feature_engineering.py` | 17 derived features + encoding + selection + PCA | Complete |
| `BUDI-ML/training/scripts/feature_engineering_forecaster.py` | Forecaster-specific feature engineering (RFM, STL, lags) | Complete |
| `BUDI-ML/training/scripts/feature_engineering_anomaly.py` | Anomaly-specific per-transaction feature engineering | Complete |
| `BUDI-ML/training/scripts/eda.py` | Exploratory data analysis with plots + report | Complete |
| `BUDI-ML/training/scripts/train_pfp.py` | PFP Classifier training (Tier 0-4), temporal fold evaluation | Complete |
| `BUDI-ML/training/scripts/train_forecaster.py` | Forecaster training (RF + PyTorch LSTM/GRU/BiLSTM) | Complete |
| `BUDI-ML/training/scripts/train_anomaly.py` | Anomaly Detector training (IF + AE) | Complete |
| `BUDI-ML/training/scripts/dimension_discovery.py` | Phase 4.5: clustering analysis + overlay feature computation | Complete |
| `BUDI-ML/training/scripts/fies_columns.py` | FIES variable ID ↔ CSV column mapping | Complete |
| `BUDI-ML/training/scripts/synthesizer.py` | Deprecated — use `preprocessor.py` instead | Deprecated |

## Pipeline Execution Order

```
1. python BUDI-ML/training/scripts/collector.py --input BUDI-ML/training/datasets/raw/ --output BUDI-ML/training/datasets/unprocessed/
   → Converts CSV files to Parquet format

2. python BUDI-ML/training/scripts/preprocessor.py --input BUDI-ML/training/datasets/unprocessed/puf.parquet --output BUDI-ML/training/datasets/processed/
   → Runs synthesis (personas + transactions → BUDI-ML/training/synth/)
   → Generates: train.parquet, val.parquet, test.parquet (raw data), temporal_folds.json

3. python BUDI-ML/training/scripts/feature_engineering.py --input BUDI-ML/training/datasets/processed/ --output BUDI-ML/training/datasets/engineered/
   → Computes 17 derived features + cyclical encoding + interaction features
   → Optional: feature selection, PCA dimensionality reduction
   → Generates: train.parquet, val.parquet, test.parquet (engineered), feature_columns.json

4. python BUDI-ML/training/scripts/eda.py --input BUDI-ML/training/datasets/engineered/ --output BUDI-ML/training/figures/
   → Generates: eda_report.md, *.png plots

4.5. python BUDI-ML/training/scripts/dimension_discovery.py --input BUDI-ML/training/datasets/processed/ --output BUDI-ML/training/datasets/dimension-discovery/
   → Unsupervised clustering on Stability/Necessity scores
   → Computes Financial Trajectory and Financial Margin features

5. python BUDI-ML/training/scripts/train_pfp.py --input BUDI-ML/training/datasets/engineered/ --output BUDI-ML/training/models/pfp/
   → Trains PFP Classifier model (Tier 0-4)
   → Generates: BUDI-ML/training/models/pfp/ (intermediate artifacts + evaluation.json + evaluation_report.md)
   → Promote the final selected artifact to BUDI-ML/models/pfp/ with metadata.json (Phase 8)

6. python BUDI-ML/training/scripts/feature_engineering_forecaster.py
   → Generates forecaster feature sets (BUDI-ML/training/datasets/forecaster/)

7. python BUDI-ML/training/scripts/train_forecaster.py
   → Trains Forecaster model (RF + PyTorch LSTM/GRU/BiLSTM)
   → Generates: BUDI-ML/training/models/forecaster/ (artifacts + evaluation)
   → Promote the final selected artifact to BUDI-ML/models/forecaster/ with metadata.json (Phase 8)

8. python BUDI-ML/training/scripts/feature_engineering_anomaly.py
   → Generates per-transaction anomaly features

9. python BUDI-ML/training/scripts/train_anomaly.py
   → Trains Anomaly Detector model (IF + AE)
   → Generates: BUDI-ML/training/models/anomaly/ (artifacts + evaluation)
   → Promote the final selected artifact to BUDI-ML/models/anomaly/ with metadata.json (Phase 8)

10. Serving: uvicorn app.main:app --reload --port 8000
    → Loads PFP, Forecaster, Anomaly artifacts; Budget Optimizer runs scipy LP
```

> **New-scope canonical artifact home** is the top-level `Odin-ML/models/` directory (one final
> artifact + `metadata.json` per family). The superseded scope's winner artifacts remain under
> `BUDI-ML/training/figures/models/`. See `Odin-ML/models/README.md` and
> `Odin-ML/training/docs/phases/`.

## Known Data & Version Gaps

- Persona source count 300 vs. 12,000 generated personas (see `TODO.md`).
- PFP per-class zero support for some labels (labeling artifact of synth data).
- Python and scikit-learn pins now aligned with the spec and training artifacts: Python 3.14.4 (`.python-version`), scikit-learn 1.9.0 (`requirements.txt`). Rebuild the venv under these pins if it predates 2026-08-13.
