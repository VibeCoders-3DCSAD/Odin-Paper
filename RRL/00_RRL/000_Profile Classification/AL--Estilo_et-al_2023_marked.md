CENTRAL PHILIPPINE UNIVERSITY
COLLEGE OF ENGINEERING
SOFTWARE ENGINEERING DEPARTMENT
ILOILO CITY PHILIPPINES

Destamp: A Mobile Application for Generating Budget-Based

Itineraries to Enhance Travel Planning

A Project Study Report

Presented to the Faculty of the

Department of Software Engineering

Central Philippine University

Jaro, Iloilo City, Philippines

In Partial Fulfillment

of the requirements for the Degree of

Bachelor of Science in Software Engineering

Estilo, Chloe Belle T.

Jondanero, Shem Jehro T.

Lajo, Jann Carmely C.

December 2023

APPROVAL SHEET

This research entitled “Destamp: A Mobile Application for Generating

Budget-Based Itineraries to Enhance Travel Planning” prepared and submitted

by Chloe Belle Estilo, Shem Jehro Jondanero, and Jann Carmelly Lajo has

been evaluated and accepted by the Panel of Evaluators in partial fulfillment of

the requirements for the course SE 4121 - Capstone Project II.

Project Study Panelists:

Signature

Date

Mr. Francis John Conde

________________

________

Mr. Sian Paul Lasaga

________________

________

Ms. Mary Kristine Jayme

________________

________

Engr. Marjee Rose Parreño

________________

________

Project Study Adviser:

Signature

Date

Mrs. Pia Bianca Ayopela

________________

________

Project Study Coordinator:

Signature

Date

Ms. Marie Ariessa Lane Ko

________________

________

OIC, SE Department:

Signature

Date

Engr. Romarie Jhoanna C. Eder

________________

________

Dean, College of Engineering:

Signature

Date

Engr. Mary Earl A. Daryl Grio

________________

________

ACKNOWLEDGEMENT

The researchers would like to thank the following who have contributed to

the successful realization of this endeavor:

First and foremost, to God Almighty, for His guidance, blessings, and the

strength and perseverance He instilled throughout this capstone journey.

Capstone adviser Anfernee Joan Ng, whose invaluable insights,

encouragement, and expert guidance have been instrumental in shaping the

direction and success of this project; His unwavering support and mentorship

have been a cornerstone of this work.

Capstone instructor Marie Ariessa Lane C. Ko, for her comprehensive

instruction, constructive feedback, and relentless dedication for their academic

growth. Her commitment to excellence has inspired them to strive for the highest

standards.

Panel members Mareee Rose Parreño, Sian Paul Lasaga, Wabee Jane,

and Francis Conde, for their critical evaluation, thoughtful suggestions, and

valuable time. Their expertise and perspectives have greatly enriched this study;

Engr. Romarie Jhianna C. Eder, OIC in the Software Engineering

Department, for her unwavering support and encouragement. Her leadership and

belief in the researchers’ abilities have been a driving force behind this

achievement;

Mrs. Ma. Arlen F. Arellado, for her meticulous review as the grammarian.

Her attention to detail and expertise in language have greatly enhanced the

clarity and precision of this work.

Miss Ericka Joy Guelos, for her generous financial support of the

backend server. Her contribution has been pivotal in the realization of this

project;

Friends and family, for the unwavering support, encouragement, and

understanding: Their love and faith have been a constant source of motivation;

without them, this accomplishment would not have been possible.

ABSTRACT

This study focuses on simplifying trip planning challenges,

leading to the

development of Destamp, an innovative mobile application designed to

streamline travel planning specifically for

Iloilo City. The app incorporates

features such as itinerary generation, personalized recommendations, and

budget tracking, offering substantial benefits not only to travelers but also to local

residents,

tourist destinations, and business operators. Developed through a

user-centered Software Development Life Cycle (SDLC),

the initial phase

involved market validation and surveys to better understand the needs of

potential users. A survey conducted from July 17 to July 31, 2023, with 319

participants aged 18 to 60, revealed that 47% lacked knowledge in creating

itineraries, 54% relied on self-research and booking, 31% spent a day or more

planning trips, 68% researched travel routes before departure, 84% considered

budget a significant factor, and 76% emphasized the importance of staying within

budget. Data collection from various sources, including a Google Maps scraper,

provided comprehensive information on tourist destinations and businesses in

Iloilo City, enhancing user experience within the app. Additionally,

the app

employs a freemium model, allowing both free and premium users access to its

features to meet diverse user needs. Powered by advanced methodologies,

Destamp utilizes Genetic Algorithms

to optimize itinerary generation,

content-based filtering for personalized recommendations, and the Mapbox

platform for enhanced mapping capabilities, all

implemented within a React

Native framework to ensure a seamless user experience. Overall, Destamp offers

a comprehensive solution to the complexities of travel planning, combining a

well-defined methodology, inclusive business model, and advanced technology to

transform the way individuals plan and experience trips in Iloilo City.

TABLE OF CONTENTS

Chapter 1

Introduction

Background and Rationale

Statement of the Problems

Objectives of the Study

Conceptual Framework

Definition of Terms

Scope and Limitations

Significance of the Product

Chapter 2

Review of Related Studies and Literature

Related Literature

Related Studies

Competitive Analysis

Product Comparison

Chapter 3

Methodology

Software Development Life Cycle

Project Initiation and Data Collection

Business Model

Business Objectives

Methods in Addressing Business Objectives

Survey

1

5

6

7

8

11

14

15

19

22

24

25

26

28

29

34

37

Chapter 4

System Design

Use Case Diagram

Technology Stack

System Architecture

Technology and Tools

Business Rules

Chapter 5

Summary, Results, Conclusions, and Recommendations

Summary

Results

Conclusions

Recommendations

Appendix

User Stories

Usability Report

Sequence Diagram

Platform Screenshots

References

43

45

46

47

49

52

53

54

55

57

61

65

72

81

Chapter 1

Introduction

BACKGROUND AND RATIONALE

Travel planning is an essential aspect of the modern travel experience,

involving the process of organizing and preparing for a trip. It allows travelers to

optimize their time, budget, and activities to make the most of their journey.

According to Focused Travels (2022), one of the factors to consider when

choosing a travel destination is the budget, as it significantly affects one’s

choices for accommodation, food, and transportation. In fact, this survey found

out that budget constraints were the top priority for 92% of respondents when

planning an itinerary and 76% said that staying on budget was very important.

This is consistent with these findings from Booking.com, which showed that 68%

of travelers were paying close attention to how much they spent on their

vacations and 61% believed they could save money by planning their vacations

further in advance. The above results that travelers are becoming more

budget-conscious and are willing to plan ahead in order to save money on their

vacations.

However, a big challenge for travelers is creating an itinerary that suits

their budget while still providing an enjoyable experience. The current process of

planning a trip is often time-consuming, overwhelming, and inefficient for

individuals seeking to organize their travel arrangements. With the abundance of

available information, travelers struggle to efficiently gather and filter relevant

details as they are required to navigate multiple websites and sources to gather

necessary information. According to Jain (2019), in a study by the founder of the

Journy app, found that the average person spends 20–30 hours on pre-travel

planning. The processes of planning a trip, such as researching destinations,

transportation, accommodations, activities, and budgeting require a significant

amount of googling. This is supported by this survey, which showed that nearly a

third of the respondents (31%) said that it took them a day or more to plan their

own trips.

To address travel planning challenges, this study introduces Genetic

Algorithms as a solution to enhance the overall travel experience. Inspired by

Charles Darwin's theory of natural evolution, Genetic Algorithms are applied for

problem-solving. As noted by Yochum et al. (2021), researchers have recently

used Genetic Algorithms in the field of tourism recommendations. This approach

involves stages such as initialization, selection, crossover, and mutation to

optimize the solution. The primary goal is to determine the most efficient and

cost-effective itinerary, comprising a set of Points of Interest (POIs), using the

Genetic Algorithm's fitness function. Moreover, the intention is to incorporate

these approaches into the budget-based itinerary generator application.

In a genetic algorithm, five phases are considered. According to

MathWorks (2023), the process begins with the creation of a random initial

population. The algorithm then generates a sequence of new populations, using

the individuals from the current generation to form the next. Each step involves

scoring each member of the current population based on its fitness value, known

as the raw fitness scores. These scores are then scaled to convert them into a

more usable range of values, referred to as expectation values. Based on these

expectation values, members, or parents, are selected. Some individuals from

the current population with lower fitness are chosen as elite and are passed onto

the next population. The algorithm then produces children from the parents either

through mutation, which involves making random changes to a single parent, or

through crossover, which combines the vector entries of a pair of parents. The

current population is then replaced with the children to form the next generation.

The algorithm continues this process until one of the stopping criteria is met. It is

worth noting that the algorithm takes modified steps for linear and integer

constraints and is further adjusted for nonlinear constraints, as detailed in the

Nonlinear Constraint Solver Algorithms for Genetic Algorithm.

2

Furthermore, some stages of the Genetic Algorithm (GA) can be

implemented in the budget-based itinerary generator. In this context, the

'initialize' stage sets the foundation by creating a random initial population of

potential Points of Interest (POIs), which are the genes representing the user's

choices for their itinerary. Following that, the 'assign fitness score' stage

evaluates each POI's suitability by computing a fitness score, taking into account

the user's budget and available time. The scoring stage is crucial in determining

the fitness of each POI based on the given constraints. Next, the 'selection of the

next generation' phase ensures that individuals with higher fitness scores are

favored, aligning the generated itinerary with the user's specific budget and time

constraints. Finally, the 'crossover' stage combines the characteristics of two

selected POIs to create a new set of potential destinations, enhancing travel

experience tailored to the user's preferences and constraints.

Figure 1.1 Genetic Algorithm

3

Route planning is an effective method to optimize the route such that less

time is spent on driving or riding, and more time can be spent on visiting

attractions (Huang et al., 2021). According to Xiongbin (2017), the result of their

study showed that the tourists’ degree of attention to travel time and travel cost

had a great influence on tour route planning. This is because tourists with a high

value of time tend to choose transportation modes with shorter travel times. In

fact, 68% of the respondents stated that they research their travel routes before

heading to their destinations.

In the traditional way of travel planning, packaged tours offer all-inclusive

and pre-arranged itineraries. A survey by AirAsia found that Filipinos are

interested in travel deals that offer good value for money specifically, 66% of

respondents are interested in complete tour package deals that include flights,

hotels, and tours and activities. Despite the availability of online resources for

tour planning and services provided by tour agencies, many travel guides simply

recommend popular points of interests (POIs) that do not reflect the tourist’s

interest preferences or consider various trip constraints (Lim, 2016). According to

the Department of Tourism's 2021 Philippine Travel Survey Report, 85% of

travelers in the Philippines wanted a do-it-yourself (DIY) arrangement or

personalized travel experience. This means that they want to have more control

over their travel plans and be able to tailor their specific interests and

preferences.

In recent years, the global tourism industry has witnessed a remarkable

resurgence, bouncing back from the devastating impact of the COVID-19

pandemic. According to Statista Research Department (2023), the number of

international tourist arrivals worldwide bounced back in 2022 after dropping

sharply with the onset of the coronavirus (COVID-19) pandemic. Despite the

significant annual increase, international tourism arrivals remained below

pre-pandemic levels, totaling to approximately 963 million in 2022, highlighting

the need for innovative approaches to revive and boost tourism in various

destinations.

4

In relation to the above-mentioned travel experiences, this study presents

an innovative solution designed to enhance the travel experience of visitors

coming to Iloilo City. Iloilo, known as "The Heart of the Philippines" due to its

location and cultural significance, is recognized as one of the prominent tourist

destinations in the Visayas region. As of 2022, according to the Philippine News

Agency (2023), Iloilo City ranked second to Boracay Island in terms of tourist

arrivals in Western Visayas. Records from the Department of Tourism showed

that in 2022, Iloilo City registered a total of 752,301 tourists - 734,218 domestic

and 18,083 foreign. Meanwhile, Boracay Island received a total of 1,759, 592

tourists in 2021.

STATEMENT OF THE PROBLEM

1. The current methods of planning a trip within budget are time-consuming

and overwhelming due to the extensive manual research, browsing of

multiple websites, and gathering of information from various sources.

2. Many travel guides and pre-arranged tours recommend popular tourist

attractions that don’t necessarily match travelers’ preferences which may

not be a good fit for all travelers.

3. Budgeting and keeping track of all expenses during a trip can be

challenging. Travelers may struggle to allocate budgets for different

aspects of the trip and monitor their expenses.

4. Lack of route optimization can lead to inefficient itineraries, increased

transportation costs, missed opportunities, and negatively affect travelers'

overall experience.

5

OBJECTIVES OF THE STUDY

The objective of this study is to design, develop, and test a budget-based

itinerary generator mobile app that enhances the travel planning experience.

Specifically, this study seeks:

1. To design, develop, and test an itinerary generator module that utilizes a

Genetic Algorithm (GA)

to recommend near-optimal combinations of

destinations based on user input factors like budget and travel constraints.

2. To design, develop, and test a content-based recommender module that

will

leverage trip preferences to offer

tailored recommendations for

attractions, dining options, and accommodations ensuring that

the

provided suggestions are better aligned with each traveler's interests.

3. To design, develop, and test a budget tracking module enabling travelers

to allocate budgets for various trip aspects.

4. To design, develop, and test a route optimization module that optimizes

routes between destinations to minimize travel time and expenses.

6

CONCEPTUAL FRAMEWORK

Figure 1.2 Conceptual Framework of the Product

7

DEFINITION OF TERMS

Account Authentication

This offers user account authentication to enable personalized

experiences, itinerary saving, and synchronization across multiple devices.

Budget Tracking

This feature helps users keep track of their expenses during their trip. It

allows them to set a budget, and monitor their spending ensuring they stay within

their financial limits.

Business Operator

One of the primary users of this application directly benefits from business

profile management features.

Business Profile Management Features

This is where business operators have greater control over their listings,

enabling them to create, edit, and delete their existing business profile

information. This data includes business name, address, contact details,

category, pricing information (admission fee for attractions, price range for meals

per person, and room rates for accommodations), hours of operation, visit

duration, description, photos, amenities, cuisine, and atmosphere. These

features are intended to assist business operators in managing their business

profiles, encompassing the following functionalities:

1. Account Authentication

Once users have registered their accounts as Business Operators,

they can now access the business side of the app.

2. Business Creation

Business operators can create their business by entering their

basic information, and establishment

type, uploading photos of

their

establishment, and verifying it by uploading their business permits.

8

3. Profile Management

Business operators will have control over their listings and may edit

their business information.

Database

The component of the application is responsible for storing and managing

all the necessary data.

Destamp Mobile Portal

This mobile portal serves as a user-friendly platform designed to

streamline trip planning, as well as facilitate the management of business profiles

for its intended user base.

Genetic Algorithm

A Genetic Algorithm (GA) is a type of optimization algorithm that mimics

the process of natural selection to solve complex problems. In the context of this

app, GA will be employed to optimize travel

itineraries considering factors of

budget, travel constraints, and user preferences to provide personalized and

efficient travel plans.

Itinerary Generator

This feature helps users plan their

trip by automatically generating

itineraries based on their specified budget, including other travel constraints such

as duration of travel and traveling companion.

Itinerary Mapping

This feature provides a visual map that allows users to see the planned

destinations of point of interest and routes. It also provides access to additional

information such as ratings, and images.

Personalized Recommendation

This feature provides personalized recommendations for attractions, food

options, and accommodations based on the user's preferences and travel

constraints.

9

Route Optimization

This feature provides users with the optimized route of their multiple-stop

destinations.

Security

The aspect of

the application focuses on protecting user data and

ensuring a safe browsing experience.

Traveler

One of the primary users of this application directly benefits from trip

planning features.

Trip Planning Features

These features are aimed at facilitating users in effortlessly planning and

customizing their travel experiences, simplifying the process while ensuring

personalization. They encompass the following functionalities:

1.

Itinerary Generation

Users will be prompted to provide essential details such as their

budget, travel duration, and the number of travelers.

2. Personalized Recommendation

This feature aims to offer personalized attraction and activity

recommendations tailored to the user's preferences.

3.

Itinerary Mapping

This feature aims to display a map of

the user's itinerary,

showcasing planned destinations and routes between them, creating an

interactive visual representation for the user.

4. Route Optimization

This feature

offers users an optimized route of

their planned

destinations.

5. Budget Tracking

This feature lets users calculate and track expenses against their

predefined budget, helping them stay within their financial limits.

10

SCOPE AND LIMITATIONS

Scope

The scope of the study is to design, develop, and test a budget-based

itinerary generator app that aims to simplify and streamline the travel planning

process. The app will provide users with a platform that combines itinerary

creation, destination information, and transportation information. Additionally, the

app includes features to assist business operators in managing their profiles,

such as account verification and business profile management tools. The app will

utilize a Genetic Algorithm (GA) to find the best combination of destinations given

the user's constraints and preferences.

The app features user account registration and login functionality, allowing

travelers to create personalized profiles. By creating an account, users can

securely save and access their travel preferences, and itineraries. Additionally,

business operators have the option to create and authenticate their accounts,

ensuring accurate and up-to-date data for their business-related information.

Users can input their travel budgets and the app automatically allocates

the funds for different aspects, including accommodation, transportation, food

options, and activities by generating the itinerary with estimated costs.

Users are able to provide information about their travel preferences and

interests. This data will be used to personalize the generated itineraries. They

have access to comprehensive information about various destinations, including

attractions, food options, accommodations, and activities.

The app integrates maps and navigation functionalities to assist users in

navigating their travel destinations and optimizing their travel routes.

The app will offer tools and features for business operators to manage

their profiles efficiently, including updating prices and information, and adding

images.

11

Limitations

The app's features and functionalities are optimized for Android devices

running Android 9 (Pie) and above. Users with other systems or devices may

experience limitations in the app's performance and compatibility.

The app's effectiveness relies on internet connectivity and access to data.

In areas with limited or no internet coverage, users may face difficulties in

accessing information, maps, and navigation features, affecting their ability to

utilize the app fully.

The app's destination database primarily focus on attractions, activities,

food options, routes, and accommodations within Iloilo City. It does not extend its

coverage to other cities, regions, or destinations beyond its boundaries.

The app is capable of generating a maximum of 5 itinerary days. This

limitation is in place to ensure the delivery of high-quality data, as it aligns with

the capabilities of the services utilized.

Travel plans can be affected by external

factors such as weather

conditions, unforeseen events, or changes in availability or pricing. While the

application can provide initial

recommendations,

it may not be able to

dynamically adjust for real-time updates or unexpected changes that occur after

the itinerary is generated.

The focus of

this personalized itineraries revolves around addressing

various factors, including accommodation type and amenities, activities, dining

styles, cuisines, and budget inclusions.

The accuracy and availability of destination information, such as

attractions, activities, food establishments, and transportation options, depend

heavily on the reliability and quality of the data sources used by the app.

12

The app may not cover all destinations, especially lesser-known or remote

places, its main emphasis is on offering itineraries for the available destinations.

Furthermore, the app aims to expand its coverage gradually over time.

The app's budget tracking feature provides users with estimated costs for

various aspects of their travel, such as accommodations, transportation, food

options, and activities. However, these estimates may not always reflect real-time

prices accurately,

leading to potential discrepancies in the actual expenses

incurred during travel.

This route optimization feature focuses on offering the fastest route based

on distance, aiming to provide users with efficient and time-saving travel options.

For this study, the platform does not include subscription payments as part

of the scope for its development, but future versions of the platform will include a

subscription system. For

this project,

the simulation of

free and premium

platforms can be achieved through the subscription page without payment, as

actual subscription functionality will not be implemented at this time.

13

SIGNIFICANCE OF THE PRODUCT

The significance of this study is to organize the way people plan their trips,

improve financial management in travel, cater to diverse traveler segments, and

benefit the travel industry.

The result of this product will benefit the following:

Travelers: Travelers who plan to visit

Iloilo City while keeping their

expenses within a certain budget will find this app valuable. It can help them

optimize their spending and make informed decisions about accommodation,

transportation, activities, and meals.

Local Residents: The app could also be useful for residents of Iloilo City

who want to discover more about their own city or plan budget-friendly outings

with their travel companions.

Tourist destinations and local businesses: The app can promote tourist

destinations and local businesses in Iloilo City by recommending them within

various budget ranges. It can drive more tourism and help small businesses

thrive.

Business Operators: The platform offers an opportunity for

local

business operators to showcase their services to a targeted audience. By being

featured in the app, business operators can attract more customers, increase

visibility, and actively participate in the growth of Iloilo City's travel industry.

14

Chapter 2

Review of Related Literature

The Future of Travel-Planning Apps

According to Destination Analysts (2019), every year, technology keeps

advancing with new and impressive developments. Smartphones have become

reliable tools that help people with daily tasks and provide vast amounts of

information. However, when it comes to travel planning, this recent survey shows

that people do not always prefer to rely on technology.

The reason for this is that travelers prefer to trust recommendations from

people they know in person, like relatives and friends. When they receive advice

through face-to-face interactions, they find it more trustworthy and are more likely

to use it for planning their trips. However, when they see travel recommendations

from friends and family on social media, they are less likely to trust them and use

them for their travel plans. When it comes to travel planning, most leisure

travelers rely on word of mouth, meaning that they prefer getting advice from

people they know in person, preferably their family members. They trust these

familiar sources more than advice from strangers through a phone or computer.

Travel apps can provide a lot of information and options, much more than

fellow travelers can offer from their experiences. Apps like TripAdvisor and Yelp

have plenty of honest reviews from real travelers, which travelers appreciate.

However, these apps may still lack the level of "quality" recommendations that

travelers truly desire.

To gain the same level of trust as word of mouth, travel marketers could

add user-generated content, like photos and videos of travelers' experiences, to

the app or website. This could increase trust beyond just reading

recommendations. Another idea is to have filter options that let users customize

their ideal vacation, and then receive recommendations based on their

preferences. If travel organizations and brands can make apps more personal

and relatable, while still providing a lot of useful information, it could greatly

impact the future of travel planning.

Factors to Consider when Choosing a Travel Destination

According to Focused Travels (2022), before embarking on one’s next

vacation, it is essential to select the ideal travel destination, and these tips can

help one make the right choice. First and foremost, consider the budget, as this

will greatly impact the options for flights, accommodation, food, and

transportation. Traveling doesn't have to break the bank, as there are plenty of

budget-friendly options available nowadays. Next, think about the duration of

your trip; if one has limited time, it is best to choose a destination that will not

require excessive travel time. Take a look at one’s travel bucket list and prioritize

the dream places to visit. Whether it is a serene beach getaway, a shopping

spree, exploring new sights, immersing in nature, experiencing festivals, or

engaging in thrilling outdoor activities, knowing the type of travel experience

desired will guide one’s decision when traveling with family or friends, ensure to

consider everyone's preferences to create a balanced vacation. On the other

hand, solo travelers have the freedom to pick destinations that resonate with their

personal interests. Seeking recommendations from friends and family who have

visited exciting places can also provide valuable insights and influence one’s

decision-making. By weighing these factors, one can confidently choose a travel

destination that aligns with the desires, budget, and overall vacation expectations

for an unforgettable experience.

Five Reasons why having a Travel Itinerary is Important

According to Silva (2018), a well-planned travel itinerary offers several

benefits that enhance the overall travel experience. Firstly, it allows travelers to

maximize their time by efficiently managing their schedule. By including travel

time between attractions and accounting for potential delays like weather

conditions and traffic, travelers can remain flexible while ensuring time is not

wasted. Secondly, having a travel itinerary helps manage expenditures as it

16

allows travelers to estimate their costs in advance and plan their budget

accordingly, avoiding any unexpected financial surprises during the trip.

Moreover, a travel itinerary facilitates easier and faster travel from one

point to another. While the internet may make it seem effortless to move between

places, in reality, it is essential to consider practical logistics. An itinerary helps

prioritize attractions and plan a route that optimizes travel time and minimizes

backtracking. It aids in making the most of the trip and ensures that travelers do

not miss out on their must-see sights. Finally, a comprehensive travel itinerary

ensures that essential items and information are not forgotten. It includes details

such as what to bring, appropriate clothing, necessary medications, and

emergency contacts, ensuring a smooth and well-prepared journey, especially

when traveling to multiple destinations. Overall, a thoughtfully curated travel

itinerary adds convenience, efficiency, and peace of mind to the travel

experience, making the trip more enjoyable and memorable.

Six Advantages of Travel Apps in Travel and Tourism Industry

According to Dhrubok Infotech Services Limited (2022), a travel app

offers a convenient all-in-one solution for travelers, providing access to various

travel services like tourist information, ticket booking, hotel reservations,

restaurant details, and transportation options. Additionally, the app can offer

weather forecasts for desired tourist destinations, enhancing the overall travel

experience. By using a travel app, businesses can stay one step ahead in the

competitive tourism industry, as it allows them to reach customers faster and

serve as a constant reminder of their services. With the ability to send

notifications about upcoming offers and new services, travel companies can

easily spread information to their customers. Being available online through an

app allows for more effective digital marketing and caters to the modern

preferences of customers who frequently use mobile devices and the internet.

Offering various transaction methods and 24/7 service availability, a travel app

ensures smooth and hassle-free transactions for customers.

17

In conclusion, a travel app brings numerous benefits for both travel

companies and customers, streamlining the travel planning process and

providing valuable convenience. As customers increasingly seek digital solutions,

a well-developed travel app becomes an indispensable tool for attracting and

retaining travelers in today's busy and fast-paced world.

Travel Apps – Thematic Intelligence

According to Global Data (2023), travelers now expect more connected

experiences, and travel apps are playing a significant role in reshaping how

travelers interact with the travel and tourism industry. As smartphones become

increasingly essential in people's lives, the convenience of using travel apps

continues to grow. It is crucial for travel companies to recognize the significance

of developing apps that address consumer needs and challenges. Many players

in the industry have yet to realize the potential value that a well-developed travel

app can bring to both the company and the traveler.

Developing Agile Methodologies for Algorithm Products

According to Young (2021), the development of agile methodologies for

algorithm products proves advantageous in addressing the unique challenges

posed by data science in contrast to traditional software development. The study

emphasizes the importance of adapting agile principles to accommodate the

longer cadence involved in algorithm development. Additionally, it underscores

the need to align engineering resources with the cyclical nature of data science

work, advocating for collaboration and understanding among product managers,

data scientists, and engineers. The conclusion of the study highlights the value of

nuanced adjustments within an agile framework to effectively navigate the

distinct characteristics of algorithm product development (Young, 2021).

18

Review of Related Studies

Trippit: An Optimal Itinerary Generator

According to Nguyen and Shoubber (2019), currently, there is a lack of

efficient methods to optimize travel itineraries, resulting in less enjoyable and less

efficient travel experiences. However, a potential solution comes from utilizing a

modified version of the Traveling Salesman algorithm combined with data from

the Google Distance Matrix and Foursquare Places API. By doing so, it becomes

possible to optimize travel itineraries effectively.

While an ideal approach would involve using powerful servers to handle

large-scale computations for the application to scale, the prototype created

demonstrates the feasibility of itinerary optimization. With the Trippit application,

users can now enjoy a hassle-free vacation, making the most of every minute of

their travel experience.

What Drives the Adoption of Smart Travel Planning Apps? The Relationship

between Experiential Consumption and Mobile App Acceptance

According to Ho and Amin (2019), smart travel apps are incredibly useful

and have become popular among travelers for making travel-related decisions.

These apps offer both practical benefits and enjoyable experiences, making

travel easier and more enjoyable. Travel operators can use the insights from this

research to create more appealing travel plans for users.

For practical purposes, travel operators should focus on providing useful

functionalities to increase app usage. In addition to including popular tourist

attractions, travel itineraries should also offer information about local eateries,

transportation routes, and cultural crafts and souvenirs. This way, the app can

help travelers with various aspects of their journey, and travel operators can

engage with customers to offer additional services.

19

On the other hand, app users also value personalized experiences.

Customized itineraries tailored to individual preferences make users feel a sense

of ownership and connection to the app. Travel operators can use this

opportunity to gather personal information and offer more personalized services,

enhancing the overall travel experience for users.

Systematic review of mobile travel apps and their smart features and

challenges

According to Sia et al. (2022), the high user ratings for apps from both app

stores revealed the acceptance of smart technology in the tourism industry.

Geolocation tracking services, travel itinerary generators, and real-time

personalization and recommendation were the three major features available in

the included mobile travel apps (MTA).

How to improve travel-app use continuance: The moderating role of culture

According to Coves-Martínez et. al. (2023), the rise of smartphones and

apps has had a significant impact on how people interact and behave. In the

tourism industry, mobile technology has led to changes in travel patterns and

tourist behavior (Wang, Xiang, & Fesenmaier, 2016). This research highlights the

significant impact of smartphone technology and apps on the tourist experience.

Destinations are increasingly using such technology to enhance the tourist

experience, making them smart tourism destinations. Tourism service providers

must recognize that offering apps has become essential for their

competitiveness, as tourists now expect them as a part of their everyday life.

App designers need to understand what factors lead to tourists continuing

to use their apps. This will help them create more effective tools that enhance the

overall travel experience and increase satisfaction with both the technology and

the destination. It is also important to consider cultural differences, as they can

affect how travelers accept and continue to use travel apps. Designers should

tailor the apps to suit the needs and preferences of users from different cultures,

ensuring they get the most out of their travel experiences.

20

A Genetic Algorithm for Travel Itinerary Recommendation with Mandatory

Points of Interest

Traveling is a widely embraced leisure activity enjoyed by people

worldwide. Typically, travelers seek out popular and unique Points of Interest

(POIs) in a city, often beginning from locations near their accommodations and

ending near transportation hubs. However, planning such itineraries can be

time-consuming and challenging due to limited time and a lack of familiarity with

the city's numerous POIs. In the study conducted by Yochum et al. (2021), they

define this process as the "Mandatory Tour problem," where tourists aim to

construct an itinerary that includes as many popular or unique POIs as possible

within their time and budget constraints.

According to Yochum et al. (2021), the researchers refer to these highly

sought-after POIs as "mandatory POIs." To address the Mandatory Tour problem,

they propose a genetic algorithm named GAM. The study evaluates their

approach alongside several baseline methods using real-world datasets from the

Yahoo Flickr Creative Commons 100 Million Dataset (YFCC100M), which

includes information about POI visits in seven tourist cities. The experimental

results show that GAM excels in recommending mandatory POIs, total POIs

visited, time budget (including travel time and visit duration), and overall profit

(indicative of POI popularity).

Genetic Algorithm for Generating Travel Itinerary Recommendation with

Restaurant Selection

According to Handayani (2018), experiencing local cuisine while traveling

has a significant impact on tourist satisfaction. Dining at restaurants has become

an integral part of a tourist's daily itinerary. However, manual itinerary planning is

a complex and time-consuming task. This study aims to introduce a planning

problem for generating travel itinerary recommendations with restaurant selection

and to provide a method to address this challenge. The problem is modeled as a

rooted orienteering problem with time windows, where selected restaurants must

be scheduled within lunch and dinner times. The objective is to maximize the

21

total collected utility at each visited location while adhering to specific constraints

on total travel time. A Genetic Algorithm was developed to solve this problem,

with Yogyakarta city as the case study. The results demonstrate that the

developed algorithm effectively generates a satisfactory travel plan, including

selected tourist destinations and restaurants, while respecting the available

constraints.

COMPETITIVE ANALYSIS

This section provides an overview of the closest competitors of the

product, as well as a high-level comparison of the available features.

Wanderlog - Trip Planner App

Created by Jeff Chen and Arthur Wu, Wanderlog is a travel planning and

itinerary management platform. It allows users to create detailed travel itineraries

by adding destinations, activities, and notes, organize flight, hotel, and car

reservations, view places to visit on a map. It also supports collaborative

planning for group trips. The key features of the app include:

1.

Itinerary Creation

2. Budget Tracker

3.

4.

Itinerary Mapping

Itinerary Sharing

5. Flight, hotel and car booking

6. Collaborative Planning

7. AI Bot Assistant

AI Trip Planner - Orbt

Developed by a group of travel enthusiasts and developers, Orbt is a

comprehensive travel app that provides itinerary planning based on the given

budget. Users can create and customize travel itineraries, and receive

22

personalized recommendations for activities and attractions. The key features of

the app include:

1.

Itinerary Generation

2. Budget-based

3. Distance & Travel Times Between Locations

4. Personalized

5.

6.

Itinerary Sharing

Itinerary Modification (Premium)

7. Regeneration (Premium)

Tripwise

Developed by Aliaksandr Kartsau, tripwise is an AI-powered travel planner

and guide that makes it easy to create personalized itineraries for cities around

the world. Users can select their destination city, travel dates, and interests, and

the app's AI technology will generate an itinerary. The key features of the app

include:

1.

2.

Itinerary Generation

Itinerary Mapping

3. Route optimization

4. Personalized

5.

Itinerary Modification (Premium)

6. Regeneration (Premium)

23

PRODUCT COMPARISON

Itinerary

Budget-

Personalization

Itinerary

Route

Budget

Generator

based

Mapping

Optimization

Tracker

Destamp

Wanderlog

Orbt

Tripwise

✓

✗

✓

✓

Itinerary

✓

✗

✗

✗

✓

✗

✓

✓

✓

✓

✗

✓

✓

✓

✓

✓

✓

✓

✗

✗

Table 2.1 Feature Comparison Overview

As evident from the conducted product comparison, none of the three

competitors have successfully implemented or integrated the same set of

features found in Destamp. Though some may have similar features, none of

them have managed to include all the same features.

24

Chapter 3

Methodology

SOFTWARE DEVELOPMENT LIFE CYCLE

Software Development Life Cycle (SDLC) is a standardized process that

IT, systems, and software engineering industries use to build and test software

products. It's a step-by-step development process with the goal of creating

high-quality software that meets or exceeds customer expectations (Hammer,

2021). The following section breaks down the different components of the SDLC

that will be used by the developers in building the product.

Figure 3.1 Scrum Process

PROJECT INITIATION AND DATA COLLECTION

Market Validation

Market validation commenced with the collection of data, which included

interviews with business owners and surveys administered to individuals across

four distinct age groups: 18 to 25, 26 to 34, 35 to 44, and 45 to 60.

Destination and Business Data Gathering

To gather information on tourist destinations and businesses in Iloilo City,

a Google Maps Scraper from Apify was employed to web crawl Google Maps.

This process extracted data such as business name, address, geolocation,

contact number, rating, images, prices, hours of operation, category, hotel

amenities, dining options, and atmosphere. The collected data serves to populate

our database of points of interest, utilized by users to plan their trips. Additionally,

business operators who use our app can also provide us with data about their

businesses such as their prices (admission fee for attractions, price range for

meals per person, and room rates for accommodations), amenities, cuisine,

dining options, and offerings, and images. This information is then added to their

business listings on our app.

Agile Software Development (Scrum Framework)

In this project, each sprint will have a duration of 2 weeks. The goal of

each sprint is to deliver value by iterating on the product within the constraints of

the following inputs:

1. Sprint Goals

2. Team Capabilities

3. Business or Technical Constraints

4. Team Velocity

5. Product Backlog

26

Sprint Planning

Each Sprint will start with Sprint Planning where the team will plan

for the sprint backlog and the tasks for the sprint. The goal of the Sprint

Planning activity is to define the goals for the sprint and allow the

development team to have an overview of the sprint's tasks. Activities

involved in Sprint Planning include identifying user stories to work on

during the sprint, estimating the effort to complete each user story,

creating a sprint backlog, and assigning tasks to team members.

Development

The next phase is development, where the team will begin working

on their assigned tasks. The team will hold Daily Stand-up Meetings to

inspect and adapt their progress. To keep track of the development

process, the team uses a task board. The cards are placed in different

sections depending on their status. When a task is started, the task card is

moved from the "To Do" section to the "In Progress" section. Once the

task is completed, the task card is transferred to the "For Review" section.

After the task is checked and approved, it is transferred to the "Done"

section.

During the development phase, a burndown chart is created to

track the progress of the development process. The burndown chart

shows the number of tasks that remain incomplete, and it is updated daily

after the stand-up meeting.

Sprint Review and Retrospective

At the end of each sprint, the team will hold a sprint review and

sprint retrospective. During the Sprint Review, the team will present their

completed work during the sprint and get feedback from the product owner

and stakeholders. They will discuss how the work meets the product goals

and whether there are any changes that need to be made. In the Sprint

Retrospective, the Scrum Master, Development Team, and Product Owner

27

will reflect on the past sprint. They will discuss what went well, what went

wrong, and what could be improved. They will then make plans to improve

their process in the next sprint.

BUSINESS MODEL

Figure 3.2 Freemium Model for Travelers

The freemium business model combines elements of both 'free' and

'premium.' In a freemium model, users are provided with essential features for

free. Additionally, for those seeking an enhanced travel experience, there are

premium features or additional services that users can access by upgrading to a

paid or premium version.

28

Figure 3.1 Key Partners

The product aims to partner with software development companies to

improve the product and provide valuable insights into the latest trends in app

development. It will also collaborate with local attractions and businesses to

curate a wide range of budget-friendly options for users. The app is built with the

needs of travelers in mind, and the team will actively engage with the user

community to gather feedback and incorporate their insights into the app's

development and updates.

BUSINESS OBJECTIVES

Create user account

The system should allow the user to create an account.

The system should allow the user to login and logout their registered

account.

The system should allow the user to choose whether to register as a

traveler or a business operator.

29

Manage Traveler Profile

The system should allow the user to edit their profile information.

The system should allow the user the option to access premium features.

Generate Trip

The system should allow the user to name the trip.

The system should allow the user to input their starting location.

The system should enable the user to set the starting and end dates of the

trip.

The system should enable the user to input their budget.

The system should enable the user to specify the number of people

included in the budget.

The system should enable the user to choose whether to include

transportation, accommodation, and food from the budget.

The system should allow users to review their entries before generating an

itinerary.

The system should allow the user to discard their trip.

The system should ask the user for confirmation if they were to discard

their trip.

The system should enable the user to generate travel itineraries tailored to

their specified budget, interests, and travel constraints.

The system should display the generated trip on the user’s my trip page.

The system should allow the user to generate multiple itinerary plans.

View Itinerary

The system should allow the user to view the generated itinerary.

The system should enable the user to see the estimated budget for the

entire day of the itinerary.

The system should enable the user to see the estimated budget for each

destination.

30

The system should enable the user to view the estimated budget for

transportation.

The system should display the distance and travel time between itinerary

destinations.

The system shall enable the user to view the travel time between

destinations.

Itinerary Mapping

The system shall display all destinations in the map.

The system shall provide directions according to the order of point of

interest.

Regenerate Itinerary

The system should enable the user to regenerate the itinerary.

The system should allow the user to view the regenerated itinerary.

Delete Itinerary

The system should allow users to delete their generated itinerary.

The system should no longer display the deleted itinerary.

Personalization

The system should enable the user to choose their preference for their

budget inclusions.

The system should prompt the user to specify their accommodation type

and preferred amenities.

The system should enable users to select their preferred activities, which

may include sightseeing, outdoor activities, shopping, arts, museums, and

architecture and landmarks.

The system should allow users to indicate their food venue preferences,

such as fast food, casual dining, fine dining and buffets.

The system should offer users the choice to select their preferred cuisine.

31

View Budget Summary

The system should enable the user to view the summary of their expenses

along with the total expense.

The system should display the expenses on each destination of the

generated trip.

The system should allow users to track their expenditure such as

accommodation, attractions, activities, transportation, and meals.

Manage Expenses

The system should allow users to create their own expenses.

The system should allow users to edit their expenses to ensure that their

budget is accurately tracked according to their spending.

The system should allow users to delete their expenses.

Create Business

The system should enable a business operator to create a business by

inputting their basic information, specifying their business type, and

uploading the required documents.

The system should enable the user to upload permits and ID for their

business.

The system should display the created business and inform the business

operator that it is still in the process of verification.

Manage Business Profile

Business operators should have the capability to edit their existing

business profile information. The system should allow them to modify any

of the data associated with their listings, ensuring that their information is

up-to-date and accurate.

32

The system should provide a feature that allows business operators to

delete their business listings. This function should assist in cases where a

listing is no longer relevant or in operation.

Business operators should be able to manage pricing information for their

listings, which includes setting admission fees for attractions, specifying

price ranges for meals per person, and indicating room rates for

accommodations.

Business operators should have control over the operational details of

their listings. They should be able to adjust operating hours, visit duration,

and other relevant information.

Usability

The system shall provide a uniform look and feel between all the mobile

application parts.

The app should feature a user-friendly and intuitive interface that allows

users to navigate and access various functionalities effortlessly.

The system should use English as its language.

The system should include informative error messages to guide users

when they encounter any issues or mistakes while creating or editing

itineraries.

Availability

The system shall be readily available to the user.

Security

The system shall require the user to have a username and password.

Store user passwords using strong hashing algorithms and ensure that no

plain-text passwords are stored on the server.

33

Data integrity

The system should ask for confirmation during updating and deletion of

information.

Reliability

The system should consistently perform all of its intended functions

without failure.

Provide a straightforward onboarding process that guides users through

the app's features, ensuring they understand how to create and manage

itineraries easily.

Data storage

Store generated itineraries and related data, such as destinations,

activities, and budgets, in a structured and organized manner.

METHODS IN ADDRESSING SPECIFIC OBJECTIVES

Itinerary Generator

This feature aims to generate travel itineraries by combining both

algorithms and user input. Users will be prompted to provide essential details

such as their budget, travel duration, and the number of travelers. To optimize

travel itinerary, the system will use a genetic algorithm (GA) to find the best

combination of destinations for the user given their constraints. GA is a search

metaheuristic inspired by the theory of biological natural evolution where the

fittest individuals survive, reproduce, and pass on their traits to the next

generation. In the context of the app, the best-performing itineraries will be

combined and mutated to create new and potentially better solutions. The GA will

use a database of points of interests to generate itineraries.

34

Personalized Recommendation

This feature aims to offer personalized attraction and activity

recommendations tailored to the user's preferences. To implement this feature,

the researchers first filter the point of interest data based on the user's

preferences and keep attractions that have at least one tag that matches the

user's preferences. They will then rank the destinations by their similarity to the

user's preferences and will use content-based filtering to calculate the similarity.

Itinerary Mapping

This feature aims to display a map of the user's itinerary, showcasing

planned destinations and routes between them creating an interactive visual

representation for the user. To implement this feature, the system will utilize

React Native for the user interface. The system will integrate with the Mapbox

Platform to provide the mapping capabilities required. The system will retrieve

supplementary information such as destination ratings, webURL, and images

from the database to enrich the user's map-viewing experience.

Route Optimization

This feature seeks to optimize users' planned routes by determining the

most efficient path between destinations. To implement this feature, the system

will employ React Native Maps for an engaging visual experience and guided by

Dijkstra's algorithm for optimal pathfinding. By utilizing a distance matrix, the

system efficiently identifies the optimal path ensuring that users are directed

along the shortest and most practical route between their planned destinations.

Budget Tracking

This feature lets users calculate and track expenses against their

predefined budget helping them stay within their financial limits. To implement

this feature, the system will use CRUD (create, read, update, and delete)

operations on the database for budget management. Users will be able to select

35

the category for each expense, input the amount spent, and optionally add notes

or descriptions. The user interface will be built using React Native.

Business Creation

This feature enables business operators to create their business listings in

the database. To implement this feature, the user provides essential details about

their business, including their basic information and establishment type. The

input is then processed by querying the database, and the user interface for this

process will be constructed using React Native. Once the information is

successfully submitted and approved, the business listing is created, allowing

users to display their businesses through this streamlined process.

Business Profile Management

This feature lets users manage their business profile. To implement this

feature, the system will use CRUD (create, read, update, and delete) operations

on the database for business profile management. The user interface will be built

using React Native.

36

SURVEY

The survey for enhancing travel planning through a budget-based itinerary

generator, was conducted from July 17 to July 31. Its aim was to collect feedback

from potential users regarding their preferences and needs related to travel

planning. A total of 319 individuals, aged from 18 to 60 years old, participated in

the survey.

Key Findings:

1. Almost half of the respondents (47%) lack knowledge on how to create

their own itinerary.

2. Over half of the respondents (54%) engage in self-research and booking

when planning their trips.

3. Nearly a third (31%) of respondents spend a day or more planning their

trips.

4. A significant majority (68%) of respondents conduct research on their

travel routes before heading to their destination.

Budget:

1. Budget plays a crucial role in itinerary planning, with 84% of respondents

considering it a significant factor.

2. Staying within budget is deemed "very important" by 76% of respondents.

Challenges in Trip Planning:

1. Finding affordable attractions and activities is a challenge for 80% of

respondents.

2. Selecting the best destinations to visit is a concern for 68%.

3. Creating a travel itinerary within a specific budget is a challenge faced by

50% of respondents.

37

Figure 3.3. Gender.

Figure 3.4. Age Group

Figure 3.5. Know how to plan

Figure 3.6. Travel Frequency

their own itinerary

Figure 3.7. Factors influencing traveler’s decision to travel.

38

Figure 3.8. Average duration of trips.

Figure 3.9. Researching the route before

traveling.

Figure 3.10. Mode of Transportation

Figure 3.11. Usual approach for

planning trips.

Figure 3.12. Average time spent on planning

Figure 3.13. Factors influencing

a trip.

decisions in planning a trip.

39

Figure 3.14 Challenging aspects of choosing accommodations and activities.

Figure 3.15. Travelers who have used a trip

Figure 3.16.Factors to consider

planning app or website.

when planning an itinerary.

40

Figure 3.17. Importance of staying within

Figure 3.18. Personalized Itinerary

the budget

Figure 3.19 Likelihood of using

Figure 3.20. Most desired features.

budget-based features.

41

Chapter 4

System Design

This chapter focuses on the functional overview and system architecture

of the proposed system.

It begins with a detailed analysis of the use case diagram, which are

specific instances of how the system will be used.

This section also covers the technological stack we have chosen for this

system, which includes various software components that will work together to

deliver the desired functionality.

The next part discusses the system architecture, which is the structural

layout of the system and how different components interact with each other.

The chapter also covers the technology and tools used in the system.

This includes software development tools, testing tools, and deployment tools

among others

The business rules are the guidelines that dictate how the data can be

created, displayed, stored, and changed within the system.

Finally, the entity relationship diagram (ERD) is presented. This is a

visual representation of the major entities within the system and the relationships

between them.

Use Case Diagram

Figure 4.1 Use Case Diagram with Traveler as Primary Actor

This diagram provides a high-level view of

the system's functionality,

showing the different features or capabilities it offers and how travelers interact

with it

to achieve specific goals or

tasks.

It encompasses several key

functionalities. The user registration extends user authentication, allowing new

users to create an account and log in securely. Once logged in, the user can

manage trips, which includes creating, deleting, and regenerating trips.

Additionally, the user can view their trip details. The user can also manage their

43

budget, which encompasses managing expenses that include creating, reading,

updating, and deleting expenses, as well as viewing a budget summary.

Figure 4.2 Use Case Diagram with Business Operator as Primary Actor

This diagram provides a high-level view of

the system's functionality,

showing the different

features or capabilities it offers and how the business

operator interacts with it to achieve specific goals or tasks. It includes several key

functionalities. The business operator can register a new user, authenticate user

credentials during login, and log out of the system. Furthermore, the business

44

operator can manage the business profile, which includes creating, deleting,

editing, and viewing the business profile.

Technology Stack

Figure 4.3 Tech Stack Diagram of the Product

The tech stack of

the product can be grouped into the frontend

components, backend components, and third-party service components.

45

System Architecture

Figure 4.4 System Architecture of the Product

The architecture of this product is built around a client-server model. The

client, in this case, is a mobile application that communicates with a server. The

server,

in turn, accesses data from our database and external data sources

through API calls.

46

TECHNOLOGY AND TOOLS

Development

Frontend: React Native with Expo and NativeWind

React Native with Expo simplifies the process of building

cross-platform mobile applications, allowing developers to create

feature-rich apps with ease while benefiting from Expo's extensive tooling

and services. NativeWind is an open-source UI component library and

styling system that allows you to build beautiful and responsive React

Native apps for all platforms. It uses Tailwind CSS as its scripting

language, so you can write the same styles for your web and mobile apps.

Backend: Supabase

Supabase is an open-source cloud database service that combines

the benefits of a relational database with the convenience and scalability

of the cloud. It offers developers a fully managed PostgreSQL database

with built-in authentication,

real-time capabilities, and APIs for easy

integration into applications. It will be used to store and manage data such

as user preferences, place details, itinerary details, and users connected

to the system.

Authentication: Clerk

Clerk is an authentication and user management service that

provides a secure and seamless solution for user registration, login, and

access control.

It will be utilized on this system to handle user

authentication.

Search and Navigation: Mapbox

Mapbox is a powerful mapping platform that provides developers

with customizable maps, geolocation services, and navigation tools. In this

app, the proponents of this study leveraged Mapbox's Geocoding API that

47

converts text addresses into geographic coordinates and the Mapbox

Matrix API to calculate distances and durations between destinations.

Version Control System: Git

Git is a distributed version control system that helps one keep track

of changes to the code over time. In this study, the proponents will use Git

to track changes to this code and GitHub to work on this projects. GitHub

will help keep the code organized and easy to manage.

Version Control Platform: GitHub

GitHub is a web-based platform designed for version control and

collaboration on software development projects. It offers features such as

issue tracking, pull

requests, and branching which streamline the

development process and teamwork. GitHub will be used as a source

code repository for the platform.

Testing: Jest

Jest is a JavaScript testing framework maintained by Meta. Jest will

be used to unit test the platform.

Project Management: Monday.com

Monday.com is a cloud-based project management platform that

helps teams organize, track, and collaborate on their work. It will be used

by the team to manage and track the project’s progress.

48

Business Rules

● Users can register an account as a traveler or business owner. Each

account is exclusive to registered users only.

● When a user registers as a business operator, the user has the option to

specify their establishment into attraction, accommodation, or restaurant

based on their primary offering.

● Users can login to their account.

● Users can logout from their account.

● A traveler can create and manage multiple trips based on their specified

destination, starting location, travel dates, time slots, travel size and

budget.

● Travelers can review and make modifications to their trip plan before

generating the final itinerary.

● A trip can span multiple days with daily itineraries.

● A daily itinerary can contain multiple points of interest (POIs) a traveler

can visit.

● Each point of interest (POI) can belong to multiple categories.

● Each point of interest (POI) can be assigned to multiple daily itineraries

allowing travelers to include the same POI in different daily schedules.

● Travelers must be able to view the daily cost breakdown for

accommodation, attractions, meals, and transportation expenses on their

itinerary.

● Travelers must be able to see the distance, travel time, and estimated cost

between each destination.

● Travelers should be able to view the cost status of each destination

indicating whether it is free or has a specific price.

● Travelers should have access to a map view that displays the locations of

their destinations.

● Travelers have the capability to regenerate their itinerary.

● Travelers can delete their trip.

49

● Each trip can have multiple expenses.

● Travelers can either add expenses linked on their daily itinerary or add

them manually.

● Travelers can specify the amount, date spent, category, and note for each

expense.

● Travelers should have the ability to view their total spending and their

remaining balance during their trip.

● Travelers must be able to see how much they have spent on

accommodation, attraction, transportation, food, and other additional

expenses.

● Travelers can apply date-based filters to categorize and view their

expenses.

● Travelers can edit or delete expenses as needed.

● A traveler can have many preferences for attraction, accommodation and

food.

● A traveler can collect many stamps.

● Travelers collect a stamp for each destination (POI) they visit.

● Free users can create up to three trips.

● Premium users can create an unlimited number of trips.

● Free users are allowed to generate itineraries with a maximum duration of

3 days.

● Premium users have the privilege to generate itinerary with a maximum

duration of 5 days.

● Business operators can create their business profile.

● Business operators can edit their profile.

● Business operators can delete their profile.

50

Figure 4.5 ERD of Destamp

51

SUMMARY, RESULTS, CONCLUSIONS, AND RECOMMENDATIONS

Chapter 5

Summary

This study focuses on simplifying trip planning challenges that has led to

the development of the "Destamp" app. This innovative mobile application,

designed to streamline travel planning in Iloilo City, incorporates features such as

itinerary generation, personalized recommendations, and budget tracking. The

app holds significant potential to streamline trip planning, offering benefits not

only to travelers but also to the local residents, tourist destinations, and business

operators.

Building on the foundation of market validation and surveys, this Software

Development Life Cycle (SDLC) ensures a user-centric approach to the app's

creation. This initial phase allows the researchers to understand the challenges

faced by potential users, as revealed in the survey conducted from July 17 to

July 31. With 319 participants aged 18 to 60, key findings indicate that 47% lack

knowledge in creating itineraries, 54% rely on self-research and booking, 31%

spend a day or more planning trips, and 68% research travel routes before

departure. 84% of respondents consider budget a significant factor and 76%

emphasize staying within budget.

A critical aspect of methodology involves data collection from various

sources. Leveraging a Google Maps Scraper, the proponents gather

comprehensive information on tourist destinations and businesses in Iloilo City.

This data forms a robust foundation for enhancing user experiences within the

app.

The implementation of a freemium model stands out as a strategic

approach in serving diverse user needs. This model allows both free and

premium users to access the app's features, fostering inclusivity and flexibility.

Delving into the specifics of this approach, this research employs

advanced methods to enhance the user experience. Genetic Algorithms power

the itinerary generator, ensuring optimized travel plans. Content-based filtering

refines personalized recommendations, tailoring suggestions to individual

preferences. React Native provides a robust framework for user interfaces,

ensuring a seamless and intuitive experience. Additionally, the integration of the

Mapbox platform enhances the app's mapping capabilities, offering users

interactive and visually appealing representations of their itineraries.

In summary, the "Destamp" app represents a comprehensive solution to

the complexities of travel planning. Through a well-defined methodology,

inclusive business model, and advanced technological approach, Destamp seeks

to transform how individuals plan and experience trips in Iloilo City.

Results

The application of

the Genetic Algorithm significantly rejects the null

hypothesis, which posited that the Genetic Algorithm would not improve travel

recommendations. This enhancement

is supported by unanimous agreement

among all 10 users during testing.

The content-based recommender module consistently aligns itineraries

with travelers' interests, decisively rejecting the null hypothesis that the module

would not significantly align with user preferences. All 10 users during testing

supported this finding.

53

The budget

tracking module proves effective in enabling travelers to

allocate budgets for various trip aspects, as indicated by the rejection of the null

hypothesis by 8 out of 10 users during testing.

The success of Destamp's route optimization module in achieving

significantly more optimal routes is evident in the rejection of the null hypothesis

by 6 out of 10 users during testing. Users' suggestions, including the desire for

real-time routing that

follows the traveler and the request

for attraction

highlighting on the map to explore additional itinerary options, provide valuable

insights for further refinement and enhancement of the route optimization feature.

These user comments indicate an opportunity to address specific user

preferences and expectations, contributing to the continuous improvement of the

app's travel planning capabilities.

Conclusions

The study successfully fulfilled its primary goal of creating, implementing,

and evaluating a budget-based itinerary generator mobile application, thereby

enhancing the travel planning experience. Each module's specific objectives

were accomplished providing valuable insights into the effectiveness of

the

implemented features.

The Genetic Algorithm (GA) incorporated into the itinerary generator

module significantly enhanced the recommendations for optimal

travel

destinations. Simultaneously,

the content-based recommender module, which

uses trip preferences, effectively provided itineraries that were strongly aligned

with each traveler's interests. Furthermore, the budget tracking module proved to

be effective in allowing travelers to allocate budgets for various trip elements.

Lastly, the route optimization module, which aims to minimize travel time and

expenses between destinations, made significant contributions towards more

optimal routes.

54

This study surpassed its objectives by developing a mobile application that

enhances the travel planning experience. The successful

implementation and

validation of each targeted module, namely the Genetic Algorithm-driven

recommendations, content-based itineraries, effective budget allocation, and

optimized routes, collectively contribute to a comprehensive and user-centric

travel planning solution.

Recommendations

Building upon the study's positive outcomes, particularly the successful

implementation of Genetic Algorithm-driven recommendations, content-based

itineraries, effective budget allocation, and optimized routes,

the following

recommendations are proposed.

1. Use AI to generate personalized itineraries based on users' past travel

experiences, preferences, and current needs. This can be done by

analyzing user behavior and feedback from previous travels.

2. For enhanced mapping features, users suggest

integrating real-time

route optimization directly into the map interface. This would provide a

dynamic and responsive experience for travel planning.

3. Allow users to customize their itineraries after they have been generated.

This could include adding or

removing destinations, changing the

sequence of activities, or adjusting the budget.

4.

Implement a feature that updates the user's itinerary in real-time based

on current conditions. If the user is planning to visit a museum, the app

could notify them if the museum is closed due to maintenance. This

feature could also alert users about price changes, discounts, or deals

that could help them save money on their trip.

55

5.

In terms of business owner

features, social media integration is

recommended. Enabling business owners to seamlessly integrate their

social media accounts into the app enhances the visibility and

engagement of businesses on the platform. Additionally, allowing

business owners to create custom tags or categories for

their

establishments provides

flexibility

for personalized and accurate

categorization.

56

APPENDIX

User Stories

Specific Objectives

Epic

User Story

Status

Addressed

To design, develop,

User

As a user, I want to be able to create

and test an

Authentication

an account so that I can access the

itinerary generator

module that utilizes

a Genetic

Algorithm (GA) to

recommend

near-optimal

combinations of

destinations based

on user input

factors like budget

and travel

constraints.

platform's features and services.

As a user, I want to be able to log in

to my account so that I can securely

access my profile and interact with

the platform.

As a user, I want to be able to log out

of my account so that I can protect

my account from unauthorized

access.

Trip

As a traveler, I want to be able to

Management

view my trips so that I can easily

keep track of my past and upcoming

travel plans.

As a traveler, I want to be able to

delete my trip so that I can remove

travel plans that are no longer

relevant or necessary.

As a traveler, I want to be able to

review my trip details before

generating an itinerary so that I can

make sure all the information is

correct.

As a traveler, I want to be able to

discard a trip so that I can avoid

generating an itinerary for a trip that

I've decided not to proceed with.

As a traveler, I want to be able to

regenerate my itinerary so that I can

57

explore alternative options and

arrangements for my journey.

As a traveler, I want to be able to

claim my stamps.

Itinerary

As a traveler, I want to be able to

Generation

enter my trip details, such as my

destination, departure area, dates of

travel, travel group size, and budget

so that the itinerary generator can

create an itinerary that meets my

needs.

As a developer, I want to implement

an algorithm that can analyze input

provided by travelers, allowing me to

generate optimized travel itineraries.

Trip Viewing

As a traveler, I want to view my

multi-day itinerary in a clear timeline

format, so that I can easily

understand the sequence of

activities and events throughout my

trip.

As a traveler, I want to be able to

view more details about a

destination on my itinerary.

As a traveler, I want to see a detailed

breakdown of each day's activities,

including timings so that I can stay

organized and ensure a smooth flow

of events during my journey.

As a traveler, I want to have a map

view integrated into my itinerary, so

that I can quickly understand the

geographical layout of my trip and

how activities are distributed across

different areas.

58

Business Profile

As a business operator, I want to be

Management

able to add my business profile so

that I can provide accurate and

up-to-date information about my

establishment.

As a business operator, I want to be

able to edit my business profile so

that I can make necessary updates

to reflect any changes in my

establishment's details.

As a business operator, I want to be

able to delete my business profile so

that I can remove my establishment

from the app if needed.

As a business operator, I want to be

able to view my business profiles so

that I can manage multiple

establishments efficiently.

As a business operator, I want to be

able to view my business profile

details so that I can review and verify

all the specific information that users

will see.

User Profile

As a user, I want to be able to view

Management

my profile so that I can review the

information associated with my

account.

As a user, I want to be able to edit

my profile so that I can keep my

personal details up-to-date.

To design, develop,

Personalized

As a developer, I want to integrate a

and test a

Itinerary

recommendation engine that

content-based

Generation

suggests activities based on user

recommender

module that will

leverage trip

preferences to

preferences so that the generated

itineraries are aligned with individual

interests

59

offer tailored

recommendations

for attractions,

dining options, and

accommodations

ensuring that the

provided

suggestions are

better aligned with

each traveler's

interests.

To design, develop,

Budget

As a traveler, I want to be able to add

and test a budget

Management

my expenses so that I can record

tracking module

enabling travelers

to allocate budgets

for various trip

aspects.

and track each spending.

As a traveler, I want to be able to

view my expenses so that I can

review spending details.

As a traveler, I want to be able to edit

my expenses so that I can correct

any mistakes or update information

to the recorded expenses.

As a traveler, I want to be able to

delete my expenses so that I can

remove any irrelevant or duplicate

entries from my expense records.

As a traveler, I want to automatically

add my expenses.

To design, develop,

Route

As a traveler, I want the itinerary tool

and test a route

Optimization

to suggest optimal routes between

optimization

module that

optimizes routes

between

destinations to

minimize travel

time and expenses.

destinations so that I can efficiently

navigate my trip and minimize travel

time.

Table 5.1 User Stories

60

Usability Report

Age

Gender

Travel Experience

Budget

Range

Travel Purpose

Tech

Income

Proficiency

Level

21

21

22

41

37

22

44

49

20

M

M

M

F

M

F

F

M

F

Occasional

1k - 3k

leisure, family vacation

Frequent

1k - 3k

leisure, family

Occasional

1k - 3k

leisure, family vacation

Frequent

9k above

leisure, family

vacation, business

travel

Holiday Traveler

6k - 9K

Family Vacations

Occasional

1k - 3k

leisure

Annual Vacationer

9k above

family vacation

Annual Vacationer

3k - 6k

Family Vacation

Frequent Traveler

3k-6k

Leisure, Family

Vacation

Table 5.2. Traveler Test Participants

9

9

9

9

9

9

7

7

9

none

none

none

50k - 100k

50k - 100k

none

50k - 100k

50k - 100k

none

Age

Gender

Business Type

Business Size

Years in

Listing Update

27

22

21

33

45

M

F

F

M

M

Food Establishment

Small business

Food Establishment

Small business

Food Establishment

Small business

Accommodation

Small Business

Business

Frequency

3

1

2

3

frequently

frequently

frequently

occasionally

Attraction

Large Business

120

occasionally

Table 5.3. Business Operators Test Participants

61

Participant

Objective 1

Objective 2 Objective 3

Objective 4

Participant 1

Participant 2

Participant 3

Participant 4

Participant 5

Participant 6

Participant 7

Participant 8

Participant 9

Participant 10

1

1

1

1

1

1

1

1

1

1

1

1

1

1

1

1

1

1

1

1

SUM

10

10

1

1

1

0

1

0

1

1

1

1

8

1

1

1

0

0

0

1

1

0

1

6

Success Rate

100%

100%

80%

60%

Table 5.4. Traveler Objective Completion

62

Task

Description

Occurred

Objective 3

Users face difficulty locating the entered

budget within the itinerary screen.

The user lacks the knowledge of how to

Objective 3

incorporate a budget into a specific

Objective 4

itinerary.

Users express concerns about the map's

size.

Users encounter issues with the map,

Objective 4

expressing a desire for more direct

navigation to specific locations.

2

2

3

2

Table 5.5. Traveler Errors and Feedback

Participant

Participant 1

Participant 2

Participant 3

Participant 4

Participant 5

SUM

Task 1

1

1

1

1

1

5

Success Rate

100%

Table 5.6. Business Operator Objective Completion

63

Observation

Interpretation

Severity

Recommendations

Users may struggle to

Implement clear and intuitive

locate and manage budget

entries, impacting user

Medium

labels for budget-related

features.

The budget screen lacks

clear labels, leading to

confusion.

Mapping features display

route inaccuracies,

affecting user navigation

experience.

satisfaction.

Users may encounter

difficulty navigating due to

the misalignment of the

High

route with the actual

location.

Business operators lack

direct communication

options.

Direct communication is

vital for business operators

to engage with travelers.

High

messaging, to facilitate direct

Enhance mapping features to

ensure precise alignment of

the route with the destination

point, providing a more

accurate and user-friendly

navigation experience.

Integrate communication

channels, such as email or

interaction between users and

business operators.

Enhance mapping features to

include real-time routing,

meeting user expectations for

dynamic and accurate

navigation information.

Users may encounter

Mapping features do not

difficulty navigating due to

currently offer real-time

the lack of real-time routing.

data, impacting user

The suggestion for real-time

navigation accuracy. Users

routing indicates a user

have expressed a desire

expectation for dynamic

for real-time routing.

and up-to-date navigation

information.

High

Table 5.7. User Recommendation

64

Sequence Diagrams

A. User Actor

Figure 5.1 User Actor for Sequence Diagram

The user actor represents the Traveler and Business Operator that will be

interacting with the platform.

B. Destamp Mobile Client Participant Group

Figure 5.2 Destamp Mobile Client Participant Group for Sequence Diagram

The Destamp Mobile Client Participant Group represents the platform as a

whole that the users will interact with.

C. User interface Participant

Figure 5.3 User interface Participant for Sequence Diagram

65

The User interface Participant represents the component of the mobile

client that displays the user interface and allows them to interact with it.

D. Business Logic Layer Participant

Figure 5.4 Business Logic Layer Participant for Sequence Diagram

The Business Logic Layer Participant represents the component of the

web client that is responsible for performing calculations to process information

for the user interface to display. It acts as a bridge between the user interface

and data access layer in order to process the data flowing between them.

Figure 5.5 User Registration Sequence Diagram

66

Figure 5.6 User Login Sequence Diagram

Figure 5.6 User Logout Sequence Diagram

67

Figure 5.7 Create Trip Sequence Diagram

68

Figure 5.8 Regenerate Trip Sequence Diagram

69

Figure 5.9 Create/Edit/Delete Expense Sequence Diagram

70

Figure 5.10 Create/Edit/Delete Business Profile Sequence Diagram

71

Platform Screenshots

Figure 5.11 User Login and Create Account Screen

72

Traveler

Figure 5.12 My Trips Screen

Figure 5.13 Profile Screen

Figure 5.14

Subscription Screen

73

Figure 5.15 Create Trip Screen

Figure 5.16 Review Trip Screen

74

Figure 5.17 Itinerary Screen

75

Figure 5.18 Add Expense Form

Figure 5.19 Expenses Screen

76

Figure 5.20 Claim Stamp Screen

Figure 5.21 Stamp Screen

77

Business Operator

Figure 5.21 My Business Screen

Figure 5.22 Profile Screen

78

Figure 5.23 Add Business Profile Screen

79

Figure 5.24 Business Profile

Figure 5.24 Edit Business

Details Screen

Screen

80

References

Black, S. (2017). How Much Time Does It Take to Research and Plan a Family

Vacation. Retrieved July 23, 2023 from https://www.vacationkids.com/v

acations-with-kids/How-much-time-does-it-take-to-research-and-plan-a-fa

mily-vacation#:~:text=When%20people%20pull%20the%20trigger,a%20n

ew%20and%20unfamiliar%20destination.

Coves-Martínez, Á.L. et al. (2023). How to improve travel-app use continuance:

The moderating role of culture. Retrieved July 27, 2023 from

https://www.sciencedirect.com/science/article/pii/S2211973622001350.

Department of Tourism, Dr. Andrew L. Tan Center for Tourism, & Guide to the

Philippines (DOT, ALTCFT, GTTP). (2021). The Philippine Travel Survey

Report: The Evolving Landscape of Domestic Travel in the Philippines.

Retrieved July 26, 2023, from https://docplayer.net/213256503-The-evolv

Ing-landscape-of-domestic-travel-in-the-philippines-a-study-of-travelers-an

d-tourism-enterprises-amidst-the-pandemic.html. and https://drive.

google.com/file/d/1o00mP7js2_T-APwsF7Vd5aHg9Wpoy49e/view.

Destination Analysts. (2019). The Future of Travel-Planning Apps. Retrieved July

18, 2023 from https://www.destinationanalysts.com/welcome-to-2019-

american-traveler-sentiment-weakens-2-2/.

Dhrubok Infotech Services Limited. (2022). 6 Advantages of Travel Apps in

Travel and Tourism Industry. Retrieved July 23, 2023 from https://dhruboki

nfotech.com/blog/adVantages-of-travel-apps.

Focused Travels. (2022). Factors to Consider when Choosing a Travel

Destination. Retrieved July 20, 2023 from https://focusedtravels.com/trav

El-destination.

81

Global Data. (2023). Travel Apps – Thematic Intelligence. Retrieved July 21,

2023 from https://www.globaldata.com/store/report/travel-apps-them

e-analysis/.

Ho, R.C. & Muslim, A. (2019). What Drives the Adoption of Smart Travel Planning

Apps? The Relationship between Experiential Consumption and Mobile

App Acceptance. Retrieved July 28, 2023 from https://knepublishing.com

/index.php/Kne-Social/article/view/5356/10577#info.

Huang, F. (2021). Multi-Task Travel Route Planning With a Flexible Deep

Learning Framework. IEEE Journals & Magazine | IEEE Xplore. Retrieved

August 1, 2023 from https://ieeexplore.ieee.org/document/9115053.

Jain, A. (2019). Is planning your travel taking up more time than you have?

Medium. Retrieved July 28, 2023 from https://medium.com/nyc-design/

Is-planning-your-travel-taking-up-more-time-than-you-have-e7a606999ea.

Lena, P. (2023). Heritage sites, good food still Iloilo City’s best tourist draw.

Philippine News Agency. Retrieved July 13, 2023 from https://www.pna

.gov.ph/articles/1202676.

Lim, K. (2016). Recommending and Planning Trip Itineraries for Individual

Travellers and Groups of Tourists. Retrieved July 24, 2023 from

https://www.researchgate.net/publication/301547665_Recommend

ing_and_Planning_Trip_Itineraries_for_Individual_Travellers_and_Grou

ps_of_Tourists.

BusinessWorld Publishing. (2021). AirAsia: 7 out of 10 Filipinos are still keen on

traveling. Retrieved July 24, 2023 from https://www.bworldonline.com

/corporate/2022/01/14/423523/airasia-7-out-of-10-filipinos-still-keen-on-tra

veling/.

82

Nguyen, A. & Shoubber, O. (2019). Trippit: An Optimal Itinerary Generator.

Retrieved July 30, 2023 from https://scholarcommons.scu.edu/cgi/view

content.cgi?article=1154&context=cseng_senior.

Schmitt, L. A., Delbosc, A., & Currie, G. (2018). Learning to use transit services:

adapting to unfamiliar transit travel. Transportation, 46(3), 1033–1049.

Retrieved July 25, 2023 https://doi.org/10.1007/s11116-018-9880-9.

Sia, P.Y.H (2022). Systematic review of mobile travel apps and their smart

features and challenges. Retrieved July 26, 2023 from https://www.e

merald.com/insight/content/doi/10.1108/JHTI-02-2022-0087/full/

html?skipTracking=true.

Silva, S. (2018). 5 Reasons why having a Travel Itinerary is Important. Retrieved

July 27, 2023 from https://www.northsouthtravel.com/5-reasons-why-havin

g-a-travel-itinerary-is-important#:~:text=Travel%20itineraries%20ens

ure%20that%20you,you%20can%20be%20more%20flexible.

Statista. (2023). Number of international tourist arrivals worldwide 1950-2022.

Retrieved July 20, 2023 from https://www.statista.com/statistics

/209334/total-number-of-international-tourist-arrivals/.

Booking.com. (2023). Travel Predictions 2023. Retrieved July 24, 2023 from

https://www.booking.com/articles/travelpredictions2023.html.

Xiong-Bin, W., Guan, H., Han, Y., & Ma, J. (2017). A tour route planning model

for tourism experience utility maximization. Advances in Mechanical

Engineering, 9(10), 168781401773230. Retrieved August 1, 2023 from

https://doi.org/10.1177/1687814017732309.

83

