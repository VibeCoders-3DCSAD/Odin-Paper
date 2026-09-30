## Objectives

The general objective of the study is to develop BUDGIE, a personal financial management application for Filipinos residing in the National Capital Region, using rule-based savings and debt classification, SARIMA expense forecasting, LP budget recommendation, and IQR unusual spending detection to generate a personalized financial plan. The system aims to produce the user’s savings and debt classifications, forecast future expenses, recommend how the user-defined budget should be allocated across expense categories, and identify recorded transactions that deviate from the user’s normal spending habits, presenting these outputs as decision-support information with explanations.

  

## Specific Objectives

To fulfill the general objective, the researchers have constructed the following specific objectives:

1. Examine the fundamental financial management challenges and needs of Filipinos aged 18 to 59 who live or work in the National Capital Region, using the PUEPS pre-survey as preliminary investigation.
    
2. Explore existing finance management systems and applications, including architectural patterns, feature sets, and analytical capabilities, to identify gaps in localization, intelligence features, and contextual sensitivity that BUDGIE aims to address.
    
3. Analyze and preprocess data from the PSA Family Income and Expenditure Survey and quarterly Household Final Consumption Expenditure data from 2022 to 2026 to prepare suitable datasets for model training, validation, and testing. Publicly available reports and microdata from the PSA Data Archive (PSADA) will be used; survey responses collected directly by the researchers will be handled under the study's informed-consent and data-protection procedures.
    
4. Train and evaluate the four models of BUDGIE : the Savings and Debt Classification Algorithm, the Budget Optimization model, the Expense Forecasting model, and the Anomalous Expense Detection model, using the following algorithms and metrics:
    
	
	1. Debt and Saving Classification (Rule Based):
	    
	
		1. Accuracy
		    
		2. Precision
		    
		3. Recall
		    
		4. F1-Score
	    
	
	2. Budget Generation (Linear Programming):
	    
	
		1. Constraint Satisfaction Rate (adherence to hard constraints such as budget ceiling, minimum floors, and profile rules)
		    
		2. Budget Utilization Rate (proportion of available funds allocated)
		    
		3. Deviation from User Preferences (deviation of the allocation from the user's category priorities and preferences)
	    
	
	3. Expense Forecasting (Seasonal Autoregressive Integrated Moving Average/SARIMA):
	    
		
		1. Mean Absolute Error (MAE)
		    
		2. Symmetric Mean Absolute Percentage Error (SMAPE)
		    
		3. Mean Directional Accuracy (MDA)
		    
		4. Root Mean Square Error (RMSE)
		    
	
	4. Anomalous Expense Detection (Inter-quartile Range/IQR):
	    
	
		1. Accuracy
		    
		2. Precision
		    
		3. Recall
		    
		4. F1-Score
    

5. Design the application with the following features:
    

	1. Dashboard - provides a quick overview of expense forecasts, recent transactions, budget plans and health, savings goals, debts, and anomalous transaction alerts.
	    
	2. Financial Plan Management - allows users to manage an accepted or created season-appropriate budget, savings contribution schedule, and debt repayment plan based on expense forecasts, available income, savings and debt classification, financial obligations, savings goals, and the target debt payoff date.
	    
	3. User Authentication - allows users to securely register, log in, log out, and recover their accounts.
	    
	4. Savings and Debt Classification - allows users to complete a questionnaire, and receive a savings classification and a debt classification that serve as inputs to the Financial Plan and update over time from their recorded financial data.
	    
	5. User Onboarding - guides new users through financial preferences, income sources, expense categories, current savings goals, and current debts.
	    
	6. Cash Flow Management - allows users to record, view, categorize, update, and monitor income and expense transactions.
	    
	7. Recurring Expense Management - allows users to manage scheduled income such as salaries and allowances, scheduled expenses such as subscriptions and bills, savings contributions, and debt repayments.
	    
	8. Billers and Remittances - allows users to create, update, and delete current bills, essential expenses, payment schedules, and upcoming financial commitments.
	    
	9. Income Sources Management - allows users to manage salaries, allowances, side income, and other sources of earnings, while organizing associated cash, bank accounts, and e-wallets based on recorded transactions and balances, without direct bank or e-wallet API integration.
	    
	10. Savings Goal Management - allows users to define targets such as emergency funds, tuition, rent, medical expenses, or planned purchases; record contributions; monitor cumulative progress; and project goal completion..
	    
	11. Debt Management - allows users to record debts, track balances and payments, compare repayment strategies such as the snowball or avalanche methods to project payoff timelines, and identify potential debt risks caused by insufficient budgets or known upcoming expenses.
	    
	12. User Settings - allows users to manage their profile, preferences, notifications, security, and application configurations.
	    
	13. Financial Reports - allows users to view summaries and reports of income, expenses, savings, and debt for specified periods and categories, including personalized spending forecasts, and alerts for unusual expenses or spending patterns that differ from their normal spending pattern.
	    

6. Test the functionality, reliability, performance efficiency, usability, security, and portability of the system.
    
7. Evaluate the system using the System Usability Scale (SUS) and metrics based on the ISO/IEC 25010 software quality model. The evaluation will cover:
    

	1. System Usability Scale:
    
	2. ISO/IEC 25010:
    
	
		1. Functional Suitability
		    
		
			1. Functional completeness
			    
			2. Functional correctness
			    
			3. Functional appropriateness
		    
		
		5. Reliability
		    
		
			1. Availability
			    
			2. Fault tolerance
			    
			3. Recoverability
		    
		
		9. Performance Efficiency
		    
			
			1. Time behavior
			    
			2. Capacity
		    
		
		12. Usability
		    
		
			1. Appropriateness recognizability
			    
			2. Learnability
			    
			3. User error protection
			    
			4. User interface aesthetics
		    
		
		17. Security
		    
		
			1. Confidentiality
			    
			2. Integrity
			
			3. Portability
			    
			
			4. Adaptability
		    

8. Deploy the personal financial management application to the Android platform and document its result.