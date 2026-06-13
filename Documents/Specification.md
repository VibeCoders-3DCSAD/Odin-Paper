# Development of Odin: A Personal Finance Management System for Filipino Working Young Adults Using Random Forest, LSTM, and Isolation Forest

---

**Document Type:** Technical Specification

**Version:** 4.0

**Date:** 2026-06-13

**Authors:**
- Gabion, Stefanie S.
- Guevarra, Joaquin Luis T.
- San Jose, Alexa Joanne Paula G.
- Togle, Charles Nathaniel B.

**Course Adviser:** Prof. Era Marie Gannaban

**Technical Adviser:** Prof. Christian Michael Mansueto

**Panels:**
- Prof. Daniel Dellosa (Chair)
- Prof. Jomariss Plan
- Prof. Janice Congzon

**Institutional Affiliation:** College of Computing and Information Sciences, University of Makati

---

# Notes

1. All *italicized statements* (including their subsections, whether italicized as well or not) hereforth are merely suggestions that may be modified, given that justification is provided. 

---

# SYSTEM SPECIFICATION

---

## ===== Article I. Interface =====

### Section 1. Platform

1. The System shall be implemented as a mobile‑first application.

    1.1. *All core user flows must be fully operable on a mobile screen width of 375 density‑independent pixels or less.*

    1.2. *The layout shall adapt to any width between 320 and 450 dp without requiring horizontal scrolling.*

    > NOTE: The LSTM model is hosted on the server. Therefore, all processes except for the forecasting module shall be available offline.

2. A desktop web version shall also be provided.

    2.1. The desktop version shall use a centered container with a maximum width of 1200 pixels.

    2.2. The desktop version may use multi‑column layouts where appropriate.

    2.3. Web screens shall support the same core workflows as mobile, with more room for analysis and reporting.

3. *The mobile web version should lead to the Google Play link or installation link of the mobile application.*

### Section 2. Screens

1. The System shall implement the following primary screens:

    1.1. Registration

        1.1.1. Onboarding Questionnaire

        1.1.2. Onboarding Result and Financial Behavioral Profile Assignment

    1.2. Login

    1.3. User Profile

    1.4. Financial Behavioral Profile Overview

        1.4.1. Financial Behavioral Profile

        1.4.1. Profile Reassignment

    1.5. Dashboard

    1.6. Transaction Entry

        1.6.1. Manual Transaction Entry

        1.6.2. Recurring Transaction Entry

    1.7. Transactions History

    1.8. Budget Overview

        1.8.1. Budget Recommendation

        1.8.2. Budget Categories

    1.9. Forecasting Overview

    1.10. Anomaly Detection Overview

        1.10.1. Overspending Detection

        1.10.2. Anomaly Detection 

    1.11. Savings Goals Overview

        1.11.1. Savings Goal Hierarchy

    1.12. Debt Overview

        1.12.1. Debt Hierarchy

    1.13. Reports & Analytics

    1.14. Settings

        1.14.1. User Settings

        1.14.2. System Settings

        1.14.3. Help & Problem Reporting

    1.15. Notifications & Alerts

---

## ===== Article II. Users =====

### Section 1. Target Users

1. The System is designed exclusively for the following users.

    1.1. Demographic requirement. The user shall be a Filipino working young adult aged twenty to forty years inclusive.

    1.2. Geographic requirement. The user shall live or work in Metro Manila, covering any of its sixteen cities and one municipality.

    1.3. Employment requirement. The user shall *classify their primary employment in* any of the following capacities:

        1.3.1 Regular Employees. This employment type is entitled to security of tenure, and usually entitled to statutory benefits (SSS, PhilHealth, Pag-IBIG, 13th month pay) on a pro-rata basis. This employment type supports the Stable income dimension.

            1.3.1.1. Full‑time Employee

            1.3.1.2. Part‑time Employee

        1.3.2. Independent Contractors. This employment type has variable security of tenure, and usually no employer-employee relationship. The individuals are responsible for their own taxes and governmental contributions as voluntary members. This employment type supports the Variable income dimension.

            1.3.2.1. Self‑employed Individual
            
            1.3.2.2. Freelancer
            
            1.3.2.3. Business Owner

            1.3.2.4. Entrepreneur

        1.3.3. Fixed-Term and Project Employees. This employment type has variable or low security of tenure. The individuals are employed only for the length of their contractual obligations (project completion dates, termination dates). This employment type supports the Variable income dimension.

            1.3.4. Contractual/project‑based employee or similar

            1.3.5. Business owner/entrepreneur

            1.3.6. Gig economy worker

    > NOTE: Primary employment is emphasized since the user can have more than one job (side hustles, freelancing). In the financial behavioral profile classification module, employment shall not bear more influence than other more appropriate features like income sources, income amount, income frequency, etc., which better defines the user's income stability.

    > NOTE: The "This employment type supports..." parts could probably be moved to the Financial Behavioral Profile Article/Section.

    > Employment classifications are based on the Department of Labor and Employment's own standards (Labor Code of the Philippines).

---

## ===== Article III. App Installation =====

### Section 1. Installation Site

1. *The System shall be distributed as a mobile‑first application for Android devices via an Android Package Kit.*

2. *The desktop web version shall be accessible via a standard web browser at a domain designated accordingly.*

### Section 2. Installation Guide

> NOTE: Add installation guide for the user starting from installation site all the way to working mobile app.

---

## ===== Article IV. Financial Behavioral Profile Structure =====

### Section 1. Financial Behavioral Dimensions

1. There are two binary dimensions that define the four financial behavioral profiles: **Income Stability** and **Obligation Level**.

2. Income stability is the capacity of the user's inflow to maintain a stable amount and frequency in regular intervals.

3. Depending on the user's income stability, they can be classified as either **Stable** or **Variable**.
    
4. Income stability shall be derived initially from the user’s *employment status and income variability as declared during onboarding*.

    4.1. Afterwards, income stability shall be derived from the user's actual transaction history.

5. Obligation level is the proportion of the user's necessary expenses (sum of Essential and Obligatory expenses; see Article X) and their total expenses.

6. Depending on the user's obligation level, they can be classified as either **Flexible** or **Obligated**.

7. Obligation level shall be derived from *declared fixed obligations, dependents, debt payments, and protected expenses as declared during onboarding*.

    7.1. Afterwards, obligation level shall be derived from the user's actual transaction history.

### Section 2. Financial Behavioral Profile

1. The financial behavioral profiles are derived from a combination of the user's income stability and obligation ratio.

2. The four financial behavioral profiles are:

    2.1. **Stable‑Flexible**

    2.2. **Stable‑Obligated**

    2.3. **Variable‑Flexible**

    2.4. **Variable‑Obligated**

---

## ===== Article V. Random Forest Algorithm Structure [DRAFT] =====

### Section 1. Input [DRAFT]

1. *The Random Forest algorithm shall receive the following inputs derived from a user’s transaction history:*

    1.1. Income frequency (number of income transactions in the last 30 days)

    1.2. Income amount variance (mean absolute deviation over 90 days)

    1.3. Fixed expense count (number of distinct payees with recurring transactions)

    1.4. Savings rate (Financial Allocation expenses divided by total income over 30 days)

    1.5. Transaction regularity score (Shannon entropy of inter‑transaction intervals over 60 days)

2. *If the user has insufficient transactions, the algorithm shall use the onboarding questionnaire instead.*

> NOTE: Need to define at what level or amount is transaction sufficient.

### Section 2. Process [DRAFT]

1. *The algorithm shall construct an ensemble of decision trees.*

    1.1. Minimum 100 trees

    1.2. Maximum depth 10

    1.3. Gini impurity as the split criterion.

2. *Class weights shall be balanced to handle potential class imbalance.*

3. *The algorithm shall output a predicted financial behavioral profile.*

    3.1. SHAP values and descriptions will also be added for explainability.

4. *The system shall retrain the Random Forest model monthly on each user’s accumulated transaction history only after obtaining explicit user consent.*

    4.1. Sliding window of 365 days

### Section 3. Output [DRAFT]

1. *The output shall be:*

    1.1. A financial behavioral profile (e.g., “Stable‑Flexible”) as a label

    1.2. A plain‑language explanation stating the two most influential features and their values
    
    1.3. A confidence score (derived from the proportion of trees voting for the predicted class)

2. *The output shall be stored in the user’s profile.*

---

## ===== Article VI. Financial Behavioral Profile Classification Process =====

### Section 1. Financial Behavioral Profile Classification

---

## ===== Article VII. Financial Behavioral Profile Module =====

### Section 1. Onboarding Questionnaire

### Section 2. Onboarding Results

### Section 3. Profile Assignment & Selection

### Section 4. User Profile Creation

---

## ===== Article VIII. User Profile Module =====

### Section 1. User Profile

---

## ===== Article IX. Financial Account Structure =====

### Section 1. Financial Account

### Section 2. Financial Account Balance

### Section 3. Financial Account Flow

---

## ===== Article X. Expense Structure =====

---

## ===== Article XI. Transaction Structure =====

---

## ===== Article XII. Transaction Entry Module =====

---

## ===== Article XIII. Transaction History Module =====

---

## ===== Article XIV. Budget Structure =====

### Section 1. Budget

---

## ===== Article XV. Linear Programming Algorithm Structure =====

> NOTE: Insert three or more sections that cover input, process, and output.

## ===== Article XVI. Budget Recommendation Process =====

---

## ===== Article XVII. Budgeting Module =====

---

## ===== Article XVIII. Forecast Structure =====

### Section 1. Forecast

---

## ===== Article XIX. Long Short-Term Memory Algorithm Structure =====

> NOTE: Insert three or more sections that cover input, process, and output.

---

## ===== Article XX. Financial Forecast Process =====

---

## ===== Article XXI. Anomalous Transaction Structure =====

### Section 1. Overspending Transactions

### Section 2. Anomalies

---

## ===== Article XXII. Exclusions =====

### Section 1. Occasions

### Section 2. Whitelist

---

## ===== Article XXIII. Isolation Forest Algorithm Structure =====

> NOTE: Insert three or more sections that cover input, process, and output.

## ===== Article XXIV. Anomaly Detection Module =====

---

## ===== Article XXV. Savings Goal Structure =====

---

## ===== Article XXVI. Savings Goal Module =====

---

## ===== Article XXVII. Debt Structure =====

---

## ===== Article XXVIII. Debt Module =====

---

## ===== Article XXIX. Notifications =====

### Section 1. Informational Notifications

### Section 2. Warning Notifications

### Section 3. Alert Notifications

---

> VVV --- Construction Zone Ahead --- VVV

## Article VIII. Transaction

### Section 1. Input Types

1. The System shall accept financial data via two input types.

    1.1. Manual transaction. The user types transaction details directly into the application.

    1.2. Recurring transaction. The user specifies a repeating transaction pattern. The System then generates the transaction automatically on scheduled dates.

### Section 2. Manual Transaction

1. Manual transactions shall require the following fields.

    2.1. Required fields are amount, category, date, and account.

    2.2. Optional fields are merchant name and description.

        2.2.1. If the merchant name is omitted, the merchant novelty feature for anomaly detection defaults to zero.

3. Recurring transactions shall require the following fields.

    3.1. Required fields are amount, category, frequency, start date, and account.

    3.2. Optional fields include an end date.

4. Transfers between accounts shall use the manual input method.

    4.1. When the user selects the transfer transaction type, the user interface shall display source account and destination account selectors.

    4.2. The System shall not display a single account field for transfer transactions.

### Section 2. Transaction Types

1. The System shall support exactly three transaction types.

    1.1. Income transaction. This represents a cash inflow into an account, moving from an external source to the available balance.

        1.1.1. Income may be recurring with frequencies of daily, weekly, monthly, yearly, or a custom interval.

    1.2. Expense transaction. This represents a cash outflow from an account, moving from available balance to an expense category.

        1.2.1. Expense may be recurring with the same frequency options as income.
        
    1.3. Transfer transaction. This moves cash from one account to another without changing net worth.

        1.3.1. Transfer may be recurring with daily, weekly, or monthly frequencies.

        1.3.2. When a transfer is recorded, the System shall subtract the amount from the source account's balance and add the same amount to the destination account's balance.

### Section 3. Manual Transaction

1. When a user manually enters a transaction, the System shall perform the following validations and actions in sequence.

    1.1. Validate amount.

        1.1.1. For income and expense, the amount must be greater than zero Philippine pesos.

        1.1.2. For transfer, the amount must be positive. The direction of transfer is captured by source and destination account selection.

    1.2. Check for negative balance (expense transactions only). The System shall verify whether deducting the amount would make the available balance negative.

        1.2.1. If a negative balance would result, the System shall display a warning message.

        1.2.2. The warning shall state: "This transaction will result in a negative balance."

        1.2.3. The System shall prompt the user to confirm whether they wish to proceed.

            1.2.3.1. The user may confirm the deduction and accept the negative balance.

            1.2.3.2. The user may cancel the transaction.

        1.2.4. This warning mechanism exists because users may occasionally forget to record income transactions. Preventing negative balances entirely would create unnecessary friction.

    1.3. Display persistent warning for negative balances. The System shall display a persistent warning badge on the dashboard whenever any account balance is negative.

        1.3.1. The System shall continue to show this badge until the balance returns to zero or positive.

    1.4. Update available balance.

        1.4.1. For an income transaction, add the amount to the available balance of the selected account.

        1.4.2. For an expense transaction, subtract the amount from the available balance.

        1.4.3. For a transfer, subtract the amount from the source account and add it to the destination account.

    1.5. Store transaction. After the transaction is saved, the System shall store it with a timestamp in ISO 8601 format.

        1.5.1. The transaction shall then be used to update downstream models, including profile classification, spending forecasts, and anomaly detection baselines.

        1.5.2. These updates shall occur asynchronously for model retraining but shall complete within twenty‑four hours. Budget actuals shall be updated immediately.

### Section 4. Recurring Transaction

1. The System shall generate recurring transactions automatically at their scheduled frequencies.

    1.1. If a generated expense or transfer transaction would cause the available balance to become negative, the System shall not create the transaction.

        1.1.1. Instead, it shall postpone the transaction, notify the user of the postponement, and re‑attempt generation on the next scheduled date and time.

    1.2. The user may pause, edit, or delete any recurring template at any time.

### Section 5. Transaction Editing and Deletion.

1. Users may edit or delete any transaction, whether manual or recurring, subject to the retention limit described in subsection 2.

    1.1. Immediate balance update. When a transaction is edited or deleted, the System shall immediately recompute the available balance for the affected account.

    1.2. Asynchronous model updates. All downstream models—profile classification, spending forecasts, and anomaly detection—shall be asynchronously retrained or re‑evaluated within twenty‑four hours.

    1.3. Immediate budget updates. Budget actuals shall be updated immediately.

    1.4. User notification. The user shall receive a notification stating: "Transaction changed. Odin will update your forecasts within 24 hours."

2. Retention limit. Users may not edit or delete transactions older than twenty‑four months from the transaction date.

    2.1. The choice of twenty‑four months replaces the provisional thirteen‑month limit from the original specification. This aligns with standard financial record‑keeping practices.

> Validation required. The researchers must validate this period against either Bangko Sentral ng Pilipinas data retention guidelines or the Data Privacy Act's legitimate purpose principle before final submission. If no authoritative source supports twenty‑four months, the team shall adopt three years to align with Philippine tax record‑keeping recommendations.

### Section 6. Category Suggestions and Smart Defaults

1. To reduce transaction entry effort, the System shall provide category suggestions or smart defaults.

    1.1. When adding a transaction, the System shall suggest the most recently used category for the same merchant (if merchant name is provided).

    1.2. If no merchant history exists, the System shall suggest the most frequently used category across all transactions in the last thirty days.

    1.3. The user may override any suggestion.

---

## Article III: Financial Behavioral Profiles

### Section 1. Profile Taxonomy

1. The System shall classify each user into exactly one of four financial behavioral profiles.

    1.1. The classification is determined by two binary dimensions.

        1.1.1. Income stability. Takes the value Stable or Variable.

        1.1.2. Obligation level. Takes the value Flexible or Obligated.

    1.2. The four resulting profiles are:

        1.2.1. Stable‑Flexible

        1.2.2. Stable‑Obligated

        1.2.3. Variable‑Flexible

        1.2.4. Variable‑Obligated

### Section 2. Income Stability

1. Income stability shall be determined by the coefficient of variation (CV) of monthly net income over the preceding ninety days.

        1.1. Definition of CV. The coefficient of variation is the standard deviation of monthly net income divided by the mean monthly net income.

    1.2. Classification rule.

        1.2.1. A user is Stable if CV is less than 0.25.

        1.2.2. A user is Variable if CV is 0.25 or greater.

    1.3. Provisional threshold. The proposed threshold of 0.25 is provisional.

        1.3.1. The researchers must validate this value through analysis of survey data (such as the BSP Consumer Finance Survey) or relevant literature.

        1.3.2. Until validation is complete, the threshold shall remain configurable via system settings without requiring code changes.

2. Cold‑start classification. For the first seven days of transaction history, the System shall use responses from the onboarding questionnaire to estimate income stability.

    2.1. Cold‑start period definition. The cold‑start period lasts until:

        2.1.1. The user has accumulated at least five income transactions, or

        2.1.2. Thirty days of history have passed,

        2.1.3. Whichever is longer.

    2.2. Transition to actual data. Only after meeting this minimum data requirement shall the System compute the coefficient of variation from actual transaction data.

> [RRL NEEDED: CV threshold of 0.25] The proposed threshold of 0.25 is provisional. The researchers must validate this value through analysis of survey data (such as the BSP Consumer Finance Survey) or relevant literature on income variability among Filipino working young adults. Until validation is complete, the threshold shall remain configurable via system settings without requiring code changes.

### Section 3. Obligation Level

1. Obligation level shall be determined by the obligation ratio.

    1.1. Definition of obligation ratio. Total unavoidable monthly expenses divided by total monthly income, averaged over the preceding sixty days.

    1.2. Classification rule.

        1.2.1. A user is Flexible if the obligation ratio is less than 0.50.

        1.2.2. A user is Obligated if the obligation ratio is 0.50 or greater.

    1.3. Provisional threshold. The proposed threshold of 0.50 is provisional and must be validated through research.

    1.4. Definition of unavoidable expenses. Includes:

        1.4.1. Rent or mortgage

        1.4.2. Utility minimum payments

        1.4.3. Debt minimum payments

        1.4.4. Insurance premiums

        1.4.5. Government‑mandated contributions (SSS, PhilHealth, Pag‑IBIG)

        1.4.6. Documented family support (e.g., monthly remittance to parents)

2. Handling mandatory contributions for salaried employees. The System shall ask the user during onboarding whether they record gross or net income.

    2.1. If the user records net income (after deductions), mandatory contributions are already accounted for and shall not be added again as separate expenses.

    2.2. If the user records gross income, the System shall treat the contribution amounts as separate unavoidable expenses when they appear as transactions.

> [RRL NEEDED: Obligation ratio threshold of 0.50] The proposed threshold of 0.50 is provisional and must be validated through research. The definition of unavoidable expenses includes rent or mortgage, utility minimum payments, debt minimum payments, insurance premiums, government‑mandated contributions (SSS, PhilHealth, Pag‑IBIG), and documented family support such as monthly remittance to parents.

### Section 4. Reclassification

1. The System shall re‑evaluate a user's profile classification when any of the following conditions occur.

    1.1. CV change. The income coefficient of variation changes by an absolute difference of 0.10 or more from the baseline used for the current classification, sustained over sixty consecutive days.

    1.2. Obligation ratio change. The obligation ratio changes by an absolute difference of 0.15 or more from the baseline, sustained over sixty consecutive days.

    1.3. User request. The user explicitly requests reclassification via the settings menu.

    1.4. Periodic refresh. Ninety days have elapsed since the last classification.

2. Upon detection of any trigger, the System shall generate a reclassification recommendation and present it to the user with an explanation using SHAP values.

    2.1. No automatic reclassification shall occur without explicit user confirmation.

    2.2. The user may accept or decline the recommended change.

    2.3. The user may also override or request a reassessment of their profile at any time.

    2.4. If the user does not respond to the recommendation within thirty days, the System shall display a persistent, non‑dismissible notification on the dashboard stating: "Your financial behavior appears to have changed. Odin recommends updating your profile. Apply now?"

    2.5. The user must either accept or decline. There is no automatic application.

### Section 5. Random Forest Algorithm

1. Classification shall be performed using a Random Forest classifier with the following specifications.

    1.1. Forest composition. The forest shall contain a minimum of one hundred decision trees.

    1.2. Tree depth. Each tree shall have a maximum depth of ten levels.

    1.3. Split criterion. The split criterion shall be Gini impurity.

    1.4. Class weights. Class weights shall be set to balanced as a robustness measure against class imbalance.

    1.5. Reproducibility. The random state shall be fixed at forty‑two for reproducibility during testing and development.

2. Feature set. The Random Forest classifier shall use exactly five behavioral features, all derived from the user's transaction history. The income coefficient of variation and the obligation ratio are explicitly excluded from this feature set.

    2.1. Income frequency. The number of income transactions recorded within the preceding thirty‑day window.

    2.2. Income amount variance. The mean absolute deviation of income transaction amounts over the preceding ninety days.

    2.3. Fixed expense count. The number of distinct payees associated with at least one active recurring transaction template.

    2.4. Savings rate. The sum of all Financial Allocation expense transactions divided by the sum of all income transactions over the preceding thirty‑day window.

        2.4.1. If no Financial Allocation transactions exist within the window, the savings rate shall default to zero.

        2.4.2. If no income transactions exist within the window, the savings rate shall default to zero and a data‑sufficiency flag shall be raised.

    2.5. Transaction regularity score. The Shannon entropy of inter‑transaction intervals computed across all expense transactions over the preceding sixty days.

        2.5.1. Higher entropy values indicate more erratic spending timing. Lower entropy values indicate more regular, predictable patterns.

3. Role of income coefficient of variation and obligation ratio. These two metrics are computed by the System and play defined roles, but they are not inputs to the Random Forest classifier.

    3.1. Synthetic data label generation. During construction of the synthetic training dataset, the income CV threshold and obligation ratio threshold are applied to each synthetic user's generated financial profile to assign a ground‑truth profile label. This is their sole function during model development.

    3.2. Reclassification triggers. At runtime, changes in a user's computed CV or obligation ratio serve as conditions that initiate re‑evaluation of the user's profile. Upon trigger, the System initiates a new Random Forest inference pass using the user's current five‑feature behavioral vector. CV and obligation ratio do not re‑enter the classifier as features.

4. Explainability with SHAP. For each classification prediction, the System shall compute SHAP (SHapley Additive exPlanations) values across the five behavioral features.

    4.1. The System shall identify the two features with the largest absolute SHAP values for the predicted class and present them to the user as a plain‑language explanation.

    4.2. Explanation format. The explanation shall be constructed from a template of the following form: "Your profile is [Profile Name] mainly because [Feature A description], and [Feature B description]."

        4.2.1. Example — Variable‑Obligated: "Your profile is Variable‑Obligated mainly because your income amount varies significantly from month to month, and you have a high number of recurring fixed obligations compared to users in other profiles."

        4.2.2. Example — Stable‑Flexible: "Your profile is Stable‑Flexible mainly because your income arrives at a consistent and regular interval, and your spending pattern shows high regularity with few fixed recurring commitments."

    4.3. SHAP values shall be computed at inference time from the trained Random Forest model. They shall be stored in the application log for audit purposes and retained for thirty days, after which they shall be anonymised by removing user identifiers.

    4.4. The explanation shall be accessible to the user via the "Why?" button on the financial behavioral profile screen.

5. Continuous learning. The Random Forest classifier shall be periodically retrained on the user's accumulated transaction history with explicit user consent.

    5.1. Retraining shall occur monthly, using a sliding window of the most recent 365 days of data.

    5.2. The user may opt out of personalised retraining and continue using the pre‑trained synthetic model.

    5.3. This decision replaces the original freeze‑all‑models approach. The PRD requires that forecasts and profiles improve as the user logs more transactions. Continuous learning with explicit consent preserves privacy while enabling personalisation.

6. Accuracy target and prototyping validation.

    6.1. The target classification accuracy is 0.85 or higher on the synthetic holdout test set.

    6.2. If classification accuracy falls below 0.85 following initial prototyping, the researchers shall apply the following remediation sequence before any other intervention.

        6.2.1. Step 1. Review and revise the synthetic data generation parameters to ensure that behavioral features correlate sufficiently with the profile labels.

        6.2.2. Step 2. If accuracy remains below 0.85 after synthetic data revision, conduct a hyperparameter search over n_estimators, max_depth, and min_samples_split.

        6.2.3. Step 3. If accuracy remains below 0.85 after both steps, the researchers shall document the achieved accuracy, report it as the thesis result, and analyse which feature or profile pair is responsible for the shortfall.

    6.3. The researchers shall not reintroduce income CV or obligation ratio into the RF feature set as a remediation measure.

> [RRL NEEDED: Behavioral feature predictiveness for profile classification] The design rationale in subsection 3.3 claims that observable behavioral transaction signals are predictive of financial behavioral profiles independently of explicit definitional metrics. This claim must be supported by at least two studies from Topic 5.C (Random Forest Classification Algorithm for Behavioral Profiles) that demonstrate RF classifying behavioral or financial profiles from transactional or behavioral proxy features rather than from the profile's own definitional criteria. The researchers shall identify and cite these studies in the methodology chapter when justifying the feature set design.

### Section 6. Cold-Start Classification

1. During the initial seven‑day period before sufficient transaction data is available, the System shall classify the user using a questionnaire.

2. The questionnaire shall contain at least the following items:

    2.1. Employment status

    2.2. Monthly income amount

    2.3. Income stability (binary)

    2.4. Income variability (percentage/range)

    2.5. Obligation ratio (percentage)

    2.6. Dependents (Yes/No, with count)

    2.7. Loans or debts (Yes/No)

    2.8. Declaration of fixed obligations, dependents, and protected categories

3. After the user completes the questionnaire, the System shall compute an initial profile and present it to the user for confirmation before proceeding to the main application.

### Section 7. Module Relationships

1. The profile label produced by the Random Forest classifier shall be passed to the following downstream modules.

    1.1. LSTM forecasting module. The profile shall be used as a contextual feature.

    1.2. Isolation Forest anomaly detection module. The profile shall be used to provide profile‑aware baselines.

    1.3. Budget recommendation module. The profile shall be used to select default priorities and constraints.

2. When a user's profile changes through reclassification, all downstream modules shall receive the updated label within twenty‑four hours.

---

## Article IV: Expense Groups and Categories

### Section 1. Expense Categories

1. The System shall implement expense categories grounded in the 2020 Philippine Classification of Individual Consumption According to Purpose (PCOICOP), cross‑validated against the BSP Consumer Finance Survey 2021.

2. The following base categories shall be implemented, each with its associated mapping to broad groups as defined in Section 2 of this Article.

    2.1. Food and Non‑Alcoholic Beverages – mapped to Essentials.

    2.2. Alcoholic Beverages, Tobacco and Narcotics – mapped to Discretionary.

    2.3. Clothing and Footwear – mapped to Discretionary.

    2.4. Housing, Water, Electricity, Gas and Other Fuels – with mappings:

        2.4.1. Actual rent payments → Obligatory.

        2.4.2. Utilities (water, electricity, gas) → Essentials.

        2.4.3. Maintenance and repair services → Discretionary.

    2.5. Furnishings, Household Equipment and Routine Household Maintenance – mapped to Discretionary.

    2.6. Health – mapped to Essentials.

    2.7. Transport – with mappings:

        2.7.1. Obligatory for essential commuting (public transport, fuel for work travel).

        2.7.2. Discretionary for vehicle purchases and non‑essential travel.

        2.7.3. The System shall not auto‑classify; the user selects the subcategory at transaction entry.

    2.8. Information and Communication – with mappings:

        2.8.1. Obligatory for basic communication services (mobile plan, home internet).

        2.8.2. Discretionary for device purchases.

    2.9. Recreation, Sport and Culture – mapped to Discretionary.

    2.10. Education Services – mapped to Obligatory.

    2.11. Restaurants and Accommodation Services – mapped to Discretionary.

    2.12. Insurance and Financial Services – with mappings:

        2.12.1. Insurance premiums → Obligatory.

        2.12.2. Financial services fees → Discretionary unless the user designates them as essential.

    2.13. Personal Care, Social Protection and Miscellaneous Goods and Services – with mappings:

        2.13.1. Discretionary for personal care and miscellaneous.

        2.13.2. Obligatory for documented social protection contributions.

3. Filipino‑specific obligations. The category taxonomy shall explicitly include the following Filipino‑context categories:

    3.1. Family support and remittances

    3.2. Paluwagan (informal rotating savings and credit association)

    3.3. Church or religious donations

    3.4. Barangay or community collections

    3.5. Government contributions (SSS, PhilHealth, Pag‑IBIG)

    3.6. Debt payments

    3.7. Insurance

    3.8. Emergency fund

    3.9. Savings and investments

4. Protected categories. The System shall support marking categories as protected.

    4.1. Default protected categories shall include essentials, debt and loan repayments, insurance, and emergency fund contributions.

    4.2. The user may declare additional protected categories during onboarding or via settings.

    4.3. Budget recommendations must not suggest reducing protected categories unless the user explicitly changes protection settings.

5. Category customization. The user may create up to five custom subcategories under any base category.

    5.1. Each custom subcategory must be mapped to exactly one base category and one broad group (Essentials, Obligatory, Discretionary, or Financial Allocation).

    5.2. The user may delete custom subcategories but may not delete or rename base categories.

6. The System shall not perform automatic categorisation of transactions. All category assignments must be made by the user at transaction entry time.

### Section 2. Expense Groups

1. For forecasting (LSTM) and budget recommendation, the thirteen base categories shall be aggregated into four broad groups.

    1.1. Essentials group. Includes Food and Non‑Alcoholic Beverages, the utilities portion of Housing (electricity, water, gas), and Health. These are expenses necessary for basic survival and well‑being.

    1.2. Obligatory group. Includes contractual and unavoidable payments: rent (actual rentals), debt minimum payments, insurance premiums, government contributions, basic transport for commuting, basic communication services, education expenses, and documented family support. These expenses are fixed in amount or timing and cannot be easily reduced in the short term.

    1.3. Discretionary group. Includes all remaining categories: alcoholic beverages and tobacco, clothing and footwear, non‑essential housing maintenance, furnishings and appliances, non‑essential transport, recreational equipment and services, dining out, accommodation, personal care, and miscellaneous goods. These expenses are optional and can be adjusted based on available surplus.

    1.4. Financial Allocation group. Includes savings deposits, investment contributions, and debt principal prepayments (beyond minimum payments). These are treated as allocations rather than expenses, though they appear as outflows from available balance. The distinction is important for the budget LP: financial allocations are not counted as "spending" in the same sense as the other three groups.

### Section 3. Custom Subcategories

1. Users may create up to five custom subcategories under any base category.

    1.1. Each custom subcategory must be mapped to exactly one base category for aggregation purposes.

    1.2. Each custom subcategory must also be assigned to one of the four broad groups (Essentials, Obligatory, Discretionary, or Financial Allocation).

    1.3. The user may delete custom subcategories but may not delete or rename base categories.

2. When a user creates a custom subcategory, the System shall prompt the user to select the appropriate broad group with a brief explanation: "Choose whether this expense is essential for survival, obligatory like rent or debt payments, discretionary like entertainment, or a financial allocation like savings."

3. The System shall not perform automatic categorisation of transactions.

    3.1. All category assignments must be made by the user at transaction entry time.

    3.2. This design choice prioritises user awareness and control over automation, and is supported by literature suggesting that manual logging improves financial mindfulness.

---

## Article V: Financial Flows

### Section 1. Financial Flow State Machine

1. The System shall model financial flows according to a simple state machine.

    1.1. Income. Income transactions add funds to the available balance of the selected account.

    1.2. Expense. Expense transactions subtract funds from the available balance, with the amount allocated to a specific expense category.

    1.3. Savings goal contribution. Savings goal contributions subtract funds from the available balance and add them to the goal's accumulated amount.

    1.4. Debt payment. Debt payments subtract funds from the available balance and reduce the outstanding balance of the specified debt account.

2. No other flows are implemented. All outflows must pass through the available balance of a cash or bank account.

### Section 2. Available Balance

1. Available balance for a given account is defined as the starting balance, plus the sum of all income transactions into that account, minus the sum of all expense transactions from that account, minus the sum of all savings contributions drawn from that account, minus the sum of all debt payments drawn from that account.

    1.1. This calculation may result in a negative value.

2. The System shall permit negative available balances, with the warning and persistent badge mechanisms described in Article II Section 3.

3. Currency and precision. All amounts shall be stored in Philippine pesos as integer centavos (e.g., 100.00 pesos stored as 10000 centavos) to avoid floating‑point rounding errors.

### Section 3. Account

1. The System shall support up to ten user‑defined accounts.

    1.1. Default account. The default first account is named "Cash".

    1.2. Account management. The user may add, rename, or delete accounts at any time, subject to the limit of ten active accounts and the requirement that at least one account remains.

    1.3. Deleting an account. When an account is deleted, all transactions associated with that account must be reassigned to another account before deletion is permitted, or the user may choose to delete the account and all its transactions permanently.

2. Each transaction must be associated with exactly one account.

    2.1. Exception for transfers. Transfer transactions associate with both a source account and a destination account.

    2.2. Separate balances. The System shall compute available balance separately for each account.

    2.3. Net worth effect. Transfers do not affect net worth; they only change the distribution of funds across accounts.

### Section 4. Transaction Recording and Balance Update

1. When a user records a transaction, the System shall update the account balance immediately after validation and confirmation of any negative balance warning.

    1.1. Income. The amount is added to the account balance.

    1.2. Expense. The amount is subtracted.

    1.3. Transfer. The amount is subtracted from the source account and added to the destination account in a single atomic operation.

        1.3.1. If either subtraction would cause a negative balance, the warning and confirmation process applies to the source account.

        1.3.2. The transfer is not partially applied.

2. Recurring transactions scheduled for a future date shall not affect current balances.

    2.1. At the time of automatic generation, the same validation and warning rules apply.

    2.2. If a recurring expense would cause a negative balance:

        2.2.1. The System shall not create the transaction.

        2.2.2. The System shall log the postponement.

        2.2.3. The System shall notify the user.

        2.2.4. The transaction shall be re‑attempted on the next scheduled date.

---

## Article VI: Budgeting Module

### Section 1. Budget Structure

1. 1. Every budget in the System shall consist of the following components.

    1.1. Total budget size. The sum of allocated amounts across all categories for a given budget period.

    1.2. Budget period. A time horizon measured in days, selectable from seven, fourteen, thirty, or ninety days.

    1.3. Per‑category allocation. For each category within the user's selected category set, the budget includes a per‑category allocation expressed in Philippine pesos.

    1.4. Per‑category actual spending. Tracked from expense transactions recorded during the period.

    1.5. Surplus or deficit. Defined as the allocated amount minus the actual spending. A positive value indicates underspending. A negative value indicates overspending.

2. The System shall only create budgets that are feasible, meaning that there exists an allocation satisfying all hard constraints defined in Section 4 of this Article.

3. The user may set total budget size and per‑category allocations and may mark budget categories as protected.

### Section 2. Budget Period

1. The System shall recommend a budget period based on the user's financial behavioral profile.

    1.1. Stable‑Flexible users. Recommended period: thirty days.

    1.2. Stable‑Obligated users. Recommended period: thirty days.

    1.3. Variable‑Flexible users. Recommended period: fourteen days.

    1.4. Variable‑Obligated users. Recommended period: fourteen days.

2. The user may override the recommended period at any time, and the System shall honour the user's selection.

> Note — RRL Validation Required: These period recommendations require validation from literature on budget horizon effectiveness for different income stability profiles.

### Section 3. Budgeting Strategies

1. 1. The System shall offer four budgeting strategy templates that the user may select at budget creation.

    1.1. Fifty‑Thirty‑Twenty strategy. Allocates fifty percent of the total budget to Needs (Essentials + Obligatory combined), thirty percent to Discretionary, and twenty percent to Financial Allocation. Recommended as a general starting point for users with stable income.

    1.2. Zero‑Based strategy. Every peso of income is assigned to a specific category, including savings and debt payments, leaving no unallocated buffer. Recommended for detailed trackers and users with variable income.

    1.3. Savings‑First strategy. The target savings contribution amount is deducted from forecast income first as a hard constraint. The remaining amount is allocated across all expense categories. Recommended for users prioritising savings goals.

    1.4. Custom strategy. The user manually defines percentage allocations per broad group or per category. Recommended for advanced users.

### Section 4. Linear Programming

1. Budget allocations shall be generated using Linear Programming.

    1.1. Objective function. Maximise the sum over categories of the user's declared priority weight for that category multiplied by the allocated amount.

    1.2. Priority range. Priorities range from one (lowest) to five (highest).

2. The default priorities per profile are defined as follows.

    2.1. Stable‑Flexible users: highest priority (five) to Financial Allocation; medium priority (four) to Essentials (specifically Food) and Discretionary (specifically Recreation); low priority (three) to all remaining categories.

    2.2. Stable‑Obligated users: highest priority (five) to Obligatory (specifically Housing and Financial Obligations such as debt minimum payments); medium priority (four) to Essentials (specifically Health) and Financial Allocation; low priority (three) to all remaining categories.

    2.3. Variable‑Flexible users: highest priority (five) to Financial Allocation; medium priority (four) to the entire Essentials group; low priority (three) to all remaining categories.

    2.4. Variable‑Obligated users: highest priority (five) to Obligatory (specifically Housing and Financial Obligations); medium priority (four) to Essentials (specifically Health); low priority (three) to all remaining categories.

3. The user may adjust priorities at any time in the Settings screen.

4. The Linear Programming constraints are as follows.

    4.1. Total budget constraint. The sum of allocations across all categories must equal the forecast income multiplied by (one minus the target savings rate). The target savings rate is a percentage defined by the user, defaulting to ten percent.

    4.2. Obligatory minimum constraint. The allocation to Obligatory categories must be at least the sum of all rent payments, minimum debt payments, insurance premiums, government‑mandated contributions, documented family support, and essential commuting/communication expenses. This is a hard constraint that cannot be relaxed.

    4.3. Financial Allocation minimum constraint. The allocation to Financial Allocation must be at least forecast income multiplied by the target savings rate. This constraint may be relaxed in the infeasibility handling procedure.

    4.4. Combined Needs floor constraint (for the Fifty‑Thirty‑Twenty strategy only). The sum of allocations to Essentials and Obligatory groups must be at least fifty percent of the total budget. For other strategies, the Essentials‑only floor below applies.

    4.4.1. Essentials‑only floor (default for non‑50‑30‑20 strategies). The allocation to the Essentials group must be at least thirty percent of the total budget.

    4.4.2. These floors may be relaxed during infeasibility handling.

    4.5. Discretionary cap constraint. The allocation to the Discretionary group must not exceed thirty percent of the total budget.

    4.6. Per‑category maximum constraint. The allocation to any single detailed category must not exceed a category‑specific maximum derived from the ninetieth percentile of the user's historical spending for that category, based on at least thirty days of data. If insufficient history exists, the maximum defaults to thirty percent of the total budget for Essentials categories and twenty percent for Discretionary categories.

    4.7. Non‑negativity constraint. All category allocations must be greater than or equal to zero.

5. Infeasibility handling. When the Linear Programming problem is infeasible, the System shall apply sequential relaxation.

    5.1. Step 1. Reduce the savings constraint (Financial Allocation minimum) to zero.

    5.2. Step 2. If still infeasible, and the active strategy is Fifty‑Thirty‑Twenty, reduce the combined Needs floor from 50% to 40%, then to 30%, then to 20%, then to 0. If another strategy is active, reduce the Essentials‑only floor from 30% to 20%, then to 10%, then to 0.

    5.3. Step 3. If still infeasible after reducing the floor to zero, remove all floor constraints entirely.

    5.4. Step 4. If the problem remains infeasible with only the Obligatory minimum sum constraint and non‑negativity (which is always feasible), the System shall display the message: "Your fixed obligations exceed your income. Odin recommends debt restructuring or increasing income before a feasible budget can be created."

### Section 5. Surplus Handling

1. At the end of a budget period, any surplus (allocated but unspent amount) shall be handled according to one of three user‑selectable strategies.

    1.1. Rollover strategy. The surplus amount is added to the next period's total budget.

    1.2. Save strategy. The surplus is automatically transferred to the user's primary savings goal as an additional contribution.

    1.3. Reset strategy. The surplus is returned to the available balance, and the next period's budget is recomputed from zero.

2. The default strategy per profile is as follows.

    2.1. Rollover for stable profiles (Stable‑Flexible and Stable‑Obligated).

    2.2. Save for variable profiles (Variable‑Flexible and Variable‑Obligated).

    2.3. The Reset strategy has no default; the user must select it explicitly.

3. At the end of each budget period, the System shall display a prompt: "You underspent by [amount in pesos]. What would you like to do with the leftover amount?" with the three options presented. If the user does not respond within seven days, the System shall apply the default strategy for that user's profile.

> Note — RRL Validation Required: The surplus handling strategies (Rollover, Save, Reset) and their default assignments require validation from literature on user preferences for windfall or surplus allocation.

### Section 6. Explainability.

1. Every budget recommendation shall be accompanied by an explanation in plain language.

    1.1. The explanation shall state the budget period, the total budget amount, the forecast income used, and the target savings amount.

    1.2. The explanation shall then describe the major constraints that shaped the allocation.

        1.2.1. Example: "Your 30‑day budget is 22,500 pesos. This is based on your predicted income of 30,000 pesos and a minimum savings target of 3,000 pesos (10 percent of your income). 11,250 pesos is allocated to Essentials because this category is required to be at least 50 percent of your budget. To change any allocation, adjust your category priorities in Settings."

2. The explanation shall be accessible via a "Why?" button next to the recommended budget.

### Section 7. Module Relationships

1. The budget recommendation module receives the following inputs.

    1.1. Forecast income and category‑level spending forecasts from the LSTM module (Article VII).

    1.2. The user's financial behavioral profile from the Random Forest classifier (Article III), which determines the default priority weights.

2. The budget recommendation is displayed to the user, who may accept, modify, or reject it.

    2.1. Once accepted, the budget becomes active, and actual spending is tracked against it.

3. Overspending alerts (Article XI) compare actual spending to the accepted budget allocations.

> NOTE: Clarification on Obligatory group usage. The budget recommendation module always enforces the Obligatory minimum sum constraint (Section 4.2). This ensures rent, debt payments, and other fixed obligations are funded before any discretionary or savings allocation. When the user selects the Fifty‑Thirty‑Twenty strategy, the combined floor (Essentials+Obligatory ≥ 50%) applies in addition to the minimum sum constraint.

---

## Article VII: Forecasting Module

### Section 1. Forecasting Targets

1. The System shall generate forecasts for four targets, each at configurable granularities and horizons.

    1.1. Target 1: Per‑category expense. Forecast at the level of the four broad groups: Essentials, Obligatory, Discretionary, and Financial Allocation. Forecast granularities: daily, weekly, and monthly aggregates. Horizons: seven, fourteen, thirty, and ninety days.

    1.2. Target 2: Total income. Forecast at daily, weekly, or monthly granularity over horizons of seven, fourteen, thirty, and ninety days.

    1.3. Target 3: Savings balance trajectory. Forecast at daily granularity over a horizon of one hundred eighty days, assuming that the user follows the current budget recommendation.

    1.4. Target 4: Debt remaining balance. Forecast at daily granularity until the projected payoff date, assuming the user follows the selected debt payoff strategy.

2. All forecasts shall include a disclaimer displayed prominently in the forecasting interface: "Forecasts are inferential and informational only, based on your past spending and current budget. Actual future spending may differ."

3. The primary forecast visualization shall include a next‑month multi‑line graph for Essentials, Discretionary, Financial Allocation, and Obligatory spending.

### Section 2. Long Short-Term Memory Algorithm

1. All forecasts shall be generated using a Long Short‑Term Memory (LSTM) network with the following architecture.

    1.1. Input sequence length. Sixty days of daily data.

    1.2. Layer configuration. Two LSTM layers: sixty‑four units in the first layer, thirty‑two units in the second layer.

    1.3. Dropout. A dropout rate of 0.2 applied after each LSTM layer to reduce overfitting.

    1.4. Output layer. Linear activation for regression.

    1.5. Loss function. Huber loss with a delta parameter of 1.0 (less sensitive to outliers than mean squared error).

    1.6. Optimizer. Adam with a learning rate of 0.001.

    1.7. Training parameters. Batch size of thirty‑two for up to one hundred epochs, with early stopping after ten epochs without improvement in validation loss.

2. The input features for the LSTM shall include the following.

    2.1. Daily amounts for each of the four broad groups (Essentials, Obligatory, Discretionary, Financial Allocation).

    2.2. Total daily spending.

    2.3. The user's income amount (updated when new income transactions are recorded).

    2.4. The user's financial behavioral profile label from the Random Forest classifier.

    2.5. Calendar features: day of week (zero to six), day of month (one to thirty‑one).

    2.6. Event flags indicating whether the day is a payday, a declared holiday, within the thirteenth‑month pay period (typically December), or within the Christmas period (December fifteen to January five).

3. Handling insufficient history. For users with fewer than sixty days of history, the LSTM shall use the available data as the input sequence.

    3.1. Missing days before the user's first transaction are set to zero.

    3.2. For users with between thirty and fifty‑nine days of history, the model accepts the variable‑length sequence by masking or by repeating the earliest available values.

    3.3. For users with fewer than thirty days of history, the LSTM is not used. The System falls back to population‑based forecasts as described in Section 3 of this Article.

4. Pre‑training. The LSTM model shall be pre‑trained on synthetic transaction data generated from the BSP Consumer Finance Survey 2021 and the PSA Family Income and Expenditure Survey.

5. Continuous learning. After deployment, the LSTM model shall be retrained weekly on each user's accumulated transaction history, with explicit user consent.

    5.1. Retraining uses a sliding window of the most recent ninety days.

    5.2. The user may opt out of personalisation and continue using the pre‑trained model.

    5.3. This decision replaces the original freeze‑all‑models approach. The PRD requires that forecasts improve as the user logs more transactions. Continuous learning with explicit consent preserves privacy while enabling personalisation.

6. Hosting and inference.

    6.1. The LSTM model shall be hosted on a cloud server (e.g., AWS Lambda or Google Cloud Run) with an inference timeout of 2500 milliseconds.

    6.2. The mobile application shall cache the most recent forecast for each target.

    6.3. When offline, the application shall display cached forecasts with a note stating: "Offline mode — forecasts from [date]."

### Section 3. Cold-Start Fallback

1. For users with fewer than thirty days of transaction history, the System shall use population‑level fallbacks instead of LSTM forecasts.

    1.1. Expense forecasts fallback. Source: Family Income and Expenditure Survey (FIES) category means, stratified by the user's income quintile as reported during onboarding.

    1.2. Income forecasts fallback. Source: BSP Consumer Finance Survey median income by occupation category, stratified by the user's occupation as reported during onboarding.

    1.3. Savings trajectory fallback. Assumes a linear contribution of five percent of monthly income to savings, with no withdrawals.

    1.4. Debt payoff fallback. Uses the user‑entered debt terms (principal, interest rate, minimum payment, due date).

2. Transition to LSTM. When the user accumulates thirty days of transaction history, the System shall automatically switch from fallback forecasts to LSTM forecasts and display a notification: "Odin now has enough data to create personalised forecasts for you."

### Section 4. Explainability

1. Explainability for LSTM forecasts shall use a feature perturbation method rather than SHAP.

    1.1. For each forecast, the System shall measure how the prediction changes when each input feature is shuffled or set to a baseline value. The feature that causes the largest change in prediction is identified as the most influential.

    1.2. For user‑facing explanations, the System shall generate a simple template sentence based on observable patterns.

        1.2.1. Example: "Your Discretionary spending is predicted to increase because your spending in the last seven days is 850 pesos higher than your thirty‑day average."

    1.3. The System shall also state confidence indirectly by comparing the forecast to the user's historical range.

        1.3.1. Example: "Forecast for tomorrow is 1,200 pesos, which is within your typical daily range of 500 to 2,000 pesos."

### Section 5. Evaluation Metrics

1. The forecasting module shall be evaluated weekly using walk‑forward validation on synthetic data.

    1.1. Primary metric: Mean Absolute Error (MAE). Acceptable threshold: less than fifteen percent of the category mean for high‑volume categories (Essentials and Discretionary).

    1.2. Secondary metric: Root Mean Square Error (RMSE). Acceptable threshold: less than twenty percent of the category mean for high‑volume categories.

    1.3. Tertiary metric: Symmetric Mean Absolute Percentage Error (sMAPE). Acceptable threshold for Essentials and Discretionary: less than twenty‑five percent. Acceptable threshold for Obligatory and Financial Allocation: less than thirty percent.

    1.4. Fourth metric: Improvement over Fallback (IoF). Calculated as (MAE of fallback model minus MAE of LSTM model) divided by MAE of fallback model. Acceptable threshold: twenty percent or higher.

    1.5. Fifth metric: Forecast bias. Calculated as the mean of (forecast minus actual) divided by the mean of actual. Acceptable range: between negative 0.10 and positive 0.10.

2. Remedial action. If any metric exceeds its acceptable threshold for three consecutive weeks on the synthetic evaluation, the researchers shall log the issue and consider retraining the model from scratch using a different hyperparameter configuration.

### Section 6. Module Relationships

1. The LSTM forecasting module receives the user's financial behavioral profile from the Random Forest classifier as an input feature (Article III).

2. The forecasted amounts for the four broad groups are passed to the budget recommendation module (Article VI) as the basis for total budget calculation and category floor/cap constraints.

3. The forecasted savings balance trajectory is displayed in the savings goal tracking interface (Article IX).

4. The forecasted debt remaining balance is displayed in the debt management interface (Article X).

5. Anomaly detection note. The Isolation Forest anomaly detection module does not directly consume LSTM forecasts in the thesis version.

---

## Article VIII: Anomaly Detection Module

### Section 1. Anomaly Detection

1. Anomaly detection shall be performed using Isolation Forest, an unsupervised algorithm that isolates anomalies by randomly partitioning the feature space.

2. The model shall operate on a per‑user basis, learning the user's baseline spending behaviour from their transaction history.

3. A minimum of fourteen days of transaction history is required before the Isolation Forest is enabled.

4. For users with fewer than fourteen days, anomaly detection shall be disabled, and only rule‑based budget overspending alerts (described in Section 5 of this Article) shall be shown.

5. The Isolation Forest shall use the following specifications.

    5.1. Number of estimators. One hundred decision trees.

    5.2. Maximum samples per tree. Two hundred fifty‑six, or the total number of transactions if fewer.

    5.3. Random state. Fixed at forty‑two for reproducibility.

    5.4. Contamination rate. The System shall not fix a constant contamination rate. Instead, the System shall use the raw anomaly scores produced by Isolation Forest and apply a dynamic threshold: the top five percent of scores by transaction volume shall be flagged as anomalies.

6. The feature vector for each expense transaction shall consist of eight dimensions, derived from the transaction and the user's historical data. All features shall be normalised or standardised before being passed to the Isolation Forest.

### Section 2. Anomaly Features

1. Each expense transaction shall be evaluated on the following feature vector (8 dimensions).

    1.1. Amount deviation. Calculation: (amount − category_30d_median) / category_30d_IQR, capped at ±5. Interpretation: How unusual the amount is for this category.

    1.2. Day‑of‑period proportion. Calculation: transaction_date_days_into_period / period_total_days. Interpretation: Where the transaction falls within the current budget period.

    1.3. Category velocity. Calculation: number of transactions in this category in the last seven days. Interpretation: Whether the user is spending more frequently than usual.

    1.4. Time since last transaction (same category). Calculation: hours, capped at 168. Interpretation: Unusually long or short gaps between transactions.

    1.5. Day of week. Calculation: 0–6 (Monday to Sunday). Interpretation: Captures weekend vs. weekday spending patterns.

    1.6. Week of month. Calculation: 1–5. Interpretation: Captures monthly bill cycles.

    1.7. Holiday proximity. Calculation: 1 if within ±3 days of a known holiday, else 0. Interpretation: Accounts for expected spending spikes around holidays.

    1.8. Merchant novelty. Calculation: 1 if merchant name not seen in last 60 days, else 0. Interpretation: New merchants are more likely to be anomalous.

### Section 3. Exclusions

1. Certain transactions that would otherwise be flagged as anomalies shall be excluded from alert generation because they represent culturally expected spending spikes.

    1.1. The System shall still compute anomaly scores for these transactions for internal logging, but shall not generate user notifications unless the user has enabled informational alerts.

2. The following periods are excluded from anomaly alerting.

    2.1. Christmas and New Year period. Transactions between December fifteen and January five shall not trigger anomaly alerts.

    2.2. Holy Week. Transactions from Palm Sunday to Easter Sunday shall not trigger alerts. The System shall use an annually updated holiday calendar stored as a JSON configuration file. If the current year's Holy Week dates are not yet loaded, the System shall compute Easter using an algorithmic method (such as the Anonymous Gregorian algorithm) as a fallback.

    2.3. Barangay fiesta. Transactions during the user's declared home barangay fiesta dates, plus or minus three days, shall not trigger alerts. The user may configure their home barangay and fiesta dates in the profile settings.

    2.4. Whitelisted transactions. Transactions manually whitelisted by the user are permanently excluded from anomaly alerts regardless of amount or timing.

3. For excluded transactions, the System may still provide an informational notification if the anomaly score exceeds the threshold, but the notification shall be labelled as informational rather than a warning. The user may configure whether informational alerts are shown.

### Section 4. Whitelist

1. When a transaction is flagged as anomalous, the System shall present the user with a notification stating: "[Amount in pesos] at [merchant name] appears unusual for your [category] spending. Was this expected?"

2. The user may select from three responses.

    2.1. "Yes, expected." The System shall add an entry to the whitelist. Each whitelist entry contains the merchant name, the detailed category of the transaction, and an amount tolerance of plus or minus twenty‑five percent. Future transactions with the same merchant name and same detailed category, and with an amount within the tolerance range, shall be suppressed from anomaly alerts. If the user selects "Always allow this merchant regardless of amount," the whitelist entry stores no amount tolerance, and all future transactions with that merchant name and category are suppressed.

    2.2. "No, unexpected." The transaction remains flagged as an anomaly. No whitelist entry is created.

    2.3. "Remind me later." The notification is dismissed for this transaction. No whitelist entry is created. Future similar transactions may still trigger alerts.

3. The user may view, edit, or delete whitelist entries in Settings under Anomaly Detection → Whitelist.

### Section 5. Overspending Detection

1. In addition to Isolation Forest, the System shall implement rule‑based budget overspending detection as a separate submodule.

    1.1. This submodule does not use machine learning and operates independently of the anomaly detection whitelist or cultural exclusions.

2. The System shall generate an alert when any category exceeds eighty percent of its budget allocation with more than twenty‑five percent of the budget period remaining.

3. The System shall generate a critical alert when any category exceeds one hundred percent of its budget allocation at any time.

4. These overspending alerts are mandatory and cannot be disabled by the user, though the user may configure notification delivery method (in‑app only or push).

### Section 6. Alert Fatigue Prevention.

1. The System shall implement three mechanisms to prevent alert fatigue.

    1.1. Cooldown period. Limit anomaly alerts to no more than three per user per twenty‑four hour period. Rule‑based overspending alerts are excluded from this cooldown.

    1.2. Bundling. Multiple anomalies detected within two hours are bundled into a single notification that lists all affected transactions.

    1.3. Snooze. The user may snooze all anomaly alerts for seven days via Settings → Notifications.

### Section 7. Explainability

1. For each anomaly alert, the System shall compute the deviation of each continuous feature from the user's baseline.

    1.1. Baseline for amount deviation. The category median over the preceding thirty days.

    1.2. Explanation selection. The explanation shall present the feature with the largest standardised deviation.

2. Example explanations.

    2.1. Amount deviation example. "This transaction was flagged because the amount (5,000 pesos) is 2.5 standard deviations above your usual Food spending of 800 pesos."

    2.2. Merchant novelty example. "This transaction was flagged because you have never spent at this merchant before in the last 60 days."

### Section 8. Evaluation

1. The anomaly detection module shall be evaluated on synthetic data using walk‑forward validation with anomalies injected at approximately five percent of transactions.

    1.1. Precision target: at least 0.70.

    1.2. Recall target: at least 0.65.

    1.3. F1 score target: at least 0.675.

    1.4. False positive rate per user per week target: no more than 1.5 false positives per week.

### Section 9. Module Relationships

1. The Isolation Forest anomaly detection module receives the user's financial behavioral profile from the Random Forest classifier (Article III), which is used as a categorical feature.

2. The rule‑based overspending detection submodule receives the current active budget allocations from the budget recommendation module (Article VI).

3. Anomaly alerts and overspending alerts are both passed to the Alerts and Notifications module (Article XI).

4. The user's whitelist entries are stored and consulted before any anomaly alert is generated.

5. Thesis limitation. In the thesis version, the Isolation Forest does not compare transactions against LSTM forecasts.

> Note — Future Work: Incorporating forecasted category spending as an additional feature for anomaly detection is recommended for future versions.

---

## Article IX: Savings Goal Management

### Section 1. Savings Goal

1. A savings goal in the System represents a target amount that the user wishes to accumulate over time through regular contributions.

2. Each goal shall consist of the following required fields.

    2.1. Goal name. A string of up to fifty characters, unique per user.

    2.2. Target amount. Desired total accumulation in Philippine pesos, minimum one hundred pesos, maximum ten million pesos.

    2.3. Target date. The date by which the user wishes to achieve the goal, at least seven days from goal creation date and no more than ten years into the future.

    2.4. Contribution amount. The amount the user commits to contribute per contribution frequency, minimum ten pesos per contribution.

    2.5. Contribution frequency. Selectable from daily, weekly, bi‑weekly, or monthly.

    2.6. Linked source account. The account from which contributions are deducted, defaulting to the user's primary cash account.

3. The System shall treat savings goals as financial allocation targets.

    3.1. Contributions to a savings goal are recorded as expense transactions under the Financial Allocation broad group, with a detailed category named after the goal.

    3.2. When a contribution is made, the System shall subtract the amount from the linked source account's available balance and add it to the goal's current accumulated amount.

### Section 2. Multiple Concurrent Savings Goals

1. The System shall support up to five concurrent savings goals per user.

2. When multiple goals exist, the user shall prioritise them via drag‑and‑drop in the user interface.

3. The System shall apply contributions in priority order during each contribution cycle.

3.1. Contribution cycle definition. The contribution cycle runs daily.

3.2. For each goal, the System checks whether the current date matches the goal's contribution schedule based on its frequency.

4. When a contribution date arrives for a goal, the System shall attempt to deduct the contribution amount from the linked source account.

4.1. If the available balance is sufficient, the deduction occurs and the goal's accumulated amount increases.

4.2. If the available balance is insufficient, the System shall skip the contribution for that goal, proceed to the next lower‑priority goal, and notify the user. The skipped contribution is not queued or retried later.

5. After processing all goals that have a contribution on the current date, any remaining available balance is left untouched for discretionary spending or future contributions.

### Section 3. Progress State

1. For each goal at each contribution date, the System shall compute the progress state as follows.

    1.1. Remaining amount. Target amount minus current accumulated amount.

    1.2. Number of remaining contributions. Calculated as the number of contribution dates between the current date and the target date.

    1.3. Required contribution per period. Remaining amount divided by the number of remaining contributions.

2. State classification based on actual contribution amount (the amount the user has committed to contribute each period, not necessarily the amount actually contributed after skipped contributions).

    2.1. Ahead. Actual contribution amount ≥ 1.10 × required contribution.

    2.2. On track. Actual contribution amount between 0.90 and 1.10 × required contribution.

    2.3. Behind. Actual contribution amount between 0.50 and 0.90 × required contribution.

    2.4. Critical. Actual contribution amount < 0.50 × required contribution.

3. The System shall display a circular progress indicator for each goal, using colour coding: green for ahead or on track, yellow for behind, red for critical.

### Section 4. Savings Goal Strategies

1. The System shall offer three contribution allocation strategies that determine how surplus funds (beyond the scheduled contributions) are distributed across multiple goals.

    1.1. Goal‑based strategy (default for all profiles). Any surplus is allocated to the highest‑priority goal first. After that goal's target is reached, surplus flows to the next‑highest priority goal.

    1.2. Snowball strategy (offered as an alternative for Variable‑Flexible users). The System allocates surplus to the goal with the smallest remaining amount.

    1.3. Avalanche strategy (offered as an alternative for Stable‑Obligated users). The System allocates surplus to the goal with the highest user‑ranked priority.

2. The user may switch strategies at any time via Savings → Strategy.

    2.1. When switching, the System shall recalculate projected completion dates for all goals under the new strategy and display a comparison message.

3. When a budget strategy includes a Financial Allocation portion (e.g., the twenty percent in the Fifty‑Thirty‑Twenty strategy), the System shall distribute that portion across active savings goals according to the selected savings goal allocation strategy.

### Section 5. Notifications

1. The System shall send the following savings‑related notifications.

    1.1. Milestone notifications. When a goal reaches twenty‑five percent, fifty percent, or seventy‑five percent of its target amount.

    1.2. Behind‑schedule advisory. When a goal has been in the "behind" state for seven consecutive days. The notification reappears every seven days until the goal returns to on track or ahead, or until the user updates the goal's parameters.

    1.3. Goal achievement notification. When a goal's accumulated amount reaches or exceeds the target amount.

### Section 6. Module Relationships

1. The savings goal tracking module receives forecasted savings balance trajectory from the LSTM forecasting module (Article VII), which is displayed as a projection line on the goal progress chart.

2. The module also receives the user's available balance from the account management system (Article V) to determine whether scheduled contributions can be fulfilled.

3. When a contribution is skipped due to insufficient balance, the module sends a notification to the Alerts and Notifications module (Article XI).

4. The contribution allocation strategies are evaluated independently; they do not interact with the budget recommendation module's surplus handling strategies (Article VI Section 5), as the two mechanisms operate on different time scales and purposes.

---

## Article X: Debt Management

### Section 1. Debt Account

1. A debt account in the System represents a liability that the user owes to a creditor, with a defined principal, interest rate, and repayment schedule.

2. Each debt account shall consist of the following required fields.

    2.1. Debt name. A string of up to fifty characters, unique per user.

    2.2. Total principal amount. The original amount borrowed, measured in Philippine pesos, minimum one hundred pesos, maximum ten million pesos.

    2.3. Annual interest rate. Stored as a decimal (e.g., 0.05 for five percent). Range: zero to one hundred percent inclusive. The System assumes simple interest for all debt accounts.

    2.4. Minimum monthly payment. The smallest amount the user must pay each month, measured in pesos. May be zero.

    2.5. Payment due day of month. An integer from one to thirty‑one. If the due day is greater than the number of days in a given month, the System shall treat the due date as the last day of that month.

    2.6. Remaining balance. Computed as the principal amount minus the sum of all payments recorded against this debt account, automatically updated whenever a debt payment transaction is recorded.

### Section 2. Debt Payoff Strategies

1. The System shall implement two debt payoff strategies, and the user may switch between them at any time.

    1.1. Avalanche strategy. The System allocates any surplus payment amount (beyond the sum of all minimum monthly payments) to the debt with the highest annual interest rate. This strategy minimises the total interest paid.

    1.2. Snowball strategy. The System allocates surplus payment amount to the debt with the smallest remaining balance, regardless of interest rate. This strategy minimises the time to the first debt payoff.

2. When the user switches from one strategy to another, the System shall recalculate the projected payoff dates and total interest for all debts under the new strategy and display a comparison message. The user must confirm the switch before it takes effect.

3. Definition of surplus payment amount. The user's total available funds allocated to debt repayment in a given month, minus the sum of all minimum monthly payments. The total available funds allocated to debt repayment is determined by the budget recommendation module as part of the Obligatory category allocation. The user may also manually specify a higher debt repayment amount.

### Section 3. Debt Account Projection

1. For each debt account individually, and for the aggregate of all debt accounts, the System shall display the following projections.

    1.1. Remaining balance. Shown in pesos, updated after each payment transaction.

    1.2. Projected payoff date. The date when the remaining balance is expected to reach zero or less, assuming the user makes the minimum monthly payment each month plus any surplus allocated according to the selected payoff strategy.

    1.3. Total interest projected under current strategy. The sum of all future interest payments until payoff.

    1.4. Total interest projected under alternative strategy. Also shown for comparison.

2. The projection calculations assume that the user continues to follow the selected strategy and that no additional debt is incurred. The System shall display a disclaimer: "Projections assume you make all minimum payments on time and do not take on new debt."

### Section 4. Debt Account Minimum Payoff

1. The System shall not permit a recorded monthly debt payment that is below the account's minimum monthly payment unless one of two conditions is met.

    1.1. User override. The user explicitly overrides the minimum payment by confirming a dialog that states: "Paying below the minimum may incur late fees and damage your credit score. Continue anyway? Yes / No."

    1.2. Hardship mode. The user's available balance across all accounts is less than the sum of all minimum payments for the month. The System shall automatically enter hardship mode.

2. When hardship mode is detected, the System shall display a debt hardship screen that includes:

    2.1. A warning that the user's total minimum payments exceed their available balance.

    2.2. A recommendation to contact each creditor, displaying the creditor's name and contact information if the user has provided it.

    2.3. A link to the National Credit Council's debt counselling page if available.

3. The System shall also display an option for the user to proceed with reduced payments by acknowledging: "I understand that paying below the minimum may incur fees and affect my credit score." No automated contact with creditors is made.

### Section 5. Debt Alerts

1. The System shall send the following debt‑related notifications.

    1.1. Upcoming due date reminder. Three days before a debt account's payment due date.

    1.2. Missed payment alert. If the due date passes and no payment has been recorded for that month by the following day.

    1.3. Milestone notification. When a debt account reaches fifty percent paid (remaining balance ≤ half of original principal).

    1.4. Payoff notification. When the remaining balance reaches zero.

2. All debt alerts are delivered via in‑app notification. The user may enable push notifications for debt alerts separately from other alert categories.

### Section 6. Module Relationships

1. The debt management module receives the user's available balance from the account management system (Article V) to validate minimum payments and detect hardship.

2. It receives the forecasted income and the Obligatory category allocation from the budget recommendation module (Article VI) to determine the surplus amount available for debt repayment beyond minimum payments.

3. The debt payoff projections are displayed in the forecasting module's debt remaining balance view (Article VII Section 1).

4. The debt alerts are passed to the Alerts and Notifications module (Article XI).

5. The debt management module does not interact directly with the Random Forest or Isolation Forest models.

---

## Article XI: System Alerts and Notifications

### Section 1. Alerts

1. The System shall generate alerts for five categories, each originating from a specific module.

    1.1. Budget overspending alerts. Originate from the rule‑based overspending detection submodule. Warning when a category exceeds eighty percent of its budget allocation with more than twenty‑five percent of the budget period remaining. Critical alert when any category exceeds one hundred percent of its budget allocation.

    1.2. Anomaly detection alerts. Trigger when the Isolation Forest identifies a transaction as anomalous and the transaction is not excluded by cultural period rules or whitelist.

    1.3. Savings goal milestone alerts. Include alerts at twenty‑five, fifty, and seventy‑five percent progress, as well as goal achievement.

    1.4. Forecast‑based advisory alerts. Provide proactive guidance when current spending patterns suggest a future budget violation.

    1.5. Debt management alerts. Include upcoming due date reminders, missed payment alerts, and payoff milestones.

2. Trigger condition for forecast‑based advisory alerts. The System shall evaluate daily whether the user's current spending trajectory, extrapolated linearly to the end of the budget period, would exceed the total budget by more than ten percent and whether more than fifty percent of the budget period remains. If both conditions are true, the System shall generate an advisory alert.

### Section 2. Alert Delivery

1. All alerts shall be delivered as in‑app notifications, appearing in a notification centre accessible via a bell icon badge on the dashboard. The badge displays a count of unread alerts.

2. If the user grants permission, the System shall also send push notifications to the user's mobile device for all alert categories except forecast‑based advisory, which is in‑app only by default.

3. The user may separately configure push notification preferences per category. Budget overspending alerts are mandatory and cannot be disabled, but the user may choose whether to receive push notifications for them.

### Section 3. Alert Structure

1. Each alert shall contain a title, a body, an action button, and a dismiss button.

    1.1. Title. Briefly identifies the alert category (e.g., "Budget Overspending Warning" or "Unusual Transaction Detected").

    1.2. Body. Provides a specific description (e.g., "You have used 85% of your Food budget with 10 days remaining").

    1.3. Action button. Opens the relevant screen where the user can take corrective action (budget screen, transaction list, forecasting dashboard, savings goal detail, or debt management screen).

    1.4. Dismiss button. Acknowledges the alert and removes it from the notification centre.

2. For anomaly alerts that include whitelist options, the acknowledgment choices ("Yes, expected," "No, unexpected," "Remind me later") are presented within the alert itself.

### Section 4. Alert Configuration

1. Users may configure alert preferences per category in Settings → Notifications, with the following exceptions.

    1.1. Budget overspending alerts. Mandatory; the user cannot disable them but may choose to receive them only in‑app without push notifications.

    1.2. Anomaly detection alerts. The user may enable or disable them entirely, or set them to informational only (no push, only in‑app).

    1.3. Forecast‑based advisory alerts. The user may enable or disable them.

    1.4. Savings milestone alerts. The user may enable or disable them.

    1.5. Debt alerts. The user may enable or disable them.

2. The user may also set a cooldown period for duplicate alerts, ranging from one to twenty‑four hours, which applies to anomaly detection alerts only.

    2.1. Within the cooldown period, if the same category and similar magnitude anomaly occurs again, no new alert is generated.

    2.2. The cooldown is per category, not per merchant or amount.

### Section 5. Alert Persistence and Acknowledgment

1. Unread alerts remain in the notification centre until the user dismisses them or acknowledges them by tapping the action button.

2. Alerts do not expire automatically.

3. When the user taps the action button and performs the suggested action (e.g., viewing the budget screen), the alert is marked as read but remains in the notification centre under a "History" section until manually cleared.

4. For anomaly alerts that include whitelist options, the acknowledgment choices ("Yes, expected," "No, unexpected," "Remind me later") are presented within the alert itself.

    4.1. Selecting "Yes, expected" creates a whitelist entry and dismisses the alert.

    4.2. Selecting "No, unexpected" dismisses the alert without whitelisting.

    4.3. Selecting "Remind me later" dismisses the alert but schedules a reminder notification for the same transaction after twenty‑four hours, unless the user has already whitelisted or dismissed it permanently.

### Section 6. Module Relationships

1. The Alerts and Notifications module receives alerts from:

    1.1. The rule‑based overspending detection submodule (Article VIII Section 5).

    1.2. The Isolation Forest anomaly detection module (Article VIII).

    1.3. The savings goal tracking module (Article IX Section 5).

    1.4. The forecasting module (Article VII Section 1 for advisory alerts).

    1.5. The debt management module (Article X Section 5).

2. The module stores alert history locally on the device and, if the user is logged in, synchronises to the server for multi‑device consistency.

3. The module does not directly interact with the Random Forest or LSTM models except to receive alert triggers.

---

> ^^^ --- Construction Zone End --- ^^^

## ===== Article XXX. Transaction History =====

---

## ===== Article XXXI. Dashboard =====

---

## ===== Article XXXII. Offboarding =====

---

## ===== Article XXXIII. Uninstallation =====

---

> VVV --- Construction Zone Ahead --- VVV

> NOTE: Explainability of each model should be tackled in its own corresponding Article.

## Article XII: Explainability

### Section 1. Explanations

1. All machine learning modules in the System shall provide human‑readable explanations for their predictions and alerts.

2. The explanation method varies by module as defined below.

    2.1. Financial Behavioral Profile classification module (Random Forest). Explainability using SHAP values. The System shall compute SHAP values for each classification prediction and present the top two features that most influenced the classification. The output format shall be a sentence constructed from the feature names and their values.

    2.2. Budget recommendation module (Linear Programming). Explainability by listing the active constraints that shaped the allocation and the user's priority settings. The output format is a template sentence followed by a list of the most binding constraints.

    2.3. Forecasting module (LSTM). Explainability using feature perturbation. For each forecast, the System shall measure how the prediction changes when each input feature is set to a baseline value. The feature causing the largest change is identified as the most influential. The System generates a simple template sentence based on observable patterns.

    2.4. Anomaly detection module (Isolation Forest). Explainability by computing the deviation of each continuous feature from the user's baseline, using pre‑computed summary statistics. The feature with the largest standardised deviation determines the explanation.

3. All explanation outputs shall be stored in the application log for audit purposes, with a retention period of thirty days. After thirty days, the logs shall be anonymised by removing user identifiers and rounding amounts to the nearest hundred pesos.

4. The user may view the explanation for any prediction or alert by tapping a "Why?" button next to the relevant interface element.

### Section 2. Explanations Storage and Retention

1. All explanation outputs shall be stored in the application log for audit purposes, with a retention period of thirty days.

2. After thirty days, the logs shall be anonymised by:

    2.1. Removing user identifiers.

    2.2. Rounding amounts to the nearest hundred pesos.

### Section 3. User Access to Explanations.

1. The user may view the explanation for any prediction or alert by tapping a "Why?" button next to the relevant interface element.

2. The explanation shall be displayed in a modal dialog that also includes a link to Settings → Explainability, where the user can learn more about how the System makes decisions.

### Section 4. Module Relationships

1. The explainability module does not directly connect to other modules except through the storage and retrieval of explanations for display.

2. The SHAP values for classification and the perturbation results for forecasting are computed at prediction time and stored alongside the prediction results.

---

> NOTE: Evaluations of each model and algorithm should be tackled in its own corresponding Article.

## Article XIII: System and Algorithm Evaluation

### Section 1. ISO/IEC 25010:2023 Quality Characteristics.

1. The System shall be evaluated against six quality characteristics from the ISO/IEC 25010:2023 standard, each with a specific measure, acceptable threshold, and evaluation method.

    1.1. Functional suitability.

        1.1.1. Measure: Percentage of specified features that pass manual test cases.
        
        1.1.2. Acceptable threshold: at least ninety‑eight percent.
        
        1.1.3. Evaluation method: Manual test script containing fifty test cases, each mapped to a specific requirement from Articles I through XII.
        
        1.1.4. The test case traceability matrix shall be included in Appendix J of the thesis.

    1.2. Performance efficiency.

        1.2.1. Measure: Time from user action to user interface response at the ninety‑fifth percentile.

        1.2.2. Non‑ML operations (transaction entry, budget viewing, alert acknowledgment): acceptable threshold ≤ 500 milliseconds.

        1.2.3. ML predictions (profile classification, spending forecast, anomaly detection): acceptable threshold ≤ 1500 milliseconds at the 95th percentile, with a maximum acceptable of 3000 milliseconds at the 99th percentile.
        
        1.2.4. Evaluation method: Automated load testing with one hundred iterations per operation.

    1.3. Usability.

        1.3.1. Measure: System Usability Scale (SUS) score.
        
        1.3.2. Acceptable threshold: 68 or higher (industry average).
        
        1.3.3. Stretch goal: 74 or higher (eighty‑fifth percentile).
        
        1.3.4. Evaluation protocol detailed in Section 2 of this Article.

    1.4. Reliability.

        1.4.1. Measure: Mean time between failures during two hours of simulated continuous use.
        
        1.4.2. Acceptable threshold: four hours or more between crashes or unhandled exceptions.
        
        1.4.3. Evaluation method: Running the application through a scripted sequence of user actions and monitoring crash logs.

    1.5. Security.

        1.5.1. Measure: Number of critical vulnerabilities identified per the OWASP Top Ten.
        
        1.5.2. Acceptable threshold: zero critical vulnerabilities.
        
        1.5.3. Evaluation method: Static code analysis and a basic penetration test focused on authentication, data storage, and network communication.

    1.6. Maintainability.

        1.6.1. Measure: Cyclomatic complexity per function, excluding user interface binding code and third‑party library calls.
        
        1.6.2. Acceptable threshold: ten or less for all application business logic functions (transaction validation, budget recalculation, alert generation, feature extraction for ML models).
        
        1.6.3. Exemptions: ML training scripts, Linear Programming solver libraries, and data preprocessing pipelines are exempt. However, wrapper functions that call these libraries shall have cyclomatic complexity of ten or less.
        
        1.6.4. Evaluation method: Static code analysis with a tool such as SonarQube.

> Note — RRL Validation Required: The cyclomatic complexity threshold of ten is provisional and should be validated against software engineering benchmarks for maintainability. The threshold is commonly cited in industry standards; the researchers should cite a relevant source such as McCabe's original paper or a software quality textbook.

### Section 2. System Usability Scale (SUS)

1. The System Usability Scale shall be administered after each participant has used the System actively for fourteen days.

    1.1. Definition of active use. Recording at least ten transaction entries during the fourteen‑day period.

    1.2. If a participant does not reach ten transactions, the SUS shall still be administered at day fourteen, but the transaction count shall be recorded as a covariate in the analysis.

2. Target sample size. Thirty participants.

    2.1. If after four weeks of recruitment the sample size is between twenty and twenty‑nine, the study shall proceed with a post‑hoc power analysis reporting the minimum detectable effect size.

    2.2. The sample shall be stratified by financial behavioural profile, with a minimum of six participants per profile.

        2.2.1. Four profiles × six participants = twenty‑four participants.
        
        2.2.2. The remaining six participants may be from any profile without stratification.

    2.3. Recruitment shall occur from at least four different cities in Metro Manila (e.g., Manila, Quezon City, Makati, Taguig). No minimum number of participants is required per city.

3. Each participant shall complete the standard ten‑item System Usability Scale questionnaire, with items scored on a five‑point Likert scale from strongly disagree to strongly agree.

    3.1. Scoring method (Brooke, 1996).

        3.1.1. For odd‑numbered items: subtract one from the score.
        
        3.1.2. For even‑numbered items: subtract the score from five.
        
        3.1.3. Sum all converted scores.
        
        3.1.4. Multiply the sum by 2.5 to obtain a score from zero to one hundred.

    3.2. The mean score across all participants shall be reported with a confidence interval.

4. The SUS shall be administered in person or via an online form.

    4.1. The researcher shall read the standardised instructions: "Please rate your agreement with the following statements about Odin. There are no right or wrong answers. Your honest feedback helps us improve the system."

### Section 3. Algorithm Evaluation

1. Each machine learning module shall be evaluated using walk‑forward validation on synthetic data.

    1.1. The synthetic dataset shall be generated from the BSP Consumer Finance Survey 2021 and the PSA Family Income and Expenditure Survey.

2. Random Forest classification module.

    2.1. Validation method: Rolling window of sixty days of training data and thirty days of test data, rolling forward by thirty days for six iterations.

    2.2. Primary metrics: Accuracy, precision, recall, and F1 score, each measured per class and macro‑averaged.

    2.3. Acceptable threshold for accuracy: 0.85 or higher.

    2.4. The confusion matrix shall be reported.

    2.5. This evaluation shall be performed before the user study to confirm model performance.

3. LSTM forecasting module.

    3.1. Validation method: Walk‑forward with sixty days of training data and seven days of test data, rolling forward by seven days for twenty‑six iterations.

    3.2. Primary metrics: Mean Absolute Error (MAE) as a percentage of category mean, Root Mean Square Error (RMSE) as a percentage of category mean, and symmetric Mean Absolute Percentage Error (sMAPE).

    3.3. Acceptable thresholds:

        3.3.1. MAE < 15% of category mean for Essentials and Discretionary.
        
        3.3.2. RMSE < 20% of category mean for Essentials and Discretionary.
        
        3.3.3. sMAPE < 25% for Essentials and Discretionary.
        
        3.3.4. sMAPE < 30% for Obligatory and Financial Allocation.

    3.4. Improvement over Fallback (IoF) shall be reported but does not have an acceptability threshold for the thesis. The researchers shall note whether the LSTM outperforms the fallback.

4. Isolation Forest anomaly detection module.

    4.1. Validation method: Walk‑forward with thirty days of training data and seven days of test data, rolling forward by seven days for thirteen iterations.

    4.2. Synthetic test set shall have anomalies injected at approximately five percent of transactions, with amounts two or more standard deviations above the category mean.

    4.3. Primary metrics: Precision, recall, F1 score, and false positive rate per user per week.

    4.4. Acceptable thresholds:

        4.4.1. Precision ≥ 0.70.
        
        4.4.2. Recall ≥ 0.65.
        
        4.4.3. F1 ≥ 0.675.
        
        4.4.4. False positive rate ≤ 1.5 per week.

5. Budget recommendation module (Linear Programming).

    5.1. Evaluation metric: Adherence rate.

        5.1.1. Definition. Percentage of users whose actual spending stays within plus or minus twenty percent of the recommended category allocation for at least three of the four broad groups, averaged over the budget period.

    5.2. Acceptable threshold: seventy percent or higher.

    5.3. The researchers shall also report the manual modification rate (percentage of users who manually adjust the recommended allocation before accepting the budget) as a proxy for recommendation quality.

    5.4. A high modification rate (above fifty percent) suggests that the default priorities or constraints do not match user preferences.

### Section 4. System and Algorithm Failure Conditions

1. The System shall detect and respond to the following failure conditions. For each condition, the detection method, system response, and user notification are defined.

    1.1. LSTM forecast MAE exceeds threshold.

        1.1.1. Detection: MAE exceeds 20% of category mean for any broad group for fourteen consecutive days during synthetic evaluation.
        
        1.1.2. Response: Log a warning visible to the developer in application logs.
        
        1.1.3. Remediation: Researchers may manually retrain the model with different hyperparameters offline.

    1.2. Isolation Forest F1 score falls below threshold.

        1.2.1. Detection: F1 score below 0.6 for seven consecutive days during synthetic evaluation.
        
        1.2.2. Response: Log a warning. The System shall continue to use Isolation Forest for anomaly detection.
        
        1.2.3. Note: In a deployed version, the System would disable Isolation Forest and revert to rule‑based overspending alerts only, but this is not implemented in the thesis.

    1.3. Random Forest accuracy falls below threshold during development.

        1.3.1. Detection: Accuracy below 0.80 after a retraining run (development only, not during user evaluation).
        
        1.3.2. Response: Do not deploy the new model. Retain the previous model. Alert the developer.
        
        1.3.3. This condition is not applicable during user evaluation because no retraining occurs.

    1.4. Unhandled exception at runtime during user evaluation.

        1.4.1. Detection: Any module throws an unhandled exception.
        
        1.4.2. Response: Catch the exception, log it, and continue with graceful degradation.
        
        1.4.3. Forecasting module exception: Display fallback message: "Forecasts are temporarily unavailable. Please check your internet connection and try again later."
        
        1.4.4. Anomaly detection module exception: Do not show anomaly alerts until the next restart. Display: "Spending alerts are temporarily simplified. Your data is safe."
        
        1.4.5. Classification module exception: Use the last known profile. Display: "Your financial profile is using saved data. Some recommendations may be less accurate."

2. Disaster recovery and backup plan.

    2.1. Automated daily backups of the server database shall be retained for thirty days.

    2.2. The user may export all their transaction data as a CSV file via Settings → Export Data.

    2.3. The user may import a previously exported CSV file to restore data after account deletion or device change.

    2.4. A developer restore procedure shall be documented in the system administrator manual.

    2.5. This backup mechanism is for data loss scenarios such as server corruption or user error, not for real‑time synchronisation.

### Section 5. Module Relationships

1. The evaluation framework described in this article is not a runtime module but a development‑time and evaluation‑time protocol.

2. The metrics defined here are computed offline using Python scripts on synthetic data, or manually during user evaluation for the System Usability Scale.

3. The results of evaluation shall be reported in the thesis findings chapter.

4. No runtime module consumes these metrics; they are for research purposes only.

---

## Article XIV: Data Privacy, Security, and Ethical Compliance

### Section 1. Compliance with RA 10173 (Data Privacy Act of 2012).

1. The System shall comply with the Data Privacy Act of 2012 in all aspects of personal financial data processing.

2. Consent. Consent shall be obtained via an explicit opt‑in screen shown before the user can enter any transaction.

    2.1. The opt‑in screen shall state: "Odin collects and processes your financial transactions to provide budget recommendations, spending forecasts, anomaly detection, and profile classification. Your data is stored encrypted and is not shared with third parties. You may delete your data at any time."

    2.2. The user must tap "I agree" to proceed; declining prevents use of the application.

3. Purpose limitation. Data shall be used only for generating budget recommendations, producing spending forecasts, detecting anomalous transactions, classifying financial behavioural profiles, and displaying transaction history.

4. Retention period. Twenty‑four months from the date of the user's last activity (any transaction entry, budget change, or login).

    4.1. After twenty‑four months of inactivity, the user's data shall be anonymised as follows: user identifier replaced with a random non‑reversible token, transaction amounts rounded to the nearest one hundred pesos, transaction dates truncated to the month only, and all merchant names and descriptions deleted.

    4.2. If the user has not given explicit opt‑in for anonymised research use, the data shall be permanently deleted instead of anonymised.

5. Data portability. The user may request a CSV export of all their transactions via Settings → Export Data. The export file shall be generated within five minutes and downloadable via a secure link that expires after twenty‑four hours.

6. Data deletion. The user may request deletion of all their data via Settings → Delete Account. Upon confirmation, the System shall immediately delete all user data from the local device and send a deletion request to the server. The server shall complete deletion within seven days, and the user shall receive an email confirmation if an email address was provided.

7. Anonymised research use (separate opt‑in). The System shall obtain separate explicit opt‑in consent on a distinct screen during onboarding. The opt‑in screen shall state: "Allow Odin to use your anonymised data to improve financial models for all users? Your data will be stripped of all identifiers, amounts will be rounded, and dates will be truncated to month. This does not identify you personally. You may opt out at any time in Settings."

### Section 2. Data Security

1. The System shall implement the following technical security controls.

    1.1. In‑transit encryption. All communications between the mobile application and the server shall use TLS version 1.3 minimum.

    1.2. At‑rest encryption on server. Stored transaction data shall be encrypted using AES‑256‑GCM.

    1.3. Key management. Encryption keys shall be managed using a key management service and shall not be stored in source code.

2. Local storage on mobile device. The System shall use an encrypted SQLite database via SQLCipher with a 256‑bit key derived from the user's six‑digit PIN or biometric authentication using PBKDF2 with 100,000 iterations.

3. Authentication. The user shall set a six‑digit PIN during onboarding. If the device supports biometric authentication, the user may enable biometric login as an alternative. The System shall lock after five failed authentication attempts and require a thirty‑second cooldown.

4. Pseudonymisation before server upload. The System shall pseudonymise user data using a salted hash: SHA‑256 of the user's local unique identifier concatenated with a per‑device salt stored only on the device. The server cannot reverse the hash to obtain the original user identifier.

### Section 3. Data Privacy

1. The following statement is added as a clear ethical declaration, replacing the original freeze‑all‑models statement:

    1.1. "For the duration of this thesis, all machine learning models are pre‑trained on synthetic data generated from BSP CFS 2021 and PSA FIES. With explicit user consent, models may be personalised using each user's own transaction data through continuous learning (weekly retraining for LSTM on a sliding window of ninety days; monthly retraining for Random Forest on a sliding window of 365 days). No user data is shared between users. Raw transaction data never leaves the device for training purposes; only aggregated features are used for server‑side personalisation. Users may opt out of personalisation at any time and continue using the pre‑trained synthetic model. For users who do not opt in, all models remain frozen on synthetic pre‑training."

2. Institutional ethics clearance shall be obtained from the University of Makati Research Ethics Committee prior to any user data collection for the study.

3. The System shall display the following disclaimer on first launch in a modal dialog that the user must scroll to the bottom and tap "I understand" before proceeding:

4. "Odin's predictions and recommendations are for informational purposes only. You retain full responsibility for all financial decisions. Odin is not a financial advisor. Do not make major financial decisions solely based on automated outputs."

### Section 4. Module Relationships

1. The privacy and security controls described in this article are implemented at the infrastructure and application layers.

2. They affect how data flows between modules.

    2.1. For example, the pseudonymised user identifier is used by the server to retrieve the correct stored data for each user, but the server never sees the raw user identifier.

3. The encryption requirements apply to the local storage used by all modules (transactions, budgets, goals, debts).

4. The consent and deletion mechanisms affect the data lifecycle for all user data collected by any module.

5. No machine learning module has special access beyond the feature vectors described in Section 3 of this Article.

---

## Article XV: System Scope and Delimitations

1. The following features and capabilities are explicitly excluded from the System for the thesis version.

    1.1. Bank or e‑wallet API integration.

    1.2. Optical character recognition of receipts.

    1.3. CSV or spreadsheet import.

    1.4. Automatic transaction import.

    1.5. Investment tracking for stocks, mutual funds, cryptocurrency, or any asset with variable returns.

    1.6. Multi‑currency support. The System operates exclusively in Philippine pesos.

    1.7. Non‑Filipino users.

    1.8. Users outside Metro Manila (for thesis validation).

    1.9. Automated bill payment.

    1.10. Credit score monitoring.

    1.11. Tax computation.

    1.12. Dedicated paluwagan module (users may create a custom subcategory under Financial Allocation).

    1.13. Credit card accounts (users must record credit card payments as expenses at the time of payment).

    1.14. Compound interest for revolving debt (all debts modelled with simple interest).

    1.15. Admin dashboards for banks or financial advisers.

    1.16. Social or gamified features.

    1.17. Public marketplace deployment beyond what is needed for thesis evaluation.

---

## Article XVI: Definitions of Terms

1. For the purpose of this specification, the following terms have the meanings assigned.

    1.1. Available balance.

        1.1.1. The sum of a specific account's starting balance plus all income transactions minus all expense transactions minus all savings contributions minus all debt payments, as defined in Article V Section 2.
        
        1.1.2. Available balance may become negative, in which case the System displays a persistent warning badge.
        
        1.1.3. This definition supersedes any prior contradictory statements.

    1.2. Behavioural drift (concept drift).

        1.2.1. A statistically significant change in any classification feature over a sixty‑day sliding window, detected by a Mann‑Whitney U test with a significance level of p < 0.05.
        
        1.2.2. The two windows compared are non‑overlapping (e.g., days one through sixty compared with days sixty‑one through one hundred twenty).

    1.3. Budget feasibility.

        1.3.1. A binary property indicating whether a set of budget allocations satisfies all hard constraints defined in Article VI Section 4, including debt minimum payments, savings minimum, and group floors and caps.
        
        1.3.2. A budget that violates any hard constraint is infeasible.

    1.4. Budget infeasibility.

        1.4.1. The condition in which no allocation satisfies all hard constraints simultaneously.
        
        1.4.2. The System handles infeasibility through sequential relaxation as described in Article VI Section 4, culminating in a message recommending debt restructuring or income increase if even the relaxed constraints cannot be satisfied.

    1.5. Budget period.

        1.5.1. The time horizon over which a budget applies, measured in days.
        
        1.5.2. The System supports periods of seven, fourteen, thirty, and ninety days.
        
        1.5.3. The recommended period depends on the user's financial behavioural profile.

    1.6. Coefficient of variation (CV).

        1.6.1. The standard deviation of monthly net income divided by the mean monthly net income, used to classify income stability.
        
        1.6.2. A CV below 0.25 indicates Stable income; a CV of 0.25 or above indicates Variable income.
        
        1.6.3. This threshold is provisional and requires validation from research.

    1.7. Cold‑start period.

        1.7.1. Subdivided into three phases.
        
        1.7.2. Profile cold‑start: First seven days of transaction history or until the user has at least five income transactions, whichever is longer. During this phase, classification uses the onboarding questionnaire.
        
        1.7.3. Forecasting cold‑start: First thirty days of transaction history. During this phase, forecasts use population fallbacks from FIES and BSP surveys.
        
        1.7.4. Anomaly detection cold‑start: First fourteen days of transaction history. During this phase, Isolation Forest is disabled and only rule‑based overspending alerts are shown.

    1.8. Debt hardship.

        1.8.1. A condition automatically detected when the user's available balance is less than the sum of all minimum monthly payments for debts due in the current month.
        
        1.8.2. Upon detection, the System displays a hardship screen with creditor contact information and a recommendation to seek counselling.

    1.9. Expense category.

        1.9.1. A classification label assigned to a financial transaction, grounded in the 2020 Philippine Classification of Individual Consumption According to Purpose.
        
        1.9.2. The System uses thirteen base categories with subcategories, as listed in Article IV Section 1.

    1.10. Financial behavioural profile (FBP).

        1.10.1. A classification of a user based on income stability (Stable or Variable) and obligation level (Flexible or Obligated).
        
        1.10.2. The four profiles are Stable‑Flexible, Stable‑Obligated, Variable‑Flexible, and Variable‑Obligated.

    1.11. Forecast bias.

        1.11.1. A metric calculated as the mean of (forecast minus actual) divided by the mean of actual, expressed as a decimal.
        
        1.11.2. An acceptable range is between negative 0.10 and positive 0.10, indicating no systematic over‑forecasting or under‑forecasting.

    1.12. Improvement over Fallback (IoF).

        1.12.1. A metric calculated as (Mean Absolute Error of fallback model minus MAE of LSTM model) divided by MAE of fallback model, expressed as a percentage.
        
        1.12.2. A positive value indicates that the LSTM outperforms the fallback.

    1.13. Isolation Forest.

        1.13.1. An unsupervised anomaly detection algorithm that isolates anomalies by randomly partitioning feature space.
        
        1.13.2. The System uses a per‑user Isolation Forest with one hundred estimators and a dynamic anomaly threshold based on the top five percent of anomaly scores.

    1.14. Linear Programming (LP).

        1.14.1. A mathematical optimisation method used to allocate budget amounts across categories subject to constraints, maximising a weighted sum of category allocations where the weights are user‑defined priorities.

    1.15. LSTM (Long Short‑Term Memory).

        1.15.1. A type of recurrent neural network suited to learning from sequential time‑series data.
        
        1.15.2. The System uses a two‑layer LSTM with input sequence length of sixty days to forecast daily spending across four broad groups.

    1.16. Obligation ratio.

        1.16.1. The sum of unavoidable monthly expenses divided by total monthly income, averaged over the preceding sixty days.
        
        1.16.2. A ratio below 0.50 indicates Flexible; a ratio of 0.50 or above indicates Obligated.
        
        1.16.3. This threshold is provisional and requires validation from research.

    1.17. Paluwagan.

        1.17.1. An informal rotating savings and credit association practised in the Philippines.
        
        1.17.2. The System does not include a dedicated module for paluwagan. Users may approximate it via a custom subcategory under Financial Allocation, but this treatment is acknowledged as a limitation. A dedicated tracker is recommended as future work.

    1.18. Personal finance management system (PFMS).

        1.18.1. A software system designed to help individuals track, plan, and manage personal income, expenses, savings, and debt.

        1.18.2. Odin is one such system.

    1.19. Pseudonymisation.

        1.19.1. The processing of personal data such that the data can no longer be attributed to a specific data subject without the use of additional information, which is kept separately and subject to technical and organisational measures.

        1.19.2. The System implements pseudonymisation for server uploads using a salted hash of the user identifier, with the salt stored only on the device.

    1.20. Random Forest.

        1.20.1. An ensemble machine learning algorithm that constructs multiple decision trees and aggregates their outputs for classification.

        1.20.2. The System uses Random Forest for financial behavioural profile classification.

    1.21. sMAPE (symmetric Mean Absolute Percentage Error).

        1.21.1. A forecasting accuracy metric calculated as the average of the absolute difference divided by the average of the forecast and actual values, expressed as a percentage.

        1.21.2. It is used for low‑volume categories where MAE may be misleading.

    1.22. Surplus handling strategies.

        1.22.1. The three methods by which the System treats unspent budget amounts at the end of a budget period.
        
        1.22.2. Rollover. Adds the surplus to the next period's total budget.
        
        1.22.3. Save. Transfers the surplus to the user's primary savings goal.
        
        1.22.4. Reset. Returns the surplus to available balance and recomputes the next period's budget from zero.
        
        1.22.5. Default strategies are assigned by financial behavioural profile.

    1.23. Walk‑forward validation.

        1.23.1. A time‑series model evaluation method in which the model is trained on past data and tested on successive future periods, rolling forward incrementally.
        
        1.23.2. The System uses walk‑forward validation for all machine learning modules on synthetic data.

    1.24. Whitelist.

        1.24.1. A user‑maintained list of merchant‑category pairs that are exempt from anomaly detection alerts.

        1.24.2. Whitelist entries may include an amount tolerance of plus or minus twenty‑five percent, or may be set to always allow regardless of amount.

---

## Article XVII: Testing Decisions

### Section 1. Testing Philosophy

1. Tests shall verify external behavior and user-visible outcomes, not internal implementation details.

### Section 2. Transaction Ledger Tests

1. Transaction ledger tests shall cover creating, editing, deleting, filtering, recurring generation, transfer handling, and balance effects.

### Section 3. Category Taxonomy Tests

1. Category taxonomy tests shall cover detailed-to-broad mappings, protected-category defaults, Filipino-context categories, and category validation.

### Section 4. Profile Module Tests

1. Profile module tests shall cover initial classification, explanation generation, reclassification triggers, and user confirmation behavior.

### Section 5. Budget Recommendation Tests

1. Budget recommendation tests shall cover protected categories, profile-specific allocations, surplus behavior, deficit behavior, recommendation explanations, and user overrides.

### Section 6. Forecasting Tests

1. Forecasting tests shall cover cold-start fallback, personalized-forecast availability, forecast metadata, per-category outputs, total outputs, and forecast consumption by dashboard and budget modules.

2. Forecasting UI tests shall verify that the next-month graph renders all four broad-category lines and remains readable on mobile.

### Section 7. Anomaly Detection Tests

1. Anomaly detection tests shall cover high category deviation, high income-ratio spending, recurring-payment suppression, user whitelisting, culturally expected exception behavior, and alert explanation output.

### Section 8. Savings Goal Tests

1. Savings goal tests shall cover goal creation, contributions, progress states, target-date projections, prioritization, and completion behavior.

### Section 9. Debt Management Tests

1. Debt management tests shall cover debt account creation, minimum payments, Avalanche order, Snowball order, projected payoff dates, and strategy switching.

### Section 10. Alerts Tests

1. Alerts tests shall cover alert creation, acknowledgement, cooldowns, notification preferences, grouped alerts, and suppression rules.

### Section 11. Reporting Tests

1. Reporting tests shall cover budget-vs-actual, forecast-vs-actual, category summaries, date filters, savings progress, and debt progress.

### Section 12. Authentication and Privacy Tests

1. Authentication and privacy tests shall cover login, logout, protected routes, consent state, account deletion flow, and sensitive-data access rules.

### Section 13. Mobile-First UI Tests

1. Mobile-first UI tests shall cover core workflows on narrow viewports: onboarding, add transaction, dashboard, budget recommendation, forecast, alerts, savings, debt, and settings.

### Section 14. Web UI Tests

1. Web UI tests shall cover dashboard, reports, transactions, budget, forecast, savings, debt, and settings on larger viewports.

### Section 15. Integration Tests

1. Integration tests shall cover the main data flow: onboarding to profile, profile to transaction logging, transactions to forecasts, forecasts to budget recommendation, transactions to anomaly alerts, and alerts to user feedback.

### Section 16. Model Evaluation

1. Model evaluation shall be separate from UI tests.

2. Forecasting shall be evaluated using time-series-appropriate metrics such as MAE, RMSE, and related forecast-error measures.

3. Anomaly detection shall be evaluated using precision, recall, and F1-score.

4. Profile classification shall be evaluated using classification metrics if the classifier remains in scope.

### Section 17. Usability Evaluation

1. Usability evaluation shall use SUS for the complete user-facing app.

### Section 18. Software Quality Evaluation

1. Software quality evaluation shall map ISO 25010 characteristics to concrete testable criteria.

---

## Article XVIII  – Out of Scope

1. The following features are explicitly out of scope for the first full-app PRD and thesis implementation:

    1.1. Bank API integration

    1.2. E-wallet API integration

    1.3. OCR or receipt scanning

    1.4. Automatic transaction import

    1.5. Investment portfolio management

    1.6. Multi-currency support

    1.7. Licensed financial advice, investment advice, retirement planning, or legal/tax advice

    1.8. Users outside the Filipino young professional target demographic

    1.9. Geographic generalization beyond Metro Manila for the thesis scope

    1.10. Full production-grade fraud detection

    1.11. Merchant-level enrichment from third-party providers

    1.12. Social or gamified features unless separately approved

    1.13. Admin dashboards for banks, institutions, or financial advisers

    1.14. Public marketplace deployment requirements beyond what is needed for thesis evaluation

---

# PAPER SPECIFICATION

---

## Article I: Introduction Section

### Section 1. Background

1. The Background subsection shall contain at least the following elements.

    1.1. Domain context. Overview of personal finance management in the Philippines, including prevalence of financial distress among young adults (cite BSP CFS 2021, PSA data).

    1.2. Problem space. Discussion of budgeting, saving, and debt management challenges specific to Metro Manila working young adults (age 20‑40).

    1.3. Existing solutions. Survey of existing PFM apps (both international and local) and their limitations for Filipino users.

2. Length requirement. Minimum 500 words, maximum 1000 words.

### Section 2. Problem Statement

1. The Problem subsection shall be structured as follows.

    1.1. General problem. A single sentence stating the overarching problem the System addresses.

        1.1.1. Example: "Filipino working young adults lack access to a personal finance management system that adapts to their variable income patterns, cultural spending norms, and behavioral profiles."

    1.2. Specific problems. Enumerated list (3‑5 items) of sub‑problems, each mapped to a system module.

### Section 3. Objectives.

1. General objective. "To design, implement, and evaluate Odin, a personal finance management system for Filipino working young adults in Metro Manila using Random Forest, LSTM, and Isolation Forest algorithms."

2. Specific objectives. Enumerated list (5‑8 items), each corresponding to a system module or evaluation activity.

    2.1. Each objective must be verifiable and mapped to a metric in Article XIII of the System Specification.

### Section 4. Significance.

1. The Significance subsection shall list primary and secondary beneficiaries.

    1.1. Primary beneficiaries. Filipino working young adults (age 20‑40, Metro Manila).

    1.2. Secondary beneficiaries.

        1.2.1. Researchers in financial technology for developing economies.
        
        1.2.2. PFM app developers targeting Southeast Asian markets.
        
        1.2.3. Policymakers interested in financial inclusion metrics.

### Section 5. Scope and Delimitations.

1. Scope (inclusions). Reference Article XV of the System Specification but restate in prose.

2. Delimitations (exclusions). Reference Article XV exclusions of the System Specification.

### Section 6. Definition of Terms.

1. Reproduce the terms from Article XVI of the System Specification that appear in the paper.

---

## Article II: Review of Related Literature (RRL) Topics

### Section 1. Topic Organization.

1. The RRL chapter shall be organized into exactly 12 topics as listed below.

2. For each topic, the paper shall contain:

    2.1. A minimum of 10 peer‑reviewed citations (except where local data is scarce, in which case government reports and conference proceedings are acceptable).

> NOTE: The minimum are actually as follows:
> Local studies: Philippines-based, does NOT discuss or utilize algorithms or models; at least 25 total.
> International studies: NOT Philippines-based, does NOT discuss or utilize algorithms or models; at least 25 total.
> Algorithm-specific:
    > Random Forest: At least 10 each for local and int'l; 20 total.
    > LSTM: At least 10 each for local and int'l; 20 total.
    > Isolation Forest: At least 10 each for local and int'l; 20 total.
    > Linear Programming: ACTUALLY this is debatable; does not technically classify as a computer algorithm or model, technically mathematical; can be classified as rule-based though; Can instead research rule-based budget recom. algos.; at least 10 each for local and int'l; 20 total.

    2.2. A synthesis paragraph that identifies gaps that Odin addresses.

    2.3. A table or figure summarizing key findings (where appropriate).

### Section 2. The Twelve Topics.

1. Topic 1. Filipino Working Young Adults and the Financial Problem.

2. Topic 2. Filipino Cultural Context in Personal Finance.

3. Topic 3. Expense Categorization in Personal Finance Systems.

4. Topic 4. Existing Personal Finance and Budget Management Systems.

5. Topic 5. Financial Behavioral Profiling.

6. Topic 6. Spending Forecasting.

7. Topic 7. Budget Recommendation.

8. Topic 8. Anomalous Spending Detection.

9. Topic 9. Mobile‑First Design.

10. Topic 10. Data Privacy, Security, and User Trust.

11. Topic 11. User Retention and Engagement.

12. Topic 12. System Evaluation.

---

## Article III: Research Methodology

### Section 1. Research Paradigm.

1. The study shall adopt a pragmatist paradigm (mixed methods) combining quantitative (ML metrics, SUS) and qualitative (thematic analysis of feedback).

### Section 2. Research Design.

1. The research design shall be developmental, with the following phases.

    1.1. Requirements analysis.

    1.2. Synthetic data generation.

    1.3. Algorithm prototyping.

    1.4. System development (Agile, 2‑week sprints).

    1.5. Internal testing.

    1.6. User evaluation.

### Section 3. Agile Development Methodology.

1. The team shall use Scrum with 2‑week sprints.

> NOTE: No. Just normal agile.

### Section 4. Evaluation Design.

1. ISO 25010 shall be operationalized via test cases.

2. SUS shall be administered after 14 days of use.

3. ML metrics shall be computed via Python on synthetic data.

### Section 5. Data Collection for ML Training.

1. Primary data source. Synthetic data from BSP CFS 2021 and PSA FIES 2018.

2. Secondary data source (optional). Pre‑survey of 50‑100 Filipino working young adults.

3. Tertiary data source (pilot). Up to 10 pilot users with consent, used only for final inference evaluation, not training.

### Section 6. Ethical Considerations.

1. The following ethical requirements shall be met.

    1.1. Informed consent obtained from all participants.

    1.2. Compliance with RA 10173 (Data Privacy Act).

    1.3. Anonymization of user data as specified in System Specification Article XIV.

    1.4. Ethics clearance from UMak Research Ethics Committee.

    1.5. App disclaimer displayed on first launch.

---

> NOTE: There's no Chapter 4 and 5.

## Article IV: Expected Outcomes and Contribution

1. The thesis shall produce the following outputs.

    1.1. Functional Odin application.

    1.2. Random Forest classifier (accuracy ≥ 0.85).

    1.3. LSTM forecasting model (sMAPE < 25% / 30% as per category).

    1.4. Isolation Forest anomaly detector (F1 ≥ 0.675).

    1.5. LP‑based budget recommendation (adherence ≥ 70%).

    1.6. Thesis manuscript.

    1.7. Public GitHub repository.

---

## Article V: Thesis Timeline

1. The following milestones and durations shall be used.

Milestone	Duration
RRL completion (12 pillars)	8 weeks
Synthetic data generation	2 weeks
Algorithm prototyping	4 weeks
System development (4 sprints)	8 weeks
Internal testing	2 weeks
User evaluation (SUS + ML metrics)	3 weeks
Thesis writing and revision	6 weeks
Final defense preparation	2 weeks

2. A Gantt chart shall be included in the final paper.

---

---

## Article VII: References Style

1. References shall follow APA 7th edition.

2. Minimum 60 references, of which at least 40 shall be peer‑reviewed journal articles or conference proceedings.

> NOTE: Update the references minimum.

---

## Article VIII: Appendices Required

1. The following appendices shall be included.

Appendix	Content
A	Onboarding questionnaire
B	SUS survey form
C	User consent form (English and Tagalog)
D	Synthetic data generation code (Python)
E	Hyperparameter tuning grids
F	Walk‑forward validation results (tables)
G	System architecture diagram
H	Database schema
I	User manual
