# Accountant Validation Question Log

> **Status:** Draft - pending accountant consultation.
> **Purpose:** Record decisions and evidence needed before the provisional synthetic-data rules in [Synthetic Data Injection Rules](synthetic-injection-rules.md) are treated as calibrated parameters.
> **Scope:** Metro Manila/NCR personal-finance behavior, unless the accountant recommends a broader or narrower population.

---

## Consultation Instructions

- Confirm whether each proposed value is appropriate, inappropriate, or not answerable from accounting practice alone.
- Where a numeric value is appropriate, provide a typical value or range, the relevant population, and the basis for it (professional experience, client records, survey, or published source).
- Distinguish a recommended financial-planning benchmark from a descriptive estimate of what people actually do.
- Record material differences by employment type, household size, dependents, income level, and location.
- Do not finalize a parameter without recording its evidence and limitations.

| Decision status | Meaning |
| :--- | :--- |
| Pending | No accountant decision recorded. |
| Approved | Accountant supports the proposed operational rule. |
| Revise | Accountant recommends a different rule or range. |
| Out of scope | Requires a behavioral, labor, payments, or transaction-data expert rather than an accountant. |

---

## A. PFP Classification Thresholds

| ID | Question for the accountant | Current proposed rule | Required response | Status |
| :--- | :--- | :--- | :--- | :--- |
| PFP-01 | Is an income coefficient of variation (CV) of `0.50` a defensible boundary for classifying monthly income as Stable (`< 0.50`) or Variable (`>= 0.50`)? Should the calculation use monthly income, a rolling window, and how many months? | `0.50` cutoff | Recommended cutoff/range, observation window, and rationale by employment type. | Pending |
| PFP-02 | Does the `0.50` CV rule sensibly classify the archetypes in Section 3.3: regular BPO and salaried workers (`0.08-0.15`), freelance/contract workers (`0.60-0.70`), and part-time sales (`0.55`)? | Archetype CVs in Section 3.3 | Confirm, revise, or identify archetypes that need different values. | Pending |
| PFP-03 | Is an obligation ratio above `0.60` an appropriate boundary for Obligated, with `<= 0.60` as Flexible? | `(essential + obligatory expenses) / total expenses` | Recommended cutoff/range and whether it differs by household composition or income band. | Pending |
| PFP-04 | Which expenses should count as essential or obligatory in the obligation ratio? Please classify rent/mortgage, utilities, food, transport to work/school, dependent support, child care, tuition, debt repayment, insurance, health care, remittances, taxes, subscriptions, and business expenses. | Current essential list: food, housing, transport, health, education; current obligatory list: debt payment | Category-by-category inclusion decision and treatment of partly discretionary expenses. | Pending |
| PFP-05 | Is three months of expenses an appropriate emergency-fund runway boundary for Tolerant (`>= 3`) versus At-Risk (`< 3`)? Is it a planning recommendation, a descriptive classification threshold, or both? | `3` months | Recommended threshold/range, including whether variable-income households need a higher runway. | Pending |
| PFP-06 | The current document labels stability from monthly *income* CV in Sections 2-4 but computes the final label from monthly *spending* CV in Rule 19. Which measure should determine Financial Stability? | Conflicting definitions | Specify the correct measure and minimum history needed. | Pending |

---

## B. Income Timing and Gaps

| ID | Question for the accountant | Current proposed rule | Required response | Status |
| :--- | :--- | :--- | :--- | :--- |
| INC-01 | Do freelancers commonly receive income two to three times per month? If so, does this vary meaningfully among virtual assistants, writers, designers, and freelance developers? | Poisson mean `2.5` receipts/month | Typical receipt count/range and the appropriate distribution or caveat. | Pending |
| INC-02 | Is a `15%` probability of no income in a month realistic for construction workers, online sellers, and freelance developers? Should each occupation use a separate probability? | `15%` per month | Recommended probability/range per occupation and supporting basis. | Pending |
| INC-03 | Is a `50%` monthly zero-income probability realistic for project-based workers between projects? | `50%` per month | Recommended probability/range and an appropriate contract-gap model. | Pending |
| INC-04 | Is `100%` zero income appropriate for the Unemployed pattern? How should pensions, severance, government support, remittances, or informal earnings be represented if present? | `100%` per month | Confirm scope and required exceptions. | Pending |
| INC-05 | Are weekly or biweekly payroll schedules common enough among BPO workers to model separately from the 15th/30th schedule? | Weekly or biweekly BPO payday | Applicable schedules, their prevalence if known, and any distinction between payroll date and credited date. | Pending |

---

## C. Expense Allocation and Payday Cycle

| ID | Question for the accountant | Current proposed rule | Required response | Status |
| :--- | :--- | :--- | :--- | :--- |
| EXP-01 | For obligated profiles, is a random obligation ratio between `65%-85%` appropriate? For flexible profiles, is `30%-55%` appropriate? | Obligated: `65%-85%`; Flexible: `30%-55%` | Recommended ranges and whether a uniform random distribution is realistic. | Pending |
| EXP-02 | Are the 15th-16th and 30th-31st reasonable dates for a post-payday spending spike for semi-monthly paid workers? How should months without a 31st be handled? | `2.1x` total-spend multiplier, clipped to `1.5x-3.0x` | Confirm dates, expected duration, and a defensible multiplier/range. | Pending |
| EXP-03 | After payday, are recreation, clothing, and miscellaneous expenses more likely to increase than other categories? By what percentage or multiplier, if measurable? | Additional `1.3x` discretionary multiplier | Category-specific multiplier/range and basis. | Pending |
| EXP-04 | Are days 10-14 and 26-29 credible `petsa de peligro` windows for semi-monthly paid households? Do they vary by pay schedule, expense due dates, or household type? | `0.50x` spend multiplier; food/transport floor `0.60x` | Confirm windows and category-specific suppression range. | Pending |
| EXP-05 | Is the generalized post-payday lifecycle appropriate: days 1-3 surge, days 4-10 normal, then spending suppression until the next payday? | Current Rule 15 | Recommended phase lengths by weekly, biweekly, and semi-monthly schedule. | Pending |
| EXP-06 | For BPO workers with weekly or biweekly pay, how much does spending increase around payday compared with regular days? | `1.5x` multiplier | Recommended multiplier/range and duration. | Pending |

---

## D. Calendar and Seasonal Effects

| ID | Question for the accountant | Current proposed rule | Required response | Status |
| :--- | :--- | :--- | :--- | :--- |
| CAL-01 | Should spending increase from September through December because of Christmas-related expenses? If so, what is a realistic increase against a regular month for September, October, November, and December? | `+10%`, `+20%`, `+40%`, `+120%` respectively | Monthly percentage/range, affected categories, and whether values apply to all households. | Pending |
| CAL-02 | After 13th-month pay, should discretionary spending rise during December? By what percentage for recreation, clothing, and food, and over what dates? | `2.0x` for Dec. 15-24 | Category-specific multiplier/range. Distinguish receipt of the benefit from spending it. | Pending |
| CAL-03 | During Semana Santa, should recreation or travel spending increase and food spending decrease? | Recreation `1.4x`; food `0.8x` | Category-specific effect/range and whether Holy Week dates should be computed annually rather than approximated by March/April. | Pending |
| CAL-04 | Do enrollment periods in June and October materially increase education spending? Does miscellaneous spending decrease when funds are redirected? | Education `1.4x`; miscellaneous `0.85x` | Applicable enrollment periods by school type and category-specific ranges. | Pending |
| CAL-05 | Do Undas activities on November 1-2 increase recreation or travel spending and reduce regular food spending? | Recreation `1.45x`; food `0.75x` | Category-specific effect/range and which households are affected. | Pending |

---

## E. Anomaly-Data Ground Truth

> Accountant input can define financially implausible or material events, but behavioral anomaly prevalence and user-specific detection thresholds should also be validated with transaction data or an anomaly-detection specialist.

| ID | Question for the accountant | Current proposed rule | Required response | Status |
| :--- | :--- | :--- | :--- | :--- |
| ANO-01 | Is a global `3%` anomaly rate appropriate for synthetic personal-finance transactions, or should the rate vary by transaction volume, income stability, and spending behavior? | `3%` overall target | Recommended overall/per-user rate or scope limitation. | Pending |
| ANO-02 | Is an amount `3x-5x` a user's usual transaction amount an appropriate monetary-spike anomaly? Should the baseline be per merchant/category and use a user-specific distribution rather than a fixed multiplier? | `3x-5x` | Recommended threshold/range and comparison baseline. | Pending |
| ANO-03 | Is inserting `3-5` additional same-category transactions over `1-7` days a realistic category-velocity anomaly? | `3-5` transactions in `1-7` days | Recommended count/window or a user-specific method. | Pending |
| ANO-04 | Are transactions at 2:00-5:00 AM anomalous in themselves, or should temporal deviation be based on each user's historical transaction times and merchant channel? | 2:00-5:00 AM | Recommended rule and exceptions (e-commerce, shift work, BPO, travel). | Pending |
| ANO-05 | Is recategorizing a transaction as recreation, clothing, or miscellaneous sufficient to represent merchant novelty? | Category change only | Confirm whether novelty must be based on a new merchant/payee, new merchant category, or both. | Pending |
| ANO-06 | Is spending `1.5x-2.5x` the allocated category budget an appropriate budget-overage anomaly? | `1.5x-2.5x` category budget | Recommended threshold/range and whether budget period is monthly, weekly, or rolling. | Pending |
| ANO-07 | Is the planned anomaly mix appropriate: 30% monetary spikes, 20% category velocity, 20% temporal deviation, 15% merchant novelty, 15% budget overage? | Proposed distribution totals 100% | Confirm distribution or identify which components require empirical transaction-data calibration. | Pending |

---

## Decision Record

| ID | Accountant decision | Evidence or source | Population/conditions | Date | Recorded by |
| :--- | :--- | :--- | :--- | :--- |
|  |  |  |  |  |  |

---

## Reconciliation Required Before Implementation

- Update Rules 5, 7-15, and 20 in `synthetic-injection-rules.md` only after the corresponding decision record is complete.
- Reconcile the stale Open Questions in Section 9 of that document with the active thresholds in Rule 20; Section 9 currently cites a `0.5` obligation threshold and `0.2` CV threshold, while Rule 20 uses `0.6` and `0.5`.
- State each finalized parameter's evidence source, target population, effective date, and any uncertainty range.
- Re-run persona validation for the Section 3.3 archetypes after any threshold or allocation change.
