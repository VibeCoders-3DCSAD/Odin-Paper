# General
* In-tandem LSTM and Isolation Forest.
    * Isolation Forest is used to see what is and isn't considered as normal (Anomalies). In this case, normal varies from user to user. How do we take the variable income into account? How is your variable income? What if I have a high salary? Will celebrations be considered as an anomaly?
    * It'll detect overspending even if it doesn't go past budget.
* We need around a year of synthetic data and 2,000 respondents' data per profile. "2 thousand data needed for profile."
* User retention for more than 1 year is needed for best results in app.
    * Corrected: LSTM only needs at least 60 days of user retention to make proper results as per Charles' research.
* Back tracking should also be easier. E.g. I couldn't enter details for the past 3 weeks. There should be an option to add past details easily without too much backtracking. 
* Isolation forest needs variance for overfeed.
* LSTM also needs to learn variable incomes.
* On-boarding needs a reassessment feature.
* Umbrella Category > Sub-category. E.g. Essentials > Food & Drinks.
* Are the system features actually useful for the user? How often does the user override the recommendations?
    * Currently no solutions for low allocation.
    * Rule-based algorithm does not learn on the first few tries. A new algorithm is needed that learns.
* Rule-based alerts for anomalies, algorithm for budget recommendations. Even just detecting that current expense is high should be able to provide results.

# Budgeting Features
* High earning = higher budget. Low earning = lower budget.
* What's taken into account in the profile is the variability of your earnings.
* Your budget per week is consistent. But, for the variable, your income size is different. Budget is different per week or per time period.
* Budget needs stretching capabilities. System doesn't know when the user will get paid. (Part of Behavioral Profile. Flexible Variable)
* System recommends a budget, the user does it.
* Excess/Remaining balance is not considered protected balance if not stated.
* Recommendation, by default, cannot go lower than 18k, but configurable by user.
* What the user does with the previous money will be used for their own discretion.
* Jacquard index to determine the number of cases that'll change if there's a fluctuation of data.
* Obligation is needed. User needs to distinguish the difference between needs and wants (obligation weight).

# Fixed Expense Tracker
* Should be able to track fixed expenses (e.g. rent, subscriptions, etc.) without bill spiking up.
* Since we can base it on a person's spending habits. E.g. if system noticed that we're continuously paying for 3 months, maybe we can move it to stable.
## Protected Category
* Protected categories like food and consumption. It will be reduced when you eat, but has a certain threshold where it can be reduced by the engine. The same will be applied to other categories.
* In another definition, Protected Category is a category where users normally won't be able to configure unless needed.
    * Algorithm will be rule-based budget recommendation for protected categories. The system would never suggest cutting budget in these categories.
* Emergency is in essentials and is a protected category. You'll put money in but cannot take it out. 
* Excess balance from monthly budget balances will be allocated into Emergency Funds, or configurable by the user.
    * Preferably, there's a hierarchy of allocation priority. If Emergency Fund requirements are met, next are Savings. Then it goes on. E.g. User has 35k remaining balance from last month. 10% of it goes to the other categories if desired by user: 5k max goes to Emergency Funds, 3k max goes to savings, etc. 

# Future Spending Forecasting for Budget Recommendation with LSTM
* Budget Recommendation should align with Future Forecast
* "If you continue this kind of spending, our forecast determines that after a few years, you will be absolutely broke."
* Implement at least 2 to 3 uses of the forecast.
* To make informed budget recommendations for the next time periods.
* Give warnings to users that their spendings might exceed their income + create a budget guide for the user.
* Income is taken into account. High fluctuations on expenses are also taken into account. 
* It can also be positive. For example, if your expenses go down, the anomaly detection can also take effect.
* Process: Pre-trained LSTM -> Budgeting Profiles -> Tracking History from user's Odin profile -> Behavioral Profile -> Analyzes data from day 1 to current -> Sent to server -> LSTM processes it.
* Seasonal spending: Christmas, New Year, etc. E.g. birthday in May = higher spending in May.

# Anomaly Alerts
* Isolation Forest.
* Only activates at a certain percentage of expense.

# Examples
- User gets paid 45k for March, therefore needs to save.
- They pay for essentials and have a few balance left.
- User will put in a protected balance (cannot be spent).
- System asks user if they want to carry over remaining balance (except protected) until next month, or put it to their savings or other categories.
- System will also recommend what else you can do with the remaining balance.
