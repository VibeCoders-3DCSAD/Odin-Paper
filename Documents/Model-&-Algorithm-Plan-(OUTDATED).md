# Model & Algorithm Plan

---

## Preface

This guide covers the full development lifecycle — planning, data design, development, testing, evaluation, and integration — for each of Odin's four core modules. It is derived directly from the BIBLE.md system specification and is intended as the authoritative implementation reference for Team Aesir.

Three constraints apply uniformly across all four modules and are stated here once to avoid repetition.

**No real user data for training.** All ML models are pre-trained exclusively on synthetic data derived from the BSP Consumer Finance Survey 2021 and the PSA Family Income and Expenditure Survey. Models are frozen before any pilot user data is collected. This is both an ethical protocol requirement and a scoping decision for Thesis 1.

**Models are hosted on the cloud, not on-device.** Inference requests are made from the mobile application to a cloud endpoint (AWS Lambda or Google Cloud Run). The mobile app caches the most recent results for each module. No ML inference executes on the device.

**All amounts are stored as integer centavos (PHP).** For example, ₱100.00 is stored as `10000`. All feature computation involving peso amounts must account for this representation.

---

## Module 1: Financial Behavioral Profile (FBP) Classification

**Algorithm:** Random Forest  
**Purpose:** Classify each user into one of four behavioral profiles — Stable-Flexible, Stable-Obligated, Variable-Flexible, Variable-Obligated — based on two dimensions: income stability and obligation level. The profile label is consumed downstream by the LSTM forecasting module, the LP budget recommendation module, and the Isolation Forest anomaly detection module.

---

### Phase 1: Planning

#### 1.1 Profile Taxonomy

The four profiles arise from the cross-product of two binary dimensions.

- **Income stability** is determined by the coefficient of variation (CV) of monthly net income over the preceding 90 days. A user is **Stable** if CV < 0.25, and **Variable** if CV ≥ 0.25.
- **Obligation level** is determined by the obligation ratio (OR): total unavoidable monthly expenses divided by total monthly income, averaged over the preceding 60 days. A user is **Flexible** if OR < 0.50, and **Obligated** if OR ≥ 0.50.

> **Open Item.** Both thresholds (CV = 0.25 and OR = 0.50) are provisional. They must be validated against BSP CFS literature or survey data before final model training. Both values are stored as configurable system parameters and must not be hardcoded.

**Unavoidable expenses** for OR calculation include: rent or mortgage, utility minimum payments, debt minimum payments, insurance premiums, SSS / PhilHealth / Pag-IBIG contributions, basic communication services, and documented family support (e.g., monthly remittance to parents). For users who record net income (post-deduction salary), mandatory contributions are already embedded and must not be double-counted.

#### 1.2 Cold-Start Period

Classification via the Random Forest is unavailable for new users with fewer than 30 days of history or fewer than 5 income transactions (whichever is longer). During this cold-start period, the system uses onboarding questionnaire responses to assign an initial provisional profile. The questionnaire maps as follows:

- Income variance question → estimated CV → Stable or Variable
- Obligation percentage question (≥ 50% → Obligated, < 50% → Flexible)

The initial questionnaire-derived profile is presented to the user for confirmation before they enter the main application. Once the cold-start minimum data threshold is met, the Random Forest replaces the questionnaire-derived classification.

#### 1.3 Reclassification Triggers

The system re-evaluates the profile when any of the following occur:

- CV changes by ≥ 0.10 absolute from the classification baseline, sustained over 60 consecutive days
- OR changes by ≥ 0.15 absolute from the classification baseline, sustained over 60 consecutive days
- User explicitly requests reclassification in Settings
- 90 days have elapsed since the last classification (periodic refresh)

No automatic reclassification occurs. Every reclassification recommendation is presented to the user with a SHAP-based explanation and requires explicit user confirmation. If the user does not respond within 30 days, a persistent non-dismissible dashboard notification is shown.

---

### Phase 2: Data Design and Synthetic Generation

#### 2.1 Training Data Requirements

The synthetic training dataset must satisfy the following constraints:

- **Class balance:** Equal representation of all four profiles — exactly 25% per class. The Random Forest uses `class_weight='balanced'`, but the synthetic data should also be balanced to avoid overrepresenting any single profile.
- **Feature coverage:** Each synthetic user record must have sufficient transaction history to compute all 7 features across all three time windows (30, 60, 90 days).
- **Diversity within classes:** Users within the same profile class must vary across income levels (income quintiles from BSP CFS), occupation types, and spending compositions. A classifier trained only on high-income Stable-Flexible users will generalize poorly.

#### 2.2 Synthetic Generation Procedure

Refer to `model-training-data-design.md` for the full generation specification. At minimum, the procedure must:

1. Sample income amounts from BSP CFS 2021 income distributions, stratified by occupation category.
2. Assign income stability by drawing CV from a distribution that produces approximately 50% Stable users and 50% Variable users.
3. Assign obligation ratios by sampling from category-specific spending distributions in PSA FIES 2021, ensuring 50% Flexible and 50% Obligated distribution.
4. Generate synthetic daily transaction histories of at least 90 days per user, respecting the assigned CV and OR.
5. Label each synthetic user record with the ground-truth profile based on the computed CV and OR against the provisional thresholds.

> **Note.** If the PSA FIES used for generation is older than 3 years at the time of development, amounts must be adjusted by cumulative CPI inflation using PSA inflation data.

#### 2.3 Feature Engineering

The following 7 features are computed per user from their transaction history. All features are continuous except income frequency (integer) and fixed expense count (integer).

| Feature | Definition | Windows |
|---|---|---|
| Income CV | std(monthly net income) / mean(monthly net income) | 30d, 60d, 90d |
| Obligation ratio | sum(unavoidable expenses) / sum(income) | 30d, 60d, 90d |
| Income frequency | Number of income transactions per 30 days | 30d |
| Income amount variance | Mean absolute deviation of income amounts | 30d |
| Fixed expense count | Count of distinct payees with `is_recurring = true` | 30d |
| Savings rate | savings deposits / income | 30d |
| Transaction regularity score | Shannon entropy of inter-transaction time intervals | 30d |

Each CV and OR are computed at three separate windows (30d, 60d, 90d), yielding 6 features from those two alone. The full feature vector is 7 conceptual features but expands to more columns when the multi-window variants are included. Normalize all continuous features to [0, 1] or standardize to zero mean and unit variance before training.

---

### Phase 3: Development

#### 3.1 Model Configuration

```python
from sklearn.ensemble import RandomForestClassifier

rf_model = RandomForestClassifier(
    n_estimators=100,
    max_depth=10,
    criterion='gini',
    class_weight='balanced',
    random_state=42,
    n_jobs=-1
)
```

All hyperparameters above are fixed per the BIBLE spec. The following are subject to tuning during development (documented in Appendix E of the thesis):

- `min_samples_split` (default 2)
- `min_samples_leaf` (default 1)
- `max_features` ('sqrt' recommended as starting point)

Hyperparameter tuning shall use 5-fold stratified cross-validation on the synthetic training set. Grid or random search results must be logged in Appendix E.

#### 3.2 SHAP Integration

For every classification inference, the system must compute SHAP values for explainability. Use `shap.TreeExplainer` (compatible with scikit-learn RandomForest). The top 3 features by absolute SHAP value are extracted and mapped to the user-facing explanation template.

```python
import shap

explainer = shap.TreeExplainer(rf_model)
shap_values = explainer.shap_values(feature_vector)
# shap_values is shape (n_classes, n_features)
# For the predicted class, extract top-3 by abs value
```

The explanation template:

> "Your profile is [Profile] mainly because your [Feature 1 name] of [value] [comparison to threshold], and your [Feature 2 name] of [value] [comparison]."

SHAP values are stored in the application log with a 30-day retention period, after which user identifiers are removed.

#### 3.3 Feature Extraction Pipeline

At inference time, the mobile application computes user-level aggregated statistics from the local transaction database and sends only the feature vector to the cloud endpoint. The endpoint must not receive raw transaction records. Build a dedicated feature extraction function for each feature, making it independently testable.

#### 3.4 Inference Flow

```
User transaction saved / reclassification trigger
  → compute feature vector (local, on device)
  → POST /classify { feature_vector }
  → Random Forest inference (cloud)
  → receive { profile_label, shap_values, confidence }
  → if profile_label ≠ current_profile:
      present reclassification recommendation to user with explanation
    else:
      update profile last-checked timestamp
  → profile label stored locally and synced to server
```

#### 3.5 Graceful Degradation

If the classification endpoint throws an unhandled exception at runtime, the system must catch it, log it, and display: *"Your financial profile is using saved data. Some recommendations may be less accurate."* The last successfully computed profile is retained.

---

### Phase 4: Testing

#### 4.1 Unit Tests

Write a unit test for each of the 7 feature extraction functions. Each test must cover:

- Normal case: sufficient transaction history, expected output within range
- Edge case: exactly at the minimum data threshold (5 income transactions, 30 days)
- Boundary case: CV = 0.25 exactly (must classify as Variable, not Stable)
- Boundary case: OR = 0.50 exactly (must classify as Obligated, not Flexible)
- Net vs. gross income handling: a user recording net income must not have contributions double-counted in OR

#### 4.2 Integration Tests

- Confirm that the feature vector sent to the cloud endpoint matches the format and dimensionality expected by the serialized model.
- Confirm that the SHAP explainer runs without error on a feature vector with all-zero values (cold-start edge case).
- Confirm that the reclassification trigger logic fires at the correct deltas (±0.10 CV, ±0.15 OR) and does not fire below those deltas.
- Confirm that the 60-day sustained period check prevents premature reclassification.
- Confirm graceful degradation: simulate endpoint failure and verify fallback behavior.

#### 4.3 Functional Test Cases (mapped to Article XIII)

Each of the following must appear in the 50-case ISO test script:

| Test Case | Expected Result |
|---|---|
| New user completes onboarding questionnaire | Initial profile assigned and presented for confirmation |
| User with CV = 0.10 and OR = 0.30 | Classified as Stable-Flexible |
| User with CV = 0.40 and OR = 0.60 | Classified as Variable-Obligated |
| CV changes by 0.12 over 60 days | Reclassification recommendation presented |
| CV changes by 0.08 | No reclassification recommendation |
| User declines reclassification | Profile unchanged; 30-day notification reminder scheduled |
| User does not respond for 30 days | Persistent non-dismissible notification shown |
| Endpoint unavailable | Graceful fallback message displayed, last known profile retained |

---

### Phase 5: Evaluation

Walk-forward validation protocol per BIBLE Article XIII Section 3:

- **Window:** 60 days training, 30 days test
- **Iterations:** 6 rolling steps (roll forward by 30 days each step)
- **Dataset:** Synthetic only; no real user data

**Primary metrics and acceptable thresholds:**

| Metric | Threshold |
|---|---|
| Accuracy (macro) | ≥ 0.85 |
| Precision per class | Report all four; macro-average ≥ 0.80 recommended |
| Recall per class | Report all four; macro-average ≥ 0.80 recommended |
| F1 per class | Report all four; macro-average ≥ 0.80 recommended |

**Required outputs:**

- Confusion matrix (4×4) for each of the 6 iterations, plus an aggregate confusion matrix
- Per-class precision, recall, and F1 for the aggregate
- Hyperparameter tuning grid and best configuration (Appendix E)

**Failure condition:** If accuracy on the validation set falls below 0.80 after a development-phase retraining run, the new model must not be deployed. The previous model is retained and the developer is alerted.

---

### Phase 6: Integration and Deployment

The Random Forest model is serialized (e.g., `joblib` or `pickle`) and deployed on the cloud inference endpoint. The mobile application sends the feature vector and receives the profile label and SHAP values. The profile label is stored locally and synced to the server.

The profile label is passed to three downstream modules:

- **LSTM:** Included as a categorical input feature in the input sequence
- **LP Budget Recommendation:** Determines the default priority weights per profile (per Article VI Section 4)
- **Isolation Forest:** Included as a categorical feature in the anomaly detection feature vector, enabling profile-aware baselines

When the profile changes via accepted reclassification, all three downstream modules must be notified and must update their behavior within 24 hours.

---

## Module 2: Spending Forecasting

**Algorithm:** Long Short-Term Memory (LSTM) Network  
**Purpose:** Generate forward-looking forecasts for four targets — per-category expenses (4 broad groups), total income, savings balance trajectory, and debt remaining balance — across configurable horizons and granularities. Forecast outputs feed directly into the LP budget recommendation module.

---

### Phase 1: Planning

#### 1.1 Forecast Targets and Horizons

| Target | Granularities | Horizons |
|---|---|---|
| Per-category expense (4 groups) | Daily, weekly, monthly | 7, 14, 30, 90 days |
| Total income | Daily, weekly, monthly | 7, 14, 30, 90 days |
| Savings balance trajectory | Daily | 180 days |
| Debt remaining balance | Daily (until projected payoff) | Until payoff date |

The savings trajectory forecast assumes adherence to the current budget recommendation (planned contributions, no unplanned withdrawals). The debt payoff forecast assumes adherence to the user's selected debt strategy (Avalanche or Snowball) with minimum payments and surplus allocation.

All forecast displays must include a prominent disclaimer: *"Forecasts are inferential and informational only, based on your past spending and current budget. Actual future spending may differ."*

#### 1.2 Cold-Start Fallback Logic

| History Available | Behavior |
|---|---|
| < 14 days | Rule-based overspending alerts only; LSTM and anomaly detection disabled |
| 14–29 days | Anomaly detection enabled (rule-based + IF after 14 days); LSTM still in fallback |
| 30–59 days | LSTM enabled with variable-length input (masked or padded); population fallback replaced |
| ≥ 60 days | Full LSTM with 60-day input sequence |

**Cold-start fallback sources:**
- Expense forecasts: PSA FIES category means, stratified by user's income quintile from onboarding
- Income forecasts: BSP CFS median income by occupation category from onboarding
- Savings trajectory: linear 5% monthly income contribution, no withdrawals
- Debt payoff: user-entered debt terms only; no population data needed

When the user crosses the 30-day threshold, the system automatically switches to LSTM and displays: *"Odin now has enough data to create personalised forecasts for you."*

---

### Phase 2: Data Design and Synthetic Generation

#### 2.1 Synthetic Training Data

The synthetic dataset produces daily time series of spending per broad group for a population of synthetic users. The generation process must:

1. Produce at least 6 months (180 days) of daily transaction sequences per synthetic user.
2. Respect BSP CFS category means and variability per income quintile.
3. Embed calendar effects: higher spending on paydays, reduced spending mid-month, elevated Discretionary spending in December and during Holy Week.
4. Include the 13th-month pay spike in December.
5. Embed the Christmas and New Year spending elevation (December 15 – January 5).
6. Generate sequences for all four profiles, with spending patterns that differ meaningfully by profile (e.g., Variable-Obligated users have high OR and high income volatility).

The training set and test set must be non-overlapping. The test set represents 6 months of simulated activity distinct from the training period.

#### 2.2 Input Feature Vector (per time step)

Each day in the input sequence has the following features:

| Feature | Description |
|---|---|
| `essentials_amount` | Daily total for Essentials group (centavos) |
| `obligatory_amount` | Daily total for Obligatory group |
| `discretionary_amount` | Daily total for Discretionary group |
| `financial_allocation_amount` | Daily total for Financial Allocation group |
| `total_daily_spending` | Sum of all four groups |
| `income_amount` | Daily income recorded (0 on non-income days) |
| `profile_label` | One-hot encoded profile (4 dimensions) |
| `day_of_week` | 0 (Monday) to 6 (Sunday) |
| `day_of_month` | 1 to 31 |
| `is_payday` | 1 if today is a recorded income day, else 0 |
| `is_holiday` | 1 if today is a declared Philippine public holiday |
| `is_13th_month_period` | 1 if month = December |
| `is_christmas_period` | 1 if Dec 15 – Jan 5 |

All peso-denominated features must be normalized (e.g., min-max over the training set per category, or divided by a rolling income baseline per user).

---

### Phase 3: Development

#### 3.1 Model Architecture

```python
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dropout, Dense

model = Sequential([
    LSTM(64, input_shape=(60, n_features), return_sequences=True),
    Dropout(0.2),
    LSTM(32, return_sequences=False),
    Dropout(0.2),
    Dense(n_output_targets, activation='linear')
])

model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
    loss=tf.keras.losses.Huber(delta=1.0)
)

early_stopping = tf.keras.callbacks.EarlyStopping(
    monitor='val_loss',
    patience=10,
    restore_best_weights=True
)

model.fit(
    X_train, y_train,
    batch_size=32,
    epochs=100,
    validation_split=0.15,
    callbacks=[early_stopping]
)
```

- `n_features`: number of features per time step (as defined in the feature vector above)
- `n_output_targets`: depends on training configuration; separate models may be trained per target (per-category expense, income, savings, debt), or a multi-output model may be used

> **Architecture Note.** The LSTM architecture does not include an attention layer in the thesis version. Attention-based explainability is therefore unavailable. Feature perturbation explainability is used instead.

#### 3.2 Variable-Length Input Handling (30–59 days)

For users with between 30 and 59 days of history, the input sequence is shorter than the expected 60-step window. The recommended handling strategy is **left-padding with zeros** (masking), using a Keras `Masking` layer before the first LSTM layer:

```python
from tensorflow.keras.layers import Masking

model = Sequential([
    Masking(mask_value=0.0, input_shape=(60, n_features)),
    LSTM(64, return_sequences=True),
    ...
])
```

Zero-padded days at the beginning of the sequence are masked out of the LSTM's gradient computation.

#### 3.3 Inference Endpoint

The LSTM model is hosted on AWS Lambda or Google Cloud Run with a maximum inference timeout of **2500 milliseconds**. The mobile application sends the last 60 days of daily aggregated spending and receives forecast arrays. Inference request payload must include only the feature vector — no merchant names, no detailed subcategory data, no raw transaction records.

The mobile application caches the most recent forecast for each target. When offline, cached forecasts are displayed with: *"Offline mode — forecasts from [date]."*

#### 3.4 Explainability: Feature Perturbation Method

For each forecast, determine the most influential feature by setting each input feature (across all 60 time steps) to its baseline value (global mean from training data) and measuring the change in prediction. The feature causing the largest change is identified as most influential.

Generate the explanation from a template:

- If recent spending drives the forecast: *"Your Discretionary spending is predicted to increase because your spending in the last 7 days is [amount] higher than your 30-day average."*
- If no single feature dominates: *"Your forecast is consistent with your recent spending patterns."*
- Confidence is communicated indirectly: *"Forecast for tomorrow is ₱1,200, which is within your typical daily range of ₱500 to ₱2,000."*

Raw perturbation values must not be shown to users.

#### 3.5 Graceful Degradation

If the forecasting endpoint throws an exception, display: *"Forecasts are temporarily unavailable. Please check your internet connection and try again later."* Show the most recently cached forecast if available. Do not attempt a second inference call automatically.

---

### Phase 4: Testing

#### 4.1 Unit Tests

- Feature extraction for each of the 13 input features, including cyclical day-of-week and day-of-month
- Calendar flag logic: `is_payday`, `is_holiday`, `is_christmas_period`, `is_13th_month_period`
- Cold-start fallback activation at exactly 30 days of history
- Masking: confirm that zero-padded time steps do not affect the prediction differently than varying the number of padded steps

#### 4.2 Integration Tests

- End-to-end: send a 60-day feature matrix to the deployed endpoint, confirm response shape and that all forecast values are non-negative
- Cold-start transition: simulate a user crossing from 29 to 30 days of history; confirm the switchover notification fires and the fallback is no longer used
- Offline caching: disconnect network, confirm cached forecasts are displayed with the correct label
- Timeout: simulate a response delay exceeding 2500ms; confirm the UI handles this gracefully

#### 4.3 Functional Test Cases

| Test Case | Expected Result |
|---|---|
| User with 60 days of history requests forecast | LSTM inference runs; forecast displayed with disclaimer |
| User with 25 days of history views forecast screen | FIES/BSP fallback displayed; LSTM not invoked |
| User crosses 30-day threshold | Switchover notification shown; LSTM activated |
| Network unavailable | Cached forecast displayed with date label |
| Endpoint times out | Graceful error message displayed; no crash |
| December 20 transaction | Christmas period flag = 1 in feature vector |

---

### Phase 5: Evaluation

Walk-forward validation per BIBLE Article XIII Section 3:

- **Window:** 60 days training, 7 days test
- **Iterations:** 26 rolling steps (roll forward by 7 days each step)
- **Dataset:** Synthetic only (6-month test set, distinct from training)

**Primary metrics and acceptable thresholds:**

| Metric | Essentials, Discretionary | Obligatory, Financial Allocation |
|---|---|---|
| MAE (% of category mean) | < 15% | Report only |
| RMSE (% of category mean) | < 20% | Report only |
| sMAPE | < 25% | < 30% |
| Improvement over Fallback (IoF) | ≥ 20% improvement over FIES baseline | ≥ 20% |
| Forecast bias | ∈ [−0.10, +0.10] | ∈ [−0.10, +0.10] |

**IoF formula:** `(MAE_fallback - MAE_LSTM) / MAE_fallback × 100%`

If IoF remains below 20% after 30 days of user data collection during the pilot, log a warning. No automatic retraining occurs in the thesis version.

**Failure condition:** If MAE exceeds 20% of the category mean for any broad group for 14 consecutive days during synthetic evaluation, log a developer warning. Manual offline retraining with different hyperparameters may follow.

All walk-forward validation results must be reported in tabular form in Appendix F.

---

### Phase 6: Integration and Deployment

The LSTM module receives the user's profile label from the Random Forest classifier as a feature. It passes forecast outputs to:

- **LP Budget Recommendation:** Forecasted category amounts used as the basis for total budget size and as inputs to floor/cap constraints
- **Savings Goal Tracking interface:** Savings balance trajectory displayed
- **Debt Management interface:** Debt payoff trajectory displayed

The forecasting module does not communicate directly with the Isolation Forest in the thesis version.

---

## Module 3: Budget Recommendation

**Algorithm:** Linear Programming (LP)  
**Purpose:** Generate personalized category-level budget allocations that maximize user-stated priorities subject to financial constraints. LP is not a machine learning algorithm and does not require a training phase, but it depends on outputs from both the Random Forest (for default priority weights) and the LSTM (for forecast income and category-level spending estimates).

---

### Phase 1: Planning

#### 1.1 Budget Periods

| Profile | Recommended Period | Rationale |
|---|---|---|
| Stable-Flexible | 30 days | Monthly salary cycle |
| Stable-Obligated | 30 days | Monthly obligations align with this horizon |
| Variable-Flexible | 14 days | Shorter horizon reduces forecast error for variable income |
| Variable-Obligated | 14 days | Same as Variable-Flexible |

Users may select from 7, 14, 30, or 90 days and may override the recommendation at any time.

#### 1.2 Budgeting Strategy Templates

| Strategy | Rule |
|---|---|
| 50-30-20 | 50% Essentials, 30% Discretionary, 20% Financial Allocation |
| Zero-Based | Every peso assigned; sum of all category allocations = forecast income − target savings |
| Savings-First | Target savings contribution deducted first as a hard constraint; remainder allocated across expense categories |
| Custom | User manually defines percentage allocations per broad group or per detailed category |

The Savings-First strategy is recommended for users prioritizing savings goals. The Zero-Based strategy is recommended for Variable profile users. The 50-30-20 strategy is recommended as a general starting point for Stable users.

---

### Phase 2: Development — LP Formulation

#### 2.1 Decision Variables

Let `x_i` denote the peso allocation for category `i`, where `i` ranges over all active detailed categories in the user's selected category set.

#### 2.2 Objective Function

Maximize:

```
Σ_i (priority_i × x_i)
```

Where `priority_i` ∈ {1, 2, 3, 4, 5} is the user's declared priority weight for category `i`. Default priorities per profile are defined in BIBLE Article VI Section 4 and are summarized below.

**Default priority weights by profile:**

| Profile | Priority 5 | Priority 4 | Priority 3 |
|---|---|---|---|
| Stable-Flexible | Financial Allocation | Food, Recreation | All remaining |
| Stable-Obligated | Housing, Financial Obligations (debt minimums) | Health, Financial Allocation | All remaining |
| Variable-Flexible | Financial Allocation | All of Essentials | All remaining |
| Variable-Obligated | Housing, Financial Obligations | Health | All remaining |

Users may adjust priorities at any time in Settings. The system must display: *"Higher priority categories get more budget, subject to spending caps."*

#### 2.3 Constraints

All eight constraints must be implemented. Constraints are listed in order of enforcement priority for the infeasibility relaxation procedure.

**Constraint 1 — Total budget equals income after savings:**
```
Σ_i x_i = forecast_income × (1 − target_savings_rate)
```
`target_savings_rate` defaults to 10% (0.10). Set by user.

**Constraint 2 — Obligatory floor (hard, non-relaxable):**
```
Σ_{i ∈ Obligatory} x_i ≥ Σ_j min_debt_payment_j + Σ_k insurance_premium_k
```

**Constraint 3 — Financial Allocation minimum:**
```
Σ_{i ∈ FinancialAllocation} x_i ≥ forecast_income × target_savings_rate
```
*(Relaxable — first to be relaxed during infeasibility)*

**Constraint 4 — Essentials floor:**
```
Σ_{i ∈ Essentials} x_i ≥ 0.50 × Σ_i x_i
```
*(Relaxable — reduced in steps: 50% → 40% → 30% → 20% → removed)*

**Constraint 5 — Discretionary cap:**
```
Σ_{i ∈ Discretionary} x_i ≤ 0.30 × Σ_i x_i
```

**Constraint 6 — Per-category historical maximum:**
```
x_i ≤ max_historical_i
```
Where `max_historical_i` is the 90th percentile of user's historical spending for category `i` over ≥ 30 days of data. If insufficient history: 30% of total for Essentials categories, 20% of total for Discretionary categories, and (sum of fixed obligations + 20% buffer) for Obligatory categories.

**Constraint 7 — Savings-First override (conditional):**
```
Σ_{i ∈ FinancialAllocation} x_i ≥ user_target_contribution_amount
```
Active only when the user has selected the Savings-First strategy. Replaces Constraint 3.

**Constraint 8 — Non-negativity:**
```
x_i ≥ 0  for all i
```

#### 2.4 Infeasibility Handling — Sequential Relaxation

When the LP is infeasible (no allocation satisfies all constraints simultaneously), apply relaxation in this exact order:

1. Set Constraint 3 (Financial Allocation minimum) to zero.
2. If still infeasible: reduce Essentials floor to 40%.
3. If still infeasible: reduce Essentials floor to 30%.
4. If still infeasible: reduce Essentials floor to 20%.
5. If still infeasible: remove Essentials floor entirely.
6. If still infeasible with only Constraint 2 (debt minimum) and Constraint 8 (non-negativity), which is always feasible: display to user — *"Your minimum debt payments and essential expenses exceed your predicted income by [amount in pesos]. Odin cannot create a balanced budget. Please consider debt restructuring or income increase. Contact a financial counselor if needed."*

#### 2.5 Surplus Handling

At the end of a budget period, if a surplus exists (allocated but unspent amount):

| Strategy | Behavior | Default for |
|---|---|---|
| Rollover | Surplus added to next period's total budget; LP re-solved with increased total | Stable-Flexible, Stable-Obligated |
| Save | Surplus transferred to user's primary savings goal as an additional contribution | Variable-Flexible, Variable-Obligated |
| Reset | Surplus returned to available balance; next period's budget starts from zero | No default; user must explicitly select |

The user is prompted: *"You underspent by [amount]. What would you like to do with the leftover amount?"* If no response within 7 days, the default strategy for the user's profile is applied.

#### 2.6 LP Solver Implementation

Use `scipy.optimize.linprog` or `PuLP` for LP solving. Both are available on the server. The LP must be solved server-side; the mobile application sends the constraint parameters (forecast income, obligation amounts, historical maxima, user priorities) and receives the solved allocation vector.

```python
from scipy.optimize import linprog

# Negate priorities for minimization (linprog minimizes)
c = [-priority_i for i in categories]

# Build constraint matrices A_ub, b_ub, A_eq, b_eq
# from the 8 constraints above

result = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq,
                 bounds=[(0, max_historical_i) for i in categories],
                 method='highs')
```

If `result.status != 0`, initiate the sequential relaxation procedure.

#### 2.7 Explainability

Every budget recommendation must be accompanied by a plain-language explanation accessible via a "Why?" button:

> *"Your 30-day budget is ₱22,500. This is based on your predicted income of ₱30,000 and a minimum savings target of ₱3,000 (10% of your income). ₱11,250 is allocated to Essentials because this category is required to be at least 50% of your budget. ₱4,500 is allocated to Discretionary because this category is capped at 30%."*

The explanation must state which constraints were active and how they shaped the allocation.

---

### Phase 3: Testing

#### 3.1 Unit Tests

- All 8 constraints individually: test that each constraint is correctly enforced when binding
- Infeasibility: construct a scenario where Constraint 3 makes the problem infeasible; confirm relaxation proceeds in the correct order
- Surplus handling: verify that Rollover, Save, and Reset each correctly update balances and next-period budgets
- Edge case: user has zero debt minimum payments and no insurance premiums (Constraint 2 becomes non-binding at zero floor)
- Edge case: user selects Savings-First strategy (Constraint 7 replaces Constraint 3)

#### 3.2 Integration Tests

- LP solver receives forecast income from LSTM endpoint and default priorities from profile label; confirm the solved allocation is feasible and all constraints are satisfied
- Verify that when a user accepts the recommended budget, actual spending tracking begins against the accepted allocations
- Confirm that manually overriding an allocation is logged and reported as a modification

#### 3.3 Functional Test Cases

| Test Case | Expected Result |
|---|---|
| Stable-Flexible user creates first budget | 30-day period recommended; Financial Allocation priority = 5 |
| LP is infeasible due to high debt obligations | Sequential relaxation applied; user informed if bare minimum is exceeded |
| User leaves surplus at end of 30-day period | Prompt shown within 7 days; default strategy applied if no response |
| User adjusts priorities and regenerates budget | New LP solved with updated priorities; explanation reflects changes |
| User selects Savings-First strategy | Constraint 7 replaces Constraint 3 in LP |

---

### Phase 4: Evaluation

LP evaluation does not use walk-forward validation. Metrics are measured during the pilot user evaluation.

**Primary metrics and acceptable thresholds:**

| Metric | Definition | Threshold |
|---|---|---|
| Adherence Rate | % of users whose actual spending stays within ±20% of recommended allocation for ≥ 3 of 4 broad groups, averaged over the budget period | ≥ 70% |
| Manual Modification Rate | % of users who manually adjust the recommended allocation before accepting | < 50% (high rate signals default priorities mismatch) |
| Constraint Satisfaction Rate | % of LP solutions that satisfy all active constraints without relaxation | Report; no minimum threshold set |
| Budget Utilization Rate | Mean of (actual spending / allocated amount) per category, per user, per period | Report distribution |
| Deviation from User Preferences | Mean absolute deviation between user's stated priorities and the proportion of budget allocated to each category | Report |

> **Note.** Do not apply MAPE or RMSE to LP evaluation. Those are forecasting metrics and are inappropriate for a deterministic optimization model. The metrics above are the correct evaluation framework for LP.

---

### Phase 5: Integration and Deployment

The LP solver receives inputs from:

- **Random Forest:** Profile label (determines default priority weights)
- **LSTM:** Forecasted income and category-level spending estimates (determine constraint parameters)
- **User:** Target savings rate, selected strategy, manual priority adjustments, historical spending data (for per-category maxima)

The LP outputs the accepted budget allocation to:

- **Dashboard:** Displays allocation per category with actuals tracked against it
- **Rule-based Overspending Detection submodule:** Budget allocations are the reference values for the 80% and 100% overspending threshold alerts
- **Surplus handling logic:** Activated at the end of each budget period

---

## Module 4: Anomaly Detection

**Algorithm:** Isolation Forest (unsupervised)  
**Purpose:** Detect unusual transactions in real time based on each user's individual spending baseline. The module also includes a separate rule-based overspending detection submodule that operates independently of machine learning.

---

### Phase 1: Planning

#### 1.1 Activation Threshold

Isolation Forest is disabled until the user has at least **14 days** of transaction history. During the first 14 days, only rule-based overspending detection is active (if an active budget exists). The 14-day rule is a hard requirement and must be enforced in the feature extraction pipeline.

#### 1.2 Per-User Model

The Isolation Forest operates on a **per-user basis**. Each user has their own model trained on their own transaction history. This is fundamentally different from the Random Forest classifier (which is a single shared model). The per-user Isolation Forest is re-evaluated periodically as new transactions are added (within 24 hours of a transaction being saved, edited, or deleted, per Article II Section 5).

Because the model is per-user and unsupervised, there is no global pre-training phase on synthetic data. However, the **feature extraction logic** and **threshold logic** are tested on synthetic data during development to verify that the anomaly detection system behaves correctly before live deployment.

#### 1.3 Cultural Occasion Exclusions

The following periods suppress anomaly alert generation (scores are still computed and logged):

| Occasion | Date Range |
|---|---|
| Christmas and New Year period | December 15 – January 5 |
| Holy Week | Palm Sunday to Easter Sunday (from JSON holiday calendar; algorithmic fallback if not loaded) |
| User's barangay fiesta | User-configured dates ±3 days |
| User whitelist entries | Any transaction matching a whitelisted merchant-category pair within ±25% amount tolerance |

Suppressed transactions may still generate **informational notifications** if the anomaly score exceeds the threshold and if the user has enabled informational alerts.

---

### Phase 2: Data Design

#### 2.1 Feature Vector (8 Dimensions)

All features must be normalized or standardized before being passed to the Isolation Forest. The feature vector is computed per expense transaction.

| # | Feature | Calculation |
|---|---|---|
| 1 | Amount deviation | `(amount − category_30d_median) / category_30d_IQR`, capped at ±5 |
| 2 | Day-of-period proportion | `transaction_date_days_into_period / period_total_days`; defaults to rolling 30-day period if no active budget |
| 3 | Category velocity | Count of transactions in same detailed category in the last 7 days |
| 4 | Time since last transaction (same category) | Hours elapsed since previous transaction in same category; capped at 168 (one week) |
| 5 | Day of week | 0 (Monday) to 6 (Sunday) |
| 6 | Week of month | 1 to 5 |
| 7 | Holiday proximity | 1 if transaction date is within ±3 days of a known Philippine holiday; else 0 |
| 8 | Merchant novelty | 1 if merchant name not seen in any transaction by this user in the last 60 days; 0 otherwise. If no merchant name is provided, defaults to 0 |

> **Design Note (open item from spec).** Feature 7 (holiday proximity) and the occasion exclusion logic in Section 1.3 both reference the same holiday calendar. These should share a single data source — the JSON holiday calendar that the team maintains annually. When the JSON is unavailable or the current year's dates are not loaded, the Easter date is computed algorithmically (Anonymous Gregorian algorithm) as a fallback. The team must confirm whether Feature 7 and the exclusion logic are considered one "occasion" concept or treated separately.

> **Open Item.** A merchant that appeared, disappeared, and reappeared after 61 days would be flagged as novel again. This is the intended behavior per the hard 60-day cutoff. A decay function alternative is noted in the spec as future work.

#### 2.2 Synthetic Test Data for Development Validation

The synthetic test dataset for Isolation Forest development must:

- Contain a minimum of 30 days of transaction history per simulated user
- Inject anomalies at approximately **5% of transactions**, distributed across categories
- Define anomalies as: amount ≥ 2 standard deviations above the category mean, or merchant novelty = 1 on a non-occasion day with unusually high amount, or unusually high category velocity
- Include ground-truth labels (normal = 0, anomaly = 1) for evaluation purposes

---

### Phase 3: Development

#### 3.1 Model Configuration

```python
from sklearn.ensemble import IsolationForest

iso_forest = IsolationForest(
    n_estimators=100,
    max_samples=256,      # or total transactions if fewer
    contamination='auto', # do NOT set a fixed contamination value
    random_state=42
)
```

**Important:** `contamination='auto'` is used because the system applies a **dynamic threshold** rather than a fixed contamination parameter. The raw anomaly scores produced by `decision_function()` are used, and the top 5% of scores by transaction volume are flagged as anomalies. This adapts to each user's actual spending variability rather than forcing exactly 5% of all transactions to be flagged.

```python
# Train per-user model on user's transaction history
iso_forest.fit(user_feature_matrix)

# At transaction time, compute anomaly score
scores = iso_forest.decision_function(new_feature_vector.reshape(1, -1))
# Lower score = more anomalous

# Dynamic threshold: flag if score is in the bottom 5% of all user scores
threshold = np.percentile(all_user_scores, 5)
is_anomalous = scores[0] < threshold
```

#### 3.2 Per-User Model Lifecycle

1. **Initialization:** After the user accumulates 14 days of history, fit the first Isolation Forest model on all available transactions.
2. **Updates:** When a new transaction is saved, edited, or deleted, refit the model asynchronously within 24 hours. Use the most recent 90 days of history (or all available if fewer) as the training window. This is computationally lightweight given the small per-user dataset.
3. **At inference:** When a new expense transaction is entered, compute the feature vector immediately, run inference against the current model, and if the dynamic threshold is exceeded and no suppression condition applies, generate the alert.

#### 3.3 Whitelist Mechanism

When an anomaly alert is generated, present the user with:

> *"[Amount] at [merchant name] appears unusual for your [category] spending. Was this expected?"*

Three response options:

1. **"Yes, expected"** → Add whitelist entry: `{merchant_name, detailed_category, amount_tolerance: ±25%}`. Future transactions matching this merchant + category within ±25% of the flagged amount are suppressed. User may also select "Always allow regardless of amount."
2. **"No, unexpected"** → Transaction remains flagged; no whitelist entry created.
3. **"Remind me later"** → Alert dismissed; no whitelist entry; future similar transactions may still trigger alerts. A reminder notification is scheduled for 24 hours later.

Whitelist entries are viewable, editable, and deletable at Settings → Anomaly Detection → Whitelist.

#### 3.4 Rule-Based Overspending Detection Submodule

This submodule operates independently of Isolation Forest. It does not use machine learning and is not subject to the whitelist or cultural occasion exclusions.

- Generate an alert when any category exceeds **80% of its budget allocation** with **more than 25% of the budget period remaining**.
- Generate a **critical alert** when any category exceeds **100% of its budget allocation** at any time.

Overspending alerts are mandatory and cannot be disabled by users (though notification delivery method — in-app vs. push — is configurable).

#### 3.5 Alert Fatigue Prevention

Three mechanisms must be implemented:

1. **Cooldown period:** No more than 3 anomaly alerts per user per 24-hour period. Rule-based overspending alerts are excluded from this limit.
2. **Bundling:** Multiple anomalies detected within 2 hours are bundled into a single notification listing all affected transactions.
3. **Snooze:** User may snooze all anomaly alerts for 7 days via Settings → Notifications.

#### 3.6 Explainability

For each flagged transaction, identify the feature with the largest standardized deviation from the user's baseline and generate the explanation template:

- Amount deviation: *"This transaction was flagged because the amount (₱5,000) is 2.5 standard deviations above your usual Food spending of ₱800."*
- Merchant novelty: *"This transaction was flagged because you have never spent at this merchant before in the last 60 days."*

Baselines required:

- Amount baseline: category median over preceding 30 days
- Amount-to-income ratio baseline: user's typical ratio for the category
- Days-since-payday baseline: user's typical transaction timing distribution

These baselines are pre-computed and stored as summary statistics per user per category. Explanation generation is instantaneous and requires no per-transaction model fitting.

#### 3.7 Graceful Degradation

If the anomaly detection module throws an unhandled exception, do not show anomaly alerts until the next application restart. Display: *"Spending alerts are temporarily simplified. Your data is safe."* Rule-based overspending alerts continue operating independently.

---

### Phase 4: Testing

#### 4.1 Unit Tests

- Feature 1 (amount deviation): test capping behavior at +5 and −5; test behavior when IQR = 0 (division by zero handling)
- Feature 2 (day-of-period proportion): test when user has no active budget (should default to rolling 30-day period from first of month)
- Feature 8 (merchant novelty): test hard 60-day cutoff; test behavior when merchant name is null (should default to 0)
- Dynamic threshold: construct a set of 100 transactions with known anomaly scores; verify that exactly the bottom 5% are flagged
- Whitelist: verify that a subsequent transaction matching a whitelisted merchant + category + amount within ±25% is correctly suppressed
- Alert fatigue: verify that the 4th anomaly alert in a 24-hour period is not generated; verify bundling within 2 hours

#### 4.2 Integration Tests

- End-to-end: inject a synthetic anomalous transaction; confirm alert is generated with correct explanation
- Occasion suppression: inject a transaction on December 20; confirm no alert is generated (but score is logged)
- Holy Week suppression: inject a transaction on Good Friday; confirm no alert generated
- Barangay fiesta: user configures fiesta on June 24; inject transaction on June 23 (+1 within ±3 days range); confirm suppression
- Profile label integration: confirm that the Isolation Forest feature vector includes the profile label as provided by the Random Forest module

#### 4.3 Functional Test Cases

| Test Case | Expected Result |
|---|---|
| User has 13 days of history | Isolation Forest disabled; only rule-based overspending active |
| User has 14 days of history | Isolation Forest model fit; anomaly detection enabled |
| ₱5,000 Food transaction (typical: ₱800) | Anomaly alert generated with amount-deviation explanation |
| Same transaction on December 20 | Score computed and logged; no user alert (suppressed) |
| User responds "Yes, expected" to alert | Whitelist entry created; future similar transactions suppressed |
| User responds "Remind me later" | Alert dismissed; reminder scheduled for 24 hours later |
| 4th anomaly alert in 24 hours | Alert suppressed by cooldown; not shown to user |
| Category reaches 80% of budget with >25% period remaining | Overspending alert generated (mandatory, not affected by anomaly cooldown) |
| Category reaches 100% of budget | Critical overspending alert generated |

---

### Phase 5: Evaluation

Walk-forward validation per BIBLE Article XIII Section 3:

- **Window:** 30 days training, 7 days test
- **Iterations:** 13 rolling steps (roll forward by 7 days each step)
- **Dataset:** Synthetic test set with injected anomalies at ~5% of transactions; anomalies defined as amounts ≥ 2 standard deviations above category mean

**Primary metrics and acceptable thresholds:**

| Metric | Definition | Threshold |
|---|---|---|
| Precision | TP / (TP + FP) | ≥ 0.70 |
| Recall | TP / (TP + FN) | ≥ 0.65 |
| F1 Score | Harmonic mean of precision and recall | ≥ 0.675 |
| False Positive Rate per user per week | FP count / (active days × 7) | ≤ 1.5 |

**Failure condition:** If F1 falls below 0.6 for 7 consecutive days during synthetic evaluation, log a developer warning. The system continues using Isolation Forest; no automatic fallback occurs in the thesis version.

**Pilot user proxies (where ground-truth labels are unavailable):**

- **User dismissal rate:** % of alerts where user selects "Yes, expected" (high rate = excessive false positives)
- **Alert acknowledgement rate:** % of alerts acknowledged vs. ignored

---

### Phase 6: Integration and Deployment

The Isolation Forest module receives:

- **Random Forest:** Profile label (included as categorical feature in the feature vector)
- **LP Budget Recommendation:** Active budget allocations (used by the rule-based overspending submodule)
- **Transaction Entry Module:** New transactions trigger feature extraction and inference

The Isolation Forest module passes:

- **Alerts and Notifications Module:** Anomaly alerts and overspending alerts are forwarded to the centralized notification system (Article XI)

The anomaly detection module does **not** consume LSTM forecasts in the thesis version. Incorporating forecasted category spending as an additional feature is noted as future work.

---

## Cross-Module Integration and Data Flow

The four core modules form a dependency chain. The following table summarizes data flows between modules.

| Producer | Consumer | Data Passed |
|---|---|---|
| Random Forest (FBP) | LSTM Forecasting | Profile label (categorical feature in input sequence) |
| Random Forest (FBP) | LP Budget Recommendation | Profile label (determines default priority weights) |
| Random Forest (FBP) | Isolation Forest | Profile label (categorical feature in anomaly feature vector) |
| LSTM Forecasting | LP Budget Recommendation | Forecasted income and category-level spending (constraint parameters) |
| LP Budget Recommendation | Overspending Submodule | Active budget allocations (reference values for 80% and 100% thresholds) |
| All ML modules | Alerts and Notifications | Alert triggers forwarded to Article XI notification system |

**Profile change propagation:** When the user accepts a reclassification recommendation from the Random Forest, the updated profile label must propagate to LSTM, LP, and Isolation Forest within 24 hours. This propagation must be asynchronous and must not block the user interface.

**Data isolation:** No module has access to raw transaction records. Each module receives only the minimal feature vector required for its inference function. Feature extraction runs locally on the device; the cloud endpoints receive only the computed feature vectors.

---

## Shared Infrastructure

### Cloud Inference Architecture

All three ML modules (Random Forest, LSTM, Isolation Forest) are hosted as separate cloud endpoints. The LP solver is also server-side. Recommended platform: AWS Lambda or Google Cloud Run for stateless, event-driven inference.

| Module | Endpoint | Timeout | Cache Policy |
|---|---|---|---|
| Random Forest | `/classify` | 1500ms (95th pct.) | Cache profile; refresh on trigger |
| LSTM | `/forecast` | 2500ms | Cache per target; refresh daily |
| Isolation Forest | `/anomaly` | 1500ms (95th pct.) | No caching; per-transaction call |
| LP Solver | `/budget` | 1500ms (95th pct.) | Cache active budget; refresh on income/profile change |

### Asynchronous Update Queue

Transaction saves, edits, and deletions trigger asynchronous updates to all downstream models. These must complete within 24 hours. A job queue (e.g., AWS SQS, Cloud Tasks) is recommended to manage the update pipeline and retry failed jobs. The user must receive a notification: *"Transaction changed. Odin will update your forecasts within 24 hours."*

### Holiday Calendar

The holiday calendar is stored as a JSON configuration file updated annually by the development team. It must cover: all regular and special Philippine public holidays, Holy Week dates (Palm Sunday, Holy Thursday, Good Friday, Black Saturday, Easter Sunday), and any user-configurable barangay fiesta dates. The calendar is loaded at application startup and cached. If the current year's data is missing or corrupt, the Easter date is computed using the Anonymous Gregorian algorithm as a fallback.

---

## Open Items and Pending Decisions

The following items from the BIBLE spec require resolution before finalization of the modules described in this guide. Each is tagged with the responsible party.

| Item | Status | Responsible |
|---|---|---|
| CV threshold (0.25) — RRL validation required | Open | Researchers |
| OR threshold (0.50) — RRL validation required | Open | Researchers |
| Reclassification thresholds (0.10 CV, 0.15 OR, 60-day sustained) — RRL required | Open | Researchers |
| Questionnaire response mapping to profile — provisional algorithm needs validation | Open | Researchers |
| Default priority weights per profile — RRL validation required | Open | Researchers |
| Budget period recommendations per profile — RRL validation required | Open | Researchers |
| Surplus handling strategy defaults — RRL validation required | Open | Researchers |
| Transaction data retention limit (13 months) — institutional source needed | Open | Researchers |
| Holiday proximity and occasion exclusion — confirm whether Feature 7 and Section 1.3 are unified | Open | Team |
| Sensitivity adjustment for anomaly detection — include as advanced setting or omit entirely | Open | Team |
| Credit card account type — include or defer as future work | Open | Team |
| Evaluation period for SUS (14 days vs. 30 days for a subset) | Open | Team + Adviser |

---

*End of Odin Core Module Development Guide v1.0*