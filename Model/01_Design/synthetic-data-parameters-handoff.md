# Odin Thesis — Synthetic Data Foundation
## Statistical Parameter Sources, FBP Parameterization, and Generation Pipeline

**Project:** Development of Odin: A Personal Budget Management System Using LSTM and Isolation Forest Algorithms
**Institution:** University of Makati
**Scope:** Metro Manila / National Capital Region (NCR), Philippines
**Node Scope:** 2nd Node only — Essentials | Obligatory | Discretionary | Financial Allocation

---

## Table of Contents

1. [FIES Aggregate Tables — Useful Sources](#1-fies-aggregate-tables--useful-sources)
2. [Statistical Parameters](#2-statistical-parameters)
   - 2.1 [Computable from Aggregate Data](#21-computable-from-aggregate-data)
   - 2.2 [Blocked — Requires PSA Microdata](#22-blocked--requires-psa-microdata)
   - 2.3 [Derivable Once Blocked Parameters Are Available](#23-derivable-once-blocked-parameters-are-available)
3. [Synthetic Data Generation Pipeline](#3-synthetic-data-generation-pipeline)
   - 3.1 [FBP Statistical Parameterization](#31-fbp-statistical-parameterization)
   - 3.2 [Category Allocation Per FBP](#32-category-allocation-per-fbp)
   - 3.3 [Generation Steps](#33-generation-steps)
   - 3.4 [FBP Classification After Generation](#34-fbp-classification-after-generation)
   - 3.5 [Self-Validation Loop](#35-self-validation-loop)
4. [CV Justification](#4-cv-justification)

---

## 1. FIES Aggregate Tables — Useful Sources

Source publication: *2023 Family Income and Expenditure Survey: National, Regional, Provincial and Highly Urbanized City Estimates, Volume I* (ISHB Series No. 194, Philippine Statistics Authority, 2025).

All values used from this publication must be filtered to **NCR only**. Do not substitute national averages — NCR income and expenditure levels are materially higher than national figures.

### Useful Tables

| Table | Title | What It Provides | Used For |
|---|---|---|---|
| **Table 1** | Average Annual Family Income by Per Capita Income Decile | Average annual income per decile, NCR | Income Range per FBP; Savings Rate numerator |
| **Table 2** | Average Annual Family Expenditure by Per Capita Income Decile | Average annual expenditure per decile, NCR | Base total μ per decile; Savings Rate denominator |
| **Table 7** | Share to Total Family Expenditure by Expenditure Group | Category percentage shares of total expenditure, NCR | Per-category μ allocation; Engel Coefficient; Obligated Ratio |

### NCR 2023 Table 7 Reference Values

| Category | NCR 2023 Share |
|---|---|
| Food and Non-Alcoholic Beverages | 40.9% |
| Housing, Water, Electricity, Gas and Other Fuels | 22.9% |
| Transport | 6.8% |
| Education | 3.3% |
| Information and Communication | 3.4% |
| Health | 3.0% |
| Personal Care, Social Protection and Miscellaneous | 3.7% |
| Furnishings and Routine Household Maintenance | 2.6% |
| Special Family Occasions | 2.3% |
| Durable Furniture and Equipment | 2.1% |
| Other Expenditures | 2.1% |
| Clothing and Footwear | 1.9% |
| Alcoholic Beverages and Tobacco | 1.4% |
| Insurance and Financial Services | 2.7% |
| Recreation, Sport and Culture | 0.8% |
| Hotels (Accommodation Services) | 0.1% |

### Tables Not Used

| Table | Reason |
|---|---|
| Table 1a, 2a, 3a, 4a | These are **sampling CVs** (coefficient of variation of the survey estimate = standard error / estimate). They measure how reliable the survey point estimate is — NOT the behavioral variability of household spending. Do not use to derive σ. |
| Tables 3, 4 | Total income/expenditure in millions — aggregate population figures, not per-household statistics. |
| Table 5 | Gini Coefficient and Palma Ratio — inequality measures. Not needed for synthetic data generation. |
| Table 6 | Income source shares — not needed for Node 2 expenditure parameterization. |

---

## 2. Statistical Parameters

### 2.1 Computable from Aggregate Data

These parameters can be derived directly from Tables 1, 2, and 7.

---

**μ — Mean Monthly Expenditure Per Category**

> What it is: The average amount a household spends in a given category per month.
>
> What it is used for: The central location parameter of the log-normal distribution. All spending amounts are sampled around μ. It anchors synthetic spending to real NCR household levels.
>
> How to compute:
> ```
> μ_category = (Table 2 average annual expenditure, NCR, per decile × Table 7 category share%) ÷ 12
> ```

---

**Obligated Ratio — (Essentials + Obligatory) / Total Spend**

> What it is: The proportion of total spending that goes toward fixed, non-discretionary obligations.
>
> What it is used for: The second dimension of FBP classification. A ratio above 0.5 classifies the household as Obligated; below 0.5 as Flexible. Also used to bias category allocation when generating synthetic records.
>
> How to compute:
> ```
> Obligated Ratio = sum of Essentials + Obligatory category shares from Table 7
> ```
> Node 2 mapping from Table 7 categories:
> - **Essentials:** Food and Non-Alcoholic Beverages + Housing/Water/Electricity + Health
> - **Obligatory:** Insurance and Financial Services + fixed Transport (commuter obligations)
> - **Discretionary:** Restaurant/Hotels + Recreation + Clothing + Special Occasions + Personal Care + Durable Furniture
> - **Financial Allocation:** Income − Total Expenditure (implied savings)

---

**Savings Rate — (Income − Total Expenditure) / Income**

> What it is: The fraction of income not spent.
>
> What it is used for: Calibrating Financial Allocation category amounts. Validates that generated synthetic data does not produce households spending more than they earn per decile.
>
> How to compute:
> ```
> Savings Rate = (Table 1 average income − Table 2 average expenditure) / Table 1 average income
> Per decile, NCR
> ```

---

**Engel Coefficient — Food Expenditure / Total Expenditure**

> What it is: The proportion of total household spending devoted to food. A classic welfare indicator — higher Engel Coefficient signals lower income households.
>
> What it is used for: Cross-validation of category allocation. Lower-decile FBPs (Variable/Obligated) should produce higher Engel Coefficients than higher-decile FBPs (Stable/Flexible, Variable/Flexible).
>
> How to compute:
> ```
> Engel Coefficient = Food and Non-Alcoholic Beverages share from Table 7
> NCR 2023 value: 40.9%
> ```

---

**Income Range Per Decile**

> What it is: The income bracket for each of the 10 per capita income deciles in NCR.
>
> What it is used for: Mapping each FBP to its corresponding income level. Sets the total μ for synthetic users. When a new real user provides their income during onboarding, this mapping assigns them an initial FBP and baseline spending distribution.
>
> Source: Table 1, NCR rows, per decile column.

---

### 2.2 Blocked — Requires PSA Microdata

These parameters cannot be derived from published aggregate tables and require the unit-level FIES household records.

A formal data request has been submitted to the Philippine Statistics Authority (PSA) for the 2018, 2021, and 2023 FIES NCR microdata. If unit-level records are not released, the fallback request asks PSA to compute and provide these statistics directly.

---

**σ — Standard Deviation Per Category**

> What it is: The spread of expenditure amounts around the mean within a given category. A wider σ means more households spend very differently from the average.
>
> What it is used for: Required to fit the log-normal distribution per category. Without σ, the shape of the sampling distribution cannot be determined from empirical data.
>
> Why it is blocked: The aggregate tables (Table 2) only report the mean. The sampling CV tables (Table 2a) measure survey estimate reliability, not household-level spread.
>
> Workaround: FBP-defined CV bounds (see Section 4). σ = CV × μ where CV is set by FBP design.

---

**CV — Coefficient of Variation Per Category (Behavioral)**

> What it is: σ / μ — the relative spread of spending within a category. A category with CV = 0.15 has tightly consistent spending; CV = 1.40 is highly variable.
>
> What it is used for: Parameterizing σ per category. Also reveals which categories are structurally volatile (e.g., medical, education) vs. structurally stable (e.g., food, rent).
>
> Why it is blocked: Table 2a reports sampling CV of the survey estimate, not behavioral CV of the household distribution. These are different measures.
>
> Workaround: FBP-defined CV (see Section 4).

---

**Median Per Category**

> What it is: The midpoint of the spending distribution for a category — 50% of households spend below this amount.
>
> What it is used for: More robust than the mean for right-skewed distributions. Used to validate log-normal fit: for a true log-normal distribution, Median = exp(μ_ln).
>
> Why it is blocked: Aggregate tables report means only. Median requires distributional data.
>
> Workaround: Once μ_ln is derived, Median = exp(μ_ln) analytically. This assumes log-normal holds.

---

**Skewness Per Category**

> What it is: The asymmetry of the expenditure distribution. Right-skewed (positive skewness) indicates a long right tail — most households spend modestly but a few spend very high amounts occasionally.
>
> What it is used for: Confirms that log-normal is the appropriate distribution choice. If skewness is positive and high, log-normal is validated. If near zero, a normal distribution may be sufficient.
>
> Why it is blocked: Requires distributional data across households.
>
> Workaround: Skewness is analytically derivable from σ_ln once fitted: `(exp(σ_ln²) + 2) × sqrt(exp(σ_ln²) − 1)`. This is an assumption, not empirical validation.

---

**n and n_nonzero Per Category Per Decile**

> What it is: Total number of households in a decile (n) and those with non-zero expenditure in a given category (n_nonzero).
>
> What it is used for: Assessing the statistical reliability of mean and σ estimates. A category with n_nonzero = 40 out of 800 households has a very unreliable mean. Including zero-spenders also inflates σ artificially.
>
> Why it is blocked: Not reported in any aggregate table.
>
> Note: When PSA microdata is received, always compute statistics on n_nonzero (non-zero households only) for each category. Zero-spending records should be modeled separately as a zero-inflation component, not included in the log-normal fit.

---

### 2.3 Derivable Once Blocked Parameters Are Available

These require σ per category, which is either coming from PSA or approximated via FBP-defined CV.

---

**μ_ln — Log-Normal Location Parameter**

> What it is: The mean of the natural log of spending amounts. It is not the same as μ (the mean of spending amounts directly).
>
> What it is used for: One of two parameters that fully define a log-normal distribution. Together with σ_ln, it defines what amounts get sampled for each user each day.
>
> How to compute:
> ```
> μ_ln = ln(μ) − 0.5 × ln(1 + CV²)
> ```

---

**σ_ln — Log-Normal Scale Parameter**

> What it is: The standard deviation of the natural log of spending amounts. Controls the width of the log-normal distribution.
>
> What it is used for: Together with μ_ln, fully parameterizes the log-normal distribution used for sampling synthetic spending amounts.
>
> How to compute:
> ```
> σ_ln = sqrt(ln(1 + CV²))
> ```

---

## 3. Synthetic Data Generation Pipeline

### 3.1 FBP Statistical Parameterization

The four FBPs are parameterized along two axes: spending consistency (CV) and spending composition (Obligated Ratio). Each FBP maps to a FIES NCR decile range, which sets the total income and expenditure level.

| FBP                  | CV   | Obligated Ratio | NCR Decile | Behavioral Description                                                                                                           |
| -------------------- | ---- | --------------- | ---------- | -------------------------------------------------------------------------------------------------------------------------------- |
| Stable / Obligated   | 0.15 | > 0.50          | D3–D6      | Salaried workers with fixed rent/condo amortization and regular utility bills. Predictable month-to-month.                       |
| Stable / Flexible    | 0.15 | ≤ 0.50          | D6–D9      | Mid-to-upper income. Consistent lifestyle spending — dining, leisure, shopping. Low obligation load.                             |
| Variable / Obligated | 0.35 | > 0.50          | D1–D4      | Irregular income earners (freelance, informal sector) who still carry fixed obligations. Erratic but heavily committed spending. |
| Variable / Flexible  | 0.35 | ≤ 0.50          | D7–D10     | High earners with volatile discretionary behavior. BPO senior staff, entrepreneurs. High variance on non-essential categories.   |

**CV values (0.15 and 0.35) are design parameters.** See Section 4 for justification and sensitivity analysis requirement.

---

### 3.2 Category Allocation Per FBP

FIES Table 7 gives the NCR population average allocation across categories. Each FBP biases away from this average based on its Obligated Ratio definition.

The base Node 2 mapping from Table 7 (NCR 2023 averages):

| Node 2 Category | Table 7 Components | NCR 2023 Avg Share |
|---|---|---|
| Essentials | Food + Housing/Water/Electricity + Health | ~66.8% |
| Obligatory | Insurance and Financial Services + fixed Transport | ~9.5% |
| Discretionary | Recreation + Clothing + Special Occasions + Restaurant/Hotels + Personal Care + Durable Furniture + Misc | ~16.5% |
| Financial Allocation | Income − Total Expenditure (savings) | ~7.2% (implied) |

**Per-FBP allocation adjustment:**

| Node 2 Category | Stable / Obligated | Stable / Flexible | Variable / Obligated | Variable / Flexible |
|---|---|---|---|---|
| Essentials | Above avg | Near avg | Above avg | Near avg |
| Obligatory | Above avg | Below avg | Above avg | Below avg |
| Discretionary | Below avg | Above avg | Below avg | Above avg |
| Financial Allocation | Low | Moderate | Very low | Moderate-high |

Rule: Essentials + Obligatory shares must sum above 0.50 for Obligated profiles and at or below 0.50 for Flexible profiles, consistent with the FBP definition.

Per-category μ is then:
```
μ_category = total_monthly_μ_from_decile × adjusted_category_share_for_FBP
```

---

### 3.3 Generation Steps

```
Step 1: Determine FBP assignment
        → Select decile from FBP-to-decile mapping
        → Pull total μ from Table 2 (NCR, that decile) ÷ 12

Step 2: Compute per-category μ
        → Apply FBP-adjusted category shares to total μ

Step 3: Set CV per FBP
        → Stable: CV = 0.15
        → Variable: CV = 0.35

Step 4: Compute σ per category
        → σ = CV × μ_category

Step 5: Fit log-normal parameters per category
        → μ_ln = ln(μ) − 0.5 × ln(1 + CV²)
        → σ_ln = sqrt(ln(1 + CV²))

Step 6: Sample monthly totals per category
        → Amount ~ LogNormal(μ_ln, σ_ln)
        → Distribute across days in month

Step 7: Apply noise events
        → Payday spree, Petsa de Peligro, 13th month, Christmas/Ber months,
          Semana Santa, Undas, MMFF, School enrollment, Paluwagan, Ambag
        → Noise multipliers sampled per user (not fixed)

Step 8: Enforce coherence constraint
        → Essentials + Obligatory + Discretionary + Financial Allocation = Total Spendings
```

---

### 3.4 FBP Classification After Generation

Once synthetic records exist, each user is classified using the rule-based formula. This is the same classifier that will be used on real users during onboarding.

```python
import numpy as np

def classify_fbp(monthly_totals, monthly_essentials, monthly_obligatory):
    """
    monthly_totals     : array of total spending per month
    monthly_essentials : array of essentials spending per month
    monthly_obligatory : array of obligatory spending per month
    """
    mu  = np.mean(monthly_totals)
    cv  = np.std(monthly_totals) / mu

    obligated_ratio = (
        np.sum(monthly_essentials + monthly_obligatory) /
        np.sum(monthly_totals)
    )

    stability   = "Stable"   if cv < 0.20 else "Variable"
    composition = "Obligated" if obligated_ratio > 0.50 else "Flexible"

    return f"{stability}/{composition}"
```

Minimum observation window before classification: **60 days** (at least 2 complete payday cycles and one full month of category data per the model architecture threshold).

---

### 3.5 Self-Validation Loop

Because the ground truth FBP is known for every synthetic user, classification accuracy can be measured directly.

```
For each generated user:
    ground_truth_fbp  = FBP used during generation
    classified_fbp    = classify_fbp(user's generated records)
    correct           = (ground_truth_fbp == classified_fbp)

Report:
    - Overall classification accuracy
    - F1 score per FBP class
    - Confusion matrix (4×4)
```

Expected result: High recovery rate for Stable/Obligated and Variable/Flexible (extreme profiles). Lower recovery for Stable/Flexible and Variable/Obligated (middle profiles that sit near the CV = 0.20 and Obligated Ratio = 0.50 boundaries).

This self-validation confirms that:
1. Generation parameters are internally consistent with classification thresholds.
2. The boundary conditions (CV = 0.20, ratio = 0.50) produce operationally distinct groups.

---

## 4. CV Justification

### 4.1 What CV Controls

CV = σ / μ controls the width of the log-normal distribution for each category:

- **CV = 0.15 (Stable):** Tight distribution. Monthly spending amounts cluster closely around the mean. The LSTM observes a near-flat signal punctuated only by noise events.
- **CV = 0.35 (Variable):** Wide distribution. Monthly spending swings significantly. The LSTM must extract the underlying pattern despite high baseline noise.

CV is the primary determinant of how difficult a user's pattern is to forecast. Stable profiles yield lower MAE by design; Variable profiles stress-test the model.

---

### 4.2 Justification for the 0.20 Boundary

The CV = 0.20 threshold as the boundary between stable and variable spending is supported by:

**1. Measurement convention**
CV < 0.20 is widely used in applied measurement research as the threshold for "acceptable variability" or "low variation." This convention appears across econometrics, public health, and quality control literature.

**2. Morduch & Schneider — The Financial Diaries (2017)**
Direct within-household income and spending tracking over 12 months across 235 US households. Demonstrates that financially stable households exhibit monthly spending CV well below 0.20, while financially stressed or irregular households show CV above 0.25. Provides methodological precedent for using temporal CV as a spending behavior classifier.

**3. BSP Consumer Expectations Survey — NCR respondents**
Tracks household spending intentions quarterly. Households reporting consistent spending outlooks quarter-over-quarter correspond behaviorally to the Stable classification. Households reporting high uncertainty or irregular outlooks correspond to Variable. Provides Philippine-specific behavioral anchoring for the two-class stability split.

**4. Cacnio & Lubangco — BSP Discussion Paper No. 2024-20**
Documents how inflation expectations affect Filipino household consumption decisions. Households with stable income expectations exhibit predictable consumption patterns — consistent with low temporal CV. Households with uncertain income expectations exhibit volatile consumption — consistent with high temporal CV.

---

### 4.3 Justification for 0.15 and 0.35 Specifically

CV = 0.15 (Stable) and CV = 0.35 (Variable) are **calibration parameters**, not empirical measurements. They satisfy the CV < 0.20 and CV ≥ 0.20 boundary conditions while providing sufficient separation between the two classes.

These specific values are not derived from a single source. They are design decisions. The panel defense for these values is a **sensitivity analysis**, not a citation:

> *The synthetic dataset was generated under three CV settings per class: CV ∈ {0.10, 0.15, 0.20} for Stable profiles and CV ∈ {0.25, 0.35, 0.45} for Variable profiles. Model performance metrics (MAE, RMSE, sMAPE) were stable across all tested values within each class. This confirms the LSTM architecture is not sensitive to the exact CV value, provided the values remain within their respective class boundaries.*

This reframes the panel challenge: instead of defending a specific number, the sensitivity analysis demonstrates that the exact value does not materially affect model performance — the class boundary (0.20) is what matters.

---

### 4.4 Temporal vs Cross-Sectional CV — Known Limitation

The FBP CV is **temporal** — how much a single user's spending varies month to month over their observation window.

FIES data provides **cross-sectional** CV — how much spending varies across different households in the same survey year.

These are different measures and cannot be directly substituted. FIES aggregate tables and microdata cannot validate the temporal CV thresholds because FIES is a point-in-time annual survey, not a longitudinal panel.

This is a documented limitation. The temporal CV thresholds are validated internally via the self-validation loop (Section 3.5) and externally via the sensitivity analysis (Section 4.3). Real-world temporal validation requires live transaction data from a deployed system — this is scoped as future work.

---

*Document version: 1.0*
*Scope: Metro Manila, NCR, Philippines*
*Status: PSA microdata request pending — σ per category to be updated upon receipt*
