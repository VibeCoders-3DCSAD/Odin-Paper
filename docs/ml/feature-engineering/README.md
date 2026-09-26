# Feature Engineering — Phase 5

## Overview

This phase transforms preprocessed raw data into engineered feature matrices ready for model training. It is a separate step from preprocessing, ensuring clear separation of concerns.

## Quick Start

```bash
# Basic usage (17 derived features + cyclical encoding)
python BUDI-ML/training/scripts/feature_engineering.py

# With feature selection
python BUDI-ML/training/scripts/feature_engineering.py \
  --select-method mutual_info \
  --select-k 15

# With PCA dimensionality reduction
python BUDI-ML/training/scripts/feature_engineering.py \
  --pca-variance 0.95

# Full pipeline
python BUDI-ML/training/scripts/feature_engineering.py \
  --input BUDI-ML/training/datasets/processed/ \
  --output BUDI-ML/training/datasets/engineered/ \
  --encoding cyclical \
  --select-method mutual_info \
  --select-k 12 \
  --pca-variance 0.95 \
  --seed 42
```

## Pipeline

1. Load preprocessed data (`BUDI-ML/training/datasets/processed/`)
2. Compute 17 derived financial features
3. Impute missing values + cap outliers (fit on train only)
4. Cyclical encoding for temporal features (month)
5. Interaction features (income×volatility, obligation×volatility)
6. Drop redundant multi-collinear features
7. Feature selection (mutual information or ANOVA F-test)
8. PCA dimensionality reduction (optional)
9. Export to `BUDI-ML/training/datasets/engineered/`

## Key Files

| File | Purpose |
|------|---------|
| `BUDI-ML/training/scripts/feature_engineering.py` | Main pipeline |
| `feature-engineering.md` | Full documentation |

## Output

```
BUDI-ML/training/datasets/engineered/
├── train.parquet
├── val.parquet
├── test.parquet
├── feature_columns.json
├── pipeline_report.json
├── scalers.json (carried forward)
├── split_metadata.json (carried forward)
└── temporal_folds.json (carried forward)
```

## Pipeline Integration

```
BUDI-ML/training/datasets/processed/ (Phase 3 output)
    ↓ BUDI-ML/training/scripts/feature_engineering.py
BUDI-ML/training/datasets/engineered/
    ↓
Phase 4.5: Dimension & Threshold Discovery (precedes this phase conceptually)
    → Financial Trajectory and Financial Margin features defined here
    → Threshold candidates feed into class labeling
Phase 7: Model Training (pending)
```
