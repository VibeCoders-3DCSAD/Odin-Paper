---
name: converted-paper
paper_id: "a3f5e2d1-4b7c-4e9f-8a2d-6c3e8b5f1d7a"
designation: international
title: "Evaluating Budgeting Apps: Limited Support for Budgeting Compared to Tracking"
authors: "Alenazi, M.; Sas, C."
year: 2023
venue: "BCS HCI 2023"
conversion_date: 2026-05-07
original_filename: "001_Alenazi_BCSHCI23.pdf"
version: "1.0"
---

# Evaluating Budgeting Apps: Limited Support for Budgeting Compared to Tracking

Financial behaviour is deeply embedded in our lives, yet for many people its success remains problematic. The need for supporting tools in this space is reflected in the growing number and popularity of budgeting apps, albeit limited research has focused on evaluating them. This paper describes a functionality review from the lens of mental accounting theory of 45 top- rated budgeting apps selected from 1335 apps on Google Play Store and Apple Store. Findings indicate that while all apps support tracking of transactions, one third of the apps do not support budgeting informed by money envelopes. We also report challenges regarding the meaning of key concepts of "accounts" and "transactions" for which we proposed novel design implications including a more nuanced vocabulary to talk about accounts and transaction types, new knowledge to have better support for budgeting through mental accounting theory and grounding budgeting as cognitive process in actual financial behaviour.

*Keywords*: Financial behaviours. Budgeting apps. Money envelopes

## 1. INTRODUCTION

HCI research on money and financial practices has focused mostly on exploratory studies (Kaye et al., 2014; Vines, Dunphy and Monk, 2014; Snow and Vyas, 2015b; Vyas et al., 2016; Lewis and Perry, 2019), whose findings indicate that people tend to use digital tools to a limited extent. As a result, we have little understanding of how digital tools such as mobile apps for personal budgeting could facilitate the tracking and monitoring of financial behaviours such as tracking and budgeting for daily expenditures. In addition to mobile banking, financial management apps supporting users to track expenses and create budgets, have also experienced rapid growth in the recent years as one of the fastest growing categories of finance apps (Bitrián, Buil and Catalán, 2021). In 2018, the global revenue for the such tools was over $1.4 million and estimated to at least double its value by 2025 (QYResearch, no date). While previous HCI research has explored functionalities of publicly available apps on marketplaces in domains such as fitness (Chung et al., 2018), diet (Zaidan and Roehrer, 2016), depression (Qu et al., 2020), personal goals (Lolla and Sas, 2023) or digital wellbeing (Almoallim and Sas, 2022), limited such work has looked at budgeting apps.

To address this gap, we explore the functionalities of top- rated budgeting apps by employing a mental accounting lens. Mental accounting is a behavioural economics theory (Thaler, 1999) according to which people commonly partition and budget money separately in mental accounts usually materialized through money envelopes for specific purposes. As the economist Thaler (Thaler, 1999) stated the main purpose of mental accounting is to use labelled categories for sources such as regular income and uses of funds such as food, to help individuals and households organize, track and monitor their spending. Our findings indicate insufficient support for budgeting functionality and important challenges of such apps due to the overlapping meanings and insufficient clarity of the key concepts. We discuss new design implications for addressing them including a more nuanced vocabulary to talk about accounts, transactions and budgeting, better support for budgeting in addition to tracking and in particular for multiple rather than single budgets.

## 2. BACKGROUND

Most HCI work on financial behaviour has focused on tracking such practices for individuals (Kaye et al., 2014; Vines, Dunphy and Monk, 2014; Lewis and Perry, 2019) and households (Snow and Vyas, 2015b, 2015a; Vyas et al., 2015, 2016) and their preferred tools. To track their spending, most of previous findings emphasize analogue tools such as coin jars (Snow and Vyas, 2015a; Vyas et al., 2016), enabling people to see how much they have spent. 2015a; Vyas et al., 2015) are also commonly used budgeting tools for monitoring expenses as their names reflect the purpose of money stored in specific envelopes, such as grocery money. There have been other common analogue tools for budgeting and tracking spending, such as wall organizers, bills attached to refrigerators, folders and handwritten diaries (Kaye et al., 2014; Snow and Vyas, 2015b, 2015a; Vyas et al., 2015, 2016), which are preferred due to their simplicity.

In contrast to such rich use of analogue tools, HCI research has reported limited digital tools supporting financial practices and in particular of budgeting apps. For instance, Snow and Vyas’s study (Snow and Vyas, 2015a) showed banking apps as more common digital tool for tracking financial transactions, with only one third of the 15 participants having used budgeting apps which they tend to discontinue after a short period of time due to the perceived challenge of entering expense and of lack of adequate control over their spending. Spreadsheets were another common tools mostly for tracking transactions (Kaye et al., 2014; Vyas et al., 2016), rather than budgeting purposes. Despite the growing HCI interest in personal finances, we have seen limited theoretical underpinning of such work, especially from the lens of mental accounting theory, although the value of behavioural economics has been previously suggested (Stockinger et al., 2013) for healthy choices (Lee, Kiesler and Forlizzi, 2011), digital wellbeing (Park, Lee and Park, 2021) or retirement savings (Gunaratne and Nov, 2015).

To summarize, HCI research on financial practices has highlighted mostly the use of analogue tools and limited use of digital ones, especially budgeting apps. Most of such work has also limitedly engaged the mental accounting theory (Thaler, 1999) despite initial acknowledgments of the value of behavioural economics in HCI.

## 3. METHOD

To identify the budgeting apps, we searched the two marketplaces in the UK: Google Play Store (for Android) and Apple Store (for iOS) using three keywords: budget, budgeting and finance. From the total of 1335 apps as shown in Figure 1, we removed duplicates, apps that were not free, apps not related to budgeting, those requiring access to one’s bank accounts and retained top- rated apps with an average rating score of four out of five and with at least 1000 reviews. This led to 45 apps being included in the analysis (Table 1, col 1): 21 apps available only on Google Play Store and 24 apps available on both platforms. The functionalities of these 45 apps were iteratively reviewed to identify functionalities, firstly through analysing all the apps’ descriptions, followed by expert evaluation. The analysis of apps’ descriptions, led to the identification of main functionalities such as tracking transactions and monitoring budgets. The limited information available in the apps’ descriptions was rather restricted to these broad functionalities.

For the expert evaluation we leveraged key concepts from mental accounting theory (Thaler, 1999) to identify functionalities pertaining to funds, i.e. sources and uses; expenditures and categories for grouping them and mental accounts or envelopes for allocating budgets to such categories. Additional functionalities identified in the reviewed apps include create transaction accounts, link the app to real bank account, as well as set date, time and currency for transactions. The identification of these functionalities involved iterations that the two authors discussed over several months.

While most functionalities were easily identified by each of them from apps’ descriptions, functionalities reflecting transactions and accounts required additional clarification reached through weekly conversations: transactions are to be considered broadly as encompassing income, expense and transfer of money between accounts. Other clarification concerned transaction accounts as containers holding each of the three types of transactions. Additional functionalities have been also identified through this iterative process, namely linking a transaction to a transaction account and differentiating existing categories for both income and expense categories. Appendix A shows the complete set of functionalities.

While analysis of the apps’ descriptions was completed by the first author, who also completed the expert evaluation of all 45 apps using Galaxy S21+. Second author also performed expert evaluation of five apps on an iPhone 12, in order to discuss and reconcile the identified functionalities. As the second author used iOS platform, these five apps were randomly selected from the 24 apps available on Apple Store.

## 4. RESULTS

The 45 identified apps belong mostly to Finance category on marketplaces (44 apps) and one app to Business category. Findings indicate different types of accounts and inconsistent terminology for labelling them. Outcomes also indicate two main types of budgeting apps, those that provide functionality of tracking expenses without monitoring (8 apps) and those that provide also, in addition to tracking expenses, the budgeting functionality for monitoring expenses against their allocated budget (33 apps). The latter use either single budget for all expenses irrespectively of their different categories (seven apps- Table 2, col 10) or multiple budgets using a different budget for each expense category such as bills, rent, groceries (26 apps- Table 2, col 11, albeit 4 of these provide budgeting only as premium, subscription-based functionality). Most of the apps show limited theoretical underpinning, with only two apps Goodbudget (Partners, no date) and SimpleBudget (Tanu, 2011) explicitly mentioning in their description that their design was informed by money envelope systems, albeit specific reference to mental accounting theory (Thaler, 1999) is not made. Also, no app’s description reports its evaluation though users’ studies.

![Figure 1: PRISMA diagram describing the process of apps’ selection.](image_placeholder_1)

> **Diagram text:**
> Identification
> Screening
> Included
> 404 apps excluded:
> Duplicated apps= 326 (Google Play: n=191, Apple Store: n=128, both: n= 7)
> Not free apps= 78 (Google Play: n=18, Apple Store: n= 60)
> 810 apps excluded:
> Apps with less than 1000 reviews and lower than 4.0 in rating score (Google Play: n=439, Apple Store: n= 371)
> 931 Remaining
> Google Play (n=533), Apple Store (n=398)
> 121 Remaining
> (Google Play: n= 94, Apple Store: n= 27)
> 71 apps excluded:
> Apps not related to budgeting (Google Play: n=44, Apple Store: n= 27)
> 50 Remaining
> (Google Play only)
> 1335 apps identified from
> Google Play (n= 742)
> Apple Store (n= 593)
> Eligible apps for analysis Google Play: n= 45
> 5 apps excluded:
> Apps required access to one’s bank account.

### 4.1 Accounts: Types and Terminology

A significant finding is the concept of accounts partially employed by our explored apps in order to support the organization of transactions. Mental accounting theory (Thaler, 1999) identifies three types of accounts, namely those for depositing and storing available funds such as monthly income (i.e. money-in), those for depositing and storing assets or wealth such as saving accounts and those for using or spending the available funds (i.e. money-out). With regard to the latter, the theory also specifies that people create mental accounts for allocating money for specific purposes or in other words for budgeting for specific categories of expenses, similar to money envelopes which will be discussed later. With regard to these three types of accounts proposed by mental accounting theory, findings indicate that most of the apps support depositing funds (44 apps) and paying for expenses (45 apps), with fewer apps support saving (11 apps- Table 2, col 3).

However, while most of the apps (41 apps- Table 2, col 2) have accounts for depositing funds or for paying for expenses, the remaining four apps (DAILY POCKET (Yjteam, 2017), EasyBudget (Letondor, 2015), Expense Tracker - Money Manager & Budget (Labs, 2019) and Budget App - Expense Tracker (HG Group Inc., 2020)) merely support the depositing of money on the app’s home screen rather than in dedicated income account. This is problematic as these four apps also fail to provide the option of linking individual transactions to specific accounts, as they are all stored directly on the home screen. Even for the remaining apps providing the option of creating income, saving or expense accounts, the income and expense, although conceptually distinct, they support the depositing and spending of the funds from the same container, respectively. In other words, for most of the apps, the income and expense accounts, although conceptually distinct, in practice they tend to be one and the same account similar to a bank account or a wallet where money are both deposited in and spent from.

Findings also indicate various terms for referring to such accounts, inconsistently used across the apps. The employed terminology appears to draw from two different sources: banking domain and everyday financial practices. A significant outcome is that most of the apps employed terms from banking domain for naming or labelling accounts. Such terms, used for income, saving or expense accounts, include: virtual bank accounts (nine apps), virtual cash accounts (17 apps), saving accounts (11 apps), investment accounts (seven apps), virtual credit card account (17 apps), virtual debit account (13 apps), with many apps (18 apps) employing more than one of these terms for organizing funds, wealth and expenses. While such terminology for banking domain can be useful as it builds on users’ familiarity with banking practices, the direct association with banking practices is limited since only seven apps support the integration of the budgeting apps with users’ online banking services and only as premium feature (Table 2, col 9). This terminology from banking domain also fails to provide specific types of expense accounts such as those for different categories of expenses or the equivalent of money envelopes (Thaler, 1999), since banking accounts capturing spending relate exclusively to debt repayment such as credit or debit card or mortgage, but not for instance to monthly grocery, bills or rent budgets.

Other terms to label accounts are borrowed from everyday financial practices and include wallet (three apps: Expense Tracker & Budget App (Estimate, 2019), Easy Home Finance (VoPo, 2015) and Spendee Budget & Money Tracker (A.s., 2013)), financial account (one app: Family budget- spending tracker (DigitLeaf, 2017)), payment account (one app - Money pro (LLC, 2017)) or even budget (two apps: Budget: Budget and expense tracking app (Connell, 2017) and Home Budget - Money Manager (Softs, no date)). Interestingly, with respect to terms from everyday practices, findings indicate that clear ones for distinguishing among available funds, wealth and expense accounts or between money- in and money- out are not employed by any of the apps except one app: GnuCash which uses multiple accounts such as income, expenses and assets.

### 4.2 Creating and Tracking Transactions: Income, Expenses, Transfer

Study findings also highlight the important distinction between accounts and transactions. We suggest that accounts are similar to containers for the organization of transactions, while each transaction represents the movement of money from a source to a destination, in other words, transactions are the ones that allow accounts to be replenished with funds or depleted of funds. Findings indicate three types of transactions for (i) depositing funds, (ii) paying for expenses or (iii) transferring money from income to expense accounts which are further detailed. All apps apart from one app (SimpleBudget: Envelope Budget) allow users to deposit funds, through income transactions (44 apps- Table 1, col 2) by specifying the name or label of the transactions, usually referring to the source of money such as salary, together with the specific amount of money being deposited, the date (all but two apps- Table 1, col 5) and time (18 apps- Table 1, col 6) of the income transaction and its currency (40 apps - Table 1, col 4).

From the 40 apps supporting the specification of the currency of deposited funds, 12 apps provide a predefined list of currencies allowing users to choose different one for each income transaction being created, while 28 apps provide a pre- defined list of currencies albeit in the app settings so each transaction with a different currency requires changing it in the app setting. These two options prioritize either the ease of changing currency or of keeping it constant across transactions. Unlike the rest of the apps, SimpleBudget app does not support the creation of an income account; instead, it supports users to create multiple envelopes, each with its own budget or available fund, without specifying the total amount of available funds to be allocated across all the envelopes. This can be problematic in terms of the cognitive load needed to ensure that the available funds not captured by the app, do not exceed the cumulative value of the money envelopes.

With respect to expense transactions, all apps support users to create them (Table 1, col 7), by specifying the names or labels of these transactions, usually the destination of money such as grocery expense, together with the specific amount of money being paid (45 apps), the date (45 apps- Table 1, col 10) and time (18 apps- Table 1, col 11) of the expense transaction and its currency (41 apps - Table 1, col 9) with similar ease of changing currency or of keeping constant characterizing income transactions. Finding show that four apps also allow the specification of the payment method for expense transactions, i.e., cash, credit/debit card or cheque.

With respect to the mode of entering the transactions, most apps support the creation of both income and expense transactions through the same interaction by tapping on the plus icon on app’s home screen (35 apps), by clicking on income button or expense button on the app’s home screen (eight apps) or by tapping on “register” button on app’s home screen which opens another page to create the income or expense (one app - MoneyWise (North, 2011). One remaining app (CoinKeeper: expense, money manager, budget planner) provides different interactions for entering income, i.e., by tapping on the plus icon on app’s home screen and for entering expense, i.e., by dragging a transaction account icon into expense category then specify the expense amount from the dragged account. Arguably, the simple interaction for tapping on the plus icon on app’s home screen to enter both income and expense transaction is preferrable in terms of increased usability.

In addition to income and expense transactions, findings also indicate the third type, namely transfer transactions (35 apps- Table 2, col 5), which we define as transfer of money from a source (available income) to a destination (for expense or saving). In addition to specifying source and destination accounts (35 apps), transfer transactions could also specify the amount of money being transferred (35 apps), transfer date (30 apps- Table 2, col 6), time (11 apps- Table 2, col 7), currency (25 apps) as well as label or receipt which can be attached to the transfer (five apps and three apps premium- Table 2, col 8). Interestingly, most of the apps supporting transfer transactions allow them without sufficient funds in the source account (33 apps out of 35). Two exceptions include the Family budget- spending tracker app, where if the transferred amount is larger than the available funds, the message of “insufficient amount” is shown in red colour and the transfer cannot be completed. For the other app (MoneyWise), the transfer transaction is a premium feature.

An important finding is that similar transactions can also be grouped in categories, for both income and expenses transactions. This functionality aligns with the cognitive operations of grouping different income and expenditures into categories mentioned by the mental accounting theory (Thaler, 1999). These categories could be of two types: provided by the app or defined by the user. The former consists of a list of categories for income such as salary, bonus, gift, refund, business and interest (38/45 apps) and for expense (40/45 apps) such as grocery, shopping, transportation, bills, education and rent. The user defined categories allow users to specify new ones if those provided by the app are not adequate, both for income (36/45 apps and two apps premium) and for expense transactions (42/45 apps and one app premium) and once crated, these categories could be re- used later with new transactions. However, some apps provide the limited option of one- off categories for income (four apps) and expense (two apps). Therefore, with each new transaction, the user needs to enter the source of income and the expense name. While most apps provided one level of categories, 15 apps provided option for subcategories of transactions. For example, car expense category can have subcategories such as fines, fuel, parking and repairs.

Finally, all transactions can be entered manually (45 apps), they can also be automatically imported from online banking accounts linked to the budgeting app (seven apps), with few apps encouraging users to compare their entered transactions with those of their bank statements (seven apps).

### 4.3 Budgeting: Tracking Balance vs Money Envelopes

Findings indicate that all apps support budgeting functionality and therefore the monitoring of expenses against the allocated budgets (45 apps), although they do so in different ways. While most of these apps support budgeting under mental accounts or money envelopes (26 apps), others do not (19 apps). We called the latter form of budgeting as single budget and the former as multiple budgets, as further detailed.

Apps supporting single budget (19 apps) rely on only one main budget (usually the same amount as the available funds) from which all expenses are to be covered. In these apps, expense transactions are not grouped under specific money envelopes with allocated budgets for each envelope, which would be consistent with mental accounting theory (Thaler, 1999). Although these apps have a single budget, they do support a high- level monitoring of expenses and do so in two ways. While all 19 apps use the account balance to represent the overspent of available funds using the minus symbol, eight apps do not change the colour of this information, albeit seven apps use colour red to provide this information of overspent.

Although single budget apps depend on the total funds, some of these apps allow to set that fund as explicit budget for all expense (five out of 19 apps). These five apps do not have a specific budget name by the user, it was named by the app as budget and the user can set the budget amount and budget period (Table 2, col 13) as daily (one app - Spending Tracker), weekly (two apps - DAILY POCKET - Budget Manager and Spending Tracker), monthly (four apps), yearly (one app - Spending Tracker) or defined by the user (one app - Monny).

## 5. DISCUSSION

### 5.1 Nuanced Vocabulary for Accounts and Transactions

### 5.2 Nuanced Vocabulary for Budgeting

### 5.3 Supporting Budgeting through Money Envelopes

### 5.4 Grounding Budgeting as Cognitive Process in Actual Financial Behaviour

through the amount being budgeted, budget name and budget period using both system- and userdefined periods, although not all apps provide support for each of these details. We suggest that budgeting apps support such a complete definition of budgets and their allocation to specific expense categories. Although the use of envelopes and jars has been noticed in previous HCI work on financial practices (Snow and Vyas, 2015a; Vyas et al., 2015, 2016), this was mostly as a way to store money for specific purposes, rather than for digital materialization of mental accounts. Therefore, we strongly call for better design for budgeting app articulating the concept of mental accounting and support the use of money envelopes with allocated budget to help users organize, track and more importantly keep their spending under control.

Budgeting apps support the tracking of expenses and monitoring them against available funds or allocated budget. Such functions however prioritize cognitive operations rather than the financial behaviours themselves. This is reflected in the small number of budgeting apps integrating online banking to support for instance automatic import of the real transactions. This indicates limited support for encouraging users to compare their entered transactions with those in bank statements. Such grounding in actual financial behaviours is crucial for infusing practical value and realism to the otherwise cognitive exercise of budgeting. We suggest the use of clear terminology differentiating banking accounts and transactions from those created in the budgeting app.

## 6. CONCLUSION

We report on functionality review of 45 top- rated budgeting apps. Findings suggest the value of more nuanced vocabulary for describing the key concepts of accounts, transactions and budgets as informed by mental accounting theory and for differentiating between tracking the transactions and monitoring the allocated budgets through money envelopes. We conclude with four design implications for financial technologies such as budgeting apps including clear definitions of accounts and transaction and their different types, supporting budgeting through money envelopes and for grounding budgeting as cognitive process in financial behaviour.

## ACKNOWLEDGMENTS

First author’s work was supported by Taibah University, Saudi Arabia and the Saudi Arabian Cultural Bureau, London.

## REFERENCES

- A.s., S. (2013) Spendee Budget & Money Tracker, Google Play. Available at: https://play.google.com/store/apps/details?id=com.cleevio.spendee (Accessed: 1 April 2022).
- Almoallim, S. and Sas, C. (2022) ‘Toward ResearchInformed Design Implications for Interventions Limiting Smartphone Use: Functionalities Review of Digital Well- being Apps’, *JMIR Formative Research*, 6(4). doi: 10.2196/31730.
- Bitrián, P., Buil, I. and Catalán, S. (2021) ‘Making finance fun: the gamification of personal financial management apps’, *International Journal of Bank Marketing*, 39(7), pp. 1310-1332. doi: 10.1108/IJBM-02-2021-0074.
- Chung, A. E. et al. (2018) ‘Health and fitness apps for hands- free voice- activated assistants: Content analysis’, *JMIR mHealth and uHealth*, 6(9), pp. 1-13. doi: 10.2196/mhealth.9705.
- Connell, D. (2017) Fudget: Budget and expense tracking app, Google Play. Available at: https://play.google.com/store/apps/details?id=com.dannyconnell.android.fudget (Accessed: 1 April 2022).
- DigitLeaf, Ilc (2016) Budget planner- Expense tracker, Google Play. Available at: https://play.google.com/store/apps/details?id=com.colpit.diamondcoming.isavemoney (Accessed: 1 April 2022).
- DigitLeaf, L. (2017) Family budget- spending tracker, Google Play. Available at: https://play.google.com/store/apps/details?id=com.colpit.diamondcoming.isavemoney (Accessed: 1 April 2022).
- Estimate, B.- B. (2019) Expense Tracker & Budget App, Google Play. Available at: https://play.google.com/store/apps/details?id=expense.tracker.income.receipt.budget (Accessed: 1 April 2022).
- Gunaratne, J. and Nov, O. (2015) ‘Informing and improving retirement saving performance using behavioral economics theory- driven user interfaces’, *Conference on Human Factors in Computing Systems - Proceedings*, 2015-April, pp. 917-920. doi: 10.1145/2702123.2702408.
- HG Group Inc. (2020) Budget App - Expense Tracker, Google Play. Available at: https://play.google.com/store/apps/details?id=com.hg.moneymanager.budgetapp (Accessed: 1 April 2022).
- Kaye, J. J. et al. (2014) ‘Money talks: Tracking personal finances’, *Conference on Human Factors in Computing Systems - Proceedings*, pp. 521-530. doi: 10.1145/2556288.2556975.
- Labs, V. (2019) Expense Tracker - Money Manager & Budget, Google Play. Available at: https://play.google.com/store/apps/details?id=com.vlab.expense.tracker (Accessed: 1 April 2022).
- Lee, M. K., Kiesler, S. and Forlizzi, J. (2011) ‘Mining behavioral economics to design persuasive technology for healthy choices’, *Conference on Human Factors in Computing Systems - Proceedings*, pp. 325-334. doi: 10.1145/1978942.1978989.
- Letondor, B. (2015) EasyBudget - Personal budget planning made simple, Google Play. Available at: https://play.google.com/store/apps/details?id=com.benoitletondor.easybudgetapp (Accessed: 1 April 2022).
- Lewis, M. and Perry, M. (2019) ‘Follow the money: Managing personal finance digitally’, *Conference on Human Factors in Computing Systems - Proceedings*, pp. 1-14. doi: 10.1145/3290605.3300620.
- LLC, Ib. (2017) Money pro, Google Play. Available at: https://play.google.com/store/apps/details?id=com.ibearsoft.moneyproandroid (Accessed: 1 April 2022).
- Lolla, S. and Sas, C. (2023) ‘Evaluating Mobile Apps Targeting Personal Goals’, *Conference on Human Factors in Computing Systems - Proceedings*. doi: 10.1145/3544549.3585725
- North, H. (2011) MoneyWise, Google Play. Available at: https://play.google.com/store/apps/details?id=com.handyorth.moneywise_free (Accessed: 1 April 2022).
- Park, J., Lee, H. and Park, S. (2021) ‘Goldentime: Exploring system- driven timeboxing and micro- financial incentives for self- regulated phone use’, *Conf. on Human Factors in Computing Systems - Proceedings*. doi: 10.1145/3411764.3445489.
- Partners, D. (no date) Goodbudget: Budget & Finance, Google Play. Available at: https://play.google.com/store/apps/details?id=com.dayspringtech.envelopes (Accessed: 1 April 2022).
- Qu, C. et al. (2020) ‘Functionality of top- rated mobile apps for depression: Systematic search and evaluation’, *JMIR Mental Health*, 7(1), pp. 1-13. doi: 10.2196/15321.
- QYResearch (no date) Global Personal Financial Management Tools Market Size, Status and Forecast 2019-2025. Available at: https://www.marketresearch.com/QYResearch-Group-v3531/Global-Personal-Financial-Management-Tools-12732938/ (Accessed: 26 December 2022).
- Snow, S. and Vyas, D. (2015a) ‘Fixing the alignment: An exploration of budgeting practices in the home’, *Conference on Human Factors in Computing Systems - Proceedings*, 18, pp. 2271-2276. doi: 10.1145/2702613.2732808.
- Snow, S. and Vyas, D. (2015b) ‘Fostering collaboration in the management of family finances’, *OzCHI 2015: Being Human - Conference Proceedings*, pp. 380-387. doi: 10.1145/2838739.2838746.
- Softs, E. (no date) Home Budget - Money Manager, Google Play. Available at: https://play.google.com/store/apps/details?id=com.easysoftsalahi.app.appFree (Accessed: 1 April 2022).
- Stockinger, T. et al. (2013) ‘SmartPiggy: A piggy bank that talks to your smartphone’, *Proceedings of the 12th International Conference on Mobile and Ubiquitous Multimedia, MUM 2013*, 43, pp. 5-6. doi: 10.1145/2541831.2541869.
- Tanu, F. (2011) SimpleBudget (Envelope Budget), Google Play. Available at: https://play.google.com/store/apps/details?id=com.simplebudget (Accessed: 1 April 2022).
- Thaler, R. H. (1999) ‘Mental accounting matters’, *Journal of Behavioral Decision Ma*, 206(September 1998), pp. 241-268. doi: 10.1017/CBO9780511803475.015.
- Vines, J., Dunphy, P. and Monk, A. (2014) ‘Pay or delay: The role of technology when managing a low income’, *Conference on Human Factors in Computing Systems - Proceedings*, pp. 501-510. doi: 10.1145/2556288.2556961.
- VoPo (2015) Easy Home Finance, Google Play. Available at: https://play.google.com/store/apps/details?id=voPo.easyhomefinance (Accessed: 1 April 2022).
- Vyas, D. et al. (2015) ‘Being thrifty on a $100K wage: Austerity in family finances’, *Proceedings of the ACM Conference on Computer Supported Cooperative Work, CSCW*, 2015-Janua, pp. 167-170. doi: 10.1145/2685553.2698998.
- Vyas, D. et al. (2016) ‘Social organization of household finance: Understanding artful financial systems in the home’, in *Proceedings of the ACM Conference on Computer Supported Cooperative Work, CSCW*. Association for Computing Machinery, pp. 1777-1789. doi: 10.1145/2818048.2819937.
- Yjteam (2017) DAILY POCKET - Budget Manager, Google Play. Available at: https://play.google.com/store/apps/details?id=kr.co.yjetam.dailypay (Accessed: 1 April 2022).
- Zaidan, S. and Roehrer, E. (2016) ‘Popular mobile phone apps for diet and weight loss: A content analysis’, *JMIR mHealth and uHealth*, 4(3). doi: 10.2196/mhealth.5406.

## Appendix A

### Table 1: The main functionalities and subfunctionalities of funds and expenses for the 45 top-rated budgeting apps.

<table>
<thead>
<tr><th rowspan="2">App name</th><th colspan="5">Tracking transaction: funds</th><th colspan="5">Tracking transaction: expenses</th></tr>
<tr><th>Create Funds</th><th>Create Funds category</th><th>Enter funds currency</th><th>Set funds date</th><th>Set funds time</th><th>Create Expense</th><th>Create expense category</th><th>Enter expense currency</th><th>Set date for expense</th><th>Set time for expense</th></tr>
</thead>
<tbody>
<tr><td>1Money (PixelRush, 2017)</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td></tr>
<tr><td>Alzex Finance (Anna Shirokova, 2015)</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td></td></tr>
<tr><td>AndroMoney (AndroMoney, 2011)</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td></td></tr>
<tr><td>Bills Reminder (TimelyBills, 2015)</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td></tr>
<tr><td>Bluecoins Finance (Mabuhay Software, 2016)</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td></td></tr>
<tr><td>Budget App (HG Group Inc., 2020)</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td></td></tr>
<tr><td>Budget planner (DigitLeaf, 2016)</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td></tr>
<tr><td>CoinKeeper (LLC, 2015)</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td></td></tr>
<tr><td>DAILY POCKET (Yjteam, 2017)</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td></tr>
<tr><td>Easy Home (VoPo, 2015)</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td></td></tr>
<tr><td>EasyBudget (Letondor, 2015)</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td></td></tr>
<tr><td>Expense Manager (Bishinwens, 2010)</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td></tr>
<tr><td>Expense Manager (Manager, 2012)</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td></td></tr>
<tr><td>Expense Tracker (Labs, 2019)</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td></td></tr>
<tr><td>Expense Tracker (Estimate, 2019)</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td></td></tr>
<tr><td>Expense Tracker (Tracker, 2016)</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td></tr>
<tr><td>Family budget (DigitLeaf, 2017)</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td></tr>
<tr><td>Fast Budget (SRL, 2014)</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td></tr>
<tr><td>Fudget (Connell, 2017)</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td></tr>
<tr><td>GnuCash (GnuCash, 2012)</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td></td></tr>
<tr><td>Goodbudget (Partners, no date)</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td></td></tr>
<tr><td>Home Budget (Softs, no date)</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td></td></tr>
<tr><td>Home Budget (SIRI, 2013)</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td></td></tr>
<tr><td>Home Finance (SoftMobile, 2015)</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td></td></tr>
<tr><td>Income Expense (SARAF, 2019)</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td></td></tr>
<tr><td>Mobilis (M. Inc., 2013)</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td></td></tr>
<tr><td>Money (Reflectly, 2014)</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td></td></tr>
<tr><td>Money Manager (R. Inc., 2013)</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td></td></tr>
<tr><td>Money manager (Exp, 2020)</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td></td></tr>
<tr><td>Money Manager (Apps, 2014)</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td></td></tr>
<tr><td>Money pro (LLC, 2017)</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td></td></tr>
<tr><td>Money Tracker (Notes, 2021)</td><td>√</td><td>√</td><td>√</td><td>√</td><td></td><td>√</td><td>√</td><td>√</td><td>√</td><td></td></tr>
<tr><td>Money+ (Studios, 2020)</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td></td></tr>
<tr><td>MoneyWise (North, 2011)</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td></td></tr>
<tr><td>Monny (Greamer, 2017)</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td></td></tr>
<tr><td>Monthly Expenses (Baruah, 2016)</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td></td></tr>
<tr><td>My Expenses (Totschnig, 2012)</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td></td></tr>
<tr><td>My Finances (7csolutions, 2015)</td><td>√</td><td>√</td><td>√</td><td>√</td><td></td><td>√</td><td>√</td><td>√</td><td>√</td><td></td></tr>
<tr><td>SimpleBudget (Tanu, 2011)</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td></td></tr>
<tr><td>Spendee Budget (A.s., 2013)</td><td>√</td><td>√</td><td>√</td><td>√</td><td></td><td>√</td><td>√</td><td>√</td><td>√</td><td></td></tr>
<tr><td>Spending Tracker (Ltd, 2014)</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td></td></tr>
<tr><td>Tosh Finance (Inc., no date)</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td></td></tr>
<tr><td>Vault (Tubin, 2013)</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td></td></tr>
<tr><td>Wallet (BudgetBakers, 2011)</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td></td></tr>
<tr><td>YNAB (YouNeedABudget, 2015)</td><td>√</td><td>√</td><td>√</td><td>√</td><td></td><td>√</td><td>√</td><td>√</td><td>√</td><td></td></tr>
</tbody>
</table>

### Table 2: The main functionalities and subfunctionalities of transaction accounts, transfer between them, and the types of provided budgets of the 45 top-rated budgeting apps (* refers to the premium feature in the apps).

<table>
<thead>
<tr><th rowspan="2">App name</th><th rowspan="2">Transaction account</th><th rowspan="2">Saving account</th><th rowspan="2">Link transaction</th><th colspan="4">Transfer between accounts</th><th rowspan="2">Link app to bank</th><th colspan="3">Monitoring budgets</th></tr>
<tr><th>Transfer</th><th>Set date for transfer</th><th>Set time for transfer</th><th>Transaction receipt</th><th>Create single budget</th><th>Create multiple budget</th><th>Set budget period</th></tr>
</thead>
<tbody>
<tr><td>1Money (PixelRush, 2017)</td><td>√</td><td></td><td></td><td>√</td><td>√</td><td>√</td><td></td><td></td><td>√</td><td></td><td></td></tr>
<tr><td>Alzex Finance (Anna Shirokova, 2015)</td><td>√</td><td>√</td><td></td><td>√</td><td>√</td><td>√</td><td></td><td></td><td>√</td><td></td><td>√</td></tr>
<tr><td>AndroMoney (AndroMoney, 2011)</td><td>√</td><td>√</td><td></td><td>√</td><td>√</td><td>√</td><td></td><td></td><td>√</td><td></td><td></td></tr>
<tr><td>Bills Reminder (TimelyBills, 2015)</td><td>√</td><td>√</td><td></td><td>√</td><td>√</td><td>√</td><td></td><td></td><td>√</td><td></td><td></td></tr>
<tr><td>Bluecoins Finance (Mabuhay Software, 2016)</td><td>√</td><td>√</td><td></td><td>√</td><td>√</td><td>√</td><td></td><td></td><td>√</td><td></td><td>√</td></tr>
<tr><td>Budget App (HG Group Inc., 2020)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>√</td><td></td><td></td></tr>
<tr><td>Budget planner (DigitLeaf, 2016)</td><td>√</td><td></td><td></td><td>√</td><td>√</td><td>√</td><td></td><td></td><td>√</td><td></td><td>√</td></tr>
<tr><td>CoinKeeper (LLC, 2015)</td><td>√</td><td>√</td><td></td><td>√</td><td>√</td><td></td><td>√</td><td></td><td>√</td><td></td><td>√</td></tr>
<tr><td>DAILY POCKET (Yjteam, 2017)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>√</td><td></td><td>√</td></tr>
<tr><td>Easy Home (VoPo, 2015)</td><td>√</td><td></td><td></td><td>√</td><td></td><td></td><td></td><td></td><td>√</td><td></td><td></td></tr>
<tr><td>EasyBudget (Letondor, 2015)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>√</td><td></td><td>√</td></tr>
<tr><td>Expense Manager (Bishinwens, 2010)</td><td>√</td><td></td><td></td><td>√</td><td>√</td><td>√</td><td></td><td></td><td>√</td><td></td><td></td></tr>
<tr><td>Expense Manager (Manager, 2012)</td><td>√</td><td>√</td><td></td><td>√</td><td>√</td><td>√</td><td></td><td></td><td>√</td><td></td><td></td></tr>
<tr><td>Expense Tracker (Labs, 2019)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>√</td><td></td><td></td></tr>
<tr><td>Expense Tracker (Estimate, 2019)</td><td>√</td><td></td><td></td><td>√</td><td>√</td><td>√</td><td></td><td></td><td>√</td><td></td><td>√</td></tr>
<tr><td>Expense Tracker (Tracker, 2016)</td><td>√</td><td>√</td><td></td><td>√</td><td>√</td><td>√</td><td></td><td></td><td>√</td><td></td><td>√</td></tr>
<tr><td>Family budget (DigitLeaf, 2017)</td><td>√</td><td></td><td></td><td>√</td><td>√</td><td>√</td><td></td><td></td><td>√</td><td></td><td>√</td></tr>
<tr><td>Fast Budget (SRL, 2014)</td><td>√</td><td></td><td></td><td>√</td><td>√</td><td>√</td><td></td><td>*</td><td>√</td><td>*</td><td></td></tr>
<tr><td>Fudget (Connell, 2017)</td><td>√</td><td></td><td></td><td>√</td><td>√</td><td>√</td><td></td><td></td><td>√</td><td></td><td>√</td></tr>
<tr><td>GnuCash (GnuCash, 2012)</td><td>√</td><td>√</td><td></td><td>√</td><td>√</td><td>√</td><td></td><td></td><td>√</td><td></td><td>√</td></tr>
<tr><td>Goodbudget (Partners, no date)</td><td>√</td><td></td><td></td><td>√</td><td>√</td><td></td><td></td><td></td><td></td><td>√</td><td>√</td></tr>
<tr><td>Home Budget (Softs, no date)</td><td>√</td><td></td><td></td><td>√</td><td>√</td><td>√</td><td></td><td></td><td>√</td><td></td><td></td></tr>
<tr><td>Home Budget (SIRI, 2013)</td><td>√</td><td>√</td><td></td><td>√</td><td>√</td><td>√</td><td></td><td></td><td>√</td><td></td><td>√</td></tr>
<tr><td>Home Finance (SoftMobile, 2015)</td><td>√</td><td>√</td><td></td><td>√</td><td>√</td><td>√</td><td></td><td></td><td>√</td><td></td><td>√</td></tr>
<tr><td>Income Expense (SARAF, 2019)</td><td>√</td><td></td><td></td><td>√</td><td>√</td><td>√</td><td></td><td></td><td>√</td><td></td><td>√</td></tr>
<tr><td>Mobilis (M. Inc., 2013)</td><td>√</td><td></td><td></td><td>√</td><td>√</td><td>√</td><td></td><td></td><td>√</td><td></td><td>√</td></tr>
<tr><td>Money (Reflectly, 2014)</td><td>√</td><td></td><td></td><td>√</td><td>√</td><td>√</td><td></td><td></td><td>√</td><td></td><td>√</td></tr>
<tr><td>Money Manager (R. Inc., 2013)</td><td>√</td><td>√</td><td></td><td>√</td><td>√</td><td>√</td><td></td><td></td><td>√</td><td></td><td>√</td></tr>
<tr><td>Money manager (Exp, 2020)</td><td>√</td><td>√</td><td></td><td>√</td><td>√</td><td>√</td><td></td><td></td><td>√</td><td></td><td>√</td></tr>
<tr><td>Money Manager (Apps, 2014)</td><td>√</td><td>√</td><td></td><td>√</td><td>√</td><td>√</td><td></td><td></td><td>√</td><td></td><td>√</td></tr>
<tr><td>Money pro (LLC, 2017)</td><td>√</td><td></td><td>*</td><td>√</td><td>√</td><td>√</td><td></td><td>*</td><td>√</td><td></td><td>*</td></tr>
<tr><td>Money Tracker (Notes, 2021)</td><td>√</td><td>√</td><td></td><td>√</td><td>√</td><td>√</td><td></td><td></td><td>√</td><td></td><td></td></tr>
<tr><td>Money+ (Studios, 2020)</td><td>√</td><td>√</td><td></td><td>√</td><td>√</td><td>√</td><td></td><td>*</td><td>√</td><td></td><td>√</td></tr>
<tr><td>MoneyWise (North, 2011)</td><td>√</td><td></td><td>*</td><td>*</td><td>*</td><td>*</td><td></td><td>*</td><td></td><td>*</td><td>*</td></tr>
<tr><td>Monny (Greamer, 2017)</td><td>√</td><td></td><td></td><td>√</td><td>√</td><td>√</td><td></td><td></td><td>√</td><td></td><td>√</td></tr>
<tr><td>Monthly Expenses (Baruah, 2016)</td><td>√</td><td></td><td></td><td>√</td><td>√</td><td>√</td><td></td><td></td><td>√</td><td></td><td>√</td></tr>
<tr><td>My Expenses (Totschnig, 2012)</td><td>√</td><td></td><td></td><td>√</td><td>√</td><td>√</td><td></td><td>*</td><td>√</td><td></td><td>*</td></tr>
<tr><td>My Finances (7csolutions, 2015)</td><td>√</td><td>√</td><td></td><td>√</td><td>√</td><td>√</td><td></td><td></td><td>√</td><td></td><td>√</td></tr>
<tr><td>SimpleBudget (Tanu, 2011)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>√</td><td>√</td></tr>
<tr><td>Spendee Budget (A.s., 2013)</td><td>√</td><td></td><td></td><td>√</td><td>√</td><td></td><td></td><td>*</td><td>√</td><td></td><td>*</td></tr>
<tr><td>Spending Tracker (Ltd, 2014)</td><td>√</td><td>√</td><td></td><td>√</td><td>√</td><td>√</td><td></td><td></td><td>√</td><td></td><td>√</td></tr>
<tr><td>Tosh Finance (Inc., no date)</td><td>√</td><td></td><td></td><td>√</td><td>√</td><td>√</td><td></td><td></td><td>√</td><td></td><td>√</td></tr>
<tr><td>Vault (Tubin, 2013)</td><td>√</td><td></td><td></td><td>√</td><td>√</td><td>√</td><td></td><td></td><td>√</td><td></td><td>√</td></tr>
<tr><td>Wallet (BudgetBakers, 2011)</td><td>√</td><td>√</td><td></td><td>√</td><td>√</td><td>√</td><td></td><td>*</td><td>√</td><td></td><td>√</td></tr>
<tr><td>YNAB (YouNeedABudget, 2015)</td><td>√</td><td>√</td><td></td><td>√</td><td>√</td><td>√</td><td></td><td></td><td>√</td><td></td><td>√</td></tr>
</tbody>
</table>

### App references (from Appendix)

- 7csolutions (2015) My Finances, Google Play. Available at: https://play.google.com/store/apps/details?id=com.sevencolutions.myfinances (Accessed: 1 April 2022).
- AndroMoney (2011) AndroMoney (Expense Track), Google Play. Available at: https://play.google.com/store/apps/details?id=com.kpmoney.android (Accessed: 1 April 2022).
- Anna Shirokova (2015) Alzex Finance, Google Play. Available at: https://play.google.com/store/apps/details?id=com.alzex.finance (Accessed: 1 April 2022).
- Apps, A. P. (2014) Money Manager: AZV Money Pro, Google Play. Available at: https://play.google.com/store/apps/details?id=com.m.azv.money (Accessed: 1 April 2022).
- Baruah, B. (2016) Monthly Expenses: Manage Money, Google Play. Available at: https://play.google.com/store/apps/details?id=com.m.kaushikbaruah.quickexpensemanagerfree (Accessed: 1 April 2022).
- Bishinews (2010) Expense Manager, Google Play. Available at: https://play.google.com/store/apps/details?id=com.m.expressmanager (Accessed: 1 April 2022).
- BudgetBakers (2011) Wallet: Budget Planner Tracker, Google Play. Available at: https://play.google.com/store/apps/details?id=com.droid4you.application.wallet (Accessed: 1 April 2022).
- DigitLeaf, Ilc (2016) Budget planner- Expense tracker, Google Play. Available at: https://play.google.com/store/apps/details?id=com.colpit.diamondcoming.isavemoney (Accessed: 1 April 2022).
- Exp, I. M. (2020) Money manager, expense tracker, budget, wallet, Google Play. Available at: https://play.google.com/store/apps/details?id=ru.i.nnim.my_finance (Accessed: 1 April 2022).
- GnuCash (2012) GnuCash, Google Play. Available at: https://play.google.com/store/apps/details?id=org.gnucash.android (Accessed: 1 April 2022).
- Greamer (2017) Monny, Google Play. Available at: https://play.google.com/store/apps/details?id=com.greamer.monny.android (Accessed: 1 April 2022).
- Inc., M. (2013) Mobills: Budget Planner, Google Play. Available at: https://play.google.com/store/apps/details?id=br.com.gerenciadorfinanceiro.controller (Accessed: 1 April 2022).
- Inc., R. (2013) Money Manager Expense & Budget, Google Play. Available at: https://play.google.com/store/apps/details?id=com.realbyteapps.moneymanagerfree (Accessed: 1 April 2022).
- Inc., T. (no date) Tosh Finance - Personal Budget & Expense Tracker, Google Play. Available at: https://play.google.com/store/apps/details?id=com.m.thirdframestudios.android.expensoor (Accessed: 1 April 2022).
- LLC, D. (2015) CoinKeeper: expense, money manager, budget planner, Google Play. Available at: https://play.google.com/store/apps/details?id=com.disrapp.coinkeeper.material (Accessed: 1 April 2022).
- Ltd, M. R. (2014) Spending Tracker, Google Play. Available at: https://play.google.com/store/apps/details?id=com.m.mhriley.spendingtracker (Accessed: 1 April 2022).
- Mabuhay Software (2016) Bluecoins Finance: Budget, Mon, Google Play. Available at: https://play.google.com/store/apps/details?id=com.m.rammigsoftware.bluecoins (Accessed: 1 April 2022).
- Manager, H. E. (2012) Expense Manager, Google Play. Available at: https://play.google.com/store/apps/details?id=mediavision.handwallet (Accessed: 1 April 2022).
- Notes, Q. S. & Q. C. G. & R. & (2021) Money Tracker: Expense Tracker, Wallet, Budget App, Google Play. Available at: https://play.google.com/store/apps/details?id=moneytracker.expensetracker.budgetplanner.spendingtracker (Accessed: 1 April 2022).
- PixelRush (2017) 1Money: expense tracker budget, Google Play. Available at: https://play.google.com/store/apps/details?id=org.pixelrush.moneyiq (Accessed: 1 April 2022).
- Reflectly (2014) Money - Budget Manager and Expense Tracker app, Google Play. Available at: https://play.google.com/store/apps/details?id=com.money.app.lite (Accessed: 1 April 2022).
- SARAF, A. (2019) Income Expense- daily expenses, Google Play. Available at: https://play.google.com/store/apps/details?id=incomeexpense.incomeexpense&hl=en_GB&gl=US (Accessed: 1 April 2022).
- SIRI (2013) Home Budget Manager Lite With Sync, Google Play. Available at: https://play.google.com/store/apps/details?id=com.siri.budgetdemo (Accessed: 1 April 2022).
- SoftMobile (2015) Home Finance, Google Play. Available at: https://play.google.com/store/apps/details?id=com.mec.homefinance (Accessed: 1 April 2022).
- SRL, A. (2014) Fast Budget - Expense Manager, Google Play. Available at: https://play.google.com/store/apps/details?id=com.mblodhgard.easybudget (Accessed: 1 April 2022).
- Studios, Z. (2020) Money+ Cute Expense Tracker, Google Play. Available at: https://play.google.com/store/apps/details?id=com.mzotiger.accountbook (Accessed: 1 April 2022).
- TimelyBills (2015) Bills Reminder, Budget Planner, Google Play. Available at: https://play.google.com/store/apps/details?id=in.usefulapp.timelybills (Accessed: 1 April 2022).
- Totschnig, M. (2012) My Expenses, Google Play. Available at: https://play.google.com/store/apps/details?id=org.totschnig.myexpenses (Accessed: 1 April 2022).
- Tracker, F.- E. (2016) Expense Tracker, Family Budget, Google Play. Available at: https://play.google.com/store/apps/details?id=com.finart (Accessed: 1 April 2022).
- Tubin, S. (2013) Vault - Budget Planner, Google Play. Available at: https://play.google.com/store/apps/details?id=ru.tubin.bp (Accessed: 1 April 2022).
- YouNeedABudget (2015) YNAB (You Need A Budget), Google Play. Available at: https://play.google.com/store/apps/details?id=com.m.youneedabudget.evergreen.app (Accessed: 1 April 2022).