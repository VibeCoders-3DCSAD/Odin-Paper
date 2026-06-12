### Core Profile Classification Features from BSP CFS

These features directly map to the onboarding questions and behavioral indicators in Odin

#### 1. Income Stability & Employment Context

This is the most critical group for distinguishing between `Stable` and `Variable` income profiles.

| BSP CFS Data Label | Concept from Odin | Feature Engineering | Notes |
| :--- | :--- | :--- | :--- |
| **Nature of Employment** | Employment Status (Regular/Permanent, Contractual, Freelancer, etc.) | Categorical variable: `Regular/Permanent`, `Temporary/Fixed-term`, `No Formal Contract`. | This is the single best proxy for income stability. |
| **Class of Worker** | Employment Status (e.g., "Business owner / Entrepreneur") | Categorical variable: `Salary/Wage worker`, `Self-employed/Employer`, `Unpaid/Volunteer`. | Identifies entrepreneurs. |
| **Specific Occupation** | Context for income variability (e.g., "Tricycle Driver", "Vendor", "Sari-sari store owner") | Categorical variable (top 10-20 occupations). | Provides granularity for variable income. |
| **Total Annual Household Income** | Income amount and frequency (converted to monthly) | Continuous variable (or binned deciles). | Base for calculating income stability metrics. |
| **Number of Income Sources** | Single vs. multiple income streams | Continuous variable (count of income sources). | Diversified income is a form of stability. |
| **Primary Income Source** | Which source is dominant (Employment, Entrepreneurial, Other) | Categorical variable. | Classifies reliance on wages vs. business vs. ayuda/remittances. |

#### 2. Obligations, Dependents & Protected Categories

These features address the user stories about "fixed obligations," "financial dependents," and "protected expense categories."

| BSP CFS Data Label | Concept from Odin | Feature Engineering | Notes |
| :--- | :--- | :--- | :--- |
| **Any Outstanding Loan** | Fixed obligations (e.g., housing, vehicle, salary loans) | Binary variable. | Indicates presence of non-discretionary monthly payments. |
| **Financial Status (Dependent)** | "Declare financial dependents or family support obligations" | Continuous variable (number of dependents in the PEU). | Key metric for household responsibility. |
| **Age Distribution (Dependency Ratio)** | Proportion of young/old dependents vs. working-age adults | Continuous variable (ratio). | Measures financial pressure on the primary earner. |
| **Expenditure Share (Housing, Utilities, Transport)** | Essential, non-negotiable spending | Continuous variable (percentage of budget). | Users can mark categories as "protected". |
| **Past Due Bills** | Difficulty meeting obligations (deficit warning) | Binary or count variable. | Indicates financial distress and inflexibility. |

#### 3. Spending Behavior (Culturally & Contextually Relevant)

These features address Filipino-specific spending patterns (e.g., "family support, paluwagan").

| BSP CFS Data Label | Concept from Odin | Feature Engineering | Notes |
| :--- | :--- | :--- | :--- |
| **Food Share (at home)** | Spending on essentials (often a large share for lower-income profiles) | Continuous variable (percentage of budget). | Reflects Engel's Law and income level. |
| **Other Savings (Paluwagan)** | Culturally cyclical spending/saving | Binary variable. | Unique Filipino financial behavior. |
| **Assistance from Family/Remittances** | Family support obligations (giving or receiving) | Continuous variable (amount or binary). | Captures financial interdependency. |
| **Miscellaneous expenses (Celebrations, Gifts)** | Culturally cyclical spending (Christmas, fiestas) | Continuous variable (amount or percentage). | Can be used to model seasonal spending pressure. |
| **Ownership of livestock/poultry** | Culturally relevant asset for family/home-based needs | Binary or count variable. | May indicate a "side hustle" or home-based economic activity. |

#### 4. Savings, Debt & Risk Profile

These features align with the savings goals and debt management modules.

| BSP CFS Data Label | Concept from Odin | Feature Engineering | Notes |
| :--- | :--- | :--- | :--- |
| **Cash Savings at Home** | Having an emergency fund / savings | Continuous variable (amount). | Primary indicator of savings behavior. |
| **Ownership of Deposit Account** | Access to formal financial system | Binary variable. | Indicates financial sophistication. |
| **Ownership of Insurance/Pension** | Long-term financial planning | Binary variable. | A hallmark of a more stable, forward-looking profile. |
| **Vehicle Loan (Motorcycle)** | Common debt for variable-income earners | Binary variable. | Motorcycles are often financed by "necessity entrepreneurs" (e.g., habal-habal drivers). |
| **Business Loan (Microfinance)** | Debt for entrepreneurial activity | Binary variable. | Strong indicator of entrepreneurial income profile. |
| **Risk Preference (Self-rating 0-10)** | User's own financial risk attitude | Ordinal variable (0-10 scale). | A powerful attitudinal feature. |

#### 5. Demographics & Context

These are control and contextual features as described in the onboarding process.

| BSP CFS Data Label | Concept from Odin | Feature Engineering | Notes |
| :--- | :--- | :--- | :--- |
| **Age of Respondent (EDM)** | Age (target 20-40) | Continuous variable. | -- |
| **Highest Educational Attainment** | Educational background | Ordinal variable. | Correlated with income stability and financial literacy. |
| **Place of Residence (NCR vs. AONCR)** | Geographic context (Metro Manila focus) | Binary variable. | Differences in cost of living and economic opportunity. |
| **Tenure Status (Homeowner vs. Renter)** | Indicator of wealth and stability | Categorical variable (Own, Rent, Neither). | -- |
| **Health Insurance Coverage** | Access to social safety net | Categorical variable (None, PhilHealth only, Private). | Reduces financial vulnerability. |

---

### Derived Composite Features for the Random Forest Model

The BSP CFS allows you to calculate powerful composite features that are more predictive than raw labels alone.

1.  **Income Stability Score (Binary/Ordinal):**
    - **Rules:** Based on `Nature of Employment` (Regular = Stable), `Class of Worker` (Self-employed = Variable), and the Coefficient of Variation (CV) of monthly income if multiple data points were available. This directly operationalizes the "Stable" vs. "Variable" income decision rule.

2.  **Obligation-to-Income Ratio (Continuous):**
    - **Formula:** `(Total monthly loan amortizations + Essential non-food expenditure) / Monthly Income`. This quantifies the pressure of "fixed obligations" and "protected categories".

3.  **Dependency Burden Score (Continuous):**
    - **Formula:** `Number of financially dependent members / Number of working members`. A core feature for identifying profiles under household financial strain.

4.  **Financial Cushion Index (Continuous):**
    - **Formula:** `(Cash savings at home + Bank deposit balance) / (3 x Monthly Expenditure)`. A proxy for the "savings goal" progress and emergency preparedness.

5.  **Debt Strategy Indicator (Categorical):**
    - **Rules:** Look at the number and types of debts. A profile with `high-interest debt` (e.g., individual money lender, credit card) but `multiple income sources` might prefer the `Avalanche` method. A profile with `many small, informal debts` might be pushed toward `Snowball`. This is not a direct label but a pattern to extract.

### How to Use These Features for Random Forest Classification (Suggestion Only)

- **Target Variable (The 4 Profiles):** While the CFS does not have a "financial behavioral profile" label, you can create a ground truth for training by clustering households based on a combination of the key features above. For example:

    - **Profile 1 (Stable/Saver):** Regular employment, high education, owns deposit account & insurance, low dependency ratio, high financial cushion.

    - **Profile 2 (Variable/Obligated):** Self-employed/contractual, high dependency ratio, has outstanding loans (e.g., motorcycle, salary), medium financial cushion.

    - **Profile 3 (Variable/Necessity Entrepreneur):** No formal contract, engaged in agriculture/retail, has microfinance loan, low education, low financial cushion.

    - **Profile 4 (Variable/Recipient):** Primary income from "Other Sources" (ayuda, remittances), possibly unemployed or elderly EDM, no formal account, low savings.

- **Training the Model:** Use the CFS dataset to train the Random Forest classifier to predict this engineered 4-profile target variable using the features extracted above.

- **Deployment (Odin App):** Once trained, the model's logic can be simplified into a rule-based system or a lightweight inference engine for the app. A new user's onboarding answers (e.g., "I am a freelance delivery rider", "I support my parents and siblings", "I have a motorcycle loan") will map to these same feature categories, allowing the app to instantly classify them and provide personalized guidance.