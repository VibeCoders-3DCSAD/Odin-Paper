# Development of Odin: A Personal Finance Management System for Filipino Working Young Adults Using Random Forest, LSTM, and Isolation Forest

---

**Document Type:** Technical Specification

**Version:** 2.0

**Date:** 2026-06-03

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

# SYSTEM SPECIFICATION

---

## Article I: Platform and Target Users

### Section 1. Platform Requirements.

The System shall be implemented as a mobile-first application. The System must be accessible via web browser on desktop devices, but all core user flows (transaction entry, budget viewing, alert acknowledgment) shall be fully operable on a mobile screen width of 375dp or less.

The mobile interface shall be tested on the following Android devices:

> TODO: Define Android devices used in system evaluation.

Layout shall adapt to any width between 320dp and 450dp without horizontal scrolling for core flows. Desktop web version shall use a centered container (max-width 1200px) with multi-column layouts.

### Section 2. Target User Definition.

The System is designed exclusively for the following user population:

- **Demographic scope:** Filipino working young adults aged 20 to 40 years inclusive
- **Geographic scope:** Metro Manila (all 16 cities and 1 municipality)
- **Employment status:** Currently employed (full-time, part-time, self-employed, freelancer, contractual, gig economy)

---

## Article II: Input Methods and Transaction Types

### Section 1. Permitted Input Methods.

The System shall accept financial data through exactly two input methods:

1. **Manual transaction**
    - Description: User types transaction details manually and directly
    - Required fields:
        - Amount
        - Category
        - Date
        - Account
        - Merchant name (optional)
        - Description (optional)
2. **Recurring transaction**
    - Description: User defines a repeating transaction pattern
    - Required fields:
        - Amount
        - Category
        - Frequency
        - Start date, end date (optional)
        - Account

> ASK: (JOAQUIN): Are all three transaction types considered in the two input methods?
> ANS: (): ___

### Section 2. Transaction Types.

The System shall support exactly three transaction types:

1. **Income**
    - Description: A cash inflow into an account
    - Direction: Source → Available balance
    - Recurring supported: Yes (daily, weekly, monthly, yearly, custom)
    - Examples:
        - Salary
        - Freelance payment
        - Remittance
2. **Expense**
    - Description: A cash outflow from an account
    - Direction: Available balance → Expense category
    - Recurring supported: Yes (daily, weekly, monthly, yearly, custom)
    - Examples:
        - Groceries
        - Rent
        - Electricity bill
        - Debt repayment
        - Savings deposit
3. **Transfer**
    - Description: A transfer of cash amounts from one account to another
    - Direction: Account → Account
    - Recurring supported: Yes (daily, weekly, monthly)
    - Examples:
        - Moving money from "Cash" account to "E-Wallet" account

> ASK: (JOAQUIN): Putting the required fields in Section 1 instead of here implies that all three transaction types follow the prescribed fields in the input methods. Is that really appropriate?
> ANS: (): ___

### Section 3. Manual Entry Workflow.

Manual transaction entry shall include the following fields:

- Amount
- Category
- Date
- Account
- Merchant name (free text, max 100 characters, optional but recommended)
- Description (optional)

> NOTE: Some of the fields are not included in Section 1.

If merchant name is not provided, the merchant novelty feature for anomaly detection defaults to 0.

> NOTE: The footnote above should be moved to the anomaly detection section instead.

Upon entering a transaction, the System shall:

1. Validate that amount:
    - Greater than PHP 0.00 for income and expense
    - Amount may be positive or negative for transfer.

> ASK: (JOAQUIN): Are those two validation criteria the only ones needed? And why can amount transferred be negative?
> ANS: (): ___

2. For expense, validate that:
    - Available balance after deduction is greater than or equal to 0. If violation, reject with an error message.

> NOTE: It should send a warning message instead, and prompt the user to confirm deduction and subsequent negative balance. Include in the balance feature the ability to display negative balance, and persistent warning badges or notifications that the balance is negative and that a re-assessment and recalibration of actual present funds should be done. There are situations that could lead to this, caused by forgetting to input incomes and such, and supported by the fact that the systme relies on manual transaction entry and no external validation other than user's account of current balance.

3. For income, add amount to available balance.

> NOTE: The expense and transfer transactions were not included here. I've created a placeholder.

4. For expense, subtract amount from available balance.
5. For transfer, subtract amount from source account's balance, and add amount to destination account's balance.
6. Store transaction with timestamp (ISO 8601).

> ASK: (JOAQUIN): Does it truly end there?
> ANS: (): ___

### Section 4. Recurring Transaction Rules.

The System shall generate recurring transactions automatically at the scheduled frequency. If a generated transaction would violate available balance (for expense or transfer), the System shall postpone the transaction and notify the user. The system shall then re-attempt on the next scheduled date and time.

User may pause, edit, or delete any recurring template at any time.

> NOTE: The footnote above should be moved to Section 5.

### Section 5. Transaction Editing and Deletion.

Users may edit or delete any transaction (including recurring transactions) at any time. When a transaction is edited or deleted, the following procedures are done:

- Available balance shall be recomputed immediately.
- All downstream models (profile classification, forecasting, anomaly detection) shall be asynchronously re-trained or re-evaluated within 24 hours.
- Budget actuals shall be updated.
- The user shall be notified: "Transaction changed. Odin will update your forecasts within 24 hours."

Users may not edit or delete transactions older than 13 months (retention limit).

---

## Article III: User Classification and Financial Behavioral Profiles

### Section 1. Profile Taxonomy.

The System shall classify each user into exactly one of four financial behavioral profiles, determined by two binary dimensions:

1. **Income stability**
    - Values:
        - Stable (S)
        - Variable (V)
2. **Obligation level**
    - Values:
        - Flexible (F)
        - Obligated (O)

The four profiles are: Stable-Flexible (S-F), Stable-Obligated (S-O), Variable-Flexible (V-F), Variable-Obligated (V-O).

### Section 2. Income Stability Thresholds.

Income stability shall be determined by the coefficient of variation (CV) of monthly net income over the preceding 90 days:

- **Stable:** CV < 0.25 (25%)
- **Variable:** CV ≥ 0.25

> NOTE: The proposed coefficient of variation of 0.25 is a placeholder. The true value must be discovered by the researchers based on surveys and analyses of related datasets.

For cold-start (first **7 days** of transaction history), classification shall use onboarding questionnaire responses. The CV threshold of 0.25 is derived from BSP Consumer Finance Survey 2021 median income variability among employed Metro Manila respondents. This threshold shall be adjustable via system configuration without code change.

> ASK: (JOAQUIN): Will 7 days truly suffice? That is something we need to discover or verify through research. The mention of 0.25 being derived from the BSP CFS is unverified. Can the source passage or inference be provided here?
> ANS: (): ___

### Section 3. Obligation Level Thresholds.

Obligation level shall be determined by the obligation ratio (OR): total unavoidable monthly expenses divided by total monthly income, averaged over 60 days:

- **Flexible:** OR < 0.50
- **Obligated:** OR ≥ 0.50

> NOTE: The proposed obligation ratio of 0.50 is a placeholder. The true value must be discovered by the researchers based on surveys and analyses of related datasets.

Unavoidable expenses are defined as:

- Rent/mortgage
- Utilities minimum payments
- Debt minimum payments
- Insurance premiums
- Government-mandated contributions (SSS, PhilHealth, Pag-IBIG)
- Documented family support (e.g., monthly remittance to parents)

> ASK: (JOAQUIN): Is this an exhaustive list of unavoidable expenses? What literature/study/report backs this up?
> ANS: (): ___

For cold-start, OR shall be estimated from onboarding questionnaire.

### Section 4. Reclassification Triggers.

The System shall re-evaluate profile classification when any of the following conditions are met:

- Income CV changes by ±0.10 or more from classification baseline, sustained over 60 consecutive days
- Obligation ratio changes by ±0.15 or more from classification baseline, sustained over 60 consecutive days

> ASK: (JOAQUIN): What is the justification for the reclassification baseline values of income CV and obligation ratio? What about for the days sustained?
> ANS: (): ___

- User explicitly requests reclassification via settings menu
- Ninety (90) days have elapsed since last classification (periodic refresh)

> NOTE: It would help if it could be research how long do behavioral profiles typically change or shift on average. That could be the baseline length for the periodic refresh.

Upon trigger detection, the System shall generate a reclassification recommendation and present it to the user with an explanation using SHAP values (see Section 5). No automatic reclassification shall occur without explicit user confirmation.

If the user does not respond to a reclassification recommendation within 30 days, the System shall display a persistent notification (cannot be dismissed without action) on the dashboard: "Your financial behavior appears to have changed. Odin recommends updating your profile. Apply now?" If the user still does not respond after 7 more days, the System may automatically apply the reclassification and log the event. The user can revert the change in Settings.

> NOTE: "the System may automatically apply the reclassification" contradicts with "No automatic reclassification shall occur without explicit user confirmation".

### Section 5. Classification Algorithm.

Classification shall be performed using a Random Forest classifier with the following specifications:

- Minimum of 100 decision trees
- Maximum depth of 10 levels
- Gini impurity as split criterion
- Class weights balanced (to address potential profile imbalance in training data)

> ASK: (JOAQUIN): Balanced how? What is potential profile imbalance in training data?
> ANS: (): ___

- Random state fixed at 42 for reproducibility

> ASK: (JOAQUIN): Is the random state for testing purposes only?
> ANS: (): ___

**Features for classification** (shall include at minimum):

1. **Income CV (30d, 60d, 90d)**
    - Source: User transactions
    - Data type: Continuous
2. **Obligation ratio (30d, 60d, 90d)**
    - Source: User transactions
    - Data type: Continuous
3. **Income frequency (payments per 30d)**
    - Source: User transactions
    - Data type: Integer
4. **Income amount variance (mean absolute deviation)**
    - Source: User transactions
    - Data type: Continuous
5. **Fixed expense count (distinct payees with recurring flag)**
    - Source: User transactions
    - Data type: Integer
6. **Savings rate (savings/income, 30d)**
    - Source: User transactions
    - Data type: Continuous
7. **Transaction regularity score (entropy of inter-transaction intervals)**
    - Source: User transactions
    - Data type: Continuous

> ASK: (JOAQUIN): Are these the only features? Are source and data types the only properties? What is a continuous and integer data type in the context of features?
> ANS: (): ___

The System shall provide SHAP (SHapley Additive exPlanations) values for each classification prediction, presented as: "Your profile is [PROFILE] mainly because [FEATURE] was [VALUE], which differs from typical [OTHER PROFILE] users by [DIFFERENCE]."

### Section 6. Cold-Start Classification (Onboarding Questionnaire).

During onboarding (first 7 days), the System shall classify the user via a questionnaire containing at least the following items:

1. **Is your monthly income roughly the same each month?**
    - Response options:
        - Yes
        - No
    - Maps to: Income stability
2. **By how much does your income typically vary?**
    - Response options:
        - <10%
        - 10-25%
        - 25-50%
        - Greater than 50%
    - Maps to: CV estimate

> PROP: It could be hard for users to think about the exact percentage their income varies. I propose to ask the user beforehand their salary amount/income amount. Maybe their latest one if they are Variable. Then, on this question, display the actual amount variation (e.g., for a salary of 25k, <10% becomes 22.5k-27.5k).

3. **What percentage of your income goes to bills you cannot skip?**
    - Response options:
        - <30%
        - 30-50%
        - 50-70%
        - >70%
    - Maps to: Obligation ratio

> PROP: Ibid.

4. **Do you have dependents (children, parents, siblings)?**
    - Response options:
        - Yes (number:___)
        - No
    - Maps to: Obligation weight

> ASK: (JOAQUIN): Does the number of dependents influence obligation weight? What is the difference between obligation weight and ratio?
> ANS: (): ___

5. **Do you have any loans or debts with minimum monthly payments?**
    - Response options:
        - Yes
        - No
    - Maps to: Obligation weight

> ASK: (JOAQUIN): Does this not just fall under question 3?
> ANS: (): ___

> NOTE: The actual values in the questionnaire need to be backed up by research.

The System shall compute an initial profile from these responses and present it to the user for confirmation.

> NOTE: There needs to be a section detailing how the computation of the initial profile is done.

---

## Article IV: Expense Categories

### Section 1. Base Category Taxonomy.

The System shall implement the following 13 expense categories and their respective subcategories, grounded in the 2020 Philippine Classification of Individual Consumption According to Purpose and cross-validated against BSP CFS 2021:

> NOTE: Just recently learned about the PCOICOP. Jackpot! That's what we'll use for the expense category taxonomy.

1. FOOD AND NON-ALCOHOLIC BEVERAGES
    - FOOD
    - NON-ALCOHOLIC BEVERAGES
    - SERVICES FOR PROCESSING PRIMARY GOODS FOR FOOD AND NON-ALCOHOLIC BEVERAGES
2. ALCOHOLIC BEVERAGES, TOBACCO AND NARCOTICS
    - ALCOHOLIC BEVERAGES
    - ALCOHOL PRODUCTION SERVICES
    - TOBACCO
    - NARCOTICS
3. CLOTHING AND FOOTWEAR
    - CLOTHING
    - FOOTWEAR
4. HOUSING, WATER, ELECTRICITY, GAS AND OTHER FUELS
    - ACTUAL RENTALS FOR HOUSING
    - IMPUTED RENTALS FOR HOUSING
    - MAINTENANCE, REPAIR AND SECURITY OF THE DWELLING
    - WATER SUPPLY AND MISCELLANEOUS SERVICES RELATING TO THE DWELLING
    - ELECTRICITY, GAS AND OTHER FUELS
5. FURNISHINGS, HOUSEHOLD EQUIPMENT AND ROUTINE HOUSEHOLD MAINTENANCE
    - FURNITURE, FURNISHINGS, AND LOOSE CARPETS
    - HOUSEHOLD TEXTILES
    - HOUSEHOLD APPLIANCES
    - GLASSWARE, TABLEWARE AND HOUSEHOLD UTENSILS
    - TOOLS AND EQUIPMENT FOR HOUSE AND GARDEN
    - GOODS AND SERVICES FOR ROUTINE HOUSEHOLD MAINTENANCE
6. HEALTH
    - MEDICINES AND HEALTH PRODUCTS
    - OUTPATIENT CARE SERVICES
    - INPATIENT CARE SERVICES
    - OTHER HEALTH SERVICES
7. TRANSPORT
    - PURCHASE OF VEHICLES
    - OPERATION OF PERSONAL TRANSPORT EQUIPMENT
    - PASSENGER TRANSPORT SERVICES
    - TRANSPORT SERVICES OF GOODS
8. INFORMATION AND COMMUNICATION
    - Information and communication equipment
    - SOFTWARE EXCLUDING GAMES
    - INFORMATION AND COMMUNICATION SERVICES
9. RECREATION, SPORT AND CULTURE
    - RECREATIONAL DURABLES
    - OTHER RECREATIONAL GOODS
    - GARDEN PRODUCTS AND PETS
    - RECREATIONAL SERVICES
    - CULTURAL GOODS
    - CULTURAL SERVICES
    - NEWSPAPERS, BOOKS AND STATIONERY
    - PACKAGE HOLIDAYS (S)
10. EDUCATION SERVICES
    - EARLY CHILDHOOD AND PRIMARY EDUCATION
    - SECONDARY EDUCATION  (S)
    - POST-SECONDARY NON-TERTIARY EDUCATION (S)
    - TERTIARY EDUCATION (S)
    - EDUCATION NOT DEFINED BY LEVEL (S)
11. RESTAURANTS AND ACCOMMODATION SERVICES
    - FOOD AND BEVERAGE SERVING SERVICES
    - ACCOMMODATION SERVICES
12. INSURANCE AND FINANCIAL SERVICES
    - INSURANCE
    - FINANCIAL SERVICES
13. PERSONAL CARE, SOCIAL PROTECTION AND MISCELLANEOUS GOODS AND SERVICES
    - PERSONAL CARE
    - OTHER PERSONAL EFFECTS
    - SOCIAL PROTECTION
    - OTHER SERVICES

### Section 2. Category Aggregation into Groups.

For budget recommendation and visualization, categories shall be aggregated into three groups:

| Group | Member Categories | Aggregation Rule |
|-------|-------------------|------------------|
| Essentials | FOOD, HOUSING, HEALTH, FINANCIAL_OBLIG | Sum of category amounts |
| Lifestyle | ALCOHOL, CLOTHING, FURNISHINGS, RECREATION, RESTAURANT, MISC | Sum of category amounts |
| Enablers | TRANSPORT, COMMS, EDUCATION, SAVINGS | Sum of category amounts |

> PROP: I propose a better aggregation of the categories into distinctive groups (e.g., Essentials, Discretionary) that use non-jargon plain language that users can easily understand.

### Section 3. User Category Overrides.

Users may create up to 5 custom subcategories under any base category. Custom subcategories must be mapped to exactly one base category for aggregation purposes. Users may not delete base categories. Category ambiguity (e.g., "Is coffee a FOOD or RESTAURANT?") shall be resolved by the user at transaction entry time via category selection; the System shall not auto-categorize.

> ASK: (JOAQUIN): Do they not have permission to make groups, categories, and subcategories? Will that over-complicate things?
> ANS: (): ___

---

## Article V: Financial Flows and Balance Model

### Section 1. Financial Flow State Machine.

The System shall model financial flows according to the following state machine:

```
Income → Available Balance
Available Balance → Expense Category (any)
Available Balance → Savings Goal (contribution)
Available Balance → Debt Payment (principal + interest)
```

No other flows (e.g., direct expense from savings goal) shall be implemented.

> ASK: (JOAQUIN): Really? This is an exhaustive list of states?
> ANS: (): ___

### Section 2. Available Balance Definition.

Available balance is defined as:

```
Available Balance   = Starting Balance 
                    + sum(Income transactions) 
                    − sum(Expense transactions) 
                    − sum(Savings contributions) 
                    − sum(Debt payments)
```

Available balance shall never be negative. All amounts in PHP, stored as integer centavos (e.g., 100.00 = 10000 centavos) to avoid floating-point errors.

> NOTE: The available balance SHOULD be able to become negative, as discussed earlier.

### Section 3. Account Separation.

The System shall support up to 5 user-defined accounts. Each transaction must be associated with exactly one account. The available balance is computed per account. The user may transfer between accounts without affecting net worth.

> ASK: (JOAQUIN): Why only 5 Accounts?
> ANS: (): ___

> PROP: I propose that the first default account is named "Cash".

---

## Article VI: Budget System

### Section 1. Budget Structure.

Every budget shall consist of:

- Total budget size (in PHP)
- Budget period (time horizon in days: 7, 14, 30, or 90)
- Per-category allocation (PHP amount per category, summing to total budget size)
- Per-category actual spending (tracked from expense transactions)
- Surplus/deficit = allocated − actual (per category and total)

> ASK: (JOAQUIN): Is this an exhaustive list of the properties of a Budget? Also, what is surplus/deficit, and how is it relevant in the system?
> ANS: (): ___

### Section 2. Budget Period Selection.

The System shall recommend a budget period based on user profile:

1. **Stable-Flexible**
    - Recommended period: 30 days
    - Justification: Monthly salary cycle typical
2. **Stable-Obligated**
    - Recommended period: 30 days
    - Justification: Monthly obligations align
3. **Variable-Flexible**
    - Recommended period: 14 days
    - Justification: Shorter horizon reduces forecast error
4. **Variable-Obligated**
    - Recommended period: 14 days
    - Justification: Shorter horizon reduces forecast error

> NOTE: Needs citations from RRL.

Users may override the recommended period at any time.

### Section 3. Budgeting Strategy Templates.

The System shall offer the following configurable budgeting strategy templates (benchmarked from RRL and existing PFM apps):

1. **50/30/20**
    - Allocation rule: 50% Essentials, 30% Lifestyle, 20% Savings
    - Best for:
        - General recommendation
        - Stable income

> ASK: (JOAQUIN): Why is this the general recommendation? What is the basis?
> ANS: (): ___

2. **Zero-based**
    - Allocation rule: Income − Expenses = 0 (every peso assigned)
    - Best for:
        - Detailed trackers
        - Variable income

> ASK: (JOAQUIN): Aren't all budgeting strategies zero-based? Don't all of them assign every peso to a group or category in the budget?
> ANS: (): ___

3. **Pay-yourself-first**
    - Allocation rule: Savings deducted first, remainder for expenses
    - Best for:
        - Users prioritizing savings goals

> ASK: (JOAQUIN): Isn't this called reverse budgeting?
> ANS: (): ___

3. **Custom**
    - Allocation rule: User-defined percentages per group
    - Best for:
        - Advanced users

> ASK: (JOAQUIN): The fundamentals of the budget formation is: (a) budget taxonomies (groups, categories), (b) allocation (percentage or absolute amount per group and category), (c) hierarchy (which allocation is fulfilled first), (d) budget horizon (how long that budget is worth for, before it is refreshed). Are these properties correct? Are they only and exactly what is needed? Is it correct to say these are the constraints that the LP will deal with? Were there any properties omitted? What other concerns are there?
> ANS: (): ___

> NOTE: These budgeting strategies need validation from the RRL and benchmarks that they truly are the widely used strategies in the Filipino context.

The user may select a template at budget creation. The System shall convert the template into LP constraints. The user may edit any allocation manually after generation.

### Section 4. Budget Recommendation Algorithm.

Budget allocations shall be generated using Linear Programming (LP) with the following objective and constraints:

> GLOBAL: There are numerous instances where terminologies for a concept are used interchangeably. There should be definite and exact terms that have uppercase first letters. For example. To denote the budget in its base essence, we use Budget. To denote the process of creating the Budget, we use Budget Formation. To denote the Budget as formatted, styled, and structured by the LP algorithm, we use Budget Recommendation.

**Objective:** Maximize `sum(utility(category) × allocation[category])` where `utility(category)` is user-declared priority (1-5). Default priorities per profile are defined below.

1. **Stable-Flexible**
    - High-priority categories (5):
        - SAVINGS
    - Medium (4)
        - FOOD, RECREATION
    - Low (3)
        - All others
2. **Stable-Obligated**
    - High-priority categories (5):
        - FINANCIAL_OBLIG, HOUSING
    - Medium (4)
        - HEALTH, SAVINGS
    - Low (3)
        - All others
3. **Variable-Flexible**
    - High-priority categories (5):
        - SAVINGS
    - Medium (4)
        - ESSENTIALS group
    - Low (3)
        - All others
4. **Variable-Obligated**
    - High-priority categories (5):
        - FINANCIAL_OBLIG, HOUSING
    - Medium (4)
        - HEALTH
    - Low (3)
        - All others

> NOTE: The categories listed above does not match the previously defined categories.

> ASK: (JOAQUIN): What about utilities 2 and 1?
> ANS: (): ___

> NOTE: The prioritization of budget categories also needs to be backed up by research.

Users may adjust priorities in Settings. The interface shall include a brief explanation: "Higher priority categories get more budget, subject to spending caps."

**Constraints:**

1. `sum(allocation[category]) = forecast_income × (1 − savings_rate_target)` across all categories
2. `allocation[FINANCIAL_OBLIG] ≥ minimum_debt_payments + insurance_premiums` (hard constraint)
3. `allocation[SAVINGS] ≥ forecast_income × 0.10` (minimum savings rate, may be reduced by user override)
4. `allocation[ESSENTIALS_GROUP] ≥ 0.50 × (forecast_income × (1 − savings_rate_target))` (spending floor)
5. `allocation[LIFESTYLE_GROUP] ≤ 0.30 × (forecast_income × (1 − savings_rate_target))` (spending cap)
6. `allocation[category] ≥ 0` for all categories
7. If user selected "Pay-yourself-first": `allocation[SAVINGS] ≥ target_contribution_amount` (hard constraint)
8. `allocation[category] ≤ max_spending_per_category` where `max_spending_per_category` is derived from the 90th percentile of the user's historical spending for that category (or 50% of total budget if no history). This prevents any single category from dominating.

> NOTE: The explanation of the constraints needs to be better, clearer, and in plain language yet maintaining complexity. The fields and equations also need to be explain; for example, I have no idea what savings_rate_target is, nor why the 1st equation is what it is.

**Infeasibility handling (sequential relaxation):**

> NOTE: Define infeasibility, or, rather, Budget Infeasibility, or even just Budget Feasibility, as a binary concept and terminology.

If the LP is infeasible:
1. Reduce savings constraint (3) to zero.
2. If still infeasible, reduce Essentials floor (4) from 50% to 40%, then 30%, then 20%.
3. If still infeasible at 20%, drop the Essentials floor entirely.
4. If still infeasible, the System shall display: "Your minimum debt payments and essential expenses exceed your predicted income by PHP[X]. Odin cannot create a balanced budget. Please consider debt restructuring or income increase. Contact a financial counselor if needed."

> NOTE: We have to be careful with how we handle Budget Infeasibility, and, again, we have to substantiate this process with research.

The LP shall then be run with only the debt minimum constraint and non-negativity, which is always feasible.

### Section 5. Surplus Handling.

At the end of a budget period, surplus (allocated but unspent amount) shall be handled per user selection from three strategies (benchmarked from RRL on reset vs. carryforward logic):

> NOTE: Correct me (Joaquin) if I'm wrong, but surplus handling is a new concept in Odin. We'll have to back this up with research as usual.

1. **Rollover**
    - Rule: Surplus added to next period's total budget
    - Default: Stable profiles
1. **Save**
    - Rule: Surplus automatically transferred to primary savings goal
    - Default: Variable profiles
1. **Rollover**
    - Reset: Surplus returned to available balance, next period budget recomputed from zero
    - Default: None (user must select)

The System shall display the end-of-period surplus with the prompt: "You underspent by PHP[X]. What would you like to do with the leftover amount?" with the three options. If user does not respond within 7 days, default strategy per profile applies.

> NOTE: Ensure that these are verified and validated with research as actual surplus handling strategies.

Under Rollover strategy, the surplus amount is added to the next period's total budget. Category allocations for the next period shall be recomputed using the LP with the increased total budget, preserving the same allocation ratios (or applying updated user priorities). The surplus is not tied to specific categories.

> GLOBAL: These enumerations should have their own heading or subsection, to include prose-style descriptions instead of relying on outlines and bullet-points.

### Section 6. Explainability.

Every budget recommendation shall be accompanied by an explanation in the following form:

"Your [PERIOD]-day budget is PHP[TOTAL]. This is based on your predicted income of PHP[INCOME] and minimum savings of PHP[SAVINGS]. PHP[ESSENTIALS_AMOUNT] is allocated to Essentials because this category is required at [PERCENTAGE]% of your budget. To change any allocation, adjust your category priorities in Settings."

Additional explanation: "The budget recommendation maximizes your stated priorities. If you set FOOD priority to 5, the system will allocate as much as possible to FOOD without exceeding your Lifestyle group cap (30% of total) or your historical maximum for FOOD. To balance spending, adjust category priorities or set manual caps."

> NOTE: For me (Joaquin), the explanations need to be better, less specific to one thing, and more encompassing of all details of the Budget Recommendation.

---

## Article VII: Forecasting Module

### Section 1. Forecasting Targets.

The System shall generate forecasts for the following four targets:

1. **Per-category expense**
    - Granularity:
        - Daily, weekly, monthly
    - Horizon (days):
        - 7, 14, 30, 90
    - User-selectable: Yes (total or per-category view)
2. **Total income**
    - Granularity:
        - Daily, weekly, monthly
    - Horizon (days):
        - 7, 14, 30, 90
    - User-selectable: Yes
3. **Savings balance trajectory**
    - Granularity:
        - Daily
    - Horizon (days):
        - 180
    - User-selectable: Yes
4. **Debt remaining balance**
    - Granularity:
        - Daily
    - Horizon (days):
        - Until projected payoff date
    - User-selectable: Yes

> NOTE: Again, the terminologies are a bit inconsistent here. Properties should be checked for exhaustiveness and validity from RRL.

### Section 2. Forecasting Algorithm.

All forecasts shall be generated using an LSTM (Long Short-Term Memory) architecture with the following specifications:

- Input sequence length: 60 days (configurable)
- Number of LSTM layers: 2
- Units per layer: 64 (first), 32 (second)
- Dropout rate: 0.2 after each LSTM layer
- Output activation: Linear (for regression)
- Loss function: Huber loss (δ = 1.0)
- Optimizer: Adam (learning rate = 0.001)
- Batch size: 32
- Epochs: 100 with early stopping (patience = 10)

> NOTE: Personally, the way these specifications are formatted feel bare. Maybe implement subsections?

**Training regime:** The System shall maintain a **global LSTM model** pre-trained on synthetic data (BSP/PSA). Weekly, the global model shall be fine-tuned (3 epochs, learning rate 0.0001) on each user's data individually. This reduces compute from hours to seconds per user. Retraining from scratch shall occur only when model architecture changes.

> GLOBAL: Model/algorithm design, development, and implementation plans were discussed by Joaquin and Charles. The outcome of the discussion is laid out in `model-training-data-design.md`. If not in context yet, be sure to ask for it.

**Deployment:** The LSTM model shall be hosted on a cloud server (AWS Lambda or Google Cloud Run) with inference timeout 2500ms. The mobile app shall cache the most recent forecast for each target. If offline, the app shall display cached forecasts with a note: "Offline mode — forecasts from [DATE]." No forecast shall be attempted from the mobile device directly.

### Section 3. Cold-Start Fallback.

For users with fewer than 30 days of transaction history (forecasting cold-start period), the System shall use population-level fallbacks:

1. **Expense forecasts**
    - Fallback source: FIES 2018 category means
    - Stratification: User's income quintile from onboarding
2. **Income forecasts**
    - Fallback source: BSP CFS 2021 median by occupation
    - Stratification: Occupation category from onboarding
3. **Savings trajectory**
    - Fallback source: 5% of monthly income contributed linearly
    - Stratification: None
4. **Debt payoff**
    - Fallback source: User-entered debt terms (interest, minimum payment)
    - Stratification: None

> NOTE: Terms are inconsistent, properties need to be exhaustive, properties need to be supported with research.

> GLOBAL: I made this global comment to address all enumerations. Check if terms are inconsistent, properties are exhaustive, and properties are supported with research. Ensure that properties are described with clearer plain language but maintains the same complexity. Ensure that subsections are used for clarity.

Fallback shall be replaced by user-specific LSTM predictions when 30 days of user data are available. The System shall notify the user: "Odin now has enough data to create personalized forecasts for you."

### Section 4. Explainability.

Explainability for LSTM forecasts shall use temporal attention weights (extracted from a trained attention layer added to the LSTM) or feature perturbation (measure prediction change when each input feature is shuffled). SHAP shall NOT be used for LSTM due to computational constraints. The simpler method: "Your [CATEGORY] spending is predicted to increase because your spending in the last 7 days is [X] higher than your 30-day average."

### Section 5. Evaluation Metrics.

The forecasting module shall be evaluated weekly using walk-forward validation on synthetic data.

1. **Mean Absolute Error (MAE)**
    - Formula: (1/n) × Σ|actual − forecast|
    - Acceptable threshold: < 15% of category mean
    - Action if exceeded for 3 weeks: Retrain model; if persists, revert to fallback
2. **Root Mean Square Error (RMSE)**
    - Formula: √[(1/n) × Σ(actual − forecast)²]
    - Acceptable threshold: < 20% of category mean
    - Action if exceeded for 3 weeks: Same as above
3. **Symmetric Mean Absolute Percentage Error (sMAPE)**
    - Formula: (1/n) × Σ(|actual−forecast|/(|actual|+|forecast|)/2) × 100
    - Acceptable threshold: < 25% (except HEALTH, FINANCIAL_OBLIG, SAVINGS: <30%)
    - Action if exceeded for 3 weeks: Same as above
4. **Improvement over fallback (IoF)**
    - Formula: (MAE_fallback − MAE_LSTM) / MAE_fallback × 100%
    - Acceptable threshold: ≥ 20%
    - Action if exceeded for 3 weeks: If IoF < 20% after 30 days, log warning; consider model retraining
5. **Forecast bias**
    - Formula: Mean(forecast − actual) / mean(actual)
    - Acceptable threshold: Between −0.10 and +0.10
    - Action if exceeded for 3 weeks: Persistent bias indicates systematic error

> ASK: (JOAQUIN): Why 3 weeks specifically?
> ANS: (): ___

Bias = (1/n) Σ ((forecast_t − actual_t) / actual_t). Acceptable range: systematic error <10% in either direction.

Compute IoF at day 30 for each user using their first 30 days of data (fallback vs LSTM trained on days 1-30, test on days 31-37).

> NOTE: These two footnotes need to be in their respective evaluation metrics, preferably in subsections.

---

## Article VIII: Anomaly Detection Module

### Section 1. Primary Detection Method.

Anomaly detection shall be performed using Isolation Forest with the following specifications:

- Contamination rate: 0.05 (expect 5% of transactions anomalous)
- Number of estimators: 100
- Max samples: 256 (or number of transactions if fewer)
- Random state: 42

> NOTE: Same stuff as last time.

The Isolation Forest shall operate on a per-user basis, learning the user's baseline spending behavior from their transaction history (minimum 14 days required). For users with <14 days, anomaly detection shall be disabled and replaced by rule-based budget overspending alerts only.

> NOTE: Actually, the budget overspending feature is always present. The anomaly detection and overspending detection features are separate. We can just simply say that there is no cold-start fallback for Isolation Forest.

### Section 2. Features for Anomaly Detection.

Each expense transaction shall be evaluated on the following feature vector (8 dimensions):

1. **Amount deviation**
    - Calculation: (amount − category_30d_median) / category_30d_IQR (capped at ±5)
2. **Day-of-period proportion**
    - Calculation: transaction_date_days_into_period / period_total_days
3. **Category velocity**
    - Calculation: number of transactions in category last 7 days
4. **Time since last transaction (same category)**
    - Calculation: hours (capped at 168)
5. **Day of week**
    - Calculation: 0-6 (Monday-Sunday)
6. **Week of month**
    - Calculation: 1-5
7. **Holiday proximity**
    - Calculation: 1 if within ±3 days of known holiday, else 0
8. **Merchant novelty**
    - Calculation: 1 if merchant name not seen in last 60 days, else 0

> NOTE: Properties need description as usual. Better to aggregate factors that affect anomaly detection (i.e., holidays, seasonalities, etc.) into one singular term (e.g., Event or Occasion or etc).

*Day-of-period proportion* is calculated based on the user's currently active budget period. If the user has no active budget, the System defaults to a 30-day rolling period starting from the first day of the current month. The period resets when the user creates a new budget or at the end of the default rolling period.

> NOTE: This footnote should have gone to the description instead.

### Section 3. Excluded Events (Culturally Expected Spending Spikes).

The following transactions shall NOT be flagged as anomalies regardless of Isolation Forest score, based on RRL on Filipino cultural spending patterns:

- Transactions between December 15 and January 5 (Christmas and New Year)
- Transactions during Holy Week (exact dates vary yearly; the System shall use a manually maintained JSON configuration file)
- Transactions during user's declared home barangay fiesta dates (±3 days, user-configurable in profile)
- Transactions manually whitelisted by user (see Section 4)

> PROP: I think the anomaly detection module should still detect anomalies during these occasions, but, instead of sending out warnings, it could send out information notifs. In this way, the user isn't blindsided by the system, and anomalies hiding in these seasonalities can still be detected.

The System shall maintain a built-in holiday calendar for Metro Manila, pre-loaded with fixed holidays (e.g., Dec 25, Jan 1) and movable holidays (e.g., Holy Week) for the current and next year. The calendar shall be updated annually via a manual configuration file (JSON) that the development team updates based on official PSA proclamations. A fallback rule shall exclude any transaction between March 25 and April 10 if the year's Holy Week dates are not yet loaded.

> PROP: I propose that the system connects to a calendar or holiday API instead.

### Section 4. Whitelist Mechanism.

When a transaction is flagged as anomalous, the System shall present the user with a notification: "PHP[AMOUNT] at [MERCHANT] appears unusual for your [CATEGORY] spending. Was this expected?" The user may select:

- **"Yes, expected"** → Add to whitelist: all future transactions with same merchant name and within ±25% amount shall be suppressed from anomaly alerts.
- **"No, unexpected"** → Keep as anomaly; no whitelist entry.
- **"Remind me later"** → Dismiss notification but do not whitelist.

Whitelist entries shall be stored per user and may be viewed/edited in Settings → Anomaly Detection → Whitelist.

> ASK: (JOAQUIN): What do whitelist entries contain? Is it a transaction amount, a specific date and time, category, and a pattern type (weekly, monthly, etc.)? Or is there more? 
> ANS: (): ___

The ±25% amount tolerance may still produce false negatives for large spending variations. Users may also whitelist a merchant entirely regardless of amount by selecting "Always allow this merchant" in the whitelist settings.

> ASK: (JOAQUIN): Tolerance for what? Considering detected anomalies within a whitelist?
> ANS: (): ___

### Section 5. Supplementary Rule-Based Detection.

In addition to Isolation Forest, the System shall implement rule-based budget overspending detection:

- Alert if a category exceeds 80% of its budget with >25% of period remaining
- Alert if any category exceeds 100% of its budget at any time

These rule-based alerts shall NOT be suppressed by whitelist or cultural exclusions.

> NOTE: This feature should be named "Overspending Detection". It is not supplementary, it is a whole module (or submodule). It just doesn't implement any intelligent features, so it's sort of similar to the Goals Management and Debt Management modules.

### Section 6. Alert Fatigue Prevention.

The System shall implement the following mechanisms:

| Mechanism | Specification |
|-----------|---------------|
| Cooldown | No more than 3 anomaly alerts per user per 24-hour period (rule-based alerts excluded) |
| Grouping | Multiple anomalies detected within 2 hours bundled into a single notification |
| Acknowledgement | User may snooze anomaly alerts for 7 days via Settings → Notifications |
| Sensitivity adjustment | User may adjust contamination rate from 0.05 (default) to 0.02 (more sensitive) or 0.10 (less sensitive) |

> PROP: Having users configure sensitivity may be too technical for a PFM app. I propose to only use the grouping mechanism.

### Section 7. Explainability.

For each anomaly alert, the System shall compute the deviation of each feature from the user's baseline (median or mean). The explanation shall be the feature with the largest standardized deviation. Example: "This transaction was flagged because the amount (PHP 5,000) is 2.5 standard deviations above your usual Food spending." This requires no per-transaction model fitting and is instantaneous.

### Section 8. Evaluation Metrics.

1. **Precision**
    - Target: ≥ 0.70
    - Calculation: TP/(TP+FP) on labeled anomalous transactions
    - Validation: Weekly on synthetic data
2. **Recall**
    - Target: ≥ 0.65
    - Calculation: TP/(TP+FN)
    - Validation: Same
3. **F1**
    - Target: ≥ 0.675
    - Calculation: 2 × (P×R)/(P+R)
    - Validation: Same
4. **False positive rate (per user per week)**
    - Target: ≤ 1.5
    - Calculation: FP / active days × 7
    - Validation: Same

> GLOBAL: The properties of evaluation metrics should be uniform as much as possible.

FPR during synthetic evaluation: count of false positives (transactions flagged as anomalous but not injected as anomalies) per 7-day window per synthetic user. For real user evaluation, FPR is not directly measurable without labels. Instead, report user dismissal rate (% of alerts dismissed as "expected") and alert acknowledgement rate as proxies.

---

## Article IX: Savings Goal Tracking

### Section 1. Goal Definition.

A savings goal shall consist of the following required fields:

> NOTE: Actually, I believe the appropriate terminology for this is "Goal", because it encompasses not just savings but funds, insurance deposits, investment deposits, etc. The point is all of these follow the same structure as savings; a static amount, a deposit rate (amount per day), and a predicted achievement date (from forecasting module).

> NOTE: Actually, investments should have their own module, since they have interest which can affect the rate. Also, they do not really count as a goal; they have no end goal.

1. **Goal name**
    - Constraints: ≤ 50 characters, unique per user
2. **Target amount**
    - Constraints: ≥ PHP 100, ≤ PHP 10,000,000
3. **Target date**
    - Constraints: ≥ 7 days from creation, ≤ 10 years
4. **Contribution amount**
    - Constraints: ≥ PHP 10 per contribution
5. **Contribution frequency**
    - Constraints: Daily, weekly, bi-weekly, monthly
6. **Linked source**
    - Constraints: Available balance (default) or specific income category

> NOTE: Same deal.

### Section 2. Multiple Concurrent Goals.

The System shall support up to 5 concurrent savings goals. Users shall prioritize goals via drag-and-drop in the UI. The System shall apply contributions in priority order: when available balance is sufficient, it shall contribute to goal 1 first, then goal 2, etc., until all scheduled contributions are satisfied or balance is exhausted.

> ASK: (JOAQUIN): Why only 5? And are the applied contributions sourced from the Budget as Financial Services or some other category?
> ANS: (): ___

### Section 3. Progress State Calculation.

For each goal at each contribution date, state shall be computed as:

```
remaining_amount = target_amount − current_amount
contribution_frequency = max(1, days_remaining / contribution_frequency_days)

required_contribution = remaining_amount / contribution_frequency

if current_contribution ≥ 1.10 × required_contribution: state = "ahead"
elif current_contribution ≥ 0.90 × required_contribution: state = "on_track"
elif current_contribution ≥ 0.50 × required_contribution: state = "behind"
else: state = "critical"
```

> GLOBAL: For code snippets, descriptive additions like comments and better variable names are a must.

Visual progress indicator: circular progress bar with color coding (green = ahead/on track, yellow = behind, red = critical).

### Section 4. Savings Contribution Strategies.

The System shall offer three contribution strategies:

1. **Goal-based (priority order)**
    - Allocation rule: Contribute to goal 1 first, then goal 2, etc.
    - Default for profile: All profiles
2. **Snowball (smallest balance first)**
    - Allocation rule: Contribute minimum to all goals, surplus to smallest-balance goal
    - Default for profile: Variable-Flexible
3. **Avalanche (highest priority first)**
    - Allocation rule: Contribute minimum to all goals, surplus to highest user-ranked goal
    - Default for profile: Stable-Obligated

> ASK: (JOAQUIN): How is the minimum defined? And what is the basis for these contribution strategies? What benchmark or study backs this up?
> ANS: (): ___

User may switch strategies at any time via Savings → Strategy.

### Section 5. Notifications.

The System shall send the following savings-related alerts:

1. **Milestone reached**
    - Trigger: Progress crosses 25%, 50%, 75%
    - Notification text: "You're 50% of the way to your [GOAL NAME] goal!"
2. **Behind schedule**
    - Trigger: State = "behind" for 7 consecutive days
    - Notification text: "Your [GOAL NAME] goal is behind schedule. Consider increasing contributions."
3. **Goal achieved**
    - Trigger: Current amount ≥ target amount
    - Notification text: "Congratulations! You achieved your [GOAL NAME] goal."

> NOTE: Again, same deal. Exhaustiveness and such.

---

## Article X: Debt Management

### Section 1. Debt Account Definition.

A debt account shall consist of the following required fields:

| Field | Constraints |
|-------|-------------|
| Debt name | ≤ 50 characters |
| Total principal amount | ≥ PHP 100, ≤ PHP 10,000,000 |
| Interest rate (annual) | 0% to 100%, stored as decimal (e.g., 0.05 for 5%) |
| Minimum monthly payment | ≥ PHP 0, ≤ principal amount |
| Payment due day of month | 1-28 |
| Remaining balance | Computed: principal − sum(payments) |

### Section 2. Payoff Strategies.

The System shall implement two payoff strategies with full switching capability:

| Strategy | Allocation Rule | Optimization target |
|----------|----------------|---------------------|
| Avalanche | Pay minimums on all debts, surplus to highest interest rate | Minimize total interest paid |
| Snowball | Pay minimums on all debts, surplus to smallest remaining balance | Minimize time to first debt payoff |

When user switches strategies, the System shall:
- Recalculate projected payoff dates and total interest for all debts
- Retain already-made payments (no retroactive changes)
- Display comparison: "If you switch to [OTHER STRATEGY], you would pay PHP[DIFF] more/less in total interest."

> ASK: (JOAQUIN): Was this process after switching strategies also done in Goal Management? Is it needed in Goal Management?
> ANS: (): ___

### Section 3. Projection Display.

For each debt account and for the aggregate, the System shall display:

- Remaining balance (current)
- Projected payoff date (date when balance ≤ 0, assuming minimum payments plus surplus as per strategy)
- Total interest projected under current strategy
- Total interest projected under alternative strategy (for comparison)

> ASK: (JOAQUIN): Ibid.
> ANS: (): ___

### Section 4. Minimum Payment Validation.

The System shall not permit a monthly debt payment below the account's minimum payment unless:

- The user explicitly overrides with a confirmation dialog: "Paying below the minimum may incur late fees and damage your credit score. Continue anyway? (Yes/No)"
- The user's available balance is less than the sum of all minimum payments (hardship mode).

If the user's available balance is less than the sum of all minimum payments, the System shall display a debt hardship screen with: (1) a warning that minimum payments exceed available balance, (2) a recommendation to contact each creditor (displaying creditor contact information if provided by user), (3) a link to the National Credit Council's debt counseling page (if available), and (4) an option to proceed with reduced payments by acknowledging: "I understand that paying below minimum may incur fees." No automated contact is made.

> NOTE: Debt Hardship as a term needs to be defined.

### Section 5. Debt Alerts.

The System shall send the following debt-related notifications:

| Alert | Trigger |
|-------|---------|
| Upcoming due date | 3 days before payment due date |
| Missed payment | Payment not recorded by due date + 1 day |
| Payoff milestone | 50% paid, 100% paid |

---

## Article XI: Alerts and Notifications (Comprehensive)

### Section 1. Alert Types.

The System shall generate alerts for the following five categories:

| Category | Specific alerts | Source module |
|----------|----------------|---------------|
| Budget overspending | Category > 80% of budget (warning), >100% (critical) | Rule-based |
| Anomaly | Unusual transaction detected | Isolation Forest |
| Savings milestone | 25%, 50%, 75%, 100% progress | Savings Goal Tracking |
| Forecast-based advisory | "Your current spending suggests you may exceed budget by [AMOUNT]" | Forecasting |
| Debt | Upcoming due date, missed payment, payoff milestone | Debt Management |

### Section 2. Delivery Method.

All alerts shall be delivered as:

- In-app notification (bell icon badge, displayed in notification center)
- Push notification (if user grants permission, with user-configurable opt-out per category)
- Optional email digest (weekly summary of all alerts, user opt-in)

> PROP: Do in-app and push notifs. only. We may not be able to do mailers, I think. Or maybe we can.

### Section 3. Alert Display Format.

Each alert shall contain:

| Field | Example |
|-------|---------|
| Title | "Budget Overspending Alert" |
| Body | "You have used 85% of your Food budget with 10 days remaining." |
| Action button | "View Budget" (opens budget screen) |
| Dismiss button | "Acknowledge" |

### Section 4. User Alert Configuration.

Users may configure per alert category:

- Enable/disable (except budget overspending which is mandatory)
- Sensitivity (low/medium/high) for anomaly and forecast-based alerts
- Cooldown period (1 to 24 hours) for duplicate alerts

> NOTE: Remember the discussion we had earlier about cooldown and sensitivity.

---

## Article XII: Explainability Requirements (Cross-Module)

All machine learning modules shall provide explainability as follows:

| Module | Method | Output format |
|--------|--------|---------------|
| Financial Behavioral Profile Classification | SHAP | Feature contribution list (top 3 features) |
| Budget Recommendation | Constraint satisfaction + feature importance | Template sentence + editable parameters |
| Forecasting (Expense/Income) | Attention weights or perturbation-based importance | "Your [CATEGORY] is predicted to [increase/decrease] because [REASON]" |
| Anomaly Detection | Feature deviation ranking | "Flagged because amount was high for this category" |

Explainability outputs shall be stored in the application log for audit and shall be viewable by the user via "Why?" button on any prediction or alert.

---

## Article XIII: Evaluation and Quality Metrics (ISO/IEC 25010:2023 + SUS)

### Section 1. ISO/IEC 25010:2023 Quality Characteristics.

The System shall be evaluated against the following characteristics with specific measures and thresholds:

| Characteristic | Measure | Acceptable threshold | Evaluation method |
|----------------|---------|----------------------|-------------------|
| Functional suitability | Percentage of specified features passing manual test cases | ≥ 98% | Manual test script (n=50 test cases) |
| Performance efficiency | Time from user action to UI response (p95) | ≤ 500ms for non-ML, ≤ 3000ms for ML predictions | Automated load testing (n=100 iterations) |
| Usability | System Usability Scale (SUS) score | ≥ 68 (industry average) | SUS survey (target n=30) |
| Reliability | Mean time between failures (MTBF) during 2-hour simulated use | ≥ 4 hours | Crash rate monitoring during pilot |
| Security | Number of critical vulnerabilities per OWASP Top 10 | 0 | Static analysis + penetration test |
| Maintainability | Cyclomatic complexity per function (excluding UI bindings) | ≤ 10 | Static code analysis (SonarQube) |

The cyclomatic complexity limit of ≤10 applies to application business logic (e.g., transaction validation, budget recalculation, alert generation). ML training scripts, LP solver libraries, and data preprocessing pipelines are exempt. Wrapper functions that call these libraries shall be kept simple (≤10).

> NOTE: Cyclomatic complexity needs to be defined. Thresholds also need to be justified and validated from benchmarks and studies.

### Section 2. System Usability Scale (SUS) Protocol.

**Target score:** ≥68 (industry average). A secondary stretch goal is ≥74 (85th percentile). The lower target accounts for the absence of bank sync (a known friction point).

**Sample size:** Target n=30. If n<30 but ≥20 after 4 weeks of recruitment, the study shall proceed with a post-hoc power analysis reporting the minimum detectable effect size.

> NOTE: Score and size need to be validated.

**Respondent profile stratification:**

| Stratum | Minimum count |
|---------|---------------|
| Stable-Flexible | 6 |
| Stable-Obligated | 6 |
| Variable-Flexible | 6 |
| Variable-Obligated | 6 |

> ASK: (JOAQUIN): Why these minimum counts? I believe our minimum total count is 50 evaluators.
> ANS: (): ___

Respondents shall be recruited from at least 4 different cities in Metro Manila (e.g., Manila, Quezon City, Makati, Taguig). No minimum per district.

**Administration:** SUS shall be administered after 14 days of active system use (minimum 10 transaction entries). Each user shall complete the standard 10-item Likert scale (1-5). Scoring per Brooke (1996): odd items contribute 1−score, even items contribute score−1, sum × 2.5.

> ASK: (JOAQUIN): Is that enough to test ALL aspects of the system? Won't we need to test monthly forecasts?
> ANS: (): ___

### Section 3. Algorithmic Module Evaluation Protocol.

| Module | Validation method | Primary metrics | Secondary metrics | Synthetic data source |
|--------|-------------------|-----------------|-------------------|----------------------|
| Forecasting | Walk-forward (60d train, 7d test, 26 iterations) | MAE, RMSE, sMAPE | Forecast bias, IoF | BSP CFS 2021 + PSA FIES 2018 |
| Anomaly detection | Walk-forward (30d train, 7d test, 13 iterations) | Precision, Recall, F1, FP rate | AUC-ROC | Same + injected anomalies (5%) |
| Profile classification | Rolling window (60d train, 30d test, 6 iterations) | Accuracy, Precision, Recall, F1 | Confusion matrix | Same + onboarding sim |

> ASK: (JOAQUIN): What about the budget recommendation module? And, as always, is this list exhaustive?
> ANS: (): ___

Walk-forward validation shall be performed on synthetic data only. Real user data collected during the pilot (max 30 days per user) is insufficient for 60-day training windows. Therefore, ML module performance metrics shall be reported based on synthetic test sets. Real user evaluation shall report SUS scores, task completion rates, and qualitative feedback only.

> GLOBAL: Markdown styles like bold and italic must be minimized as much as possible. Text must be in prose form as much as possible.

**Acceptable thresholds for each metric are defined in the respective Articles.**

### Section 4. Failure Conditions and System Responses.

| Condition | Detection | System Response | User notification |
|-----------|-----------|-----------------|-------------------|
| Forecast MAE > 20% for 14 days | Daily cron job | Log warning; continue current model; flag for retraining | None (developer notified) |
| Anomaly detection F1 < 0.6 for 7 days | Weekly evaluation | Disable Isolation Forest; revert to rule-based only | "Spending alerts are temporarily simplified. Your data is safe." |
| Classification accuracy < 0.80 on validation set | After each retraining | Do not deploy; retain previous model; alert developer | None |
| Any module throws unhandled exception | Runtime error handler | Graceful degradation: disable module; serve fallback | "[Module] is temporarily unavailable. Please try again later." |

---

## Article XIV: Data Privacy, Security, and Ethical Compliance

### Section 1. Compliance with RA 10173 (Data Privacy Act of 2012).

The System shall comply with the following Data Privacy Act requirements:

- **Consent:** All personal financial data shall be processed only with user consent obtained via explicit opt-in screen before first transaction entry.
- **Purpose limitation:** Data shall be used only for budget recommendation, forecasting, anomaly detection, and profile classification as described in this document.
- **Retention period:** 13 months from last user activity. After 13 months of inactivity, data shall be anonymized (user ID removed, transactions rounded to nearest PHP 100, dates truncated to month).
- **Anonymized research use:** Anonymized data may be used for aggregate research **only if** the user has given explicit opt-in consent on a separate screen during onboarding. The opt-in screen shall state: "Allow Odin to use your anonymized data to improve financial models for all users? This does not identify you personally." Users who do not opt in shall have their data permanently deleted after 13 months.
- **Portability:** User may request CSV export of all transactions via Settings → Export Data.
- **Deletion:** User may request deletion of all data via Settings → Delete Account, with confirmation. Deletion shall complete within 7 days.

### Section 2. Technical Security Controls.

| Control | Implementation | Standard |
|---------|----------------|----------|
| In-transit encryption | TLS 1.3 minimum for all server communications | NIST SP 800-52 |
| At-rest encryption (server) | AES-256-GCM for stored transaction data | FIPS 197 |
| Local storage (mobile) | Encrypted SQLite (SQLCipher) with 256-bit key derived from user PIN/biometric | SQLCipher 4.x |
| Authentication | Biometric (FaceID/TouchID/Android Biometric) + 6-digit PIN fallback | OWASP MASVS |
| Anonymization before server upload | User ID replaced with salted hash (SHA-256 with per-user salt stored only on device); no name/email sent | NIST SP 800-185 |

### Section 3. AI/ML Model Privacy.

No user transaction data shall be used to train global models without:

- Explicit opt-in consent separate from general Terms of Service (checkbox: "Allow anonymized data to improve Odin for everyone")
- Aggregation satisfying k-anonymity with k ≥ 20 before any model weight update
- Option to delete user's data from training corpus via Settings → Privacy → Remove from Training

Inference requests shall send only anonymized feature vectors (no raw transactions). The LSTM model shall run on a serverless function; no user data is persisted on the inference server beyond the request lifetime.

### Section 4. Ethical Review and Disclaimers.

The System shall display the following disclaimer on first launch and annually thereafter:

> NOTE: Should just be one-time.

"Odin's predictions and recommendations are for informational purposes only. You retain full responsibility for all financial decisions. Odin is not a financial advisor. Do not make major financial decisions solely based on automated outputs."

> This disclaimer must be prominent and displayed somewhere at the start, like in onboarding.

Institutional ethics clearance shall be obtained from the University of Makati Research Ethics Committee prior to any user data collection for research purposes.

---

## Article XV: Scope and Delimitations (Exclusions)

The following features and capabilities are explicitly **excluded** from the System:

| Exclusion | Reason |
|-----------|--------|
| Bank or e-wallet API integration | Registration fees and compliance complexity; manual entry is a deliberate design choice to increase mindfulness |
| Optical Character Recognition (OCR) of receipts | Increases complexity beyond thesis scope |
| Investment tracking (stocks, mutual funds, crypto) | Not part of core PFM for target users per RRL |
| Multi-currency support | Target users operate in PHP only |
| Non-Filipino users | Geographic and cultural delimitation |
| Users outside Metro Manila | Validation scope limitation |
| Automated bill payment | Security and regulatory complexity |
| Credit score monitoring | Requires third-party API with recurring fees |
| Tax computation | Requires professional certification |
| Paluwagan (informal rotating savings) dedicated module | No dedicated module; however, users may create a custom subcategory under SAVINGS named "Paluwagan" and manually record contributions and payouts. Future work may include a dedicated tracker. |

Bank and e-wallet API integration is excluded because: (1) API registration fees (e.g., GCash requires a partnership agreement with undisclosed fees), (2) compliance with BSP circulars on data sharing requires legal review beyond thesis scope, (3) manual entry, while frictionful, is a deliberate design choice to increase user awareness (evidence from RRL: manual logging improves financial mindfulness). This is noted as a limitation and recommended for future work.

> NOTE: This footnote should be part of the description or reason.

---

## Article XVI: Definitions of Terms (Operational)

For the purpose of this specification, the following terms have the meanings assigned:

| Term | Definition |
|------|------------|
| **Available balance** | Starting balance plus sum of income minus sum of expenses minus savings contributions minus debt payments. May not be negative. |
| **Behavioral drift (concept drift)** | A statistically significant change (p < 0.05 by Mann-Whitney U test) in any classification feature over a 60-day sliding window. |
| **Cold-start period** | The initial phase of user activity. Subdivided into: *Profile cold-start*: First 7 days – classification uses onboarding questionnaire; *Forecasting cold-start*: First 30 days – forecasts use population fallbacks (FIES/BSP). After 30 days, LSTM predictions replace fallbacks. |
| **Coefficient of variation (CV)** | Standard deviation of monthly net income divided by mean monthly net income. |
| **Expense category** | A classification label assigned to a financial transaction, grounded in PSA FIES 2018 taxonomy. |
| **Financial behavioral profile** | A classification of a user based on income stability (stable/variable) and obligation level (flexible/obligated). |
| **Obligation ratio** | Sum of unavoidable monthly expenses divided by total monthly income, averaged over 60 days. |
| **Paluwagan** | An informal rotating savings and credit association practiced in the Philippines. (Excluded from v1.0 as a dedicated module but can be tracked via custom category.) |
| **Personal Finance Management System (PFMS)** | A software system designed to help individuals track, plan, and manage personal income, expenses, savings, and debt. |
| **Walk-forward validation** | A time-series model evaluation method in which the model is trained on past data and tested on successive future periods, rolling forward incrementally. |
| **Random Forest** | An ensemble machine learning algorithm that constructs multiple decision trees and aggregates their outputs for classification. |
| **LSTM (Long Short-Term Memory)** | A type of recurrent neural network architecture suited to learning from sequential time-series data. |
| **Linear Programming (LP)** | A mathematical optimization method used to allocate limited resources subject to defined constraints. |
| **Isolation Forest** | An unsupervised anomaly detection algorithm that isolates anomalies by randomly partitioning feature space. |
| **SHAP** | SHapley Additive exPlanations — a game-theoretic method for explaining machine learning model outputs. |
| **LIME** | Local Interpretable Model-agnostic Explanations — a method for explaining individual predictions. (Used only for reference; anomaly detection uses feature deviation ranking.) |
| **FIES** | Family Income and Expenditure Survey — conducted by the Philippine Statistics Authority (PSA). |
| **BSP CFS** | Bangko Sentral ng Pilipinas Consumer Finance Survey. |
| **Avalanche method** | A debt payoff strategy prioritizing highest interest rate first to minimize total interest paid. |
| **Snowball method** | A debt payoff strategy prioritizing smallest outstanding balance first to build repayment momentum. |
| **Alert fatigue** | Desensitization to alerts due to excessive frequency or low relevance, resulting in ignored notifications. |

> NOTE: THIS is the Definition of Terms I've been looking for! This needs to be higher up, around the very start, and include the MANY new terminologies we have.

---

# PAPER SPECIFICATION

---

## Article I: Introduction Section Requirements

### Section 1. Background.

The Background subsection shall contain at least the following elements:

- **Domain context:** Overview of personal finance management in the Philippines, including prevalence of financial distress among young adults (cite BSP CFS 2021, PSA data).
- **Problem space:** Discussion of budgeting, saving, and debt management challenges specific to Metro Manila working young adults (age 20-40).
- **Existing solutions:** Survey of existing PFM apps (both international and local) and their limitations for Filipino users.

**Length:** Minimum 500 words, maximum 1000 words.

### Section 2. Problem Statement.

The Problem subsection shall be structured as:

- **General problem:** A single sentence stating the overarching problem the System addresses. Example: "Filipino working young adults lack access to a personal finance management system that adapts to their variable income patterns, cultural spending norms, and behavioral profiles."
- **Specific problems:** Enumerated list (3-5 items) of sub-problems, each mapped to a system module.

### Section 3. Objectives.

- **General objective:** "To design, implement, and evaluate Odin, a personal finance management system for Filipino working young adults in Metro Manila using Random Forest, LSTM, and Isolation Forest algorithms."
- **Specific objectives:** Enumerated list (5-8 items), each corresponding to a system module or evaluation activity. Each objective must be verifiable and mapped to a metric in Article XIII.

### Section 4. Significance.

List primary and secondary beneficiaries:

- **Primary:** Filipino working young adults (age 20-40, Metro Manila)
- **Secondary:** Researchers in financial technology for developing economies; PFM app developers targeting Southeast Asian markets; policymakers interested in financial inclusion metrics

### Section 5. Scope and Delimitations.

- **Scope (inclusions):** Reference Article XV but restate in prose.
- **Delimitations (exclusions):** Reference Article XV exclusions.

### Section 6. Definition of Terms.

Reproduce the terms from Article XVI that appear in the paper.

---

## Article II: Review of Related Literature (RRL) Pillars

The RRL chapter shall be organized into exactly 12 pillars as listed below. For each pillar, the paper shall contain:

- A minimum of 10 peer-reviewed citations (except where local data is scarce, in which case government reports and conference proceedings are acceptable)
- A synthesis paragraph that identifies gaps that Odin addresses
- A table or figure summarizing key findings (where appropriate)

**Pillar 1:** Filipino Working Young Adults and the Financial Problem  
**Pillar 2:** Filipino Cultural Context in Personal Finance  
**Pillar 3:** Expense Categorization in Personal Finance Systems  
**Pillar 4:** Existing Personal Finance and Budget Management Systems  
**Pillar 5:** Financial Behavioral Profiling  
**Pillar 6:** Spending Forecasting  
**Pillar 7:** Budget Recommendation  
**Pillar 8:** Anomalous Spending Detection  
**Pillar 9:** Mobile-First Design  
**Pillar 10:** Data Privacy, Security, and User Trust  
**Pillar 11:** User Retention and Engagement  
**Pillar 12:** System Evaluation  

Required subtopics for each pillar are defined in the internal research protocol (not repeated here for brevity but shall be followed).

---

## Article III: Research Methodology

### Section 1. Research Paradigm.

The study shall adopt a **pragmatist paradigm** (mixed methods) combining quantitative (ML metrics, SUS) and qualitative (thematic analysis of feedback).

### Section 2. Research Design.

Developmental research design with phases: requirements analysis, synthetic data generation, algorithm prototyping, system development (Agile, 2-week sprints), internal testing, user evaluation.

### Section 3. Agile Development Methodology.

Scrum with 2-week sprints. Roles: Product Owner (adviser), Scrum Master (group leader), Development Team (all members).

### Section 4. Evaluation Design.

ISO 25010 operationalized via test cases. SUS administered after 14 days of use. ML metrics computed via Python on synthetic data.

### Section 5. Data Collection for ML Training.

- **Primary:** Synthetic data from BSP CFS 2021 and PSA FIES 2018.
- **Secondary (optional):** Pre-survey of 50-100 Filipino working young adults.
- **Tertiary (pilot):** Up to 10 pilot users with consent, used only for final inference evaluation, not training.

**No real user data shall be used for training or fine-tuning any ML model.** Models frozen before pilot deployment.

### Section 6. Ethical Considerations.

Informed consent, RA 10173 compliance, anonymization, ethics clearance from UMak Research Ethics Committee, app disclaimer.

---

## Article IV: Expected Outcomes and Contribution

The thesis shall produce:

1. Functional Odin application
2. Random Forest classifier (accuracy ≥ 0.85)
3. LSTM forecasting model (sMAPE < 25% / 30% as per category)
4. Isolation Forest anomaly detector (F1 ≥ 0.675)
5. LP-based budget recommendation (adherence ≥ 70%)
6. Thesis manuscript
7. Public GitHub repository

---

## Article V: Thesis Timeline (Gantt Chart Required)

| Milestone | Duration |
|-----------|----------|
| RRL completion (12 pillars) | 8 weeks |
| Synthetic data generation | 2 weeks |
| Algorithm prototyping | 4 weeks |
| System development (4 sprints) | 8 weeks |
| Internal testing | 2 weeks |
| User evaluation (SUS + ML metrics) | 3 weeks |
| Thesis writing and revision | 6 weeks |
| Final defense preparation | 2 weeks |

A Gantt chart shall be included in the final paper.

---

## Article VI: Budget and Resources

| Item | Estimated cost (PHP) |
|------|----------------------|
| Server hosting (AWS/GCP t2.micro, 12 months) | 12,000 |
| Domain name (odin.ph) | 500 |
| Push notification service (Firebase, free tier) | 0 |
| SSL certificate (Let's Encrypt) | 0 |
| User incentives (GCash raffle) | 2,000 |
| **Total** | **14,500** |

---

## Article VII: References Style

APA 7th edition. Minimum 60 references, of which at least 40 peer-reviewed journal articles or conference proceedings.

---

## Article VIII: Appendices Required

| Appendix | Content |
|----------|---------|
| A | Onboarding questionnaire |
| B | SUS survey form |
| C | User consent form (English and Tagalog) |
| D | Synthetic data generation code (Python) |
| E | Hyperparameter tuning grids |
| F | Walk-forward validation results (tables) |
| G | System architecture diagram |
| H | Database schema |
| I | User manual |
