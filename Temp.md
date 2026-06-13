# SPECIFICATION: Odin Personal Finance Management System

**Document Type:** Technical Specification

**Version:** 4.0

**Date:** 2026-06-13

---

## Article I: Platform and Target Users

### Section 1. Platform

1. The System shall be implemented as a **mobile‑first application with web access**.

2. **Mobile requirements:**
   - All core user flows must be fully operable on a mobile screen width of 375 density‑independent pixels or less
   - The layout shall adapt to any width between 320 and 450 dp without horizontal scrolling

3. **Web requirements:**
   - The desktop version shall use a centered container with a maximum width of 1200 pixels
   - The desktop version may use multi‑column layouts where appropriate
   - Web screens shall support the same core workflows as mobile, with more room for analysis and reporting

4. **Offline capability:** The mobile application shall support draft or offline‑tolerant transaction entry. A poor connection shall not prevent logging.

### Section 2. Target Users

1. The System is designed exclusively for Filipino working young adults aged twenty to forty years inclusive, who live or work in Metro Manila.

2. Employment requirements (user selects from):
   - Full‑time (Regular / Permanent employee)
   - Part‑time employee
   - Self‑employed / Freelancer
   - Contractual / Project‑based employee
   - Business owner / Entrepreneur
   - Gig economy worker
   - Other (with text field)

### Section 3. Confirmed Screens

The System shall implement the following primary screens:

1. Login / Register
2. Onboarding questionnaire
3. Profile result / financial behavioral profile
4. Dashboard / overview
5. Add transaction
6. Transactions list / history
7. Recurring transactions
8. Categories / category settings
9. Budget setup
10. Budget recommendation
11. Forecast dashboard
12. Alerts / anomaly review
13. Savings goals
14. Debt accounts
15. Reports / analytics
16. Settings / privacy / account

---

## Article II: Transaction Management

### Section 1. Input Types

1. The System shall accept financial data via two input types:

   **1.1. Manual transaction.** The user types transaction details directly into the application.

   **1.2. Recurring transaction.** The user specifies a repeating transaction pattern. The System generates the transaction automatically on scheduled dates.

2. **Manual transaction fields:**
   - Required: amount, category, date, account
   - Optional: merchant name, description

3. **Recurring transaction fields:**
   - Required: amount, category, frequency, start date, account
   - Optional: end date

4. **Transfers between accounts** use the manual input method with source and destination account selectors.

### Section 2. Transaction Types

The System shall support exactly three transaction types:

1. **Income transaction** – cash inflow (salary, freelance payment, remittance)
2. **Expense transaction** – cash outflow (groceries, rent, bills)
3. **Transfer transaction** – moves cash between accounts without changing net worth

### Section 3. Manual Transaction Processing

When a user manually enters a transaction, the System shall:

1. Validate amount > 0 PHP
2. For expenses: check for negative balance, display warning with confirmation prompt
3. Update available balance accordingly
4. Store transaction with ISO 8601 timestamp
5. Trigger downstream model updates (profile, forecasts, anomaly detection) **immediately for budget actuals; asynchronously for models within 24 hours**

### Section 4. Recurring Transaction Generation

1. Recurring transactions generate automatically at scheduled frequencies.

2. If a generated expense or transfer would cause negative balance:
   - Do not create the transaction
   - Postpone it
   - Notify the user
   - Re‑attempt on next scheduled date

3. The user may pause, edit, or delete any recurring template at any time.

### Section 5. Transaction Editing and Deletion

1. Users may edit or delete any transaction, manual or recurring.

2. **Immediate effects:**
   - Available balance recomputed immediately
   - Budget actuals updated immediately

3. **Asynchronous effects (within 24 hours):**
   - Profile classification re‑evaluated
   - Spending forecasts updated
   - Anomaly detection baselines updated

4. **User notification:** "Transaction changed. Odin will update your forecasts within 24 hours."

5. **Retention limit (RE-EVALUATED):** Users may not edit or delete transactions older than **twenty‑four months** from the transaction date. This aligns with standard financial record‑keeping practices. The researchers shall validate against BSP guidelines or DPA requirements before final submission.

### Section 6. Category Suggestions and Smart Defaults

To reduce transaction entry effort, the System shall provide:

1. Most recently used category for the same merchant (if merchant provided)
2. If no merchant history, most frequently used category from last 30 days
3. User may override any suggestion

---

## Article III: Financial Behavioral Profiles

### Section 1. Profile Taxonomy

The System shall classify each user into exactly one of four financial behavioral profiles, determined by two binary dimensions:

| Income Stability | Obligation Level | Profile |
|-----------------|------------------|---------|
| Stable (CV < 0.25) | Flexible (ratio < 0.50) | Stable‑Flexible |
| Stable (CV < 0.25) | Obligated (ratio ≥ 0.50) | Stable‑Obligated |
| Variable (CV ≥ 0.25) | Flexible (ratio < 0.50) | Variable‑Flexible |
| Variable (CV ≥ 0.25) | Obligated (ratio ≥ 0.50) | Variable‑Obligated |

### Section 2. Income Stability (CV-Based)

1. **Coefficient of Variation (CV)** = standard deviation of monthly net income ÷ mean monthly net income

2. **Classification rule:**
   - Stable if CV < 0.25
   - Variable if CV ≥ 0.25

3. **Threshold validation (RE-EVALUATED):** The 0.25 threshold is provisional. The researchers shall validate using survey data or literature. Until validation, the threshold shall be configurable via system settings.

4. **Cold‑start classification (first 7 days or <5 income transactions):** Uses onboarding questionnaire.

### Section 3. Obligation Level

1. **Obligation ratio** = total unavoidable monthly expenses ÷ total monthly income (averaged over 60 days)

2. **Classification rule:**
   - Flexible if ratio < 0.50
   - Obligated if ratio ≥ 0.50

3. **Unavoidable expenses include:** rent/mortgage, utility minimum payments, debt minimum payments, insurance premiums, government contributions (SSS, PhilHealth, Pag-IBIG), documented family support

4. **Salaried employee handling:** The System asks whether user records gross or net income. If net, mandatory contributions are already accounted for.

### Section 4. Reclassification Triggers

The System shall re‑evaluate classification when:

1. CV changes by absolute difference ≥ 0.10 sustained over 60 consecutive days
2. Obligation ratio changes by absolute difference ≥ 0.15 sustained over 60 consecutive days
3. User explicitly requests reclassification
4. 90 days have elapsed since last classification

**Important:** No automatic reclassification occurs without explicit user confirmation. The user retains full control.

### Section 5. Random Forest Classification Algorithm (RE-EVALUATED)

**Decision reversal: Continuous learning IS permitted.**

#### 5.1 Algorithm Selection and Justification

The System uses **Random Forest** for financial behavioral profile classification because:
- Handles non-linear relationships between behavioral features
- Provides built-in feature importance (SHAP values for explainability)
- Robust to outliers in financial data
- Performs well with tabular data of moderate size

#### 5.2 Forest Composition

| Parameter | Value | Justification |
|-----------|-------|---------------|
| Number of trees | 100 (minimum) | Balances accuracy and computation |
| Max depth | 10 levels | Prevents overfitting |
| Split criterion | Gini impurity | Standard for classification |
| Class weights | Balanced | Robustness against imbalance |
| Random state | 42 | Reproducibility |

#### 5.3 Feature Set (5 Behavioral Features)

The classifier uses **exactly five** features derived from transaction history. Income CV and obligation ratio are **excluded** from the feature set (they serve only as label generators for synthetic training and reclassification triggers).

| Feature | Definition | Time Window | Type |
|---------|-----------|-------------|------|
| Income frequency | Number of income transactions | 30 days | Integer |
| Income amount variance | Mean absolute deviation of income amounts | 90 days | Continuous |
| Fixed expense count | Number of distinct payees with active recurring templates | Current | Integer |
| Savings rate | Financial Allocation expenses ÷ total income | 30 days | Continuous |
| Transaction regularity score | Shannon entropy of inter-transaction intervals | 60 days | Continuous |

#### 5.4 Training Data (RE-EVALUATED)

**Primary source:** Synthetic data generated from BSP Consumer Finance Survey 2021 and PSA Family Income and Expenditure Survey, with equal representation of all four profiles.

**Secondary source (if needed):** Pre‑survey of 50-100 Filipino working young adults to validate synthetic distributions.

**Continuous learning (RE-EVALUATED - PREDECENCE CHANGE):** The Random Forest classifier **SHALL** be periodically retrained on accumulated transaction history with explicit user consent. Retraining shall occur monthly using a sliding window of the most recent 365 days. The user may opt out of personalised retraining and continue using the pre‑trained synthetic model.

> **Rationale for reversal:** Freezing models on synthetic data alone ignores the PRD's requirement that "forecasts improve as the user logs more transactions" (User Story 53) and "the app becomes more personalized over time." Continuous learning with explicit consent preserves privacy while enabling personalization.

#### 5.5 Explainability with SHAP

For each classification prediction:
- Compute SHAP values across the 5 behavioral features
- Identify the 2 features with largest absolute SHAP values
- Generate plain‑language explanation via template

Example: *"Your profile is Variable‑Obligated mainly because your income amount varies significantly from month to month, and you have a high number of recurring fixed obligations."*

The explanation is accessible via a **"Why?"** button on the profile screen.

#### 5.6 Accuracy Target

| Metric | Target | Evaluation Method |
|--------|--------|-------------------|
| Accuracy | ≥ 0.85 | Holdout test set (synthetic) |
| Precision (macro) | ≥ 0.80 | Walk‑forward validation |
| Recall (macro) | ≥ 0.80 | Walk‑forward validation |
| F1 (macro) | ≥ 0.80 | Walk‑forward validation |

#### 5.7 Remediation Sequence (if accuracy < 0.85)

1. Review and revise synthetic data generation parameters
2. Conduct hyperparameter search (n_estimators, max_depth, min_samples_split)
3. If still below threshold, document achieved accuracy and analyse responsible feature/profile pair

> **Prohibited:** Reintroducing income CV or obligation ratio into the feature set (would create circularity).

---

## Article IV: Expense Categories (PCOICOP-Based)

### Section 1. Base Categories and Broad Groups

The System uses the 2020 Philippine COICOP, cross‑validated with BSP Consumer Finance Survey 2021.

| Base Category | Broad Group |
|---------------|-------------|
| Food and Non‑Alcoholic Beverages | Essentials |
| Alcoholic Beverages, Tobacco and Narcotics | Discretionary |
| Clothing and Footwear | Discretionary |
| Housing (actual rent) | Obligatory |
| Housing (utilities: water, electricity, gas) | Essentials |
| Housing (maintenance) | Discretionary |
| Furnishings, Household Equipment | Discretionary |
| Health | Essentials |
| Transport (essential commuting) | Obligatory |
| Transport (non‑essential) | Discretionary |
| Information and Communication (services) | Obligatory |
| Information and Communication (devices) | Discretionary |
| Recreation, Sport and Culture | Discretionary |
| Education Services | Obligatory |
| Restaurants and Accommodation | Discretionary |
| Insurance (premiums) | Obligatory |
| Financial Services (fees) | Discretionary |
| Personal Care | Discretionary |

### Section 2. Filipino‑Context Categories

The taxonomy explicitly includes:

1. Family support and remittances
2. Paluwagan (informal rotating savings)
3. Church or religious donations
4. Barangay or community collections
5. Government contributions (SSS, PhilHealth, Pag-IBIG)
6. Debt payments
7. Insurance
8. Emergency fund
9. Savings and investments

### Section 3. Protected Categories

1. **Default protected categories:** Essentials, debt repayments, insurance, emergency fund contributions
2. User may declare additional protected categories during onboarding or via settings
3. **Budget recommendations must not suggest reducing protected categories** unless the user explicitly changes protection settings

### Section 4. Category Customization

1. Users may create up to 5 custom subcategories under any base category
2. Each custom subcategory must map to exactly one base category and one broad group
3. Users may delete custom subcategories but not base categories
4. The System does not perform automatic categorisation (user selects at transaction entry time)

---

## Article V: Financial Flows and Accounts

### Section 1. Available Balance

Available balance for a given account is defined as:

```
Starting balance
+ Sum of all income transactions
- Sum of all expense transactions
- Sum of all savings contributions
- Sum of all debt payments
```

The System permits negative available balances with:
- Warning before transaction confirmation
- Persistent warning badge on dashboard until balance returns to ≥ 0

### Section 2. Accounts

1. The System supports up to 10 user‑defined accounts
2. Default account named "Cash"
3. Transfers associate with both source and destination accounts
4. At least one account must exist at all times

### Section 3. Currency

All amounts stored in Philippine pesos as integer centavos (e.g., 100.00 PHP = 10000 centavos) to avoid floating‑point errors.

---

## Article VI: Budgeting Module

### Section 1. Budget Structure

Every budget consists of:
- Total budget size (sum of all category allocations)
- Budget period (7, 14, 30, or 90 days, user‑selectable)
- Per‑category allocation (PHP)
- Per‑category actual spending
- Surplus/deficit (allocated minus actual)

### Section 2. Recommended Budget Period by Profile

| Profile | Recommended Period | Justification |
|---------|-------------------|---------------|
| Stable‑Flexible | 30 days | Monthly salary cycle |
| Stable‑Obligated | 30 days | Monthly obligations align |
| Variable‑Flexible | 14 days | Shorter horizon reduces forecast error |
| Variable‑Obligated | 14 days | Shorter horizon reduces forecast error |

User may override at any time.

### Section 3. Budgeting Strategy Templates

| Strategy | Description | Recommended For |
|----------|-------------|-----------------|
| 50‑30‑20 | 50% Needs (Essentials+Obligatory), 30% Wants (Discretionary), 20% Financial Allocation | Stable income |
| Zero‑Based | Every peso assigned; no unallocated buffer | Variable income, detailed trackers |
| Savings‑First | Savings deducted first as hard constraint | Users prioritising savings |
| Custom | User manually defines percentages | Advanced users |

### Section 4. Linear Programming for Budget Allocation (RE-EVALUATED)

**Decision clarification:** LP is a mathematical optimisation method, not a machine learning algorithm. It is appropriate for budget allocation because the problem (maximise user priorities subject to constraints) is inherently linear.

#### 4.1 Objective Function

Maximise: Σ (priority_weight_category × allocated_amount_category)

Priority weights: 1 (lowest) to 5 (highest)

#### 4.2 Default Priorities by Profile

| Profile | Highest (5) | Medium (4) | Low (3) |
|---------|-------------|------------|---------|
| Stable‑Flexible | Financial Allocation | Essentials (Food), Discretionary (Recreation) | All others |
| Stable‑Obligated | Obligatory (Housing, Debt) | Essentials (Health), Financial Allocation | All others |
| Variable‑Flexible | Financial Allocation | Essentials (all) | All others |
| Variable‑Obligated | Obligatory (Housing, Debt) | Essentials (Health) | All others |

User may adjust priorities at any time.

#### 4.3 Constraints (Hard)

| Constraint | Formula | Relaxable? |
|------------|---------|------------|
| Total budget | Σ allocations = forecast_income × (1 - savings_rate) | No |
| Obligatory minimum | Σ obligatory ≥ sum of all fixed obligations | No |
| Financial Allocation minimum | Σ financial_allocation ≥ forecast_income × savings_rate | Yes (Step 1) |
| Essentials floor (non-50-30-20) | Σ essentials ≥ 30% of total budget | Yes (Step 2) |
| Needs floor (50-30-20 only) | Σ essentials + obligatory ≥ 50% of total budget | Yes (Step 2) |
| Discretionary cap | Σ discretionary ≤ 30% of total budget | No |
| Per‑category max | allocation ≤ 90th percentile historical (or default if insufficient history) | No |
| Non‑negativity | All allocations ≥ 0 | No |

#### 4.4 Infeasibility Handling (Sequential Relaxation)

**Step 1:** Reduce savings constraint to 0  
**Step 2:** Reduce floor constraints progressively (50%→40%→30%→20%→0 for Needs floor; 30%→20%→10%→0 for Essentials floor)  
**Step 3:** Remove all floor constraints  
**Step 4:** If still infeasible (impossible with only Obligatory minimum), display: *"Your fixed obligations exceed your income. Odin recommends debt restructuring or increasing income before a feasible budget can be created."*

### Section 5. Surplus Handling

At end of budget period, user selects one of three strategies:

| Strategy | Behavior | Default Profile |
|----------|----------|-----------------|
| Rollover | Added to next period's budget | Stable‑Flexible, Stable‑Obligated |
| Save | Transferred to primary savings goal | Variable‑Flexible, Variable‑Obligated |
| Reset | Returned to available balance; budget recomputed from zero | No default (user must select) |

If user does not respond within 7 days, System applies default strategy.

### Section 6. Explainability

Every budget recommendation includes plain‑language explanation stating:
- Budget period and total amount
- Forecast income and target savings
- Major constraints that shaped allocation

Example: *"Your 30‑day budget is ₱22,500. This is based on predicted income of ₱30,000 and minimum savings of ₱3,000 (10%). ₱11,250 is allocated to Essentials because this category is required to be at least 50% of your budget."*

Accessible via **"Why?"** button.

---

## Article VII: Forecasting Module (LSTM)

### Section 1. Forecasting Targets

The System generates forecasts for:

| Target | Granularity | Horizons |
|--------|-------------|----------|
| Per‑category expense (4 broad groups) | Daily, weekly, monthly | 7, 14, 30, 90 days |
| Total income | Daily, weekly, monthly | 7, 14, 30, 90 days |
| Savings balance trajectory | Daily | 180 days |
| Debt remaining balance | Daily | Until projected payoff |

**Disclaimer displayed prominently:** *"Forecasts are inferential and informational only, based on your past spending and current budget. Actual future spending may differ."*

### Section 2. LSTM Architecture (RE-EVALUATED)

**Decision reversal: Continuous learning IS permitted with safeguards.**

#### 2.1 Architecture Specifications

| Component | Specification |
|-----------|---------------|
| Input sequence length | 60 days of daily data |
| LSTM layer 1 | 64 units |
| LSTM layer 2 | 32 units |
| Dropout | 0.2 after each LSTM layer |
| Output layer | Linear (regression) |
| Loss function | Huber loss (delta=1.0) - less sensitive to outliers |
| Optimizer | Adam (learning rate=0.001) |
| Batch size | 32 |
| Epochs | Up to 100 with early stopping (patience=10) |

#### 2.2 Input Features

- Daily amounts for 4 broad groups (Essentials, Obligatory, Discretionary, Financial Allocation)
- Total daily spending
- User's income amount
- User's financial behavioral profile label
- Calendar features: day of week (0-6), day of month (1-31)
- Event flags: payday, declared holiday, 13th month period, Christmas period

#### 2.3 Training Approach (RE-EVALUATED)

**Pre‑training (before user data):**
- Train on synthetic data from BSP CFS 2021 and PSA FIES
- Establish baseline performance

**Continuous learning (after deployment) - PRD TAKES PRECEDENCE:**
- The LSTM model **SHALL** be retrained weekly on each user's accumulated transaction history
- Retraining uses a sliding window of the most recent 90 days
- **Explicit user consent required** (separate opt‑in during onboarding)
- User may opt out of personalisation and continue using the pre‑trained model
- **Privacy safeguard:** Raw transaction data never leaves device for training; only aggregated features used for server‑side personalisation

> **Rationale for reversal:** The PRD explicitly states (User Story 53): "As a user, I want forecasts to improve as I log more transactions, so that the app becomes more personalized over time." Freezing the model on synthetic data directly contradicts this requirement. Continuous learning with explicit consent preserves privacy while enabling personalisation.

#### 2.4 Cold‑Start Fallback (First 30 days)

For users with <30 days of history:
- Expense forecasts: FIES category means stratified by income quintile
- Income forecasts: BSP CFS median income by occupation category
- Savings trajectory: Linear contribution of 5% of monthly income
- Debt payoff: User‑entered terms (no population data)

When user accumulates 30 days of history, System automatically switches to LSTM forecasts and displays notification.

#### 2.5 Explainability (Feature Perturbation)

For each forecast:
- Measure how prediction changes when each input feature is shuffled or set to baseline
- Feature causing largest change is most influential
- Generate template sentence: *"Your Discretionary spending is predicted to increase because your spending in the last 7 days is ₱850 higher than your 30‑day average."*

### Section 3. Evaluation Metrics (RE-EVALUATED)

| Metric | Formula | Acceptable Threshold |
|--------|---------|---------------------|
| MAE (Mean Absolute Error) | Σ\|forecast - actual\|/n | <15% of category mean (Essentials, Discretionary) |
| RMSE (Root Mean Square Error) | √(Σ(forecast - actual)²/n) | <20% of category mean (Essentials, Discretionary) |
| sMAPE | (200/n) Σ\|forecast - actual\|/(\|forecast\|+\|actual\|) | <25% (Essentials, Discretionary); <30% (Obligatory, Financial Allocation) |
| IoF (Improvement over Fallback) | (MAE_fallback - MAE_LSTM)/MAE_fallback | ≥20% target (log if <20% after 30 days) |
| Forecast Bias | mean(forecast - actual)/mean(actual) | [-0.10, 0.10] |

**Remedial action:** If any metric exceeds threshold for 3 consecutive weeks, log issue and consider retraining with different hyperparameters.

---

## Article VIII: Anomaly Detection (Isolation Forest)

### Section 1. Algorithm Overview

The System uses **Isolation Forest** for unsupervised anomaly detection, operating on a per‑user basis.

**Minimum history required:** 14 days of transaction history before Isolation Forest is enabled. For users with <14 days, only rule‑based budget overspending alerts are shown.

### Section 2. Isolation Forest Specifications

| Parameter | Value |
|-----------|-------|
| Number of estimators | 100 |
| Max samples per tree | 256 (or total transactions if fewer) |
| Random state | 42 |
| Contamination | Not fixed; dynamic threshold = top 5% of anomaly scores |

### Section 3. Feature Vector (8 Dimensions)

| Feature | Calculation | Interpretation |
|---------|-------------|----------------|
| Amount deviation | (amount - category_30d_median) / category_30d_IQR, capped ±5 | How unusual amount is for this category |
| Day‑of‑period proportion | transaction_date_days_into_period / period_total_days | Position within budget period |
| Category velocity | # transactions in category in last 7 days | Spending frequency |
| Time since last transaction (same category) | Hours, capped at 168 | Unusually long/short gaps |
| Day of week | 0-6 (Monday to Sunday) | Weekend vs weekday patterns |
| Week of month | 1-5 | Monthly bill cycles |
| Holiday proximity | 1 if within ±3 days of holiday, else 0 | Expected spikes around holidays |
| Merchant novelty | 1 if merchant not seen in last 60 days, else 0 | New merchants more likely anomalous |

### Section 4. Cultural Exclusions (RE-EVALUATED - ADDED)

Transactions during the following periods **shall NOT trigger anomaly alerts** (but may show informational notifications):

| Period | Dates | Notes |
|--------|-------|-------|
| Christmas/New Year | December 15 - January 5 | Culturally expected spending |
| Holy Week | Palm Sunday to Easter Sunday | Computed algorithmically (Anonymous Gregorian) as fallback |
| Barangay fiesta | User‑declared dates ±3 days | User configurable in profile settings |
| Whitelisted transactions | User‑approved | Merchant + category + amount tolerance (±25%) |

The user may configure whether informational alerts are shown.

### Section 5. Whitelist

When a transaction is flagged as anomalous, the user may select:

1. **"Yes, expected"** → Add to whitelist (merchant + category + ±25% tolerance, or "always allow")
2. **"No, unexpected"** → Remains flagged; no whitelist entry
3. **"Remind me later"** → Dismissed; no whitelist entry; future similar may still trigger

User may view, edit, or delete whitelist entries in Settings.

### Section 6. Rule‑Based Overspending Detection (Mandatory)

Independent of Isolation Forest:

| Condition | Alert Type |
|-----------|------------|
| Category exceeds 80% of budget with >25% of period remaining | Warning |
| Category exceeds 100% of budget at any time | Critical alert |

These alerts are **mandatory** and cannot be disabled (user may configure delivery method).

### Section 7. Alert Fatigue Prevention

| Mechanism | Specification |
|-----------|---------------|
| Cooldown | Max 3 anomaly alerts per user per 24 hours |
| Bundling | Multiple anomalies within 2 hours bundled into single notification |
| Snooze | User may snooze all anomaly alerts for 7 days |

### Section 8. Explainability

For each anomaly alert, compute deviation of each continuous feature from baseline. Present feature with largest standardised deviation.

Examples:
- *"This transaction was flagged because the amount (₱5,000) is 2.5 standard deviations above your usual Food spending of ₱800."*
- *"This transaction was flagged because you have never spent at this merchant before in the last 60 days."*

### Section 9. Evaluation Metrics

| Metric | Target | Method |
|--------|--------|--------|
| Precision | ≥ 0.70 | Walk‑forward validation on synthetic data with injected anomalies (~5%) |
| Recall | ≥ 0.65 | Walk‑forward validation |
| F1 | ≥ 0.675 | Harmonic mean |
| False positive rate | ≤ 1.5 per week | Per user per week |

---

## Article IX: Savings Goal Management

### Section 1. Savings Goal Structure

Each goal contains:

| Field | Constraints |
|-------|-------------|
| Goal name | ≤50 chars, unique per user |
| Target amount | ₱100 - ₱10,000,000 |
| Target date | ≥7 days from creation, ≤10 years |
| Contribution amount | ≥₱10 per contribution |
| Contribution frequency | Daily, weekly, bi‑weekly, monthly |
| Linked source account | Default: primary cash account |
| Priority rank | User‑assignable (drag‑and‑drop) |

### Section 2. Multiple Concurrent Goals

1. System supports up to 5 concurrent savings goals per user
2. User prioritises goals via drag‑and‑drop
3. Contributions processed in priority order each contribution cycle (daily)

### Section 3. Contribution Allocation Strategies (RE-EVALUATED - CLARIFIED)

| Strategy | Allocation Rule | Default Profile |
|----------|----------------|-----------------|
| Goal‑based | Surplus to highest‑priority goal first | All profiles (default) |
| Snowball | Surplus to goal with smallest remaining amount | Alternative for Variable‑Flexible |
| Avalanche | Surplus to goal with highest user‑ranked priority | Alternative for Stable‑Obligated |

User may switch strategies at any time via Savings → Strategy.

**When a budget strategy includes a Financial Allocation portion (e.g., 20% in 50/30/20), Odin distributes that portion across active savings goals according to the selected savings goal allocation strategy.**

### Section 4. Progress State

| State | Condition | Color |
|-------|-----------|-------|
| Ahead | Actual ≥ 1.10 × required contribution | Green |
| On track | 0.90 - 1.10 × required contribution | Green |
| Behind | 0.50 - 0.90 × required contribution | Yellow |
| Critical | < 0.50 × required contribution | Red |

### Section 5. Notifications

- Milestone: 25%, 50%, 75% progress
- Behind schedule: 7 consecutive days in "behind" state (repeats every 7 days until resolved)
- Achievement: Goal reached

---

## Article X: Debt Management

### Section 1. Debt Account Structure

| Field | Constraints |
|-------|-------------|
| Debt name | ≤50 chars, unique per user |
| Principal | ₱100 - ₱10,000,000 |
| Annual interest rate | 0.00 - 1.00 (simple interest assumption) |
| Minimum monthly payment | ≥₱0 |
| Payment due day | 1-31 (last day of month if > days in month) |
| Remaining balance | Computed: principal - sum of payments |

### Section 2. Payoff Strategies

| Strategy | Allocation Rule | Outcome |
|----------|----------------|---------|
| Avalanche | Surplus to debt with highest interest rate | Minimises total interest |
| Snowball | Surplus to debt with smallest remaining balance | Minimises time to first payoff |

User may compare strategies and switch at any time. When switching, System recalculates projections and displays comparison message.

### Section 3. Hardship Mode

Automatically detected when available balance < sum of all minimum payments for the month.

System displays:
1. Warning that minimum payments exceed available balance
2. Creditor contact information (if provided)
3. Link to National Credit Council debt counselling (if available)

### Section 4. Alerts

- Upcoming due date reminder (3 days before)
- Missed payment alert (day after due date)
- Milestone: 50% paid
- Payoff notification

---

## Article XI: Explainability (Cross-Module)

| Module | Method | User‑Facing Format |
|--------|--------|---------------------|
| Random Forest (Profile) | SHAP values, top 2 features | Template sentence |
| Linear Programming (Budget) | Active constraints listing | Template + constraint list |
| LSTM (Forecast) | Feature perturbation | Template sentence based on observable patterns |
| Isolation Forest (Anomaly) | Feature deviation from baseline | Template sentence with numerical comparison |

All explanation outputs stored in application log for audit purposes, retained for 30 days, then anonymised.

---

## Article XII: Data Privacy, Security, and Ethical Compliance (RA 10173)

### Section 1. Consent

**Explicit opt‑in screen** before transaction entry:

> *"Odin collects and processes your financial transactions to provide budget recommendations, spending forecasts, anomaly detection, and profile classification. Your data is stored encrypted and is not shared with third parties. You may delete your data at any time."*

User must tap "I agree" to proceed.

### Section 2. Data Retention (RE-EVALUATED)

**Retention period:** 24 months from date of user's last activity (login, transaction, or budget change).

After 24 months of inactivity:
- User identifier replaced with random non‑reversible token
- Transaction amounts rounded to nearest ₱100
- Transaction dates truncated to month only
- All merchant names and descriptions deleted

If user has not given explicit opt‑in for anonymised research use, data is permanently deleted instead.

### Section 3. Data Portability and Deletion

- **Export:** CSV download of all transactions via Settings → Export Data (generated within 5 minutes, secure link expires in 24 hours)
- **Deletion:** Settings → Delete Account (confirmation required, immediate local deletion, server deletion within 7 days with email confirmation)

### Section 4. Security Controls

| Layer | Control |
|-------|---------|
| In‑transit | TLS 1.3 minimum (NIST SP 800‑52) |
| At‑rest (server) | AES‑256‑GCM (FIPS 197) |
| Local storage | SQLCipher with 256‑bit key from 6‑digit PIN or biometric |
| Key derivation | PBKDF2, 100,000 iterations |
| Authentication | 6‑digit PIN + optional biometric; lock after 5 failed attempts (30s cooldown) |
| Pseudonymisation | SHA‑256 of user identifier with device‑local salt (server cannot reverse) |

### Section 5. Ethical Declaration (CRITICAL - RE-EVALUATED)

**Original Specification stated:** *"For the duration of this thesis, all machine learning models remain frozen on their synthetic‑data pre‑training. No real user data—whether from pilot users, evaluation participants, or any other source—is used for model training, fine‑tuning, or weight updates of any kind."*

**This is REVERSED per PRD precedence.** The correct ethical declaration is:

> *"For the duration of this thesis, all machine learning models are pre‑trained on synthetic data. With explicit user consent, models may be personalised using each user's own transaction data through continuous learning (weekly retraining on a sliding window of 90 days). No user data is shared between users. Raw transaction data never leaves the device for training purposes; only aggregated features are used for server‑side personalisation. Users may opt out of personalisation at any time and continue using the pre‑trained synthetic model."*

**Research use opt‑in (separate):** User may allow anonymised data (stripped of identifiers, amounts rounded, dates truncated to month) to improve models for all users. May withdraw consent at any time.

### Section 6. Disclaimers

Displayed on first launch (user must scroll and tap "I understand"):

> *"Odin's predictions and recommendations are for informational purposes only. You retain full responsibility for all financial decisions. Odin is not a financial advisor. Do not make major financial decisions solely based on automated outputs."*

---

## Article XIII: System and Algorithm Evaluation (ISO/IEC 25010)

### Section 1. Quality Characteristics

| Characteristic | Measure | Threshold | Method |
|----------------|---------|-----------|--------|
| Functional suitability | % features passing manual tests | ≥98% | 50 test cases mapped to requirements |
| Performance efficiency | 95th percentile response time | Non‑ML: ≤500ms; ML: ≤1500ms | Automated load testing (100 iterations) |
| Usability | SUS score | ≥68 (stretch: ≥74) | 30 participants, 14 days active use |
| Reliability | Mean time between failures | ≥4 hours | 2 hours simulated continuous use |
| Security | Critical vulnerabilities (OWASP Top 10) | 0 | Static analysis + basic penetration test |
| Maintainability | Cyclomatic complexity per function | ≤10 (excluding UI binding, 3rd-party libs) | SonarQube static analysis |

### Section 2. System Usability Scale (SUS)

- **Sample size:** 30 participants
- **Stratification:** Minimum 6 per financial behavioural profile (4 × 6 = 24) + 6 any profile
- **Recruitment:** At least 4 different Metro Manila cities
- **Active use:** At least 10 transactions over 14 days
- **Scoring:** Standard Brooke (1996) method, 0-100 scale

### Section 3. Algorithm Evaluation (Walk‑Forward Validation on Synthetic Data)

#### Random Forest (Classification)

| Parameter | Value |
|-----------|-------|
| Validation method | Rolling window: 60 days train, 30 days test, roll 30 days, 6 iterations |
| Primary metrics | Accuracy, precision, recall, F1 (per class + macro) |
| Target | Accuracy ≥ 0.85 |

#### LSTM (Forecasting)

| Parameter | Value |
|-----------|-------|
| Validation method | Walk‑forward: 60 days train, 7 days test, roll 7 days, 26 iterations |
| Primary metrics | MAE (% of category mean), RMSE (%), sMAPE (%), IoF (%), Forecast bias |
| Targets | MAE <15% (Essentials, Discretionary); sMAPE <25% (Essentials, Discretionary), <30% (Obligatory, Financial Allocation) |

#### Isolation Forest (Anomaly Detection)

| Parameter | Value |
|-----------|-------|
| Validation method | Walk‑forward: 30 days train, 7 days test, roll 7 days, 13 iterations |
| Synthetic anomalies | ~5% of transactions, ≥2 standard deviations above category mean |
| Targets | Precision ≥0.70, Recall ≥0.65, F1 ≥0.675, FPR ≤1.5/week |

### Section 4. Failure Conditions

| Condition | Detection | Response |
|-----------|-----------|----------|
| LSTM MAE exceeds threshold | >20% of category mean for 14 consecutive days (synthetic evaluation) | Log warning; researchers may retrain offline |
| Isolation Forest F1 < 0.6 | 7 consecutive days (synthetic evaluation) | Log warning; continue using IF |
| Random Forest accuracy < 0.80 | During development retraining | Do not deploy; retain previous model |
| Unhandled runtime exception | Any module throws exception | Catch, log, graceful degradation with fallback message |

---

## Article XIV: Scope and Delimitations (Out of Scope)

The following are explicitly excluded from the thesis version:

1. Bank or e‑wallet API integration
2. OCR receipt scanning
3. CSV or spreadsheet import
4. Automatic transaction import
5. Investment portfolio tracking (stocks, mutual funds, crypto)
6. Multi‑currency support
7. Licensed financial, investment, retirement, or tax advice
8. Automated bill payment
9. Credit score monitoring
10. Users outside Metro Manila (for thesis validation)
11. Users outside Filipino working young adult demographic
12. Full production‑grade fraud detection
13. Merchant‑level enrichment from third‑party providers
14. Dedicated paluwagan module (users may approximate via custom subcategory)
15. Credit card accounts (users record payments as expenses)
16. Compound interest for revolving debt (simple interest only)
17. Admin dashboards for banks or financial advisers
18. Social or gamified features
19. Public marketplace deployment beyond thesis evaluation

---

## Article XV: Development Phases for Models & Algorithms

Based on this merged specification, the following development plan is recommended:

### Phase 1: Preparation (2 weeks)

| Activity | Deliverables |
|----------|--------------|
| Finalise synthetic data generation parameters | Python script (Appendix D) |
| Define feature distributions per profile for RF training | Configuration file |
| Define spending patterns per broad group for LSTM pre‑training | Configuration file |
| Define anomaly injection rules for IF validation | Configuration file |
| Set up version control for model code | GitHub repository |
| Literature review completion (12 topics, RRL chapter) | RRL chapter draft |

### Phase 2: Synthetic Data Generation (2 weeks)

| Activity | Deliverables |
|----------|--------------|
| Generate synthetic user population (BSP CFS 2021 + PSA FIES) | Synthetic dataset (users + transactions) |
| Generate labelled profiles for RF training | Labelled dataset (4 profiles × equal representation) |
| Generate time‑series data for LSTM pre‑training | Daily aggregated spending per broad group |
| Generate anomaly‑injected test set for IF | Test set with known anomaly labels (~5%) |
| Validate synthetic distributions against real survey data | Validation report |

### Phase 3: Algorithm Prototyping (4 weeks)

**Week 1-2: Random Forest (Profile Classification)**
- Implement RF with 5 features per Article III Section 5.3
- Train on synthetic labelled data
- Implement SHAP explainability
- Walk‑forward validation (60/30 day rolling window, 6 iterations)
- **Success criteria:** Accuracy ≥ 0.85

**Week 2-3: LSTM (Forecasting)**
- Implement architecture per Article VII Section 2.1
- Pre‑train on synthetic daily aggregated data
- Implement feature perturbation explainability
- Walk‑forward validation (60/7 day rolling window, 26 iterations)
- **Success criteria:** MAE <15% (Essentials, Discretionary); sMAPE <25%/<30%

**Week 3-4: Isolation Forest (Anomaly Detection)**
- Implement IF with 8 features per Article VIII Section 3
- Implement dynamic threshold (top 5% of scores)
- Implement cultural exclusions and whitelist logic
- Walk‑forward validation (30/7 day rolling window, 13 iterations) on injected anomalies
- **Success criteria:** Precision ≥0.70, Recall ≥0.65, F1 ≥0.675

**Week 4: Linear Programming (Budget Recommendation)**
- Implement LP solver with constraints per Article VI Section 4.3
- Implement infeasibility handling (sequential relaxation)
- Implement explainability (constraint listing)
- Test with synthetic user profiles
- **Success criteria:** Adherence rate ≥70% in simulation

### Phase 4: System Development (8 weeks, 4 sprints)

| Sprint | Focus |
|--------|-------|
| Sprint 1 | Backend: Transaction ledger, category taxonomy, account management, authentication |
| Sprint 2 | Backend: Budget LP, savings goals, debt management, alerts |
| Sprint 3 | Model integration: RF (profile), LSTM (forecast), IF (anomaly) as services |
| Sprint 4 | Frontend: All 16 screens, offline support, exports |

### Phase 5: Internal Testing (2 weeks)

| Activity | Deliverables |
|----------|--------------|
| Execute 50 test cases (functional suitability) | Traceability matrix |
| Load testing (100 iterations per operation) | Performance report |
| Security testing (static analysis + basic pen test) | Security report |
| Code quality (cyclomatic complexity) | SonarQube report |

### Phase 6: User Evaluation (3 weeks)

| Activity | Deliverables |
|----------|--------------|
| Ethics clearance (UMak Research Ethics Committee) | Approval letter |
| Recruit 30 participants (stratified by profile, ≥4 Metro Manila cities) | Participant log |
| 14 days active use (monitor transaction count) | Usage logs |
| SUS administration after 14 days | SUS scores (target ≥68) |
| Thematic analysis of feedback | Qualitative findings |
| Model inference on real user data (frozen for evaluation) | Performance report |

### Phase 7: Thesis Writing and Revision (6 weeks)

| Activity | Deliverables |
|----------|--------------|
| Introduction and RRL chapters | Draft complete |
| Methodology chapter | Draft complete |
| Results (model metrics, SUS, ISO 25010) | Draft complete |
| Discussion and conclusions | Draft complete |
| Revisions based on adviser feedback | Final manuscript |

### Phase 8: Final Defense Preparation (2 weeks)

| Activity | Deliverables |
|----------|--------------|
| Presentation slides | Slides deck |
| Live demo script | Demo recording |
| Appendix finalisation (A-I) | Complete appendices |

---

## Appendix: Decisions Re-Evaluated and Changed

| Original Decision | Re-Evaluated Decision | Rationale (PRD precedence) |
|-------------------|----------------------|---------------------------|
| Models frozen on synthetic data; no user data for training | Continuous learning with explicit consent (weekly retraining on user's own data, sliding 90-day window) | PRD User Story 53: "forecasts improve as user logs more transactions"; "app becomes more personalized over time" |
| 13-month retention limit | 24-month retention limit | Aligns with standard financial record‑keeping; provisional, requires validation against BSP/DPA |
| No savings goal priority table or Snowball/Avalanche strategies | Priority table with Snowball and Avalanche allocation strategies | PRD User Story 64 explicitly requires this |
| Forecast horizons: 7, 30, 90 days | Forecast horizons: 7, 14, 30, 90 days (added 14-day) | PRD default for Variable profiles |
| No mention of offline support | Offline-tolerant transaction entry | PRD User Story 80 explicitly requires this |
| No mention of savings goal distribution from budget allocation | Budget's Financial Allocation portion distributed across savings goals per selected strategy | PRD Implementation Decisions explicitly states this |

---

This merged specification is now internally consistent, prioritises the PRD where conflicts exist, and provides a clear development plan for the model and algorithm work.