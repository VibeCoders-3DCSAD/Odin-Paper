# Superseded Training-Era Docs — Scope-Change Notice

**Date:** 2026-09-21

The phase folders under `docs/ml/` (`problem-statement/`, `data-collection/`,
`data-preprocessing/`, `exploratory-data-analysis/`, `dimension-threshold-discovery/`,
`feature-engineering/`, `model-training/`) document the **superseded training-era
model scope** — trained PFP SVM tiers, trained forecaster candidates, and learned
anomaly detectors (IF / autoencoder / hybrid).

They are kept for **historical reference only**. The adopted new-scope designs are:

| Module | Adopted design | Trained model? |
| :--- | :--- | :---: |
| Financial classification v2 | Rule-based (EFC, DSTI, Financial Margin, credit-card behavior) | No |
| Anomaly alerts v2 | Personalized dual-channel IQR (transaction + forecast-residual) | No |
| Budget optimizer v2 | Hierarchical LP with feasibility / partial-allocation | No |
| Expense forecasting | Pooled SARIMA (`forecaster_v2`; v3 gated) | Yes |

Authoritative methodology and implementation documentation lives in **`BUDI-ML`**:

- `BUDI-ML/training/docs/model-methodologies/` — adopted methodology + evaluation plans
- `BUDI-ML/docs/models/` — condensed service-contract specs
- `BUDI-ML/README.md` — service and pipeline

Do not cite the superseded winners (e.g., "forecaster: Random Forest wins",
"anomaly: Isolation Forest wins") in thesis documents without an explicit
"superseded scope" qualifier.