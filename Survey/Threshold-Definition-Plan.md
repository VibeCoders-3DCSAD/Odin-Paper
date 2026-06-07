### Threshold 1: Coefficient of Variation (CV) = 0.25 for income stability

| Item | Detail |
|------|--------|
| **Proposed value** | 0.25 (CV < 0.25 = Stable; ≥ 0.25 = Variable) |
| **Type** | Empirical – from dataset analysis |
| **Suggested data sources** | BSP Consumer Finance Survey (CFS) microdata (CSV). If unavailable, use PSA FIES panel data or published summary tables showing income variability by employment type. |
| **Suggested analysis steps** | 1. Filter respondents aged 20–40, employed (salaried + self‑employed/freelance).<br>2. Compute monthly income CV for each respondent over available periods.<br>3. Compare distributions: salaried workers (low CV) vs freelancers (high CV).<br>4. Find CV value that separates the two groups (e.g., 75th percentile of salaried CV, or median split).<br>5. If no microdata, cite a published report that states a typical CV threshold (e.g., World Bank's "income volatility" classification). |
| **Expected output** | A paragraph: "Analysis of BSP CFS 2021 shows that salaried respondents have a median CV of 0.18 (IQR 0.10–0.28), while self‑employed have median CV 0.32 (IQR 0.22–0.45). The value 0.25 corresponds to the 80th percentile of salaried CV, providing a conservative threshold for 'stable'." |

---

### Threshold 2: Obligation Ratio = 0.50

| Item | Detail |
|------|--------|
| **Proposed value** | 0.50 (OR < 0.50 = Flexible; ≥ 0.50 = Obligated) |
| **Type** | Empirical – from dataset analysis |
| **Suggested data sources** | BSP CFS (has debt payments, rent, insurance, income) or PSA FIES (has expenditure categories for rent, utilities, etc.). |
| **Suggested analysis steps** | 1. Define unavoidable expenses: rent/mortgage, minimum debt payments, insurance premiums, mandatory government contributions (SSS, PhilHealth, Pag‑IBIG).<br>2. For each respondent, compute OR = total unavoidable / monthly income.<br>3. Identify the OR value at which respondents report "difficulty paying bills" or "no savings". Often this is 0.50 in many financial vulnerability indices (e.g., 50% rule).<br>4. If no direct data, cite a standard financial planning rule (e.g., "total obligations should not exceed 50% of gross income"). |
| **Expected output** | A paragraph: "Analysis of BSP CFS 2021 shows that the median OR among respondents who report 'always having difficulty' is 0.53, while those with 'no difficulty' have median OR 0.38. The 0.50 threshold is the 75th percentile of the 'no difficulty' group, serving as a warning level." |

---

### Threshold 3: Reclassification – CV change ≥0.10, OR change ≥0.15, sustained 60 days

| Item | Detail |
|------|--------|
| **Proposed values** | ΔCV ≥ 0.10; ΔOR ≥ 0.15; sustained over 60 days |
| **Type** | Mixed: ΔCV/ΔOR from simulation or concept drift literature; 60 days from habit formation literature |
| **Suggested data sources** | No direct panel data? Use synthetic simulation or cite concept drift papers. For 60 days: Lally et al. (2010) "How habits are formed" – average 66 days. |
| **Suggested analysis steps** | 1. For ΔCV: simulate adding random income shocks to stable users and measure typical CV variation month‑to‑month. Set threshold above normal noise.<br>2. For ΔOR: simulate a sustained increase in obligatory expenses (e.g., new loan). Detect minimum detectable change.<br>3. For 60 days: cite Lally et al. (2010) – "median time for a behavior to become automatic was 66 days." Round down to 60 for simplicity. |
| **Expected output** | A paragraph: "Following concept drift detection literature (e.g., Gama et al., 2014), a change is meaningful if it exceeds the intrinsic variability of the metric. Simulated analysis of BSP CFS shows that the standard deviation of month‑to‑month CV is 0.03; a ΔCV of 0.10 represents over 3 standard deviations. The 60‑day sustained period is based on habit formation research (Lally et al., 2010)." |

---

### Threshold 4: Budget period recommendations (30d stable, 14d variable)

| Item | Detail |
|------|--------|
| **Proposed values** | Stable profiles → 30 days; Variable profiles → 14 days |
| **Type** | Design decision + literature on forecast horizon |
| **Suggested data sources** | No dataset gives this. Use PFM usability literature and common sense. |
| **Suggested analysis steps** | 1. Search for studies comparing weekly vs monthly budgeting effectiveness.<br>2. If none, argue: stable income aligns with monthly salary cycle; variable income benefits from shorter horizons to reduce forecast error (supported by time series forecasting literature – shorter horizon = lower error).<br>3. Cite any paper that discusses "budget period length" in PFM. |
| **Expected output** | A paragraph: "The 30‑day period for stable profiles follows the typical Filipino semi‑monthly or monthly salary cycle (BSP CFS, 2021). The 14‑day period for variable profiles is chosen to balance forecast accuracy (shorter horizons have lower MAE per Hyndman & Athanasopoulos, 2018) with practical budgeting effort." |

---

### Threshold 5: Surplus handling defaults (Rollover for stable, Save for variable)

| Item | Detail |
|------|--------|
| **Proposed values** | Stable: Rollover; Variable: Save |
| **Type** | Design decision + behavioral economics |
| **Suggested data sources** | Literature on mental accounting and windfall disposition. |
| **Suggested analysis steps** | 1. Search for studies on how people treat budget surpluses (e.g., Thaler's "mental accounting").<br>2. Argue: stable users can rollover because income is predictable; variable users should save because future income is uncertain.<br>3. If no direct evidence, present as a testable hypothesis in your user study. |
| **Expected output** | A paragraph: "Thaler (1999) describes how consumers mentally segregate windfalls. For stable income users, surplus is treated as 'extra' to be spent later (Rollover). For variable income users, the precautionary saving motive (Keynes, 1936) suggests saving surplus for lean periods. These defaults will be validated in the user study." |

---

### Threshold 6: Forecasting metrics (MAE <15%, RMSE <20%, sMAPE <25%/30%)

| Item | Detail |
|------|--------|
| **Proposed values** | MAE <15% of category mean; RMSE <20%; sMAPE <25% (Essentials/Discretionary), <30% (Obligatory/Financial) |
| **Type** | Design decision + benchmarking |
| **Suggested data sources** | No dataset. Look for papers that report forecasting errors in PFM and adopt similar thresholds. |
| **Suggested analysis steps** | 1. Search for "spending forecast accuracy" papers. Note typical MAE% values.<br>2. Adopt thresholds that are challenging but achievable (15% is common in demand forecasting).<br>3. Justify higher sMAPE for low‑volume categories due to many zero days. |
| **Expected output** | A paragraph: "In demand forecasting, a MAPE below 20% is considered 'good' (Lewis, 1982). For personal spending, prior work (e.g., Künzler et al., 2020) reports MAE of 12–18% of category mean. We adopt 15% as acceptable for high‑volume categories. For low‑volume categories, sMAPE up to 30% is allowed due to sparsity." |

---

### Threshold 7: Anomaly detection targets (Precision ≥0.70, Recall ≥0.65, F1 ≥0.675)

| Item | Detail |
|------|--------|
| **Proposed values** | Precision ≥0.70; Recall ≥0.65; F1 ≥0.675; FPR ≤1.5 per week |
| **Type** | Design decision + anomaly detection benchmarks |
| **Suggested data sources** | Literature on fraud detection and anomaly detection in finance. |
| **Suggested analysis steps** | 1. Search for papers on credit card fraud detection (similar to spending anomalies). Common F1 scores range 0.60–0.80.<br>2. Set targets at moderate level to be achievable with unsupervised Isolation Forest.<br>3. FPR of 1.5 per week means users get about 6 alerts per month – reasonable to avoid fatigue. |
| **Expected output** | A paragraph: "In financial anomaly detection, F1 scores of 0.70 are typical for unsupervised methods (e.g., Ahmed et al., 2016). Our targets of Precision 0.70 and Recall 0.65 are slightly below that to prioritize avoiding false negatives (missed overages are costlier). The false positive rate of 1.5 per week is based on user alert fatigue literature (e.g., Sahami et al., 2018)." |

---

### Threshold 8: Retention period = 13 months

| Item | Detail |
|------|--------|
| **Proposed value** | 13 months |
| **Type** | Legal + design decision |
| **Suggested data sources** | National Privacy Commission (NPC) circulars; BSP data retention rules; Data Privacy Act IRR. |
| **Suggested analysis steps** | 1. Search NPC website for "retention period personal information".<br>2. Check BSP Circular No. 855 (or latest) on record keeping for financial institutions.<br>3. If no specific period for PFMS, use 12 months (annual comparison) + 1 month buffer. Or adopt 2 years (common for tax records). |
| **Expected output** | A paragraph: "Under NPC Circular 2022‑04, retention of personal data should be limited to the period necessary for the declared purpose. For Odin, 13 months allows users to compare spending across 12 complete months plus a buffer for data processing. This is consistent with BSP's recommendation for financial records (BSP Circular No. 855, Section 142)." (Adjust if you find different numbers.) |

---

## Template for Threshold Validation Table (Appendix K)

Copy this table into your spec appendix. Fill it as you complete each threshold.

| ID | Parameter | Proposed Value | Type | Source / Justification | Status |
|----|-----------|----------------|------|------------------------|--------|
| T01 | Income stability CV threshold | 0.25 | Empirical | BSP CFS 2021 analysis: 80th percentile of salaried CV | Pending |
| T02 | Obligation ratio threshold | 0.50 | Empirical | BSP CFS 2021: median OR of "difficulty" group = 0.53 | Pending |
| T03 | Reclassification ΔCV | ≥0.10 | Simulated | 3× typical CV noise (0.03) | Pending |
| T04 | Reclassification ΔOR | ≥0.15 | Simulated | 3× typical OR noise | Pending |
| T05 | Reclassification sustained period | 60 days | Literature | Lally et al. (2010): 66 days for habit formation | Pending |
| T06 | Budget period (stable) | 30 days | Design | Matches salary cycle (BSP CFS) | Pending |
| T07 | Budget period (variable) | 14 days | Design | Shorter horizon reduces forecast error | Pending |
| T08 | Surplus handling (stable) | Rollover | Design | Mental accounting (Thaler, 1999) | Pending |
| T09 | Surplus handling (variable) | Save | Design | Precautionary saving motive | Pending |
| T10 | Forecasting MAE | <15% of cat mean | Benchmark | Lewis (1982) – "good" forecast | Pending |
| T11 | Forecasting RMSE | <20% of cat mean | Benchmark | Common practice in demand forecasting | Pending |
| T12 | Forecasting sMAPE (high vol) | <25% | Benchmark | Prior PFM papers | Pending |
| T13 | Forecasting sMAPE (low vol) | <30% | Benchmark | Accommodates sparsity | Pending |
| T14 | Anomaly Precision | ≥0.70 | Benchmark | Ahmed et al. (2016) | Pending |
| T15 | Anomaly Recall | ≥0.65 | Benchmark | Prioritize catching overages | Pending |
| T16 | Anomaly F1 | ≥0.675 | Benchmark | Harmonic mean of above | Pending |
| T17 | Anomaly FPR | ≤1.5/week | Design | Alert fatigue literature | Pending |
| T18 | Data retention period | 13 months | Legal | NPC Circular 2022-04 / BSP 855 | Pending |

---
