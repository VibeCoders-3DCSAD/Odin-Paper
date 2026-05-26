# Panel Comments and Suggestions

## Ma'am Jomariss Baccay Plan

- The nature of the application was raised — specifically whether it was mobile or web-based.
  - The application was clarified to be accessible on both mobile and web platforms. The mobile application was intended for the primary target users (Filipino young professionals), while the web platform served as an additional access point for users who preferred to use the application on a personal computer. There were no administrator users — the system was solely for general users.

- The machine learning components of the system were raised.
  - The system used **LSTM** for expense and income **forecasting**, and **Isolation Forest** for **anomaly detection**. The distinction between "prediction" and "forecasting", and between "detection" and "anomaly detection", was noted and clarified.

- The classification of users into financial behavioral profiles (Stable-Flexible, Stable-Obligated, Variable-Flexible, Variable-Obligated) was raised, with the note that a clustering or classification algorithm must be used for this purpose.
  - During onboarding, users answered a set of questions regarding income type and obligation weight. These answers, guided by income brackets from the Bangko Sentral ng Pilipinas and other governmental sources, determined the user's profile. The panel noted that this rule-based approach was insufficient and required that a proper **clustering or classification algorithm** be used to classify users into their respective profiles.

- The need to track changes in the user's behavioral profile over time was raised.
  - The group confirmed that users could change their behavioral profile. The panel required that profile changes be tracked progressively, and that the exact mechanism by which user behavior and progress influenced or updated the profile be clearly defined.

- The handling of users with no historical data in the forecasting module was raised.
  - The system was explained to have a **cold-start fallback** for new users without historical data.

- The method for calculating savings goal projections was raised.
  - Savings goal projections were calculated based on the rate at which the user was contributing to the savings goal over time.

- The inclusion of both the Avalanche and Snowball debt repayment methods and the difference between them was raised.
  - The **Snowball method** prioritized the smallest debt first, providing psychological wins through early payoffs. The **Avalanche method** prioritized the highest-interest debt first, offering mathematically optimal repayment. Both methods were included because different users would prefer different approaches. Users retained full control over how debts were paid, with the system providing these as recommendations only.

- The rationale for protecting certain budget categories from reduction was raised.
  - Categories such as **Essentials** and **Investments** were protected from budget reduction recommendations because they were either critical to the user's daily needs or necessary for building long-term financial health.

---

## Ma'am Janice Pola Congzon

- What distinguished Odin from other personal finance and budgeting applications was raised.
  - Unlike other systems that displayed only basic static statistics, Odin **dynamically forecasted** expenses, savings, and repayment goals for the next week or month. The system projected the user's financial trajectory based on continued patterns of income, expenses, and savings — making it an active financial planning tool rather than a passive tracker.

- The categorization of users into financial behavioral profiles and whether the profiles were anchored to spending habits and financial planning was raised.
  - During consultation with Subject Matter Expert Dr. Pamela A. Go from the College of Business and Financial Science, it was determined that Filipino young professionals were best described by **income type** (Stable or Variable) and **obligation weight** (Flexible or Obligated). The resulting profiles served as the foundation for budget-building in the system. For example, Stable-Flexible users received larger allocations for Discretionary expenses, while Variable-Obligated users received smaller allocations for the same. Users retained the ability to modify these allocations, as the budget was a recommendation, not a mandate.

- The function of the Isolation Forest anomaly detection module and the steps taken by the system after flagging an anomaly were raised.
  - When spending in a category exceeded the defined threshold, the system flagged the transaction and alerted the user. Following the flag, the system suggested that excess spending be **redirected to higher-priority categories** such as emergency funds, and reduced the allocation for the flagged category in the next budgeting period. Protected categories were excluded from reduction.

- The availability of analytics and reporting features in the system was raised.
  - Analytics were available on the **Dashboard**, including income-expense forecasting, spending breakdowns, and budget health indicators.

---

## Sir Daniel Dellosa, Panel Chairperson

- Whether transaction inputs were manual or automatic, and whether government contributions such as SSS and Pag-IBIG were automatically deducted from income, was raised.
  - All transaction inputs were **manual**. The system could not integrate with banking or e-wallet systems due to integration fees and technical complexity. Regarding government contributions, **regular employees** had SSS and Pag-IBIG automatically deducted from salary by the employer as required by law, so these were already reflected in the net income input. For **variable-income users** such as freelancers and contract workers, these contributions were voluntary considerations and could be optionally accounted for in the budget.

- Whether a feature for scheduling recurring expenses existed, and whether integration with utility applications such as the Meralco app was feasible, was raised.
  - Integration with third-party utility applications was outside the scope of the proposal due to technical complexity. The feasibility of a recurring expense scheduling feature was acknowledged as a valid consideration for the system.
