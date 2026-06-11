# Odin — Critical Gap Analysis: Algorithm and Model Design
**Scope:** System Specification v3.1 (2026-06-07)  
**Analyst focus:** ML algorithm design, model architecture, training pipeline, inference pipeline, evaluation methodology  
**Prepared for:** Joaquin Luis T. Guevarra, Team Aesir (Group 4)  
**Date:** 2026-06-11  
**Status:** Pre-implementation review — for team discussion before any model code is written

---

## How to Read This Document

Gaps are classified into three tiers:

- **🔴 CRITICAL** — Blocks implementation. No model code should be written until this is resolved. These are architectural or conceptual contradictions.
- **🟡 MAJOR** — Requires a design decision before implementation. Not a blocker for planning, but a blocker for the coding sprint.
- **🟢 MINOR** — A known risk or ambiguity that can be acknowledged and monitored. Low immediate impact.

Gaps are organized by module, then by cross-cutting concerns.

---

## Module 1: Random Forest (Profile Classification)

### 🔴 CRITICAL-RF-1: The role of Random Forest is architecturally circular

**Location:** Article III, Sections 2, 3, 5

**The problem:** Income stability and obligation level are each deterministically assigned by threshold rules:

- CV < 0.25 → Stable; CV ≥ 0.25 → Variable (Art. III, Sec. 2.1.2)
- Obligation ratio < 0.50 → Flexible; ratio ≥ 0.50 → Obligated (Art. III, Sec. 3.1.2)

These two binary rules fully determine which of the four profiles a user receives. The Random Forest is then trained on features that include CV (at 30/60/90-day windows) and obligation ratio — the same values used to generate the labels.

This creates a circular design: RF is being trained to reproduce two threshold conditions from the very features that encode those conditions. If that is the intent, RF will learn the decision boundaries trivially and achieve near-perfect accuracy on any holdout set — making the accuracy metric meaningless as evidence of ML contribution.

**What needs resolution:** The team must explicitly define what the RF is doing *beyond* the threshold rules. Two defensible interpretations exist:

1. **RF as soft/generalizing classifier:** The threshold rules generate training labels from synthetic data. RF then learns to classify profiles from a richer feature set (transaction regularity, savings rate, income frequency, etc.) that the threshold rules don't use, allowing it to classify users even when CV or obligation ratio are uncertain or noisy. This is a legitimate ML contribution — but the spec currently lists CV and obligation ratio as RF features, making it redundant.

2. **RF as label replicator:** RF learns to replicate what the threshold rules produce, providing SHAP-based explainability that threshold rules cannot. This is also defensible but must be framed as such.

Neither interpretation is currently stated. Until this is resolved, the model's purpose, training label generation procedure, and expected accuracy are all undefined. **This is the most consequential gap in the entire ML design.**

**Recommended action:** Add a specification note in Article III Section 5 that explicitly states the intent of using RF over rule-based classification. If RF is intended to go beyond the thresholds, the features fed into it must differ from the features used to generate labels, and the label generation procedure for synthetic data must be clearly documented.

---

### 🔴 CRITICAL-RF-2: Walk-forward validation is the wrong method for this classifier

**Location:** Article XIII, Section 3.2

**The problem:** The spec requires RF evaluation using "a rolling window of sixty days of training data and thirty days of test data, rolling forward by thirty days for six iterations."

Walk-forward validation is a time-series evaluation technique designed for models that predict future values from past values. Random Forest as specified is a **static profile classifier** — it takes a feature vector representing a user's financial statistics and outputs a profile label. It does not predict at time T+1 from history up to T.

Using rolling window temporal splits for RF creates a methodological error. A 60-day training window implies the model is trained only on synthetic user records from a 60-day window, then tested on users from the next 30 days. This is only sensible if user profiles change over time in the synthetic data, which is not specified.

**What needs resolution:** RF should be evaluated with a standard **train/test split** on synthetic users with known profiles. The correct methodology is:

- Generate N synthetic users, each with a known ground-truth profile.
- Split users 80/20 into train and test sets.
- Train RF on training users, evaluate on held-out test users.
- Report accuracy, per-class precision/recall, F1, and confusion matrix.
- Optionally apply k-fold cross-validation across user splits.

The walk-forward design should be removed from the RF section of Article XIII, Section 3.2.

---

### 🟡 MAJOR-RF-3: Cold-start period is stated inconsistently in three places

**Location:** Article III Sec. 2.2.1, Sec. 6.1, and Article XVI Sec. 1.7.2

**The problem:**
- Article III Section 6.1 states: *"During the initial seven-day period before sufficient transaction data is available."*
- Article III Section 2.2.1 states: cold-start ends when the user has at least 5 income transactions **or** 30 days, whichever is **longer**.
- Article XVI Section 1.7.2 states: cold-start ends when the user has at least 5 income transactions, whichever is **longer** (than 7 days, not 30).

These three statements disagree. "Seven days," "thirty days," and "whichever is longer between 5 income transactions and 7 days" are three different conditions.

**What needs resolution:** Pick one definition and apply it everywhere. The Article XVI definition (7 days OR 5 income transactions, whichever is longer) is the most operationally precise and should be the canonical source. Sections 2 and 6 of Article III must be updated to match.

---

### 🟡 MAJOR-RF-4: No hyperparameter search procedure is specified

**Location:** Article III, Section 5.1; Appendix E ("Hyperparameter tuning grids")

**The problem:** The RF parameters (n_estimators=100, max_depth=10, Gini, random_state=42) are presented as fixed specifications. Appendix E requires a hyperparameter tuning grid, but there is no specification of how tuning is conducted — what parameters are searched, what ranges, what cross-validation strategy.

These two things are in tension: fixed parameters imply no tuning; Appendix E implies tuning happened.

**What needs resolution:** Either (a) state that the parameters are defaults and no tuning will be done (justifiable for a thesis), or (b) specify the grid search procedure, the parameter ranges, and the cross-validation strategy. If tuning is done, the fixed parameters in Section 5 should be labeled as the *result* of tuning, not as a priori specifications.

---

### 🟡 MAJOR-RF-5: "Savings rate" feature is undefined with sufficient precision

**Location:** Article III, Section 5, Feature 2.6

**The problem:** Feature 2.6 is "savings rate computed as savings divided by income over a thirty-day window." In Odin's data model, savings goal contributions are recorded as expense transactions under the Financial Allocation broad group (Article IX, Section 3.1). There is no separate savings account or savings balance that is distinct from the transaction ledger.

This means "savings" could be interpreted as:
(a) Total contributions to savings goals (Financial Allocation expense transactions)
(b) Net disposable cash not spent (income minus all expenses, a derived value)
(c) Some other definition

Interpretation (a) could be zero for users who save informally or do not create savings goals in the app. Interpretation (b) could be negative if spending exceeds income. Neither is stated.

**What needs resolution:** Provide an explicit formula: `savings_rate = sum(Financial Allocation expense transactions in last 30 days) / sum(income transactions in last 30 days)`. Acknowledge that this feature may be zero for users who do not use the savings goal module, and that the RF may have low explanatory power from this feature for such users.

---

### 🟢 MINOR-RF-6: Feature 2.5 (fixed expense count) depends on user behavior, not actual spending patterns

**Location:** Article III, Section 5, Feature 2.5

**The problem:** Feature 2.5 is "number of distinct payees with the recurring flag enabled." This is a UX-derived feature — it counts how many recurring templates the user has created — not a feature derived from actual spending patterns. A user with stable, predictable recurring expenses who manually enters every transaction will have a fixed expense count of 0. A user with the same cash flow but who uses recurring templates will have a higher count.

This could introduce measurement artifacts in the RF, where users who prefer manual entry are systematically classified differently from users who use recurring templates, independent of their actual financial behavior.

**What needs resolution:** Consider replacing or supplementing this feature with a computed regularity score (Feature 2.7, transaction entropy) which captures actual behavioral patterns rather than UX usage patterns. At minimum, document this limitation in the paper.

---

## Module 2: LSTM (Forecasting)

### 🔴 CRITICAL-LSTM-1: Multi-target forecast architecture is not specified

**Location:** Article VII, Sections 1 and 2

**The problem:** Section 1 defines four forecast targets:
- Target 1: Per-category expense (4 broad groups)
- Target 2: Total income
- Target 3: Savings balance trajectory (180-day)
- Target 4: Debt remaining balance

Section 2.1 states: *"All forecasts shall be generated using a Long Short-Term Memory (LSTM) network."* But the architectural specs describe one LSTM with a single linear output layer. This is internally contradictory. The following questions are unresolved:

**Architecture question 1:** Is there one LSTM with multiple output neurons (multi-output), or are there separate models per target? A single multi-output model requires care in loss function design and can suffer from conflicting gradient signals if targets are on very different scales (e.g., daily food spending of ~800 pesos vs. savings balance of ~50,000 pesos).

**Architecture question 2:** Targets 3 and 4 are not time-series forecasts in the meaningful sense. The savings balance trajectory is deterministic given a fixed contribution schedule (accumulated amount + N future contributions). The debt remaining balance is deterministic given interest rate, minimum payment, and payoff strategy. Using LSTM for these targets adds complexity without benefit. A simple projection formula is more accurate, more interpretable, and requires no training data for these targets.

**What needs resolution:** The spec must explicitly state:
1. How many LSTM models exist (one global multi-output, or N single-output models).
2. Whether Targets 3 and 4 are actually LSTM-generated or are computed deterministically from user-entered debt/savings parameters. If deterministic, the statement "All forecasts shall be generated using LSTM" must be amended.

---

### 🔴 CRITICAL-LSTM-2: Input normalization is not specified

**Location:** Article VII, Section 2 (entire feature list)

**The problem:** The LSTM processes a mixed feature vector including peso amounts (potentially ranging from hundreds to tens of thousands per day), binary flags (0 or 1), day-of-week integers (0–6), and a categorical profile label. Without normalization, the LSTM gradient updates will be dominated by high-magnitude features (spending amounts), and the model will fail to learn from low-magnitude but informative features (holiday flags, day-of-week).

This is especially critical because the model is pre-trained globally on synthetic data representing users with very different income levels. A normalized peso amount that is meaningful for a 20,000-peso/month earner is very different from the same nominal amount for a 60,000-peso/month earner. The model must be able to generalize across income levels.

**What needs resolution:** Specify the normalization strategy for every feature type:
- Peso amounts: normalize by the user's average monthly income? Z-score per synthetic user? Min-max per category?
- Categorical profile label: one-hot encoding (4 binary features) or embedding?
- Day-of-week, day-of-month: leave as-is or cyclical encoding (sin/cos)?
- Binary flags: leave as 0/1?

The normalization strategy must be consistent between training on synthetic data and inference on real user data. If the normalization parameters (mean, std, income) are estimated from the user's own history, that procedure must be specified.

---

### 🔴 CRITICAL-LSTM-3: Profile label encoding is not specified

**Location:** Article VII, Section 2.4

**The problem:** The profile label (Stable-Flexible, Stable-Obligated, Variable-Flexible, Variable-Obligated) is listed as an LSTM input feature. LSTM layers operate on continuous numerical vectors. The spec never states how this categorical variable is encoded.

- **Label encoding (0, 1, 2, 3):** Incorrect. Implies ordinal relationship (Variable-Obligated = 3 is "more" than Stable-Flexible = 0) that does not exist.
- **One-hot encoding (4 binary features):** Correct for nominal categories. Adds 4 features to the input vector instead of 1.
- **Learned embedding:** Appropriate for large categorical spaces but unnecessary for 4 classes.

**What needs resolution:** Specify one-hot encoding for the profile label. Update the input feature count accordingly (the total feature dimensions will be 4 more than if naively listed). Document this in the architecture spec.

---

### 🔴 CRITICAL-LSTM-4: The 180-day savings trajectory forecast requires autoregressive rollout, which is unspecified

**Location:** Article VII, Section 1.3

**The problem:** Target 3 (savings balance trajectory) is to be forecast at daily granularity over 180 days. The LSTM is trained and evaluated with a 7-day test window (per Article XIII, Section 3.2). To produce a 180-day forecast, the model must either:

(a) **Direct multi-step:** Train with 180 separate output neurons. The training data must then include sequences with a 180-step lookahead, which requires synthetic data spanning at least 240 days (60 lookback + 180 output).

(b) **Recursive/autoregressive:** Generate the next 7-day prediction, append it to the input sequence, slide the window, and repeat until 180 days are produced. This compounds forecasting error — errors in early predictions become inputs for later ones. By day 90, the error can be substantial.

(c) **Hybrid:** Use direct prediction for certain horizons and recursive for others.

If the 180-day horizon is legitimately LSTM-based, strategy (a) or (c) must be specified. If the savings trajectory is actually a deterministic projection (as argued in CRITICAL-LSTM-1), this gap disappears.

**What needs resolution:** Either define the multi-step architecture explicitly, or reclassify Target 3 as a deterministic projection computed outside the LSTM.

---

### 🟡 MAJOR-LSTM-5: "Income amount" feature is ambiguously defined as a time-series input

**Location:** Article VII, Section 2.3

**The problem:** Section 2.3 lists "the user's income amount (updated when new income transactions are recorded)" as an LSTM input feature. For a 60-day daily sequence, this is ambiguous:

- **Interpretation A — Daily income series:** Day d has value equal to any income transaction recorded on day d, else 0. This is sparse (most days = 0) with periodic spikes. This is useful but the "updated when new income is recorded" language suggests it's scalar.
- **Interpretation B — Scalar broadcast:** The current expected income (e.g., declared monthly income / 30) is used as a constant for all 60 days. This fails to capture payday timing, which is presumably why the payday flag (Feature 2.6.1) also exists.

These interpretations have very different dimensionalities in the input tensor.

**What needs resolution:** Clarify whether income is a per-day time-series feature or a scalar contextual feature. If scalar, explain how it enters the model (concatenated at each time step, or passed to a separate dense layer). If time-series, clarify how zero-income days are handled.

---

### 🟡 MAJOR-LSTM-6: Payday flag has no defined data source

**Location:** Article VII, Section 2.6.1

**The problem:** "Payday" is listed as an event flag feature. However, nowhere in the specification is there a mechanism for the system to know when the user's paydays occur. There is no "payday date" field in the onboarding questionnaire (Article III, Section 6), no "pay cycle" setting, and the recurring transaction setup does not automatically export payday information to the ML pipeline.

**What needs resolution:** Either (a) add a payday schedule field to the onboarding questionnaire (ask: "When do you typically get paid? Select frequency and day."), or (b) specify that payday dates are inferred from income transaction history (e.g., the most frequent recurring income date, detected by finding peaks in income time-series), or (c) remove the payday flag as a feature. Option (a) is simplest.

---

### 🟡 MAJOR-LSTM-7: Synthetic dataset size for training is completely unspecified

**Location:** Article VII, Section 2.4; Article XIII, Section 3.1

**The problem:** The LSTM is pre-trained on synthetic data. The spec references a companion document "synthetic-data-design.md" / "model-training-data-design.md" (mentioned in Art. VII, Sec. 4.1). This document does not appear to exist yet. Without it, the training phase cannot be planned. Specifically undefined:

- How many synthetic users are generated?
- How many days of transaction history per user?
- Are all 4 profiles represented equally?
- Are all income quintiles represented?
- How are spending amounts calibrated to BSP CFS / FIES data?

This document is not a minor companion file — it is the primary specification for the most time-consuming part of the entire thesis.

**What needs resolution:** `synthetic-data-design.md` must be drafted before algorithm prototyping begins. The timeline allocates 2 weeks for synthetic data generation; design of that pipeline should have already begun.

---

### 🟢 MINOR-LSTM-8: The 26-iteration walk-forward evaluation requires 242 days of synthetic test data per user

**Location:** Article XIII, Section 3.2

**The problem:** Walk-forward with 60-day training window, 7-day test window, 26 iterations requires 60 + (26 × 7) = 242 days per synthetic test user. The spec says "the synthetic test set is distinct from the training set and represents six months of simulated user activity" — six months is approximately 182 days, which is less than the required 242. Either the test set must be at least 9 months of simulated history, or the number of iterations must be reduced to 17 (which gives 60 + 17×7 = 179 days).

**What needs resolution:** Reconcile the "six months" claim with the 26-iteration formula. Update whichever is incorrect.

---

## Module 3: Isolation Forest (Anomaly Detection)

### 🔴 CRITICAL-IF-1: Per-user model fitting procedure is entirely unspecified

**Location:** Article VIII, Sections 1 and 2

**The problem:** This is the most severe gap in the Isolation Forest design. Unlike RF (pre-trained globally) and LSTM (pre-trained globally), Isolation Forest is specified to "operate on a per-user basis, learning the user's baseline spending behaviour" (Art. VIII, Sec. 1.2). This is an unsupervised, personalized model — it must be fitted on each individual user's transaction data.

But the spec never answers any of the following questions:

1. **When** is the IF model first fitted for a user? (At the end of the 14-day cold-start period? After every new transaction? Weekly?)
2. **How often** is the model re-fitted as new transactions accumulate?
3. **Where** is the fitting done? (On the mobile device? On the cloud server?)
4. **How much data** is used for each fitting? (All available history? A rolling 60-day window? A rolling 90-day window?)
5. **Is consistency preserved across re-fittings?** A transaction scored as anomalous one day could score differently after the model is re-fitted the next day. Does the score from the original fitting persist, or is it recalculated?

Without answers to these questions, the Isolation Forest module cannot be implemented. This is the primary implementation blocker for this module.

**What needs resolution:** Add a section titled "Model Fitting Schedule" to Article VIII. Recommended approach:
- IF is first fitted after 14 days of transaction history (end of cold-start).
- IF is re-fitted once per week, using all available transaction history (no rolling window cap, since the model is lightweight).
- Fitting occurs server-side, and the fitted model's anomaly score threshold (the 95th percentile score) is stored per user.
- New transactions are scored against the most recently fitted model.
- Anomaly score for historical transactions is not recalculated upon re-fitting (the original score at time of logging persists).

---

### 🔴 CRITICAL-IF-2: The 5% dynamic threshold is undefined and breaks at low transaction counts

**Location:** Article VIII, Section 1.5.4.1

**The problem:** The spec says: *"The top five percent of scores by transaction volume shall be flagged as anomalies."* At the 14-day minimum, a user might have 10–20 transactions. 5% of 15 = 0.75, so either 0 or 1 transactions get flagged. This is a floor-of-zero problem that could make the anomaly detection effectively silent for new users.

Additionally, "by transaction volume" is ambiguous: does this mean the top 5% of all transactions the user has ever recorded? Top 5% of transactions in the current evaluation window? Top 5% per category?

**What needs resolution:**
1. Specify a minimum flagging count: "At least one transaction per user per 14-day rolling window shall be evaluated, and those above the score threshold are flagged." Or set a minimum threshold of at least 1 flag per 30-day period.
2. Clarify whether the 5% is computed over the user's entire history, a rolling window, or per-category. Per-category creates many near-zero counts; over entire history is more stable.
3. Consider specifying a minimum anomaly score threshold as a secondary gate (i.e., only flag if score > absolute minimum, in addition to being in the top 5%).

---

### 🟡 MAJOR-IF-3: Whitelisted transactions are included in IF training data, creating a false-normal feedback loop

**Location:** Article VIII, Sections 1, 2, and 4

**The problem:** When a user marks a transaction as "Yes, expected," it is added to the whitelist and suppressed from future alerts (Art. VIII, Sec. 4.2.1). However, the spec never states that whitelisted transactions are removed from the IF fitting data.

This creates a progressive distortion: over time, genuinely unusual transactions (large amounts at new merchants) that the user normalizes through whitelisting also get incorporated into the IF's "normal" distribution during re-fitting. The IF gradually learns that these anomalous patterns are normal, making it increasingly less sensitive.

This is a known issue in feedback-driven anomaly detection. The spec should explicitly state whether whitelisted transactions are excluded from future re-fitting windows, or whether they are included (and the resulting desensitization is accepted as a feature, not a bug).

**What needs resolution:** Add a clause: "When re-fitting the Isolation Forest model, the feature extractor shall exclude transactions that are present in the user's active whitelist from the training window." Or alternatively: "Whitelisted transactions are included in IF fitting; the whitelist mechanism is the primary instrument of false-positive control." Either choice is defensible — just make one.

---

### 🟡 MAJOR-IF-4: The explainability method is explicitly decoupled from IF's actual scoring, but this is not clearly documented as a limitation

**Location:** Article VIII, Section 7; Article XII, Section 2.4

**The problem:** The explanation presented to the user is derived by finding the feature with the largest standardized deviation from the user's baseline statistics (median, IQR). This is computed *independently* of the Isolation Forest's score.

Isolation Forest scores anomalies based on isolation path length — it does not internally rank feature importance per transaction. The explanation method is a reasonable approximation but it can contradict the actual IF reasoning. For example, IF may flag a transaction primarily because of a rare combination of (merchant novelty = 1) + (category velocity = high), while the amount is moderate. But the explanation shows "amount is 2.5 SD above your usual spending" because the amount deviation is numerically larger.

This mismatch can confuse users ("Why am I being told my amount is unusual when I just bought the usual thing from a new store?") and undermines the trust the explainability system is supposed to build.

**What needs resolution:** Add a statement to Article VIII Section 7 and Article XII Section 2.4 explicitly acknowledging: "The deviation-based explanation is an approximation. Isolation Forest does not produce per-feature importance scores. The presented explanation identifies the most statistically unusual feature, which may not precisely correspond to the reason Isolation Forest isolated the transaction. This is a known limitation of the thesis version." This limitation should also be noted in the paper.

---

### 🟢 MINOR-IF-5: Day-of-period proportion feature creates a discontinuity when a new budget is created

**Location:** Article VIII, Section 2, Feature 1.2

**The problem:** Feature 1.2 (day-of-period proportion) is calculated relative to the user's active budget period. When no budget exists, it defaults to a 30-day rolling period. When a new budget is created mid-cycle, the period resets. This means the same calendar day could have a day-of-period proportion of 0.8 one moment and 0.03 the next (if a new budget begins).

If IF is re-fitted immediately after a new budget is created, the training data contains inconsistent period references. This is a low-frequency edge case but worth noting.

**What needs resolution:** Specify that the period reference for historical feature re-computation uses the period that was *active when the transaction was recorded*, not the current period. This requires storing the period-at-recording with each transaction's feature vector. Or simplify: always use the calendar-month proportion (day of month / days in month), removing the dependency on budget state.

---

## Module 4: Linear Programming (Budget Recommendation)

### 🟡 MAJOR-LP-1: No LP solver is specified

**Location:** Article VI, Section 4

**The problem:** The LP objective function and constraint set are well-defined. However, the solver library is never named. The choice of solver matters for implementation: PuLP, SciPy linprog, CVXPY, and Google OR-Tools each have different APIs, dependency footprints, and hosting requirements.

**What needs resolution:** Specify the solver. Recommended: PuLP with CBC backend for simplicity and zero licensing cost. If server-side execution is planned, note that OR-Tools is also an option. The choice should be recorded as a design decision.

---

### 🟡 MAJOR-LP-2: The role of LSTM forecasts in LP constraints is ambiguous

**Location:** Article VI, Section 4.6; Article VI, Section 7.1

**The problem:** Section 7.1 says the LP "receives forecast income and category-level spending forecasts from the LSTM module." Section 4.1 says the total budget is "forecast income × (1 − savings rate)" — so the income forecast clearly drives the total budget. But Section 4.6 says the per-category maximum constraint is the 90th percentile of the user's historical spending.

So what is the LSTM category-level spending forecast actually used for in the LP? The spec implies it feeds the LP constraints, but the stated per-category maximum is historical, not forecast-based. Are LSTM forecasts used to:

(a) Set the total budget only (income forecast)?  
(b) Also set per-category maximums (replacing or supplementing the 90th percentile rule)?  
(c) Inform the user's expected spending but not directly constraint the LP?

**What needs resolution:** Add explicit language to Article VI, Section 7.1 that specifies exactly which LP inputs come from LSTM and which come from historical data. A clear data flow table would suffice.

---

### 🟢 MINOR-LP-3: The infeasibility handling procedure requires up to 4 sequential LP solves; latency is unspecified

**Location:** Article VI, Section 5; Article XIII, Section 1.2

**The problem:** The infeasibility procedure applies up to 4 relaxation steps, each requiring a new LP solve. The general ML latency spec (≤1500ms at 95th percentile) presumably applies, but 4 × LP_solve_time must fit within this budget. LP solves for small problems (< 20 variables, < 15 constraints) are millisecond-scale, so this is likely not a practical issue. However, it is unspecified.

**What needs resolution:** Add a note that the infeasibility handling procedure is expected to complete within the general ML latency budget (1500ms at 95th percentile), and that empirical testing should confirm this during internal testing.

---

### 🟢 MINOR-LP-4: The LP objective can produce degenerate allocations for extreme priority configurations

**Location:** Article VI, Section 4.1

**The problem:** The objective maximizes the sum of (priority × allocation). If one category has priority 5 and all others have priority 1, the optimizer will allocate as much as possible to that category — limited only by the per-category maximum (Section 4.6) and group caps. For a new user with no historical data, the per-category maximum defaults to 30% (Essentials) or 20% (Discretionary) of total budget. This could legitimately produce an allocation where most of the budget goes to one category.

This is technically correct behavior, but it may produce unintuitive outputs if users set extreme priorities without understanding the implications.

**What needs resolution:** The current explanation mechanism (Section 6) partially addresses this by telling users what shaped their allocation. Consider whether the LP should include a "smoothing" constraint (e.g., no single category can receive more than N times its proportional share) to prevent degenerate allocations. This is optional but worth team discussion.

---

## Cross-Cutting ML Gaps

### 🔴 CRITICAL-CROSS-1: `synthetic-data-design.md` does not exist but is the foundation for all ML development

**Location:** Article VII, Section 4.1

**The problem:** The specification references a companion document (`synthetic-data-design.md` or `model-training-data-design.md`) that defines the synthetic data generation procedure for all three trained models. This document is cited as the source for training data distributions, correlation structures, anomaly injection rates, and profile-to-spending-pattern mappings. It does not appear to exist.

Every ML module's training pipeline depends on this document:
- RF training: synthetic users with labeled profiles
- LSTM training: synthetic daily transaction sequences per user per category
- IF evaluation: synthetic sequences with injected anomalies at 5% rate

The 2-week "Synthetic data generation" phase in the thesis timeline cannot begin until this design is complete.

**What needs resolution:** `synthetic-data-design.md` should be drafted before any model code is written. It is the highest-priority missing document in the project. It must specify at minimum: number of synthetic users, transaction frequency distributions per profile, amount distributions per category calibrated to FIES/BSP CFS data, correlation structure, cold-start simulation, and anomaly injection procedure for IF evaluation.

---

### 🔴 CRITICAL-CROSS-2: Timezone is unspecified across all ML feature computations

**Location:** Throughout Article III, VII, and VIII feature definitions

**The problem:** All time-based features reference "30 days ago," "last 7 days," "day of week," "week of month," "holiday proximity," and "day of period." None of these specify the timezone used to define daily boundaries (midnight).

Metro Manila is UTC+8 (Philippine Standard Time). Development servers and cloud inference endpoints may default to UTC. A transaction logged at 11:30 PM PHT on December 14 would be attributed to December 15 in UTC, misaligning with the holiday exclusion period (December 15 to January 5). A transaction logged at 11:50 PM PHT on a Sunday would appear as Monday UTC.

This timezone mismatch will produce subtle, difficult-to-debug errors in all time-based features across RF, LSTM, and IF.

**What needs resolution:** Add a clause to Article I (or Article XVI, definitions) stating: "All datetime computations in the System shall use Philippine Standard Time (PST, UTC+8). All timestamps stored in the database shall be in ISO 8601 format with the UTC+8 offset explicitly encoded. The feature extraction pipeline shall convert all timestamps to PHT before computing daily, weekly, and monthly aggregations."

---

### 🟡 MAJOR-CROSS-3: Inference architecture for RF and IF is unspecified

**Location:** Article VII, Section 2.6 (LSTM only specified); Article XIV, Section 3.4

**The problem:** The spec explicitly states that LSTM inference is server-hosted (cloud server, Art. VII, Sec. 2.6). The spec says nothing equivalent for RF and IF.

This matters because:
- **RF on-device:** An RF with 100 trees at max depth 10 is approximately 1–5 MB serialized. Mobile deployment is feasible with scikit-learn. No privacy concerns. But the classification must run locally.
- **RF server-side:** The feature vector sent to the server is specified in Art. XIV, Sec. 3.4.1 (aggregated statistics, no raw transactions). This is fine for privacy, but requires a server endpoint.
- **IF per-user on-device:** Fitting IF on a mobile device is computationally feasible for small transaction counts (< 1000). But the fitting procedure (see CRITICAL-IF-1) must be implemented in a mobile-compatible library.
- **IF server-side:** Requires sending per-transaction feature vectors to the server (Art. XIV, Sec. 3.4.3 specifies this is allowed) and managing per-user fitted models on the server.

The system architecture diagram (Appendix G) presumably captures this, but the spec must first resolve the decision.

**What needs resolution:** Add inference hosting specifications for RF and IF equivalent to Article VII Section 2.6 for LSTM. Each model should have a specified hosting environment (on-device vs. server-side) and the corresponding latency implications.

---

### 🟡 MAJOR-CROSS-4: Profile reclassification creates a pending-state gap in the LSTM and IF pipelines

**Location:** Article III, Section 4.2.3; Article VII, Section 2.4; Article III, Section 7.2

**The problem:** When a reclassification is triggered, the user sees a recommendation and has up to 30 days to accept or decline (Art. III, Sec. 4.2.3). During this period, the user's official profile label remains the old one. But LSTM uses the profile label as an input feature. Does LSTM use the old profile or the pending recommended profile during this 30-day window?

Additionally, IF uses the profile label as a categorical feature (Art. VIII, Sec. 1, and Art. VIII, Section 9.1). An IF re-fitting during the 30-day pending window would be trained on the old profile — but if the user then accepts the new profile, the IF model trained on the old profile is now misaligned.

**What needs resolution:** Add a clause that explicitly states: "During a pending reclassification period, all downstream models (LSTM, IF) shall continue to use the current accepted profile label. Upon user acceptance of the new profile, downstream model updates (LSTM re-inference, IF re-fitting) shall occur within 24 hours."

---

### 🟡 MAJOR-CROSS-5: The feature extraction pipeline has no specification of its own

**Location:** Article III Sec. 5, Article VII Sec. 2, Article VIII Sec. 2

**The problem:** All three models require computed features derived from raw transaction data: CV over 30/60/90-day windows, obligation ratio, daily category totals, time-since-last-transaction, category velocity, merchant novelty, etc. Computing these features requires a non-trivial data access and aggregation pipeline.

The spec defines what the features are, but never specifies:
- Where is feature computation done (on-device vs. server)?
- Is feature computation event-driven (on each new transaction) or scheduled (nightly batch)?
- Are computed feature vectors stored, or are they recomputed fresh for each inference request?
- When a transaction is edited or deleted (Art. II, Sec. 5.1.2), which features are invalidated and must be recomputed?
- What is the interface between the feature extraction layer and the model inference layer?

**What needs resolution:** Add an Article or Section (possibly as part of the system architecture) titled "Feature Extraction Pipeline" that addresses these questions. This is distinct from the model specs themselves and is a critical infrastructure component.

---

### 🟢 MINOR-CROSS-6: Behavioral drift detection (Mann-Whitney U test) requires 120 days of history that most users won't have during the thesis evaluation

**Location:** Article XVI, Section 1.2.1

**The problem:** Behavioral drift is defined as a statistically significant change detected by comparing non-overlapping 60-day windows (days 1–60 vs. 61–120). This requires 120 days of transaction history before any drift can be detected. The user evaluation phase is 14 days (Art. XIII, Sec. 2). Pilot users have up to 10 participants. No participant in the thesis evaluation will accumulate enough history for drift detection to trigger.

**What needs resolution:** Acknowledge in the spec that behavioral drift detection is a thesis design provision for future production use and will not be observable during the thesis evaluation phase. Consider reducing the detection window to 30-day pairs (days 1–30 vs. 31–60) to potentially make it observable during evaluation.

---

### 🟢 MINOR-CROSS-7: LP budget adherence metric cannot be evaluated on synthetic data

**Location:** Article XIII, Section 3.5

**The problem:** The LP adherence metric requires observing whether real users' spending stays within the recommended allocations. This requires real user behavior, not synthetic data. But Article XIII Section 3.1 states that all algorithm evaluations use synthetic data.

The LP evaluation is therefore structurally different from the three ML model evaluations: it must be conducted during the live user evaluation phase, not during the development-phase synthetic evaluation. This is not explicitly acknowledged, creating potential confusion in the thesis methodology chapter.

**What needs resolution:** Add a note to Article XIII Section 5 stating that LP adherence is evaluated only during the user evaluation phase (not on synthetic data), and that this metric's threshold (≥70%) is assessed from the 30-participant SUS cohort's budget behavior data.

---

### 🟢 MINOR-CROSS-8: The 24-hour asynchronous update window applies differently to LP vs. RF/LSTM/IF

**Location:** Article II, Section 5.1.2; Article III, Section 7.2

**The problem:** When a transaction is edited or deleted, the spec says "all downstream models shall be asynchronously retrained or re-evaluated within twenty-four hours." This makes sense for LSTM (re-inference with updated history) and IF (re-fitting on updated transaction data). But LP is not a trained model — it is re-solved on demand using current data. LP should update immediately upon any transaction change that affects budget actuals, not within 24 hours.

Article II Section 5.1.3 correctly states "budget actuals shall be updated immediately" for edited transactions — but this refers to the actuals tracking, not the LP recommendation. The LP-generated recommendation for the next budget period would not change due to a transaction edit unless the edit also changes the LSTM income forecast.

**What needs resolution:** Clarify that the 24-hour window applies to ML model outputs (profile classification, spending forecasts, anomaly baselines), while LP budget recommendations for the current active period are not re-generated due to individual transaction edits. Only when the next budget period begins, or when the user manually requests a new recommendation, is the LP re-solved.

---

## Summary Table

| ID | Tier | Module | One-Line Description |
|---|---|---|---|
| CRITICAL-RF-1 | 🔴 | Random Forest | Role of RF is architecturally circular with threshold rules |
| CRITICAL-RF-2 | 🔴 | Random Forest | Walk-forward validation is methodologically incorrect for RF |
| CRITICAL-LSTM-1 | 🔴 | LSTM | Multi-target architecture (4 targets) is unspecified |
| CRITICAL-LSTM-2 | 🔴 | LSTM | Input normalization strategy is completely absent |
| CRITICAL-LSTM-3 | 🔴 | LSTM | Profile label encoding is unspecified |
| CRITICAL-LSTM-4 | 🔴 | LSTM | 180-day savings forecast requires autoregressive rollout, not specified |
| CRITICAL-IF-1 | 🔴 | Isolation Forest | Per-user fitting schedule and procedure are entirely unspecified |
| CRITICAL-IF-2 | 🔴 | Isolation Forest | 5% dynamic threshold breaks at low transaction counts |
| CRITICAL-CROSS-1 | 🔴 | All | `synthetic-data-design.md` does not exist |
| CRITICAL-CROSS-2 | 🔴 | All | Timezone (PHT/UTC+8) not specified for any feature computation |
| MAJOR-RF-3 | 🟡 | Random Forest | Cold-start period is inconsistently stated in three places |
| MAJOR-RF-4 | 🟡 | Random Forest | No hyperparameter search procedure defined |
| MAJOR-RF-5 | 🟡 | Random Forest | "Savings rate" feature definition is imprecise |
| MAJOR-LSTM-5 | 🟡 | LSTM | "Income amount" feature is ambiguously defined as scalar vs. time-series |
| MAJOR-LSTM-6 | 🟡 | LSTM | Payday flag has no defined data source |
| MAJOR-LSTM-7 | 🟡 | LSTM | Synthetic dataset size for training is unspecified |
| MAJOR-IF-3 | 🟡 | Isolation Forest | Whitelisted transactions included in IF training — false-normal feedback |
| MAJOR-IF-4 | 🟡 | Isolation Forest | Explainability decoupled from IF scoring; not stated as limitation |
| MAJOR-LP-1 | 🟡 | LP | LP solver library not specified |
| MAJOR-LP-2 | 🟡 | LP | LSTM category forecasts' role in LP constraints is ambiguous |
| MAJOR-CROSS-3 | 🔴 | All | RF and IF inference hosting architecture is unspecified |
| MAJOR-CROSS-4 | 🟡 | RF/LSTM/IF | Pending reclassification creates undefined pipeline state |
| MAJOR-CROSS-5 | 🟡 | All | Feature extraction pipeline has no specification |
| MAJOR-LSTM-8 | 🟢 | LSTM | 26-iteration walk-forward requires more data than "6 months" |
| MINOR-RF-6 | 🟢 | Random Forest | Fixed expense count (Feature 2.5) is UX-derived, not behavior-derived |
| MINOR-IF-5 | 🟢 | Isolation Forest | Day-of-period feature discontinuity at budget creation |
| MINOR-LP-3 | 🟢 | LP | Infeasibility handling (4 LP solves) latency is unspecified |
| MINOR-LP-4 | 🟢 | LP | Extreme priority settings can produce degenerate allocations |
| MINOR-CROSS-6 | 🟢 | All | Drift detection requires 120 days; no thesis user will reach this |
| MINOR-CROSS-7 | 🟢 | LP | LP adherence metric requires real users, not synthetic data |
| MINOR-CROSS-8 | 🟢 | LP/All | 24-hour async window incorrectly applied to LP |

**Totals: 10 Critical · 14 Major · 8 Minor**

---

## Recommended Resolution Order Before First Model Sprint

The following must be resolved — in this order — before any model code is written:

1. **CRITICAL-RF-1** — Define what RF contributes beyond the threshold rules. Resolve the conceptual design.
2. **CRITICAL-CROSS-1** — Draft `synthetic-data-design.md`. Everything else depends on it.
3. **CRITICAL-CROSS-2** — Lock PHT as the system timezone in the spec.
4. **CRITICAL-IF-1** — Define the IF fitting schedule and hosting environment.
5. **CRITICAL-LSTM-2 & LSTM-3** — Define normalization strategy and profile label encoding before the LSTM input tensor can be designed.
6. **CRITICAL-RF-2** — Fix the RF evaluation methodology (replace walk-forward with train/test split).
7. **MAJOR-CROSS-5** — Sketch the feature extraction pipeline's compute and storage design, even informally.
8. **CRITICAL-LSTM-1** — Decide whether Targets 3 and 4 are LSTM-based or deterministic projections.
9. **MAJOR-LP-1** — Select a solver.
10. **MAJOR-LSTM-6** — Define how payday dates are sourced.

---

*End of Gap Analysis — v1.0*  
*Document type: Working document for internal team review*  
*Next action: Present to team; prioritize resolution of Critical gaps before algorithm prototyping sprint begins*