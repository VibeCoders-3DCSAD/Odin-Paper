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

Every budget shall consist of:

- Total budget size (in PHP)
- Budget period (time horizon in days: 7, 14, 30, or 90)
- Per-category allocation (PHP amount per category, summing to total budget size)
- Per-category actual spending (tracked from expense transactions)
- Surplus/deficit = allocated − actual (per category and total)

> ASK: (JOAQUIN): Is this an exhaustive list of the properties of a Budget? Also, what is surplus/deficit, and how is it relevant in the system?
> ANS: (): ___

> Claude: Section 1 defines "surplus/deficit = allocated − actual." ASK: Is deficit handled differently from surplus? The spec only discusses surplus handling (Section 5). Deficit (spending more than allocated) should trigger alerts and possibly reduce next period's budget or adjust savings contributions. This is missing.

> ADD: (J): Deficits should trigger the overspending detection submodule, iirc. Regarding the adjustment of the budgets, you raise a good point. I don't think any discussion about budget adjustment after overspending was made. We could probably also consider anomaly detections, and overall behavior. For example, if the user spent only 70% of the allocation for leisure, then reduce the size a bit. Though that also raises the question: what if the user actually needs to spend more for something suddenly? We need to allow a mechanism not just for downsizing allocations, but upsizing. It should also not conflict with the anomaly detection if possible. What do you guys think?

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

> Claude: Section 2 recommends budget periods based on profile. NOTE: Variable-Obligated users are recommended 14-day periods, but their obligations (rent, utilities, debt payments) are typically monthly. A 14-day budget may not align with bill due dates. PROP: For Obligated profiles, always recommend 30-day periods regardless of income stability, because obligations follow monthly cycles. Variable-Flexible can use 14 days.

> ADD: (J): We have to be careful with these parameters. I suggest just validating these decisions with research.

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

> Claude: Section 3 templates: "Zero-based" is described as "Income − Expenses = 0." The ASK correctly notes that all budgets sum to total budget. The distinguishing feature of zero-based budgeting is that every peso is assigned to a specific category (no unassigned "buffer"). Rename to "Zero-based (every peso assigned)" or "Detailed allocation" to avoid confusion.

> Claude: Section 3 templates: "Pay-yourself-first" - The ASK asks if this is called reverse budgeting. Yes. Recommend using the more common term "Reverse budgeting" or "Savings-first" in the UI.

> ADD: (J): Just remember that we're primarily Philippines-based.

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

> Claude: Section 4 LP constraints: The explanation of equation (1) is unclear: sum(allocation[category]) = forecast_income × (1 − savings_rate_target). NOTE: This implies that the total budget is income minus savings. But savings are also a category (allocation[SAVINGS]). ASK: Is SAVINGS included in the sum on the left? If yes, then the equation becomes: (spending categories + savings) = income × (1 - savings_rate_target). That is circular because savings_rate_target determines savings allocation. Clarify: The total amount available for spending (excluding savings) is income minus target savings. Savings is then allocated separately, possibly exceeding the target. Rewrite constraints to avoid this confusion.

> Claude: Section 4: max_spending_per_category is derived from 90th percentile of historical spending. ASK: What about new categories with no history? The fallback is "50% of total budget" - that seems extremely high. A single category could consume half the budget. PROP: Use 30% as fallback, or derive from population averages (FIES) for that category.

### Section 5. Surplus Handling.

At the end of a budget period, surplus (allocated but unspent amount) shall be handled per user selection from three strategies (benchmarked from RRL on reset vs. carryforward logic):

> NOTE: Correct me (Joaquin) if I'm wrong, but surplus handling is a new concept in Odin. We'll have to back this up with research as usual.

1. **Rollover**
    - Rule: Surplus added to next period's total budget
    - Default: Stable profiles
1. **Save**
    - Rule: Surplus automatically transferred to primary savings goal
    - Default: Variable profiles
1. **Reset**
    - Rule: Surplus returned to available balance, next period budget recomputed from zero
    - Default: None (user must select)

The System shall display the end-of-period surplus with the prompt: "You underspent by PHP[X]. What would you like to do with the leftover amount?" with the three options. If user does not respond within 7 days, default strategy per profile applies.

> NOTE: Ensure that these are verified and validated with research as actual surplus handling strategies.

Under Rollover strategy, the surplus amount is added to the next period's total budget. Category allocations for the next period shall be recomputed using the LP with the increased total budget, preserving the same allocation ratios (or applying updated user priorities). The surplus is not tied to specific categories.

> GLOBAL: These enumerations should have their own heading or subsection, to include prose-style descriptions instead of relying on outlines and bullet-points.

> Claude: Section 5: Under Rollover, "surplus is not tied to specific categories." ASK: What about category-specific surpluses? For example, if a user underspends on Food by 500 but overspends on Transport by 300, the net surplus is 200. If rolled over, should the 200 be added to total budget without adjusting category allocations? That could perpetuate the overspending in Transport. PROP: Implement category-level rollover: each category's surplus/deficit carries forward to the same category in the next period, with total budget adjusted accordingly. This is more complex but more accurate to user behavior.

> Claude: Section 6 explainability example mentions "minimum savings" but the LP uses savings_rate_target which is a percentage, not a fixed amount. The example should show both: "minimum savings of PHP[X] (10% of your income)."

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

> Claude: Section 1 Forecasting Targets: Savings balance trajectory and debt remaining balance are listed. ASK: How does the system forecast savings balance without knowing the user's future contributions? Contributions are discretionary (except for automated savings goals). The spec should clarify: savings trajectory forecast assumes the user follows the current budget recommendation (including savings contributions) and does not make unplanned withdrawals. This assumption should be stated in the explainability.

> ADD: (J): I would argue that this is sorta implied already. The forecasting module should inform the user that Forecasts are inferential and informational only, and may not represent actual trends.

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

> Claude: Section 2 LSTM specifications: "Input sequence length: 60 days" - ASK: For users with less than 60 days of history, does the model pad with zeros or use fallback? The cold-start fallback (Section 3) applies for <30 days, but between 30-60 days, the model would have insufficient sequence length. PROP: Use the available data (e.g., 30-59 days) as input, and set missing days to 0 or repeat the earliest value. Document this.

> ASK: (J): Is this just a natural limit of LSTM? How can we get evaluations for the forecasting module if the evaluators have to wait 60 days for a forecast?

> Claude: Section 2: "global LSTM model pre-trained on synthetic data (BSP/PSA)." ASK: BSP CFS and PSA FIES are survey data, not time-series transaction data. They provide aggregates (e.g., average monthly spending per category), not daily sequences. How will synthetic daily transactions be generated from these aggregates? This is a critical methodological gap. The document references model-training-data-design.md - that file must specify the synthetic data generation process in detail (e.g., using statistical models or generative AI).

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

> Claude: Section 3 Cold-start fallback: "FIES 2018 category means" - NOTE: FIES 2018 is now outdated (6+ years old). Inflation and spending patterns have changed significantly, especially post-pandemic. PROP: Use FIES 2023 when released, or adjust 2018 means by cumulative inflation (PSA inflation data) as a temporary measure.

> ADD: (J): Yeah, why are we using FIES 2018? We can use the PSA FIES 2023 or a later version if found.

### Section 4. Explainability.

Explainability for LSTM forecasts shall use temporal attention weights (extracted from a trained attention layer added to the LSTM) or feature perturbation (measure prediction change when each input feature is shuffled). SHAP shall NOT be used for LSTM due to computational constraints. The simpler method: "Your [CATEGORY] spending is predicted to increase because your spending in the last 7 days is [X] higher than your 30-day average."

> Claude: Section 4 Explainability: "temporal attention weights" - ASK: The LSTM architecture specified does not include an attention layer. Adding attention changes the model architecture. Is attention part of the design? If not, use feature perturbation as the primary method. The simpler method described ("your spending in the last 7 days is X higher") does not require attention; it can be computed directly from data.

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

> Claude: Section 5 Evaluation Metrics: MAE threshold "<15% of category mean" - ASK: For low-spending categories (e.g., EDUCATION where many users spend 0), 15% of mean may be a very small absolute number. A small absolute error could still be a large relative error. Consider using different metrics for sparse categories (e.g., sMAPE is already specified for this purpose). Clarify that MAE and RMSE are for high-volume categories only.

> ADD: (J): It would be excellent if, globally, the purpose of all metrics are described. 

> Claude: Section 5: "Action if exceeded for 3 weeks" - ASK: Why 3 weeks? This is a heuristic. PROP: Justify with concept drift literature: financial behavior typically changes slowly, so 3 weeks of degraded performance indicates a real shift or model issue, not noise.

> ADD: (J): Good catch. All heuristics must be detected and should be validated.

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

> Claude: Section 1: "Isolation Forest with contamination rate 0.05" - ASK: Is contamination rate fixed or adaptive? A fixed 0.05 means exactly 5% of transactions are flagged as anomalies regardless of actual behavior. This is problematic for users with very regular spending (should flag <1%) or very irregular spending (should flag >5%). PROP: Use adaptive contamination based on historical user behavior, or remove the fixed contamination parameter and use isolation forest's raw anomaly scores with a dynamic threshold (e.g., top 5% of scores, not exactly 5% of transactions).

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

### Section 3. Excluded Events (Culturally Expected Spending Spikes).

The following transactions shall NOT be flagged as anomalies regardless of Isolation Forest score, based on RRL on Filipino cultural spending patterns:

- Transactions between December 15 and January 5 (Christmas and New Year)
- Transactions during Holy Week (exact dates vary yearly; the System shall use a manually maintained JSON configuration file)
- Transactions during user's declared home barangay fiesta dates (±3 days, user-configurable in profile)
- Transactions manually whitelisted by user (see Section 4)

> PROP: I think the anomaly detection module should still detect anomalies during these occasions, but, instead of sending out warnings, it could send out information notifs. In this way, the user isn't blindsided by the system, and anomalies hiding in these seasonalities can still be detected.

The System shall maintain a built-in holiday calendar for Metro Manila, pre-loaded with fixed holidays (e.g., Dec 25, Jan 1) and movable holidays (e.g., Holy Week) for the current and next year. The calendar shall be updated annually via a manual configuration file (JSON) that the development team updates based on official PSA proclamations. A fallback rule shall exclude any transaction between March 25 and April 10 if the year's Holy Week dates are not yet loaded.

> PROP: I propose that the system connects to a calendar or holiday API instead.

> Claude: Section 3 Excluded Events: The PROP suggests still detecting anomalies but sending informational notifications instead of warnings. I support this. PROP enhancement: Use a severity scale: Critical (red) for anomalies outside excluded periods; Informational (blue) for anomalies during holidays/fiestas; and allow users to configure whether they want informational alerts.

> Claude: Section 3: "fallback rule shall exclude any transaction between March 25 and April 10 if Holy Week dates not loaded." ASK: March 25 to April 10 is 17 days. Holy Week is typically 7-8 days (Palm Sunday to Easter Sunday). This fallback is overly broad. PROP: Use a narrower fallback, e.g., the week containing Easter (computed via algorithm for the given year, even if holiday calendar not maintained). There are open-source algorithms for computing Easter dates.

> ADD: (J): Again, it would be helpful to utilize a calendar or holiday API.

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

> Claude: Section 4 Whitelist: "all future transactions with same merchant name and within ±25% amount shall be suppressed." ASK: What about the same merchant but different category? Example: User buys groceries (FOOD) at SM Supermarket, then buys electronics (FURNISHINGS) at SM Appliance Store (same merchant name "SM"). Should the second be whitelisted? The current rule would suppress it because merchant name matches. PROP: Whitelist should be per (merchant, category) pair, or require user to confirm category matching.

### Section 5. Supplementary Rule-Based Detection.

In addition to Isolation Forest, the System shall implement rule-based budget overspending detection:

- Alert if a category exceeds 80% of its budget with >25% of period remaining
- Alert if any category exceeds 100% of its budget at any time

These rule-based alerts shall NOT be suppressed by whitelist or cultural exclusions.

> NOTE: This feature should be named "Overspending Detection". It is not supplementary, it is a whole module (or submodule). It just doesn't implement any intelligent features, so it's sort of similar to the Goals Management and Debt Management modules.

> Claude: Section 6 Alert Fatigue Prevention: The PROP suggests removing sensitivity adjustment for users. I partially agree: keep sensitivity as an advanced setting hidden behind an "Advanced" expander, not in main settings. Grouping and cooldown are sufficient for most users.

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

> Claude: Section 8 Evaluation Metrics: FPR target "≤ 1.5" - ASK: 1.5 what? False positives per user per week? The description says "FP / active days × 7" - so it's a weekly rate. 1.5 false positives per week is reasonable. However, note that with contamination=0.05, a user with 100 transactions per week would have 5 flagged anomalies. If only 3.5 of those are true positives (recall 0.70), then false positives would be 1.5. The target is mathematically consistent with precision≥0.70 and recall≥0.65. Good.

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

> Claude: Section 1 Goal Definition: The NOTE suggests that "Goal" is broader than "Savings Goal" and includes funds, insurance deposits, etc. However, the fields defined (target amount, contribution amount, contribution frequency) do not fit insurance (which has premiums, not contributions to a target) or investments (which have variable returns). PROP: Keep "Savings Goal" as is. For future work, create separate modules for Insurance and Investment tracking. Do not overload the Goal concept.

> Claude: Section 1: "Linked source: Available balance (default) or specific income category." ASK: What does linking to a specific income category mean? Example: User wants to save 100% of freelance income for a goal. How is this enforced technically? Does the system automatically create a transaction from that income to savings? This needs more detail.

### Section 2. Multiple Concurrent Goals.

The System shall support up to 5 concurrent savings goals. Users shall prioritize goals via drag-and-drop in the UI. The System shall apply contributions in priority order: when available balance is sufficient, it shall contribute to goal 1 first, then goal 2, etc., until all scheduled contributions are satisfied or balance is exhausted.

> ASK: (JOAQUIN): Why only 5? And are the applied contributions sourced from the Budget as Financial Services or some other category?
> ANS: (): ___

> Claude: Section 2: "up to 5 concurrent savings goals." ASK: Why 5? Similar to accounts limit. If the limit is due to UI complexity, consider making it configurable with a warning beyond 5 (e.g., "Too many goals may reduce contribution effectiveness").

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

> Claude: Section 3 Progress State Calculation: The formula uses required_contribution = remaining_amount / contribution_frequency. But contribution_frequency is defined as days? The code shows days_remaining / contribution_frequency_days. ASK: Is contribution_frequency the number of remaining contributions, or the frequency in days? The variable naming is inconsistent. Rewrite the pseudo-code with clear names: remaining_contributions = days_remaining / frequency_days (rounded up). Then required_contribution = remaining_amount / remaining_contributions.

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

> Claude: Section 4 Savings Contribution Strategies: "Snowball (smallest balance first)" - ASK: In savings, "smallest balance" means the goal with the least accumulated savings so far, not the smallest target amount. This prioritizes nearly-empty goals. Is that intentional? The classic debt snowball prioritizes smallest outstanding balance (debt amount), which in savings would be smallest remaining amount (target - current), not smallest current balance. Clarify.

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

> Claude: Section 5 Notifications: "Behind schedule" triggers after 7 consecutive days of "behind" state. ASK: What if the user is "behind" but has no control (e.g., unexpected expense)? The notification should include an action: "Adjust contribution amount or postpone goal target date?"

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

> Claude: Section 1: "Interest rate (annual) 0% to 100%" - ASK: What about loans with compound interest (e.g., credit cards)? The simple annual interest model does not capture compounding. Credit card interest is typically daily or monthly compounding. PROP: Add a compounding frequency field (none, monthly, daily) and compute effective annual rate accordingly. Or limit to simple-interest loans (personal loans, salary loans) as scope, explicitly excluding credit card debt.

> Claude: Section 1: "Payment due day of month: 1-28." ASK: What about due dates on 29th, 30th, 31st? Some loans have those dates. For February, if due date is 30th, the system needs a rule (e.g., last day of February). PROP: Allow 1-31, with validation for month lengths (e.g., if due day > month length, use last day).

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

> Claude: Section 2 Payoff Strategies: The ASK asks whether Goal Management has the same switching process. It does not appear to. PROP: Add similar "before/after comparison" to Goal Management when switching contribution strategies, for consistency.

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

> Claude: Section 4 Minimum Payment Validation: "hardship mode" - ASK: Is hardship mode a user-declared state or automatically detected? The spec says "if available balance is less than sum of all minimum payments" - that is automatic detection. PROP: When detected, the system should also offer to reschedule payments (e.g., propose a reduced payment plan to the user, not automatically to creditors). The user can then decide which debts to underpay.

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

> Claude: Section 1: "Forecast-based advisory: 'Your current spending suggests you may exceed budget by [AMOUNT]'" - ASK: When is this triggered? At what threshold? For example, if the forecast shows exceeding budget by >10% with >50% of period remaining. Define the triggering rule.

### Section 2. Delivery Method.

All alerts shall be delivered as:

- In-app notification (bell icon badge, displayed in notification center)
- Push notification (if user grants permission, with user-configurable opt-out per category)
- Optional email digest (weekly summary of all alerts, user opt-in)

> PROP: Do in-app and push notifs. only. We may not be able to do mailers, I think. Or maybe we can.

> Claude: Section 2 Delivery Method: The PROP suggests no email digest. I agree for the thesis scope, but note that the evaluation (SUS) may include questions about notification preferences. Document that email is out of scope.

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

> Claude: Section 4: "budget overspending which is mandatory" - ASK: Can users disable all notifications for a specific category? For example, a user might not care about exceeding a very flexible category like MISC. PROP: Allow per-category notification enable/disable, with overspending alerts still recorded in notification center but not pushed.

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

> Claude: This article is concise but missing evaluation criteria. ASK: How will the researchers evaluate whether explainability outputs are effective? Consider adding: (1) User comprehension test: After seeing an explanation, can the user correctly state why a prediction was made? (2) Trust rating: On a 1-5 scale, does the explanation increase trust in the system? These could be part of the SUS or a separate post-task questionnaire.

> Claude: "Explainability outputs shall be stored in the application log for audit" - ASK: For how long? Log retention should be specified (e.g., 30 days) to comply with data minimization under DPA.

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

> Claude: Section 1: "Functional suitability: ≥98% of specified features passing manual test cases" - ASK: Who defines the test cases? The researchers should produce a test case traceability matrix mapping each requirement (from Articles I-XII) to at least one test case. This is not mentioned in appendices; consider adding as Appendix J.

> Claude: Section 1: "Performance efficiency: ≤500ms for non-ML, ≤3000ms for ML predictions" - ASK: Is 3000ms (3 seconds) acceptable for a mobile app? Users may perceive 3 seconds as slow. Consider a lower target (≤1500ms) for ML predictions, with a loading indicator. 3 seconds could be the maximum acceptable (p99), not p95.

> Claude: Section 1: "Cyclomatic complexity ≤10" - The NOTE says ML training scripts and LP solvers are exempt. ASK: What about the code that prepares inputs for ML models (feature extraction from transactions)? That is business logic and should be included. Clarify exemption only for third-party library code, not for wrapper functions that transform data.

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

> Claude: Section 2 SUS Protocol: "Target n=30" - The ASK notes minimum total of 50 evaluators. PROP: 30 is acceptable for a thesis (standard for SUS studies), but the stratification (6 per profile) sums to 24, not 30. The extra 6 can be unstratified. Ensure recruitment over-recruits to hit each stratum's minimum.

> Claude: Section 2: "SUS shall be administered after 14 days of active system use (minimum 10 transaction entries)." ASK: What if a user does not reach 10 transactions in 14 days? They may be a low-activity user, but their SUS score is still valuable (reflects real-world usage). PROP: Administer after 14 days regardless of transaction count, but record transaction count as a covariate in analysis.

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

> Claude: Section 3: Algorithmic Module Evaluation Protocol - The ASK asks about budget recommendation evaluation. PROP: Budget recommendation can be evaluated by adherence rate: percentage of users whose actual spending stays within ±20% of recommended category allocations over the budget period. Target ≥70%. Also measure user modification rate (how often users manually adjust recommendations) as a proxy for recommendation quality.

> Claude: Section 3: "Walk-forward validation shall be performed on synthetic data only" - This is a strong limitation. ASK: After the pilot with real users (up to 30 days per user), can the researchers do a post-hoc evaluation using real data? For example, train on days 1-20, test on days 21-30 (10 days). This would be a weaker validation (small window) but still valuable to compare synthetic vs real performance. Recommend adding this as an exploratory analysis.

### Section 4. Failure Conditions and System Responses.

| Condition | Detection | System Response | User notification |
|-----------|-----------|-----------------|-------------------|
| Forecast MAE > 20% for 14 days | Daily cron job | Log warning; continue current model; flag for retraining | None (developer notified) |
| Anomaly detection F1 < 0.6 for 7 days | Weekly evaluation | Disable Isolation Forest; revert to rule-based only | "Spending alerts are temporarily simplified. Your data is safe." |
| Classification accuracy < 0.80 on validation set | After each retraining | Do not deploy; retain previous model; alert developer | None |
| Any module throws unhandled exception | Runtime error handler | Graceful degradation: disable module; serve fallback | "[Module] is temporarily unavailable. Please try again later." |

> Claude: Section 4 Failure Conditions: "Forecast MAE > 20% for 14 days" - ASK: 20% of what? MAE is an absolute value, not a percentage. Should be "MAE > 20% of category mean" (consistent with earlier threshold). Also, what about categories with zero mean? Use sMAPE for those.

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

> Claude: Section 1: "Retention period: 13 months from last user activity." ASK: Why 13 months? This is unusual. Standard retention for financial data in other PFM apps is often 3-7 years or indefinite. The DPA allows retention as long as necessary for the purpose. If the purpose is to train ML models, 13 months may be insufficient to capture annual cycles (e.g., Christmas spending). PROP: Justify 13 months (13 = 12 months + 1 month grace for user to return) or extend to 24 months.

> Claude: Section 1: "Anonymized research use" requires separate opt-in. This is good. However, ASK: What constitutes "anonymized" under DPA? The spec uses salting and hashing (Section 2). Salt stored only on device means the server cannot re-identify. That is strong. But the spec also says "dates truncated to month" - ASK: Can a sequence of monthly transactions with rounded amounts still be linked to an individual via unique patterns (e.g., exact rent amount on 1st of each month)? Consider adding noise (differential privacy) if true anonymization is required.

### Section 2. Technical Security Controls.

| Control | Implementation | Standard |
|---------|----------------|----------|
| In-transit encryption | TLS 1.3 minimum for all server communications | NIST SP 800-52 |
| At-rest encryption (server) | AES-256-GCM for stored transaction data | FIPS 197 |
| Local storage (mobile) | Encrypted SQLite (SQLCipher) with 256-bit key derived from user PIN/biometric | SQLCipher 4.x |
| Authentication | Biometric (FaceID/TouchID/Android Biometric) + 6-digit PIN fallback | OWASP MASVS |
| Anonymization before server upload | User ID replaced with salted hash (SHA-256 with per-user salt stored only on device); no name/email sent | NIST SP 800-185 |

> Claude: Section 2: "Anonymization before server upload: User ID replaced with salted hash (SHA-256 with per-user salt stored only on device)" - ASK: How does the server match a user's subsequent uploads if the salt is only on the device? The device must send the same hash each time. That means the hash is deterministic and can be used as a persistent identifier. This is pseudonymization, not anonymization. For true anonymization, the salt should be rotated periodically or the server should not be able to link uploads from the same user. Clarify which level is actually needed.

### Section 3. AI/ML Model Privacy.

No user transaction data shall be used to train global models without:

- Explicit opt-in consent separate from general Terms of Service (checkbox: "Allow anonymized data to improve Odin for everyone")
- Aggregation satisfying k-anonymity with k ≥ 20 before any model weight update
- Option to delete user's data from training corpus via Settings → Privacy → Remove from Training

Inference requests shall send only anonymized feature vectors (no raw transactions). The LSTM model shall run on a serverless function; no user data is persisted on the inference server beyond the request lifetime.

> Claude: Section 3: "aggregation satisfying k-anonymity with k ≥ 20 before any model weight update" - ASK: k-anonymity on what attributes? On transaction-level data? Or on feature vectors? This is a strong requirement that may be infeasible for a small user base (<20 users per profile). Consider: For the thesis, there may be no real user data used for training at all (as stated in Article III Section 5 of the PAPER SPECIFICATION). If that's the case, this section is only for future deployment, not for the thesis evaluation.

### Section 4. Ethical Review and Disclaimers.

The System shall display the following disclaimer on first launch and annually thereafter:

> NOTE: Should just be one-time.

"Odin's predictions and recommendations are for informational purposes only. You retain full responsibility for all financial decisions. Odin is not a financial advisor. Do not make major financial decisions solely based on automated outputs."

> This disclaimer must be prominent and displayed somewhere at the start, like in onboarding.

Institutional ethics clearance shall be obtained from the University of Makati Research Ethics Committee prior to any user data collection for research purposes.

> Claude: Section 4: "institutional ethics clearance shall be obtained from the University of Makati Research Ethics Committee" - This is mandatory. ASK: Has the application been submitted? Ethics clearance can take weeks to months. Start early. The timeline (Article V of PAPER SPEC) allocates 3 weeks for user evaluation, which likely includes ethics clearance. That may be insufficient.

> ANS: (J): Submission of applications are after the first semester of 4th year I believe, after Thesis 1. Basically, it's a long time before we need to submit. We need to accomplish Chapters 1-3 first.

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

> Claude: "Paluwagan ... users may create a custom subcategory under SAVINGS named 'Paluwagan'." ASK: Paluwagan has a unique mechanism: members contribute periodically, and one member receives the entire pot each cycle. This is not a savings goal (target amount with contributions) nor an expense. A custom subcategory under SAVINGS would treat contributions as savings (correct) but receiving the pot as a negative expense? That would distort spending patterns. PROP: Either (a) exclude paluwagan completely with a clear note that it cannot be modeled correctly, or (b) add a simple dedicated module that tracks contributions and payouts without affecting budgeting. (b) is better for Filipino context.

> ADD: (J): I mean yeah it sucks, but paluwagan really is engraved in Filipino financial culture. Idk if a good percentage of society practices it, but yeah.

> Claude: "Bank or e-wallet API integration is excluded because ... manual entry is a deliberate design choice." This justification is strong. However, ASK: Does the spec consider CSV/Excel import as a semi-automated input method? Many PFM apps allow importing bank statements. This would reduce friction while still requiring user action (downloading and uploading). Consider adding CSV import as a future work item or explicitly excluding it.

> ANS: (J): We'll see if we can include it. We don't want to bloat our scope, so we'll have to deliberate this feature.

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

> Claude: The NOTE says this should be moved higher. I agree. Recommend placing it immediately after Article I (Platform and Target Users) or as an appendix. For readability, keep it here but cross-reference from earlier articles.

> Claude: "Available balance: May not be negative" - This contradicts the NOTE in Article II Section 3. As noted multiple times, resolve this consistently.

> Claude: "Behavioral drift (concept drift): statistically significant change (p < 0.05 by Mann-Whitney U test)" - ASK: Mann-Whitney U test compares two independent samples. For time-series drift, you would compare two windows (e.g., days 1-60 vs days 61-120) as independent samples. That is acceptable but note that overlapping windows violate independence. Specify that windows are non-overlapping.

> Claude: "Cold-start period: Profile cold-start: first 7 days; Forecasting cold-start: first 30 days" - ASK: What about anomaly detection cold-start? Section VIII says "minimum 14 days required" before Isolation Forest is enabled. That should be defined here as a third cold-start period.

> Claude: Missing definitions: Add "Budget Infeasibility" (Article VI Section 4), "Debt Hardship" (Article X Section 4), "Walk-forward validation" (already present, good), "Surplus handling strategies" (Rollover, Save, Reset).

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
