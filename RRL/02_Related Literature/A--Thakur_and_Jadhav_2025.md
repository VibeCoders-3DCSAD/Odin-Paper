---
paper_id: "c3f5a6d8-9e1b-4c7a-8d2f-6e9b4a7c1d5e"
designation: algorithm-specific
title: "Expense tracker management system using machine learning"
authors: "Thakur, R. S.; Jadhav, A."
year: 2025
venue: "Sigma Journal of Engineering and Natural Sciences"
---

# Expense tracker management system using machine learning

## ARTICLE INFO

## ABSTRACT

The transition from "Income and Expense Tracker" to "Expense Tracker Management System" marks a strategic evolution in financial management tools. This shift underscores a more focused approach towards efficiently tracking and managing expenses. While the former emphasized both income and expenses, the latter places a heightened emphasis on expense management specifically. This refined system aims to streamline expense tracking processes, offering users a robust platform to meticulously monitor and analyze their spending habits. Through customizable features, intuitive interfaces, and comprehensive reporting functionalities, the "Expense Tracker Management System" empowers users to take full control of their finances, fostering greater financial awareness and facilitating smarter spending decisions which makes it better than the existing state-of-the-art. The article also emphasizes predicting future expenses based on prior experience of the user, using machine learning techniques. Different machine learning techniques are used for prediction purposes such as multi-layer perceptron, extreme gradient boosting, support vector machine and ensemble techniques such as bagging, boosting. Extreme Boost (XGBoost) outperforms other individual models with highest R-square value and voting ensemble regressor outperforms ensemble techniques with highest R-square value of \(78.11\%\) and lowest relative absolute error of 0.6121.

Cite this article as: Thakur RS, Jadhav A. Expense tracker management system using machine learning. Sigma J Eng Nat Sci 2025;43(4):1265-1275.

## INTRODUCTION

Introducing the "Expense Tracker Management System," a cutting-edge solution designed to revolutionize the way individuals track and manage their expenses in today's fast-paced world. Since the dawn of civilization, economic transactions have been a fundamental aspect of human existence, evolving into an indispensable component of daily life. With most individuals operating on fixed incomes, effective budgeting becomes paramount, necessitating the meticulous tracking of expenditures to ensure financial stability.

necessitating the meticulous tracking of expenditures to ensure financial stability.

Traditionally, expense tracking involved laborious manual methods, such as recording transactions with pen and paper. However, the proliferation of electronic devices, notably smartphones and computers, has ushered in a new era of convenience and efficiency. Today, a myriad of software applications exists to assist users in monitoring their daily expenses, providing invaluable insights into spending habits and ensuring adherence to budgetary constraints.

Despite the availability of expense tracking apps, many still rely on manual input systems, which can be time-consuming and prone to error. Recognizing this challenge, we propose an innovative approach to expense management that leverages automation to streamline the process. Our system aims to offer users a seamless and efficient experience, allowing them to input, track, and monitor their expenses with ease. At the heart of our solution lies the concept of automation, which eliminates the need for manual data entry and significantly reduces the time and effort required to manage expenses. By harnessing the power of technology, users can effortlessly stay on top of their finances, ensuring that expenditures remain within budgetary limits.

The "Expense Tracker Management System" offers a comprehensive suite of features designed to meet the diverse needs of users. From categorizing expenses into predefined categories such as food, entertainment, transportation, education, health, and clothing to generating detailed reports of spending patterns, our system provides users with invaluable insights into their financial health. Furthermore, our system incorporates predictive analytics capabilities, allowing users to forecast their monthly budgets with precision. By analyzing past spending patterns and income trends, the system can generate accurate projections, empowering users to make informed financial decisions and avoid budgetary pitfalls.

In addition to its predictive capabilities, the "Expense Tracker Management System" also offers real-time notifications and alerts to keep users informed about their financial status. Whether it's a reminder to pay bills or a warning that expenses are approaching budgetary limits, our system ensures that users always stay proactive and in control of their finances.

Overall, the "Expense Tracker Management System" represents a paradigm shift in the way individuals approach expense tracking and management. Our platform is designed to offer users a customized experience through a personalized dashboard, enabling seamless financial management.

Personalized Dashboard: Our platform features a personalized dashboard, eliminating the need for generic interfaces. This dashboard is uniquely crafted to adapt to individual financial needs and preferences, providing users with a comprehensive overview of their financial status briefly. Advanced Expense Categorization: Simplifying expense tracking is at the core of our platform's functionalities. With our advanced categorization feature, users benefit from intelligent expense management capabilities. This system efficiently categorizes expenses, facilitating easier tracking and analysis of spending habits. Intelligent Alerts and Notifications: Ensuring users stay informed and in control is paramount. Our platform incorporates intelligent alerts and notifications to keep users updated on significant financial events, impending bill payments, and deviations in spending patterns.

This proactive approach ensures users remain vigilant and responsive to their financial circumstances.

The article delves into how machine learning techniques are leveraged to predict future expenses based on the prior experiences of users. This involves analyzing past spending patterns and behaviors to forecast future financial needs and trends. In recent years, machine learning (ML) has experienced significant growth and has demonstrated its potential across a wide array of applications. This expansion is driven by the ability of ML algorithms to process vast amounts of data and extract meaningful patterns, leading to smarter, more efficient, and innovative solutions across various fields. By leveraging these diverse machine learning techniques, financial institutions and services can offer more accurate and personalized expense predictions. This helps users manage their finances better, anticipate future spending needs, and make informed financial decisions.

Let's review the existing methods and analyses previously conducted in this domain. The article examines some of these prior works and identifies the limitations that our work aims to address. The state-of-the-art description of existing work is discussed in Table 1.

The rest of the article is organized as follows: after discussing introduction and literature review, which provides insight of the existing expense tracker management system, Section 2 provides information on the dataset utilized for experimentation, along with description of machine learning models. Section 3 discusses the proposed work. Section 4 illustrates results and outcomes in terms of evaluation metrics and web application design. Finally, section 5 discusses concluding remarks and recommendations for future work.

## MATERIALS AND METHODS

The section discusses the details of dataset utilized in our experiment, along with different machine learning models applied to predict expenses.

### Dataset Description

The "Daily Household Transactions" [16] file contains information about the virtual transactions people make every day. This information includes information about the products purchased, the price used for each product, the date and time of each transaction, the payment for each transaction, and the location of each document (debit/income). Data can be used to analyze purchasing behavior and financial management, estimate expenses, and develop savings strategies and budgets. This data is ideal for data analysis and machine learning and can be used to train predictive models and make decisions from the data. The dataset attributes are as follows.

- Date: The date and time of the transaction
- Mode: The payment method used for the transaction
- Category: Transactions are grouped into various categories
- Subcategory: Categories are further divided into subcategories of transactions
- Note: A short description of the transaction
- Amount: The transaction amounts
- Income/Expense: Indicates whether the transaction is an expense or income.
- Currency: All transactions are recorded in the official currency of India

### Machine Learning Models

Nowadays, machine learning has potential applications which continues to evolve and expand into new various areas such as healthcare, finance, industry etc. By leveraging vast amounts of data and advanced algorithms, ML enables smarter, more efficient, and innovative solutions across various fields [17].

- **Extra Tree (ET)**: ET is an ensemble learning method that aggregates the predictions of multiple de-correlated decision trees collected in a "forest" to improve the predictive accuracy and control overfitting. Unlike Random Forest, which selects optimal cut-points for splits, Extra Trees split nodes using random cut-points for each feature, which introduces more randomness into the model.
- **Categorical Boosting (CatBoost)**: CatBoost incorporates advanced techniques like ordered boosting, which improves training speed and reduces overfitting. Its strength lies in its robustness, ease of use, and ability to deliver high-quality predictions on a wide range of datasets without extensive hyperparameter tuning, especially for complex data that can be resolved with techniques such as pruning and integration.

### Ensemble Learning Models

Ensemble learning [18, 19] is a technique in machine learning where we combine the predictions of several different models to make a stronger and more accurate model than any individual model. By pooling together predictions from diverse models, ensemble learning helps to reduce the weaknesses of individual models while maximizing their strengths, resulting in better overall performance [20].

- **Bagging**: Involves training multiple instances of the same base model on different subsets of the training data and averaging their predictions.
- **Boosting**: Builds a strong learner by sequentially training multiple weak learners, where each subsequent learner focuses more on the misclassified instances from the previous learners.
- **Stacking**: Involves training multiple base models and then using a meta-model to combine their predictions, treating the predictions of base models as additional features.
- **Voting**: Combines the predictions of multiple models by aggregating their individual predictions using a simple voting mechanism (e.g., majority vote for classification or averaging for regression).
- **Blending**: Blending is like stacking, but it uses a holdout set (a part of the training set) to generate predictions for the training set of the meta-model. This can be more robust than voting or a single layer of models since it incorporates multiple stages of learning and validation.

## PROPOSED WORK

The section discusses the proposed work in terms of data preparation phase and regression phase. The Daily Household Transaction dataset is pre-processed to apply machine learning models for training and predicting expenses. The data preprocessing is divided into multiple steps; the first step is normalization using MinMax scaling technique which scales each feature to a given range, between 0 and 1 [21]. This scaling is useful when you want all features to be on a similar scale, which can improve the performance of many machine learning algorithms. In second step is transformation of amount attribute using log1p function. The log1p function computes the natural logarithm of \(1 + x\) which is useful for transforming data (amount in our case) that may contain zero or small positive values as shown in Figure 1.

![Figure 1: Data Transformation, distribution of log(1 + amount)](image_placeholder_1)

Lastly, the third step in data preprocessing is vectorizer process using 'TfidfVectorizer (min_df=3)', it transforms text data into numerical values based on the term frequency-inverse document frequency (TF-IDF) statistic, parameter 'min_df=3' specifies that only terms (words or tokens; in our case 'Mode', 'Category', 'Subcategory', 'Note', 'Income/Expense') that appear in at least three documents will be considered, reducing noise and dimensionality. By converting the text data into TF-IDF vectors, it transforms the text into a numerical format that can be fed into algorithms.

After successful preprocessing, the dataset is divided into the ratio of 70:30, where \(70\%\) is used for training and \(30\%\) is used for testing purposes. The next phase is regression phase, the training data and testing data is fed to multiple machine learning models and predictions are made, evaluated using two regression metrics; r-squared value and mean absolute error.

## RESULTS AND DISCUSSION

The section discusses the evaluation parameters used in the experiment, along with a description, results of the machine learning model. The section also showcases the web application description and screenshots of the web application for better understanding.

### Evaluation Parameters

The results of the Expense Tracker Management System are evaluated in terms of R-squared value, Mean Absolute Error, Mean Square Error and Relative absolute error. These are the common parameters used in regression analysis. They provide different perspectives on how well a model is performing.

#### R-squared (R2) value

Also known as the coefficient of determination, R-squared measures the proportion of the variance in the dependent variable (target) that is predictable from the independent variables (features). Higher R-squared scores (closer to 1) indicate better model fit.

$$R^2 = 1 - \frac{SS_{res}}{SS_{tot}} \tag{1}$$

where, \(SS_{res}\) and \(SS_{tot}\) the sum of the squared differences between the observed values and the predicted values, and the sum of the squared differences between the observed values and the mean of the observed values respectively.

#### Mean absolute error (MAE)

This metric quantifies the average magnitude of errors between predicted and actual values. Lower MAE values indicate better model performance.

$$MAE = \frac{1}{n}\sum_{i = 1}^{n}\left|y_{i} - \hat{y}_{i}\right| \tag{2}$$

where, \(n\) is the number of observations, \(y_i\) is the actual value, and \(\hat{y}_i\) is the predicted value.

#### Mean square error (MSE)

MSE measures the average of the squares of the errors that is, the average squared difference between the actual values and the predicted values.

$$MSE = \frac{1}{n}\sum_{i = 1}^{n}\left(y_{i} - \hat{y}_{i}\right)^{2} \tag{3}$$

where, \(n\) is the number of observations, \(y_i\) is the actual value, and \(\hat{y}_i\) is the predicted value.

#### Relative absolute error (RAE)

RAE measures the total absolute error as a proportion of the total absolute error of a simple predictor, such as the mean of the actual values. It provides a normalized measure of prediction accuracy.

$$RAE = \frac{\sum_{i = 1}^{n}|y_{i} - \hat{y}_{i}|}{\sum_{i = 1}^{n}|y_{i} - \bar{y}|} \tag{4}$$

where, \(n\) is the number of observations, \(y_i\) is the actual value, \(\hat{y}_i\) is the predicted value, and \(\bar{y}\) is the mean of actual value.

The R-square value provides an indication of how well the model's predictions match the actual data. MAE measures the average magnitude of errors in a set of predictions. Relative absolute error is particularly useful when comparing different models. Mean square error is a preferred metric for optimizing and assessing model fitness, also offers an absolute measure of predictive accuracy. The performance of the different machine learning and ensemble models is evaluated over these metrics and is shown in Table 2.

The results in Table 2 showcase the performance of individual machine learning models and ensemble learning techniques. The parameter tuning process for the selected machine learning models involves identifying key hyperparameters such as learning rate for XGBoost or number of neighbors for KNN, by using Hit and Trial method. The models are evaluated based on performance metrics such as R-squared and Mean Absolute Error through cross-validation to prevent overfitting. The best-performing hyperparameters are selected and validated on a test set to ensure that improvements are generalizable to new data. The performance of XGBoost technique outperforms other individual machine learning models with a highest r-square value of 77.89, while Voting Ensemble Regressor outperforms individual models and other ensemble approaches with highest r-square value of 78.11 and lowest relative absolute error of 0.1765. As r-square value is a useful metric for evaluating the explanatory power of a model, it does not always provide a complete picture of model performance. Since there is no more difference in the r-square value of models because of characteristics of the dataset, as the distribution of the variables and the nature of their relationships, explaining the same amount of variance. RAE stands out be the deciding factor in our approach as the RAE of voting ensemble regressor is lowest.

### Web Application Development

The application development for expense tracking involves ensuring seamless user experience by incorporating features such as income and expense limits, savings tracking, and intuitive interfaces. The effectiveness of the reminder system is crucial for user engagement and adherence to budgeting goals. A user-friendly design reduces the learning curve, making the app accessible to diverse demographics. The framework behind the application development is described below.

#### Backend Development

- **Django (Python)**: Django is chosen for its robust framework and extensive built-in features, which streamline the development process.
- **Django's Built-in Authentication**: Implement role-based access control (RBAC) using Django's authentication system.
- **Django Paginator Class**: Implement server-side pagination for efficient data management.
- **Django Admin Customization**: Customize the Django Admin interface for better usability.
- **Database**: PostgreSQL is selected for its reliability, robustness, and support for complex queries and transactions.

#### Frontend Development

- **HTML, CSS, JavaScript Ajax**: Use jQuery for making asynchronous requests to the server.
- **JavaScript and Django**: Develop Ajax-based search functionality for querying the database in real-time.

#### Application Features

1. **User Authentication and Security**: Utilize Django's built-in authentication for user registration, login, and role-based access control (RBAC).
2. **Expense Tracking**: Allow users to manually enter expenses via forms.
3. **Expense Categorization**: Predefined Categories which provide categories such as food, transportation, entertainment, and utilities. Also, custom categories which allow users to create custom categories.
4. **Analytics and Reporting**
   - Visual Reports: Generate visual reports using JavaScript charting libraries like Chart.js.
   - Predictive Analytics: Implement machine learning models for expense prediction.
   - Budget Forecasting: Offer monthly budget forecasts and highlight potential overspending areas.

### Application Description

The section provides the screenshots of the application and its working in the form of description. User authentication in Django involves configuring the built-in authentication system, creating login views and templates, and managing user sessions using functions like 'login()' and 'logout()'. User authorization utilizes Django's permissions system, where permissions can be defined at the model level and enforced using decorators like '@login_required' to restrict access to views based on authentication status. Customization can be done by creating custom authentication backends or user models to suit specific requirements, the login page is shown in Figure 2.

![Figure 2: Login page](image_placeholder_2)

The expense tracker management system provides a detailed expense summary that offers users a comprehensive view of their financial activity. The summary includes the total expenses for a selected period, along with a breakdown by categories such as food, transportation, and entertainment, visualized through pie or bar charts as shown in Figure 3. Monthly spending trends are depicted using line charts, highlighting patterns and significant variances. Detailed transaction lists are available for review, showing individual expenses with dates, amounts, and descriptions. Users can also see their top expenses, compare their actual spending against budget limits with progress bars, and view predictive analytics for future expenses. Additionally, a savings overview indicates the total savings achieved, helping users monitor their financial goals effectively. To enhance financial management, the system allows users to create and manage custom expense categories, provides expense forecasting through advanced algorithms, and tracks income sources alongside expenses for a complete financial picture.

![Figure 3: Expense summary](image_placeholder_3)

The income summary in the expense tracker management system offers users a clear and detailed overview of their earnings over a specified period as shown in Figure 4. It includes the total income received, broken down by sources such as salary, freelance work, and other income streams. This breakdown is visualized through charts like pie charts or bar graphs for easy analysis. Monthly income trends are displayed using line charts, helping users identify patterns and variations in their earnings. A detailed list of income transactions is provided, showing dates, amounts, and sources, enabling users to verify and track their earnings accurately. The summary also compares actual income against projected income targets, highlighting any discrepancies. Overall, the Income Summary helps users understand their financial inflows, track performance against income goals, and plan for future financial stability. Additionally, users can set and monitor income goals, and the system offers projections based on historical data and trends. The Income Summary integrates with other financial reports to provide a comprehensive view of overall financial health. Overall, the Income Summary helps users understand their financial inflows, track performance against income goals, and plan for future financial stability, ultimately aiding in better budgeting and financial decision-making.

![Figure 4: Income summary](image_placeholder_4)

Expense entry in the expense tracker management system involves creating a model to represent individual expenses, including fields such as the amount, description, date, and category as depicted in Figure 5. Users can input their expenses through a form or API endpoint, which validates the data and saves it to the database. Additionally, expense entry functionalities may include the ability to view, update, and delete existing expenses and features like filtering and sorting to analyze spending patterns. Additionally, expense entry functionalities include the ability to view, update, and delete existing expenses, and features like filtering and sorting to analyze spending patterns. Users can categorize expenses for more detailed tracking and apply tags for specific projects or events. The system also provides tools to generate expense reports and visualize spending trends over time.

![Figure 5: Expense entry](image_placeholder_5)

The income entry feature in the expense tracker management system enables users to easily record and manage their earnings. Users can input details such as the date, source, amount, and mode of payment for each income entry, ensuring accurate and comprehensive financial records as shown in Figure 6. They can also add descriptions and categorize their income to facilitate better tracking and analysis. Additionally, the system allows users to mark certain income entries as recurring, automating future entries and saving time. Once entered, the income details are saved and displayed in the income summary and transaction list, where users can view, edit, or delete entries as needed. This streamlined process helps users maintain an accurate overview of their financial inflows, aiding in budgeting and financial planning.

![Figure 6: Income entry](image_placeholder_6)

Expense categorization in the expense tracker management system allows users to classify their expenses into predefined categories for better organization and analysis. This involves creating a model for expense categories, which typically includes fields like name, description, and possibly a color or icon for visual distinction such as in Figure 7, it indicates shopping, food, rent and other. Users can assign categories to their expenses either manually or through automated rules. The system may provide features for managing categories, such as adding, editing, or deleting them, as well as reporting functionalities to track spending across different categories over time.

![Figure 7: Expense categorization](image_placeholder_7)

Figure 8 depicts the search and filter capabilities in the debt tracking system allow customers to effectively and efficiently identify their debts based on specific criteria. This includes using features that allow users to search for debt using keywords or phrases, filter debt by attributes such as date, category, price or description, and combine multiple filters to narrow down. The system may provide user interfaces such as a search bar, drop-down menu, or date picker to facilitate filter selection. Additionally, advanced filter options such as sorting by relevance or custom filter presets can improve user experience and productivity.

![Figure 8: Search and filtering](image_placeholder_8)

### Application Benefits

Our application outperforms other applications from the state-of-the-art discussed in the literature. Here are some points which outstand our application.

- **Advanced Analytics and Prediction**: Existing systems often provide basic data analysis and are limited to simple expense tracking. Our system leverages machine learning for advanced analytics and precise expense predictions, offering users a deeper understanding of their financial patterns.
- **Customizable Reporting**: Earlier solutions often offer limited customization for financial reports and categories. Our system provides extensive options for customizing categories, reports, and catering to diverse user needs and preferences.
- **User-Friendly Design**: Older systems might have complex interfaces. Our application features a simple, intuitive design, making it easy for users to navigate and use effectively.
- **Interactive Dashboards**: Existing solutions might offer static reports. Our system features interactive dashboards that allow users to explore their financial data through dynamic charts and graphs.

Our proposed ML based Expense Tracker Management System helps individuals and organizations manage finances by using machine learning to predict and analyze expenses. Its features offer valuable insights into spending patterns, benefiting personal finance enthusiasts, small businesses, and financial advisors by improving budgeting and financial planning. The findings from the Expense Tracker Management System demonstrate its effectiveness in predicting and analyzing expenses using machine learning. These insights are valuable for a broad audience, including individuals managing personal finances and small businesses optimizing budgets.

## CONCLUSION

Expense Tracker Management System provides individuals and businesses with effective solutions to track, analyze, and manage their spending through intuitive and powerful features such as categorization, fundraising, and advertising recommendations to present to users. Financial gaining control over their situation improving health clean budgeting and decisions access across multiple devices and improving accountability and transparency, especially in an environment where many people can integrate and share future expenses transactions can include scanning of receipts and instant integration with bank accounts Features such as syncing and spend-based personal financial advice are used as important tools to promote financial literacy, budgeting, and overall health for individuals and organizations.

To conclude, various machine learning techniques and ensemble methods like bagging, boosting, stacking, voting, and blending are employed for prediction. Among these, XGBoost achieves R-squared value of \(77.89\%\) the highest compared to other individual models, while the voting ensemble regressor surpasses other ensemble methods with the highest R-squared value of \(78.11\%\) and the lowest relative absolute error of 0.6121. The proposed approach helps to forecast future expenses by analyzing users' past spending patterns and behaviors. By leveraging historical data, these methods provide valuable insights into future financial needs and trends of any individual or business.

The future evolution of the Expense Tracker Management System holds promise for even greater innovation and impact. Potential enhancements may include integration with emerging technologies such as advanced artificial intelligence and machine learning, enabling predictive analytics for personalized financial insights and automated expense categorization. We aim to enhance application functionality and user experience by incorporating automated transaction tracking, cloud-based data synchronization, multi-language support, and AI-driven recommendations. We also aim in developing a dataset for expense tracker system to ensure that the dataset captures distinct and meaningful patterns, leading to better performance and more reliable predictions.
