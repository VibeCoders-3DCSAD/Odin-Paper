# Test-Time Adaptation for Non-stationary Time Series: From Synthetic Regime Shifts to Financial Markets

## Metadata

```yaml
---
paper_id: "5f8c9e4a-3b2d-4e1f-8a7b-6c5d4e3f2a1b"
designation: algorithm-specific
title: "Test-Time Adaptation for Non-stationary Time Series: From Synthetic Regime Shifts to Financial Markets"
authors: "Wu, Y.; Deng, Q.; Chung, W.; Li, M."
year: 2026
venue: "Unknown"
odin_topics: ["5.B", "6.A", "6.B", "12.B"]
shorthand_tags: ["/concept-drift", "/forecast-algo-comparison", "/forecast-eval-metrics", "/eval-ml-design"]
member_checklist:
  - name: "Gabion, Stefanie S."
    status: "[ ]"
  - name: "Guevarra, Joaquin Luis T."
    status: "[X]"
  - name: "San Jose, Alexa Joanne Paula G."
    status: "[ ]"
  - name: "Togle, Charles Nathaniel B."
    status: "[ ]"
---
```

## TL;DR

Updating batch‑normalization statistics at test time is a safe default for financial forecasting, while updating affine parameters helps under smooth drift but can hurt on noisy real markets.

## Problem and Motivation

Time series in finance and other domains are non‑stationary, causing frozen forecasting models to degrade in accuracy after deployment. This matters because models trained on past data may fail under regime shifts like the COVID‑19 pandemic or high inflation. Prior test‑time adaptation (TTA) methods for time series lacked a systematic comparison of lightweight, causal updates across controlled and real shifts.

## Approach

- **TTA variants**: no adaptation (no_tta), refresh BN stats only (bn_stats), update only normalization affine parameters (norm_only) with entropy/consistency for classification or variance/EMA for regression.
- **Uncertainty fallback**: skip gradient updates when entropy or augmentation variance exceeds validation 80th percentile.
- **Drift penalty**: quadratic penalty on daily parameter changes to stabilize updates.
- **Backbones**: compact TCN (3 residual blocks, hidden 64) and Transformer (2–4 layers); GRU/LSTM references.
- **Data**: ETT benchmarks with synthetic shifts (gradual drift, noise bursts, structural switches); daily SPY, QQQ, EUR/USD (2020–2025, split into pandemic, inflation, recovery regimes).
- **Evaluation**: MAE/RMSE/R² for regression; accuracy/F1/AUC/ECE for classification; Diebold–Mariano tests; directional trading backtest with Newey–West t‑statistics.

## Findings

1. Under synthetic gradual drift on ETTh1, norm_only reduced MAE from 0.28 to 0.22 (R² improved from -0.31 to -0.02), but structural switches caused large errors (R² = -20.8) even with bn_stats.
2. On QQQ direction classification, bn_stats achieved **52.5% accuracy vs. 50.3% for no_tta** (DM p = 0.022), while norm_only dropped to 46.3%.
3. Diebold–Mariano tests: bn_stats significantly better than no_tta on SPY (DM = -2.78, p=0.005) and QQQ (DM = -2.29, p=0.022); norm_only significantly worse on both (p<0.001).
4. In backtests, bn_stats produced the highest Sharpe ratio on SPY (1.93 vs. 1.75 for no_tta) and QQQ (4.08 vs. 3.21 for no_tta); norm_only underperformed (Sharpe 1.54 and 1.35).

- Rolling metrics show TTA gains concentrated in pandemic and early recovery periods when distributional change is strongest.
- Uncertainty fallback mitigated harmful norm_only updates but did not fully prevent overfitting on noisy windows.

## Key Figures and Tables

- Table 2: Directional accuracy (2020–2025) → bn_stats best on QQQ (0.525) and EUR/USD (0.520); norm_only worst on QQQ (0.463).
- Figure 3: Rolling accuracy/RMSE with regime shading → bn_stats stable gains during pandemic/recovery on SPY; norm_only volatile.
- Table 3: Diebold–Mariano tests → bn_stats significantly better than no_tta on all three assets (p<0.05) except norm_only vs. no_tta on EUR/USD (p=0.91).
- Table 4 & 5: Backtest Sharpe ratios → bn_stats highest on both SPY (1.93) and QQQ (4.08); norm_only lowest.

## Key Equations

$$H(\hat{p}) = -p \log p - (1-p)\log(1-p)$$
*Entropy minimized to push predictions toward 0/1 under covariate shift.*

$$L_{cons} = \frac{1}{|B|}\sum_{X \in B} \|\hat{p}(X) - \hat{p}(T(X))\|_2^2$$
*Consistency penalizes sensitivity to weak, causality‑preserving transforms.*

$$L_{var} = \frac{1}{|B|}\sum_{X \in B} \mathrm{Var}\bigl(\{\hat{y}(T_k(X))\}_{k=1}^K\bigr)$$
*Variance reduction lowers local Lipschitz constant, helpful under noise bursts.*

$$L_{drift} = \gamma \|\theta^{(t)} - \theta^{(t-1)}\|_2^2$$
*Quadratic penalty limits inter‑day parameter motion, preventing overreaction.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| TTA | Test‑time adaptation – updating a small part of a model during deployment using unlabeled data. |
| BN | Batch normalization – layer that re‑centers and re‑scales activations. |
| norm_only | Updating only BN affine parameters (γ, β) at test time via gradient descent. |
| bn_stats | Refreshing BN running means/variances on current batch without gradients. |
| EMA | Exponential moving average – smooths model parameters over time for stable teacher targets. |
| DM test | Diebold–Mariano test – statistical comparison of two forecast accuracy series. |

## Critical Citations

- [Wang et al., 2021] – Foundational TTA via entropy minimization on BN affine parameters; inspired norm_only design.
- [Kim et al., 2022] – RevIN normalization; context for complementary TTA and backbone defenses.
- [Diebold & Mariano, 1995] – Standard test for predictive accuracy comparison used throughout evaluation.

## Relevance to Odin

**Topics:**

5.B — Profile Dynamics and the Cold‑Start Problem

6.A — Predictive Modeling in Personal Finance Systems

6.B — Spending Forecasting Algorithm

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This paper directly informs Odin’s spending forecasting module by demonstrating when lightweight test‑time adaptation (bn_stats vs. norm_only) improves forecast accuracy under distribution shifts – a core challenge as user spending patterns evolve. The finding that simple BN statistics refresh outperforms gradient‑based norm_only on noisy real‑world data (equity markets) provides a strong justification for using a conservative, zero‑gradient adaptation strategy in Odin’s forecasting pipeline, especially given manual transaction input which may produce irregular, noisy sequences. The paper’s use of Diebold–Mariano tests and Newey–West adjustments offers a template for evaluating Odin’s module‑level performance under non‑stationary user behavior.

**Directly justifies:**

- “Refreshing batch‑normalization statistics at test time (bn_stats) improves direction accuracy on QQQ from 50.3% to 52.5% (p = 0.022) without requiring gradient updates.”
- “Gradient‑based norm‑only adaptation can hurt performance on noisy financial series – on QQQ accuracy dropped to 46.3% despite drift control and uncertainty fallback.”
- “Quadratic drift penalty and uncertainty‑triggered fallback (80th percentile of entropy/augmentation variance) reduce harmful updates, but do not fully prevent overfitting on short windows.”
- “Diebold–Mariano tests with Newey–West HAC variance estimation provide statistically rigorous comparison of forecast losses under autocorrelated daily errors.”
- “Synthetic gradual drift (mean/variance shift) is well handled by norm‑only adaptation (MAE 0.22 vs. 0.28), suggesting value for slow concept drift in user spending patterns.”

**Limits of relevance:**

- Financial returns have different dynamics than personal spending sequences (e.g., lower signal‑to‑noise, heavy tails).
- The study uses daily prices; Odin’s transactions are irregular and user‑logged, not regularly spaced.
- No evaluation on cold‑start users – all models had historical training windows before deployment.
- Benchmark datasets (ETT, equity indices) are not from personal finance or Filipino context.

## Limitations

- All financial experiments use daily OHLCV only; no user‑level transaction data or personal budgets. [unacknowledged]
- Synthetic shifts on ETT are stylized and may not capture real spending pattern changes (e.g., payday cycles, unexpected expenses). [unacknowledged]
- Backtest strategy is a simple directional bet (long/neutral) ignoring transaction costs and slippage, so Sharpe ratios are upper bounds.
- Uncertainty threshold τ = 80th percentile was set on validation; optimal threshold may vary across users or regimes.
- Only one backbone size (TCN hidden 64) and fixed window length (L=96); sensitivity to input frequency (e.g., daily vs. weekly) not explored.

## Remember This

- 📌 **bn_stats beat norm_only** – BN refresh gained 2.2% accuracy on QQQ while norm_only lost 4.0%.
- 🔑 **DM test says bn_stats wins** – significant at p<0.05 on SPY, QQQ, and EUR/USD vs. no_tta.
- 💡 **Noisy markets need safe TTA** – norm_only overfits short windows even with drift penalty and fallback.
- ⚠️ **Smooth drift loves norm_only** – synthetic gradual shift improved MAE from 0.28 to 0.22 on ETTh1.
- 🔍 **Uncertainty fallback helps but doesn't fix** – high entropy/variance days skip gradient steps, yet harmful updates still occur.
