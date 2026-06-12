# Model Training Data Design

This document defines the training data shape, sample synthetic rows, inputs, outputs, model connections, and column importance for the three final Odin models:

- Random Forest for Financial Behavioral Profile classification
- LSTM for spending forecasting
- Isolation Forest for transaction anomaly detection

---

## 1. Random Forest

### 1.1 Purpose of Model

Random Forest classifies each user into one Financial Behavioral Profile (FBP):

- `Stable_Obligated`
- `Stable_Flexible`
- `Variable_Obligated`
- `Variable_Flexible`

The FBP is used to personalize forecasting, budget recommendations, and anomaly detection baselines.

Random Forest operates at the user level:

```text
1 row = 1 user
```

### 1.2 Synthetic Data Sample Rows

| user_id | income_source_count | income_amount | income_frequency | income_cv | employment_type | monthly_spending_cv | obligation_ratio | fixed_obligations_income_ratio | debt_payments_income_ratio | essentials_spend_ratio | obligatory_spend_ratio | discretionary_spend_ratio | financial_allocation_ratio | savings_rate | dependents_count | recurring_expense_count | fbp_label |
|---|---:|---:|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| U001 | 1 | 30000 | bi_monthly | 0.03 | salaried | 0.12 | 0.66 | 0.42 | 0.18 | 0.45 | 0.21 | 0.24 | 0.10 | 0.08 | 2 | 6 | Stable_Obligated |
| U002 | 1 | 45000 | monthly | 0.04 | salaried | 0.15 | 0.38 | 0.20 | 0.05 | 0.30 | 0.08 | 0.42 | 0.20 | 0.18 | 0 | 3 | Stable_Flexible |
| U003 | 3 | 28000 | variable | 0.31 | freelance | 0.41 | 0.62 | 0.36 | 0.20 | 0.39 | 0.23 | 0.30 | 0.08 | 0.04 | 1 | 5 | Variable_Obligated |
| U004 | 2 | 52000 | variable | 0.27 | commission | 0.37 | 0.34 | 0.14 | 0.03 | 0.25 | 0.09 | 0.50 | 0.16 | 0.12 | 0 | 2 | Variable_Flexible |
| U005 | 1 | 25000 | weekly | 0.06 | contractual | 0.19 | 0.55 | 0.31 | 0.12 | 0.40 | 0.15 | 0.35 | 0.10 | 0.07 | 3 | 7 | Stable_Obligated |

### 1.3 Input Data vs Output Data

Input data:

| Input Type | Columns |
|---|---|
| Income features | `income_source_count`, `income_amount`, `income_frequency`, `income_cv`, `employment_type` |
| Spending stability features | `monthly_spending_cv` |
| Obligation features | `obligation_ratio`, `fixed_obligations_income_ratio`, `debt_payments_income_ratio` |
| Spending composition features | `essentials_spend_ratio`, `obligatory_spend_ratio`, `discretionary_spend_ratio`, `financial_allocation_ratio` |
| Household and behavior features | `savings_rate`, `dependents_count`, `recurring_expense_count` |

Output data:

| Output | Description |
|---|---|
| `fbp_label` | Predicted Financial Behavioral Profile |
| `class_probability` | Confidence score per FBP class, if exposed by the implementation |
| `top_features` | Optional explanation fields showing strongest contributors to the classification |

Example:

```text
Input user features -> Random Forest -> Stable_Obligated
```

### 1.4 Connection to Other Models

Random Forest connects to LSTM by producing the user-level `fbp` value used as an LSTM context feature.

```text
User profile features
        ->
Random Forest
        ->
fbp_label
        ->
LSTM training rows
```

Random Forest also connects to Isolation Forest by providing a profile-aware anomaly baseline.

```text
fbp_label -> choose FBP/category anomaly threshold or fallback Isolation Forest model
```

### 1.5 Dataset Column Importance

| Importance | Column | Reason |
|---:|---|---|
| 1 | `monthly_spending_cv` | Separates Stable from Variable users. |
| 2 | `obligation_ratio` | Separates Obligated from Flexible users. |
| 3 | `fixed_obligations_income_ratio` | Identifies users dominated by recurring fixed costs. |
| 4 | `debt_payments_income_ratio` | Strengthens obligated classification when debt burden is high. |
| 5 | `income_cv` | Captures income instability for freelancers, commission workers, and variable earners. |
| 6 | `discretionary_spend_ratio` | Helps identify Flexible users. |
| 7 | `savings_rate` | Helps distinguish financially flexible users from obligation-heavy users. |
| 8 | `dependents_count` | Supports obligated classification where household support is present. |
| 9 | `recurring_expense_count` | Indicates fixed-payment behavior. |
| 10 | `income_amount` | Useful for scaling but should not dominate classification alone. |

---

## 2. LSTM

### 2.1 Purpose of Model

LSTM forecasts future spending by broad category using historical daily spending sequences.

LSTM operates at the user-day level:

```text
1 row = 1 user-day
```

The model forecasts the next day, week, or month of spending for:

- `essentials`
- `obligatory`
- `discretionary`
- `financial_allocation`

### 2.2 Synthetic Data Sample Rows

| user_id | date | essentials_amount | obligatory_amount | discretionary_amount | financial_allocation_amount | total_spending | income | fbp | day_of_week | day_of_month | is_payday | is_holiday | is_13th_month_period | is_christmas_period |
|---|---|---:|---:|---:|---:|---:|---:|---|---:|---:|---:|---:|---:|---:|
| U001 | 2026-01-13 | 420 | 0 | 120 | 0 | 540 | 30000 | Stable_Obligated | 2 | 13 | 0 | 0 | 0 | 0 |
| U001 | 2026-01-14 | 300 | 0 | 80 | 0 | 380 | 30000 | Stable_Obligated | 3 | 14 | 0 | 0 | 0 | 0 |
| U001 | 2026-01-15 | 900 | 2500 | 850 | 1500 | 5750 | 30000 | Stable_Obligated | 4 | 15 | 1 | 0 | 0 | 0 |
| U001 | 2026-01-16 | 550 | 0 | 600 | 0 | 1150 | 30000 | Stable_Obligated | 5 | 16 | 0 | 0 | 0 | 0 |
| U001 | 2026-01-17 | 480 | 0 | 350 | 0 | 830 | 30000 | Stable_Obligated | 6 | 17 | 0 | 0 | 0 | 0 |

### 2.3 Input Data vs Output Data

Input data:

| Input Type | Columns |
|---|---|
| Historical spending sequence | `essentials_amount`, `obligatory_amount`, `discretionary_amount`, `financial_allocation_amount`, `total_spending` |
| User context | `income`, `fbp` |
| Calendar context | `day_of_week`, `day_of_month` |
| Event context | `is_payday`, `is_holiday`, `is_13th_month_period`, `is_christmas_period` |

Output data:

| Output | Description |
|---|---|
| `forecast_essentials_amount` | Predicted future essentials spending. |
| `forecast_obligatory_amount` | Predicted future obligatory spending. |
| `forecast_discretionary_amount` | Predicted future discretionary spending. |
| `forecast_financial_allocation_amount` | Predicted future savings/investment/allocation amount. |
| `forecast_total_spending` | Sum of the four forecast categories. |

Example:

```text
Past 60 user-day rows -> LSTM -> next-day category spending forecast
```

### 2.4 Connection to Other Models

LSTM receives the FBP output from Random Forest.

```text
Random Forest output:
U001 -> Stable_Obligated

LSTM input:
U001 daily spending rows + fbp = Stable_Obligated
```

LSTM connects to Isolation Forest and budget recommendation by providing expected spending baselines.

```text
LSTM forecast -> expected category spending
Actual transaction -> Isolation Forest anomaly features
Actual spending vs forecast -> budget recommendation engine
```

### 2.5 Dataset Column Importance

| Importance | Column | Reason |
|---:|---|---|
| 1 | Previous category amounts | Core time-series signal for spending behavior. |
| 2 | `total_spending` | Helps the model learn total spending movement. |
| 3 | `fbp` | Gives profile context from Random Forest. |
| 4 | `income` | Scales expected spending capacity. |
| 5 | `is_payday` | Captures payday spending spikes and allocation behavior. |
| 6 | `day_of_month` | Captures rent, bills, and monthly payment timing. |
| 7 | `day_of_week` | Captures weekday/weekend spending patterns. |
| 8 | `is_christmas_period` | Captures seasonal December/Ber-month spending increases. |
| 9 | `is_13th_month_period` | Captures income and spending changes caused by 13th month pay. |
| 10 | `is_holiday` | Captures culturally expected spikes that should not be treated as ordinary days. |

---

## 3. Isolation Forest

### 3.1 Purpose of Model

Isolation Forest detects anomalous transactions.

Isolation Forest operates at the transaction level:

```text
1 row = 1 transaction
```

This model is used for user-facing anomaly alerts, such as:

```text
Unusual spending detected: PHP 4,800 online shopping is much higher than your normal online shopping amount.
```

### 3.2 Synthetic Data Sample Rows

| transaction_id | user_id | date | detailed_category | lstm_category | amount | monthly_income | amount_income_ratio | category_30d_avg | amount_category_avg_ratio | days_since_payday | day_of_month | is_payday | is_holiday | is_recurring | fbp |
|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| T001 | U001 | 2026-01-03 | groceries | essentials | 650 | 30000 | 0.0217 | 580 | 1.12 | 3 | 3 | 0 | 0 | 0 | Stable_Obligated |
| T002 | U001 | 2026-01-05 | transport | essentials | 80 | 30000 | 0.0027 | 75 | 1.07 | 5 | 5 | 0 | 0 | 0 | Stable_Obligated |
| T003 | U001 | 2026-01-15 | credit_card_payment | obligatory | 2500 | 30000 | 0.0833 | 2500 | 1.00 | 0 | 15 | 1 | 0 | 1 | Stable_Obligated |
| T004 | U001 | 2026-01-15 | dining_out | discretionary | 850 | 30000 | 0.0283 | 420 | 2.02 | 0 | 15 | 1 | 0 | 0 | Stable_Obligated |
| T005 | U001 | 2026-01-22 | online_shopping | discretionary | 4800 | 30000 | 0.1600 | 700 | 6.86 | 7 | 22 | 0 | 0 | 0 | Stable_Obligated |

### 3.3 Input Data vs Output Data

Input data:

| Input Type | Columns |
|---|---|
| Transaction amount features | `amount`, `amount_income_ratio`, `amount_category_avg_ratio` |
| Category features | `detailed_category`, `lstm_category` |
| Time features | `days_since_payday`, `day_of_month`, `is_payday`, `is_holiday` |
| User behavior features | `category_30d_avg`, `is_recurring`, `fbp` |

Output data:

| Output | Description |
|---|---|
| `anomaly_label` | `normal` or `anomaly`. |
| `anomaly_score` | Numeric anomaly score from Isolation Forest. |
| `alert_reason` | Human-readable explanation generated from feature values. |

Example:

```text
Transaction features -> Isolation Forest -> anomaly
```

### 3.4 Connection to Other Models

Isolation Forest receives the FBP output from Random Forest as user context.

```text
Random Forest -> fbp -> Isolation Forest context
```

Isolation Forest can also compare transactions against LSTM forecast expectations.

```text
LSTM forecast:
expected discretionary spending today = PHP 900

Actual transaction:
online shopping = PHP 4,800

Isolation Forest:
flag as anomaly if transaction is unusual against user/category/profile baseline
```

Isolation Forest output feeds alerts and budget recommendation.

```text
anomaly alert -> user confirmation -> future whitelist/suppression rules
```

### 3.5 Dataset Column Importance

| Importance | Column | Reason |
|---:|---|---|
| 1 | `amount_category_avg_ratio` | Strongest signal that a transaction is unusual for its category. |
| 2 | `amount_income_ratio` | Identifies transactions unusually large relative to income. |
| 3 | `amount` | Raw transaction size still matters. |
| 4 | `is_recurring` | Prevents normal recurring bills from being flagged. |
| 5 | `detailed_category` | Gives category-specific anomaly context. |
| 6 | `days_since_payday` | Distinguishes payday spikes from unusual off-cycle spending. |
| 7 | `is_payday` | Helps avoid false positives on normal payday spending. |
| 8 | `is_holiday` | Helps suppress culturally expected spending spikes. |
| 9 | `fbp` | Provides profile-aware expectations. |
| 10 | `day_of_month` | Captures monthly bills and recurring payment timing. |

---

## 4. Overall Model Connection

The final model pipeline is:

```text
Raw user onboarding data + early transaction summaries
        |
        v
Random Forest
        |
        v
FBP label per user
        |
        +------------------+
        |                  |
        v                  v
LSTM forecasting       Isolation Forest anomaly detection
        |                  |
        v                  v
Spending forecasts     Transaction anomaly alerts
        |                  |
        +---------+--------+
                  |
                  v
Budget recommendation and user-facing guidance
```

Input-output summary:

| Model | Unit of Data | Input | Output | Consumed By |
|---|---|---|---|---|
| Random Forest | User | User-level financial features | FBP label | LSTM, Isolation Forest, budget recommendation |
| LSTM | User-day sequence | Daily category spending + FBP + calendar/event features | Future category spending forecast | Budget recommendation, dashboards, anomaly context |
| Isolation Forest | Transaction | Transaction features + FBP + calendar/event features | Anomaly label and score | Alerts, user feedback loop, budget recommendation |

---

## 5. Data Storage Recommendation

Store detailed raw transactions, then transform them into model-specific datasets.

```text
Raw transactions
1 row = 1 user transaction

        ->

Random Forest features
1 row = 1 user

        ->

LSTM features
1 row = 1 user-day

        ->

Isolation Forest features
1 row = 1 transaction
```

Recommended category handling:

| Data Layer | Category Level |
|---|---|
| Raw transaction storage | Detailed categories such as groceries, rent, dining_out, transport, debt_payment |
| LSTM training | Broad categories: essentials, obligatory, discretionary, financial_allocation |
| Budget recommendation | Detailed categories, using LSTM broad forecasts as context |
| Isolation Forest | Detailed category plus broad LSTM category |

