# Development of Odin: A Personal Finance Management System for Filipino Working Young Adults Using Random Forest, LSTM, and Isolation Forest

---

**Document Type:** Technical Specification

**Version:** 3.0

**Date:** 2026-06-04

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

## Global Comments

### 1. Opening Overall

> **Claude:** Overall, this is a remarkably detailed specification. However, I note several recurring issues:  
> (1) The document mixes prescriptive requirements ("shall") with research questions ("needs to be discovered"), which creates ambiguity about what is already decided versus what is still unknown.  
> (2) Many thresholds and parameters are labeled as placeholders but later appear as fixed values in code-like specifications.  
> (3) The relationship between synthetic data (BSP/PSA) and actual Filipino user behavior needs stronger justification, as synthetic data cannot fully capture cultural spending nuances.  
> (4) The document would benefit from a single source of truth for all configurable parameters (e.g., a table in an appendix) rather than scattering them across articles.

---

### 2. On Contradictions and Inconsistencies (scattered, but synthesized here)

> **Claude (multiple places):** The spec has contradictory requirements regarding negative available balance (Article II Section 3 allows warnings, Article V Section 2 says "shall never be negative"). Resolution needed.  
> **Claude:** Reclassification triggers have a contradiction: "No automatic reclassification" vs "may automatically apply."  
> **Claude:** The document uses "shall" and "should" inconsistently across sections.

---

### 3. On Missing Evaluation for Explainability

> **Claude (Article XII):** This article is concise but missing evaluation criteria. How will researchers evaluate whether explainability outputs are effective? Suggest user comprehension test and trust rating.

---

### 4. On Real User Data vs Synthetic Data

> **Claude (Article III Section 5 of PAPER SPEC, but applicable globally):** The statement "No real user data shall be used for training or fine-tuning any ML model" contradicts the weekly fine-tuning described in Article VII Section 2. Resolution needed.

---

### 5. On Terminology and Definitions

> **Claude (Article XVI):** Missing definitions: Add "Budget Infeasibility", "Debt Hardship", "Surplus handling strategies".  
> **Claude:** "Available balance: May not be negative" contradicts earlier NOTE – resolve consistently.

---

### 6. On Document Structure and Navigation

> **Claude GLOBAL:** The document is extremely long and dense. Consider adding:
> - A **master parameter table** (Appendix K) listing every configurable threshold (CV=0.25, OR=0.50, contamination=0.05, etc.) with source/justification.
> - A **cross-reference index** showing where each term is defined and where it is used.
> - **Hyperlinks** (if digital) from each "ASK" to its corresponding "ANS" when resolved.

---

### 7. On the Balance Between Prescription and Research

> **Claude GLOBAL:** Many sections say "The System shall..." but then a NOTE says "this is a placeholder, must be discovered by research." This creates confusion. Recommend splitting the document into:
> - **Part A: Frozen Requirements** (what is fixed for implementation)
> - **Part B: Research Questions** (to be answered via surveys/literature)
> - **Part C: Configurable Parameters** (defaults that can be changed without code)
> 
> Currently, all three are mixed.

---

### 9. On the Scope of "No Real User Data for Training"

> **Claude GLOBAL:** Article III Section 5 of PAPER SPEC states no real user data shall be used for training. However, the system spec describes weekly fine-tuning on each user's data (Article VII Section 2). To resolve:
> - Option A: Remove fine-tuning for the thesis; use only the global pre-trained model on synthetic data.
> - Option B: Allow fine-tuning with explicit user consent and on-device training (data never leaves the phone).
> 
> Recommend Option A for ethics simplicity and thesis feasibility.

---

### 10. On the Definition of "Working Young Adult"

> **Claude GLOBAL:** The target user is defined as "aged 20 to 40, employed, Metro Manila." However, many freelancers and gig workers in this age range have irregular income and multiple "jobs." The spec should clarify whether a user with **zero income in a given month** (e.g., between projects) is still considered "working" and whether they remain in the system. Suggestion: Add a minimum income frequency rule (e.g., at least one income transaction every 90 days to remain active).

---

### 11. On the Handling of "Paluwagan"

> **Claude GLOBAL:** The current solution (custom subcategory under SAVINGS) is inadequate because receiving the pot would distort spending/savings. Since paluwagan is culturally significant, consider one of:
> - Explicitly exclude it with a clear note that it cannot be modeled correctly.
> - Add a minimal dedicated module that tracks contributions and payouts **without** affecting the main budget (i.e., a separate "rotating savings" ledger).
> 
> If excluded, mention this as a **key limitation** in the thesis.

---

### 12. On the Formatting of Code Snippets

> **Claude GLOBAL:** The spec contains pseudo-code (e.g., in Article IX Section 3) without comments or clear variable naming. For the final thesis, all code snippets should follow a consistent style:
> - Use `snake_case` for variables.
> - Add inline comments explaining non‑obvious logic.
> - Specify the language (e.g., Python, pseudocode).
> 
> This improves readability for panel members who may not be familiar with the algorithms.

---

### 13. On the Absence of a Disaster Recovery / Backup Plan

> **Claude GLOBAL:** The spec describes failure conditions for ML modules (Article XIII Section 4) but does not address **data loss scenarios** (e.g., server crash, database corruption, user accidentally deleting all transactions). Recommend adding:
> - Automated daily database backups (retention: 30 days).
> - User‑initiated export/import of all data (CSV) as a manual backup mechanism.
> - A "restore from backup" procedure for developers.

---

### 14. On the Document Version and Change Log

> **Claude GLOBAL:** The document is version 2.0 dated 2026-06-03, but there is no change log or list of what changed from version 1.0. For a living specification, add a **Revision History** table at the beginning showing:
> - Version number
> - Date
> - Author
> - Summary of changes
> - Resolution of which ASKs/NOTEs were addressed

---

# SYSTEM SPECIFICATION

---

## Article I: Platform and Target Users

### Section 1. Platform Requirements.

1. The System shall be implemented as a mobile‑first application. 

    A. All core user flows, such as transaction entry, budget viewing, and alert acknowledgment, must be fully operable on a mobile screen width of 375 density‑independent pixels or less, and the layout shall adapt to any width between 320 and 450 dp without requiring horizontal scrolling. 

    B. A desktop web version shall also be provided, using a centered container with a maximum width of 1200 pixels and multi‑column layouts where appropriate. 

> [OPEN - Team]: The specific Android device models to be used for system evaluation are not yet finalised. The team should select at least one low‑end device, such as a Samsung A series handset, and one mid‑range device, as many target users may not own flagship phones. This section should be updated once the evaluation devices are procured.

### Section 2. Target User Definition.

1. The System is designed exclusively for the following user population. 

    A. Demographically, it targets Filipino working young adults aged twenty to forty years inclusive. 
    
    B. Geographically, it includes individuals who either live or work in Metro Manila, covering any of its sixteen cities and one municipality. 
    
    C. Employment status includes anyone currently employed, whether full‑time, part‑time, self‑employed, freelancer, contractual, or working in the gig economy.

2. This geographic definition intentionally includes commuters who reside in neighbouring provinces such as Cavite, Rizal, or Bulacan but work in Metro Manila, as these individuals are economically integrated with the target area.

---

## Article II: Input Methods and Transaction Types

### Section 1. Permitted Input Methods.

1. The System shall accept financial data through exactly two input methods. 

    A. The first is manual transaction entry, where the user types transaction details directly into the application. 
    
    B. The second is recurring transaction definition, where the user specifies a repeating transaction pattern that the System then generates automatically on the scheduled dates.

2. For manual entry, the required fields are amount, category, date, and account. 

    A. The merchant name is optional but recommended; if omitted, the merchant novelty feature for anomaly detection defaults to zero. 
    
        i. The description field is also optional. 
        
    B. For recurring transactions, the required fields are amount, category, frequency, start date, and account; an end date is optional.

3. Transfers between accounts use the manual input method. 

    A. In the user interface, when the user selects the transfer transaction type, the System shall display source account and destination account selectors instead of a single account field.

### Section 2. Transaction Types.

1. The System shall support exactly three transaction types.

    A. An income transaction represents a cash inflow into an account, moving from an external source to the available balance. 
    
        i. Income may be recurring with frequencies of daily, weekly, monthly, yearly, or a custom interval. 
        
        ii. Examples include salary, freelance payment, and remittance.

    B. An expense transaction represents a cash outflow from an account, moving from available balance to an expense category. 
    
        i. Expense may also be recurring with the same frequency options. 
        
        ii. Examples include groceries, rent, electricity bills, debt repayment, and savings deposits.

    C. A transfer transaction moves cash from one account to another without changing net worth. 
    
        i. Transfer may be recurring with daily, weekly, or monthly frequencies. 
        
        ii. Examples include moving money from a cash account to an e‑wallet account. 
        
        iii. When a transfer is recorded, the System shall subtract the amount from the source account's balance and add the same amount to the destination account's balance.

### Section 3. Manual Entry Workflow.

1. When a user manually enters a transaction, the System shall perform the following validations and actions in sequence. 

    A. First, the amount shall be validated. 
    
        i. For income and expense, the amount must be greater than zero Philippine pesos. 
        
        ii. For transfer, the amount may be positive; a negative amount is not permitted, as the direction of transfer is captured by the source and destination account selection.

    B. Second, for an expense transaction, the System shall check whether deducting the amount would make the available balance negative. 
    
        i. If so, the System shall display a warning message explaining that this transaction will result in a negative balance, and prompt the user to confirm whether they wish to proceed. 
        
            1. The user may confirm the deduction and accept the negative balance, or cancel the transaction. 
            
            2. This warning mechanism exists because users may occasionally forget to record income transactions, and preventing negative balances entirely would create unnecessary friction. 
        
        ii. The System shall display a persistent warning badge on the dashboard whenever any account balance is negative, and shall continue to show this badge until the balance returns to zero or positive.

    C. Third, for an income transaction, the System shall add the amount to the available balance of the selected account. 
    
        i. For an expense transaction, the System shall subtract the amount from the available balance. 
        
        ii. For a transfer, the System shall subtract the amount from the source account and add it to the destination account.

    D. Fourth, after the transaction is saved, the System shall store it with a timestamp in ISO 8601 format. 
    
        i. The transaction shall then be used to update downstream models, including profile classification, spending forecasts, and anomaly detection baselines. 
        
        ii. These updates may occur asynchronously, but shall complete within twenty‑four hours.

### Section 4. Recurring Transaction Rules.

1. The System shall generate recurring transactions automatically at their scheduled frequencies. 

    A. If a generated expense or transfer transaction would cause the available balance to become negative, the System shall not create the transaction. 

        i. Instead, it shall postpone the transaction, notify the user of the postponement, and re‑attempt generation on the next scheduled date and time. 
        
    B. The user may pause, edit, or delete any recurring template at any time.

### Section 5. Transaction Editing and Deletion.

1. Users may edit or delete any transaction, whether manual or recurring, at any time, subject to the retention limit described below. 

    A. When a transaction is edited or deleted, the System shall immediately recompute the available balance for the affected account. 
    
    B. All downstream models—profile classification, spending forecasts, and anomaly detection—shall be asynchronously retrained or re‑evaluated within twenty‑four hours. 
    
    C. Budget actuals shall be updated immediately. 
    
    D. The user shall receive a notification stating, "Transaction changed. Odin will update your forecasts within 24 hours."

> [RRL NEEDED: Retention limit] Users may not edit or delete transactions older than thirteen months from the transaction date. The choice of thirteen months is provisional and requires validation from either Bangko Sentral ng Pilipinas data retention guidelines, the Data Privacy Act's legitimate purpose principle, or a relevant study on financial data retention periods. If no authoritative source supports thirteen months, the team should adopt a more standard period such as twenty‑four months or align with tax record‑keeping recommendations (typically three years in the Philippines).

---

## Article III: User Classification and Financial Behavioral Profiles

### Section 1. Profile Taxonomy.

1. The System shall classify each user into exactly one of four financial behavioral profiles, determined by two binary dimensions. 

    A. The first dimension is income stability, which takes the value Stable or Variable. 
    
    B. The second dimension is obligation level, which takes the value Flexible or Obligated. 
    
    C. The four resulting profiles are Stable‑Flexible, Stable‑Obligated, Variable‑Flexible, and Variable‑Obligated.

### Section 2. Income Stability Thresholds.

1. Income stability shall be determined by the coefficient of variation of monthly net income over the preceding ninety days. 

    A. The coefficient of variation is defined as the standard deviation of monthly net income divided by the mean monthly net income. 
    
    B. A user is classified as Stable if the coefficient of variation is less than 0.25, and Variable if the coefficient is 0.25 or greater.

> [RRL NEEDED: CV threshold of 0.25] The proposed threshold of 0.25 is provisional. The researchers must validate this value through analysis of survey data (such as the BSP Consumer Finance Survey) or relevant literature on income variability among Filipino working young adults. Until validation is complete, the threshold shall remain configurable via system settings without requiring code changes.

2. For cold‑start classification during the first seven days of transaction history, the System shall use responses from the onboarding questionnaire to estimate income stability. 

    A. The cold‑start period lasts until the user has accumulated either at least five income transactions or thirty days of history, whichever is longer. 
    
    B. Only after meeting this minimum data requirement shall the System compute the coefficient of variation from actual transaction data.

### Section 3. Obligation Level Thresholds.

1. Obligation level shall be determined by the obligation ratio, defined as total unavoidable monthly expenses divided by total monthly income, averaged over the preceding sixty days. 

    A. A user is classified as Flexible if the obligation ratio is less than 0.50, and Obligated if the ratio is 0.50 or greater.

> [RRL NEEDED: Obligation ratio threshold of 0.50] The proposed threshold of 0.50 is provisional and must be validated through research. The definition of unavoidable expenses includes rent or mortgage, utility minimum payments, debt minimum payments, insurance premiums, government‑mandated contributions (SSS, PhilHealth, Pag‑IBIG), and documented family support such as monthly remittance to parents.

2. For salaried employees whose mandatory contributions are automatically deducted from gross salary, the System shall ask the user during onboarding whether they record gross or net income. 

    A. If the user records net income (after deductions), then mandatory contributions are already accounted for and shall not be added again as separate expenses. 
    
    B. If the user records gross income, the System shall treat the contribution amounts as separate unavoidable expenses when they appear as transactions.

### Section 4. Reclassification Triggers.

1. The System shall re‑evaluate a user's profile classification when any of the following conditions occur. 

    A. First, the income coefficient of variation changes by an absolute difference of 0.10 or more from the baseline used for the current classification, sustained over sixty consecutive days. 
    
    B. Second, the obligation ratio changes by an absolute difference of 0.15 or more from the baseline, sustained over sixty consecutive days. 
    
    C. Third, the user explicitly requests reclassification via the settings menu. 
    
    D. Fourth, ninety days have elapsed since the last classification, providing a periodic refresh.

> [RRL NEEDED: Reclassification thresholds and sustained periods] The values of 0.10 for CV change, 0.15 for obligation ratio change, and the sixty‑day sustained period are provisional. These should be validated against literature on how long financial behavioral profiles typically take to shift.

2. Upon detection of any trigger, the System shall generate a reclassification recommendation and present it to the user with an explanation using SHAP values (see Section 5). 

    A. No automatic reclassification shall occur without explicit user confirmation. 
    
    B. The user may accept or decline the recommended change. 
    
    C. If the user does not respond to the recommendation within thirty days, the System shall display a persistent, non‑dismissible notification on the dashboard stating, "Your financial behavior appears to have changed. Odin recommends updating your profile. Apply now?" 
    
    D. The user must either accept or decline; there is no automatic application. This design ensures that the user retains full control over their profile classification at all times.

### Section 5. Classification Algorithm.

1. Classification shall be performed using a Random Forest classifier with the following specifications. 

    A. The forest shall contain a minimum of one hundred decision trees, each with a maximum depth of ten levels. 
    
    B. The split criterion shall be Gini impurity. 
    
    C. Class weights shall be balanced to address potential imbalance in the training data, meaning that the synthetic training dataset shall be generated with equal representation of all four profiles (twenty‑five percent each). 
    
    D. The random state shall be fixed at forty‑two for reproducibility, primarily for testing and development purposes.

2. The features used for classification shall include at minimum the following. 

    A. Income coefficient of variation computed over thirty‑day, sixty‑day, and ninety‑day windows. 
    
    B. Obligation ratio computed over the same three windows. 
    
    C. Income frequency measured as the number of income payments per thirty days. 
    
    D. Income amount variance using mean absolute deviation. 
    
    E. Fixed expense count, defined as the number of distinct payees with the recurring flag enabled. 
    
    F. Savings rate computed as savings divided by income over a thirty‑day window. 
    
    G. Transaction regularity score calculated as the entropy of inter‑transaction intervals.

3. All features are continuous except income frequency and fixed expense count, which are integers. 

    A. The data source for all features is the user's transaction history.

4. For each classification prediction, the System shall provide SHAP (SHapley Additive exPlanations) values. 

    A. The explanation shall be presented to the user in a sentence such as, "Your profile is Stable‑Obligated mainly because your obligation ratio of 0.55 is higher than typical Flexible users, and your monthly spending coefficient of variation of 0.12 indicates stable income."

### Section 6. Cold-Start Classification (Onboarding Questionnaire).

1. During the initial seven‑day period before sufficient transaction data is available, the System shall classify the user using a questionnaire. 

2. The questionnaire shall contain at least the following items, presented in order.

    A. First, the System shall ask the user for their typical monthly income amount in Philippine pesos. 
    
        i. This amount is then used to contextualise subsequent questions.

    B. Second, the System shall ask, "Is your monthly income roughly the same each month?" with response options Yes or No. 
    
        i. This maps to the income stability dimension.

    C. Third, the System shall ask, "By how much does your monthly income typically vary?" 
    
        i. The response options shall be presented both as percentages and as actual peso ranges based on the user's stated income. 
        
            1. For example, for a user with a monthly income of 25,000 pesos, the options would be: less than 10% (less than 2,500 pesos), 10‑25% (2,500 to 6,250 pesos), 25‑50% (6,250 to 12,500 pesos), and greater than 50% (more than 12,500 pesos). 
            
        ii. This maps to an estimate of the coefficient of variation.

    D. Fourth, the System shall ask, "What percentage of your monthly income goes to bills and expenses that you cannot skip?" 
    
        i. The response options shall be less than 30%, 30‑50%, 50‑70%, and greater than 70%. 
        
            1. To aid understanding, the System shall display the corresponding peso amounts based on the user's stated income. 
            
        ii. This maps to the obligation ratio.

    E. Fifth, the System shall ask, "Do you have dependents such as children, parents, or siblings whom you support financially?" with response options Yes or No. 
    
        i. If the user answers Yes, the System shall ask for the number of dependents. 
        
        ii. This provides context for explainability but does not directly adjust the obligation ratio calculation.

    F. Sixth, the System shall ask, "Do you have any loans or debts with required minimum monthly payments?" with response options Yes or No. 
    
        i. This also provides contextual information and is already captured in the obligation ratio question; it is retained to help users understand what counts as an unavoidable expense.

> [RRL NEEDED: Questionnaire response mapping to profiles] The exact algorithm for converting questionnaire responses into an initial profile classification must be validated through research. The provisional approach is to treat a "No" answer to income stability as Variable, and a "Yes" answer to the obligation percentage question at or above 50% as Obligated, with the remaining combinations producing the corresponding profiles.

3. After the user completes the questionnaire, the System shall compute an initial profile and present it to the user for confirmation before proceeding to the main application.

### Section 7. Connection to Other Modules

1. The profile label produced by the Random Forest classifier shall be passed to the LSTM forecasting module as a contextual feature, and to the Isolation Forest anomaly detection module to provide profile‑aware baselines. 

2. The profile is also used by the budget recommendation module to select default priorities and constraints. 

3. When a user's profile changes through reclassification, all downstream modules shall receive the updated label within twenty‑four hours.

---

## Article IV: Expense Categories

### Section 1. Base Category Taxonomy.

1. The System shall implement expense categories grounded in the 2020 Philippine Classification of Individual Consumption According to Purpose (PCOICOP), cross‑validated against the BSP Consumer Finance Survey 2021. 

    A. However, categories that represent purely economic concepts with no corresponding cash flow shall be excluded. 
    
        i. Specifically, imputed rentals for housing, which represent the economic value of owner‑occupied housing, shall not appear as a user‑selectable category because no actual expense transaction occurs.

2. The following base categories shall be implemented, each with its associated subcategories as listed. 

    A. The System shall store transactions at the most granular subcategory level, but shall also maintain a mapping from each subcategory to one of four broad groups: Essentials, Obligatory, Discretionary, and Financial Allocation. 
    
        i. This mapping is defined in Section 2.

3. The following base categories shall be implemented, each with its associated subcategories as listed:

    A. Food and Non‑Alcoholic Beverages — includes Food, Non‑Alcoholic Beverages, and Services for Processing Primary Goods for Food and Non‑Alcoholic Beverages. 
    
        i. Mapped to Essentials.

    B. Alcoholic Beverages, Tobacco and Narcotics — includes Alcoholic Beverages, Alcohol Production Services, Tobacco, and Narcotics. 
    
        i. Mapped to Discretionary.

    C. Clothing and Footwear — includes Clothing and Footwear. 
    
        i. Mapped to Discretionary.

    D. Housing, Water, Electricity, Gas and Other Fuels — includes Actual Rentals for Housing, Maintenance Repair and Security of the Dwelling, Water Supply and Miscellaneous Services Relating to the Dwelling, and Electricity Gas and Other Fuels. 
    
        i. Imputed rentals are excluded. 
        
        ii. Actual rent payments are mapped to Obligatory.
        
        iii. Utilities (water, electricity, gas) are mapped to Essentials. 
        
        iv. Maintenance and repair services are mapped to Discretionary.

    E. Furnishings, Household Equipment and Routine Household Maintenance — includes Furniture Furnishings and Loose Carpets, Household Textiles, Household Appliances, Glassware Tableware and Household Utensils, Tools and Equipment for House and Garden, and Goods and Services for Routine Household Maintenance. 
    
        i. Mapped to Discretionary.

    F. Health — includes Medicines and Health Products, Outpatient Care Services, Inpatient Care Services, and Other Health Services. 
    
        i. Mapped to Essentials.

    G. Transport — includes Purchase of Vehicles, Operation of Personal Transport Equipment, Passenger Transport Services, and Transport Services of Goods. 
    
        i. Mapped to Obligatory for essential commuting (public transport, fuel for work travel). 
        
        ii. Mapped to Discretionary for vehicle purchases and non‑essential travel. 
        
        iii. The System shall not auto‑classify; the user selects the category at transaction entry, and the mapping follows the selected subcategory.

    H. Information and Communication — includes Information and Communication Equipment, Software Excluding Games, and Information and Communication Services (such as mobile data, internet, and postpaid plans). 
    
        i. Mapped to Obligatory for basic communication services (mobile plan, home internet). 
        
        ii. Mapped to Discretionary for device purchases.

    I. Recreation, Sport and Culture — includes Recreational Durables, Other Recreational Goods, Garden Products and Pets, Recreational Services, Cultural Goods, Cultural Services, Newspapers Books and Stationery, and Package Holidays. 
    
        i. Mapped to Discretionary.

    J. Education Services — includes Early Childhood and Primary Education, Secondary Education, Post‑Secondary Non‑Tertiary Education, Tertiary Education, and Education Not Defined by Level. 
    
        i. Mapped to Obligatory.

    K. Restaurants and Accommodation Services — includes Food and Beverage Serving Services (dining out) and Accommodation Services (hotels, resorts). 
    
        i. Mapped to Discretionary.

    L. Insurance and Financial Services — includes Insurance premiums (health, life, vehicle) and Financial Services (bank fees, remittance fees). 
    
        i. Insurance premiums are mapped to Obligatory. 
        
        ii. Financial services fees are mapped to Discretionary unless the user designates them as essential.

    M. Personal Care, Social Protection and Miscellaneous Goods and Services — includes Personal Care (haircuts, cosmetics, toiletries), Other Personal Effects, Social Protection (voluntary contributions beyond mandatory), and Other Services. 
    
        i. Mapped to Discretionary for personal care and miscellaneous. 
        
        ii. Mapped to Obligatory for documented social protection contributions.

### Section 2. Category Aggregation into Groups.

1. For forecasting (LSTM) and budget recommendation, the thirteen base categories shall be aggregated into four broad groups, which serve as the forecast targets and the primary budget allocation units. 

    A. The mapping from each base category to a broad group is defined below.

2. The four broad groups are the following:

    A. The Essentials group includes Food and Non‑Alcoholic Beverages, the utilities portion of Housing (electricity, water, gas), and Health. 
    
        i. These are expenses necessary for basic survival and well‑being.

    B. The Obligatory group includes contractual and unavoidable payments: rent (actual rentals), debt minimum payments (tracked via a separate debt management module but recorded as expenses under a Obligatory subcategory), insurance premiums, government contributions, basic transport for commuting, basic communication services (mobile and internet), education expenses, and documented family support. 
    
        i. These expenses are fixed in amount or timing and cannot be easily reduced in the short term.

    C. The Discretionary group includes all remaining categories: alcoholic beverages and tobacco, clothing and footwear, non‑essential housing maintenance, furnishings and appliances, non‑essential transport, recreational equipment and services, dining out, accommodation, personal care, and miscellaneous goods. 
    
        i. These expenses are optional and can be adjusted based on available surplus.

    D. The Financial Allocation group includes savings deposits, investment contributions, and debt principal prepayments (beyond minimum payments). 
    
        i. These are treated as allocations rather than expenses, though they appear as outflows from available balance. 
        
            1. The distinction is important for the budget LP: financial allocations are not counted as "spending" in the same sense as Essentials, Obligatory, or Discretionary expenses.

> [OPEN: Team Decision] The mapping of specific subcategories to these four groups may be adjusted based on user feedback or cultural context. For example, some users may consider mobile data an Essential rather than Obligatory. The System shall allow users to override the default group mapping for any subcategory via Settings → Categories, but such overrides apply only to that user's budgeting and forecasting; the ML models continue to use the standard mapping for training and inference.

### Section 3. User Category Overrides.

1. Users may create up to five custom subcategories under any base category. 

    A. Each custom subcategory must be mapped to exactly one base category for aggregation purposes, and must also be assigned to one of the four broad groups (Essentials, Obligatory, Discretionary, or Financial Allocation). 
    
    B. The user may delete custom subcategories but may not delete or rename base categories.

2. When a user creates a custom subcategory, the System shall prompt the user to select the appropriate broad group with a brief explanation: "Choose whether this expense is essential for survival, obligatory like rent or debt payments, discretionary like entertainment, or a financial allocation like savings."

3. The System shall not perform automatic categorisation of transactions. 

    A. All category assignments must be made by the user at transaction entry time. 
    
    B. This design choice prioritises user awareness and control over automation, and is supported by literature suggesting that manual logging improves financial mindfulness.

> [FUTURE WORK] Optional auto‑categorisation based on merchant name or transaction description is recommended as a future enhancement. The current version excludes this feature to maintain scope focus.

---

## Article V: Financial Flows and Balance Model

### Section 1. Financial Flow State Machine.

1. The System shall model financial flows according to a simple state machine. 

    A. Income transactions add funds to the available balance of the selected account. 
    
    B. Expense transactions subtract funds from the available balance, with the amount allocated to a specific expense category. 
    
    C. Savings goal contributions subtract funds from the available balance and add them to the goal's accumulated amount. 
    
    D. Debt payments subtract funds from the available balance and reduce the outstanding balance of the specified debt account.

2. No other flows are implemented. 

    A. In particular, expenses cannot be paid directly from a savings goal, and debt payments cannot be made directly from a savings goal. 
    
    B. All outflows must pass through the available balance of a cash or bank account.

### Section 2. Available Balance Definition.

1. Available balance for a given account is defined as the starting balance plus the sum of all income transactions into that account, minus the sum of all expense transactions from that account, minus the sum of all savings contributions drawn from that account, minus the sum of all debt payments drawn from that account. 

    A. This calculation may result in a negative value.

2. The System shall permit negative available balances. 

    A. When a transaction would cause a balance to become negative, the System shall first display a warning message explaining that the transaction will result in a negative balance, and prompt the user to confirm whether they wish to proceed. 
    
        i. If the user confirms, the transaction is recorded and the balance becomes negative. 
        
        ii. If the user cancels, the transaction is not recorded.

3. Whenever any account has a negative available balance, the System shall display a persistent warning badge on the dashboard, visible in all main views. 

    A. The warning shall state that one or more accounts are overdrawn and that the user should review recent transactions or add missing income. 
    
    B. The badge shall disappear only when all account balances return to zero or positive.

4. All amounts shall be stored in Philippine pesos as integer centavos, for example 100.00 pesos stored as 10000 centavos, to avoid floating‑point rounding errors.

### Section 3. Account Separation.

1. The System shall support up to ten user‑defined accounts. 

    A. The default first account is named "Cash". 
    
    B. The user may add, rename, or delete accounts at any time, subject to the limit of ten active accounts. 
    
    C. When an account is deleted, all transactions associated with that account must be reassigned to another account before deletion is permitted, or the user may choose to delete the account and all its transactions permanently.

2. Each transaction must be associated with exactly one account. 

    A. Transfer transactions are an exception: they associate with both a source account and a destination account. 
    
    B. The System shall compute available balance separately for each account. 
    
    C. Transfers do not affect net worth, only the distribution of funds across accounts.

> [OPEN: Team Decision] Credit card accounts are not explicitly modelled in this version. A credit card would behave as a liability account where spending increases the outstanding balance rather than decreasing available cash. The current scope assumes that users record credit card payments as expenses at the time of payment, not at the time of swipe. If the team decides to include credit card support, a dedicated account type with separate rules would be required. For the thesis, this is recommended as future work.

### Section 4. Transaction Recording and Balance Update Order

1. When a user records a transaction, the System shall update the account balance immediately after validation and confirmation of any negative balance warning. 

    A. For income, the amount is added to the account balance. 
    
    B. For expense, the amount is subtracted. 
    
    C. For transfer, the amount is subtracted from the source account and added to the destination account in a single atomic operation.
    
        i. If either subtraction would cause a negative balance, the warning and confirmation process applies to the source account, and the transfer is not partially applied.

2. Recurring transactions scheduled for a future date shall not affect current balances. 

    A. At the time of automatic generation, the same validation and warning rules apply. 
    
    B. If a recurring expense would cause a negative balance, the System shall not create the transaction, shall log the postponement, and shall notify the user. 
    
        i. The transaction shall be re‑attempted on the next scheduled date.

---

## Article VI: Budget System

### Section 1. Budget Structure.

1. Every budget in the System shall consist of the following components. 

    A. The total budget size is the sum of allocated amounts across all categories for a given budget period. 
    
    B. The budget period is a time horizon measured in days, selectable from seven, fourteen, thirty, or ninety days. 
    
    C. For each category within the user's selected category set, the budget includes a per‑category allocation expressed in Philippine pesos, and a per‑category actual spending amount tracked from expense transactions recorded during the period. 
    
    D. The surplus or deficit for a category is defined as the allocated amount minus the actual spending, with a positive value indicating underspending and a negative value indicating overspending. 
    
        i. The same calculation applies to the total budget.

2. The System shall only create budgets that are feasible, meaning that there exists an allocation satisfying all hard constraints defined in Section 4. 

    A. A budget that violates any hard constraint is considered infeasible and triggers the infeasibility handling procedure also defined in Section 4.

### Section 2. Budget Period Selection.

1. The System shall recommend a budget period based on the user's financial behavioral profile. 

    A. For Stable‑Flexible users, the recommended period is thirty days, justified by the typical monthly salary cycle. 
    
    B. For Stable‑Obligated users, the recommended period is also thirty days, as monthly obligations align with this horizon. 
    
    C. For Variable‑Flexible users, the recommended period is fourteen days, as a shorter horizon reduces forecast error for variable income. 
    
    D. For Variable‑Obligated users, the recommended period is fourteen days, also to reduce forecast error. 
    
> [RRL NEEDED: These period recommendations require validation from literature on budget horizon effectiveness for different income stability profiles.] 

2. The user may override the recommended period at any time, and the System shall honour the user's selection.

### Section 3. Budgeting Strategy Templates.

1. The System shall offer four budgeting strategy templates that the user may select at budget creation. 

    A. The first is the Fifty‑Thirty‑Twenty strategy, which allocates fifty percent of the total budget to Essentials, thirty percent to Discretionary, and twenty percent to Financial Allocation (savings and debt prepayment). 
    
        i. This strategy is recommended as a general starting point for users with stable income.

    B. The second is the Zero‑Based strategy, where every peso of income is assigned to a specific category, including savings and debt payments, leaving no unallocated buffer. 
    
        i. This means that the sum of all category allocations equals the forecast income minus the target savings rate, and every category has a non‑zero allocation. 
        
        ii. This strategy is recommended for detailed trackers and users with variable income who need to account for every peso.

    C. The third is the Savings‑First strategy, also known as reverse budgeting or pay‑yourself‑first. 
    
        i. Under this strategy, the target savings contribution amount is deducted from forecast income first as a hard constraint, and the remaining amount is allocated across all expense categories. 
        
        ii. This strategy is recommended for users prioritising savings goals.

    D. The fourth is the Custom strategy, where the user manually defines percentage allocations per broad group or per category. 
    
        i. This strategy is recommended for advanced users who already know their preferred spending distribution.

> [OPEN: Team Decision] The naming of these strategies in the user interface should use plain Filipino‑friendly terms. For example, "Savings‑First" may be clearer as "Savings Muna" in Tagalog, but the team should decide whether to localise interface text. The technical names above are for specification purposes only.

### Section 4. Budget Recommendation Algorithm.

1. Budget allocations shall be generated using Linear Programming. 

    A. The objective is to maximise the sum over categories of the user's declared priority weight for that category multiplied by the allocated amount. 
    
    B. Priorities range from one (lowest) to five (highest). 

2. The default priorities per profile are defined as follows:

    A. For Stable‑Flexible users:

        i. The highest priority (five) is assigned to Financial Allocation. 

        ii. Medium priority (four) is assigned to Essentials (specifically Food) and Discretionary (specifically Recreation). 
        
        iii. Low priority (three) is assigned to all remaining categories.

    B. For Stable‑Obligated users:

        i. The highest priority (five) is assigned to Obligatory (specifically Housing and Financial Obligations such as debt minimum payments). 
        
        ii. Medium priority (four) is assigned to Essentials (specifically Health) and Financial Allocation. 
        
        iii. Low priority (three) is assigned to all remaining categories.

    C. For Variable‑Flexible users:

        i. The highest priority (five) is assigned to Financial Allocation. 
        
        ii. Medium priority (four) is assigned to the entire Essentials group. 
        
        iii. Low priority (three) is assigned to all remaining categories.

    D. For Variable‑Obligated users:

        i. The highest priority (five) is assigned to Obligatory (specifically Housing and Financial Obligations). 
        
        ii. Medium priority (four) is assigned to Essentials (specifically Health). 
        
        iii. Low priority (three) is assigned to all remaining categories.

> [RRL NEEDED: Default priorities per profile require validation from literature on financial goal prioritisation among different user segments.]

3. The user may adjust priorities at any time in the Settings screen, with an explanation: "Higher priority categories get more budget, subject to spending caps."

4. The Linear Programming constraints are as follows:

    A. First, the sum of allocations across all categories must equal the forecast income multiplied by one minus the target savings rate. 
    
        i. The target savings rate is a percentage defined by the user, defaulting to ten percent. 
        
        ii. This equation ensures that the total budget available for spending is income after setting aside savings.

    B. Second, the allocation to Obligatory categories must be at least the sum of all minimum debt payments and insurance premiums. 
    
        i. This is a hard constraint that cannot be relaxed.

    C. Third, the allocation to Financial Allocation must be at least forecast income multiplied by the target savings rate. 
    
        i. This constraint may be relaxed in the infeasibility handling procedure.

    D. Fourth, the allocation to the Essentials group must be at least fifty percent of the total budget (forecast income after savings). 
    
        i. This is a spending floor designed to ensure basic needs are covered. 
        
        ii. This constraint may also be relaxed.

    E. Fifth, the allocation to the Discretionary group must not exceed thirty percent of the total budget. 
    
        i. This is a spending cap designed to limit non‑essential spending.

    F. Sixth, the allocation to any single detailed category must not exceed a category‑specific maximum. 
    
        i. This maximum is derived from the ninetieth percentile of the user's historical spending for that category, based on at least thirty days of data. 
        
        ii. If insufficient history exists, the maximum defaults to thirty percent of the total budget for Essentials categories and twenty percent for Discretionary categories. 
        
        iii. For Obligatory categories, the maximum is the sum of all known fixed obligations plus twenty percent as a buffer.

    G. Seventh, if the user has selected the Savings‑First strategy, the allocation to Financial Allocation must be at least the user's target contribution amount, specified when creating the strategy. 
    
        i. This replaces the percentage‑based savings constraint.

    H. Eighth, all category allocations must be greater than or equal to zero.

5. When the Linear Programming problem is infeasible, meaning no allocation satisfies all hard constraints simultaneously, the System shall apply sequential relaxation. 

    A. First, the savings constraint (Financial Allocation minimum) is reduced to zero. 
    
    B. If still infeasible, the Essentials floor is reduced from fifty percent to forty percent, then to thirty percent, then to twenty percent. 
        
    C. If still infeasible after reducing the Essentials floor to twenty percent, the Essentials floor is removed entirely. 
    
    D. If the problem remains infeasible with only the debt minimum constraint and non‑negativity, which is always feasible, the System shall display a message: "Your minimum debt payments and essential expenses exceed your predicted income by [amount in pesos]. Odin cannot create a balanced budget. Please consider debt restructuring or income increase. Contact a financial counselor if needed."

> [OPEN: Team Decision] The sequential relaxation percentages and steps are provisional. The team may adjust these values based on testing with real user scenarios.

### Section 5. Surplus Handling.

1. At the end of a budget period, any surplus (allocated but unspent amount) shall be handled according to one of three user‑selectable strategies. 

    A. Under the Rollover strategy, the surplus amount is added to the next period's total budget, and category allocations for the next period are recomputed using the Linear Programming solver with the increased total budget while preserving the same allocation ratios relative to the total. 
    
    B. Under the Save strategy, the surplus is automatically transferred to the user's primary savings goal as an additional contribution. 
    
    C. Under the Reset strategy, the surplus is returned to the available balance, and the next period's budget is recomputed from zero as if no prior surplus existed.

2. The default strategy per profile is Rollover for stable profiles (Stable‑Flexible and Stable‑Obligated) and Save for variable profiles (Variable‑Flexible and Variable‑Obligated). 

    A. The Reset strategy has no default; the user must select it explicitly.

3. At the end of each budget period, the System shall display a prompt: "You underspent by [amount in pesos]. What would you like to do with the leftover amount?" with the three options presented. 

    A. If the user does not respond within seven days, the System shall apply the default strategy for that user's profile.

> [RRL NEEDED: The surplus handling strategies (Rollover, Save, Reset) and their default assignments require validation from literature on user preferences for windfall or surplus allocation.]

### Section 6. Explainability.

1. Every budget recommendation shall be accompanied by an explanation in plain language. 

    A. The explanation shall state the budget period, total budget amount, forecast income used, and target savings amount. 
    
    B. It shall then explain the major constraints that shaped the allocation. 
    
        i. For example: "Your 30‑day budget is 22,500 pesos. This is based on your predicted income of 30,000 pesos and a minimum savings target of 3,000 pesos (10 percent of your income). 11,250 pesos is allocated to Essentials because this category is required to be at least 50 percent of your budget. To change any allocation, adjust your category priorities in Settings."

2. Additional explanation shall be provided for users who wish to understand the optimisation: 

    A. For example: "The budget recommendation maximises your stated priorities. If you set Food priority to 5, the system will allocate as much as possible to Food without exceeding your Discretionary group cap (30 percent of total) or your historical maximum for Food. To balance spending, adjust category priorities or set manual caps."

    B. The explanation shall be accessible via a "Why?" button next to the recommended budget.

### Section 7. Connection to Other Modules

1. The budget recommendation module receives forecast income and category‑level spending forecasts from the LSTM module. 

2. It also receives the user's financial behavioral profile from the Random Forest classifier, which determines the default priority weights. 

3. The budget recommendation is displayed to the user, who may accept, modify, or reject it. 

    A. Once accepted, the budget becomes active, and actual spending is tracked against it. 
    
4. Overspending alerts (defined in Article XI) compare actual spending to the accepted budget allocations.

---

## Article VII: Forecasting Module

### Section 1. Forecasting Targets.

1. The System shall generate forecasts for four targets, each at configurable granularities and horizons. 

    A. The first target is per‑category expense, forecast at the level of the four broad groups: Essentials, Obligatory, Discretionary, and Financial Allocation. 
    
        i. Forecast granularities include daily, weekly, and monthly aggregates. 
        
        ii. Horizons include seven, fourteen, thirty, and ninety days. 
        
        iii. The user may select the horizon per view, either for total spending or per category.

    B. The second target is total income, forecast at daily, weekly, or monthly granularity over the same horizons of seven, fourteen, thirty, and ninety days. 
    
    C. The third target is savings balance trajectory, forecast at daily granularity over a horizon of one hundred eighty days. 
    
        i. This forecast assumes that the user follows the current budget recommendation, including planned savings contributions, and does not make unplanned withdrawals. 
        
    D. The fourth target is debt remaining balance, forecast at daily granularity until the projected payoff date, assuming the user follows the selected debt payoff strategy (avalanche or snowball) with minimum payments and any surplus allocated according to that strategy.

2. All forecasts shall include a disclaimer displayed prominently in the forecasting interface: "Forecasts are inferential and informational only, based on your past spending and current budget. Actual future spending may differ."

### Section 2. Forecasting Algorithm.

1. All forecasts shall be generated using a Long Short‑Term Memory (LSTM) network with the following architecture. 

    A. The input sequence length is sixty days of daily data. 
    
    B. The network has two LSTM layers, with sixty‑four units in the first layer and thirty‑two units in the second layer. 
    
    C. A dropout rate of 0.2 is applied after each LSTM layer to reduce overfitting. 
    
    D. The output layer uses linear activation for regression. 
    
    E. The loss function is Huber loss with a delta parameter of 1.0, which is less sensitive to outliers than mean squared error. 
    
    F. The optimizer is Adam with a learning rate of 0.001. 
    
    G. Training uses a batch size of thirty‑two for up to one hundred epochs, with early stopping after ten epochs without improvement in validation loss.

2. The input features for the LSTM include:

    A. The daily amounts for each of the four broad groups (Essentials, Obligatory, Discretionary, Financial Allocation).
    
    B. Total daily spending.
    
    C. The user's income amount (updated when new income transactions are recorded).
    
    D. The user's financial behavioral profile label from the Random Forest classifier.
    
    E. Calendar features including day of week (zero to six) and day of month (one to thirty‑one).
    
    F. Event flags indicating whether the day is a payday, a declared holiday, within the thirteenth‑month pay period (typically December), or within the Christmas period (December fifteen to January five).

3. For users with fewer than sixty days of history, the LSTM shall use the available data as the input sequence. 

    A. Missing days before the user's first transaction are set to zero. 
    
    B. For users with between thirty and fifty‑nine days of history, the model accepts the variable‑length sequence.
    
        i. The architecture is designed to handle sequences shorter than the maximum length by masking or by repeating the earliest available values. 
        
    C. For users with fewer than thirty days of history, the LSTM is not used.
    
        i. The System falls back to population‑based forecasts as described in Section 3.

4. The LSTM model shall be pre‑trained on synthetic transaction data generated from the BSP Consumer Finance Survey 2021 and the PSA Family Income and Expenditure Survey. 

    A. The synthetic data generation process produces daily sequences of spending across the four broad groups, respecting the aggregate category means and variability reported in the surveys. 
    
> [OPEN: The detailed synthetic data generation procedure is documented in the companion file model‑training‑data‑design.md, which the researchers should reference for reproducibility.]

5. In the thesis version, the LSTM model shall be deployed as a frozen pre‑trained model. 

    A. No fine‑tuning on individual user data shall occur, because the thesis ethical protocol prohibits using real user data for training or updating models. 
    
    B. This is a deliberate scope limitation; the model uses only the global pre‑trained weights and the user's own transaction history as input features at inference time. 
    
    C. The System shall not perform weekly fine‑tuning as previously contemplated. 
    
> [FUTURE WORK] Fine‑tuning on user data with explicit consent and on‑device training is recommended for future versions beyond the thesis.

6. The LSTM model shall be hosted on a cloud server, such as AWS Lambda or Google Cloud Run, with an inference timeout of 2500 milliseconds. 

    A. The mobile application shall cache the most recent forecast for each target. 
    
    B. When offline, the application shall display cached forecasts with a note stating, "Offline mode — forecasts from [date]." 
    
    C. No forecast inference shall be attempted directly from the mobile device.

### Section 3. Cold-Start Fallback.

1. For users with fewer than thirty days of transaction history, the System shall use population‑level fallbacks instead of LSTM forecasts.

2. For expense forecasts, the fallback source is the Family Income and Expenditure Survey category means, stratified by the user's income quintile as reported during onboarding. 

    A. The researchers shall use the most recent available FIES data at the time of development. 
    
> [RRL NEEDED: If the most recent FIES is older than three years, the researchers should adjust historical means by cumulative inflation using PSA inflation data as a temporary measure. The specific adjustment method requires validation.]

3. For income forecasts, the fallback source is the BSP Consumer Finance Survey median income by occupation category, stratified by the user's occupation as reported during onboarding.

4. For savings trajectory forecasts, the fallback assumes a linear contribution of five percent of monthly income to savings, with no withdrawals.

5. For debt payoff forecasts, the fallback uses the user‑entered debt terms, including principal, interest rate, minimum payment, and due date. No population data is required.

6. When the user accumulates thirty days of transaction history, the System shall automatically switch from fallback forecasts to LSTM forecasts. 

    A. Upon switching, the System shall display a notification: "Odin now has enough data to create personalised forecasts for you."

### Section 4. Explainability.

1. Explainability for LSTM forecasts shall use a feature perturbation method rather than SHAP, which is computationally expensive for sequential models. 

    A. For each forecast, the System shall measure how the prediction changes when each input feature is shuffled or set to a baseline value. 
    
    B. The feature that causes the largest change in prediction is identified as the most influential.

2. For user‑facing explanations, the System shall not present raw perturbation values. 

    A. Instead, it shall generate a simple template sentence based on observable patterns. 
    
    B. For example: "Your Discretionary spending is predicted to increase because your spending in the last seven days is 850 pesos higher than your thirty‑day average." 
    
    C. The System shall also state the confidence indirectly by comparing the forecast to the user's historical range: "Forecast for tomorrow is 1,200 pesos, which is within your typical daily range of 500 to 2,000 pesos."

> [OPEN: Team Decision] The attention‑based explainability method mentioned in the BIBLE is not implemented because the LSTM architecture in this version does not include an attention layer. Adding attention would change the model architecture and increase complexity. The feature perturbation method described above is sufficient for the thesis scope.

### Section 5. Evaluation Metrics.

1. The forecasting module shall be evaluated weekly using walk‑forward validation on synthetic data. 

    A. The synthetic test set is distinct from the training set and represents six months of simulated user activity. 
    
    B. The evaluation uses a rolling window: train on the first sixty days, test on the next seven days, then roll forward by seven days, repeating for a total of twenty‑six iterations.

2. The primary metric is Mean Absolute Error (MAE), calculated as the average absolute difference between forecast and actual spending. 

    A. The acceptable threshold is less than fifteen percent of the category mean for high‑volume categories (Essentials and Discretionary). 
    
    B. For low‑volume categories (Obligatory and Financial Allocation, where many users have zero spending on many days), MAE is less informative.
    
        i. The System shall instead rely on sMAPE as defined below.

3. The secondary metric is Root Mean Square Error (RMSE), calculated as the square root of the average squared difference. 

    A. The acceptable threshold is less than twenty percent of the category mean for high‑volume categories.

4. The tertiary metric is the symmetric Mean Absolute Percentage Error (sMAPE), calculated as the average of the absolute difference divided by the average of the forecast and actual values, expressed as a percentage. 

    A. The acceptable threshold is less than twenty‑five percent for Essentials and Discretionary. 
    
    B. The acceptable threshold is less than thirty percent for Obligatory and Financial Allocation.

5. The fourth metric is Improvement over Fallback (IoF), calculated as the MAE of the fallback model minus the MAE of the LSTM model, divided by the MAE of the fallback model, expressed as a percentage. 

    A. The acceptable threshold is twenty percent or higher. 
    
    B. If IoF remains below twenty percent after thirty days of user data collection, the System shall log a warning, but no automatic retraining occurs because the model is frozen for the thesis.

6. The fifth metric is forecast bias, calculated as the mean of (forecast minus actual) divided by the mean of actual. 

    A. The acceptable range is between negative 0.10 and positive 0.10, indicating that the model does not systematically over‑forecast or under‑forecast.

> [RRL NEEDED: The three‑week persistence threshold for action (exceeding acceptable metrics for three consecutive weeks) is provisional. The researchers should justify this based on concept drift literature or adjust the threshold after pilot testing.]

7. If any metric exceeds its acceptable threshold for three consecutive weeks on the synthetic evaluation, the researchers shall log the issue and consider retraining the model from scratch using a different hyperparameter configuration. 

    A. In the thesis context, this retraining would occur offline, not automatically.

### Section 6. Connection to Other Modules

1. The LSTM forecasting module receives the user's financial behavioral profile from the Random Forest classifier as an input feature. 

    A. The forecasted amounts for the four broad groups are passed to the budget recommendation module as the basis for total budget calculation and category floor/cap constraints. 
    
    B. The forecasted savings balance trajectory is displayed in the savings goal tracking interface. 
    
    C. The forecasted debt remaining balance is displayed in the debt management interface. 
    
    D. The Isolation Forest anomaly detection module does not directly consume LSTM forecasts in the thesis version, but future versions may compare actual transactions against forecasted category amounts to improve anomaly detection.

---

## Article VIII: Anomaly Detection Module

### Section 1. Primary Detection Method.

1. Anomaly detection shall be performed using Isolation Forest, an unsupervised algorithm that isolates anomalies by randomly partitioning the feature space. 

2. The model shall operate on a per‑user basis, learning the user's baseline spending behaviour from their transaction history. 

3. A minimum of fourteen days of transaction history is required before the Isolation Forest is enabled. 
    
4. For users with fewer than fourteen days, anomaly detection shall be disabled, and only rule‑based budget overspending alerts (described in Section 5) shall be shown.

5. The Isolation Forest shall use the following specifications:

    A. The number of estimators (decision trees) is one hundred. 
    
    B. The maximum number of samples used to train each tree is two hundred fifty‑six, or the total number of transactions if fewer. 
    
    C. The random state is fixed at forty‑two for reproducibility. 
    
    D. The contamination rate, which represents the expected proportion of anomalous transactions in the data, shall not be fixed at a constant value. 
    
        i. Instead, the System shall use the raw anomaly scores produced by Isolation Forest and apply a dynamic threshold: the top five percent of scores by transaction volume shall be flagged as anomalies. 
    
        ii. This approach adapts to each user's actual spending variability rather than forcing exactly five percent of transactions to be flagged regardless of behaviour.

6. The feature vector for each expense transaction shall consist of eight dimensions, derived from the transaction and the user's historical data. 

    A. All features are normalised or standardised before being passed to the Isolation Forest.

7. The feature vector dimensions are the following:

    A. The amount deviation feature is calculated as the transaction amount minus the median amount for the same detailed category over the preceding thirty days, divided by the interquartile range of amounts for that category over the same period. 
    
        i. The result is capped at plus or minus five to prevent extreme outliers from dominating.

    B. The amount‑to‑income ratio is calculated as the transaction amount divided by the user's monthly income (updated when new income transactions are recorded). 
    
        i. This feature identifies transactions that are unusually large relative to the user's earning capacity.

    C. The category average ratio is calculated as the transaction amount divided by the average amount for the same detailed category over the preceding thirty days. 
    
        i. A value substantially greater than one indicates an unusually large transaction for that category.

    D. The days since payday feature captures the number of days between the transaction date and the most recent payday. 
    
        i. This helps distinguish normal payday spending spikes from off‑cycle unusual spending.

    E. The `is_recurring` flag, a binary feature, indicates whether the transaction is part of a recurring template (as defined in Article II). 
    
        i. Recurring transactions are rarely anomalous and this feature helps the model suppress false positives on regular bills.

    F. The detailed category is encoded as a one‑hot vector representing the specific subcategory selected by the user. 

        i. The broad LSTM category (Essentials, Obligatory, Discretionary, or Financial Allocation) is also included as an additional categorical feature.

    G. The day of month (one to thirty‑one) and day of week (zero to six) are included as cyclical features to capture monthly bill cycles and weekday versus weekend spending patterns.

    H. The merchant novelty flag is set to one if the merchant name has not appeared in any transaction by this user in the preceding sixty days, and zero otherwise. 
    
        i. When the user does not provide a merchant name, this flag defaults to zero.

> [OPEN: Team Decision] The merchant novelty flag uses a hard sixty‑day cutoff. An alternative approach using a decay function (where novelty decays gradually over time) may produce smoother results but adds complexity. The hard cutoff is acceptable for the thesis scope.

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

Day-of-period proportion is calculated based on the user's currently active budget period. If the user has no active budget, the System defaults to a 30-day rolling period starting from the first day of the current month. The period resets when the user creates a new budget or at the end of the default rolling period.

> NOTE: This footnote should have gone to the description instead.

> Claude: Section 2 Features: "Merchant novelty" - 1 if merchant not seen in last 60 days. ASK: What about merchants that appear, disappear, then reappear after 61 days? That would be flagged as novel again. Is that intended? Consider using a decay function rather than a hard cutoff.

> Claude: Section 2: "Day-of-period proportion" depends on active budget period. ASK: What if the user has multiple overlapping budgets (e.g., monthly budget and a separate event budget)? The system only supports one active budget at a time per Article VI. Clarify that the anomaly detection period aligns with the single active budget period.

### Section 3. Occasions

1. Certain transactions that would otherwise be flagged as anomalies shall be excluded from alert generation because they represent culturally expected spending spikes. 

    A. The System shall still compute anomaly scores for these transactions for internal logging and model evaluation, but shall not generate user notifications unless the user has enabled informational alerts.

2. The following periods are excluded from anomaly alerting:

    A. Transactions between December fifteen and January five (the extended Christmas and New Year period) shall not trigger anomaly alerts. 
    
    B. Transactions during Holy Week (from Palm Sunday to Easter Sunday) shall not trigger alerts. 
    
    C. For Holy Week dates, the System shall use an annually updated holiday calendar stored as a JSON configuration file. 
    
    D. If the current year's Holy Week dates are not yet loaded, the System shall compute Easter using an algorithmic method (such as the Anonymous Gregorian algorithm) as a fallback, rather than using an overly broad date range.

    E. Transactions during the user's declared home barangay fiesta dates, plus or minus three days, shall not trigger alerts. The user may configure their home barangay and fiesta dates in the profile settings.

    F. Transactions manually whitelisted by the user, as described in Section 3, are permanently excluded from anomaly alerts regardless of amount or timing.

3. For excluded transactions, the System may still provide an informational notification if the anomaly score exceeds the threshold, but the notification shall be labelled as informational rather than a warning. 

    A. The user may configure whether informational alerts are shown.

> [OPEN: Team Decision] The System shall not automatically connect to a calendar or holiday API, as this adds external dependencies and potential failure points. A manually maintained JSON holiday calendar updated annually is sufficient for the thesis scope. The researchers may recommend API integration as future work.

### Section 4. Whitelist Mechanism.

1. When a transaction is flagged as anomalous, the System shall present the user with a notification stating, "[Amount in pesos] at [merchant name] appears unusual for your [category] spending. Was this expected?" 

2. The user may select from three responses.

    A. If the user selects "Yes, expected," the System shall add an entry to the whitelist. 
    
        i. Each whitelist entry contains the merchant name, the detailed category of the transaction, and an amount tolerance of plus or minus twenty‑five percent. 
        
        ii. Future transactions with the same merchant name and same detailed category, and with an amount within the tolerance range, shall be suppressed from anomaly alerts. 
        
        iii. If the user selects "Always allow this merchant regardless of amount," the whitelist entry stores no amount tolerance, and all future transactions with that merchant name and category are suppressed.

    B. If the user selects "No, unexpected," the transaction remains flagged as an anomaly, and no whitelist entry is created. 
    
    C. If the user selects "Remind me later," the notification is dismissed for this transaction but no whitelist entry is created.
    
        i. Future similar transactions may still trigger alerts.

The user may view, edit, or delete whitelist entries in Settings under Anomaly Detection → Whitelist.

### Section 5. Overspending Detection.

1. In addition to Isolation Forest, the System shall implement rule‑based budget overspending detection as a separate submodule. 

    A. This submodule does not use machine learning and operates independently of the anomaly detection whitelist or cultural exclusions.

3. The System shall generate an alert when any category exceeds eighty percent of its budget allocation with more than twenty‑five percent of the budget period remaining. 

4. The System shall generate a critical alert when any category exceeds one hundred percent of its budget allocation at any time.

5. These overspending alerts are mandatory and cannot be disabled by the user, though the user may configure notification delivery method (in‑app only or push). 

    A. The alerts are displayed regardless of whether the transactions would otherwise be considered anomalous or culturally expected.

### Section 6. Alert Fatigue Prevention.

1. The System shall implement three mechanisms to prevent alert fatigue:

    A. First, a cooldown period limits anomaly alerts to no more than three per user per twenty‑four hour period. 
    
        i. Rule‑based overspending alerts are excluded from this cooldown. 
        
    B. Second, multiple anomalies detected within two hours are bundled into a single notification that lists all affected transactions. 
    
    C. Third, the user may snooze all anomaly alerts for seven days via Settings → Notifications.

> [OPEN: Team Decision] Sensitivity adjustment (allowing the user to change the contamination threshold) is not exposed in the main settings. It may be added as an advanced setting hidden behind an expander, but for the thesis scope the default dynamic threshold (top five percent of anomaly scores) is sufficient. The team may decide to omit sensitivity adjustment entirely.

### Section 7. Explainability.

1. For each anomaly alert, the System shall compute the deviation of each continuous feature from the user's baseline. 

    A. The baseline for amount deviation is the category median over the preceding thirty days.
    
    B. The baseline for amount‑to‑income ratio is the user's typical ratio for that category.
        
    C. The baseline for days since payday is the user's typical distribution of transaction timing. 
        
    D. The explanation shall present the feature with the largest standardised deviation.

2. For example: "This transaction was flagged because the amount (5,000 pesos) is 2.5 standard deviations above your usual Food spending of 800 pesos." 

    A. For a merchant novelty flag: "This transaction was flagged because you have never spent at this merchant before in the last 60 days."

3. This explanation method requires no per‑transaction model fitting and is instantaneous, as it uses pre‑computed summary statistics.

### Section 8. Evaluation Metrics.

1. The anomaly detection module shall be evaluated on synthetic data using walk‑forward validation. 

    A. The synthetic dataset shall include injected anomalies at a rate of approximately five percent, distributed across categories and amount deviations. 
    
    B. The validation window uses thirty days of training data, tests on the next seven days, and rolls forward for thirteen iterations.

2. Precision, defined as true positives divided by the sum of true positives and false positives, shall have a target of at least 0.70. 

3. Recall, defined as true positives divided by the sum of true positives and false negatives, shall have a target of at least 0.65. 

4. The F1 score, the harmonic mean of precision and recall, shall have a target of at least 0.675.

5. The false positive rate per user per week, calculated as the number of false positives divided by active days multiplied by seven, shall have a target of no more than 1.5 false positives per week. 

    A. This target is mathematically consistent with the precision and recall targets given a typical transaction volume.

6. For real user evaluation where true labels are not available, the System shall report the user dismissal rate (percentage of alerts that the user marks as "Yes, expected") and the alert acknowledgement rate as proxies for precision. 

    A. A low dismissal rate (many users marking alerts as expected) indicates excessive false positives.

### Section 8. Connection to Other Modules

1. The Isolation Forest anomaly detection module receives the user's financial behavioural profile from the Random Forest classifier, which is used as a categorical feature. 

    A. The rule‑based overspending detection submodule receives the current active budget allocations from the budget recommendation module. 
    
    B. Anomaly alerts and overspending alerts are both passed to the Alerts and Notifications module (Article XI). 
    
    C. The user's whitelist entries are stored and consulted before any anomaly alert is generated.

2. In the thesis version, the Isolation Forest does not compare transactions against LSTM forecasts. 

> [FUTURE WORK] Incorporating forecasted category spending as an additional feature for anomaly detection is recommended for future versions.

---

## Article IX: Savings Goal Tracking

### Section 1. Goal Definition.

1. A savings goal in the System represents a target amount that the user wishes to accumulate over time through regular contributions. 

2. Each goal shall consist of the following required fields. 
    
    A. The goal name is a string of up to fifty characters and must be unique per user. 
    
    B. The target amount is the desired total accumulation, measured in Philippine pesos, with a minimum of one hundred pesos and a maximum of ten million pesos. 
    
    C. The target date is the date by which the user wishes to achieve the goal, which must be at least seven days from the goal creation date and no more than ten years into the future. 
    
    D. The contribution amount is the amount the user commits to contributing per contribution frequency, with a minimum of ten pesos per contribution. 
    
    E. The contribution frequency is selectable from daily, weekly, bi‑weekly, or monthly. 
    
    F. The linked source is the account from which contributions are deducted.
    
        i. The default is the available balance of the user's primary cash account, but the user may select any specific income category or account.

3. The System shall treat savings goals as financial allocation targets. 

    A. Contributions to a savings goal are recorded as expense transactions under the Financial Allocation broad group, with a detailed category named after the goal. 
    
    B. When a contribution is made, the System subtracts the amount from the linked source account's available balance and adds it to the goal's current accumulated amount.

3. The System does not support investment goals with variable returns, insurance premium tracking, or any goal type where the accumulation amount is not deterministic. 

    A. These are explicitly excluded from the thesis scope. 
    
> [FUTURE WORK] Separate modules for investment tracking and insurance management are recommended for future versions.

### Section 2. Multiple Concurrent Goals.

1. The System shall support up to five concurrent savings goals per user. 

    A. When multiple goals exist, the user shall prioritise them via drag‑and‑drop in the user interface. 
    
    B. The System shall apply contributions in priority order during each contribution cycle. 
    
    C. The contribution cycle runs daily: for each goal, the System checks whether the current date matches the goal's contribution schedule based on its frequency. 
    
    D. For daily goals, every day is a contribution date. 
    
    E. For weekly goals, contributions occur on the same day of the week as the creation date. 
    
    F. For bi‑weekly goals, contributions occur every fourteen days. 
    
    G. For monthly goals, contributions occur on the same day of the month as the creation date, or on the last day of the month if that day does not exist in a given month.

2. When a contribution date arrives for a goal, the System shall attempt to deduct the contribution amount from the linked source account. 

    A. If the available balance is sufficient, the deduction occurs and the goal's accumulated amount increases. 
    
    B. If the available balance is insufficient, the System shall skip the contribution for that goal and proceed to the next lower‑priority goal. 
    
    C. The skipped contribution is not queued or retried later. 
    
        i. The user is notified of the skipped contribution and may manually contribute later or adjust the contribution amount.

3. After processing all goals that have a contribution on the current date, any remaining available balance is left untouched for discretionary spending or future contributions. 

    A. The System does not automatically redistribute unused contribution capacity.

4. The limit of five concurrent goals is based on user interface complexity and cognitive load. 

> [OPEN: Team Decision] If the team determines that users may need more than five goals, the limit may be increased to ten with appropriate UI changes such as collapsible sections or a goals summary screen.

### Section 3. Progress State Calculation.

1. For each goal at each contribution date, the System shall compute the progress state as follows:

    A. The remaining amount is the target amount minus the current accumulated amount. 
    
    B. The number of remaining contributions is calculated as the number of contribution dates between the current date and the target date, based on the goal's contribution frequency. 
    
    C. If the number of remaining contributions is zero (the target date has passed), the goal state is evaluated as achieved or failed based on whether the accumulated amount meets or exceeds the target.

2. The required contribution per period is the remaining amount divided by the number of remaining contributions. 

    A. If the user's actual contribution amount (the amount the user has committed to contribute each period, not necessarily the amount actually contributed after skipped contributions) is greater than or equal to 1.10 times the required contribution, the state is "ahead." 
    
    B. If the actual contribution amount is between 0.90 and 1.10 times the required contribution, the state is "on track." 
    
    C. If the actual contribution amount is between 0.50 and 0.90 times the required contribution, the state is "behind." 
    
    D. If the actual contribution amount is less than 0.50 times the required contribution, the state is "critical."

3. The System shall display a circular progress indicator for each goal, using colour coding: green for ahead or on track, yellow for behind, and red for critical. 

    A. Hovering or tapping the indicator shows the numeric percentage and the state description.

### Section 4. Savings Contribution Strategies.

1. The System shall offer three contribution allocation strategies that determine how surplus funds (beyond the scheduled contributions) are distributed across multiple goals. 

    A. These strategies apply only when the user has more than one goal and when the available balance after all scheduled contributions is positive.

2. The three contribution allocation strategies are the following:

    A. Under the Goal‑based strategy, which is the default for all profiles, any surplus is allocated to the highest‑priority goal first. 
    
        i. After that goal's target is reached, surplus flows to the next‑highest priority goal, and so on. 
        
        ii. This strategy aligns with the user's explicit ranking of goals.

    B. Under the Snowball strategy, which is offered as an alternative for Variable‑Flexible users, the System allocates surplus to the goal with the smallest remaining amount (target minus current accumulated). 
    
        i. The rationale is to provide psychological motivation by paying off smaller goals quickly, analogous to the debt snowball method.

    C. Under the Avalanche strategy, which is offered as an alternative for Stable‑Obligated users, the System allocates surplus to the goal with the highest user‑ranked priority. 
    
        i. This is identical to the Goal‑based strategy in outcome but emphasises the interest analogy. 
        
        ii. The name is retained for consistency with debt management terminology.

3. The user may switch strategies at any time via Savings → Strategy. 

    A. When switching, the System shall recalculate projected completion dates for all goals under the new strategy and display a comparison: "If you switch to Snowball, Goal A would be completed 3 months earlier, but Goal B would be completed 2 months later."

> [RRL NEEDED] The assignment of default strategies to profiles (Goal‑based for all profiles, with Snowball and Avalanche as alternatives) requires validation from literature on savings motivation and goal prioritisation. The researchers should survey target users or cite existing studies on what drives savings behaviour among Filipino young adults.

### Section 5. Notifications.

1. The System shall send the following savings‑related notifications:

    A. When a goal reaches twenty‑five percent, fifty percent, or seventy‑five percent of its target amount, the System shall send a milestone notification: "You're 50% of the way to your [goal name] goal!" 
    
    B. When a goal has been in the "behind" state for seven consecutive days, the System shall send an advisory notification: "Your [goal name] goal is behind schedule. Consider increasing your contribution amount or adjusting the target date." 
    
        i. The user may dismiss this notification, but it will reappear every seven days until the goal returns to on track or ahead, or until the user updates the goal's parameters.

    C. When a goal's accumulated amount reaches or exceeds the target amount, the System shall send a congratulatory notification: "Congratulations! You achieved your [goal name] goal." 
    
        i. The goal is then marked as completed and is removed from the active goals list. 
        
        ii. The user may archive completed goals for historical reference.

### Section 6. Connection to Other Modules

1. The savings goal tracking module receives forecasted savings balance trajectory from the LSTM forecasting module (Article VII), which is displayed as a projection line on the goal progress chart. 

2. The module also receives the user's available balance from the account management system (Article V) to determine whether scheduled contributions can be fulfilled. 

3. When a contribution is skipped due to insufficient balance, the module sends a notification to the Alerts and Notifications module (Article XI). 

4. The contribution allocation strategies are evaluated independently; they do not interact with the budget recommendation module's surplus handling strategies (Article VI Section 5), as the two mechanisms operate on different time scales and purposes.

---

## Article X: Debt Management

### Section 1. Debt Account Definition.

1. A debt account in the System represents a liability that the user owes to a creditor, with a defined principal, interest rate, and repayment schedule. 

2. Each debt account shall consist of the following required fields:

    A. The debt name is a string of up to fifty characters, unique per user. 
    
    B. The total principal amount is the original amount borrowed, measured in Philippine pesos, with a minimum of one hundred pesos and a maximum of ten million pesos. 
    
    C. The annual interest rate is stored as a decimal, for example 0.05 for five percent, and may range from zero to one hundred percent inclusive. 
    
    D. The System assumes simple interest for all debt accounts. 
    
    E. Compound interest, such as that on credit card revolving balances, is not supported in this version. 
    
    F. The minimum monthly payment is the smallest amount the user must pay each month to keep the account in good standing, measured in pesos, and may be zero. 
    
    G. The payment due day of month is an integer from one to thirty‑one; if the due day is greater than the number of days in a given month, the System shall treat the due date as the last day of that month. 
    
    H. The remaining balance is computed as the principal amount minus the sum of all payments recorded against this debt account, and is automatically updated whenever a debt payment transaction is recorded.

2. The System shall also store, optionally, the creditor name and contact information, which may be displayed to the user during hardship scenarios as described in Section 4.

> [OPEN: Team Decision] Compound interest for credit cards and similar revolving debt is explicitly excluded from the thesis scope. The System assumes that users will either pay credit card balances in full each month (thus incurring no interest) or will treat credit card debt as a separate simple‑interest loan with an agreed interest rate. If the team determines that compound interest is essential for the target users, a future version should add a compounding frequency field.

### Section 2. Payoff Strategies.

1. The System shall implement two debt payoff strategies, and the user may switch between them at any time. 

    A. Under the Avalanche strategy, the System allocates any surplus payment amount (beyond the sum of all minimum monthly payments) to the debt with the highest annual interest rate. 

        i. This strategy minimises the total interest paid over the life of all debts. 
    
    B. Under the Snowball strategy, the System allocates surplus payment amount to the debt with the smallest remaining balance, regardless of interest rate. 
    
        i. This strategy minimises the time to the first debt payoff, providing psychological motivation.

2. When the user switches from one strategy to another, the System shall recalculate the projected payoff dates and total interest for all debts under the new strategy. 

    A. Retained payments already made are not changed retroactively. 
    
    B. The System shall display a comparison message: "If you switch from Avalanche to Snowball, you would pay an additional 1,200 pesos in total interest, but you would pay off your smallest debt three months earlier. Continue?" 
    
    C. The user must confirm the switch before it takes effect.

3. The surplus payment amount is defined as the user's total available funds allocated to debt repayment in a given month, minus the sum of all minimum monthly payments. 

    A. The total available funds allocated to debt repayment is determined by the budget recommendation module (Article VI) as part of the Obligatory category allocation. 
    
    B. The user may also manually specify a higher debt repayment amount.

### Section 3. Projection Display.

1. For each debt account individually, and for the aggregate of all debt accounts, the System shall display the following projections:

    A. The remaining balance is shown in pesos, updated after each payment transaction. 
    
    B. The projected payoff date is the date when the remaining balance is expected to reach zero or less, assuming the user makes the minimum monthly payment each month plus any surplus allocated according to the selected payoff strategy. 
    
    C. The total interest projected under the current strategy is the sum of all future interest payments until payoff, assuming no changes to the payment schedule. 
    
    D. The total interest projected under the alternative strategy is also shown for comparison, with an explanation of the difference.

2. The projection calculations assume that the user continues to follow the selected strategy and that no additional debt is incurred. 

    A. The System shall display a disclaimer: "Projections assume you make all minimum payments on time and do not take on new debt."

### Section 4. Minimum Payment Validation.

1. The System shall not permit a recorded monthly debt payment that is below the account's minimum monthly payment unless one of two conditions is met. 

    A. First, the user may explicitly override the minimum payment by confirming a dialog that states: "Paying below the minimum may incur late fees and damage your credit score. Continue anyway? Yes / No." 
    
    B. Second, if the user's available balance across all accounts is less than the sum of all minimum payments for the month, the System shall automatically enter hardship mode.

2. When hardship mode is detected, the System shall display a debt hardship screen that includes three elements. 

    A. First, a warning that the user's total minimum payments exceed their available balance. 
    
    B. Second, a recommendation to contact each creditor, displaying the creditor's name and contact information if the user has provided it. 
    
    C. Third, a link to the National Credit Council's debt counselling page if available. 
    
3. The System shall also display an option for the user to proceed with reduced payments by acknowledging: "I understand that paying below the minimum may incur fees and affect my credit score." No automated contact with creditors is made.

> [OPEN: Team Decision] The definition of "available balance is less than the sum of all minimum payments" is evaluated at the time the user attempts to record debt payments, typically at the end of the month before due dates. The System does not automatically detect hardship in advance; the user must initiate the payment recording process. A future enhancement could proactively alert the user when upcoming minimum payments exceed projected available balance based on the LSTM forecast.

### Section 5. Debt Alerts.

1. The System shall send the following debt‑related notifications:

    A. Three days before a debt account's payment due date, the System shall send an upcoming due date reminder: "Your [debt name] payment of [minimum amount] pesos is due on [date]." 
    
    B. If the due date passes and no payment has been recorded for that month by the following day, the System shall send a missed payment alert: "Your [debt name] payment was due yesterday. Please record your payment to avoid late fees." 
    
    C. When a debt account reaches fifty percent paid (remaining balance is less than or equal to half of the original principal), the System shall send a milestone notification: "You have paid off 50% of your [debt name]!" 
    
    D. When the remaining balance reaches zero, the System shall send a payoff notification: "Congratulations! You have fully paid off your [debt name]."

2. All debt alerts are delivered via in‑app notification. 

3. The user may enable push notifications for debt alerts separately from other alert categories.

### Section 6. Connection to Other Modules

1. The debt management module receives the user's available balance from the account management system (Article V) to validate minimum payments and detect hardship. 

2. It receives the forecasted income and the Obligatory category allocation from the budget recommendation module (Article VI) to determine the surplus amount available for debt repayment beyond minimum payments. 

3. The debt payoff projections are displayed in the forecasting module's debt remaining balance view (Article VII Section 1). 

4. The debt alerts are passed to the Alerts and Notifications module (Article XI). 

5. The debt management module does not interact directly with the Random Forest or Isolation Forest models.

---

## Article XI: Alerts and Notifications (Comprehensive)

### Section 1. Alert Types.

1. The System shall generate alerts for five categories, each originating from a specific module. 

    A. The first category is budget overspending, which includes two specific alerts: 
    
        i. A warning when a category exceeds eighty percent of its budget allocation with more than twenty‑five percent of the budget period remaining.
        
        ii. A critical alert when any category exceeds one hundred percent of its budget allocation at any time. 
        
        iii. These alerts originate from the rule‑based overspending detection submodule (Article VIII Section 4).

    B. The second category is anomaly detection, which triggers when the Isolation Forest identifies a transaction as anomalous and the transaction is not excluded by cultural period rules or whitelist (Article VIII Sections 1 through 3). 
    
    C. The third category is savings milestone, which includes alerts at twenty‑five, fifty, and seventy‑five percent progress toward a savings goal, as well as goal achievement (Article IX Section 5). 
    
    D. The fourth category is forecast‑based advisory, which provides proactive guidance when current spending patterns suggest a future budget violation. 
    
    E. The fifth category is debt management, which includes upcoming due date reminders, missed payment alerts, and payoff milestones (Article X Section 5).

2. For forecast‑based advisory alerts, the trigger condition is defined as follows. 

    A. The System shall evaluate daily whether the user's current spending trajectory, extrapolated linearly to the end of the budget period, would exceed the total budget by more than ten percent, and whether more than fifty percent of the budget period remains. 
    
        i. If both conditions are true, the System shall generate an advisory alert: "Your current spending suggests you may exceed your budget by [amount in pesos] by the end of the period. Consider reducing discretionary spending." 
        
        ii. The threshold of ten percent and fifty percent remaining are configurable via system parameters but shall not be user‑adjustable in the thesis version.

### Section 2. Delivery Method.

1. All alerts shall be delivered as in‑app notifications, appearing in a notification centre accessible via a bell icon badge on the dashboard. 

    A. The badge displays a count of unread alerts. 

2. When the user opens the notification centre, alerts are grouped by category and sorted chronologically with the most recent first.

3. If the user grants permission, the System shall also send push notifications to the user's mobile device for all alert categories except forecast‑based advisory, which is in‑app only by default. 

4. The user may separately configure push notification preferences per category, enabling or disabling push for anomaly, savings milestone, and debt alerts. 

5. Budget overspending alerts are mandatory and cannot be disabled for either in‑app or push delivery. 

    A. The user may only choose whether to receive push notifications for them.

6. Email digests are excluded from the thesis scope. 

> [FUTURE WORK] A weekly email summary of alerts may be added in a future version.

### Section 3. Alert Display Format.

1. Each alert shall contain a title, a body, an action button, and a dismiss button. 

    A. The title briefly identifies the alert category, for example "Budget Overspending Warning" or "Unusual Transaction Detected." 
    
    B. The body provides a specific description. 
    
        i. For a budget overspending alert: "You have used 85% of your Food budget with 10 days remaining." 
        
        ii. For an anomaly alert: "PHP 4,800 at OnlineShop is higher than your usual PHP 700 for online shopping." 
        
        iii. For a forecast advisory: "Your current spending suggests you may exceed your total budget by PHP 1,500 by the end of the month."

    C. The action button opens the relevant screen where the user can take corrective action. 
    
        i. For budget alerts, the action button opens the budget screen showing the affected category. 
        
        ii. For anomaly alerts, the action button opens the transaction list filtered to the flagged transaction, with the whitelist options available. 
        
        iii. For forecast advisories, the action button opens the forecasting dashboard. 
        
        iv. For savings milestones, the action button opens the savings goal detail screen. 
        
        v. For debt alerts, the action button opens the debt management screen.

    D. The dismiss button acknowledges the alert and removes it from the notification centre. 
    
        i. Dismissed alerts are logged but not shown again. 
        
        ii. The user may also clear all alerts at once using a "Clear all" button.

### Section 4. User Alert Configuration.

1. Users may configure alert preferences per category in Settings → Notifications, with the following exceptions. 

    A. Budget overspending alerts are mandatory; the user cannot disable them but may choose to receive them only in‑app without push notifications. 
    
    B. For anomaly detection alerts, the user may enable or disable them entirely, or set them to informational only (no push, only in‑app). 
    
    C. For forecast‑based advisory alerts, the user may enable or disable them. 
    
    D. For savings milestone alerts, the user may enable or disable them. 
    
    E. For debt alerts, the user may enable or disable them.

2. The user may also set a cooldown period for duplicate alerts, ranging from one to twenty‑four hours, which applies to anomaly detection alerts only. 

    A. Within the cooldown period, if the same category and similar magnitude anomaly occurs again, no new alert is generated. 
    
    B. The cooldown is per category, not per merchant or amount.

3. Sensitivity adjustment (low, medium, high) for anomaly detection is not exposed to users in the main settings. 

4. The dynamic threshold described in Article VIII Section 1 (top five percent of anomaly scores) is fixed. 

> [OPEN: Team Decision] If the team determines that users require sensitivity control, it may be added as an advanced setting behind an expander. The thesis scope does not require this feature.

### Section 5. Alert Persistence and Acknowledgment

1. Unread alerts remain in the notification centre until the user dismisses them or acknowledges them by tapping the action button. 

2. Alerts do not expire automatically. 

3. When the user taps the action button and performs the suggested action (for example, viewing the budget screen), the alert is marked as read but remains in the notification centre under a "History" section until manually cleared.

4. For anomaly alerts that include whitelist options, the acknowledgment choices ("Yes, expected," "No, unexpected," "Remind me later") are presented within the alert itself. 

    A. Selecting "Yes, expected" creates a whitelist entry and dismisses the alert. 
    
    B. Selecting "No, unexpected" dismisses the alert without whitelisting. 
    
    C. Selecting "Remind me later" dismisses the alert but schedules a reminder notification for the same transaction after twenty‑four hours, unless the user has already whitelisted or dismissed it permanently.

### Section 6. Connection to Other Modules

1. The Alerts and Notifications module receives alerts from:

    A. The rule‑based overspending detection submodule (Article VIII Section 4).
    
    B. The Isolation Forest anomaly detection module (Article VIII).
    
    C. The savings goal tracking module (Article IX Section 5).
    
    D. The forecasting module (Article VII Section 1 for advisory alerts).
    
    E. The debt management module (Article X Section 5). 

2. The module stores alert history locally on the device and, if the user is logged in, synchronises to the server for multi‑device consistency. 

3. The module does not directly interact with the Random Forest or LSTM models except to receive alert triggers.

---

## Article XII: Explainability Requirements (Cross-Module)

1. All machine learning modules in the System shall provide human‑readable explanations for their predictions and alerts. 

2. The explanation method, output format, and evaluation approach vary by module as defined below.

    A. For the Financial Behavioral Profile classification module using Random Forest, explainability shall be provided using SHAP (SHapley Additive exPlanations). 
    
        i. The System shall compute SHAP values for each classification prediction and present the top three features that most influenced the classification. 
        
        ii. The output format shall be a sentence constructed from the feature names, their values, and the difference from typical users of other profiles. 
        
            a. For example: "Your profile is Stable‑Obligated mainly because your obligation ratio of 0.55 is higher than typical Flexible users, and your monthly spending coefficient of variation of 0.12 indicates stable income." 
            
        iii. The SHAP values shall be stored in the application log for audit purposes and shall be retained for thirty days, after which they are anonymised by removing user identifiers.
        
    B. For the budget recommendation module using Linear Programming, explainability shall be provided by listing the active constraints that shaped the allocation and the user's priority settings that influenced the objective function. 
    
        i. The output format is a template sentence followed by a list of the most binding constraints. 
        
        ii. The template shall state: "Your [period]-day budget is [total] pesos. This is based on your predicted income of [income] and minimum savings target of [savings]." 
        
        iii. Then the System shall add one or two sentences explaining the major constraints: "[amount] pesos is allocated to Essentials because this category is required to be at least [percentage] percent of your budget. [amount] pesos is allocated to Discretionary because this category is capped at [percentage] percent." 
        
        iv. The explanation shall be accessible via a "Why?" button on the budget recommendation screen. 
        
        v. The user may then edit any allocation manually, and the System shall note which constraints were overridden.

    C. For the forecasting module using LSTM, explainability shall be provided using a feature perturbation method rather than SHAP, as SHAP is computationally expensive for sequential models. 
    
        i. For each forecast, the System shall measure how the prediction changes when each input feature is set to a baseline value or shuffled. 
        
        ii. The feature causing the largest change is identified as the most influential. 
        
        iii. For user‑facing explanations, the System shall not present raw perturbation values. 
        
            a. Instead, it shall generate a simple template sentence based on observable patterns: "Your Discretionary spending is predicted to increase because your spending in the last seven days is [amount] higher than your thirty‑day average." 
            
        iv. If no single feature dominates, the System shall state: "Your forecast is consistent with your recent spending patterns." 
        
        v. The LSTM architecture does not include an attention layer in this version, so attention‑based explanations are not available.

    D. For the anomaly detection module using Isolation Forest, explainability shall be provided by computing the deviation of each continuous feature from the user's baseline, using pre‑computed summary statistics (median and interquartile range per category). 
    
        i. The feature with the largest standardised deviation determines the explanation. 
        
        ii. The output format shall be a sentence such as: "This transaction was flagged because the amount (5,000 pesos) is 2.5 standard deviations above your usual Food spending of 800 pesos." 
        
        iii. For the merchant novelty feature, the explanation shall be: "This transaction was flagged because you have never spent at this merchant before in the last 60 days." 
        
        iv. This method requires no per‑transaction model fitting and is instantaneous.

2. All explanation outputs shall be stored in the application log for audit purposes, with a retention period of thirty days. 

3. After thirty days, the logs shall be anonymised by removing user identifiers and rounding amounts to the nearest hundred pesos. 

4. The user may view the explanation for any prediction or alert by tapping a "Why?" button next to the relevant interface element. 

5. The explanation shall be displayed in a modal dialog that also includes a link to Settings → Explainability where the user can learn more about how the System makes decisions.

> [OPEN: Team Decision] The effectiveness of explainability outputs shall be evaluated as part of the user study. The researchers may include two additional measures in the post‑task questionnaire. First, a comprehension check: after showing a user an explanation for a profile classification, ask the user to select which feature was most important from a list. Second, a trust rating: on a scale of one to five, ask the user whether the explanation increased their trust in the System's recommendation. These measures are not mandatory for the thesis but are recommended for a complete evaluation. If the team decides to include them, they should be added to the evaluation protocol in Article XIII.

6. The explainability module does not directly connect to other modules except through the storage and retrieval of explanations for display. 

7. The SHAP values for classification and the perturbation results for forecasting are computed at prediction time and stored alongside the prediction results.

---

## Article XIII: Evaluation and Quality Metrics (ISO/IEC 25010:2023 + SUS)

### Section 1. ISO/IEC 25010:2023 Quality Characteristics.

1. The System shall be evaluated against six quality characteristics from the ISO/IEC 25010:2023 standard, each with a specific measure, acceptable threshold, and evaluation method.

    A. Functional suitability measures the percentage of specified features that pass manual test cases. 
    
        i. The acceptable threshold is at least ninety‑eight percent. 
        
        ii. Evaluation shall be performed using a manual test script containing fifty test cases, each mapped to a specific requirement from Articles I through XII. 
        
        iii. The test case traceability matrix shall be included in Appendix J of the thesis.

    B. Performance efficiency measures the time from user action to user interface response at the ninety‑fifth percentile. 
    
        i. For non‑machine‑learning operations such as transaction entry, budget viewing, and alert acknowledgment, the acceptable threshold is 500 milliseconds or less. 
        
        ii. For machine learning predictions, including profile classification, spending forecast, and anomaly detection, the acceptable threshold is 1500 milliseconds or less at the ninety‑fifth percentile, with a maximum acceptable of 3000 milliseconds at the ninety‑ninth percentile. 
        
        iii. Evaluation shall use automated load testing with one hundred iterations per operation.

    C. Usability shall be measured using the System Usability Scale. 
    
        i. The acceptable threshold is a score of 68 or higher, which represents the industry average. 
        
        ii. A secondary stretch goal is 74 or higher, representing the eighty‑fifth percentile. 
        
        iii. The evaluation protocol is detailed in Section 2.

    D. Reliability shall be measured as mean time between failures during two hours of simulated continuous use. 
    
        i. The acceptable threshold is four hours or more between crashes or unhandled exceptions. 
        
        ii. Evaluation shall be performed by running the application through a scripted sequence of user actions and monitoring crash logs.

    E. Security shall be measured as the number of critical vulnerabilities identified per the OWASP Top Ten. 
    
        i. The acceptable threshold is zero critical vulnerabilities. 
        
        ii. Evaluation shall use static code analysis and a basic penetration test focused on authentication, data storage, and network communication.

    F. Maintainability shall be measured by cyclomatic complexity per function, excluding user interface binding code and third‑party library calls. 
    
        i. The acceptable threshold is ten or less for all application business logic functions, including transaction validation, budget recalculation, alert generation, and feature extraction for machine learning models. 
        
        ii. Machine learning training scripts, Linear Programming solver libraries, and data preprocessing pipelines are exempt, but wrapper functions that call these libraries shall have cyclomatic complexity of ten or less. 
        
        iii. Evaluation shall use static code analysis with a tool such as SonarQube.

> [RRL NEEDED] The cyclomatic complexity threshold of ten is provisional and should be validated against software engineering benchmarks for maintainability. The threshold is commonly cited in industry standards; the researchers should cite a relevant source such as McCabe's original paper or a software quality textbook.

### Section 2. System Usability Scale (SUS) Protocol.

1. The System Usability Scale shall be administered after each participant has used the System actively for fourteen days. 

    A. Active use is defined as recording at least ten transaction entries during the fourteen‑day period. 
    
    B. If a participant does not reach ten transactions, the SUS shall still be administered at day fourteen, but the transaction count shall be recorded as a covariate in the analysis.

2. The target sample size is thirty participants. 

    A. If after four weeks of recruitment the sample size is between twenty and twenty‑nine, the study shall proceed with a post‑hoc power analysis reporting the minimum detectable effect size. 

    B. The sample shall be stratified by financial behavioural profile, with a minimum of six participants per profile. 

    C. The four profiles sum to twenty‑four participants.

        i. The remaining six participants may be from any profile without stratification. 

    D. Recruitment shall occur from at least four different cities in Metro Manila, for example Manila, Quezon City, Makati, and Taguig, but no minimum number of participants is required per city.

3. Each participant shall complete the standard ten‑item System Usability Scale questionnaire, with items scored on a five‑point Likert scale from strongly disagree to strongly agree. 

    A. Scoring shall follow the Brooke (1996) method: for odd‑numbered items, subtract one from the score; for even‑numbered items, subtract the score from five; sum all converted scores; multiply the sum by 2.5 to obtain a score from zero to one hundred. 
    
    B. The mean score across all participants shall be reported with a confidence interval.

4. The SUS shall be administered in person or via an online form. 

    A. The researcher shall read the standardised instructions: "Please rate your agreement with the following statements about Odin. There are no right or wrong answers. Your honest feedback helps us improve the system."

> [OPEN: Team Decision] The fourteen‑day period may be insufficient for users with monthly obligations to experience all system features, such as budget period rollover or end‑of‑month surplus handling. The researchers may consider extending the evaluation period to thirty days for a subset of participants, or acknowledge this as a limitation in the thesis.

### Section 3. Algorithmic Module Evaluation Protocol.

1. Each machine learning module shall be evaluated using walk‑forward validation on synthetic data. 

    A. The synthetic dataset shall be generated from the BSP Consumer Finance Survey 2021 and the PSA Family Income and Expenditure Survey. 
    
    B. No real user data shall be used for training or validation.
    
        i. The pilot user data, if collected, shall be used only for final inference demonstration and not for metric calculation.

2. For the Random Forest classification module, validation shall use a rolling window of sixty days of training data and thirty days of test data, rolling forward by thirty days for six iterations. 

    A. The primary metrics are accuracy, precision, recall, and F1 score, each measured per class and macro‑averaged. 
    
    B. The acceptable threshold for accuracy is 0.85 or higher. 
    
    C. The confusion matrix shall be reported. 
    
    D. This evaluation shall be performed before the user study to confirm model performance.

3. For the LSTM forecasting module, validation shall use walk‑forward with sixty days of training data and seven days of test data, rolling forward by seven days for twenty‑six iterations. 

    A. The primary metrics are Mean Absolute Error (MAE) as a percentage of category mean, Root Mean Square Error (RMSE) as a percentage of category mean, and symmetric Mean Absolute Percentage Error (sMAPE). 
    
    B. The acceptable thresholds are: 
    
        i. MAE less than fifteen percent of category mean for Essentials and Discretionary.
        
        ii. RMSE less than twenty percent of category mean for Essentials and Discretionary.
        
        iii. sMAPE less than twenty‑five percent for Essentials and Discretionary, and less than thirty percent for Obligatory and Financial Allocation. 
        
    C. Improvement over Fallback shall be reported but does not have an acceptability threshold for the thesis.
    
        i. The researchers shall note whether the LSTM outperforms the fallback.

4. For the Isolation Forest anomaly detection module, validation shall use walk‑forward with thirty days of training data and seven days of test data, rolling forward by seven days for thirteen iterations. 

    A. The synthetic test set shall have anomalies injected at approximately five percent of transactions, with amounts two or more standard deviations above the category mean. 
    
    B. The primary metrics are precision, recall, F1 score, and false positive rate per user per week. 
    
    C. The acceptable thresholds are: precision at least 0.70, recall at least 0.65, F1 at least 0.675, and false positive rate no more than 1.5 per week.

5. For the budget recommendation module, which uses Linear Programming rather than machine learning, evaluation shall measure adherence rate. 

    A. Adherence rate is defined as the percentage of users whose actual spending stays within plus or minus twenty percent of the recommended category allocation for at least three of the four broad groups, averaged over the budget period. 
    
    B. The acceptable threshold is seventy percent or higher. 
    
    C. The researchers shall also report the manual modification rate, defined as the percentage of users who manually adjust the recommended allocation before accepting the budget, as a proxy for recommendation quality. 
    
    D. A high modification rate (above fifty percent) suggests that the default priorities or constraints do not match user preferences.

> [RRL NEEDED] The three‑week threshold for triggering retraining or logging warnings (mentioned in earlier articles for forecasting and anomaly detection) is provisional. The researchers should justify this based on concept drift literature or adjust the threshold after pilot testing. In the thesis version, because models are frozen and not retrained on real user data, the three‑week threshold applies only to synthetic evaluation and serves as a diagnostic for model stability, not an automatic action trigger.

### Section 4. Failure Conditions and System Responses.

1. The System shall detect and respond to the following failure conditions. 

2. For each condition, the detection method, system response, and user notification are defined.

3. When the LSTM forecast Mean Absolute Error exceeds twenty percent of the category mean for any broad group for fourteen consecutive days during synthetic evaluation, the System shall log a warning. 

    A. The warning shall be visible to the developer in the application logs. 
    
    B. No automatic action is taken, as the model is frozen for the thesis. 
    
    C. The researchers may manually retrain the model with different hyperparameters offline.

4. When the Isolation Forest anomaly detection F1 score falls below 0.6 for seven consecutive days during synthetic evaluation, the System shall log a warning. 

    A. The System shall continue to use the Isolation Forest for anomaly detection.
    
        i. No automatic fallback to rule‑only occurs, as the synthetic evaluation is offline. 
        
    B. In a deployed version, the System would disable Isolation Forest and revert to rule‑based overspending alerts only, but this is not implemented in the thesis.

5. When the Random Forest classification accuracy on the validation set falls below 0.80 after a retraining run (which occurs only during development, not during user evaluation), the System shall not deploy the new model. 

    A. The previous model shall be retained, and the developer shall be alerted. 
    
    B. This condition is not applicable during the user evaluation because no retraining occurs.

6. When any module throws an unhandled exception at runtime during user evaluation, the System shall catch the exception, log it, and continue operating with graceful degradation. 

    A. For the forecasting module, if an exception occurs, the System shall display a fallback message: "Forecasts are temporarily unavailable. Please check your internet connection and try again later." 
    
    B. For the anomaly detection module, if an exception occurs, the System shall not show anomaly alerts until the next restart, and shall display: "Spending alerts are temporarily simplified. Your data is safe." 
    
    C. For the classification module, if an exception occurs during inference, the System shall use the last known profile and display: "Your financial profile is using saved data. Some recommendations may be less accurate."

7. The System shall also include a disaster recovery and backup plan. 

    A. Automated daily backups of the server database shall be retained for thirty days. 
    
    B. The user may export all their transaction data as a CSV file via Settings → Export Data, and may import a previously exported CSV file to restore data after account deletion or device change. 
    
    C. A developer restore procedure shall be documented in the system administrator manual. 
    
    D. This backup mechanism is for data loss scenarios such as server corruption or user error, not for real‑time synchronisation.

### Section 5. Connection to Other Modules

1. The evaluation framework described in this article is not a runtime module but a development‑time and evaluation‑time protocol. 

2. The metrics defined here are computed offline using Python scripts on synthetic data, or manually during user evaluation for the System Usability Scale. 

3. The results of evaluation shall be reported in the thesis findings chapter. 

4. No runtime module consumes these metrics; they are for research purposes only.

---

## Article XIV: Data Privacy, Security, and Ethical Compliance

### Section 1. Compliance with RA 10173 (Data Privacy Act of 2012).

1. The System shall comply with the Data Privacy Act of 2012 in all aspects of personal financial data processing. 

2. Consent shall be obtained via an explicit opt‑in screen shown before the user can enter any transaction. 

    A. The opt‑in screen shall state: "Odin collects and processes your financial transactions to provide budget recommendations, spending forecasts, anomaly detection, and profile classification. Your data is stored encrypted and is not shared with third parties. You may delete your data at any time." 

    B. The user must tap "I agree" to proceed; declining prevents use of the application.

4. Purpose limitation shall be strictly observed. 

    A. Data shall be used only for the following purposes: generating budget recommendations, producing spending forecasts, detecting anomalous transactions, classifying financial behavioural profiles, and displaying transaction history to the user. 
    
    B. No data shall be used for any other purpose without new consent.

5. Retention period shall be thirteen months from the date of the user's last activity. 

    A. User activity includes any transaction entry, budget change, or login. 
    
    B. After thirteen months of inactivity, the user's data shall be anonymised as follows: the user identifier is removed and replaced with a random non‑reversible token; transaction amounts are rounded to the nearest one hundred pesos; transaction dates are truncated to the month only; all merchant names and descriptions are deleted. 
    
    C. If the user has not given explicit opt‑in for anonymised research use (see below), the data shall be permanently deleted instead of anonymised.

> [RRL NEEDED: Retention period of thirteen months] The choice of thirteen months is provisional and requires validation from either Bangko Sentral ng Pilipinas data retention guidelines, a provision of the Data Privacy Act, or literature on financial data retention for personal finance management systems. If no authoritative source supports thirteen months, the team should adopt a standard period such as twenty‑four months or align with tax record‑keeping recommendations (typically three years in the Philippines). The researchers must resolve this before final submission.

6. Data portability shall be supported. 

    A. The user may request a CSV export of all their transactions, including date, amount, category, merchant name (if provided), and account, via Settings → Export Data. 
    
    B. The export file shall be generated within five minutes of the request and shall be downloadable via a secure link that expires after twenty‑four hours.

7. Data deletion shall be supported. 

    A. The user may request deletion of all their data via Settings → Delete Account. 
    
    B. The System shall display a confirmation dialog: "This will permanently delete all your transactions, budgets, goals, and settings. This action cannot be undone. Continue?" 
    
    C. Upon confirmation, the System shall immediately delete all user data from the local device and send a deletion request to the server. 
    
    D. The server shall complete deletion within seven days, and the user shall receive an email confirmation if an email address was provided.

7. For anonymised research use, the System shall obtain separate explicit opt‑in consent on a distinct screen during onboarding. 

    A. The opt‑in screen shall state: "Allow Odin to use your anonymised data to improve financial models for all users? Your data will be stripped of all identifiers, amounts will be rounded, and dates will be truncated to month. This does not identify you personally. You may opt out at any time in Settings." 
    
    B. Users who do not opt in shall have their data permanently deleted after the retention period rather than anonymised. 
    
    C. Users who opt in may later withdraw consent via Settings → Privacy → Remove from Research, and their data shall be excluded from future research datasets.

### Section 2. Technical Security Controls.

1. The System shall implement the following technical security controls. 

    A. For in‑transit encryption, all communications between the mobile application and the server shall use TLS version 1.3 minimum, following NIST SP 800‑52 guidelines. 
    
    B. For at‑rest encryption on the server, stored transaction data shall be encrypted using AES‑256‑GCM, compliant with FIPS 197. 
    
    C. The encryption keys shall be managed using a key management service and shall not be stored in source code.

2. For local storage on the mobile device, the System shall use an encrypted SQLite database via SQLCipher with a 256‑bit key derived from the user's six‑digit PIN or biometric authentication. 

    A. The key is derived using PBKDF2 with 100,000 iterations. The PIN is stored only as a salted hash; the biometric authentication invokes the device's secure hardware.

3. For authentication, the user shall set a six‑digit PIN during onboarding. 

    A. If the device supports biometric authentication (FaceID, TouchID, or Android Biometric), the user may enable biometric login as an alternative to the PIN. 
    
    B. The PIN is required as a fallback. 
    
    C. The System shall lock after five failed authentication attempts and require a thirty‑second cooldown.

4. For anonymisation before server upload, the System shall pseudonymise user data, not fully anonymise it, because the server must be able to associate subsequent uploads from the same user to maintain a coherent transaction history. 

    A. The user identifier sent to the server shall be a salted hash: SHA‑256 of the user's local unique identifier concatenated with a per‑device salt that is stored only on the device. 
    
    B. This produces a deterministic but non‑reversible identifier. 
    
    C. The server cannot reverse the hash to obtain the original user identifier, and without the device‑local salt, the hash cannot be recomputed from other data. 
    
    D. This scheme achieves pseudonymisation as defined under the Data Privacy Act. 
    
    E. For true anonymisation after account deletion or retention expiry, the server shall delete the mapping entirely.

> [OPEN: Team Decision] The pseudonymisation scheme described above is sufficient for the thesis scope because no real user data is used for training global models. If the System were to be deployed commercially, a more robust anonymisation scheme with differential privacy would be required. The team should document this as a limitation.

### Section 3. AI/ML Model Privacy.

1. No user transaction data shall be used to train or fine‑tune any global machine learning model during the thesis study. 

    A. This includes the Random Forest classifier, the LSTM forecasting model, and the Isolation Forest anomaly detector. 
    
2. All models shall be pre‑trained exclusively on synthetic data generated from public surveys (BSP CFS 2021 and PSA FIES). 

3. The models shall be frozen before any user data is collected. 

    A. This design ensures that no personal financial information influences the model weights.

4. Inference requests sent from the mobile application to the server shall contain only the minimal feature vector required for each prediction. 

    A. For the Random Forest, the feature vector includes the user's aggregated statistics (income CV, obligation ratio, etc.) but no raw transaction details. 
    
    B. For the LSTM, the feature vector includes the last sixty days of daily aggregated spending per broad group, calendar features, and the user's profile, but no merchant names, descriptions, or detailed category information beyond the four broad groups. 
    
    C. For the Isolation Forest, the feature vector includes the transaction amount, category, day‑of‑period proportion, and merchant novelty flag, but not the merchant name string itself. 
    
    D. The server shall not persist any feature vectors beyond the request lifetime; logs shall be disabled for inference requests.

5. For future deployment beyond the thesis, if the researchers ever consider using real user data for model improvement, the following conditions shall apply. 

    A. Explicit opt‑in consent separate from the general Terms of Service shall be required. 
    
    B. Data shall be aggregated to satisfy k‑anonymity with k ≥ 20 before any model weight update. 
    
        i. That is, any batch of data used for training shall contain at least twenty users who cannot be distinguished from each other on the set of quasi‑identifiers (income quintile, profile, age bracket, city). 
        
        ii. This is a strong requirement that may be infeasible for a small user base. 
        
        iii. For the thesis, because no real user data is used for training, the k‑anonymity condition is not evaluated. 
        
> [FUTURE WORK] A production deployment would need to either maintain a large user base or forgo personalised fine‑tuning.

6. Users shall have the right to request removal of their data from any training corpus. 

    A. A Settings → Privacy → Remove from Training option shall be provided. 
    
    B. Upon selection, the user's data shall be excluded from any future training batches. 
    
    C. This applies to future versions only.
    
        i. For the thesis, there is no training corpus to remove from.

### Section 4. Ethical Review and Disclaimers.

1. The System shall display the following disclaimer on first launch. 

    A. The disclaimer shall be shown in a modal dialog that the user must scroll to the bottom and tap "I understand" before proceeding to the main application: "Odin's predictions and recommendations are for informational purposes only. You retain full responsibility for all financial decisions. Odin is not a financial advisor. Do not make major financial decisions solely based on automated outputs."

2. Institutional ethics clearance shall be obtained from the University of Makati Research Ethics Committee prior to any user data collection for the study. 

    A. The ethics application shall include the informed consent form (in English and Tagalog), the data privacy notice, the onboarding questionnaire, the SUS questionnaire, and a description of the synthetic data generation and model training procedures. 
    
    B. The researchers shall start the ethics application process early, as review may take several weeks. 
    
    C. The timeline in Article V of the Paper Specification allocates three weeks for user evaluation, which may be insufficient if ethics clearance is not obtained in advance.

3. The informed consent form shall include, at minimum, the following elements: 

    A. A description of the study purpose.
    
    B. description of procedures (fourteen days of system use, transaction entry, completing a questionnaire).
    
    C. A statement that participation is voluntary and may be withdrawn at any time without penalty.
    
    D. A description of risks (none beyond those of ordinary app use) and benefits (improved financial awareness).
    
    E. A statement about data privacy and retention.
    
    F. Contact information for the researchers and the ethics committee.
    
    G. Signature lines for the participant and the researcher. 
    
4. A copy shall be provided to the participant.

### Section 5. Connection to Other Modules

1. The privacy and security controls described in this article are implemented at the infrastructure and application layers. 

2. They affect how data flows between modules.

    A. For example, the pseudonymised user identifier is used by the server to retrieve the correct stored data for each user, but the server never sees the raw user identifier. 
    
3. The encryption requirements apply to the local storage used by all modules (transactions, budgets, goals, debts). 

4. The consent and deletion mechanisms affect the data lifecycle for all user data collected by any module. 

5. No machine learning module has special access beyond the feature vectors described in Section 3.

---

## Article XV: Scope and Delimitations (Exclusions)

1. The following features and capabilities are explicitly excluded from the System for the thesis version, with the reasons for exclusion stated for each.

    A. Bank or e‑wallet API integration is excluded. 
    
        i. Application programming interface registration fees for Philippine financial institutions such as GCash and Maya require formal partnership agreements with undisclosed fees and legal review. 
        
        ii. Compliance with Bangko Sentral ng Pilipinas circulars on data sharing adds complexity beyond the thesis scope. 
        
        iii. Furthermore, manual transaction entry is a deliberate design choice supported by literature indicating that manual logging increases financial mindfulness. 
        
        iv. This exclusion is noted as a limitation, and API integration is recommended for future work.

    B. Optical character recognition of receipts is excluded. 
    
        i. The ability to photograph a receipt and automatically extract transaction details would reduce user friction but introduces computer vision complexity and accuracy requirements that are not central to the personal finance management objectives of the thesis.

    C. Investment tracking for stocks, mutual funds, cryptocurrency, or any asset with variable returns is excluded. 
    
        i. These instruments require different modelling assumptions, including price volatility and market data integration, which are outside the defined scope of a personal finance management system for young adults focused on budgeting, saving, and debt management.

    D. Multi‑currency support is excluded. 
    
        i. The System operates exclusively in Philippine pesos. 
        
        ii. All amounts are stored as integer centavos of PHP. 
        
        iii. Foreign currency transactions, if any, must be manually converted by the user at the time of entry.

    E. Non‑Filipino users are excluded. 
    
        i. The System is designed for the Filipino cultural and financial context, including local spending patterns, holidays, and financial products. 
        
        ii. Geographic scope is limited to individuals who live or work in Metro Manila, as defined in Article I Section 2.

    F. Users outside Metro Manila are excluded from the evaluation, though the application may function for them. 
    
        i. The validation study recruits participants only from Metro Manila cities, consistent with the geographic delimitation.

    G. Automated bill payment is excluded. 
    
        i. The System does not initiate payments to creditors, utilities, or any third party. 
        
        ii. All payments are manually recorded by the user. 
        
        iii. This exclusion is due to security and regulatory complexity, including requirements for payment system operator licences.

    H. Credit score monitoring is excluded. 
    
        i. Accessing credit scores in the Philippines requires third‑party API integration with recurring fees and compliance with the Credit Information Corporation regulations, which is outside the thesis budget and timeline.

    I. Tax computation is excluded. 
    
        i. Tax preparation requires professional certification and knowledge of each user's specific deductions, dependents, and filing status. 
        
        ii. The System does not provide tax advice.

    J. Paluwagan, the informal rotating savings and credit association practised in the Philippines, is excluded as a dedicated module. 
    
        i. Users may create a custom subcategory under the Financial Allocation broad group named "Paluwagan" and manually record contributions as expenses and payouts as negative expenses or transfers. 
        
        ii. However, this treatment distorts spending patterns because receiving the pot appears as a negative expense rather than a cash inflow. 
        
        iii. The researchers acknowledge this as a limitation. 
        
        iv. A dedicated module that tracks contributions and payouts without affecting the main budget is recommended for future work.

    K. CSV or spreadsheet import is excluded. 
    
        i. The System does not accept batch uploads of transactions from bank‑exported files or manually created spreadsheets. 
        
        ii. All transactions must be entered manually. 
        
> [FUTURE WORK] CSV import may be added in a future version to reduce data entry friction while preserving user control.

2. Optical character recognition of receipts and CSV import are both excluded for the same reason: the thesis focuses on the machine learning models and budget recommendation engine, not on data ingestion automation. 

    A. The researchers explicitly delimit these features to maintain scope.

3. All exclusions listed in this article are permanent for the thesis version. 

    A. They may be reconsidered for future versions of the System beyond the academic requirement.

---

## Article XVI: Definitions of Terms (Operational)

1. For the purpose of this specification, the following terms have the meanings assigned.

    A. Available balance is the sum of a specific account's starting balance plus all income transactions minus all expense transactions minus all savings contributions minus all debt payments, as defined in Article V Section 2. 
    
        i. Available balance may become negative, in which case the System displays a persistent warning badge. 
        
        ii. This definition corrects any prior contradictory statements that disallowed negative balances.

    B. Behavioural drift (concept drift) refers to a statistically significant change in any classification feature over a sixty‑day sliding window, detected by a Mann‑Whitney U test with a significance level of p < 0.05. 
    
        i. The two windows compared are non‑overlapping, for example days one through sixty compared with days sixty‑one through one hundred twenty.

    C. Budget feasibility is a binary property indicating whether a set of budget allocations satisfies all hard constraints defined in Article VI Section 4, including debt minimum payments, savings minimum, and group floors and caps. 
    
        i. A budget that violates any hard constraint is infeasible.

    D. Budget infeasibility is the condition in which no allocation satisfies all hard constraints simultaneously. 
    
        i. The System handles infeasibility through sequential relaxation as described in Article VI Section 4, culminating in a message recommending debt restructuring or income increase if even the relaxed constraints cannot be satisfied.

    E. Budget period is the time horizon over which a budget applies, measured in days. 
    
        i. The System supports periods of seven, fourteen, thirty, and ninety days. 
        
        ii. The recommended period depends on the user's financial behavioural profile.

    F. Coefficient of variation (CV) is the standard deviation of monthly net income divided by the mean monthly net income, used to classify income stability. 
    
        i. A CV below 0.25 indicates Stable income; a CV of 0.25 or above indicates Variable income. 
        
        ii. This threshold is provisional and requires validation from research.

    G. Cold‑start period is subdivided into three phases. 
    
        i. Profile cold‑start lasts for the first seven days of transaction history or until the user has at least five income transactions, whichever is longer; during this phase, classification uses the onboarding questionnaire. 
        
        ii. Forecasting cold‑start lasts for the first thirty days of transaction history; during this phase, forecasts use population fallbacks from FIES and BSP surveys. 
        
        iii. Anomaly detection cold‑start lasts for the first fourteen days of transaction history; during this phase, Isolation Forest is disabled and only rule‑based overspending alerts are shown.

    H. Debt hardship is a condition automatically detected when the user's available balance is less than the sum of all minimum monthly payments for debts due in the current month. 
    
        i. Upon detection, the System displays a hardship screen with creditor contact information and a recommendation to seek counselling.

    I. Expense category is a classification label assigned to a financial transaction, grounded in the 2020 Philippine Classification of Individual Consumption According to Purpose. 
    
        i. The System uses thirteen base categories with subcategories, as listed in Article IV Section 1.

    J. Financial behavioural profile (FBP) is a classification of a user based on income stability (Stable or Variable) and obligation level (Flexible or Obligated). 
    
        i. The four profiles are Stable‑Flexible, Stable‑Obligated, Variable‑Flexible, and Variable‑Obligated.

    K. Forecast bias is a metric calculated as the mean of (forecast minus actual) divided by the mean of actual, expressed as a decimal. 
    
        i. An acceptable range is between negative 0.10 and positive 0.10, indicating no systematic over‑forecasting or under‑forecasting.

    L. Improvement over Fallback (IoF) is a metric calculated as the Mean Absolute Error of the fallback model minus the MAE of the LSTM model, divided by the MAE of the fallback model, expressed as a percentage. 
    
        i. A positive value indicates that the LSTM outperforms the fallback.

    M. Isolation Forest is an unsupervised anomaly detection algorithm that isolates anomalies by randomly partitioning feature space. 
    
        i. The System uses a per‑user Isolation Forest with one hundred estimators and a dynamic anomaly threshold based on the top five percent of anomaly scores.

    N. Linear Programming (LP) is a mathematical optimisation method used to allocate budget amounts across categories subject to constraints, maximising a weighted sum of category allocations where the weights are user‑defined priorities.

    O. LSTM (Long Short‑Term Memory) is a type of recurrent neural network suited to learning from sequential time‑series data. 
    
        i. The System uses a two‑layer LSTM with input sequence length of sixty days to forecast daily spending across four broad groups.

    P. Obligation ratio is the sum of unavoidable monthly expenses divided by total monthly income, averaged over the preceding sixty days. 
    
        i. A ratio below 0.50 indicates Flexible; a ratio of 0.50 or above indicates Obligated. 
        
        ii. This threshold is provisional and requires validation from research.

    Q. Paluwagan is an informal rotating savings and credit association practised in the Philippines. 
    
        i. The System does not include a dedicated module for paluwagan. 
        
        ii. Users may approximate it via a custom subcategory under Financial Allocation, but this treatment is acknowledged as a limitation. 
        
        iii. A dedicated tracker is recommended as future work.

    R. Personal finance management system (PFMS) is a software system designed to help individuals track, plan, and manage personal income, expenses, savings, and debt. 
    
        i. Odin is one such system.

    S. Pseudonymisation is the processing of personal data such that the data can no longer be attributed to a specific data subject without the use of additional information, which is kept separately and subject to technical and organisational measures. 
    
        i. The System implements pseudonymisation for server uploads using a salted hash of the user identifier, with the salt stored only on the device.

    T. Random Forest is an ensemble machine learning algorithm that constructs multiple decision trees and aggregates their outputs for classification. 
    
        i. The System uses Random Forest for financial behavioural profile classification.

    U. sMAPE (symmetric Mean Absolute Percentage Error) is a forecasting accuracy metric calculated as the average of the absolute difference divided by the average of the forecast and actual values, expressed as a percentage. 
    
        i. It is used for low‑volume categories where MAE may be misleading.

    V. Surplus handling strategies are the three methods by which the System treats unspent budget amounts at the end of a budget period. 
    
        i. Rollover adds the surplus to the next period's total budget. 
        
        ii. Save transfers the surplus to the user's primary savings goal. 
        
        iii. Reset returns the surplus to available balance and recomputes the next period's budget from zero. 
        
        iv. Default strategies are assigned by financial behavioural profile.

    W. Walk‑forward validation is a time‑series model evaluation method in which the model is trained on past data and tested on successive future periods, rolling forward incrementally. 
    
        i. The System uses walk‑forward validation for all machine learning modules on synthetic data.

    X. Whitelist is a user‑maintained list of merchant‑category pairs that are exempt from anomaly detection alerts. 
    
        i. Whitelist entries may include an amount tolerance of plus or minus twenty‑five percent, or may be set to always allow regardless of amount.

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
