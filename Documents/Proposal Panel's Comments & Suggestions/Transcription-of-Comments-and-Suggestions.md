# Transcription of Comments and Suggestions for "Development of Odin: A Personal Budget Management System Using LSTM and Isolation Forest Algorithms"

## Ma'am Jomariss Baccay Plan, Panel Member

- Asked if the application is a mobile application.
	- The group clarified that the application is both for mobile and web.
- Asked who will use the web-based application.
	- Presumed that the mobile-based application will be used by the target users, then asked who the target users are.
		- The group answered that Filipino young professionals are the target users.
	- Asked who will use the web side.
		- The group answered that the web side is for additional accessibility, for when the users want to use the application on their personal computers.
	- Asked if there are no administrator users in the application.
		- The group confirmed.
	- Asked if the system is solely for general users.
		- The group confirmed.
	- Clarified that the system is accessible through web and mobile.
		- The group agreed.
- Asked about the machine learning component.
	- Clarified if LSTM will be used for prediction.
		- The group agreed but corrected "prediction" to "forecast."
	- Clarified if Isolation Forest will be used for detection.
		- The group agreed but corrected "detection" to "anomaly detection."
	- Asked how users are assigned to the financial behavioral profiles (Stable-Flexible, Stable-Obligated, Variable-Flexible, Variable-Obligated).
		- The group answered that during onboarding, users answer a set of basic questions to determine their profile.
	- Asked how users are going to be classified or categorized based on behavior if the system will not use clustering or classification algorithms.
		- The group reiterated that the set of questions concerning income range and obligation weight will determine the profile.
	- Asked how that will be classified.
		- The group answered that classification will be based on guidelines provided by the Bangko Sentral ng Pilipinas and governmental sources indicating income ranges or brackets.
	- Stated that during registration it is indicated that inputs will be obtained, extracted, and used on a machine learning algorithm.
	- Further added that the group can choose which machine learning algorithm will be used for that, then asked if the group intended not to.
		- The group answered that, currently, only rule-based algorithms are used for classification.
	- Finally stated that users must be classified into one of the four financial behavioral profiles using any clustering or classification algorithm of the group's choice.
- Asked about progressively changing behavioral profiles.
	- Asked if a user's behavioral profile can change or be changed over time.
		- The group answered that the user is able to change their behavioral profile.
	- Asked how often it can be changed.
		- The group answered any time.
	- Expressed brief confusion, then reiterated that the group will be responsible for classification.
	- Further elaborated with an example of being classified as "Flexible," then asked if the classification can be changed over time.
		- The group confirmed.
	- Asked if the progress must be tracked in a way that can affect or influence the profile.
	- Finally stated that if this topic were to be approved — and it is — the group needs to identify exactly how.
- Asked about the forecasting module.
	- Asked how users with no historical data will be handled.
		- The group answered that the system has a cold-start fallback.
- Asked about the savings goal module.
	- Asked how the savings goal projection will be calculated.
		- The group answered that the calculation is based on the rate at which the user is putting into the savings goal.
- Asked about the debt management module.
	- Asked why both the Avalanche and Snowball methods for debt payment were included, and what the difference between them is.
		- The group answered that the Snowball method prioritizes the smallest debt first for psychological wins, and the Avalanche method prioritizes the largest debt first for mathematically optimal repayment.
		- The group further explained that some users will prefer one method over the other.
		> NOTE: Though these are simply just recommendations, users should ultimately be able to pay their debts however they choose.
- Asked about protected categories.
	- Asked why some categories are protected from reduction.
		- The group answered that some categories like Essentials and Investments should be protected from reduction by the budget recommendation, as they are either essential to the user's day-to-day or are necessary to build wealth.

## Ma'am Janice Pola Congzon, Panel Member

- Asked about Odin.
	- Asked what distinguishes Odin from other personal finance and budgeting apps.
		- The group answered that other systems are "static," i.e., only basic statistics are displayed.
		- The group further explained that Odin dynamically forecasts expenses, savings, and repayment goals for the next week or month, i.e., the trajectory if the pattern of expenses, savings, and income are continued.
- Asked about the user financial behavioral profiles.
	- Asked how users are categorized, then stated a presumption that categorization is similar to "health apps" where the user is categorized based on their answers.
		- The group answered that during consultation with the Subject Matter Expert, Dr. Pamela A. Go from the College of Business and Financial Science, the question of the best way to categorize Filipino young professionals was raised.
		- The group continued explaining that Filipino young professionals are best described by income type and obligation weight.
	- Asked if the profiles are anchored to spending habits and expenses, i.e., if a user were a "Flexible" type, the financial plan and budget would be designed based on that behavior.
		- The group confirmed, stating that the basis for budget building in the system is heavily defined by the profiles.
		- The group further explained that, for example, Stable-Flexible users will have larger allocations for Discretionary expenses, and Variable-Obligated users have smaller allocations for them.
	- Asked if ultimately the user will decide allocations.
		- The group answered that the budget provided by the system is simply a recommendation, and users are still able to modify it.
- Asked about the Isolation Forest anomaly detection module.
	- Asked what it does.
		- The group explained that when users input expenses for a category that exceeds the thresholds of said category, the system will flag the transaction and alert the user.
	- Asked what the next steps are after the flagging, like if the system will reduce allocations for that category the next time.
		- The group confirmed, and noted that the protected categories are excluded from the reduction.
		- The group added an example that the system will suggest excess spending to be redirected to high priority categories such as emergency funds.
- Asked about additional recommendation features and reports.
	- Asked if there are analytics in the system.
		- The group answered that the analytics are in the Dashboard page, including income-expense forecasting, spending breakdowns, and budget health.

## Sir Daniel Dellosa, Panel Chairperson

- Asked about user transactions.
	- Asked if inputs are manual and not automatic.
		- The group confirmed, stating that the system cannot integrate banking and e-wallet systems due to integration fees and complexity.
	- Reframed the question, asking if governmental contributions like SSS and Pag-IBIG are automatically deducted in the income input.
		- The group confirmed that the deductions are not automatic.
	- Asked again if the contributions are deducted automatically.
		- The group answered that governmental contributions like SSS and Pag-IBIG are only voluntary when being considered in the budget, and only for Variable users such as freelancers, irregulars, and contract workers, as regular employees have those contributions automatically deducted from their salary as mandated by their employer.
	- Asked if the system is designed for regular working professionals.
		- Ma'am Plan corrected, saying that the system is for general users.
		- The group corroborated that the users encompass regular employees, freelancers, and contract workers.
	- Asked if there is a way to schedule expenses, stating that utility bills, for example, are charged regularly, and even a way to integrate utility apps like the Meralco app.
		- The group reiterated that integration is hard and beyond the scope of the proposal.
