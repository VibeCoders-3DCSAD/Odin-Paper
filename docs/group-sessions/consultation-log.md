# Consultation Log

> Adviser: Dr. Go
> Date: TBD
> Attendees: Gabion, Guevarra, San Jose, Togle2

---

## Resolved Items

### Savings & Debt

1. **Timeline-based priority for savings.** Savings goals are prioritized first by target date/deadline, then by priority level (urgent, high, medium, low). User may override.

2. **Unified budgeting for debt.** A single debt budget envelope is allocated first, then split across debt categories. Visualized via pie chart.

3. **Per-debt strategy selection.** Users may select repayment strategy (avala nche, snowball, custom) per individual debt, not just per category group.

4. **Debt balances displayed as negative.** Confirmed convention.

5. **Missed payments incur consequences.** Interest accrual, increased payment for the next cycle to stay on the user's desired payoff timeline.

6. **Debt-free fallback.** When a user has no remaining debts, the system prompts them to reallocate the freed amount elsewhere, with recommendations based on the priority hierarchy. Example: Debt → Savings.

### Prioritization

7. **Default allocation priority:**
   1. Essentials
   2. Debt (if applicable)
   3. Savings & Investments

8. **Surplus rollover.** Remaining budget surplus is allocated to the next item in the same priority order, not returned to general balance.

9. **New cash flow or increased money availability prioritization (Dr. Go, 2026-07-29).** When the user receives new income, a windfall, or any increase in available money, the System recommends directing it in this order:
   1. **Essentials first** — top up essential categories if underfunded. If essentials are already covered, move to 2.
   2. **Increase debt payments** — accelerate debt repayment to finish them faster. If no active debts, move to 3.
   3. **Savings & Investments** — allocate to the highest-priority savings goal.
   - These are **recommendations only**; the user always retains freedom to choose where the money goes.

### Profile & Questionnaire

9. **Dr. Go recommended using an established questionnaire.** Specific instrument TBD.

10. **Recommended research into business ratios and personal finance ratios.** Contributes to discovery of hidden features for machine learning models.

### FBP → PFP Rename

11. **"Financial Behavioral Profile" renamed to "Personal Financial Profile" (PFP).** Rationale: the profile is not purely behavioral but is accurately personal. Better alignment with the system's purpose as a personal finance management system.

---

## Unresolved / Action Items

### Presets

- [x] Define scope of preset savings configurations (system defaults vs. user templates).
	- **DECIDED (Dr. Go, 2026-07-29):** The top 10 savings are **presets with their own business logic (fields)** — e.g., interest rate, target amount heuristic, contribution frequency. Users may also create **custom savings goals** with their own user-defined fields outside the top 10. Category groups (Article XXX §4 / Article XXXII §2) are superseded by presets.
	- Still need RRL to validate the specific top 10 savings presets for Filipinos.
	- Possible List (strawman):
		- Traditional savings account: Standard bank accounts with easy ATM access and very low interest rates.High-yield savings account: Online accounts offering much higher interest rates to grow your money faster.Certificates of deposit (CDs): Time-deposit accounts that lock your money away for a fixed period in exchange for a guaranteed, higher return.Money market accounts: Hybrid accounts that pay interest and often include check-writing or debit card features.Purpose-Driven Savings TypesEmergency fund: Money saved for unexpected life events, typically kept in a high-yield account for fast access.Short-term savings: Funds set aside for near-future goals like a vacation, gadget, or major purchase.Retirement savings: Long-term accounts (like IRAs) built to support you later in life.
- [x] Define scope of preset debt configurations (preloaded categories, interest-rate fields, minimum-payment formulas).
	- **DECIDED (Dr. Go, 2026-07-29):** The top 10 debts are **presets with their own business logic (fields)** — e.g., interest rate, minimum payment formula, amortization schedule, annual fee. Users may also create **custom debts** with their own user-defined fields outside the top 10.
	- Still need RRL to validate the specific top 10 debt presets for Filipinos.
	- Possible List (strawman):
		- Secured: Tied to physical property or assets (collateral). If you fail to pay, the lender takes the asset. Examples include home mortgages and auto loans.Unsecured: Not backed by collateral. Lenders approve these based on your credit history. Examples include credit cards and signature loans.Revolving vs. Installment DebtRevolving: A flexible credit line with a borrowing limit. You can borrow, repay, and borrow again. Examples include credit cards and lines of credit.Installment: A fixed lump sum paid back in equal monthly amounts over a set period. Examples include personal loans and student loans.Business and Corporate Debt ConfigurationsSenior vs. Subordinated: Senior debt gets paid first if a company goes bankrupt. Subordinated (mezzanine) debt gets paid later and carries higher risk.Convertible Debt: A loan that starts as money owed but can change into company shares later.
- [x] Clarify whether preset savings goals include preset target amounts (e.g., "Emergency Fund → 6 months of expenses") or only category/structure.
	- **DECIDED (Dr. Go, 2026-07-29):** Presets carry their own business logic — target amounts are part of that logic where applicable (e.g., Emergency Fund heuristic), but **users must set/override the actual target values**.

### Prioritization

- [ ] Specify which prioritizations are default-overridable: savings goal hierarchy, debt repayment order, budget allocation order — or all three.
	-  All three are overridable, system gives recommendation not tight constraints.
	-  Hierarchy 
		- Essentials
		- Debts
		- Savings & Investments
- [ ] Define the two-axis hierarchy mechanics: does deadline always sort first, or can priority override deadline with sufficient gap?
	-  Deadline always sort first, but users can override this priority based on what they want

### Ratios → ML Features

- [ ] Identify which specific business ratios apply (current ratio, debt-to-income, savings rate, liquidity ratio, etc.).
- [ ] Identify which personal finance ratios apply (50/30/20, 20% savings rate, 28% housing rule, Filipino-context ratios).
- [ ] Define how ratios become engineered features: as classifier inputs, drift-detection thresholds, or both.

### Archetype Roster

- [ ] Obtain and review the two resources provided by Dr. Go.
- [ ] Determine whether the archetype roster is the same as PFP classes or a separate persona concept.
- [ ] Determine whether revision changes the number of classes (currently 4) or only names/fields/features.
- [ ] Revise archetype roster (name, fields, features) based on Dr. Go's resources.

### Profile Classification & Drift

- [ ] Confirm: questionnaire is primary classifier at onboarding; RF model takes over once sufficient transaction history exists. 
	- Still open for discussion. Easy way out is finding a literature and get the average months/years at which people change personal profiles. Or better we can ask the users when they want to be reclassified at onboarding
- [ ] Define treatment of manual classification relative to questionnaire and model classification.
- [ ] Define drift detection trigger: time-based (N days), event-based (N transactions), or statistical (confidence below threshold).
- [ ] Formally define statistical and behavioral features for drift detection.
- [ ] Determine whether drift detection is server-side (requires model) or client-side (statistical, offline-capable).

### Intelligence Module

- [ ] Decide: single screen or single architectural module with multiple screens?
	-  Best decision is a modular architecture in which the model can be implemented. single module with multiple screenns
- [ ] Determine whether budget recommender is model-based or rule-based.
	-  Linear Programming
- [ ] Define scope of "behavioral assistant" submodule.
- [ ] Confirm inclusion/exclusion of "investment manager" submodule.
- [ ] Confirm inclusion/exclusion of receipt OCR (camera permission conflict with Article I §3).

### Transaction Class Hierarchy

- [x] Decide: are Savings and Debt true Transaction subclasses, or are they accounts/destinations?
	-  They are accounts/destinations

- [x] Define class hierarchy for Savings and Debt.
	- **DECIDED (Dr. Go, 2026-07-29):** Presets as categories, implemented via inheritance:
    ```
    Parent class: DEBT              (abstract — amount, balance, status)
    ├── Child: CreditCard           (interest_rate, statement_date, min_payment_formula, annual_fee, …)
    ├── Child: PersonalLoan         (interest_rate, loan_term, amortization_schedule, …)
    ├── Child: AutoLoan             (interest_rate, collateral, loan_term, …)
    ├── Child: HomeMortgage         (interest_rate, interest_type[fixed|variable], loan_term, …)
    ├── Child: StudentLoan          (interest_rate, grace_period, …)
    ├── Child: SSS/PagIBIGLoan      (interest_rate, payroll_deduction, …)
    ├── Child: SalaryLoan           (interest_rate, max_multiplier_of_salary, …)
    ├── Child: PeerInformalDebt     (interest_rate, lender_name, …)
    ├── Child: MedicalDebt          (interest_rate, payment_plan, …)
    └── Child: BusinessDebt         (interest_rate, business_name, …)
    ```
    - Same pattern applies to Savings:
    ```
    Parent class: SAVINGS            (abstract — target_amount, current_balance, deadline)
    ├── Child: EmergencyFund         (months_of_expenses, target_heuristic, liquidity_requirement, …)
    ├── Child: ShortTermSavings      (goal_description, target_date, …)
    ├── Child: RetirementSavings     (interest_rate, contribution_frequency, …)
    ├── Child: EducationFund         (target_date, institution_name, …)
    ├── Child: TravelFund            (target_date, destination, …)
    ├── Child: MajorPurchase         (item_description, target_date, …)
    ├── Child: HealthMedicalFund     (target_amount, …)
    ├── Child: HomePropertyDownPayment (target_amount, target_date, interest_rate, …)
    ├── Child: BusinessCapital       (target_amount, business_name, …)
    └── Child: GeneralSavings        (target_amount, target_date, …)
    ```
    - Users may create **custom child classes** outside the top 10 with their own field definitions.

- [x] UX flow for adding a debt instance:
    1. User navigates to Debts
    2. System displays available presets (displayed as **categories** in the UI)
    3. User selects a preset category (e.g., CreditCard)
    4. System presents the fields defined by that preset's business logic
    5. User fills in values → creates a **debt instance** that inherits from the selected preset

- [x] Map category groups to Article XXX §4 (Top 10 Filipino Savings Goal Categories) and Article XXXII §2 (Top 10 Filipino Debt Categories).
	- **RESOLVED:** Articles XXX §4 and XXXII §2 should be updated to describe the parent-child preset hierarchy instead of flat category labels. The top 10 presets ARE the categories as presented in the UI. Pending Specification revision.

### Specification Revision

- [ ] Complete finalization pass: resolve all TODOs, PROPs, and NOTE items.
- [ ] Cascade FBP → PFP rename through all articles, screen names, and navigation items.
- [ ] Explicitly define scope and limitations in a dedicated article or section.

---

## Unasked Questions

- Question 1.3 was not raised during the consultation.
