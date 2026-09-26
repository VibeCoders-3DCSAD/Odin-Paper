# Accountant Validation Evidence Review

**Document version:** 1.0  
**Status:** Literature-informed review — pending accountant consultation and empirical calibration  
**Scope:** Metro Manila/NCR household and personal-finance synthetic data  
**Related document:** `synthetic-injection-rules.md`

> **Validation limitation**
>
> This document is a research-informed methodological review, not an accountant’s signed approval. The underlying FIES extract, BSP tables, and implementation files have not been independently inspected. Reported source statistics must be reproduced or verified before being marked validated.
>
> International research cited here supports mechanisms and methods. It does not automatically establish numerical estimates for NCR households.

---

## 1. Executive Summary

The proposed rules can support an experimental synthetic-data generator, but several parameters should not yet be described as empirically calibrated NCR behavior.

### Supported design principles

- Income stability and spending variability should be measured separately.
- Spending can respond to income receipt timing.
- Emergency runway should use accessible liquid reserves, not annual income minus expenditure alone.
- Employment arrangements, household composition, and dependents affect financial behavior.
- Anomalies should be assessed against user-specific behavior and transaction context.
- Train/test splits must prevent user, donor-household, and future-information leakage.

### Parameters not established by the cited evidence

- Income CV threshold of `0.50`.
- Obligation-ratio threshold of `0.60`.
- Occupation-specific zero-income probabilities of `15%` or `50%`.
- Payday spending multiplier of `2.1×`.
- December spending multiplier of `2.2×`.
- Overall personal-finance anomaly prevalence of `3%`.
- Proposed anomaly-type mixture of `30/20/20/15/15`.

These may remain experimental parameters if clearly labeled as assumptions.

### Defensible numerical reference

A reserve of **three to six months of living expenses** is common financial-planning guidance.[7]

However:

- It is a planning recommendation, not an estimate of actual household behavior.
- Three months is not independently established as the optimal NCR classification boundary.
- Variable-income households may require a larger planning buffer.
- Financial risk tolerance is not the same construct as liquidity capacity.

---

## 2. Evidence and Decision Framework

### 2.1 Evidence classes

| Evidence class | Meaning |
|---|---|
| Statutory rule | Supported by an applicable law or administrative rule. |
| Planning benchmark | Recommended financial practice, not observed population behavior. |
| Empirical estimate | Estimated from a defined dataset and population. |
| Construct definition | A chosen definition of what a metric measures. |
| Engineering choice | A modeling or implementation decision. |
| Simulation assumption | A hypothetical parameter used to generate scenarios. |
| Pending verification | Requires source-table, data, or expert confirmation. |

### 2.2 Consultation statuses

| Status | Meaning |
|---|---|
| Pending | No accountant decision recorded. |
| Approved | Accountant supports the proposed operational rule. |
| Revise | Accountant recommends changing the rule. |
| Out of scope | Requires additional behavioral, labor, payments, or transaction-data expertise. |

> The dispositions below are review recommendations. They must not be entered as completed accountant decisions without consultation.

---

## 3. Parameter Validation Summary

| Parameter | Evidence assessment | Recommended treatment |
|---|---|---|
| Income CV `0.50` | Not established as a universal stability boundary. | Retain only as a provisional classification convention. |
| Obligation ratio `0.60` | Not an established accounting standard for the stated denominator. | Clarify the construct and empirically calibrate. |
| Emergency runway `3 months` | Consistent with the lower end of common planning guidance.[7] | Planning benchmark, not descriptive prevalence. |
| Freelancer receipts `2.5/month` | Not established across freelance occupations. | Calibrate by payment arrangement. |
| Zero-income probability `15%` | Not verified for the listed occupations. | Estimate separately and distinguish missing data from true gaps. |
| Project-worker gap probability `50%` | Not established as a general estimate. | Model contracts, milestones, and gap durations. |
| Payday multiplier `2.1×` | Payday responsiveness is supported; this magnitude is not.[3–5] | Scenario parameter pending local calibration. |
| December multiplier `2.2×` | Not established as an NCR household estimate. | Apply only as a documented scenario assumption. |
| Anomaly prevalence `3%` | No universal personal-finance anomaly rate.[11] | Experimental injection setting. |
| Transactions at `2–5 AM` | Not universally anomalous. | Use personal and channel-specific timing baselines. |
| Private-sector 13th-month pay | Statutory basis exists.[9] | Correct legal citation and benefit calculation. |

---

## 4. Numerical and Accounting Corrections

### 4.1 Output labels and class balance

Each user or observation window should receive:

- One eight-class PFP label.
- Optionally, three separate binary dimension labels.

The current 12-archetype design produces:

- Four PFP classes with 2,000 users each.
- Four PFP classes with 1,000 users each.

Therefore, the dataset is balanced by archetype, not by PFP class.

### 4.2 Zero-income rate reconciliation

If four of twelve equally represented archetypes have a 15% monthly probability of zero income:

\[
P(\text{zero income from these groups})
=
\frac{4}{12}\times0.15
=
0.05
\]

This contributes **5% of user-months**, not 15.4%, assuming no other zero-income mechanisms.

For a Poisson receipt count:

\[
N\sim Poisson(2.5)
\]

\[
P(N=0)=e^{-2.5}\approx8.21\%
\]

If a separate 15% gap probability is applied before that receipt-count process:

\[
P(\text{zero receipts})
=
0.15+0.85e^{-2.5}
\approx21.98\%
\]

This is the affected group’s zero-receipt probability.

**Required actions:**

1. Define whether gaps come from an explicit income state or receipt-count sampling.
2. Avoid unintentionally applying both mechanisms.
3. Reconcile the occupation names in Section 4.1.1 with archetypes A–L.
4. State whether the denominator is users, user-months, or transaction rows.

### 4.3 Correct lognormal parameterization

For target arithmetic mean \(m\) and target CV \(c\):

\[
\sigma_{\ln}
=
\sqrt{\ln(1+c^2)}
\]

\[
\mu_{\ln}
=
\ln(m)-\frac{\sigma_{\ln}^2}{2}
\]

```python
sigma_ln = np.sqrt(np.log1p(target_cv**2))
mu_ln = np.log(target_mean) - 0.5 * sigma_ln**2

monthly_income = rng.lognormal(
    mean=mu_ln,
    sigma=sigma_ln,
    size=12,
)
```

NumPy uses `mean` and `sigma`, not `mu_ln` and `sigma_ln`.

For a target CV of `0.70`:

- Correct log-space sigma: approximately `0.6316`.
- Using log-space sigma `0.70` produces population CV approximately `0.7952`.

These formulas describe the generating distribution. A 12-month realization will not exactly match the target.

Recompute realized CV after clipping, bonuses, income gaps, and calendar allocation.

### 4.4 Hard monthly clipping conflicts with target CVs

For positive monthly income bounded by \(a\) and \(b\), the population-style CV satisfies:

\[
CV\leq\frac{b-a}{2\sqrt{ab}}
\]

| Archetype | Monthly bounds | Maximum possible CV under those bounds | Target CV |
|---|---:|---:|---:|
| E | ₱25,000–₱60,000 | Approximately `0.452` | `0.70` |
| F | ₱18,000–₱40,000 | Approximately `0.410` | `0.65` |
| H | ₱8,000–₱20,000 | Approximately `0.474` | `0.80` |

The listed ranges cannot simultaneously constrain every month and produce the target CVs.

**Recommendation:** Treat income ranges as typical or annual-average monthly income ranges, if that is the intended meaning.

### 4.5 Correct obligation-ratio scaling

Current problems:

- `debt_payment` is referenced but absent from the category dictionary.
- `total_ratio` is retained from before normalization.
- Only essential categories are rescaled.
- Final category shares may not sum to one or match the intended obligation ratio.

For a complete, mutually exclusive category partition:

\[
p'_k=
\begin{cases}
q\frac{p_k}{\sum_{j\in E}p_j}, & k\in E\\
(1-q)\frac{p_k}{\sum_{j\notin E}p_j}, & k\notin E
\end{cases}
\]

Where:

- \(E\) is the essential/obligatory category set.
- \(q\) is the target share.

Handle zero-total groups explicitly.

Multiplying every category by the same scale factor and then normalizing does not change category composition.

### 4.6 Baseline shares conflict with flexible-profile requirements

The supplied essential-category shares sum to:

\[
41.1+28.9+5.9+2.4+1.7=80.0\%
\]

Including communication and insurance gives:

\[
80.0+3.9+2.6=86.5\%
\]

A persona cannot simultaneously match those average shares and have a flexible obligation ratio of 30–55%.

**Recommendation:** Validate weighted population or subgroup aggregates, not every individual household against the overall average.

### 4.7 Expense generation must preserve budgets

The current rule:

```python
daily_base = monthly_income * category_ratio / 30
```

approximately allocates all income to spending before noise and seasonal effects.

Use a separate expenditure budget:

\[
E_{\text{annual}}=\text{calibrated annual cash expenditure}
\]

Or, where definitions are compatible:

\[
E_{\text{annual}}=I_{\text{annual}}(1-s)
\]

Allocate this budget across categories and dates.

Normalize temporal weights when the intention is to redistribute expenditure rather than increase annual expenditure.

The listed September–December multipliers imply an equal-month average uplift of:

\[
\frac{8+1.1+1.2+1.4+2.2}{12}-1
\approx15.8\%
\]

Stacked December, payday, discretionary, and bonus-period multipliers can produce:

\[
2.2\times2.1\times1.3\times2.0=12.012
\]

This is approximately 12 times baseline spending before random noise.

### 4.8 Runway requires liquid assets and opening balances

Period income minus period spending is net cash flow, not necessarily available savings.

Use:

\[
L_t=L_0+\sum_{\tau\leq t}
(\text{cash inflows}_{\tau}-\text{cash outflows}_{\tau})
\]

Then:

\[
\text{runway}_t=
\frac{\text{accessible emergency reserves}_t}
{\text{typical monthly essential cash outflows}_t}
\]

Exclude unavailable or inappropriate assets such as:

- Owner-occupied housing.
- Unavailable retirement assets.
- Credit limits.
- Funds already committed to near-term obligations.

If total spending remains the denominator, name the metric **total-spending runway**.

### 4.9 Daily category transactions create constant features

One transaction per category every day implies:

- Category diversity approximately `1.0`.
- Average gap between active dates approximately `1 day`.
- Gap variance approximately `0`.

Model transaction occurrence separately from amount.

Examples:

- Rent: scheduled.
- Utilities: billing-cycle based.
- Tuition: enrollment or term based.
- Health care: intermittent.
- Food: frequent but not necessarily daily in every category.
- Durables: infrequent.

### 4.10 Anomaly injection does not produce exactly 3%

Under the current mixture:

- 80% of selections add one transaction.
- 20% add an average of four transactions.

Expected added records per selection:

\[
0.8(1)+0.2(4)=1.6
\]

For `0.03N` selections:

\[
A\approx0.048N
\]

Expected final flagged fraction:

\[
\frac{0.048N}{N+0.048N}\approx4.58\%
\]

For append-only injection targeting final fraction \(r\):

\[
A=\frac{rN}{1-r}
\]

Track anomaly events separately from affected transaction records.

---

## 5. Accountant Validation Answers

## A. PFP Classification Thresholds

| ID | Evidence-informed answer | Recommended disposition |
|---|---|---|
| PFP-01 | No universal `0.50` CV cutoff is established. Use monthly income and complete calendar months. Twelve complete months is a reasonable initial engineering window for one annual cycle, not a validated minimum. Evaluate shorter windows separately.[3–6] | Pending calibration. |
| PFP-02 | Lower variability for regular salaries is plausible, but exact archetype CVs are unverified. Weekly or biweekly pay does not inherently mean unstable earnings. Biweekly payroll can produce two- and three-paycheck months. | Revise: separate employment type, payroll frequency, and income variability. |
| PFP-03 | `0.60` is not an established standard for essential/obligatory spending divided by total spending. This measures composition, not direct affordability. Add essential committed outflows divided by disposable cash income as a separate metric. | Pending calibration; revise interpretation. |
| PFP-04 | Classify expenses by purpose and commitment, not broad category name alone. Use the category policy below. | Revise taxonomy; accountant review appropriate. |
| PFP-05 | Three months is defensible as a planning floor within common three-to-six-month guidance.[7] It is not a verified NCR population boundary. Variable-income households may need a larger planning buffer. | Provisionally retain as planning guidance. |
| PFP-06 | Use income CV for income stability. Spending CV is a separate feature. Rule 19 currently risks mixing transaction types and uses spending rather than income. | Revise before training. |

### PFP-04: Category policy

| Expense | Essential/obligatory treatment | Accounting or modeling caution |
|---|---|---|
| Rent | Generally include. | Use actual payments, not imputed rent. |
| Mortgage | Include required payment for cash-flow burden. | Split principal and interest; avoid housing/debt duplication. |
| Utilities | Include basic service. | Separate optional upgrades where feasible. |
| Food | Include basic nourishment. | Separate premium dining and alcohol. |
| Work/school transport | Generally include. | Separate leisure travel. |
| Dependent support | Include necessary or committed support. | Avoid counting both household transfers and resulting purchases. |
| Child care | Include when necessary. | Distinguish discretionary extras. |
| Tuition | Generally include committed basic education. | Separate elective courses and premium extras. |
| Debt repayment | Include minimum required payment. | Extra principal is a separate allocation choice. |
| Insurance | Include required/basic protection where appropriate. | Separate investment components when possible. |
| Health care | Include necessary treatment and medication. | Elective cosmetic/wellness spending may differ. |
| Remittances sent | Depends on necessity and commitment. | Separate required support from voluntary gifts. |
| Taxes | Include mandatory cash taxes where relevant. | Avoid double-counting withholding if income is net. |
| Subscriptions | Usually discretionary. | Exceptions include essential work tools and basic connectivity. |
| Business expenses | Separate from household consumption. | Do not deduct costs twice from already-net business income. |

### Terminology correction

Financial risk tolerance is a preference or attitude.

Emergency runway measures liquidity capacity.

Consider replacing:

- `Tolerant` with `Adequate buffer`.
- `At-Risk` with `Low buffer`.

If existing labels are retained, explicitly document their operational meaning and limitations.

---

## B. Income Timing and Gaps

| ID | Evidence-informed answer | Recommended disposition |
|---|---|---|
| INC-01 | No shared `2.5 receipts/month` estimate is established for VAs, writers, designers, and developers. Model monthly retainers, weekly payouts, and milestone payments separately. Poisson is a candidate distribution, not an occupational fact. | Pending transaction-data calibration. |
| INC-02 | A shared `15%` zero-income probability is unsupported. Distinguish zero revenue, zero net earnings, zero payout, and zero observed household income. | Revise; estimate by arrangement and measurement scope. |
| INC-03 | `50%` is unsupported as a general project-worker estimate. Independent monthly draws can create unrealistic gap sequences. Prefer contract duration, milestones, delays, and gap-duration models. | Requires contract/payment evidence. |
| INC-04 | Unemployment does not imply zero total household income. Pensions, assistance, remittances, and informal earnings may remain. A retired household should not automatically be assigned zero income. | Revise. |
| INC-05 | Labor Code Article 103 generally supports at-least-biweekly or twice-monthly wage payment, subject to applicable rules.[9] It does not establish BPO-specific payroll prevalence. Record scheduled payday and actual credit date separately. | Obtain payroll/HR evidence. |

### Recommended income-source representation

```text
regular_salary
seasonal_wages
net_business_income
pension
remittances_received
government_cash_support
other_income
```

Track the following separately:

```text
loan_proceeds
asset_sale_proceeds
own_account_transfers
withdrawals_from_savings
refunds_and_reversals
```

The second group must not automatically inflate earned or disposable income.

---

## C. Expense Allocation and Payday Cycle

Research supports income-timing effects on spending, but not the exact proposed NCR multipliers.[3–5]

| ID | Evidence-informed answer | Recommended disposition |
|---|---|---|
| EXP-01 | `65–85%` and `30–55%` are class-separation assumptions, not verified population ranges. Uniform sampling is also unverified and leaves limited near-boundary coverage. Prefer weighted donor distributions or fitted bounded distributions. | Revise; label as simulation assumptions. |
| EXP-02 | Anchor spikes to actual credited payday, not fixed calendar dates. Handle month-end, February, weekends, and holidays explicitly. `2.1×` is not validated locally. | Mechanism supported; magnitude pending. |
| EXP-03 | Discretionary purchases may respond to liquidity, but an additional `1.3×` is not established. Essential purchases can also be deferred until payday. | Estimate category-specific responses. |
| EXP-04 | Late-cycle suppression is plausible for cash-constrained users. Fixed dates and `0.50×` are not established. Use days until next pay, available cash, and bill schedules. | Revise; magnitude pending. |
| EXP-05 | The same phase lengths cannot represent weekly, biweekly, and semimonthly cycles. Use normalized position within the pay cycle. | Revise feature definition. |
| EXP-06 | No BPO-specific `1.5×` spending effect is established. BPO export statistics do not measure employee payroll or spending behavior. | Requires payroll-linked transaction evidence. |

Suggested cycle-position feature:

\[
\text{cycle position}
=
\frac{\text{days since previous payday}}
{\text{days between adjacent paydays}}
\]

When estimating payday effects, control for:

- Day of week.
- Month.
- Holidays.
- Scheduled bills.
- Transaction category.
- Household and employment characteristics.

---

## D. Calendar and Seasonal Effects

| ID | Evidence-informed answer | Recommended disposition |
|---|---|---|
| CAL-01 | Christmas-related spending is plausible, but `+10%, +20%, +40%, +120%` is not established for NCR household transactions. Consumer outlook or retail indicators cannot be directly converted into personal spending multipliers. | Pending behavioral calibration. |
| CAL-02 | Separate benefit receipt from spending response. For covered private-sector employees, the general minimum 13th-month calculation is total basic salary earned during the calendar year divided by 12, subject to applicable rules.[9] No universal `2.0×` spending response is established. | Correct benefit generation; spending multiplier pending. |
| CAL-03 | Compute Holy Week dates annually. Travel-volume evidence does not establish `1.4×` recreation or `0.8×` total food spending. Food purchased while traveling remains consumption. | Keep calendar event; remove unsupported universal effects. |
| CAL-04 | Apply education seasonality only to relevant households. Use actual school calendars and billing schedules. June/October and miscellaneous suppression are not universal. | Revise applicability and timing. |
| CAL-05 | Undas can involve transport, flowers, donations, and family purchases. These should not all be labeled recreation. The proposed multipliers are unverified. | Revise categories; magnitude pending. |

### Legal citation correction

Use the appropriate distinction:

- Private-sector 13th-month pay: **Presidential Decree No. 851**, as modified by **Memorandum Order No. 28**, plus applicable DOLE guidance.
- Government Christmas bonus and cash gift: separate statutory and administrative arrangements, including **Republic Act No. 6686** where applicable.

Do not automatically apply one benefit rule to government and private-sector personas.

---

## E. Anomaly-Data Ground Truth

An unusual transaction is not necessarily fraud, an accounting error, or harmful behavior.[11]

| ID | Evidence-informed answer | Recommended disposition |
|---|---|---|
| ANO-01 | `3%` is an experimental contamination setting, not validated prevalence. Fraud rates cannot substitute for personal-finance anomaly rates. | Evaluate `0%, 1%, 3%, 5%` as explicit stress-test scenarios. |
| ANO-02 | `3–5×` a global typical amount is insufficient. Compare within user, category, merchant/channel, and season. Use empirical tails or robust scores with calibrated false-alert rates. | Retain multipliers only as injected severity levels. |
| ANO-03 | `3–5` extra transactions may be normal for groceries but unusual for insurance. Use contextual counts and defined windows. | Revise to category-specific velocity. |
| ANO-04 | `2–5 AM` is not intrinsically anomalous. Account for shift work, e-commerce, travel, automated billing, timezone, and posting delays. | Reject as a universal rule. |
| ANO-05 | Recategorization alone is not merchant novelty. Store merchant/payee IDs and distinguish new merchant, new category, mismatch, and categorization error. | Revise schema and definition. |
| ANO-06 | Compare cumulative spending over the budget period with that period’s budget. Spending above `1.0×` a hard budget is an overage, but alert materiality is a separate decision. | Separate budget alerts from behavioral anomalies. |
| ANO-07 | The proposed mixture is an experimental design, not an empirically established distribution. Report performance by anomaly type and test alternative mixtures. | Pending empirical calibration. |

Never expose the following as model input features:

```text
anomaly_type
injection_flag
injection_severity
synthetic_ground_truth_label
```

---

## 6. Preprocessing and Data-Cleaning Requirements

### 6.1 Source-data audit

| Audit item | Required check |
|---|---|
| Provenance | Source edition, access date, file hash, dictionary version. |
| Row counts | Before filtering, after NCR filtering, after exclusions. |
| Column counts | Raw schema versus selected modeling schema. |
| Geography | Confirm NCR coding from the actual dictionary. |
| Observation unit | Household, family, person, or transaction. |
| Weights | Identify correct household/person weight and use. |
| Monetary basis | Annual/monthly, current prices, gross/net, cash/noncash. |
| Identifiers | Verify uniqueness; determine whether composite keys are required. |
| Missing codes | Decode source-specific sentinel values. |

Reconcile the document’s references to:

- 41,380 households.
- 87 columns.
- Approximately 40 CSV columns.

These may describe separate stages, but the stages must be identified.

### 6.2 Reproduce financial baselines

Household-weighted mean:

\[
\bar{x}_w=\frac{\sum_iw_ix_i}{\sum_iw_i}
\]

Aggregate food expenditure share:

\[
R_{\text{aggregate}}
=
\frac{\sum_iw_iFOOD_i}{\sum_iw_iTOTEX_i}
\]

Weighted mean household food share:

\[
R_{\text{household}}
=
\frac{\sum_iw_i(FOOD_i/TOTEX_i)}{\sum_iw_i}
\]

These estimators are not interchangeable.

Similarly, distinguish:

\[
1-\frac{\sum_iw_iTOTEX_i}{\sum_iw_iTOINC_i}
\]

from:

\[
\frac{\sum_iw_i(1-TOTEX_i/TOINC_i)}{\sum_iw_i}
\]

For every reported statistic, record:

- Estimator.
- Population.
- Weight.
- Missing-value treatment.
- Zero/negative denominator treatment.
- Source table or reproducible query.

### 6.3 Avoid hierarchical double-counting

Check relationships among:

- `WAGES`, `REG_SAL`, and `SEASON_SAL`.
- `FOOD` and detailed food components.
- `NFOOD` and nonfood components.
- `TOINC` and income components.
- `TOTEX` and expenditure components.

Aggregate fields should be used for reconciliation, not added as independent categories.

Verify dictionary treatment of:

- Imputed rent.
- Own-produced consumption.
- In-kind receipts.
- Entrepreneurial losses.
- Taxes.
- Loan repayments.

Do not fabricate bank transactions from noncash accounting concepts.

### 6.4 Distinguish missing, zero, negative, and absent

| Situation | Treatment |
|---|---|
| No earnings from a source | Valid zero if supported by source definition. |
| Missing income response | Missing, not zero. |
| No connected-account transactions | Could reflect true inactivity or incomplete coverage. |
| Negative net business earnings | Potentially valid loss. |
| Negative transaction amount | Interpret using ledger, refund, and reversal conventions. |
| Expenditure exceeds income | Potentially valid financing from savings, debt, or support. |
| Extreme income/expense | Investigate before deleting or winsorizing. |

For income CV:

- Require a positive mean for the standard definition.
- Include verified zero-income months.
- Flag incomplete months.
- Record the number of complete observed months.
- Return undefined/missing when the measure is not meaningful.

Do not assign an all-zero-income user `CV = 0` and label that user Stable merely to avoid division by zero.

### 6.5 Correct inferred household and employment features

The formula:

```text
(FSIZE - 1) / earners
```

requires actual information about earners and dependents.

Also:

- `NET_RECEIPT > 0` does not establish freelance employment.
- Income plus urban residence does not identify BPO work.
- `CASH_ABROAD > 0` does not prove an exclusively OFW-funded household.

Treat unsupported occupation mappings as synthetic assignments, not observed FIES classifications.

### 6.6 Recommended generation sequence

1. Select weighted donors or calibrated subgroups.
2. Establish annual income by source.
3. Establish annual cash expenditure.
4. Set opening accessible liquid reserves.
5. Generate income receipt dates and amounts.
6. Allocate expense budgets across months and categories.
7. Generate transaction occurrence dates.
8. Generate amounts conditional on occurrence.
9. Reconcile totals and balances.
10. Compute realized metrics and labels.
11. Create separate anomaly-injected copies.
12. Validate and export.

Use actual calendar months.

A reusable generator must handle leap years rather than assuming every calendar year has 365 days.

### 6.7 Prevent label leakage

If:

\[
label=f(CV,\ obligation\ ratio,\ runway)
\]

and those exact features are model inputs, classification accuracy primarily measures reproduction of the rule.

This may be acceptable for rule emulation, but it is not independent validation of real-world financial risk.

Recommended evaluation:

| Model | Required evaluation design |
|---|---|
| PFP classifier | Compare with the direct rule-based baseline. |
| Questionnaire mode | Use responses available at prediction time; document synthetic response assumptions. |
| Forecaster | Chronological evaluation over intended forecast horizons. |
| Anomaly detector | Per-type performance and legitimate rare-event negatives. |
| All models | Separate users and preferably FIES donor households across splits. |

Do not attach a full-year label to early-year records and treat it as a contemporaneous label without acknowledging future-information use.[14–15]

### 6.8 Separate coverage sampling from population representation

Five of twelve archetypes are Tolerant:

\[
5/12=41.7\%
\]

If the supplied BSP 2% emergency-fund statistic is verified and comparable, this design deliberately oversamples adequately buffered households.

Describe the dataset as:

> An archetype-coverage training dataset, not a representative NCR population sample.

Keep appropriate sampling/calibration metadata.

Do not infer population prevalence from synthetic class balance.

---

## 7. Interim Parameter Register

| Item | Interim treatment | Evidence class |
|---|---|---|
| Stability measure | Monthly income CV. | Construct definition. |
| Observation window | Initially 12 complete months where available. | Engineering choice. |
| CV cutoff | `0.50`, versioned and provisional. | Simulation convention. |
| Obligation cutoff | `0.60`, only after taxonomy and denominator correction. | Simulation convention. |
| Emergency reserve | Three-month planning floor; six-month planning scenario. | Planning benchmark. |
| Receipt count | Payment-arrangement-specific. | Pending estimate. |
| Income gaps | Separate true gaps from missing coverage. | Measurement rule. |
| Temporal multipliers | Explicit scenarios until estimated locally. | Simulation assumption. |
| Anomaly rate | Test `0%, 1%, 3%, 5%`. | Experimental design. |
| Boundary tests | CV `0.50`; obligation `0.60`; runway `3.0`. | Software validation. |
| Randomness | Seeded generator and versioned configuration. | Reproducibility requirement. |

The generator should be described as:

> A reproducible stochastic generator conditional on source data, parameter version, and random seed.

It is not deterministic in the ordinary sense unless these inputs are fixed.

---

## 8. References and Evidence Limitations

### [1] Philippine Statistics Authority — FIES 2023

**Source:** *2023 Family Income and Expenditure Survey*: statistical tables, technical documentation, and public-use-file dictionary.

**Official entry point:**  
https://psa.gov.ph/statistics/income-expenditure/fies

**Supports:**

- Household financial aggregates.
- Variable definitions.
- Survey population and weights.
- Sampling methodology.

**Does not establish:**

- Daily payday behavior.
- Monthly CV from annual aggregates.
- Current bank balances.
- Exact PFP thresholds.

### [2] Bangko Sentral ng Pilipinas — Consumer Finance Survey 2021

**Source:** *2021 Consumer Finance Survey* results and methodological documentation.

**Official entry point:**  
https://www.bsp.gov.ph/

Locate the Consumer Finance Survey publication and relevant tables.

**Supports:**

- Covered household financial-access, asset, liability, and related survey indicators.

**Limitations:**

- Verify every percentage against its exact table and question.
- Record geography, denominator, and population.
- National household findings are not automatically NCR individual estimates.

### [3] Gelman et al. (2014)

Gelman, M., Kariv, S., Shapiro, M. D., Silverman, D., & Tadelis, S. (2014). Harnessing naturally occurring data to measure the response of spending to income. *Science, 345*(6193), 212–215.

https://doi.org/10.1126/science.1247727

**Supports:** High-frequency measurement of spending responses to income receipt.

**Limitation:** Does not validate a Philippine payday multiplier of `2.1×`.

### [4] Stephens (2003)

Stephens, M., Jr. (2003). “3rd of tha Month”: Do Social Security recipients smooth consumption between checks? *American Economic Review, 93*(1), 406–422.

**Supports:** Expenditure can vary around predictable income receipt.

**Limitation:** US Social Security recipients are not equivalent to NCR wage earners.

### [5] Stephens (2006)

Stephens, M., Jr. (2006). Paycheque receipt and the timing of consumption. *The Economic Journal, 116*(513), 680–701.

**Supports:** Consumption timing can respond to paycheck arrival.

**Limitation:** Does not establish universal phase lengths or NCR occupational multipliers.

### [6] Farrell, Greig, and Yu (2019)

Farrell, D., Greig, F., & Yu, C. (2019). *Weathering Volatility 2.0: A Monthly Stress Test to Guide Savings.* JPMorgan Chase Institute.

**Supports:**

- Joint income and expenditure volatility.
- Transaction-data approaches to liquid-buffer analysis.

**Limitation:** Findings from US banking customers should not be copied numerically into NCR calibration.

### [7] FINRA — Emergency-Fund Guidance

FINRA. *Start an Emergency Fund.*

https://www.finra.org/investors/insights/start-emergency-fund

**Supports:** Common three-to-six-month emergency-fund planning guidance and potentially larger needs for variable income.

**Limitation:** Planning guidance, not a peer-reviewed estimate of actual NCR reserve ownership.

### [8] Lusardi, Schneider, and Tufano (2011)

Lusardi, A., Schneider, D., & Tufano, P. (2011). Financially fragile households: Evidence and implications. *Brookings Papers on Economic Activity*, Spring, 83–134.

**Supports:** Measuring financial fragility through capacity to meet unexpected expenses.

**Limitation:** Does not derive the proposed three-month binary boundary or equate liquidity with risk preference.

### [9] Philippine Legal and Administrative Sources

- Presidential Decree No. 851.
- Memorandum Order No. 28, s. 1986.
- Labor Code, Article 103.
- DOLE, *Handbook on Workers’ Statutory Monetary Benefits*, applicable edition.
- Republic Act No. 6686, where relevant to government benefits.

**Official/legal entry points:**

- https://www.dole.gov.ph/
- https://www.officialgazette.gov.ph/
- https://lawphil.net/

**Supports:**

- Statutory benefit rules.
- Wage-payment requirements.

**Does not establish:**

- Employee spending multipliers.
- BPO payroll-schedule prevalence.

### [10] Deaton and Paxson (1998)

Deaton, A., & Paxson, C. (1998). Economies of scale, household size, and the demand for food. *Journal of Political Economy, 106*(5), 897–930.

**Supports:** Household composition and scale affect food expenditure patterns.

**Limitation:** Does not prescribe a Philippine Engel-coefficient acceptance interval of `0.30–0.60`.

### [11] Chandola, Banerjee, and Kumar (2009)

Chandola, V., Banerjee, A., & Kumar, V. (2009). Anomaly detection: A survey. *ACM Computing Surveys, 41*(3), Article 15.

https://doi.org/10.1145/1541880.1541882

**Supports:**

- Point, contextual, and collective anomalies.
- Context-dependent anomaly definitions.

**Limitation:** Does not establish universal personal-finance anomaly prevalence.

### [12] Liu, Ting, and Zhou (2008)

Liu, F. T., Ting, K. M., & Zhou, Z.-H. (2008). Isolation Forest. *IEEE International Conference on Data Mining*, 413–422.

https://doi.org/10.1109/ICDM.2008.17

**Supports:** Isolation-based anomaly detection.

**Limitation:** Algorithm choice does not validate injection realism or prevalence.

### [13] Saito and Rehmsmeier (2015)

Saito, T., & Rehmsmeier, M. (2015). The precision-recall plot is more informative than the ROC plot when evaluating binary classifiers on imbalanced datasets. *PLOS ONE, 10*(3), e0118432.

https://doi.org/10.1371/journal.pone.0118432

**Supports:** Precision-recall evaluation for rare anomalies.

**Application:** Also report recall at a tolerable false-alert rate.

### [14] Roberts et al. (2017)

Roberts, D. R., et al. (2017). Cross-validation strategies for data with temporal, spatial, hierarchical, or phylogenetic structure. *Ecography, 40*(8), 913–929.

https://doi.org/10.1111/ecog.02881

**Supports:** Validation designs that respect dependency and intended prediction settings.

**Application:** Split by user/donor and time.

### [15] Kapoor and Narayanan (2023)

Kapoor, S., & Narayanan, A. (2023). Leakage and the reproducibility crisis in machine-learning-based science. *Patterns, 4*(9), 100804.

https://doi.org/10.1016/j.patter.2023.100804

**Supports:** Avoiding target leakage and future-information leakage.

**Application:** Exclude injected labels and unavailable future-window features from predictors.

---

## 9. Decision Record Template

| ID | Accountant decision | Recommended value/range | Evidence/source | Population/conditions | Limitations | Date | Recorded by |
|---|---|---|---|---|---|---|---|
| PFP-01 | Pending | | | | | | |
| PFP-03 | Pending | | | | | | |
| PFP-05 | Pending | | | | | | |
| INC-02 | Pending | | | | | | |
| EXP-02 | Pending | | | | | | |
| CAL-01 | Pending | | | | | | |
| ANO-01 | Pending | | | | | | |

Add one row for every remaining consultation ID.

---

## 10. Implementation Acceptance Checklist

### Source verification

- [ ] Verify FIES geography, record count, dictionary, and observation unit.
- [ ] Reproduce financial baselines using documented estimators.
- [ ] Verify BSP percentages, denominators, and population.
- [ ] Separate cash and noncash concepts.
- [ ] Document all source versions and file hashes.

### Accounting and generator corrections

- [ ] Correct lognormal parameterization.
- [ ] Reconcile hard income bounds with target CVs.
- [ ] Correct obligation-ratio scaling.
- [ ] Preserve annual expense budgets.
- [ ] Add opening liquid reserves.
- [ ] Separate transfers, borrowing, and income.
- [ ] Generate realistic transaction occurrence schedules.
- [ ] Correct 13th-month benefit logic and citation.
- [ ] Reconcile zero-income probabilities.
- [ ] Calculate anomaly rates from final transaction counts.

### Labels and evaluation

- [ ] Compute stability from income rather than spending.
- [ ] Define a consistent observation window.
- [ ] Handle zero and undefined denominators explicitly.
- [ ] Test all classification boundaries.
- [ ] Keep ground-truth metadata out of predictors.
- [ ] Split by user/donor and time.
- [ ] Compare the PFP classifier with a direct rule-based baseline.
- [ ] Evaluate anomaly performance by type and false-alert burden.
- [ ] Distinguish archetype coverage from population representation.
- [ ] Document questionnaire-generation rules and leakage risks.

### Governance

- [ ] Reconcile stale Section 9 thresholds with active rules.
- [ ] Label every parameter by evidence class.
- [ ] Record accountant consultation decisions.
- [ ] Record behavioral/payment expert decisions where required.
- [ ] Re-run archetype validation after parameter changes.

---

## 11. Recommended Replacement Statement

> Financial aggregates are calibrated to documented FIES estimates using applicable survey weights and variable definitions. Behavioral parameters are classified separately as statutory rules, financial-planning benchmarks, empirical estimates, engineering choices, or simulation assumptions. Unless supported by a specific population-matched source, payday multipliers, income-gap probabilities, seasonal effects, classification cutoffs, and anomaly prevalence remain provisional experimental parameters. Accountant consultation validates accounting treatment and planning interpretation; behavioral prevalence requires suitable survey or transaction evidence.

---

## 12. Final Assessment

The most defensible numerical items currently available are:

1. Mathematical corrections derived from the proposed generator.
2. Applicable statutory benefit calculations.
3. The three-to-six-month emergency-fund planning range.

The remaining behavioral values should remain provisional until supported by appropriate evidence.

**Do not mark the current rules as accountant-approved or empirically calibrated solely on the basis of this review.**
