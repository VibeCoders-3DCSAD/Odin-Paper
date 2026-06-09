On the human-centered AI transformation of
banking: Exploring the impact of behavioral
finance & AI on banking transformation
Authors van Thiel,H.B.
DOI 10.26116/tsb.4096899
Publication Date 2025-01-08
Document Version publishersversion
Link https://research.tilburguniversity.edu/en/publications/44fed669-8c39-4966-
a784-b2de8154e188
Citation van Thiel, H B 2025, 'On the human-centered AI transformation of banking :
Exploring the impact of behavioral finance & AI on banking transformation',
Doctor of Philosophy, s.l.. https://doi.org/10.26116/tsb.4096899
Download Date 2026-05-10 09:37:00
Rights General rights
Copyright and moral rights for the publications made accessible in the public
portal are retained by the authors and/or other copyright owners and it is a
condition of accessing publications that users recognise and abide by the legal
requirements associated with these rights.
- Users may download and print one copy of any publication from the public
portal for the purpose of private study or research.
- You may not further distribute the material or use it for any profit-making
activity or commercial gain
- You may freely distribute the URL identifying the publication in the public
portal"
Take down policy
If you believe that this document breaches copyright please contact us
providing details, and we will remove access to the work immediately and
investigate your claim.

On
The Human-Centered AI Transformation
of Banking
Exploring the impact of behavioral finance & AI
on banking transformation
Diederick van Thiel
1

Lay-out & drukwerk : Studio | powered by Canon
ã 2024: Diederick van Thiel, The Netherlands. All rights reserved. No part of this publication may be
reproduced, stored in a retrieval system, or transmitted, in any form or by any means, electronic, photocopying,
or otherwise, without the permission of the author, or, when appropriate, of the publishers of the publications.
This dissertation was made possible by financial support of AdviceRobo.com & E-cology Innovations.
22

On
The Human-Centered AI
Transformation of Banking
Exploring the impact of behavioral finance & AI
on banking transformation
Proefschrift
ter verkrijging van de graad van doctor aan Tilburg University op gezag van de rector magnificus, prof. dr.
W.B.H.J. van de Donk, in het openbaar te verdedigen ten overstaan van een door het college voor promoties
aangewezen commissie in de aula van de Universiteit op 8 januari 2025 om 14.00 uur
door
Henricus Bartholomeus van Thiel
Geboren op 13 juli 1968 te Maastricht
33

44

Promotores : Prof. Dr. J. Goedee (Tilburg University)
Prof. Dr. R.TA.J. Leenders (Tilburg University)
Leden promotiecommissie : Prof. Dr. L.A.G. Oerlemans (Tilburg University)
Prof. Dr. M. Chen (Cardiff University)
Prof. Dr. B. Bosma (Tilburg University)
Prof. Dr. Ir. J.M.L. van Engelen (TU Delft)
CNL-Studio Tilburg University
©2025 Henricus Bartholomeus van Thiel, The Netherlands. All rights reserved. No parts of this thesis
may be reproduced, stored in a retrieval system or transmitted in any form or by any means without
permission of the author. Alle rechten voorbehouden. Niets uit deze uitgave mag worden
vermenigvuldigd, in enige vorm of op enige wijze, zonder voorafgaande schriftelijke toestemming
van de auteur.
4 55

“We think, each of us, that we are much more rational than we are. And we think we make our
decisions because we have good reasons to make them. Even if it’s the other way around. We
believe in reasons because we’ve already made the decision. But in practice we make
financial decisions based on emotions rather than rationality”
(Daniel Kahneman, Professor of Psychology at Princeton University & Amos Tversky, Professor of Psychology
at Stanford University; Founding fathers of behavioral finance & winners of the Nobel Price for Economy.)
“Artificial intelligence is not a substitute for human intelligence; it is a tool to amplify human
creativity and ingenuity.”
(Fei-Fei Li, Sequoia Capital Professor, Denning Co-Director of the Stanford Institute for Human-Centered AI
(HAI), Senior Fellow at HAI and Professor, by courtesy, of Operations, Information and Technology at the
Graduate School of Business).
“AI will enhance human capabilities rather than replace them.”
(Satya Nadella, CEO Microsoft).
For Rosali, Rutger-Guy, Roderick, Maurits, Lily Roos, Mum and Dad &
all financially underserved people in the world
66

Contents
Chapter 1 : Introduction
Chapter 2 : Explaining the customer experience of digital advice
Chapter 3 : Targeting the Robo-advice Customer: The Development
of a Psychometric Segmentation Model
for Financial Advice Robots
Chapter 4 : Leveraging financial personality
for inclusive credit scoring amidst global uncertainty
Chapter 5 : Artificial Intelligent Credit Risk Prediction
Chapter 6 : Responsible Access to Credit for Sole-Traders
and Micro-Organisations under Unstable Market Conditions
with Psychometrics
Chapter 7 : Conclusion
77

In our journey through this dissertation, we begin by setting the stage with Banking 5.0 and
the principles of human-centered AI, exploring how these transformative forces are shaping
the financial industry. The first chapter delves into how these concepts drive inclusivity and
accessibility in financial services. With this groundwork, we will next explore how these
technologies can be harnessed to elevate inclusive customer experiences, particularly through
digital advisory services and inclusive credit decision making.
88

Chapter 1
Introduction

Chapter 1
HUMAN-CENTERED AI TRANSFORMING BANKING benefits, such as transparency, accessibility, and security that interact well with the evolving
demands of the next generations for financial services like digital accessibility, instantaneity,
personalization, and sustainability (Far et al, 2023). This shift currently propels a transition
towards embedded finance (EmFi). EmFi is the integration of financial services into the
1| INTRODUCTION customer offerings of non-financial institutions (Ozili, 2023). EmFi allows non-financial
companies like retailers, game providers and social media environments to incorporate
1.1.Towards the Banking 5.0 paradigm financial services into their payments journey through easy-to-use application programming
In recent decades, the rise of new technologies has significantly boosted organizational interface (API) integrations that are modular by design.
efficiency (Maddikunta et al., 2021). Technology, coupled with political and economic
factors, stands as a key driver shaping the future of banking (Mehdiabadi et al., 2022). The Another example of such a decentralized environment for embedded finance is the Metaverse
progression towards Industry 5.0 in banking is rooted in the fundamental value of inclusive (Far et al., 2023). The Metaverse is the post-reality universe, a perpetual and persistent
human-centricity, supporting the Sustainable Development Goals (SDGs) outlined by the multiuser environment merging physical reality with digital virtuality (Mystakidis, 2022). It is
United Nations. These SDGs, namely 1, 8, 9, 10, and 16, underscore the significance of based on the convergence of technologies that enable multisensory interactions with virtual
financial inclusion in empowering individuals, mitigating poverty and inequalities, fostering environments, digital objects and people such as virtual reality (VR) and augmented reality
economic growth and entrepreneurship, and fortifying inclusive and resilient societies. (AR). In the Metaverse digital advisors and mobile apps, often evolving into super apps, serve
Financial inclusion refers to a process that ensures the ease of access, availability, and usage as virtual guardian angels in the realm of inclusive responsible Banking 5.0. These platforms
of the formal financial system for all members of an economy. It facilitates the efficient leverage advanced technologies such as augmented reality and deep learning to provide
allocation of productive resources and thus can potentially reduce the cost of capital (Sarma & hyper-personalized financial advice and assistance to users. By integrating virtual assistants
Pais, 2011). Endeavors to promote financial inclusion are in line with broader development and AI-driven algorithms, these tools offer unparalleled convenience and accessibility,
aims and can significantly contribute to achieving the SDGs. Tech-savvy younger generations, empowering individuals to manage their finances effectively from anywhere, at any time.
such as millennials and Gen Z, demonstrate a greater inclination towards sustainable Moreover, as the digital landscape continues to evolve, these platforms are poised to play a
consumption facilitated by advanced integration between smart systems in their personal and pivotal role in shaping the emerging metaverse of banking, where virtual interactions and
professional lives compared to preceding generations. When offered ethically and sustainably immersive experiences redefine the way we engage with financial services. In this metaverse,
in a well-regulated environment, digital financial inclusion encourages development and digital advisors and mobile apps serve as gateways to a dynamic ecosystem of financial
accelerates progress toward the Sustainable Development Goals (SDGs) (Tay et al., 2022). opportunities, seamlessly integrating with emerging technologies to provide holistic and
inclusive financial wellness driving banking experiences for users across the globe. The
While Industry 4.0 is predominantly technology-driven, the shift to Industry 5.0 is dissertation focuses on the lending market and the role of AI applications in fostering
characterized by a focus on the intelligent integration of inclusive human-centered values. In inclusive lending by utilizing psychometric and attitudinal insights. These personal data-
this context, behavioral finance surpasses traditional advice notably across various driven innovations are explored in the context of these innovative financial environments,
dimensions, such as enhancing investor or borrower trust, improving the perceived which, together, are referred to as the "Banking 5.0 paradigm. This paradigm represents the
advantages of financial advice, and increasing the likelihood of adhering to such advice integration of advanced technologies to create a more inclusive and personalized financial
(Dharma, 2022; Lewis et al., 2021). Nonetheless, to the best of my knowledge, there has been ecosystem.
minimal research exploring the shift to inclusive responsible Banking 5.0 from a behavioral
finance perspective. This dissertation seeks to bridge this gap by introducing a pioneering The main research question of this dissertation focuses on understanding how integrating
behavioral psychometric finance framework. This framework facilitates a deeper behavioral and psychometric finance principles can enhance human-centered AI technologies.
understanding of the underlying behavioral traits influencing responsible and irresponsible The goal is to see how these technologies can support the transition to technology-driven
financial behaviors, essential for inclusive financial advice and risk management. Such inclusive and responsible banking within the Banking 5.0 framework. Additionally, the study
insights are crucial for transitioning banking towards the inclusive, predictive, and automated explores what strategies can be developed based on this integration to further improve the
era of Banking 5.0. financial sector.
Modern financial innovations come in many forms such as open finance (OpFi) – the use of Technological leaps from the beginning of industrialization have caused extensive changes in
API’s to promote information sharing between financial institutions, while simultaneously the process of business (efficiency) development and innovation. Hence, these effects can be
giving consumers more control about how their personal financial information is used and by introduced as industrial revolutions. The industrial revolutions are presented in table 1.
whom (Awrey & Macey, 2023), sustainable finance (SuFi) - the integration of environmental,
social, and governance (“ESG”) issues into financial decisions (Edmans & Kacperczyk,
2022), social finance (SoFi) – social or peer interactions driving financial decion making
(Kuchler & Stroebel, 2021), decentralized finance (DeFi) – the decentralized provision of
financial services using distributed ledger technology (Zetsche et al, 2020), and so on. They
exist mainly to increase access to finance for specific activities or projects (Ozilli, 2023).
Specifically, DeFi technology operates on a decentralized platform and offers various
1100 11

Introduction
benefits, such as transparency, accessibility, and security that interact well with the evolving
demands of the next generations for financial services like digital accessibility, instantaneity,
personalization, and sustainability (Far et al, 2023). This shift currently propels a transition
towards embedded finance (EmFi). EmFi is the integration of financial services into the
customer offerings of non-financial institutions (Ozili, 2023). EmFi allows non-financial
companies like retailers, game providers and social media environments to incorporate
financial services into their payments journey through easy-to-use application programming
interface (API) integrations that are modular by design.
Another example of such a decentralized environment for embedded finance is the Metaverse
(Far et al., 2023). The Metaverse is the post-reality universe, a perpetual and persistent
multiuser environment merging physical reality with digital virtuality (Mystakidis, 2022). It is
based on the convergence of technologies that enable multisensory interactions with virtual
environments, digital objects and people such as virtual reality (VR) and augmented reality
(AR). In the Metaverse digital advisors and mobile apps, often evolving into super apps, serve
as virtual guardian angels in the realm of inclusive responsible Banking 5.0. These platforms
leverage advanced technologies such as augmented reality and deep learning to provide
hyper-personalized financial advice and assistance to users. By integrating virtual assistants
and AI-driven algorithms, these tools offer unparalleled convenience and accessibility,
empowering individuals to manage their finances effectively from anywhere, at any time.
Moreover, as the digital landscape continues to evolve, these platforms are poised to play a
pivotal role in shaping the emerging metaverse of banking, where virtual interactions and
immersive experiences redefine the way we engage with financial services. In this metaverse,
digital advisors and mobile apps serve as gateways to a dynamic ecosystem of financial
opportunities, seamlessly integrating with emerging technologies to provide holistic and
inclusive financial wellness driving banking experiences for users across the globe. The
dissertation focuses on the lending market and the role of AI applications in fostering
inclusive lending by utilizing psychometric and attitudinal insights. These personal data-
driven innovations are explored in the context of these innovative financial environments,
which, together, are referred to as the "Banking 5.0 paradigm. This paradigm represents the
integration of advanced technologies to create a more inclusive and personalized financial
ecosystem.
The main research question of this dissertation focuses on understanding how integrating
behavioral and psychometric finance principles can enhance human-centered AI technologies.
The goal is to see how these technologies can support the transition to technology-driven
inclusive and responsible banking within the Banking 5.0 framework. Additionally, the study
explores what strategies can be developed based on this integration to further improve the
financial sector.
Technological leaps from the beginning of industrialization have caused extensive changes in
the process of business (efficiency) development and innovation. Hence, these effects can be
introduced as industrial revolutions. The industrial revolutions are presented in table 1.
1111

Chapter 1
Table 1
Industrial Revolutions and General Purpose Technologies
Industry 1.0 Industry 2.0 Industry 3.0 Industry 4.0 Industry 5.0
Timeframe
(1760 –1840) (1870 –1969) (1970 -2000) (2000 -2030) (2030 -->)
General • Steam engine • Electricity in • Information & • Cloud computing • Human-machine
Purpose • Waterpower industrial processes communication • Narrow AI integration
Technologies • Massproduction technology • Internet-of-things • Augmentedreality
• Industrial • Robo-proces • Hyper-
automation automation personalization
technologies
• Sustainable
technologies
• Advancedrobotics
Organizations are interested in using the benefits of innovation to meet the needs of their
customers as well as to obtain useful information from them (Nethravathi et al., 2020). The
development of new technologies and their increasing democratisation have enabled the
digitalisation of the banking domain (Rozanec et al., 2023). In the course of the industrial
revolutions, five major changes in industry throughout history are considered. While Industry
5.0 is considered the next industrial development, its goal is to use the creativity of human
experts in collaboration with efficient, intelligent, and accurate machines, to achieve
production solutions with more efficient and user-friendly resources compared to Industry
4.0 (Motienko, 2020). The invention of the steam engine (between 1760 and 1840) defines the
first industrial revolution. The second industrial revolution is defined by the use of electricity
in industrial processes (between 1870 and 1969). The third revolution began in the 1970s with
the use of information and communication technology and industrial automation, and the
fourth industrial revolution (Industry 4.0) emerged from several developed countries, in a
public-private initiative in Germany to build smart factories by integrating physical objects
with digital technologies (Hermann et al., 2016). The main elements that describe the stages
of Industry 4.0 are the profound change in the connection of production systems due to the
integration of information and communication technology (Motienko, 2020) in the internet-
of-things (Mehdiabadi et al.,2020; Noreen et al. 2023)), machines in cyber-physical systems
(Jamal et al. 2021), big data analyses (Sung et al. 2021), 3D printing (Soo et al. 2021),
advanced robotics (Parmar et al. 2022), intelligent sensors (Yu et al. 2022), augmented reality
(Bryceson et al. 2022), cloud computing (Vinoth et al. 2022), artificial intelligence (Noreen et
al. 2023), nano technology (Koc, 2021) and human machine interfaces (Gorodesky et al.,
2019). Progress towards Industry 4.0 has had a significant impact on the industry, and this is
based on the establishment of intelligent factories, intelligent products, and intelligent
services based on the Internet of Things and services connected to the industrial Internet
(Kagermann, 2015). In their study, Xu et al. (2021) have illustrated that the beginning of the
transition from Industry 4.0 to Industry 5.0 is understood to recognize the power of industry
to achieve societal goals beyond jobs and growth, to become a resilient provider of prosperity
by making production respect the boundaries of our planet and placing the wellbeing of the
industry worker at the center of the production process. Industry 5.0 is expected to integrate
high-speed, high-precision machines with critical and human cognitive thinking. Hyper-
personalization is another important affordance of Industry 5.0 as customers can choose
personalized and customized products according to their tastes and needs. Industry 5.0
significantly increases production efficiency, creating human-machine adaptability, and
enabling responsibility for interaction and continuous monitoring activities. The goal of
1122

Introduction
human-machine cooperation is to increase production at a high rate. Industry 5.0 can increase
production quality by assigning repetitive and uniform tasks to robots/machines and tasks that
require critical thinking for humans (Motienko, 2021).
The primary function of a bank is to gather funds, known as deposits, from individuals with
surplus money, consolidate these funds, and then lend them to those in need of financial
assistance (International Monetary Fund, 2023). Additionally, banks engage in various other
activities, making banking the intermediary between depositors, who provide money to the
bank, and borrowers, who receive loans from the bank. Banking, being one of the largest
active industries, is also evolving through the adoption of general-purpose technologies.
To capitalize on prevailing conditions, banks must strive to establish an integrated system
aimed at facilitating inclusive and mobile banking processes. As illustrated in table 2,
Banking 4.0 focuses on offering personalized, customer-centric experiences through digital
channels and embraces innovative solutions offered by FinTech companies. Banking 5.0
places emphasis on seamlessly integrating technology with human touchpoints to enhance
customer experiences, with a particular focus on sustainable banking (Nicoletti, 2021).
Banking 5.0 envisions banks acting as platforms that collaborate with various ecosystem
partners to provide comprehensive financial and non-financial services.
The evolution towards Banking 5.0 is not solely attributable to new inventions but rather to
the maturation and proliferation of technologies such as artificial intelligence, virtual and
augmented reality, and voice recognition systems, which collectively form a potent
combination for advancing banking services and addressing contemporary banking challenges
(Shahabi et al., 2020). Banking is not confined solely to traditional banks. It should instead be
integrated into the operations and responsibilities of all organizations and individuals. Routine
tasks and business activities should incorporate banking whenever and wherever required.
Even non-financial transactions should accurately document banking activities for the benefit
of the customer. This does not imply that every business or individual must function as a
bank. Rather, banking transactions should seamlessly integrate into their regular operations.
The initiation and processing of these transactions should typically be handled by an external
entity, which, if necessary, holds a banking license to ensure the reliability and trustworthiness
of the transaction for the customer. In essence, the focal point of the transaction should be the
customer and their needs, prioritizing customer-centricity over the bank's interests.
1133

Chapter 1
Table 2

Overview of the Transformation of Banking

Paradigms of  Traditional banking Digital & Smart banking Human-Centered & Sustainable banking
Lending
|     | Banking evolution | (1760 –1969) |     | (1970 –2030) | (2025 –2050)  |     |
| --- | ----------------- | ------------ | --- | ------------ | ------------- | --- |
Business Model
| Components |     | Banking 1.0 –3.0 | Banking 4.0 |     | Banking 5.0 |     |
| ---------- | --- | ---------------- | ----------- | --- | ----------- | --- |
• M a s s - p e r s o n a li z a ti o n
|     |     | • T r a d it io n a l   m ar k e t in g  &   b randing | • M a s s   m a r k e t i n | g   | • P e r s o n a l iz e d   m | a r k e t i n g  &  b r a n d in g |
| --- | --- | ------------------------------------------------------ | --------------------------- | --- | ---------------------------- | ---------------------------------- |
Marketing & Customer acquisition • R e la t io n s h i p  m a n a g e m e n t • D ig i t a l  m a r k e t i n g  &   b ra n ding • E c o - s y s t e m   m a r k e t i n g     &  b r a n d in g
|     |     |     | • Co - m a r k e t i n g   & |   b ra n d in g | • E S G - im p a c t   t r a | n s p a r e n c y |
| --- | --- | --- | ---------------------------- | --------------- | ---------------------------- | ----------------- |
• Hyper-personalization
|     |     | • B r a n c h e s | • O m n i- c h a n n e l |     | • D i g i t a l e c o - sy s t | em   p l a t fo rms andhybrid |
| --- | --- | ----------------- | ------------------------ | --- | ------------------------------ | ----------------------------- |
Financial advice & Loan Origination • Tr a d i t io n al advice • D i g i t a l   p r o c e s s e s • O m n i- c h a n n e l &  s o c i a l
|     |     |     | • D i g i t a l   t o o l s   &   a | dvice | • D i g i t a l ,   in s t a n t   | p r o c e ss e s |
| --- | --- | --- | ----------------------------------- | ----- | ---------------------------------- | ---------------- |
• Robo-advice& virtual assistance
|     |     | • M a n u a l   u n d e r w r i t in g | • D ig i t a l   u n d e r w r | i t i n g               | • C o n t i n o u s ,   i n c l | u s i v e u n d e r w r it i n g |
| --- | --- | -------------------------------------- | ------------------------------ | ----------------------- | ------------------------------- | -------------------------------- |
|     |     | • P e r s o n a l   j u d g e m e n t  | • B o r r o w e r b e h a      | v i o r - c e n t r i c | • B o r r o w e r l i f e - c   | e n t r i c                      |
Underwriting & Risk management • B o r r o w e r c h a r a c t e r - c e n tricrisk management • P r o f i t - f o c u s s e d c r e d it   s c o r e   c a r d s • L i f e   c e n t r i c s c o r e   c a r d s   t h a t i n c l u d e
|     |     | • E m e r g i n g e x p e r t   m o d e ls | • L o g i s t i c r e g r e s s | i o n &   h i s t o r i c a l d a t a            | e n v i r o n m e n t a l       | &   s o c i a l c o s t s                  |
| --- | --- | ------------------------------------------ | ------------------------------- | ------------------------------------------------ | ------------------------------- | ------------------------------------------ |
|     |     | • R e a c t i v e m o n i t o r i n g      | • P r o a c t i v e m o n i     | t o r i n g   ( e a r l y w a r n i n g systems) | • A I   a n d d y n a m i c     | d a t a d r i v e n r i s k   m a nagement |
|     |     |                                            |                                 |                                                  | • P r e s c r i p t i v e m     | o n i t o r i n g                          |
|     |     |                                            |                                 |                                                  | • H u m a n   c e n t e r e     | d f i n a n c ia l   w e l ln e s s        |
|     |     | • I n c o m e c e n t e r e d              | • P r o f i t   c e n t e r e d |                                                  | • M o b i l e ,   v i r t u a l |  b a n k i n g   &   a s s is t a n c e    |
Servicing & innovation • R e l a t i o n s h i p m a n a g e m e n t • W e b ,   m o b i l e  2 4   x   7   s e lf - s e r v ic e • S e r v i c e - e c o s y s t e m s
|     |     | • S l o w   p r o c e s s in g                 | • F a st ,   d ig i t a l ,  p r | e d i c t i v e p r o c e ss ing | • R e a l - t i m e ,   p e r s | o n a l ,   p re s c r i p t i v e p r ocessing |
| --- | --- | ---------------------------------------------- | -------------------------------- | -------------------------------- | ------------------------------- | ----------------------------------------------- |
|     |     | • L o w   d e g r e e o f   i n n o v a ti o n | • H ig h   d e g r e e o f       |  in n o v a t i o n              | • C o n t i n i o u s i n n o   | v a t i o n                                     |
• Seamlessautomatedprocesseswith
|     |     | • Historicaldata | • (Big) data analyticsandAI forpersonalization |     | high speed, high precisionmachines  |     |
| --- | --- | ---------------- | ---------------------------------------------- | --- | ----------------------------------- | --- |
Technology & Automation • M a n u al  p ro c e ss e s • I m p le m e n t a t io n o f  m ac h i n e  l e arningalgorithms i n t e g r a t e d w i t h h u m a n   c o g n it i o n
|     |     | • De c is io n m a k in g  o n personal relationships | • H ig h e rs e lf - s e rv | ic e p ro d u c t iv i ty | • I n t e g r a t io n  o f   bl    | o ck c h a i n  f o r s e c ure &  |
| --- | --- | ----------------------------------------------------- | --------------------------- | ------------------------- | ----------------------------------- | ---------------------------------- |
|     |     | • Limited useof techology                             | • Digital fastprocesses     |                           | transparenttransactions             |                                    |
|     |     |                                                       | • Data-drivendecisionmaking |                           | • Advanced AI & machine learningfor |                                    |
|     |     |                                                       |                             |                           | real-time decisionmaking            |                                    |

1.2. Next generation centric banking
Millennials and Gen Z, known as digital natives, are driving the shift toward digital banking
(Choudhary et al., 2020). A new generation has matured, molded by an unprecedented
technological revolution encompassing mobile phones, social media, and AI, along with
impactful events like a global economic crisis, a health pandemic, and natural disasters, both
domestically and internationally. They are Generation Next, the cohort of young adults who
have grown up with personal computers, cell phones and the internet and are now taking their
place in a world where the only constant is rapid change (Pew Research, 2007). Generation
Next consists of 4.3 billion people worldwide (MSCI, 2020; Mc Crindle, 2024).
Millennials (Gen Y) will soon make up the largest share of the labor market: It is projected
that by 2025, three out of every four workers globally is millennial (Schawbel, 2012).
Members of Gen Z—loosely, people born from 1995 to 2010—are true digital natives: from
earliest youth, they have been exposed to the internet, to social networks, and to mobile
systems. Their exposure to the Internet, social networks, and mobile systems thereby
produced a hyper-cognitive generation that is very comfortable with collecting and cross-
referencing many sources of information and with integrating virtual and offline experiences
(Kangwa et al., 2021). That context has also produced a generation which views consumption
differentily. Consumption as access rather than as possession. Consumption as an an
expression of individual identity and as a matter of ethical concern. That coupled with
technological advances is transforming the consumer landscape through all socioeconomic
classes (Choudhary et al., 2020).

Both generations are considered a tech-savvy generation and therefore are the main target
segment of digital banking services (Lipton, Shrier, & Pentland, 2016). Generations Y and Z
are predicted to have different consumption behavior, especially through digital platforms
compared to the older generation (Eastman, Iyer, & Thomas, 2013; Obal & Kunz, 2013). In
particular, there are some differences in experiencing digital services for younger customers.
|     |     |     | 1144  |     |     |     |
| --- | --- | --- | ----- | --- | --- | --- |

Introduction
Young (vs. older) consumers are more likely to rely less on heuristic processing (Yoon, 1997).
As consumers move through their life cycle, their needs and responses to marketing programs
tend to shift to be more benefit-oriented (Akturan & Tezcan, 2012; Khan, et al., 2020).
Customer experience develops younger customers’ affective commitment but not older
customers’. For younger (vs. older) customers, a stronger effect of customer experience on
affective commitment confirms that consumers with different age profiles experience brand-
related stimuli differently. The development of experiential value-laden interactions seems
most promising for young customers (Khan et al., 2020).
Through a behavioral finance lens millennials are often referred to as the “instant-gratification
generation,” with high expectations for their professional and personal lives (Bishop, 2006).
The supreme confidence and high optimism characteristic of this generation have, indeed,
informed its attitudes about professional achievement. Also, because of their technology
adoption and social and environmental awareness their financial behavior will more greatly
affect the global economy than the financial behavior of the generations that preceded them.
The abundance of products and investment choices in an online realm, coupled with
information overload, poses challenges for these by student debts and high housing costs
economically pressured customer segments in making optimal financial decisions. Financial
literacy is essential for millennials, as they face financial decisions that can have important
consequences throughout their life (Lussardi and Oggero, 2017). The financial choices that
younger generations face are far more challenging than those faced by past generations.
Individuals today must take on greater responsibility for decisions like investing in additional
education and planning for retirement. When facing major decisions such as these, financial
literacy is critical. Financial ignorance carries significant costs. Consumers who fail to
understand the concept of interest compounding incur more transaction fees, run up bigger
debts, and engage in loans with higher interest rates (Lusardi and Tufano, 2015; Lusardi and
de Bassa Scheresberg, 2013). They also end up borrowing more and saving less money
(Stango and Zinman, 2009). Meanwhile, the potential benefits of financial literacy are
manifold. People with strong financial skills do a better job planning and saving for
retirement (Behrman et al., 2012; Lusardi and Mitchell, 2014). Financially savvy investors are
more likely to diversify risk (Van Rooj, Lusardi, and Alessie, 2011).
This makes financial literacy important for millennials (Lusardi and Oggero, 2017). In
another study on financial literacy among the millennial generation, Dewi found a positive
relation between financial attitude, financial skills and financial behavior of millennials (Dewi
et al., 2022). The availability of new technologies like mobile bandwidth, augmented reality,
artificial intelligence, user-generated, open and dynamic data, blockchain, and digital
currencies provides opportunities to better serve and financially include these generations at a
lower cost (Dubey, 2019). To the best of my knowledge, this dissertation represents the first
attempt to propose a behavioral finance framework that incorporates financial advice and
banking tailored to the next generations. Its aim is to facilitate a deeper comprehension of the
underlying factors influencing financial behavior. Such understanding is essential for
transitioning towards predictive, instantaneous, and continuously accessible inclusive finance,
promoting financial well-being.
1155

Chapter 1
Table 3
Novel Conceptual Behavioral Finance Framework
Inclusive Finance Inclusive Finance
Data Sources Behavioral Finance Lens
Strategy Applications
• Transactions
• Openbanking • Savings apps
• Credit scores • Budgettingtools
• Budgettracking apps Observed financial behavior Symptomfighting • Traditional Credit scoring
• Financial management tools • Debtmanagementprograms
• Biometrics
• Advisor meetings
• Personality assessments
Financial • Financialliteracyassessments • Financial literacy education
situation • Psychometric credit scores • Financialeducation
• Digital footprint Psychological determinants Root cause adressing • Behavioral coaching
• Mobileapps • Inclusive credit scoring
• Mobile meta-data
• Gadgetdata
• Transactions
• Openbanking • Financial planning
• Credit scores Integrated observed behavior • Holisticfinancialwellness
• Advisor meetings with psychological Holistic platforms
• Personality assesments determinants financial wellness • Employer sponsored
• Psychometriccreditscores interventions financial wellness programs
• Dynamic data
1.3 Conclusion
In conclusion, as presented in table 2, the banking industry has undergone significant
transformations over the years, driven by technological advancements and changing customer
expectations. From the traditional branch-based banking model (Banking 1.0) to the digital
era of online banking (Banking 3.0) and the current phase of personalized, customer-centric
experiences through digital channels (Banking 4.0), the industry has evolved to meet the
demands of the digital age. The emergence of Industry 4.0, with its integration of technologies
like IoT, big data analytics, AI, and robotics, has had a profound impact on the banking sector
and is a key driver of Banking 4.0. Furthermore, the upcoming concept of Banking 5.0
envisions the seamless integration of technology and human touchpoints to enhance customer
experiences and promote sustainable inclusive banking practices. Millennials and Gen Z, as
digital natives, are leading the shift towards digital banking, and their preferences and
behaviors play a crucial role in shaping next generation centric banking.Understanding their
psychological determinants will enable tailored inclusive finance and financial wellness
strategies.
In the next chapter, we will delve into the research context and explore the research questions
in this dissertation related to the impact of technological advancements, changing customer
behavior, and the rise of digital natives on the banking industry. We will also examine the
importance of financial literacy, the role of AI in risk management, and the factors influencing
positive customer experiences in the digital banking realm.
1166

Introduction
1.4 Research
1.4.1. Research context: facilitators of Banking 5.0
As previously discussed, the banking sector is currently experiencing significant changes due
to advancements in technology (table 2) and shifting customer expectations. To effectively
respond to these changes and align with the envisioned Banking 5.0 transformation (as
illustrated in table 2), there's a growing acknowledgment of the shortcomings of traditional
financial advice and risk assessment models in consumer and small business finance. These
conventional models, which rely on historical financial data, expert judgment, and linear
approaches, often are short-focussed and lack true customer centricity. Moreover, the quality
of professional financial advice has attracted considerable attention (d’Astous et al., 2022).
The question is important, considering that professional financial advice represents an
estimated market of $60 billion in the U.S. only. Existing research does not paint a very
positive portrait of advice quality. Some advice is, at worst, dishonest (Egan et al., 2019);
under-performs in terms of returns (Hackethal et al., 2012, Hoechle et al., 2018);
discriminates against women (Bhattacharya et al., 2020); or at best, acts out of good faith but
with misguided beliefs (Linnainmaa et al., 2021). To solve these issues for the future I suggest
the implementation of digital or robo-advice.
To address these issues, I propose to accelerate the adoption and integration of holistic and
inclusive robo-advisors, driven by alternative, more foundational, segmentation and credit
decision models that integrate personality traits and artificial intelligence (AI) to promote
more sustainable and longer-term customer-centric inclusive practices in banking. This
dissertation aims to provide insights that enable the development of these foundational
holistic models. It is, however, not a one-size-fits-all. In the transition towards Banking 5.0,
it's essential for financial advisors and digital banks to assess digital financial advice within
various cultural contexts. Moreover, as outlined in table 3, the development of next-
generation inclusive finance solutions, incorporating real-time behavioral and lifestyle data, is
imperative.
This dissertation explores customer-centered digital financial advice and dynamic risk
assessment solutions driven by these foundational psychological determinants within credit
markets. It investigates the human-centered requirements and introduces a novel-personality-
driven segmentation model and strategies for digital advice. Also, it suggests an innovative
personality-centered credit scoring solution to advance inclusive credit decision-making and
validates the impact of psychometric data and AI on inclusive lending practices in small
business credit markets. The overarching objective is to offer foundational insights to
financial institutions, lenders, financial advisors, regulatory bodies, technology providers,
fintech companies, consumer advocacy groups, and consumers themselves. These insights
aim to facilitate their transition towards an intelligent, human-centered, and inclusive Banking
5.0 ecosystem, ultimately driving financial inclusion and wellness.
1177

Chapter 1
1.4.1.1. Digital advice transformation
The digital transformation process towards Banking 5.0 is revolutionizing financial advice.
For financial advisors, however, these technologies are just a tool. Service eco-systems
(platforms) and mobile technologies help them to improve their advice and lower their cost of
operation.
Table 4
Overview of the Transformation of Financial Advice & Risk Management
Timeframe Banking 1.0 Banking 2.0 Banking 3.0 Banking 4.0 Banking 5.0
1760 - 1840 1870 - 1969 1979 - 2000 2000 - 2030 2030 ->
Technology Mechanization Mass Production Automation Digitization Integration
Advice type TraditionalAdvice Advice Automation Digital (Robo) Advice Inclusive Holistic Advice
Financial advice F p i e n r a s n o c n i a c l o a n d s v u i l c ta e t i i s o n p s ro w v i i t d h e f d in t a h n ro c u ia g l h a d in v - isors. E f a i m n cc a e e n r s c g s i e a t n l o p c f e o in r o t a a f n l o s c n ia b li e l n i g n e i f n b o s r r o m to k a e d t r e i a o m g n e . o s c r a a n t d iz e O b in e n f g o li i r n n m e s a b t t o r i o o d k n e e . m ra o g c e ra s t a iz n e d a f c in c a e n ss c i t a o l p fi o n r a t n a c ls ia l F h g w i o o n e l a a i l s l l n n s t , e i c c s i s , a u s i l n s m a t t a e d e i g v n t r i r a c a ic b e t s i i n l b . it g e y c f p o a r m c e to f e e r s s r e i n li n k c c r e e e l s a if , s e a in s n t g d y l y le
Financial advisors start using basic digital Digital & Robo-advisors gain popularity, Hyper-personalized recommendations
Information is paper-based. tools for analysis and communication with providing algorithm-based advice and tailored to individual circumstances and
clients. portfolio management services. preferences.
D ex e p c e is r i i o e n n s c e re o ly f t h h e e a a v d ily v i o so n r t . he expertise and R l a a e n n g d d u s o l c n a a t li i p n o e e n , t f b r o a e c n g u s i s n a i s n c g t t i o o m a n o d s r a e p o t n to d t a h t e a d s i e g c it u a r l i ty D p a e n a r d t s a o r i a n s n k a a l a iz ly s e s t d i e c s f s i s n a m a n n e d c n m i t a s a l . r c e h c i o n m e l m ea e r n n d in a g t i f o o n r s S i G n u o c s o v t r e a p r in o n a r a a b n t l c i e n e g f ( i n E E a S n n G v c i ) r e o c r b n it y m e a r e i d a n v t i a n is l t o , o S r s t o h c e ia ir l , a a d n v d ic e.
L in im ve it s e t d m a e c n c t e o s p s t t i o on m s a fo rk r e re t t in a f il o i r n m ve a s ti t o o n rs a . nd R f t o r e a c g n u u s s l a i a n c t g t io i o m n n o a s r d e a o p n ts d t a o t a th s e e d cu ig r i i t t a y l a la n n d d o s n ca lin p e e , R t E f h i e S n e g G a u c n i o l n c a e m v to e p r s l y e ti n x fr i g t a i , e m a s n e o d w f t o h h r o e k l i s e s t e t i h c v i o c fi a l n v l a e u n s t c o e ia a o l d f a d A d r I v e i i s n c s e ,
Regulations are relatively basic and focus on
preventing fraud and ensuring fair dealing
Risk Management R p i r s im k m ar a ily n a m g a e n m u e a n l. t in banks rudimentary and R st is re k a m m a li n n a e g d e . ment processes became more S d i i g g n it i i f z i a ca ti n o t n s o h f i f r t i s t k o w m a a r n d a s g a e u m to e m n a t t p io ro n c a e n ss d e s. B a i n g d d m at a a c h a i n n a e l y le ti a c r s n , i a n r g ti f ( i M cia L l ) intelligence (AI), S o e rg a a m n l i e za s t s i o in n t e a g n r d a e ti c o o n s a y c s r t o e s m s . the
B a a n n d k h s u r m el a ie n d j u h d e g a m vi e ly n o t n fo p r a r p is e k r - a b s a s s e e s d sm re e c n o t r . ds S a ca i n m l d c p u a l l e n a a t s i l o o y n f s t s i w s . , a e r n e a s b y li s n t g e m fa s s t f e o r r r d is a k ta storage A m d o v n a it n o c r e in d g r i a s n k d m re a p n o a r g t e in m g. ent for real-time L m i m d e e u a v n l k e t t i i r p i n a f l i g g e c . a i s n t o g io u n v rc , a e p s s r t e a t d o m i c e o t n i u o h n n a t , n s a c o n e f d r d i d s a e k t c a i s f i r o o n m - I g e n a x t t t e e h r r e c n o r a n a l n n s d e o c u a t r n e c a d e l s y s y i z n e s t r d e e a m a t l- a s t i a f m r n o e d m . p i l n a t t e fo rn rm al s a t n o d
R w is e k re m re o a n c it t o iv r e in r g a a th n e d r m th i a ti n g a p t r i o o a n c s t t iv ra e t . egies R o ca i n s p k h a i m s b t i o l o it r d i i e c e a s ls l r d e a la ta ti , v w e i l t y h s l i im mp it l e is d t i p c r a e n d d ic t b i a v s e e d Risk models more sophisticated, Advanced predictive analytics & blockchain F c e y i n n b v a e i n r r o c s n i e a m c l u a e r n i n t d y ta , n l r o e s n u g - s u f t i l a n a i a t n o n a r c y b ia i c li l o t r y m is . k p s li a s n u c c e h , a a s n d
AI and ML algorithms for adaptive risk
models that can quickly respond to evolving
threats and market conditions.
F
a
l
n
o
d
u r
r
i
e
s
g
h
u
in
la
g
t o
co
ry
ll a
b
b
o
o
d
r
i
a
e
t
s
ion with fintech firms
Digital advisors are driven by service ecosystems (Kucharska, 2019; Dahl et al., 2018),
changing how services are created, delivered and evaluated (Hilken et al., 2018; Peltier et al.,
2020). Digital servitization, which leverages digital technology to open up opportunities for
value creation and revenue generation (Sihi, 2018; Sklyar et al., 2019; Adapa et al., 2020),
empowers consumers to control how, when and where services are delivered (Dahl et al.,
2018a). Firms seeking to capitalize on the digitalization of service relationships must find
ways to co-create value with customers through market efficiencies and data integration
(Grönroos and Ravald, 2011; Elsharnouby and Mahrous, 2015; Huang and Rust, 2018).
Despite the potential benefits of co-created value through digital servitization, research
exploring how service ecosystems evolve in response to new technologies and relationship
platforms is limited (Dahl et al., 2019; Patrício et al., 2018).
Digital advisors increasingly become mobile. Mobile banking is transforming the customer
experience from primarily brick-and-mortar, face-to-face transactions to technology-
mediated, consumer-centered services (Laukkanen, 2016; Baabdullah et al., 2019). This is
altering the roles that digital technologies, financial institutions and customers play in the
value co-creation and service delivery process (Choudrie et al., 2018; Dwivedi et al., 2020).
Furthermore, mobile banking technologies, especially those related to capturing, storing and
analyzing customer data, are motivating banks to implement artificial intelligence (AI) in
their digital and mobile platforms (Khrais and Shidwan, 2020). The use of open data and AI
1188

Introduction
has significantly impacted the financial decision-making processes in the banking industry. AI
algorithms can analyze large volumes of data quickly and accurately, making it easier for
banks and their customers to make informed decisions. Examples of AI mobile banking
(AIMB) services range from (gen AI) chatbots, which interact with customers in auditory or
textual format (Suhaili, 2021), to more complex, problem-solving services, such as
personalized investment advice, advanced risk management (Van Thiel & Van Raaij, 2019)
and fraud detection (Alhaddad, 2018).
Also the evolution of risk management in the banking industry from Banking 1.0 to Banking
5.0 has been influenced by technological advancements, changing regulatory landscapes, and
a shift in customer expectations. Table 4 presents the development of financial advice and risk
management across the different timeframes.
In the early days of banking, risk management 1.0 was relatively rudimentary and focused on
basic credit assessments and loan underwriting. Banks relied heavily on manual processes,
historical data, and personal judgment to evaluate creditworthiness and manage risk (Brown
and Moles, 2014). The lack of sophisticated tools and technology limited the scope and
accuracy of risk analysis. With the advent of computers and data processing capabilities, risk
management 2.0 and 3.0 started to incorporate more advanced data analytics. (Crouhy at al.,
2000). Banks began using statistical models and basic algorithms to assess credit risk and
identify potential default signals on portfolio level. However, the reliance on historical data
and limited computing power still constrained risk management practices. The widespread
adoption of the internet and digital technologies brought significant changes towards risk
management 3.0. Banks could now access larger datasets and employ more sophisticated risk
models (Bahillo et al., 2016). Credit scoring models based on statistical analysis and historical
data became more prevalent, enabling banks to make more informed decisions.
The rise of big data and artificial intelligence (AI) marked a major shift in risk management
practices, named risk management 4.0. Banks started using AI algorithms and machine
learning techniques to process vast amounts of data in real-time to assess the risk on an
individual level (Shi et al., 2022). This allowed for more accurate risk assessments, fraud
detection, and real-time monitoring of customer behavior, enhancing enterprise wide risk
management capabilities. In the context of Banking 5.0, risk management is characterized by
advanced AI-driven decision-making and the integration of the eco-system and their dynamic
data sources. Psychometric data, open banking data, social media interactions, and other
alternative data are used to build comprehensive consumer profiles and assess and mitigate
creditworthiness in real-time (Aitken, 2017). Customer-centric approaches prioritize both the
individual's financial behavior and lifestyle, leading to personalized inclusive risk
management solutions.
In the banking industry's evolution from Industry 1.0 to Industry 5.0, risk management has
transformed from manual assessments to data-driven, AI-powered strategies. By incorporating
dynamic data sources and customer-centricity, banks have vastly improved risk management
practices, adapting to the ever-changing financial landscape.
The research at hand encompasses two studies. The first study delves into Generation Next's
expectations regarding digital financial advice. Meanwhile, the second study explores how AI
can empower banks to establish automated and advanced risk management practices, driving
mobile financial assistant solutions that engage with Generation Next, promote financial
inclusion, and bolster resilience against unforeseen events. Moreover, these practices open
doors to embedded finance, next-gen wealth management, and small business lending.
1199

Chapter 1
Real-time user-generated data holds immense value for banks, offering insights into customer
behavior, preferences, and needs. Examples include open banking, allowing third-party
financial service providers access to user financial information with permission, and
psychometric data, derived from personality, behavior, and cognitive assessments. Such data
empowers 5.0 banking apps to provide personalized services, identify behavioral risks, and
offer valuable financial advice.
By leveraging real-time user-generated data, banks can create more accurate risk assessments,
enhancing the power of automated and advanced risk management practices within mobile
financial assistant solutions. These data applications range from monitoring spending habits
and location data for tailored promotions to analyzing app usage and social media activity for
a comprehensive understanding of user interests and behavior.
Within this research, psychometric data plays a crucial role in creating digital advice profiles
and creditworthiness assessments for customers. Additionally, exploration of diverse dynamic
user-generated data sources leads to the development of advanced risk management practices.
Overall, this research strives to harness the potential of AI and real-time data to revolutionize
banking practices and deliver exceptional customer experiences.
1.4.2. Research questions
1.4.2.1. Credit advice
Credit advice and risk evaluation have traditionally been the realm of specialized experts.
When consumers buy a house, they often seek guidance from mortgage advisors, while small
business owners rely on intermediaries and accountants for credit advice. This is done to
address information asymmetry and ensure informed decision-making. However, the
compensation structure in the form of commission payments to advisors can create a conflict
of interest, potentially leading to biased advice favoring higher-commission products.
To address this conflict, regulators worldwide have proposed restrictions on commission
payments in various financial and healthcare markets. In response to this issue, during my
tenure as Chief Marketing Officer at ING between 2006 and 2010, we initiated digital tooling
to help our customers reduce the information gap. After leaving ING in 2009, we launched an
AI- robo-mortgage advice platform called eyeOpen in the UK and the Netherlands. The
eyeOpen business model aimed to eliminate the agency conflict by providing direct digital
advice and charging consumer advisory fees instead of relying on commissions from lenders.
Despite the digital model, we found that 70% of mortgage applicants still desired a video call
with an advisor to alleviate their uncertainty.
In the consumer market, the significance of expert advice is said to be diminished with the
emergence of social media and user-generated content. However, even a decade after selling
eyeOpen to Aegon Transamerica, we continue to observe the significant impact brokers have
in credit advice. As a non-executive director at Ikano Bank (IKEA), a position I have held
since 2014, we notice that brokers still account for 60% to 70% of credit sales to consumers
and small businesses in the larger EU countries and the UK.
We argue that the next generation, whether applying for loans for their businesses or buying
houses privately, prefers to engage digitally without relying on intermediaries. Digital advice
has the potential to support financial inclusion by providing access to underserved customer
2200

Introduction
segments at lower costs compared to traditional advisory services. A first objective of this
dissertation is to provide evidence for the development and targeting of digital financial
advice to reduce information asymmetry and empower individuals in their financial decision-
making within the context of Banking 5.0. The first hypothesis therefore is:
H1: The integration of experiential and psychometric determinants in digital financial
advice systems increases the likelihood of advice usage and significantly improves
customer satisfaction.
1.4.2.2 Credit management
Credit management plays a crucial role in the banking industry, focusing on controlling credit
policies to enhance revenues and mitigate financial risks. Effectively managing customer
credit lines is a key aspect of credit management, as it allows companies to minimize bad debt
exposure, over-reserving, and bankruptcies. Insights into customer financial strength, credit
score history, and payment patterns are vital for making informed credit decisions. Economic
conditions also significantly influence a firm's credit policy, necessitating adjustments as
economic factors change.
After the sale of eyeOpen, we undertook the development of an AI-credit decision engine
called AdviceRobo. The primary aim was to leverage the amounts of personal dynamic data
to enable inclusive credit management solutions within the framework of Banking 5.0.
Initially, the engine generated proprietary psychometric credit scores, but it has evolved into a
comprehensive decision-making tool that combines multiple sources of dynamic data for real-
time, AI-driven credit decisions and predictive servicing. We called it human-centered AI.
Human-centered AI refers to the use of artificial intelligence (AI) technology to enhance the
human experience by creating more personalized and efficient interactions between customers
and financial institutions (Schneiderman 2022). This approach allows banks to better
understand the needs and preferences of their customers, and provide them with tailored
financial services that help them achieve their financial goals. Drawing from a decade of
pioneering credit management 5.0, we argue that while new data and technologies do not alter
the role of credit management in organizations, they enhance its capabilities and provide
greater value to customers through more accurate risk predictions. This, in turn, promotes
access to finance and financial inclusion for sole traders, small businesses, and tailored
financial health support, resulting in reduced defaults and increased financial wellness. A
second objective of this dissertation therefore is to present evidence showcasing how AI will
revolutionize real-time credit management within the framework of Banking 5.0, enabling
more accurate and efficient credit management processes.
2211

Chapter 1
1.4.2.3. Open data
Driven by legislation and initiatives like the Payment Service Directive 2 (PSD2), the advent
of open data has ushered in a customer-centric approach to banking. Previously, banks relied
on historical transaction data and expert judgments, but the open data economy has widened
access to consumer and small business financial information. Governments, such as the
European Union, Australia, and the United Kingdom, have spearheaded this shift, creating
opportunities for utilizing dynamic open data.
Open data sources encompass various types, including open banking data, governmental data,
social media data, satellite data, mobile data, and psychometric data. These sources offer
valuable insights into individual behavior across digital platforms. Leveraging alternative
dynamic open data sources, such as public data, satellite imagery, registered company data,
and social media interactions, artificial intelligence (AI) can generate comprehensive
consumer profiles. The second objective of this dissertation is to provide evidence that the
utilization of psychological determinants in credit scorecards improves credit scorecards for
inclusive finance.
H2: The application of psychometric determinants in digital credit scorecards improves
access to finance.
The AI-enabled profiles empower lenders to make more informed assessments of consumer
behavior and predict the likelihood of loan repayment defaults. Incorporating open banking
payment models, mobile phone data, and social media data has been found to significantly
enhance the predictive accuracy and performance of credit scoring models compared to
traditional approaches. Banks swith their traditional credit approaches to more advanced AI-
scorecards to leverage these vast amounts of data.
The third objective of this dissertation is to provide evidence for the utilization of AI-models
in advancing credit scoring in the context of Banking 5.0. This involves counterfactually
exploring the performances of AI-trained credit scorecards against traditional credit
scorecards.
H3: The application of artificial intelligence in credit scoring systems improves risk
model accuracy and predictive power.
1.4.2.4. Conclusion: this dissertation’s practical objective
In summary, this dissertation explores the transformation of the banking industry in the
context of Banking 5.0, driven by technological advancements and evolving customer
expectations. The research focuses on three main areas: digital financial advice, AI-driven
credit management, and the utilization of open, and more specifically, psychometric data. In
the realm of digital financial advice, the study aims to develop targeted solutions that reduce
information asymmetry and empower individuals in their financial decision-making. The
research also investigates the role of artificial intelligence (AI) in revolutionizing credit
management, enhancing risk prediction, and promoting financial inclusion. Furthermore, the
dissertation explores the potential of leveraging psychometric data to advance credit scoring,
customer profiling, and financial health development. The ultimate objective is to foster
customer-centric approaches, improve access to finance and financial wellbeing, and enhance
the overall banking experience in the digital era of Banking 5.0.
2222

Introduction
1.4.3. Theoretical knowledge gaps
1.4.3.1.Theoretical knowledge gaps
In the preceding sections, we discussed the impact of technological advancements and
evolving customer expectations on the shift towards Banking 5.0. We also outlined the key
research questions and objectives related to the role of AI and dynamic data in credit advice
and credit management. However, limited research has been conducted on the specific aspects
of Banking 5.0, where banking becomes an integral part of the activities and tasks of all
organizations and individuals. The focus should be on placing the customer and their needs at
the center of transactions, rather than the bank. This research aims to explore how the
lifestyles, attitudes and financial personalities of consumers and small business entrepreneurs
in combination with AI contribute to this customer-centric transformation of credit advice and
decision-making processes.
1.4.3.2.Financial lifestyles & personalities: Psychometrics for credit decision-making
From the extant psychometric literature, evidence suggests variables and constructs that could
assist in improving the accuracy of open banking data for AI-enabled credit scoring models.
To explain, the human trait of impatience is found to be correlated with defaulting behaviours
(Meier & Sprenger, 2007). Similarly, sixty-six psychometric variables (not defined in the
study) were applied to data relating to credit applicants from micro, small and medium-sized
enterprises in Peru (N=275), to establish psychological traits linked to the propensity for loans
to be repaid, returning an Area Under the Curve (AUC) measure of 0.7 which indicates
excellent levels of discriminatory model power (Klinger et al. 2013, Goel & Ratogi 2023, see
methodology for AUC description). To test the resultant default model premised on
psychological constructs, the authors estimated a similar model with data obtained from four
African countries¾Kenya, South Africa, Ghana, and Nigeria, and tested the model on the
Peruvian data set, resulting in an AUC of 0.56-0.58 in relation to an average default period of
≥ 60 days which indicates no model discrimination effects and limits the usability of the
model. Also, the lack of clarity regarding the sixty-six variables applied to the two data sets
raises questions of internal and external validity to warrant replicating the protocol for this
study.
This problematic trend of psychometric variables within the literature providing interesting
insights but failing to define or clarify which variables were tested is reflected in Arraiz et al.,
(2017). The authors used a larger sample (N=1993) to investigate psychometric variables that
formed part of traditional CSMs and concluded that psychometric models’ predictive
capabilities for repayment or default proved worse in rejecting applicants in contrast to using
traditional models. A limitation of this study concerns the sample of banked entrepreneurs and
did not apply the models to underbanked entrepreneurs. To increase financial inclusion of this
group and facilitate access to finance, data relating to micro-entrepreneurs in Kenya was
explored from a psychometric perspective (Dlogosch et al., 2017). The psychometric
variables were based on the big five psychometric model constructs to measure the role of
conscientiousness, emotional stability, openness to experience and integrity in defaulting
behaviour of micro-entrepreneurs (Tupes & Christal, 1992). In these early studies evidence
emerged, with an AUC of 0.67, at acceptable levels of discriminatory model power for the
inclusion of psychometric predictors and resulted in additional predictive power of defaulting
tendencies of micro-entrepreneurs. Such studies have combined psychometric covariates with
traditional financial variables like business credit history, financial statements, business
assets, market conditions and a business plan, finding no benefit of including psychometric
measures in predicting the likelihood of defaulting behaviours on repayment of capital loans.
2233

Chapter 1
In contrast, more recent research found that personal behaviour and attitudes could
substantially influence financial behaviour (Liberati & Camillo, 2018). The authors extracted
six psychological constructs from responses to a questionnaire administered by an Italian
bank. The six dimensions were i) preference for advice, ii) duty/pleasure, iii)
attachment/detachment, iv) sublimation/materialism, v) idealisation/pragmatism, and vi)
humility/sovereignty scale items. The study showed that when these constructs are included in
traditional credit scoring models (CSM) used in providing banking services, cash flow, and a
solvency score, the AUC increased considerably, from 0.554 to 0.850 indicating excellent
discrimination of the model. Likewise, a CSM trained on a dataset from a pilot study with a
Mexican bank included psychometric variables and produced an AUC of 0.6 (acceptable
discrimination) indicating that the inclusion of the right psychometric attributes has the
potential to improve the accuracy of traditional CSMs prediction capabilities (Djeundje et al.,
2021).
That said, considering the flaws of the different defined or undefined psychometric variables
cited in the above literature, this dissertation proposes a new psychometric credit decisioning
model that focuses on detecting behavioral biases of applicants rather than on drawing their
psychometric profile. The model attributes and the model itself is seriously developed and
tested on real consumer and small business customers for application in a Banking 5.0
context.
1.4.3.3.Customer experience of digital credit advice
The concept of customer experience is closely related to user experience, but it takes a more
comprehensive approach by considering all aspects of the customer's interaction, rather than
solely focusing on digital interfaces. Verhoef et al. (2009) defined customer experience as a
result of interactions between the customer and a product, a company, or a part of its
organization, which provoke a reaction. This experience is unique to each customer and
involves their engagement at various levels, including rational, emotional, sensory, physical,
and spiritual (Gentile, Spiller, & Noci, 2007, p. 397). This research builds on previous studies
of customer experience and service quality. Earlier models of service quality concentrated on
the discrepancy between the expected and perceived service quality. Grönroos (1984)
proposed that managing perceived service quality requires the firm to align the expected
service and perceived service to attain customer satisfaction.
Nelson (1970) classified products into two categories: search goods and experience goods.
Search goods provide consumers with the ability to obtain product quality information before
purchase. Experience goods, such as financial advice, do not. Credence goods are a specific
type of experience goods. Wolinsky (1995) defined credence goods as a category of
experience goods in which the sellers are the experts who determine the customers' needs. His
research into competition in credence goods markets reveals that information asymmetry in
these markets leads to prices that include mark-ups over costs and that the equilibrium does
not maximize expected customers' surplus. The third implication of information asymmetry in
credence goods is fraud (Wolinsky, 1995; Emons, 1997). Since customers cannot be certain
about the quality of the sellers' services, experts have a strong incentive to cheat.
Several authors (e.g., Alba et al, 1997; Klein, 1998; Peterson et al, 1997) suggest that the
Internet enables consumers to learn from the experiences of others and to gather product
information that is often difficult to obtain in offline settings (Klein, 1998; Lynch & Ariely,
2000). It makes all attributes searchable and eliminates differences between searching and
experiencing goods. However, for credit advice, borrowers are typically unaware of the
attributes that determine advice quality, and I disagree with the authors on this point.
Although substantial research has been conducted on the drivers of customer experience and
2244

Introduction
user experience, there is still a knowledge gap in identifying the lifestyle factors that drive
responsible digital financial advice. This dissertation provides evidence of these lifestyle
factors for targeting and application of digital credit advice.
1.4.3.4. Advanced technologies for credit decision-making: AI in credit risk
In recent years, the emergence of big data and artificial intelligence technology has made
Internet finance a brand new development model in the new era. As an emerging financial
format, Internet finance plays an important role in providing people with convenient and
efficient services (Wang, 2022). At present, the research results on the combination of big data
and artificial intelligence in Internet financial risk management are also relatively rich (Bi,
2022). With the rapid development of Internet technology and the advent of the era of big
data, people's information processing and acquisition methods have undergone tremendous
changes. In this case, a large number of user records are generated (Fang, 2021). Breeden
(2020) highlighted that machine learning is now dominating many industries and is
increasingly being applied in credit scoring and credit risk management. He also indicated
that the use of machine learning techniques comes with risks so the research now should
focus on how to use machine learning models in a regulatory-compliant business context.
Research from Nyon and Matsishela (2018) insinuates that there is a lot of data collected by
various companies which can be used in the determination of credit risk worthiness of a
company or an individual through the application of machine learning techniques. Using
various machine learning techniques to do a comparative analysis, the results showed that
Lasso regression gives the best estimation for default with an Area Under the Receiver
Operating Characteristic Curve (AUROC) of 0.8048 followed by Random Forest Model with
0.7869 AUROC. The results further revealed that the commonly used logit model was better
than the Support Vector Machine with 0.7678 AUROC compared to 0.7581 AUROC of the
Support Vector Machine. In this research we investigated the power of random forests and
neural networks for the prediction of credit risk for three financial institutions and discuss the
impact of the advanced models.
1.4.3.5. Conclusion: assessing the theoretical knowledge gaps
This dissertation addresses several theoretical knowledge gaps in the context of Banking 5.0.
Firstly, the research focuses on understanding the customer experience of digital credit advice.
It takes a comprehensive approach to customer experience, considering various aspects of
customer interaction. While previous studies have examined service quality and customer
expectations, there is still a knowledge gap in identifying the lifestyle factors that drive
responsible digital financial advice. This research aims to fill that gap by providing evidence
of these lifestyle factors for smarter customer segmentation and profiling for personalized
digital credit advice.
Secondly, it explores the role of psychometric variables in credit decision-making, aiming to
enhance the accuracy of AI-enabled credit scoring models. Previous studies have shown
promising results in using psychometric variables, but there have been issues with defining
and clarifying the variables tested. This research proposes a new psychometric credit
decisioning model that focuses on detecting behavioral biases of applicants, providing a more
reliable and usable approach.
Lastly, the research explores advanced technologies, specifically AI, in credit decision-
making and risk management. With the emergence of big data and AI, there is a need to
2255

Chapter 1
develop robust machine learning models that can accurately predict credit risk. While
previous research has highlighted the importance of machine learning techniques, there is a
need to understand how to use these models in a regulatory-compliant business context. The
research investigates the power of random forests and neural networks for credit risk
prediction and discusses their impact on financial institutions.
Overall, the research contributes to the theoretical understanding of psychometric variables in
credit decision-making, the customer experience of digital credit advice, and the application
of advanced technologies, such as AI, in credit risk management within the context of
Banking 5.0.
1.5 Dissertation outline
This section outlines the dissertation's structure and progression, aiming to answer the
research questions posed earlier. Chapters 2 and 3 focus on the desired customer experience
of digital advice and smart targetting in the market, utilizing lifestyle-centered segmentation
models and cross-cultural measurements for customer experience. Chapter 4 delves into the
application of a novel psychometric credit scoring solution to measure pscyhological
determinants for inclusive credit scoring in vulnerable consumer segments. Chapter 5
examines the impact of artificial intelligence credit modeling techniques on risk assessments,
exploring advanced technologies in credit decision-making and chapter 6 applies the novel
psychometric credit scoring solution on small business segments like sole-trader and micro-
orgnaisations and trains a new AI model for inclusive SME credit scoring. Finally, Chapter 7
concludes the dissertation, addresses the research questions and provides a vision for the
transformation of banking. The progression encompasses understanding digital credit advice,
exploring AI-based credit modeling, and culminating in a psychometric model for assessing
root causes of behavioral biases in credit applicants.
Examining the research flow illustrated in Figure 6 reveals the following structure. The
research is designed to investigate the entire customer credit journey comprehensively.
Chapters 2 and 3 concentrate on the commercial aspects of lifestyle targeting and customer
experience monitoring. On the other hand, Chapters 4, 5 and 6 shift the focus towards the
credit decisioning side, exploring the application of AI credit scoring techniques and
psychometric detemrinants.
2266

Introduction
Figure 6
General Flow of this Study
Chapter 1 Introduction
Do behavioral and psychological determinants improve digital advice?
Does the application of psychometric determinants improve credit management ?
Does the application of AI improve credit management ?
Conceptualizing & exploring Conceptualizing & exploring
behavioral& psychologicaldeterminants psychologicaldeterminants& AI
for tailoring inclusive digital advice forinclusiverisk management
Chapter 2 Chapter 4
Explaining the customer experience Human centered credit decision making
of digital advice with open data
Chapter 3 Chapter 5
Targetting the robo-advice customer Artificial intelligent credit risk prediciton
Chapter 6
Access toSmall Business Credit
underInstableMarket ConditionswithOpen data
Chapter 7.
Conclusion
In chapter 2 I develop a cross-cultural model for customer experience in digital financial
advice. This chapter focuses on the analysis of customer experiences in digital-driven
financial advice systems across different cultural contexts. The objective is to develop a cross-
cultural model that validates customer experiences. Both objective and subjective system
aspects are considered, with emphasis on experiential subjective factors. Through surveys
conducted in the UK and the Netherlands, structural equation modeling techniques are applied
to identify dominant factors influencing customer experiences. The resulting digital customer
experience model (DCX model) contributes to value creation, differentiation, regulation, and
future research. This research is published in the Journal of Economics World in 2017.
Chapter 3 is about psychometric market segmentation for personalized financial advice. This
chapter delves into the development of a psychometric market segmentation model to support
personalization in financial advice. Existing segmentation models primarily rely on
demographics and economic criteria, limiting personalization. Through surveys conducted in
the UK and the Netherlands, psychometric factors such as convenience, financial illiteracy,
and rigid personality are identified. These factors facilitate a deeper understanding of
customer preferences and behaviors, enabling tailored financial advice and potential inclusion
of underserved populations. This research is presented at the scientific conference of the
2277

Chapter 1
Society for Advancements in Behavioral Economics (SABE) in Lake Tahoe in 2017 and later
that year published in the peer-reviewed Journal of Financial Transformation in 2017.
Chapter 4 is about ensuring financial inclusion for vulnerable consumers in turbulent western
markets with psychometrics. This chapter addresses the challenges faced by vulnerable
consumer groups, such as start-up entrepreneurs, sole traders, migrants, expatriates, and
young individuals without established credit histories, in accessing finance in turbulent
Western markets. The Ukraine war, high inflation, and rising interest rates have created an
environment where people struggle to afford basic necessities like food and energy, leading to
a widespread sense of vulnerability. To tackle this issue, the study explores the potential of
using individuals' financial personality for credit scoring in these uncertain circumstances.
The research focuses on a sample of low-income individuals in the US and the Netherlands,
employing psychometric scoring models (PSMs) to analyze their financial behaviors. The
findings indicate that late payments can be attributed to various factors, including financial
capability, materialistic tendencies, impulsive buying behavior, social desirability, and
attitudes towards debt. These PSMs demonstrate that psychometrics offer a viable solution for
supporting financial inclusion among vulnerable customer segments in unstable market
conditions. This research is published in the peer-reviewed European Journal of Finance in
2023.
Chapter 5 is about artificial intelligence-based credit risk scoring for digital lending: This
chapter investigates the application of artificial intelligence in credit risk scoring for digital
lending. Traditional credit risk assessment methods face challenges in an increasingly digital
lending landscape. Supervised learning techniques, specifically neural nets and random
forests, are employed to develop individual risk assessments using mortgage and credit card
customer data from European lenders in the UK and the Netherlands. The research compares
the performance of artificial intelligence models with traditional logistic models, highlighting
the potential for scalable automated credit risk solutions.This research is presented at the
Scientific conference of the Western Economic Association International (WEAI) in San
Francisco in 2019 and later that year published in both the peer-reviewed Journal Risk
Management in Financial Institutions and the Journal of Accounting and Finance in 2019.
Chapter 6: Psychometric Credit Scoring for Financial Inclusion in Unstable Market
Conditions: This chapter explores the use of individuals' financial personality for credit
scoring, particularly in unstable market conditions. The research investigates low-income
individuals in the US and the Netherlands and develops psychometric credit scoring models
(PSMs) that consider factors such as financial capability, materialistic tendencies, and
attitudes towards debt. The findings demonstrate the potential of PSMs to support financial
inclusion for vulnerable customer segments under unstable market conditions.
Conclusion: This thesis examines various aspects of transforming financial services, including
psychometric market segmentation for personalization, cross-cultural models for customer
experience, artificial intelligence-based credit risk scoring, and psychometric credit scoring
for financial inclusion. By addressing these research areas, the thesis aims to enhance the
understanding and implementation of innovative approaches that promote personalized
financial services, improved customer experiences, and financial inclusion for all. This
research is published in the peer-reviewed Journal of Risk Management in Financial
Institutions in 2023.
In the concluding chapter 7 the three research questions of this dissertation are answered, its
contributions to theory and practice are stated and suggestions for future research are
2288

Introduction
provided. Research question 1 will be answered directly through the results of testing
behavioral and psychological determinants on customer experience and digital advice
applications (chapter 2 and 3). Research question 2 can be answered by the research
performed on the application of psychometric determinants in a novel personality credit
scoring solution and the application of it on small businesses (chapter 4 and 6). Research
question 3 can be answered by the counterfactual testing of AI scorecards against traditional
scorecards for credit scoring (chapter 5).
2299

Chapter 1
References
Adapa, S., Fazal-e-Hasan, S. M., Makam, S. B., Azeem, M. M., & Mortimer, G. (2020).
Examining the antecedents and consequences of perceived shopping value through smart
retail technology. Journal of Retailing and Consumer Services, 52, 101901.
Aitken, M. (2017). "The FinTech Ecosystem Report: Measuring the Effects of Technology on
the Entire Financial Services Industry." Business Insider Intelligence.
Akturan, U., & Tezcan, N. (2012). Mobile banking adoption of the youth market: Perceptions
and intentions. Marketing Intelligence & Planning, 30(4), 444-459.
Alba, J. W., Lynch, J. G., Weitz, B. A., Janiszewski, C., Lutz, R. J., Sawyer, A. G., & Wood, S.
(1997). "Interactive Home Shopping: Consumer, Retailer, and Manufacturer Incentives to
Participate in Electronic Marketplaces." Journal of Marketing, 61(3), 38-53.
Alhaddad, M. M. (2018). Artificial intelligence in banking industry: A review on fraud
detection, credit management, and document processing. Research Berg Review of Science
and Technology, 2(3), 25-46.
Arraiz, I., Bruhn, M., & Stucchi, R. (2017). "Psychometrics as a Tool to Improve Screening
and Access to Credit." In Credit and Collateral (pp. 91-104). Palgrave Macmillan, Cham.
Awrey, D., & Macey, J. (2023). The promise & perils of open finance. Yale J. on Reg., 40, 1.
Bahillo, A., Amato, F., Lopez, J., & Corchado, J. M. (2016). "Intelligent Credit Risk
Assessment Using CBR and Ontologies in Banking Services." Expert Systems with
Applications, 59, 293-301.
Baabdullah, A. M., Alalwan, N. F., Rana, N. P., Tamilmani, K., & Dwivedi, Y. K. (2019).
"Consumer Adoption of Mobile Banking in Saudi Arabia: An Examination of the Moderating
Role of Social, Trust, and Legal Risks." International Journal of Information Management,
49, 442-456.
Behrman, J. R., Mitchell, O. S., Soo, C. K., & Bravo, D. (2012). How financial literacy
affects household wealth accumulation. American Economic Review, 102(3), 300-304.
Bhattacharya, U., Kumar, A., Visaria, S., & Zhao, J. (2023). Do Women Receive Worse
Financial Advice? An Audit Study in Hong Kong, China. An Audit Study in Hong Kong,
China (June 1, 2023). Asian Development Bank Economics Working Paper Series, (684).
Bi, W., & Liang, Y. (2022). Risk Assessment of Operator’s Big Data Internet of Things Credit
Financial Management Based on Machine Learning. Mobile Information Systems, 2022.
Bishop, J. (2019). Supporting Millennials in Adult and Community Education Settings:
Reflective Interviews With Caregivers in the Form of Parents and Guardians. In Care and
Culturally Responsive Pedagogy in Online Settings (pp. 299-330). IGI Global.
3300

Introduction
Breeden, L. (2020). "From Financial Services to Fintech: Building on Our Successes and
Learning from Our Mistakes." Washington and Lee Law Review, 77(1), 3-10.
Brown, L. D., & Moles, P. (2014). "Bank Management and Control: Strategy, Capital and
Risk Management." John Wiley & Sons.
Bryceson, D., Pratt, G., & Millington, S. (2022). Augmented reality in Industry 4.0: A review.
International Journal of Advanced Manufacturing Technology, 108(5-6), 1591-1604.
Choudhary, A., Raina, V., & Kumar, A. (2020). Millennials and Gen Z: Key drivers of digital
banking adoption. International Journal of Bank Marketing, 38(6), 1369-1384.
Choudrie, J., Vyas, A., & Holmes, E. (2018). "Bank Customers’ Adoption of Mobile Banking:
A Literature Review." International Journal of Bank Marketing, 36(7), 1183-1209.
Crouhy, M., Galai, D., & Mark, R. (2000). "Risk Management." McGraw-Hill.
Dahl, D. W., Fuchs, C., & Schreier, M. (2019). "Customer Empowerment in New Product
Development." Journal of Product Innovation Management, 36(3), 275-285.
Dahl, D. W., Fuchs, C., & Schreier, M. (2018a). "The Emotional Path to Action: Empathy
Moderates the Association of Distress with Prosocial Behavior." Journal of Experimental
Social Psychology, 79, 116-124.
Dahl, D. W., Fuchs, C., & Schreier, M. (2018b). "Customers as New Product Developers:
Empathy Leads to Greater Success in Creating Breakthrough Products." Journal of Marketing
Research, 55(3), 363-375.
Dahl, D. W., Fuchs, C., & Schreier, M. (2018c). "Why and How to Innovate: A Guidebook for
Managers." Journal of Product Innovation Management, 35(6), 934-936.
Dahl, D. W., Fuchs, C., & Schreier, M. (2018d). "Caring for the Future Self: How Future
Perspective and Empathy Moderate the Link between Unconsciously Primed Goals and
Subsequent Saving." Journal of Consumer Research, 45(2), 382-396.
Dhama, J. (2022). The future of financial advice.
https://openresearch.ocadu.ca/id/eprint/3569/
Dewi, V. I. (2022). How do demographic and socioeconomic factors affect financial literacy
and its variables?. Cogent Business & Management, 9(1), 2077640.
Djeundje, V., Sun, Q., Oni, A. O., Zhao, X., & Hu, Y. (2021). "The Application of Machine
Learning Techniques in Predicting Credit Risk: A Comparative Analysis." Financial
Innovation, 7(1), 1-16.
Dlogosch, T. J., Klinger, B., & Frese, M. (2017). Personality-based selection of
entrepreneurial borrowers to reduce credit risk: two studies on prediction models in lowand
high-stakes settings in developing countries. Journal of Organisational Behaviour, 39, 612-
628.
3311

Chapter 1
Dubey, A. (2019). New technologies and opportunities in digital banking for millennials and
Gen Z. International Journal of Bank Marketing, 37(5), 1092-1106.
Dwivedi, Y. K., Rana, N. P., Jeyaraj, A., Clement, M., & Williams, M. D. (2020). "Artificial
Intelligence (AI): Multidisciplinary Perspectives on Emerging Challenges, Opportunities, and
Agenda for Research, Practice and Policy." International Journal of Information
Management, 51, 101994.
Eastman, J. K., Iyer, R., & Thomas, G. M. (2013). The impact of generational cohorts on
status consumption: A comparative test of Gen X and Gen Y. Journal of Business Research,
66(8), 8-14.
Egan, M., Matvos, G., & Seru, A. (2019). The market for financial adviser
misconduct. Journal of Political Economy, 127(1), 233-295.
Elsharnouby, M. H., & Mahrous, A. A. (2015). "Digital Servitization: A Revolution to
Service." International Journal of Computer Applications, 111(5).
Emons, W. (1997). Credence goods and fraudulent experts. The RAND Journal of Economics,
107-119.
Edmans, A., & Kacperczyk, M. (2022). Sustainable finance. Review of Finance, 26(6), 1309-
1313.
Fang, H. (2021). "Digitalization and Credit Access: Evidence from Micro Lending in China."
American Economic Review, 111(6), 1771-1824.
Far, S. B., Rad, A. I., & Asaar, M. R. (2023). Blockchain and its derived technologies shape
the future generation of digital businesses: a focus on decentralized finance and the
Metaverse. Data Science and Management, 6(3), 183-197
Gentile, C., Spiller, N., & Noci, G. (2007). "How to Sustain the Customer Experience: An
Overview of Experience Components that Co-create Value with the Customer." European
Management Journal, 25(5), 395-410.
Goel, V., & Ratogi, A. (2023). "Leveraging Psychometric and Open Banking Data to Improve
Credit Scoring Models in Micro, Small and Medium-Sized Enterprises (MSMEs) in
Developing Economies." In Innovations in Open and Big Data (pp. 33-55). Springer,
Singapore.
Gorodesky, R. S., da Rocha, M. F. M., de Souza, V. N., & Cruz, S. C. A. (2019). Human-
machine interfaces in Industry 4.0: A systematic review. International Journal of Production
Research, 57(6), 1604-1623.
Grönroos, C. (1984). "A Service Quality Model and its Marketing Implications." European
Journal of Marketing, 18(4), 36-44.
Grönroos, C., & Ravald, A. (2011). Service as business logic: implications for value creation
and marketing. Journal of Service Management, 22(1), 5-22.
3322

Introduction
Gui, X., & Van der Burg, P. J. (2019). "Credit Scoring Models and Implementation: A
Framework and Case Study." European Journal of Operational Research, 272(1), 220-235.
Gui, X., & van der Burg, P. J. (2020). "Machine Learning Models and their Applications in
Credit Risk Management." European Journal of Operational Research, 285(1), 232-242.
Hackethal, A., Haliassos, M., & Jappelli, T. (2012). Financial advisors: A case of
babysitters?. Journal of Banking & Finance, 36(2), 509-524.
Hermann, M., Pentek, T., & Otto, B. (2016). Design principles for Industrie 4.0 scenarios: A
literature review. 2016 49th Hawaii International Conference on System Sciences, 3928-3937.
Hilken, T., Jung, M., Grönroos, C., & Ravald, A. (2018). "Co-creating Customer Value in
Mobile Banking Services: The Role of Customer Participation and the Self-Concept." Journal
of Service Theory and Practice, 28(2), 170-199.
Hoechle, D., Ruenzi, S., Schaub, N., & Schmid, M. (2018). Financial advice and bank
profits. The Review of Financial Studies, 31(11), 4447-4492.
Huang, M. H., & Rust, R. T. (2018). "Artificial Intelligence in Service." Journal of Service
Research, 21(2), 155-172.
International Monetary Fund. (2023).
https://www.imf.org/en/Publications/fandd/issues/Series/Back-to-
Basics/Banks#:~:text=Although%20banks%20do%20many%20things,whom%20the%20bank
%20lends%20money).
Jamal, A., Noor, R. M., Harun, A. N., & Islam, R. U. (2021). Cyber-physical systems in
Industry 4.0: A systematic literature review. Journal of Manufacturing Systems, 59, 291-313.
Kagermann, H., Wahlster, W., & Helbig, J. (2015). Recommendations for implementing the
strategic initiative Industrie 4.0. acatech - National Academy of Science and Engineering.
Kangwa, D., Mwale, J. T., & Shaikh, J. M. (2021). The social production of financial
inclusion of generation Z in digital banking ecosystems. Australasian Accounting, Business
and Finance Journal, 15(3), 95-118.
Khan, I., Fatma, M., Shamim, A., Joshi, Y., & Rahman, Z. (2020). Gender, loyalty card
membership, age, and critical incident recovery: Do they moderate experience-loyalty
relationship?. International Journal of Hospitality Management, 89, 102408.
Khan, I., Hollebeek, L. D., Fatma, M., Islam, J. U., & Riivits-Arkonsuo, I. (2020). Customer
experience and commitment in retailing: Does customer age matter?. Journal of Retailing and
Consumer Services, 57, 102219.
Khrais, S., & Shidwan, S. (2020). "Artificial Intelligence and Big Data Analytics for
Enhanced Cybersecurity in Mobile Banking Services." In Cyber Security and Global
Information Assurance (pp. 203-225). IGI Global.
3333

Chapter 1
Klein, L. R. (1998). "Evaluating the Potential of Interactive Media Through a New Lens:
Search Versus Experience Goods.
Klinger, B., Khwaja, A., & LaMonte, J. (2013). Improving credit risk analysis with
psychometrics in Peru. Inter-American Development Bank. Technical Note No. IDB-TN-587.
Koc, A. (2021). Nanotechnology in Industry 4.0: A review. Journal of Manufacturing
Systems, 58, 249-265.
Kore Fusion (2021), “Embedded finance: this decade’s largest creator of value”, A Kore
Fusion Report, New York, available at: https://korefusion.com/embedded-finance-this-
decades-largest-creator-of-valu/.
Kucharska, W. (2019), “Online Brand communities’ contribution to digital business models:
social drivers and mediators”, Journal of Research in Interactive Marketing, Vol. 13 No. 4,
pp. 437-463.
Kuchler, T., & Stroebel, J. (2021). Social finance. Annual Review of Financial
Economics, 13(1), 37-55.
Laukkanen, T. (2016). Consumer adoption versus rejection decisions in seemingly similar
service innovations: The case of the Internet and mobile banking. Journal of Business
Research, 69(7), 2432-2439.
Lewis et al. (2021). The value of behaviourally informed advice study. BE Works Research
Institute.
https://russellinvestments.com/Publications/US/Document/Value_of_an_Advisor_Study.pdf
Liberati, C., & Camillo, F. (2018). Personal values and credit scoring: new insights in the
financial prediction. Journal of the Operational Research Society, 69(12), 1994-2005.
Linnainmaa, J. T., Melzer, B. T., & Previtero, A. (2021). The misguided beliefs of financial
advisors. The Journal of Finance, 76(2), 587-621.
Lipton, A. J., Shrier, D. A., & Pentland, A. S. (2016). Digital banking manifesto. The Journal
of Applied Corporate Finance, 28(1), 16-24.
Lusardi, A., & de Bassa Scheresberg, C. (2013). Financial literacy and high-cost borrowing
in the United States (No. w18969). National Bureau of Economic Research.
Lusardi, A., & Mitchell, O. S. (2014). The economic importance of financial literacy: Theory
and evidence. American Economic Journal: Journal of Economic Literature, 52(1), 5-44.
Lusardi, A., & Oggero, N. (2017). Financial literacy and planning: Implications for retirement
wellbeing. Numeracy, 10(1), 1-20.
Lusardi, A., & Oggero, N. (2017). Millennials and financial literacy: A global
perspective. Global Financial Literacy Excellence Center, 5, 17.
3344

Introduction
Lusardi, A., & Tufano, P. (2015). Debt literacy, financial experiences, and
overindebtedness. Journal of Pension Economics & Finance, 14(4), 332-368.
Lynch, J., & Ariely, D. (2000). Electronic shopping for wine: how search costs for
information on price, quality, and store comparison affect consumer price sensitivity,
satisfaction with merchandise, and retention. Marketing Science, 19(1).
Maddikunta, P. K., Das, A. K., Wang, S., Alazab, M., & Wang, H. (2021). Internet of Things
(IoT)-based smart systems: A survey. Journal of Ambient Intelligence and Humanized
Computing, 12(4), 3897-3933.
McCrindle research (2024). GenZ and Gen Alpha Inforgraphic Update.
https://mccrindle.com.au/article/topic/generation-z/gen-z-and-gen-alpha-infographic-update/
Mehdiabadi, A. R., Siadat, A., & Mousavi, S. F. (2020). Industry 4.0-based smart factories: A
taxonomy and trends of smart manufacturing systems. Computers & Industrial Engineering,
139, 105695.
Mehdiabadi, A. R., Siadat, A., & Mousavi, S. F. (2022). Future of banking in Industry 4.0 era.
Procedia Computer Science, 202, 655-664.
Meier, S., & Sprenger, C. (2007). Impatience and credit behavior: evidence from a field
experiment.
Motienko, A. (2020). Industry 4.0: Definition, principles, business impact, challenges, and
opportunities. Journal of Industrial Engineering and Management, 13(3), 509-536.
Motienko, A. (2021). Industry 5.0: A human-centric perspective of the new industrial
revolution. Technological Forecasting and Social Change, 170, 120848.
MSCI (2020). Millennials: Demographic change and the impact of a generation.
https://www.msci.com/documents/1296102/23766493/ThematicIndexInsight-Millenials-cbr-
en.pdf
Mystakidis, S. (2022). Metaverse. Encyclopedia, 2(1), 486-497.
Nelson, P. (1970). Information and consumer behavior. Journal of Political Economy, 78(2),
311-329.
Nethravathi, R., Dinesh, B., & Parida, A. (2020). Industry 4.0: A survey on technologies,
applications, challenges and opportunities. Journal of Cleaner Production, 261, 121067.
Nicoletti, B. (2021). Banking 5.0: Building a customer-centric digital ecosystem. The Journal
of Bank Cost & Management Accounting, 35(2), 20-35.
Noreen, S., Usman, M., & Shah, S. J. H. (2023). Internet-of-things based smart manufacturing
in Industry 4.0: A comprehensive survey. Computers in Industry, 135, 103710.
Nyon, E. E., & Matshisela, N. (2018). Credit scoring using machine learning
algorithims. Zimbabwe Journal of Science and Technology, 13(1), 26-34.
3355

Chapter 1
Obal, M., & Kunz, M. (2013). Generation Z: Marketing to digital natives. Journal of
Behavioral Studies in Business, 6(1), 1-9.
Ozili, P. K. (2023). Assessing global interest in decentralized finance, embedded finance, open
finance, ocean finance and sustainable finance. Asian Journal of Economics and
Banking, 7(2), 197-216.
Patrício, L., de Pinho, N. F., Teixeira, J. G., & Fisk, R. P. (2018). Service design for value
networks: enabling value cocreation interactions in healthcare. Service Science, 10(1), 76-97.
Parmar, S., Samalia, H., Vashisht, A., & Patel, R. (2022). Robotics in Industry 4.0: A
comprehensive review. Robotics and Computer-Integrated Manufacturing, 73, 101891.
Pew Research. (2007). Generation Next: A portrait of the next generation. Retrieved from
https://www.pewresearch.org/wp-content/uploads/sites/3/reports/725.pdf
Peltier, J. W., Dahl, A. J., & Swan, E. L. (2020). Digital information flows across a B2C/C2C
continuum and technological innovations in service ecosystems: A service-dominant logic
perspective. Journal of Business Research, 121, 724-734.
Peterson, R. A., Balasubramanian, S., & Bronnenberg, B. J. (1997). Exploring the
implications of the Internet for consumer marketing. Journal of the Academy of Marketing
science, 25, 329-346.
Rožanec, J. M., Novalija, I., Zajec, P., Kenda, K., Tavakoli Ghinani, H., Suh, S., ... &
Soldatos, J. (2023). Human-centric artificial intelligence architecture for industry 5.0
applications. International Journal of Production Research, 61(20), 6847-6872.
Sarma, M., & Pais, J. (2011). Financial inclusion and development. Journal of International
Development, 23(5), 613-628.
Schawbel, D. (2012). Why Gen Y will rule the corporate world. TIME, 179(23), 1-3.
Shahabi, A., Mirbaha, F., Javanmardi, M., & Alizadeh, M. (2020). Next-generation banking
with artificial intelligence. International Journal of Advanced Computer Science and
Applications, 11(1), 421-429.
Shneiderman, B. (2022). Human-centered AI. Oxford University Press.
Shi, S., Tse, R., Luo, W., D’Addona, S., & Pau, G. (2022). Machine learning-driven credit
risk: a systemic review. Neural Computing and Applications, 34(17), 14327-14339.
Sihi, D. (2018). Home sweet virtual home: The use of virtual and augmented reality
technologies in high involvement purchase decisions. Journal of Research in Interactive
Marketing, 12(4), 398-417.
Soo, S. L., Ching, K. Y., & Lim, W. S. (2021). 3D printing in Industry 4.0: A review. Robotics
and Computer-Integrated Manufacturing, 68, 101986.
3366

Introduction
Sklyar, A., Kowalkowski, C., Tronvoll, B., & Sörhammar, D. (2019). Organizing for digital
servitization: A service ecosystem perspective. Journal of Business Research, 104, 450-460.
Stango, V., & Zinman, J. (2009). Exponential growth bias and household finance. the Journal
of Finance, 64(6), 2807-2849.
Suhaili, S. M., Salim, N., & Jambli, M. N. (2021). Service chatbots: A systematic
review. Expert Systems with Applications, 184, 115461.
Sung, S. Y., Kwon, O., Kim, D., & Yoon, J. (2021). Big data analytics in Industry 4.0: A
survey. Journal of Industrial Information Integration, 23, 100248.
Tay, L. Y., Tai, H. T., & Tan, G. S. (2022). Digital financial inclusion: A gateway to
sustainable development. Heliyon, 8(6).
Tupes, E. C., & Christal, R. E. (1992). Recurrent personality factors based on trait
ratings. Journal of Personality, 60(2), 225-251.
Verhoef, P. C., Lemon, K. N., Parasuraman, A., Roggeveen, A., Tsiros, M., & Schlesinger, L.
A. (2009). Customer experience creation: Determinants, dynamics and management
strategies. Journal of Retailing, 85(1), 31-41.
Van Rooij, M. C., Lusardi, A., & Alessie, R. J. (2011). Financial literacy and retirement
planning in the Netherlands. Journal of Economic Psychology, 32(4), 593-608.
Van Thiel, D., & Van Raaij, W. F. F. (2019). Artificial intelligence credit risk prediction: An
empirical study of analytical artificial intelligence tools for credit risk prediction in a digital
era. Journal of Risk Management in Financial Institutions, 12(3), 268-286.
Vinoth, S., Vemula, H. L., Haralayya, B., Mamgain, P., Hasan, M. F., & Naved, M. (2022).
Application of cloud computing in banking and e-commerce and related security
threats. Materials Today: Proceedings, 51, 2172-2175.
Wang, N., & Wang, K. (2022). Internet financial risk management in the context of big data
and artificial intelligence. Mathematical Problems in Engineering, 2022.
Wolinsky, A. (1995). Competition in markets for credence goods. Journal of Institutional and
Theoretical Economics (JITE)/Zeitschrift für die gesamte Staatswissenschaft, 117-131.
Yoon, C. (1997). Age differences in consumers' processing strategies: An investigation of
moderating influences. Journal of Consumer Research, 24(3), 329-342.
Xu, X., Lu, Y., Vogel-Heuser, B., & Wang, L. (2021). Industry 4.0 and Industry 5.0—
Inception, conception and perception. Journal of Manufacturing Systems, 61, 530-535.
Yu, Z., Khan, S. A. R., & Umar, M. (2022). Circular economy practices and industry 4.0
technologies: A strategic move of automobile industry. Business Strategy and the
Environment, 31(3), 796-809.
3377

Chapter 1
Zetzsche, D. A., Arner, D. W., & Buckley, R. P. (2020). Decentralized finance. Journal of
Financial Regulation, 6(2), 172-203.
3388

Introduction
In the next chapter, we focus on customer experiences within digital advice services, which
have become central to the way people interact with financial institutions today.
Understanding how customers perceive and engage with AI-driven digital advice is crucial for
ensuring widespread acceptance and effectiveness. This chapter serves as a springboard for
exploring how customer insights can be translated into personalized digital advisory solutions,
paving the way for closing the global advisory gap.
3399

Chapter 1
40

Chapter 2
Explaining the Customer Experience of
Digital Financial Advice
Published as:
Van Thiel, D., & Van Raaij, F. (2017).
Explaining customer experience of digital financial advice.
Economics, 5(1), 69-84.
Presented at:
van Thiel, D., & van Raaij, F. (2014, July 21 – 24)
The development of a psychometric segmentation model for digital financial advice [Paper
presentation]. The annual conference of The Society for the Advancement of Behavioral Economics,
Lake Tahoe, Nevada, United States

Chapter 2
advice platforms that provide advice by complex computer algorithms (Bradbury, 2014).
ABSTRACT Robo advisors can be fully aligned with customers’ interest in conjunction with numerous
behavioural decision-making issues that are faced by individuals (Shanmuganathan, 2020).
Examples are investment brokers, such as Betterment, Wealthfront, and Nutmeg that optimize
The objective of this research is to examine the customer experience of digital-driven personal investment portfolios. Lend Up, Kreditech and my exited company eyeOpen match
financial advice systems. This study aims to establish a cross-cultural model for validating borrowers on their profiles with loans, and platform lenders such as Zopa or Funding Circle
inclusive customer experiences in digital financial advice. In pursuit of this goal, both connect savers to borrowers. Furthermore, established traditional advice firms have
objective and subjective aspects of the system have been taken into consideration. It has been introduced robo-advisors. Vanguard and Schwab introduced a free robo-service in addition to
determined that experiential subjective aspects of the system hold the utmost significance. their offline advice, and they are growing faster than the internet-only robo-advisors. Fidelity
Surveys were conducted in both the United Kingdom and The Netherlands. Structured offers robo-advice to customers making use of the Betterment platform. Intermediaries like
equation modeling (SEM) was utilized through exploratory and confirmatory factor analyses. Learnvest, Money super market and eye Open also introduced robo-related services.
Through the factor analysis process, five prominent factors were identified that elucidate However, further growth of robo-advice services is expected. Research agency AT Kearny
customer experience. Building upon the factor scores, multiple regression analysis was predicts robo-advisors will run $2.2 trillion in assets in 2020 because of the fast growing
undertaken to formulate the digital customer experience model (DCX model). To the best of adoption rate of this service model among young generations.
our knowledge, this represents the inaugural cross-cultural model for assessing the customer
experience of digital financial advice. In a time marked by competition among financial The market of digital financial services
institutions and FinTech companies for customer engagement, the DCX model stands as the Financial decision-making and thus traditional financial advice is being transformed by
pioneering digital advice framework poised to fundamentally enhance value creation, digitalization (Malhotra, Rashmi & D.K. Malhotra, 2006). Financial advice is defined as
differentiation, regulation, and future research endeavors. third-party services that help consumers reach financial decisions (Collins, 2010). As
consumers are getting more and more self-directed, financial capability building is becoming
Keywords: Digital financial advice, robo-advice, behavioral finance, customer experience increasingly digital. Collin’s (2010) review of financial advice models defines a model for
modelling financial capability building. The model contains three financial advice pillars describing the
advisory service models in financial retail.
2.1 Introducton
Pillar 1 contains all information models, like printed product information, tools, websites,
The financial advisor is dead comparison and recommendation sites, and workshops. The impact of digitalization on these
Whether planning for retirement or borrowing for an investment property, the increasing information models is evident. The growth of price comparison websites like Money
complexity of financial decision-making stresses the need for personal financial advice supermarket, Compare the Market, and Money Savings Expert are only a few examples of the
(Kofman, 2024). Unfortunately, the high cost of personal advice and a lack of confidence in digital impact on information models.
engaging with financial advisors keeps it out of reach for many (Robb et al., 2012). This lack
of confidence can be attributed to low levels of financial literacy and a general distrust of Pillar 2 contains all advice models; Collins distinguishes (a) technical experts such as
financial (advice) services (Egan et al. 2019). The trend in the financial technology (FinTech) mortgage or financial planning advisors, (b) transactional agents who perform the same
community therefore points to the digitalization of financial advice. Because of the scale that advising activities as technical experts, although they are tied to a brand, (c) counselors who
automation makes possible, these services have the potential to provide higher quality and work with people on their personal financial issues that often are as a result of their financial
more transparent financial advice to more people at lower cost than human financial advisors illiteracy, and (d) financial coaches who focus on designing and realizing financial goals with
(Baker, 2015). People globally will soon be dealing with a robot for their financial affairs their customers.
(Dunbar, 2015). Indeed, the University of Oxford University places financial advisors on their
list of the “Top five jobs that robots are already taking” (Frey & Osborne, 2015). Frey and The growth of robo-advisors for investment firms such as Wealthfront, Betterment,
Osborne’s (2015) research indicates that financial analysts and advisors are being replaced by FutureAdvisor, Learnvest, Nutmeg, and lending such as eyeOpen, Zopa, and Funding Circle
robo-advisors, driven by predictive systems, big data, and computing power. This research show the impact of digitalization on this advice pillar. Interestingly, the robo-investment
explores what features a digital advice system needs to keep customers satisfied so it can advisors currently perform more like mechanism models, which have the objective of making
provide financial advice to large numbers of people worldwide who currently lack access to it. consumer’s financial decisions easier by automating intelligence. Future development of these
models will be towards providing tailored personal behavioral and product advice and
The market of robo-advice services (L’Hostis & Ensor, 2015).
Nowadays, banking sector clientele expects intelligent and practical financial services
regardless of location and time with progressively decreasing fees (Rhanoui, 2022). Novel Pillar 3 contains mechanism models: (a) default (prediction) models, (b) automatic deposit
practice designs of digital devices, broadcasting and the increasing willingness to use online models, and (c) product constraints models. Companies such as Creditkarma, Zestfinance,
channels to search and financial businesses are crucial operational changes driving this Ondeck, AdviceRobo, and actually all investment robo-advisors show that digitalization also
progress (Gomber et al., 2017). Therefore, across many geographies, an increasing number of impacts this mechanism advice pillar.
financial service providers are operating or considering the use of robo-advisors; online
4421 42

Explaining the Customer Experience of Digital Financial Advice
advice platforms that provide advice by complex computer algorithms (Bradbury, 2014).
Robo advisors can be fully aligned with customers’ interest in conjunction with numerous
behavioural decision-making issues that are faced by individuals (Shanmuganathan, 2020).
Examples are investment brokers, such as Betterment, Wealthfront, and Nutmeg that optimize
personal investment portfolios. Lend Up, Kreditech and my exited company eyeOpen match
borrowers on their profiles with loans, and platform lenders such as Zopa or Funding Circle
connect savers to borrowers. Furthermore, established traditional advice firms have
introduced robo-advisors. Vanguard and Schwab introduced a free robo-service in addition to
their offline advice, and they are growing faster than the internet-only robo-advisors. Fidelity
offers robo-advice to customers making use of the Betterment platform. Intermediaries like
Learnvest, Money super market and eye Open also introduced robo-related services.
However, further growth of robo-advice services is expected. Research agency AT Kearny
predicts robo-advisors will run $2.2 trillion in assets in 2020 because of the fast growing
adoption rate of this service model among young generations.
The market of digital financial services
Financial decision-making and thus traditional financial advice is being transformed by
digitalization (Malhotra, Rashmi & D.K. Malhotra, 2006). Financial advice is defined as
third-party services that help consumers reach financial decisions (Collins, 2010). As
consumers are getting more and more self-directed, financial capability building is becoming
increasingly digital. Collin’s (2010) review of financial advice models defines a model for
financial capability building. The model contains three financial advice pillars describing the
advisory service models in financial retail.
Pillar 1 contains all information models, like printed product information, tools, websites,
comparison and recommendation sites, and workshops. The impact of digitalization on these
information models is evident. The growth of price comparison websites like Money
supermarket, Compare the Market, and Money Savings Expert are only a few examples of the
digital impact on information models.
Pillar 2 contains all advice models; Collins distinguishes (a) technical experts such as
mortgage or financial planning advisors, (b) transactional agents who perform the same
advising activities as technical experts, although they are tied to a brand, (c) counselors who
work with people on their personal financial issues that often are as a result of their financial
illiteracy, and (d) financial coaches who focus on designing and realizing financial goals with
their customers.
The growth of robo-advisors for investment firms such as Wealthfront, Betterment,
FutureAdvisor, Learnvest, Nutmeg, and lending such as eyeOpen, Zopa, and Funding Circle
show the impact of digitalization on this advice pillar. Interestingly, the robo-investment
advisors currently perform more like mechanism models, which have the objective of making
consumer’s financial decisions easier by automating intelligence. Future development of these
models will be towards providing tailored personal behavioral and product advice and
services (L’Hostis & Ensor, 2015).
Pillar 3 contains mechanism models: (a) default (prediction) models, (b) automatic deposit
models, and (c) product constraints models. Companies such as Creditkarma, Zestfinance,
Ondeck, AdviceRobo, and actually all investment robo-advisors show that digitalization also
impacts this mechanism advice pillar.
4423

Chapter 2
Robo-advisors are service models bringing easy-to-use, low-cost advice services. Therefore,
they have the potential of reducing financial stress and improving financial security for mass
consumers in both and developing countries. To be able to reach this potential, it is important
to build superior customer experience to traditional bank digital environments for many
people. Customer experience is the internal and subjective response customers have to any
direct or indirect contact with a company (Verhoef et al., 2009). Because customer experience
is important for the future adoption of robo-advisors and no research has been done on this
topic so far, the scope of this paper is on explaining the customer experience of digital advice
models as described in Pillar 2. Driven by the complexity of financial advice, (individual
products vs. portfolios) digital advice in both lending and investment shows high thresholds.
Because authors have lengthy experience in consumer lending, this research focusses on
customer experiences of robo-advisors in the lending market. To understand and improve the
customer experience, it is necessary to conduct empirical evaluations that consider the entire
process of how the customer chooses and buys a mortgage. Therefore, the DCX-model is the
first to describe how objective aspects in the advice system are subjectively perceived by the
customer and how these perceptions result in specific customer experience evaluation. Such a
user-centric model will provide a deeper understanding of what parameters drive customer
experience of digital financial advice systems, and what impact these parameters have on the
actual customer experience. It also allows for a better understanding of how certain aspects of
the digital financial advice systems result in a better customer experience, which helps further
user-centric research and the development of robo-advisors.
2.2 From service quality to customer experience
Service Quality
Nelson (1970) classified products into search and experience goods. Search goods offer
consumers the ability to obtain product quality information prior to purchase. Experience
goods, like financial advice, do not. Credence goods are a specific category of experience
goods. Wolinsky, (1995) defined credence goods as a specific category of experience goods.
He defines credence goods as experience goods whose sellers are also the experts who
determine the customers’ needs. Insights from his research into competition of credence
goods markets are that the information asymmetry in credence goods markets, leads to prices
that embody mark-ups over costs and that the equilibrium does not maximize expected
customers’ surplus. The third consequence of information asymmetry in credence goods is
fraud (Wolinsky, 1995; Emons, 1997). Since customers can never be certain about the quality
of sellers’ services, experts have strong incentives to cheat. Financial advice is an example of
a good driven by information asymmetry. However, several authors (e.g. Alba, Lynch, Weitz,
Janiszewski, Lutz, Sawyer, & Wood, 1997; Klein, 1998; Peterson, Balasubramanian, &
Bronnenberg, 1997) suggest that because the Internet enables consumers to learn from the
experiences of others and to gather product information that is often difficult to obtain in
offline settings (Klein, 1998; Lynch & Ariely, 2000), it makes all attributes searchable and
erases differences between the searching and the experience of goods.
Friends and family members, price comparison and recommendation systems provide value to
financial customers by low cost, broad offering, and support in making financial decisions.
Stigler (1961) introduced the concept of returns to information search. According to Stigler’s
analysis, consumers stop searching for information at the point when the marginal cost of
additional searching (time, effort, and other resources) equals the marginal benefit. Less-
experienced and less-educated consumers will have to work hard to find and assimilate
4443

Explaining the Customer Experience of Digital Financial Advice
information. Therefore, this relatively higher marginal cost of searching for information may
result in less searching, overall. Nonetheless, all consumers, regardless of their experience and
expertise, will cease searching for information when the marginal cost equals the marginal
benefit, and hiring a financial advisor may lower the marginal cost of searching for
information relative to searching on one’s own. Regarding financial products, consumers find
it difficult to evaluate complex financial products offered, such as investments, life insurance,
and mortgages, as their assessment requires domain knowledge and long-term vision.
Therefore, financial advice is able to play an essential role in the retailing of financial
products (Inderst & Ottaviani, 2012).
A financial advisor may lower the marginal cost of searching for information by acquiring
expertise on a relatively complex topic and then working with multiple clients, each of whom
may only need the information once in a lifetime. The scarcity of scholarly research on the
service quality of (digital) financial advice, calls for the development of a model to explain
the customer experience of digital financial advice models based on adjacent research to
service quality, user experience, and customer experience.
Earlier service quality models focus primarily on the gap between expected and perceived
service quality. Grönroos (1984) already suggested that managing perceived service quality
implies that that the firm has to match the expected service and perceived service to each
other to achieve consumer’s satisfaction. Furthermore, he identified three components of
service quality, namely: technical quality of what customers actually receive as a result of
their interaction with the service firm; functional quality of how they actually get the
outcome; and image as hedonic factors like tradition, ideology, word-of-mouth, or pricing.
Later models (Parasumaran, Zeithaml & Berry, 1985, 1991, 1994; Cronin & Taylor, 1992;
Broderick & Vichirapronpuk, 2002; Santos, 2003) build on this and reveal that the service
quality outcome and measurement is dependent on type of service setting, situation, time and
need factors. Furthermore, a customer’s expectations toward particular services constantly
change due to factors such as time, an increase in the number of encounters with a particular
service and a competitive environment (Seth & Deshmukh, 2005).
From service quality to user experience
With the development of human-computer services, service quality models evolved into
human-computer interaction models on user and customer experience. User experience relates
to their subjective evaluation of the interaction with a system (Knijnenburg, Willemsen,
Ganter, Soncu, Newell, 2012). Knijnenberg et al.’s research to the user experience of
recommender systems shows a historical trend in user experience on recommender system
research. A significant part of the earlier research concerns creating and evaluating more
effective prediction algorithms (Koren, 2010, Koren, Bell & Volinksy, 2009, McNee, Riedl &
Konstan, 2006, Herlocker, Konstan & Tervee, 2004, Cosley, Lam, Albert, Konstan & Riedl,
2003). According to Knijnenberg et al. (2012) the premise of this algorithm research is: better
algorithms lead to perceivably better recommendations. These improved recommendations, in
turn, lead to better user experience in terms of choice, satisfaction, and perceived system
effectiveness. For digital financial advice this could imply that the advice quality would be
the most important attribute of the customer experience.
H1: The quality of the recommendation or, in the scope of this paper, advice quality is an
important factor in explaining the customer experience of digital advice systems.
Furthermore, Knijnenberg et al. (2012) suggested other factors that influence the user
experience of recommender systems (Pu, Chen & Hu, 2012; Konstan & Riedl, 2012; Ozok,
4445

Chapter 2
Fan & Norcio, 2010; Murray & Haubl. 2009; McNee et al., 2006, Cosley et al. 2003). System
aspects other than accuracy, situational, personal and privacy concerns can influence system
satisfaction (Knijnenberg et al., 2011; Knijnenberg & Willemsen, 2009, 2010; Komiak &
Benbasat, 2006; Teltzrow &and Kobsam 2004). Knijnenberg et al. (2012) integrated these and
other aspects into a user-centric framework for the evaluation of recommender systems. In
their framework the evaluation of the system is, just as in service quality models, driven by a
user’s perception of the system in terms of outcome-related, system-related, and process-
related aspects. Furthermore, it is influenced by the objective effect of the system in terms of
views, purchases and usage. In the scope of this paper, actual quality of the financial advice
should be a less important attribute of customer experience than attributes describing ‘the
making of’ the advice.
H2: Both the system-related aspect as well as the process-related aspect of digital financial
advice have more impact on customer experience than outcome-related aspects such as the
quality of the advice.
From user experience to customer experience
Customer experience is strongly related to user experience, but it is holistic, rather than
simply focusing on digital interactions. Verhoef et al. (2009) defined customer experience as
originating from a set of interactions between a customer and a product, a company, or part of
its organization, which provoke a reaction. This experience is strictly personal and implies a
customer’s involvement at different levels “(rational, emotional, sensorial, physical, and
spiritual)” (Gentile, Spiller, & Noci, 2007, p. 397). Another and related definition is that
“customer experience is the internal and subjective response customers have to any direct or
indirect contact with a company. Direct contact generally occurs in the course of purchase,
use, and service and is usually initiated by the customer. Indirect contact most often involves
unplanned encounters with representatives of a company’s products, service or brands and
takes the form of word-of-mouth recommendations or criticisms, advertising, news reports,
reviews and so forth.” (Meyer & Schwager, 2007, p. 118). Adding to the above, Verhoef et al.
(2009) argued that the customer experience construct is holistic in nature and involves a
customer’s cognitive, affective, emotional, social, and physical responses to the retailer. This
experience is created, not only by those elements that the retailer can control (e.g., service
interface, retail atmosphere, assortment, and price), but also by elements that are out of the
retailer’s control (e.g., influence of others, purpose of shopping). Additionally, Verhoef et al.
(2009) stated that the customer experience encompasses the total experience, including the
search, purchase, consumption, and after-sale phases of the experience. Therefore, it may
involve multiple retail channels. As digital financial advice models will be both digital-only
robo-advice systems and hybrid systems that combine both on- and offline interactions, the
holistic view on the total customer experience of information search, purchase and after-sales
are important to understand.
H3: Holistic hedonic experiential aspects of the customer experience in digital financial
advice models are more important than functional aspects.
2.3 Method
Purpose of this research
The goal of this research is to provide a cross-cultural set of structurally related factors and
their attributes that explain customer experience of digital financial advice systems. Customer
experience and financial advice are ill-defined concepts and lack well developed assessment
4465

Explaining the Customer Experience of Digital Financial Advice
methods and metrics. The influence of self-directedness on financial decision-making
increases because the Internet enables consumers to learn from the experiences of others and
to gather product information. Therefore, it is the objective to develop a cross-cultural model
for validating the customer experience of digital financial advice. In doing so, the study
considers the impact of both objective and subjective system aspects.
The aim is to develop an easily applicable model for validating the customer experience of
digital and hybrid financial advice systems. The research particularly identifies the
explanatory factors and underlying attributes of customer experiences with digital financial
advice. However, it also identifies the parameters of these factors and their functional or
experiential nature. Having insight into the explanatory factors and their attributes and
parameters, this paper aims to validate the stated hypotheses.
Developing and piloting the DCX model
As banks, financial advisors and robo-advisors are more focused on customer centricity, this
research objective is to support improved understanding of the customer experience of user-
centric digital financial advice models. The model is an objective validation instrument of
customer experiences of digital financial advice brands. Therefore, it can help digital financial
advisors to build deeper customer centric advice relations and better support differentiation
with their advice systems. The model can also inspire researchers toward future digital advice
systems.
To develop and test the model, an online survey among 2,332 consumers has been conducted
across two experiments. All respondents had experience with buying a house and choosing a
mortgage. The respondents were randomly selected from the GfK-consumer panels in the
United Kingdom and The Netherlands and divided into two groups (1) 2013 The Netherlands
(N=1407) and (2) 2013 The United Kingdom (N=935). To design the model, these two front-
running financial advice markets were selected. The UK and The Netherlands are being
understood as front-runners because of their advanced financial advice eco-systems (financial
advisors, governmental regulation and FinTech industry). The first online survey experiment
was held in Q1 2013 in The Netherlands (N=1407). The second experiment was held in Q4
2013 in the United Kingdom (N=935). The experiments were used to develop the DCX
model. On the data structured equation modelling (SEM) was applied in the form of
confirmative analysis on the conceptual model and exploratory factor analysis to design the
best fitting model. The chi-square of the confirmative analysis did not show a good fit. With
exploratory factor analysis the DCX model has been designed. From factor analysis, five
dominant factors were obtained explaining customer experience. Driven by the size of the
sample, the maximum-likelihood method was applied to test the goodness-of-fit of the model.
The root-mean-square explains over half of the variance as shown (R-square NL = .52; R-
square UK = .81). On the factor scores, multiple regression analysis was applied to develop
the digital customer experience model (DCX model).
Developing a conceptual model and survey design
Based on earlier research, field studies, and several brainstorms, the conceptual model has
been developed (Figure 1). The variables that could potentially have impact on the customer
experiences of digital financial advice systems are given in Table1.
Figure 1
Conceptual Digital Customer Experience Model
4467

Chapter 2
Table 1
List of psychometric features
4487

Explaining the Customer Experience of Digital Financial Advice
A good working relationship with the advisor
Accessibility - a location easy to get
Accuracy
Advice geared towards getting the lowest monthly cost (price)
Advice that matches personal situation
Advice with only your best interest at heart
Being able to arrange the mortgage through the advisor
Being able to get advice about mortgage related financial products
Being able to get advice about other financial products
Being given the feeling of being equal
Empathy
Expertise
Freedom to decide on the place and time of appointment
Friendliness
Helpfulness
Honesty
Honouring agreements
Independent advice
Methods to get in contact
Preference for a mortgage provider being taken into account in the advice
Preference for a type of mortgage being taken into account in the advice
Proactivity (providing useful information beyond what is asked)
Reliability
Reputation of the mortgage provider(s)
Room for negotiation
Size of the company giving advice
Speed of response
Taken into account the degree of risk willing to take
Time taken to give advice
Transparency of way of work
Usefulness of the advice
Using understandable language
Well-know (good reputation, references)
# different types of compared mortgages
# different type of mortgages to choose from
# mortgage providers to choose from
Based on the variable list, a survey was composed in close co-operation with research agency
GfK, which was applied in this research. The survey design consisted of five lettered sections
with 38 questions on satisfaction with attributes of the advisor and the advice service quality.
The A-section contained screening questions to build a social-demographic profile of the
respondents. The B-section contained questions for performance evaluation of recent
mortgage closings. Respondents were asked to rank their experience with the performance on
the variable list of their most important financial advisor. Scoring took place on a 7-point
4489

Chapter 2
Likert-scale. The C-section contained questions for benefit evaluation on the variable list of
mortgage closings. Again, scoring took place on a 7-point Likert-scale. The D- and E-section
contained questions about the respondents’ motivational profiles. The survey was validated on
a pilot-group of 100 respondents prior to the larger online field study.
2.4 Experiments and Results
2.4.1. Experiments
2.4.1.1. DCX experiment 1, The Netherlands
The first online field experiment was held in 2013 in The Netherlands among 1,407
respondents. The respondents varied in experienced advice users (N=815; consumers who
received mortgage advice in the last year) and inexperienced users (N=592; consumers who
had received mortgage advice longer than one year ago) to compensate for recency effects in
defining the parameters of the model. The questionnaires were factor-analyzed to develop the
DCX model. First confirmative and later exploratory factor analysis was applied to come to
the six-factor model. The model fits well with an R-square of 0.52. Factor scores were
developed through multiple regression analysis (Table 2). Based on these outcomes the
conceptual model was rejected and the DCXnl model developed (Figure 2).
Figure 2
Digital Customer Experience Model The Netherlands
Factors Regression weights
F1 Advising qualities .77
F2 Pre-selection .31
F3 Co-creation .26
F4 Advicsing style .46
F5 Accessibility .14
F6 Price .21
Constant 5.86
R2 = .52
5409

Explaining the Customer Experience of Digital Financial Advice
Table 2

Factor table The Netherlands.

|              | F1 F2         | F3          | F4    | F5            | F6    |
| ------------ | ------------- | ----------- | ----- | ------------- | ----- |
|              | Advising      | Advising    |       |               |       |
|              | Pre-selection | Co-creation |       | Accessibility | Price |
|              |  Qualities    |             | Style |               |       |
| Reliability  | 0,69          |             |       |               |       |
| Accuracy     | 0,69          |             |       |               |       |
| Expertise    | 0,75          |             |       |               |       |
| Helpfulness  | 0,66          |             | 0,45  |               |       |
| Friendliness | 0,66          |             |       |               |       |
| Honesty      | 0,71          |             |       |               |       |
"click"
0,63
| Understandable  | 0,63      |     |     |     |     |
| --------------- | --------- | --- | --- | --- | --- |
| Independent     | 0,62 0,42 |     |     |     |     |
| "best interest" | 0,60 0,41 |     |     |     |     |
"personal match"
0,69
| Empathy               | 0,71 |     |      |     |      |
| --------------------- | ---- | --- | ---- | --- | ---- |
| Proacitveness         | 0,69 |     |      |     |      |
| Monthly costs         | 0,67 |     |      |     |      |
| Usefulness            | 0,71 |     |      |     |      |
| Time taken            | 0,52 |     | 0,59 |     |      |
| Transparency          | 0,58 |     |      |     |      |
| Advisors rate         |      |     |      |     | 0,75 |
| Contact possibilities | 0,44 |     | 0,64 |     |      |
Response rate
|                 | 0,46 |     | 0,71 |      |     |
| --------------- | ---- | --- | ---- | ---- | --- |
| Availability    |      |     |      | 0,77 |     |
| Freedom to meet |      |     | 0,55 |      |     |
| Reknown         | 0,50 |     |      | 0,43 |     |
Company size
|                          | 0,43      |     |      | 0,48 |     |
| ------------------------ | --------- | --- | ---- | ---- | --- |
| Closing process          | 0,62      |     | 0,47 |      |     |
| Honouring agreements     | 0,61      |     | 0,55 |      |     |
| Broad offering brands    | 0,78      |     |      |      |     |
| Reputation offering      | 0,72      |     |      |      |     |
| Broad offering types     | 0,73      |     |      |      |     |
| Broadness compared       | 0,67      |     |      |      |     |
| Clarity conditions       | 0,49 0,56 |     |      |      |     |
| Possibility other advice | 0,71      |     |      |      |     |
Possibility non-mortgage
0,72
| Own brand wishes used |      | 0,69 |     |     |     |
| --------------------- | ---- | ---- | --- | --- | --- |
| Own type wishes used  |      | 0,68 |     |     |     |
| Equality in relation  | 0,51 | 0,64 |     |     |     |
Negotiation space
0,53
| Risk appetite | 0,40 | 0,70 |     |     |     |
| ------------- | ---- | ---- | --- | --- | --- |

|     | 5501  |     |     |     |     |
| --- | ----- | --- | --- | --- | --- |

Chapter 2
2.4.1.2. DCX-experiment 2, The United Kingdom
The second online field experiment was held after the first, and also took place in 2013, in the
United Kingdom and included 935 respondents. Because the differentiation between
experienced and inexperienced users in the first experiment created no significant insights, the
respondents in this experiment were only experienced advice users (consumers who had
received mortgage advice in the last year). To be able to compare the results over the
experiments, exactly the same questionnaires and analysis were applied. The questionnaires in
this second experiment were exploratory and factor-analyzed to develop the five-factor
model. The model fits even better than in The Netherlands with an R-square of 0.81. Factor
scores were developed through a multiple regression analysis (Table 3). Based on the results
the DCXuk model was developed (Figure 3).
Figure 3
Digital Customer Experience Model United Kingdom
Factors Regression weights
F1 Advising qualities .71
F2 Process influence .32
F3 Advising width .23
F4 Price image .28
F5 Accessibility .09
Constant 5.93
R2 = .81
5521

Explaining the Customer Experience of Digital Financial Advice

Table 3

Factor table United Kingdom

|     |     |     | F1 F2           | F3 F4          | F5  |
| --- | --- | --- | --------------- | -------------- | --- |
|     |     |     | Advising Proces | Advising Price |     |
Accessibility
|     | Attributes |     |  Qualities  influence |  width  image |     |
| --- | ---------- | --- | --------------------- | ------------- | --- |
Reliability
0,79
| Accuracy                                     |     |     | 0,77 |      |     |
| -------------------------------------------- | --- | --- | ---- | ---- | --- |
| Expertise                                    |     |     | 0,76 |      |     |
| Helpfulness                                  |     |     | 0,77 |      |     |
| Friendliness                                 |     |     | 0,66 |      |     |
| Honesty                                      |     |     | 0,75 |      |     |
| A good working relationship with the advisor |     |     | 0,75 |      |     |
| Using language you can understand            |     |     | 0,57 |      |     |
| Independent advice                           |     |     | 0,57 | 0,51 |     |
Advice with only your best interests at heart
0,71
| Advice that matches your personal situation (income, education, family situation) |     |     | 0,66 |     |     |
| --------------------------------------------------------------------------------- | --- | --- | ---- | --- | --- |
Empathy (can empathize with my situation)
0,63
| Proactivity (providing useful advice and information beyond what you asked about) |     |     | 0,69 |      |     |
| --------------------------------------------------------------------------------- | --- | --- | ---- | ---- | --- |
| Advice geared towards getting the lowest monthyl cost (price)                     |     |     | 0,62 |      |     |
| Usefulness of the advice                                                          |     |     | 0,73 |      |     |
| Time to taken to get to giving you advice                                         |     |     | 0,75 |      |     |
| Transparency of the way the advisor works                                         |     |     | 0,74 |      |     |
| The cost of getting advice                                                        |     |     | 0,45 | 0,56 |     |
| How you can get in contact (telephone, mail, face to face)                        |     |     | 0,65 |      |     |
| Speed of response                                                                 |     |     | 0,74 |      |     |
Accessibility: a location that is easy for you to get to
0,57
| Freedom to decide on the place and time of appointment yourself |     |     | 0,53 |      |      |
| --------------------------------------------------------------- | --- | --- | ---- | ---- | ---- |
| Well-known (good reputation, references)                        |     |     | 0,46 | 0,44 |      |
| Size of the company that's giving advice                        |     |     |      |      | 0,67 |
| Being able to arrange the mortgage through the advisor          |     |     | 0,69 |      |      |
| Honouring agreements                                            |     |     | 0,75 |      |      |
The number of mortgage providers from which you can choose 0,68
The reputation of the mortgage provider(s) from which you can choose 0,41 0,51
The number of different types of mortgage from which you can choose 0,51 0,45 0,48
The number of different types of mortgages that are compared
|     |     |     |     | 0,51 0,45 0,44 |     |
| --- | --- | --- | --- | -------------- | --- |
The clarity of the explanation of the mortgage terms and conditions 0,45 0,51 0,47
Being able to get advice about financial products that go with a mortgage 0,74
| Being able to get advice about other financial products |     |     |     | 0,79 |     |
| ------------------------------------------------------- | --- | --- | --- | ---- | --- |
My preference for a mortgage provider being taken into account in the advice 0,73
My preference for a type of mortgage being taken into account in the advice 0,43 0,73
| Being given the feeling that I am unequal |     |     | 0,46 | 0,68 |     |
| ----------------------------------------- | --- | --- | ---- | ---- | --- |
| Room for negotiation                      |     |     |      | 0,68 |     |
Taking into account the degree of risk I am willing to take 0,73

2.4.2. Results

DCXnl factor model
The experiments in The United Kingdom and The Netherlands point toward the same factors
for customer experience in digital financial advice. This supports the explanation of the cross-
cultural expectations of digital financial advice.
Based on the results of the first experiment in The Netherlands the DCXnl model has been
developed (Figure 3). The DCXnl model differed from the conceptual model initially
developed. The factors of the DCX model explain more than half of the variance (CX: R-
square = .52). If DCXnl is the dependent variable and advising quality (F ), advising width
1
(F ), co-creation (F ), advising style (F ), accessibility (F5), and price (F6) are the
| 2   | 3   | 4   |     |     |     |
| --- | --- | --- | --- | --- | --- |
independent variables that define DCXnl as:

|     |     | 5523  |     |     |     |
| --- | --- | ----- | --- | --- | --- |

Chapter 2
DCXnl = 0.56F + 0.22F + 0.19F + 0.33F + 0.1F + 0.15F + 5.86
1 2 3 4 5 6
DCXuk factor model
The second experiment (UK) shows a DCX model that also differs from the initial conceptual
model. The factors of the DCX model explain over 80% of the variance (CX:R-square =.81).
If DCXuk is the dependent variable and advising quality (F ), process influence (F ), advising
1 2
width (F ), price (F ) and accessibility (F ) are the independent variables defining DCXuk as:
3 4 5
DCXuk = 0.58F + 0.26F + 0.19F + 0.23F + 0.07F + 5.93
1 2 3 4 5
Hypotheses testing
As the regression formulas show, the DCX model shows important similarities between the
British and the Dutch market. In both markets, F (advising qualities) is a significant
1
explanatory factor of customer experience. The DCXnl shows a factor score of a = .56. The
DCXuk shows a factor score of a = 58. Both scores have a significance of p<0.01. Therefore,
the first hypothesis can be validated.
H1: Although people lack the knowledge to validate it, the quality of the recommendation, or
in the scope of this paper, advice quality is the most important factor in explaining the
customer experience of digital advice systems.
To assess the second hypothesis, the nature of the explanatory attributes for factor F1 advising
quality has been assessed. The hypothesis covers the domain of how consumers assess the
quality of a piece of advice. This is very hard to do without in-depth product knowledge.
From the factor tables can be seen that the explanatory variables of F advising quality
1
contain, as hypothesized, outcome, system, and process attributes.
Outcome-related attributes are the accuracy of the advice given (.770), honesty (.751),
friendliness (.664), match of advice with personal situation(.660), usefulness of the advice
(.733), honoring agreements (.752) (UK) usability (.711), and honesty (.708) (NL).
Process-related attributes are reliability (.789), helpfulness (.774), good working relationship
(.754), advice with the best interest at heart (.706) empathy (.628) (UK), and empathy (.711)
(NL) and care (.695) (NL).
System-related attributes are expertise (.756), time taken to come to concluding advice (.747),
transparency (.741) (UK), and expertise (.746) (NL).
In relation to F , advising quality, indeed outcome, process, and system attributes play an
1
important role in the customer experience. In both markets’ factor loadings of process and
system related attributes are indeed slightly higher than the outcome-related factor loadings.
In this respect, the UK also seems to have higher thresholds for the performance of digital
advisors on customer experience than that of the Dutch (p < 0,01). The attributes explaining
their experience of F advising quality are also more outcome-oriented and richer. All in all,
1
H2 can be validated.
5543

Explaining the Customer Experience of Digital Financial Advice
H2: Because people find it difficult to evaluate financial advice quality, both system-related
aspects and process-related aspects of digital financial advice have more impact on customer
experience than outcome-related aspects as the quality of the advice.
To validate the third hypothesis, the other factors in the DCX-model and their attributes were
assessed to discover experiential attributes. Looking at the names of the factors, one may get
the impression that higher DCX-scores can be obtained by improving functionality (process
influence (UK: .26), advising width (UK .19; NL .22) and price (UK .23; NL .15)).
Nevertheless, as presented in the factor tables, except from outcome-related attributes such as
the accuracy of the advice (.770), usability of the advice (.711), advice width (UK .19; NL
.22), size of the company (.032), and price (UK .23; NL .15), all other attributes carry
experiential value. Attributes such as honesty (UK .751; NL .133) friendliness (UK .664; NL
.115), helpfulness (UK .774; NL .088), and empathy (UK .628; NL .131) are examples that
play an important role in both markets. As expected with financial advice as a credence good,
looking at the scores of the attributes, the experiential value of digital financial advice is
important for choice satisfaction and customer engagement. Although financial institutions
primarily invest in customer experience to grow product sales, DCX of financial advice shows
many experiential attributes in both the UK and Dutch market. The third hypothesis can
therefore be validated. With the upcoming of unknown brands as robo-or digital advisors we
argue that because of the ill-differentiating outcome attributes in digital financial advice,
experiential service attributes in digital environments will have increasingly differentiating
power.
H3: Although traditional financial institutions underinvested in customer experience, we
therefore hypothesize that hedonic experiential aspects of the customer experience in digital
financial advice models are more important than functional aspects.
2.5 Discussion
The aim of this research is to create a cross-cultural framework of interconnected factors and
their characteristics that explain customer satisfaction with digital financial advice systems.
Since concepts like customer experience and financial advice are not clearly defined and lack
well-established assessment methods and metrics, this study introduces a new customer
satisfaction model specifically for digital financial advice. In developing this model, both
objective and subjective system attributes were evaluated across The United Kingdom and
The Netherlands. In both countries, objective attributes include factors such as reliability,
accuracy, and the range of advice offered, while subjective attributes encompass aspects like
helpfulness, how well personal preferences are taken into account, and the perceived honesty
of the advice. This newly developed DCX model is by our knowledge the first cross cultural
scientific model to integrate both objective and subjective factors and attributes that influence
customer satisfaction with digital financial advice systems.
Previous research on service quality (Grönroos, 1984), human-computer interaction
(Knijnenburg, 2010, 2011, 2012), and customer experience (Verhoef, 2009) has found that
customer satisfaction depends on aligning expected quality or experience with the actual
quality or experience. Many scholars emphasize the need to balance functional outcome
attributes with experiential attributes. This research supports those findings, but it also
highlights the growing importance of experiential attributes—such as helpfulness, co-creation
in considering customer preferences, and perceived honesty—in influencing customer
satisfaction with digital financial advice systems. The study also shows that process and
system-related attributes like reliability, room for co-creation and width of the advice are
5545

Chapter 2
already having a greater impact on customer experience than outcome-related attributes like
price or price image. This trend is likely to continue over the next five to ten years, reshaping
customer expectations of their banks and (digital) financial advisors.
The managerial impact for companies providing digital financial advice lies in creating
experience-driven systems that not only deliver quality advice but also involve the customer
in the process, offering a broad range of options, value for money, and easy accessibility.
Customers increasingly expect features that promote professional co-creation, responsive
support, and a wide product selection, which together contribute to a more personalized
experience beyond the basic functions of online banking and advisory systems. The DCX
model offers a valuable framework for designing and monitoring the performance of these
service systems. Additionally, it provides a basis for better differentiation between advice
brands and platforms, allowing companies to meet evolving customer expectations and stand
out in the competitive landscape.
The DCX model developed in this study could significantly aid regulators in overseeing the
provision of digital financial advice. By integrating both objective and subjective factors that
drive customer satisfaction, the model offers a comprehensive framework for assessing the
quality of digital advisory services. Regulators can use this model to establish clearer
guidelines and benchmarks for customer experience, helping to ensure that digital advice
systems meet high standards of reliability, transparency, and personalization. Furthermore, the
model's emphasis on experiential attributes like helpfulness, preference co-creation, and
perceived honesty can guide regulators in monitoring these systems for fairness and ethical
considerations, ultimately safeguarding consumer interests. As digital financial advice
continues to expand, the DCX model can support regulatory efforts to promote innovation
while maintaining a focus on customer-centricity and service quality.
As banks, financial advisors, robo-advisors, and regulators increasingly emphasize customer-
centricity, this study aimed to enhance the understanding of customer experiences within user-
focused digital financial advice models. The developed DCX model serves as a valuable tool
for evaluating the customer experience with digital financial advice brands. From a
managerial perspective, it can help digital financial advisors build stronger, more customer-
focused relationships. For regulators, it offers a framework to expand their oversight in the
digital era, ensuring that these systems meet evolving standards for quality, transparency, and
consumer protection.
2.6 Limitiations and further research
The DCX-model may inspire researchers to further explore the customer experience of digital
advice. As customer behavior becomes more self-directed, the expectations customers have
from their experience of credence goods, such as financial advice, will be impacted. The
application of the DCX model on different financial service markets such as smart budgeting,
investing, small business lending or financial planning will grow the quality of the DCX as a
comparison instrument. However, the application of the DCX model on other credence goods
markets, for example healthcare, mobile and internet communications, and automotive repair
services can further develop toward an improved DCX model.
There are some limitations to this research that should be considered when interpreting
findings. The new models are derived from research in the UK and Dutch markets. Although
5565

Explaining the Customer Experience of Digital Financial Advice
these markets are known as precursors in digital financial advice, additional geographic-
specific research has to be conducted to generalize the findings to other global markets.
The data of this research were gathered in the year when both the UK and the Dutch
governments introduced commission stops on complex financial advice. This stimulated the
growth of online low-cost financial advisors since 2013. Due to the short period between the
introduction of the commission stop and the moment of this research, the price and
accessibility benefits offered by these online financial advisors are still in its’ infancy.
Additional time-series research should be performed to monitor the changing impact of the
drivers in the DCX model and especially the price-elasticity of (digital) financial advice. In
2015, no difference was found in the factors and attributes described in this paper.
Finally, this research has been singularly performed on digital financial advice. Further
research might be conducted to focused business models such as comparison sites, robo-
advisors, and also advisors in other service industries like healthcare and utilities.
5567

Chapter 2
References
Alba, A., Lynch, J., Weitz, B., Janiszewski, C., Lutz, R., Sawyer, A., & Wood, S. (1997).
Interactive home shopping: Consumer, retailer, and manufacturer incentives to participate in
electronic marketplaces. Journal of Marketing, 61, 38-53.
Baker, T., & Dellaert, B. (2017). Regulating robo advice across the financial services
industry. Iowa L. Rev., 103, 713.
Broderick, A. J., & Vachirapornpuk, S. (2002). Service quality in internet banking: The
importance of customer role. Marketing Intelligence & Planning, 20, 327-335.
Collins, J. M. (2010). A review of financial advice models and the take-up of financial
advice. Center for Financial Security WP, 10(5).
Cosley, D., Lam, S. K., Albert, I., Konstan, J. A., & Riedl, J. (2003). Is seeing believing? How
recommender system interfaces affect users' opinions. In Proceedings of the SIGCHI
Conference on Human Factors in Computing Systems. ACM.
Cronin Jr., J. J., & Taylor, S. A. (1992). Measuring service quality: A reexamination and
extension. Journal of Marketing, 56, 55-68.
De Goede, M. (2008). The politics of preemption and the war on terror in Europe. European
Journal of International Relations, 14, 161-185.
Dunbar, I. (2016). Robo-advice – short-term fad, or the future of financial advice? Equity.
Egan, M., Matvos, G., & Seru, A. (2019). The market for financial adviser misconduct.
Journal of Political Economy, 127(1), 233–295.
Emons, W. (1997). Credence goods and fraudulent experts. The RAND Journal of Economics,
28, 107-119.
L’Hostis, A., & Ensor, B. (2015). Follow best practices to encourage mobile banking
use. Forrester.
Frey, C. B., & Osborne, M. (2015). Technology at work: The future of innovation and
employment.
Gentile, C., Spiller, N., & Noci, G. (2007). How to sustain the customer experience: An
overview of experience components that co-create value with the customer. European
Management Journal, 25, 395-410.
Gomber, P., Koch, J.A., Siering, M. (2017), Digital Finance and FinTech:
Current research and future research directions. Journal of Business
Economics, 87(5), 537-580.
Grönroos, C. (1984). A service quality model and its marketing implications. European
Journal of Marketing, 18, 36-44.
5587

Explaining the Customer Experience of Digital Financial Advice
Herlocker, J. L., Konstan, J. A., & Terveen, L. G. (2004). Evaluating collaborative filtering
recommender systems. ACM Transactions on Information Systems, 22, 5-53.
Inderst, R., & Ottaviani, M. (2012). Financial advice. Journal of Economic Literature, 50,
494-512.
Knijnenburg, B. P., & Willemsen, M. C. (2009). Understanding the effect of adaptive
preference elicitation methods on user satisfaction of a recommender system. In Proceedings
of the Third ACM Conference on Recommender Systems. ACM.
Knijnenburg, B. P., Willemsen, M. C., & Hirtbach, S. (2010). Receiving recommendations
and providing feedback: The user-experience of a recommender system. In E-Commerce and
Web Technologies (pp. 207-216). Springer Berlin Heidelberg.
Knijnenburg, B. P., Willemsen, M. C., & Kobsa, A. (2011). A pragmatic procedure to support
the user-centric evaluation of recommender systems. In Proceedings of the Fifth ACM
Conference on Recommender Systems. ACM.
Knijnenburg, B. P., Willemsen, M. C., Ganter, Z., Soncu, H., & Newell, C. (2012). Explaining
the user experience of recommender systems. User Modeling and User-Adapted Interaction,
22, 441-504.
Klein, L. R. (1998). Evaluating the potential of interactive media through a new lens: Search
versus experience goods. Journal of Business Research, 41, 195-203.
Kofman, P. (2024). Scoring the Ethics of AI Robo-Advice: Why We Need Gateways and
Ratings. Journal of Business Ethics, 1-13.
Komiak, S. Y. X., & Benbasat, I. (2006). The effects of personalization and familiarity on
trust and adoption of recommendation agents. MIS Quarterly, 30, 941-960.
Konstan, J. A., & Riedl, J. (2012). Recommender systems: From algorithms to user
experience. User Modeling and User-Adapted Interaction, 22, 101-123.
Koren, Y., Bell, R., & Volinsky, C. (2009). Matrix factorization techniques for recommender
systems. Computer, 8, 30-37.
Koren, Y. (2010). Collaborative filtering with temporal dynamics. Communications of the
ACM, 53(4), 89-97.
Lynch Jr., J. G., & Ariely, D. (2000). Wine online: Search costs affect competition on price,
quality, and distribution. Marketing Science, 19, 83-103.
Malhotra, R., & Malhotra, D. K. (2006). The impact of internet and e-commerce on the
evolving business models in the financial services industry. International Journal of
Electronic Business, 4(1), 56-82.
McNee, S. M., Riedl, J., & Konstan, J. A. (2006). Making recommendations better: An
analytic model for human-recommender interaction. In CHI'06 Extended Abstracts on Human
Factors in Computing Systems. ACM.
5589

Chapter 2
Meyer, C., & Schwager, A. (2007). Understanding customer experience. Harvard Business
Review, 85, 116-.
Murray, K. B., & Häubl, G. (2009). Personalization without interrogation: Towards more
effective interactions between consumers and feature-based recommendation agents. Journal
of Interactive Marketing, 23, 138-146.
Nelson, P. (1970). Information and consumer behavior. Journal of Political Economy, 78,
311-329.
Ozok, A. A., Fan, Q., & Norcio, A. F. (2010). Design guidelines for effective recommender
system interfaces based on a usability criteria conceptual model: Results from a college
student population. Behaviour & Information Technology, 29, 57-83.
Pu, P., Chen, L., & Hu, R. (2012). Evaluating recommender systems from the user’s
perspective: Survey of the state of the art. User Modeling and User-Adapted Interaction, 22,
317-355.
Santos, J. (2003). E-service quality: A model of virtual service quality dimensions. Managing
Service Quality: An International Journal, 13, 233-246.
Seth, N., Deshmukh, S. G., & Vrat, P. (2005). Service quality models: A review. International
Journal of Quality & Reliability Management, 22, 913-949.
Parasuraman, A., Zeithaml, V. A., & Berry, L. L. (1985). A conceptual model of service
quality and its implications for future research. Journal of Marketing, 49, 41-50.
Parasuraman, A., Berry, L. L., & Zeithaml, V. A. (1991). Refinement and reassessment of the
SERVQUAL scale. Journal of Retailing, 67, 420-.
Parasuraman, A., Zeithaml, V. A., & Berry, L. L. (1994). Reassessment of expectations as a
comparison standard in measuring service quality: Implications for further research. Journal
of Marketing, 58, 111-124.
Peterson, R. A., Balasubramanian, S., & Bronnenberg, B. J. (1997). Exploring the
implications of the Internet for consumer marketing. Journal of the Academy of Marketing
Science, 25, 329-346.
Regan, M. P. (2015, June 18). Robo-advisors to run $2 trillion by 2020. Bloomberg.
Bradbury, T. (2014). Robo-advice is coming: What it means, who will buy it—and
why. Professional Planner, 69, 40.
Rhanoui, S. (2022). Banking goes digital: the main determinants of the clients’ satisfaction
and trust toward fintech-based services. International Journal of Economics and Financial
Issues, 12(5), 10-20.
Santos, J. (2003). E-service quality: A model of virtual service quality dimensions. Managing
Service Quality: An International Journal, 13(3), 233-246.
6509

Explaining the Customer Experience of Digital Financial Advice
Shanmuganathan, M. (2020). Behavioural finance in an era of artificial intelligence:
Longitudinal case study of robo-advisors in investment decisions. Journal of Behavioral and
Experimental Finance, 27, 100297.
Stigler, G. J. (1961). The economics of information. Journal of Political Economy, 69, 213-
225.
Teltzrow, M., & Kobsa, A. (2004). Impacts of user privacy preferences on personalized
systems. In Designing Personalized User Experiences in eCommerce (pp. 315-332). Springer,
Netherlands.
Verhoef, P. C., Lemon, K. N., Parasuraman, A., Roggeveen, A., Tsiros, M., & Schlesinger, L.
A. (2009). Customer experience creation: Determinants, dynamics, and management
strategies. Journal of Retailing, 85, 31-41.
Wolinsky, A. (1995). Competition in markets for credence goods. Journal of Institutional and
Theoretical Economics, 151, 117-131.
6601

Chapter 2
With a picture of customer experience in digital financial advice, emphasizing the growing
importance of experiential attributes in this area, we now turn to psychometric segmentation
to identify the diverse needs of those who use digital advisory services. This chapter builds a
framework for targeting specific customer groups based on their financial personalities and
behaviors. By tailoring our approach, we can create more effective and personalized robo-
advisory models that resonate with the right audiences, setting the stage
for more inclusive credit assessments.
6621

Chapter 3
Targeting the robo-advice customer:
The development of a psychometric segmentation
model for financial advice robots
Published as:
van Thiel, D., & van Raaij, F. (2017).
Targeting the robo-advice customer: The development of a psychometric segmentation model for
financial advice robots.
Journal of Financial Transformation, 46, 88-104.
Presented at:
van Thiel, D., & van Raaij, F. (2014, July 21 – 24)
The development of a psychometric segmentation model for digital financial advice [Paper
presentation]. The annual conference of The Society for the Advancement of Behavioral Economics,
Lake Tahoe, Nevada, United States

Chapter 3
ABSTRACT
The aim of this study is to pioneer the development of the world's first psychometric market
segmentation model, designed to facilitate personalization, customer education, customer
activation, and customer engagement strategies within the realm of inclusive financial advice
robots. While conventional segmentation models in consumer finance typically rely on
externally observable demographics or economic indicators such as profession, age, income,
or wealth, post-hoc psychometric segmentation offers additional support for personalization
in the service delivery of digital advisors. Furthermore, it holds potential for shedding light on
how to integrate the 4.5 billion financially underserved individuals and assist inexperienced
millennials in securing their financial future. To construct the psychometric segmentation, a
survey comprising 2,232 respondents was conducted across the United Kingdom and the
Netherlands. Factor analysis was employed to delineate the key psychometric factors, namely
"convenience," "financial illiteracy," and "rigid personality." Subsequently, a Ward cluster
analysis was executed to define the psychometric segments across both markets.
Keywords: Robo-advice, Digital advice, Personalization strategies, Psychometrics
segmentation, Inclusive finance
3.1 Introduction
Financial advice is essential for many consumers, as general financial literacy remains limited
(Van Raaij, 2016). Financial advice refers to third-party services that assist consumers in
making financial decisions (Collins, 2010). This advice can typically be provided face-to-
face, by phone, or digitally. As today’s consumers face more financial decisions than ever
before, within an increasingly complex environment, financial advice has become even more
important (ASIC, 2010). Digitalization is transforming financial decision-making and
traditional financial advice (Malhotra & Rashmi, 2006). Younger generations, especially
millennials, embrace digital lifestyles (PWC, 2014), which have driven the digitization of
financial services and the adoption of financial tools that support financial decision-making.
As consumers become more self-directed, building financial capability is increasingly taking
place through digital channels (Van Thiel & Van Raaij, 2017). Therefore, this research
investigates the psychometric drivers of various customer groups to enhance the tailoring and
personalization of digital financial advice solutions, making them more impactful and
accessible to a broader audience.
Intelligent agents, such as robo-advisors and digital financial assistants, can serve as cost-
effective financial support tools (Van Thiel et al., 2008). One of the main advantages of using
a robo-advisor is the lower cost and the absence of biases in the advice, such as investment
portfolio restrictions or biases from a human advisor when offering mortgage advice
(Rusciano, 2023). Robo-advisors respond to an attempt to democratize advisory services
(reserved by traditional channels) in order to encourage the financial inclusion of subjects
considered unbanked (Rusciano, 2023).
The ultra-low costs at which these digital advisors can provide services greatly expand the
global accessibility of financial advice. This service gap has been well-documented by
researchers worldwide. According to the National Financial Capability Study (FINRA, 2012),
only 50% of Americans received any form of financial advice over a five-year period.
6643

Targeting the robo-advice customer:
The development of a psychometric segmentation model for financial advice robots
Similarly, ASIC reports that fewer than 40% of Australian adults have ever consulted a
financial planner (ASIC, 2010), and access to financial advice is even more limited in
developing countries. The World Bank highlights that 2 billion people globally lack access to
financial services (World Bank, 2015), with many also lacking the financial advice needed to
make informed financial decisions.
Currently, across many geographies, an increasing number of financial service providers are
considering the use of robo-advisors: online advice platforms that provide advice by using
complex algorithms (Bradbury, 2014). Research agency AT Kearny predicts robo-wealth
advisors will run $2.2 trillion in assets by 2020 because of the fast-growing adoption rate of
this model among younger generations (Van Thiel & Van Raaij, 2017). The Financial Times
estimates that the market for funds advized by hybrid-robo-human services will grow to $16.3
trillion by 2025. Additionally, the growth of the credit-side of the market growth is clear; the
global automated peer-2-peer lending market is expected to grow from $64 billion in 2015 to
$897 billion by 2024 (Transparency Research, 2016).
As the digital lifestyles are becoming commonplace around the world, people are producing
an increasing amount of behavioral data. Robo-advisors make use of this and apply
algorithms that match consumers or small businesses with financial products or portfolios. As
brands increasingly compete on understanding customer DNA at every touch point,
behavioral data from all kinds of sources can form the game changers in financial services.
Big behavioral data analytics is being applied to find hidden patterns and correlations to more
deeply understand customers’ behavior. These deep customer DNA insights can drive
personalized and predictive services. Personalization and predictive services are, especially in
relation to personal finance and financial planning, services that can facilitate sound financial
decision-making across populations.
The increasing number of behavioral data driven services forecast the strong growth of robo
advisors, intelligent agents and virtual assistants in the coming decades. The University of
Oxford places financial advisors on their list of the ‘Top five jobs that robots are already
taking’ (Frey & Osborne, 2015). Frey and Osborne’s (2015) research indicates that financial
analysts and advisors are being replaced by robo-advisors, driven by predictive systems, big
data and computing power. Robo-advice is swiftly growing because of the increasing self-
directedness of people; the full potential of robo-advice can only be reached by larger
adoption.
The change of customer-need structures through the increasing impact millennials have, as
well as the introduction of modern technologies such as digital and robo-advice increases the
need for more personalized segmentation models. The objective of this research is to develop
the world’s first psychometric segmentation model that uncovers and monitors the elements
that motivate consumers to make use of digital or robo-advice. Psychometric segmentation is
an approach to financial advice market segmentation based on the personality characteristics
of consumers. Banks can apply it in more personalized strategies for increasing customer
engagement and lowering the cost of acquisition and servicing. In this study on financial
advice, we focus on one of the most complex forms: mortgage advice. Also, to validate the
model, research has been conducted in Europe’s two most advanced mortgage advice
markets: the UK and The Netherlands. The segmentation model provides insight in
psychometric factors and variables that drive perceived satisfaction with financial advice
robots and can be applied in advanced marketing and risk strategies.
6645

Chapter 3
3.2 From consumer segmentation to personalization
Financial advice and customer segmentation models
Product differentiation and market segmentation are marketing strategies aimed to increase
engagement with customers. Product differentiation refers to the differentiation in the product
perception due to physical and non-physical attributes, including price to better meet human
expectations (Dickson & Ginter, 1987). In imperfect market situations, in occasions where
there is no homogeneity for all competitors in the market, market segmentation is another
commonly used strategy (Smith, 1956). Smith illustrated that market segmentation involves
viewing a heterogeneous market as several smaller homogeneous markets. Smith suggested
three criteria to be fulfilled in segmentation: (1) homogeneity (i.e. communality needs within
groups); (2) distinction (i.e. uniqueness between groups); and, (3) reaction (i.e. similarity of
response toward marketing strategy, product, offer or services within a group). Market
segmentation and product differentiation are two sides of the same coin. The link between
product differentiation and market segmentation is the product benefit (Van Raaij & Verhallen
1994). Market segmentation is also defined as a recognition of the existence of multiple
demand functions and the development of a plan to meet one or more of these functions
(Frank, Massy & Wind, 1972). These groups can be addressed by specially designed, but also
standardized, strategies (Kotler & Keith, 1980). Kotler (1980) claims that market
segmentation creates a more finely tuned product or service offering a price appropriate for
the target segment. Kotler (1980) also claims that three major segmentation forms are
commonly used: demographic, psychometric and behavioral (Andreasen, Kotler & Parker
2003). Customer segmentation by banks, however, is remains largely limited to categories of
corporate and retail customers as traditionally defined (Machauer & Morgner, 2001).
Corporate customers are distinguished by their geographic range of activities, sector and size.
In personal retail banking, externally observed demographic or economic criteria such as
profession, age, income or wealth or often the preferred dimensions for segmentation
(Mouthino & Meidan, 1984; Harrison, 1994). However, demographic and economic criteria
are rough indicators for the need structures and the reaction patterns of retail customers
(Machauer & Morgner, 2001).
These forms of traditional market segmentation are bound to a high probability that
standardized service packages are offered to customers that are not suitable. Thus, low
satisfaction and possible migration of customers is to be expected (Machauer & Morgner,
2001). As segmentation can be forward, backward and simultaneous (Van Raaij & Verhallen,
2016), modern forms of segmentation are post-hoc. Backward or reverse segmentation means
dividing customers into need clusters based on the data a company already has. Thus, a
heterogeneous population is surveyed and segments are determined based on homogeneous
response patterns from within the population (Machauer & Morgner, 2001). The research
seeks measures that cluster consumers into potentially profitable but unique groups within the
population. Some studies in this area use customer responses related to questions on product
features or usage. Product usage frequency patterns (Burnett & Chonko, 1944), for example,
identified four customer segments for packaging banking products. Accordingly, the segment
labels ‘traditional’, ‘convenience’, ‘investment’ and ‘debt’ were derived from the
characteristics of the preferred products within these segments.
Psychometric segmentation
Several other studies using post hoc segmentation approaches are oriented toward the
psychological determinants of customers in that they refer to psychometric segmentation or
benefit segmentation (Machauer & Morgner, 2001). The purpose of psychometrics is to obtain
6665

Targeting the robo-advice customer:
The development of a psychometric segmentation model for financial advice robots
a better understanding of the consumer as a person by measuring psychological dimensions,
way of living, interests and opinions (Ziff, 1971). The most widely used approach to measure
lifestyle is by using activities, interests and opinion (AIO) rating statements (Plummer, 1974).
A widely used tool for lifestyle segmentation is the VALS scheme (Rokeach, 1973), which
blends research of values, hierarchy of needs and sociology in its operation. Another
frequently used tool for lifestyle segmentation is the ‘List of Values’ (Kahle, Beatty & Homer,
1983).
In this era whereby millennials force their digital lifestyles to markets and technologies as
machine learning brings enhanced analytic possibilities, big data based segmentation
revolutionizes opportunities for personalized targeting. As f.e. segmentation for mobile
devices is typically based on demographics and reported use, smartphone measurement
software enables us to directly add observed user behavior and psychometrics (Hamka et al.,
2014). Big data insight is generated through analytics, which can be subdivided into:
descriptive analytics, analytics activities that explain the past; predictive analytics that
predict/forecast future outcomes; and, prescriptive analytics, which predict future outcomes
and suggest options for decision-making. In the last step of the ‘virtual value chain’ the data
or insight might be visually represented, the data distributed or access to the data or analytics
results provided, for example, through an API (Hartmann et al., 2014).
Hypothesis 1: Psychometric segmentation can be effectively utilized in defining market
segments within the digital or robo financial advice industry, thereby facilitating the
development of personalized robo-advice strategies.
Financial advice and financial literacy
On the demand side of robo and digital financial advice, the issue in global financial advice
markets is that financial advice is being perceived as inaccessible. The National Financial
Capability Study (FINRA, 2012) conducted a survey among US citizens (n=1488) to discover
the number who obtained some form of financial advice in the past five years: 57% did,
which 8% on debt management, 21% on tax planning, 24% on receiving a loan, 33% on
investments, and 33% on insurance. Furthermore, the survey showed that a higher income,
good education and sound financial literacy led to more financial advice being sought. Also,
the generation of millennials are approaching their peek buying years (Goldman Sachs, 2017).
According to Goldman Sachs this generation is on their way to marry, buy cars and houses for
their family life. PWC researched the financial literacy of millennials (PWC, 2015) and found
that millennials struggle with their financial lives. Only 24% have adequate financial
knowledge, 34% are very dissatisfied with their current financial situation but still only 27%
seek professional financial advice on saving and investment. They are inexperienced
financially and also embrace a digital lifestyle, thus new financial technology such as
financial advice robots can fill this knowledge gap.
Hypothesis 2: Financial illiteracy serves as a differentiating factor within the psychometric
segmentation model, contributing to the formulation of personalized robo-advice strategies.
Financial advice and motivation
FINRA-research (2012) shows that people’s level of financial literacy and education impacts
their openness for financial advice. PWC research illustrates that only 27% of millennials use
financial advice. Motivation to use digital financial advice therefore is a potential factor that
differentiates customer segments for building personalized robo-advice strategies. To be
motivated means to be moved to do something; motivation concerns energy, direction,
persistence and equifinality; all aspects of activation and intention (Deci & Ryan, 2000).
6667

Chapter 3
Therefore, a person who feels no impetus or inspiration to act is characterized as unmotivated, financial advice robot service delivery. It might furthermore provide insight on how to include
whereas someone who is energized or activated toward a goal is motivated. People do not the 4.5 billion underserved people financially and support inexperienced millennials with
only have different degrees of motivation, but also various kinds of motivations. The building financially stable lives.
orientation of motivation concerns the underlying attitudes and goals that give rise to action
(Deci & Ryan, 2000). In their Self-Determination Theory, Ryan and Deci distinguish several
types of motivation based on various reasons or goals that give rise to an action. Whereas
intrinsic motivation refers to do something because it is inherently interesting or enjoyable, 3.3 Methodology & results
extrinsic motivation refers to do something as a means to reach another goal or outcome.
3.3.1. Developing the Digital Psychometric Segmentation (DPS) Model
Hypothesis 3: Motivation constitutes a distinguishing factor within the psychometric
segmentation model, contributing to the formulation of personalized robo-advice strategies. Developing a conceptual model and survey design
Firstly, the main psychometric dimensions were determined. These psychometric dimensions
Financial advice and risk appetite. served as the conceptual basis for a questionnaire (which is explained in the following
Nelson (1970) classifies products into search and experience goods. Search goods offer section) which aimed to gain evaluations from digital mortgage advice customers of their
consumers the ability to obtain product quality information prior to purchase, whereas psychometric profile and their perceived acceptation of digital financial advice. Based on
experience goods, like financial advice, do not. Credence goods are a specific category of earlier scholarly research (Machauer & Morgner, 2001; FINRA, 2009; Deci & Ryan, 2000;
experience goods. Wolinsky (1995) defines credence goods as experience goods whose sellers Tversky & Kahneman 1975), AFM field studies (Van Raaij, 2016), and several brainstorms
are also experts who determine customers’ needs. Information asymmetry in credence goods among academic peers, the variables for psychometric segmentation have been defined. The
markets lead to prices that embody mark-ups over costs. Furthermore, the equilibrium does survey confirmed the importance of the following variables:
not maximize expected customers’ surplus. Another consequence of information asymmetry
in credence goods is fraud (Wolinsky, 1995; Emons, 1997). Since customers can never be 1. Need for relevant information
certain about the quality of the sellers’ services, experts have opportunities and incentives to 2. Time spent on finding relevant information
cheat. Therefore, regulators force financial advisors to investigate the risk profile of a 3. Span of alternatives evaluated in the decision process
customer and match their advice. Due to the 2008 economic crisis, trustworthy assessments of 4. Support being asked for in the information search
risk perception and risk tolerance of financial customers became a central element in financial 5. Level of trust in financial advisors
supervision (Roszkowsky, 2010). To differentiate between risk tolerance and risk perception, 6. Openness to new products and services
we must first define risk. According to Roszkowsky, risk is the uncertainty that exists as to 7. Rationality in the buying decision
what the eventual outcome will be. Risk arises in any decision where there is some doubt 8. Level of financial knowledge
about at least one of the possible outcomes. The risk inherent in any given situation will 9. Level of following financial market developments
depend on the range of possible outcomes and the likelihood and value of each outcome. 10. Risk appetite
Thus, in a financial context, risk tolerance is the amount of risk an individual chooses when 11. Level of maximization in the buying decision
making a financial decision. Although risk tolerance is largely a fixed personality trait and 12. Level of ‘social opinions’ applied in buying decision
stable, it is nonetheless marginally subject to situational influences (for example mood) and
may change due to life circumstances (for example aging). The psychological profiles composed of these variables should characterize the way a person
Furthermore, an evaluation of the degree of risk generally involves a perception of the is open to digital financial advice. It should provide an input to digital and robo-advice
situation, which means that there is some interpretation of the objective reality. Tversky and leadership teams on how to design digital advice strategies and personalized services per
Kahneman show that risk perception is a function of intuitive notions of risk (e.g. probability customer segment.
of loss and loss aversion) than of technical risk measures such as beta, standard deviation, or
variance (Tversky & Kahneman, 1975). Based on the variables, a survey was composed in close co-operation with research agency,
GfK. The survey design consisted of five sections with 38 questions on satisfaction with
Hypothesis 4: Risk tolerance functions as a differentiating factor within the psychometric attributes of the advisor and the advice service quality. Section A contained screening
segmentation model, influencing the development of personalized robo-advice strategies. questions to build a social-demographic profile of the respondents. Section B contained
questions for the performance evaluation of recent mortgage closings. Respondents were
Purpose of this research asked to rank their experience with the performance on the variable list of their most
As defined in the introduction, the purpose of this study is to develop the world’s first important financial advisor. To measure latent constructs such as opinions and interests,
psychometric market segmentation model that supports personalization, customer education, scoring took place on a 7-point Likert-scale. Section C contained questions for benefit
customer activation and customer engagement strategies with financial advice robots. As evaluation on the variable list of mortgage closings. Again, scoring took place on a 7-point
traditional segmentation models in consumer finance primarily focus on externally observed Likert-scale. These sections were applied in composing the DCX-model (Van Thiel & Van
demographics or economic criteria such as profession, age, income or wealth (Meidan, 1984; Raaij, 2016). Section D and Section E contained statements about respondents’
Harrison, 1994), post hoc psychometric segmentation might support further personalization in psychometrics. To measure the latent construct of financial behavior, the responses were also
6687 68

Targeting the robo-advice customer:
The development of a psychometric segmentation model for financial advice robots
financial advice robot service delivery. It might furthermore provide insight on how to include
the 4.5 billion underserved people financially and support inexperienced millennials with
building financially stable lives.
3.3 Methodology & results
3.3.1. Developing the Digital Psychometric Segmentation (DPS) Model
Developing a conceptual model and survey design
Firstly, the main psychometric dimensions were determined. These psychometric dimensions
served as the conceptual basis for a questionnaire (which is explained in the following
section) which aimed to gain evaluations from digital mortgage advice customers of their
psychometric profile and their perceived acceptation of digital financial advice. Based on
earlier scholarly research (Machauer & Morgner, 2001; FINRA, 2009; Deci & Ryan, 2000;
Tversky & Kahneman 1975), AFM field studies (Van Raaij, 2016), and several brainstorms
among academic peers, the variables for psychometric segmentation have been defined. The
survey confirmed the importance of the following variables:
1. Need for relevant information
2. Time spent on finding relevant information
3. Span of alternatives evaluated in the decision process
4. Support being asked for in the information search
5. Level of trust in financial advisors
6. Openness to new products and services
7. Rationality in the buying decision
8. Level of financial knowledge
9. Level of following financial market developments
10. Risk appetite
11. Level of maximization in the buying decision
12. Level of ‘social opinions’ applied in buying decision
The psychological profiles composed of these variables should characterize the way a person
is open to digital financial advice. It should provide an input to digital and robo-advice
leadership teams on how to design digital advice strategies and personalized services per
customer segment.
Based on the variables, a survey was composed in close co-operation with research agency,
GfK. The survey design consisted of five sections with 38 questions on satisfaction with
attributes of the advisor and the advice service quality. Section A contained screening
questions to build a social-demographic profile of the respondents. Section B contained
questions for the performance evaluation of recent mortgage closings. Respondents were
asked to rank their experience with the performance on the variable list of their most
important financial advisor. To measure latent constructs such as opinions and interests,
scoring took place on a 7-point Likert-scale. Section C contained questions for benefit
evaluation on the variable list of mortgage closings. Again, scoring took place on a 7-point
Likert-scale. These sections were applied in composing the DCX-model (Van Thiel & Van
Raaij, 2016). Section D and Section E contained statements about respondents’
psychometrics. To measure the latent construct of financial behavior, the responses were also
6689

Chapter 3
measured on a 7-pont Likert scale. For this paper on psychometric segmentation, Section E  1.  Explained variance
and the response in Section A, are used. The survey was validated on a pilot group of 100  2.  Group size >100
respondents prior to the larger online field experiment.   3.  Interpretation of homogeneity of the groups
|                         |     |     |     | 4.  If no clear interpretation, start at rule 1  |     |     |     |     |
| ----------------------- | --- | --- | --- | ------------------------------------------------ | --- | --- | --- | --- |
| Performing the survey   |     |     |     |                                                  |     |     |     |     |
To develop and test the model, an online survey of 2,332 consumers has been conducted  The dominant psychometric segments and their means are displayed in Table 2.
across two experiments. Respondents were grouped based on their recent experience with
buying a house and choosing a mortgage. The respondents were randomly selected from the  Table 2
GfK-consumer panels of the UK and The Netherlands and divided into two groups (1) 2013
The Netherlands (n=1407); and, (2) 2013 The UK (n=935). The first online survey  Psychometric segments in The United Kingdom and The Netherlands
experiment was held in Q1 2013 in The Netherlands (n=1407). In the experiment,
|     |     |     |     |     | United Kingdom |     | Netherlands |     |
| --- | --- | --- | --- | --- | -------------- | --- | ----------- | --- |
experienced financial advice users (N=815) were differentiated from inexperienced financial
|     |     |     |     |     | Convenience  | Convenience  | Trustful with  | Financially  |
| --- | --- | --- | --- | --- | ------------ | ------------ | -------------- | ------------ |
advice users (n=592). The second experiment was held in Q4 2013 in the UK (n=935).  seekers Financial illiterates Rigids seekers knowledgables Rigidits unknowledgebales
Because the differentiation between experienced and inexperienced users in the first  Mean Mean Mean Mean Mean Mean Mean
|     |     |     |     | C1 Convenience | 1,56149 -,05108 | ,09060 1,6 | -0,3 -0,4 | -0,3 |
| --- | --- | --- | --- | -------------- | --------------- | ---------- | --------- | ---- |
experiment created no significant insights, the respondents in this experiment were only  C2 Trustful with knowledge -,26301 -,90491 -,84376 -0,1 -0,9 -0,3 0,8
experienced advice users (consumers who had received mortgage advice in the last year). To  C3 Rigid -,44974 -,33342 1,03366 0,1 -0,8 1,0 -0,4
|     |     |     |     | C4 No financial knowledge | -,28716 ,83885 | -,40067 - | - - | -   |
| --- | --- | --- | --- | ------------------------- | -------------- | --------- | --- | --- |
be able to compare the results over the experiments, the same questionnaires and analyses
were applied. The experiments were used to develop and validate the Digital Psychometric  The validation approach for the discovered psychometric segments was in performing this
Segmentation model (DPS-model).   study across Europe’s two foremost mortgage advice markets: The UK and The Netherlands.
  The UK and The Netherlands are understood as front-runners because of their advanced
Psychometric Segmentation  financial advice eco-systems (financial advisors, governmental regulation and FinTech
On the survey response, principal component factor analysis with Varimax rotation was  industry).
applied with the 12 psychometric variables. The Varimax rotation with Kaiser normalization
was performed over four rotations. Both in the UK as in The Netherlands, three components  3.3.2. The DPS-model and its validation in two markets.
(convenience with eigenvalue of 1.89; financial illiteracy with eigenvalue of 1 and rigidity
with eigenvalue of 0.51) resulted from the principal component analysis. Based on the Kaiser  Digital Psychometric Segmentation in The Netherlands
criterium that eigenvalues, >1 should be selected, only convenience and financial illiteracy  The principal component analysis in the first experiment shows the factors and their variables
should be components in the psychometric model. However, based on the importance of risk  across the experienced and inexperienced customer groups through the surveys in the UK and
appetite and emotionality in decision-making according to regulators, a third component  The Netherlands that point toward similar factors for psychometric segmentation in digital
‘rigidity’ is added to the model. The rotated component matrix for the UK and The  financial advice. This supports the explanation of the cross-cultural expectations of digital
Netherlands are shown in Table 1.   financial advice. The factors are (1) need for convenience, (2) level of financial literacy and
  (3) need for rigidity. The Digital Psychometric Segmentation-model (DPS) is presented in
| Table 1  |     |     |     | Figure 1.  |     |     |     |     |
| -------- | --- | --- | --- | ---------- | --- | --- | --- | --- |
|          |     |     |     |            |     |     |     |     |
Rotated component matrices for the United Kingdom and The Netherlands
|                                                |                                  |                   |                            |     |     |     |     |     |
| ---------------------------------------------- | -------------------------------- | ----------------- | -------------------------- | --- | --- | --- | --- | --- |
|                                                | United Kingdom                   |                   | Netherlands                |     |     |     |     |     |
|                                                | Convenience Financial illiteracy | Rigid Convenience | Financial illiteracy Rigid |     |     |     |     |     |
| Information: Seek a lot - Try to limit         | ,800                             | ,830              |                            |     |     |     |     |     |
| Time: Take all I need - As quickly as possible | ,737                             | ,776              |                            |     |     |     |     |     |
| Alternatives: Many - Limited amount            | ,801                             | ,701              |                            |     |     |     |     |     |
Research: All myself - Let others do as much as possible ,646 ,642 ,420
| Trust advisors: Easily - Do not    |      | ,671 | -,464 ,394 |     |     |     |     |     |
| ---------------------------------- | ---- | ---- | ---------- | --- | --- | --- | --- | --- |
| Products: Try new - Stick to known | ,407 | ,468 | ,719       |     |     |     |     |     |
Decisions: Based on feelings - Logically and systematically
,747 ,645
| Financial knowledge: A great deal - Very little | ,832 |     | ,780 |     |     |     |     |     |
| ----------------------------------------------- | ---- | --- | ---- | --- | --- | --- | --- | --- |
Financial market developments: Fully abreast - Barely follow ,834 ,726
Risks: Fully prepared to take - Averse (maximum security) ,598 ,453 ,401 ,677
Product search: Until the best possible - As soon as found ,826 ,808
Comparitive shopping (usage rating & reviews websites): Use a lot - Do not use ,628 ,357

With the components discovered, a Ward’s minimum variance clustering model was applied
to classify financial advice consumers. Based on the three components, four dominant

segments were obtained explaining psychometric differences in suitability for digital financial

advice. The following decision rules were applied to assign to each cluster:

|     | 7609  |     |     |     |     | 70  |     |     |
| --- | ----- | --- | --- | --- | --- | --- | --- | --- |

Targeting the robo-advice customer:
The development of a psychometric segmentation model for financial advice robots
1. Explained variance
2. Group size >100
3. Interpretation of homogeneity of the groups
4. If no clear interpretation, start at rule 1
The dominant psychometric segments and their means are displayed in Table 2.
Table 2
Psychometric segments in The United Kingdom and The Netherlands
United Kingdom Netherlands
Convenience Convenience Trustful with Financially
seekers Financial illiterates Rigids seekers knowledgables Rigidits unknowledgebales
Mean Mean Mean Mean Mean Mean Mean
C1 Convenience 1,56149 -,05108 ,09060 1,6 -0,3 -0,4 -0,3
C2 Trustful with knowledge -,26301 -,90491 -,84376 -0,1 -0,9 -0,3 0,8
C3 Rigid -,44974 -,33342 1,03366 0,1 -0,8 1,0 -0,4
C4 No financial knowledge -,28716 ,83885 -,40067 - - - -
The validation approach for the discovered psychometric segments was in performing this
study across Europe’s two foremost mortgage advice markets: The UK and The Netherlands.
The UK and The Netherlands are understood as front-runners because of their advanced
financial advice eco-systems (financial advisors, governmental regulation and FinTech
industry).
3.3.2. The DPS-model and its validation in two markets.
Digital Psychometric Segmentation in The Netherlands
The principal component analysis in the first experiment shows the factors and their variables
across the experienced and inexperienced customer groups through the surveys in the UK and
The Netherlands that point toward similar factors for psychometric segmentation in digital
financial advice. This supports the explanation of the cross-cultural expectations of digital
financial advice. The factors are (1) need for convenience, (2) level of financial literacy and
(3) need for rigidity. The Digital Psychometric Segmentation-model (DPS) is presented in
Figure 1.
7701

Chapter 3
Figure 1
Digital Psychometric Advice Segmentation Model
Although the inexperienced and experienced people show great similarities, the factor impact
differs across both customer groups. Inexperienced people give more importance to trust in
advisors (24.7%) and process rigidity (18.4%), where experienced people give more
importance to financial knowledge (34.2%).
Applying the factors in a Ward cluster analysis yielded a 4-segment psychometric model. For
defining the psychometric profiles, the answers in Section E of the questionnaire were merged
with Sections A, B and C. The profiles designed are: (1) convenience seekers; (2) trustful with
knowledge, (3) rigid; and, (4) financially ignorant (no financial knowledge). The
psychometric segments are shown in Figure 2: Digital Psychometric Consumer Segments.
7721

Targeting the robo-advice customer:
The development of a psychometric segmentation model for financial advice robots
Figure 2
Digital Psychometric Consumer Advice Segments
Convenience seekers score high on (1) try to limit information search (.830); (2) buy the
product as soon as one is found (.808); (3) buy the mortgage as quickly as possible (0.776);
(4) evaluate limited alternatives (.701); and, (5) let others do the research (.642).
Rigid people are more conservative mortgage buyers. The do not trust advisors very much
(.394), tend to stick to known products and brands (.719), and decide logically and
systemically (.645) and are risk-averse (.677).
On the knowledge factor, differentiation is seen in the segments ‘trustful with knowledge’
with high scores on financial knowledge (.780) and financial market developments (.726).
The knowledge aspect makes this segment progressive showing a willingness to spend time
on finding relevant information and the best product for their needs. The customer segment
‘financially ignorant’ instead spends no time on financial decision-making. They therefore
tend to be neutral and follow financial advice.
Digital Psychometric segmentation in the UK
Although the second experiment (UK) also shows the same psychometric factors segmenting
the market, their impact differs from the Dutch market. Financial knowledge (34.1%) is the
most important variable. But rigidity (28.1%) is important for the British. Convenience
(17.1%) on the other hand is less important in the UK. Applying the factors in a Ward cluster
analysis led to a three-segment psychometric model. The British psychometric customer
segments resulting from the Ward-analyses are: (1) convenience seekers; (2) the financially
illiterate; and, (3) rigid consumers.
As in the Netherlands, British convenience seekers score high on (1) try to limit information
search (.800); (2) buy the product as soon a one is found (.826); (3) buy the mortgage as
quickly as possible (0.737); (4) evaluate limited alternatives (.801); and, (5) let others do the
7723

Chapter 3
research (.646). Different from the Dutch, British convenience seekers do look at comparative
shopping instruments such as ratings and reviews (.628).
Rigid people are more conservative mortgage buyers. They do not trust advisors very much
(.671) and decide logically and systemically (.747) They are less loyal than the Dutch
mortgage buyers in their intention to remain loyal to known products and brands (.468).
The financially illiterate group are the third psychometric segment in the British market with
low financial knowledge (.832), low financial market knowledge (.834) and are looking for
financial security (.598).
Hypothesis testing for model integration
Hypothesis 1: Psychometric segmentation can be effectively utilized in defining market
segments within the digital or robo financial advice industry, thereby facilitating the
development of personalized robo-advice strategies.
The principal component analysis with Varimax rotation showed three factors that
differentiate in psychometric mortgage advice segments. The factors are convenience
(eigenvalue of 1.89); financial illiteracy (eigenvalue of 1) and rigidity (eigenvalue of 0.51).
Based on the Kaiser criterium that eigenvalues >1 should be selected, only convenience and
financial illiteracy should be components of the psychometric model. Therefore hypothesis 1
can be validated.
Hypothesis 2: Financial illiteracy serves as a differentiating factor within the psychometric
segmentation model, contributing to the formulation of personalized robo-advice strategies.
The principal component analysis with Varimax rotation showed that financial illiteracy is a
differentiating factor in psychometric advice segmentation. The eigenvalue of 1 is good
enough to select financial illiteracy as a factor. Financial illiterates in the UK have low
financial knowledge (.832), low financial market knowledge (.834) and are looking for
financial security (.598). Also in the Dutch market, financial illiterates have low financial
knowledge (.780), low financial market knowledge (.726). Also, the study in the Dutch
market revealed a fourth segment ‘trustful with knowledge’. They are the most progressive
customer segment and spend a lot of time in finding the best solution matching their needs.
Financial (il)literacy is a differentiating factor in psychometric customer segmentation. So
also, the second hypothesis can be validated.
Hypothesis 3: Motivation constitutes a distinguishing factor within the psychometric
segmentation model, contributing to the formulation of personalized robo-advice strategies.
The principal component analysis did not show motivation as a differentiating psychometric
factor. Nevertheless, in the factor, scores differentiating between people who actively seek
relevant information, spend time and keep searching until they find the best solution for their
needs show high loadings. These people are segmented in the UK in the psychometric
segment of the ‘rigids’. In The Netherlands, they are segmented in the psychometric segment
of ‘trustful with knowledge’. So, although not a factor in the model, someone’s personal
motivation is something to consider when developing digital strategies. Thus, hypothesis 3
cannot be validated.
7743

Targeting the robo-advice customer:
The development of a psychometric segmentation model for financial advice robots
Hypothesis 4: Risk tolerance functions as a differentiating factor within the psychometric
segmentation model, influencing the development of personalized robo-advice strategies.
The principal component analysis did not show risk tolerance as a differentiating
psychometric factor. The influence of risk tolerance in the UK is seen in the customer
segment of the financially illiterate who seek maximum security. In the Dutch psychometric
segmentation risk tolerance also influences the behavior of the financially ignorant who seek
maximum security. But also, ‘trustful with knowledge’ with a higher risk tolerance include
people that are open for trying new products and services. Nevertheless, hypothesis 4 cannot
be validated.
3.4 Discussion
As outlined in the introduction, the purpose of this study is to develop a psychometric market
segmentation model to enhance the inclusivity, tailoring, personalization, and overall impact
of digital financial advice. Traditional segmentation models in consumer finance primarily
focus on observable demographic or economic criteria, such as profession, age, income, or
wealth (Meidan, 1984; Harrison, 1994). However, this research is, by our knowledge, the first
that identified post hoc psychometric factors—such as the effort invested in finding financial
information, the process of selecting financial products, the level of financial knowledge and
understanding, risk appetite, and individual decision-making styles—for financial advice that
support digital advice usage.
Based on the psychometric attributes tested in the United Kingdom and the Netherlands, this
cross-cultural study identified three key psychometric factors that should be considered when
targeting a market with a digital advice solution. Convenience emerged as the dominant
factor, highlighting the need for customers to find the best-fit product with minimal effort.
This segment is particularly receptive to content personalization strategies, as well as
predictive and prescriptive automated services. When effectively implemented, these
strategies make this segment approachable for digital advice solutions like intelligent agents
and virtual assistants.
Financial literacy emerged as the second key psychometric factor to consider when targeting a
digital advice market. This factor is influenced by attributes such as the level of financial
knowledge, understanding of financial market developments, and individual risk appetite.
Financial literacy is a bipolar attribute: those with low literacy often require education and
support in their financial decision-making, primarily seeking solutions that provide financial
security. Although individuals with low financial literacy may not be the most promising
segment for digital or robo-advice, digital advisors can still serve this group through
educational resources, orientation tools, and transaction aids that support informed financial
decisions. There is a significant opportunity to develop digital educational tools to promote
financial inclusion for the 4.5 billion underserved people globally.
At the other end of the spectrum are customers with high financial literacy. These individuals
have a strong interest in personal finance and market developments and tend to invest
considerable time in expanding their knowledge. They are often seen as role models by
friends and family due to their expertise. This highly knowledgeable segment is an attractive
target for digital advice solutions like robo-advice, as they are open to new products and
services. Similar to the convenience-driven segment, they respond well to content
7745

Chapter 3
personalization and predictive services. However, unlike the convenience segment, these
“knowledgeable and trusting” customers value additional resources such as reviews, ratings,
and blogs to further expand their understanding.
The third psychometric factor identified in the research is rigidity, or the degree of process
orientation, which is relevant when targeting a market for digital advice. Individuals with high
rigidity make financial decisions logically and systematically, often taking a conservative
approach and seeking control over their decisions. They invest considerable time in finding
the best solution due to a general distrust of advisors. This segment may seem less appealing
for digital financial advsors because of their emphasis on process trust. However, if digital
tools—such as decision support or content tools—are developed to effectively support
information searches and enhance financial control, these individuals may be more inclined to
use them. A targeting model for digital and robo-advisors addressing the different
psychometric segments is presented in Figure 3.
Figure 3
Digital Psychometric Segmentation Model (DPS)
The DPS-model offers financial advisors and regulators valuable tools for delivering
personalized, customer-centric financial services. For advisors, the model allows for targeted
service customization, particularly for vulnerable customers, by providing insights into
psychometric traits such as financial literacy and rigidity. This enables proactive support to at-
risk customers, helping to prevent poor financial behaviors through tailored guidance. The
model also aids in the strategic deployment of robo-advisors, focusing on segments like
convenience seekers and financially knowledgeable individuals, ensuring digital resources are
used effectively to enhance customer engagement.
For regulators, the DPS-model provides a framework to ensure financial institutions are
meeting the diverse needs of their customers, particularly the most underserved. By
promoting the inclusion of educational and control tools, regulators can oversee that banks
support sound financial decision-making across all customer segments. This model not only
7765

Targeting the robo-advice customer:
The development of a psychometric segmentation model for financial advice robots
enhances personalization and financial inclusion but also helps align financial services with
responsible practices that promote customer well-being.
For researchers, the DPS-model presents a robust framework for advancing digital advice
through the integration of next-generation AI, machine learning, deep learning, and big data.
By leveraging these technologies, researchers can enhance the model's ability to analyze and
predict complex customer behaviors, providing deeper insights into psychometric traits and
their impact on financial decision-making. With AI and machine learning, the DPS-model can
be continuously refined to identify emerging patterns, making it more responsive and
adaptable to evolving customer needs. Additionally, the vast data available through big data
analytics enables researchers to validate and expand the model across diverse demographics
and geographic regions, offering a more comprehensive understanding of digital advice
effectiveness. Ultimately, the DPS-model equips researchers with a powerful tool for
exploring how advanced technologies can optimize personalized financial advice on a larger
scale, contributing to a more data-driven and dynamic approach to inclusive customer-centric
digital financial services.
3.5 Limitations
There are some limitations to this research that should be considered when interpreting the
findings. Firstly, the new models were derived from research conducted in the UK and Dutch
markets. While these markets are considered leaders in digital financial advice, further
research is needed in other regions to determine if the findings can be generalized globally.
Additionally, the data for this study were gathered in the year when both the UK and Dutch
governments implemented commission bans on complex financial advice, which has since
driven the growth of low-cost online financial advisors. However, as this research was
conducted shortly after these changes, the benefits related to pricing and accessibility from
these digital advisors are still in early stages. To fully understand the long-term effects, future
research should incorporate time-series data to monitor how the drivers in the DPS-model
evolve over time.
Lastly, this research focused exclusively on digital mortgage advice. Further studies could
expand the scope to include other business models, such as comparison sites, robo-wealth
advisors, and digital advisors in other sectors, like healthcare and utilities. This would provide
a broader understanding of how the DPS-model applies across various industries.
7767

Chapter 3
REFERENCES
Andreasen, A. R., Kotler, P. & Parker, D. (2003) Strategic marketing for nonprofit
organizations. Upper Saddle River, NJ: Prentice Hall.
ASIC (2010). ‘Access to financial advice in Australia’. Australian Securities & Investment
Committee, Report 224
Bradbury, T. (2014) ‘Robo advice is coming: What it means, who will buy it-and why’,
Professional Planner, 69, 40.
Burnett, J. J. & Chonko, L. B. (1984) ‘A segmental approach to packaging bank products.’
Journal of Retail Banking 6.1/2, 9-17.
Collins, M. J. (2010) ‘A review of financial advice models and the take-up of financial
advice’. Center for Financial Security WP 10.5.
Deci, E. L. & Ryan, R. (2010) Self‐determination. John Wiley & Sons Inc.
Demirguk-Kunt, A. et al. (2014). ‘Measuring financial inclusion around the world’. World
Bank Policy Working Paper.
Dickson, P. R. & Ginter, J. L. (1987) ‘Market segmentation, product differentiation, and
marketing strategy.’ The Journal of Marketing, 1-10.
Emons & Winand (1997) ‘Credence goods and fraudulent experts.’ The RAND Journal of
Economics, 107-119.
FINRA (2012) ‘Financial capability in the United States’. Report of findings of the 2012
national financial capability study.
Frank, Ronald Edward, William F. Massy, and Yoram Wind. Market segmentation.
Englewood Cliffs, NJ: Prentice-Hall, 1972.
Frey, C. B. & Osborne, M. (2015) ‘Technology at work: The future of innovation and
employment’, Citi GPS.
Goldman Sachs (2017) ‘Millennials coming of age’. Retrieved from: Goldman Sachs.com.
Hamka, F. et al. ‘Mobile customer segmentation based on smartphone measurement.’
Telematics and Informatics 31.2 (2014): 220-227.
Harrison, T. S. (1994) ‘Mapping customer segments for personal financial services.’
International Journal of Bank Marketing 12.8: 17-25.
Hartmann, P. M. et al. (2014) ‘Big data for big business? A taxonomy of data-driven business
models used by start-up firms.’ A Taxonomy of Data-Driven Business Models Used by Start-
Up Firms.
7787

Targeting the robo-advice customer:
The development of a psychometric segmentation model for financial advice robots
Kahle, L. R., Beatty, S.E. & Homer, P. (1986) ‘Alternative measurement approaches to
consumer values: the list of values (LOV) and values and life style (VALS).’ Journal of
consumer research 13.3: 405-409.
Kotler, P. & Cox, K.K. (1980) Marketing Management and Strategy, Prentice Hall.
Machauer, A. & Morgner, S. (2001) ‘Segmentation of bank customers by expected benefits
and attitudes.’ International Journal of Bank Marketing 19.1: 6-18.
Malhotra, R. & Malhotra, M.K. (2006). ‘The impact of internet and e-commerce on the
evolving business models in the financial services industry.’ International Journal of
Electronic Business 4.1: 56-82.
Moutinho, L. & Meidan, A. (1989) ‘Bank Customers′ Perceptions, Innovations and New
Technology.’ International Journal of Bank Marketing 7.2: 22-27.
Nelson, P. (1970) ‘Information and consumer behavior.’ Journal of Political Economy 78.2:
311-329.
Plummer, J. T. (1974) ‘The concept and application of life style segmentation.’ The Journal of
Marketing 33-37.
Price Waterhouse Coopers (2014) ‘Engaging and empowering millennials’. A follow-up to
PWC’s next-gen global generational study.
Rokeach, M. (1973) The nature of human values. Free press.
Roszkowski, M. J. & Davey, G. (2010) ‘Risk perception and risk tolerance changes
attributable to the 2008 economic crisis: A subtle but critical difference.’ Journal of Financial
Service Professionals 64.4: 42-53.
Rusciano, R., & Pilusop, F. (2023). Innovative digital tools in financial advice: robo-
advisors. UNICARTradEconomy & Finance, 421.
Smith, W. R. (1956) ‘Product differentiation and market segmentation as alternative
marketing strategies.’ The Journal of Marketing: 3-8.
Transparency Research (2016) ‘Increasing small business units to act as building blocks for
peer to peer lending market’.
Tversky, A. & Kahneman, D. (1974) ‘Judgment under uncertainty: Heuristics and biases.’
Utility, probability, and human decision-making. Springer Netherlands, 141-162.
Van Raaij, W. F. (2016) Understanding Consumer Financial Behavior. Money Management in
an Age of Financial Illiteracy. New York: Palgrave Macmillan.
van Raaij, W. F. & Verhallen, T.M.M. (1994) ‘Domain-specific market segmentation’,
European Journal of Marketing, 28(10), 49-66.
7789

Chapter 3
van Thiel, Diederick, Goedee, J. & Reijnders, W.J.M. (2008) ‘Riding the waves. The future of
| banking starts now.’, Pearson Prentice Hall.  |     |     |     |
| --------------------------------------------- | --- | --- | --- |
|                                               |     |     |     |
van Thiel, Diederick. & Van Raaij, W.F. (2017) ‘Explaining Customer Experience of Digital
| Financial Advice.’ Economics 5.1: 69-84.  |     |     |     |
| ----------------------------------------- | --- | --- | --- |
|                                           |     |     |     |
Wolinsky, A. (1995) ‘Competition in markets for credence goods’, Journal of Institutional
and Theoretical Economics (Zeitschrift für die gesamte Staatswissenschaft), 151, 117-131.
Worldbank (2015) ‘Access to financial services – A key to lifting people out of poverty.’
| World Bank research.  |     |     |     |
| --------------------- | --- | --- | --- |
|                       |     |     |     |
Ziff, R. (1971) ‘Psychometrics for market segmentation.’ Journal of Advertising Research  Equipped with a psychometric segmentation model, we shift to the realm of credit
11.2: 3-9.
    assessment, where we explore how financial personality profiles can improve inclusivity,
accuracy and predicitve power. This chapter investigates the application of psychometric data
to credit scoring, especially relevant in an era of global financial uncertainty. Here, we lay the
groundwork for understanding how psychometric data can further revolutionize
credit assessment and decision-making.

|     | 8709  |     | 80  |
| --- | ----- | --- | --- |

Targeting the robo-advice customer:
The development of a psychometric segmentation model for financial advice robots
Equipped with a psychometric segmentation model, we shift to the realm of credit
assessment, where we explore how financial personality profiles can improve inclusivity,
accuracy and predicitve power. This chapter investigates the application of psychometric data
to credit scoring, especially relevant in an era of global financial uncertainty. Here, we lay the
groundwork for understanding how psychometric data can further revolutionize
credit assessment and decision-making.
8801

Chapter 3
82

Chapter 4
Leveraging Financial Personality for
Inclusive Credit Scoring Amidst Global
Uncertainty
Published as:
Van Thiel, D., Goedee, J., & Leenders, R. (2023).
Leveraging financial personality for inclusive credit scoring amidst global uncertainty.
Journal of Risk Management in Financial Institutions, 17(1), 22-42.

Chapter 4
ABSTRACT
The Ukraine war, high inflation, and rising interest rates are jeopardizing people's ability to
afford essential items such as food and energy, causing a widespread sense of vulnerability
worldwide. Consequently, access to finance has become increasingly challenging for
vulnerable consumer groups, including young adults without established credit histories,
senior citizens with fixed incomes, start-up entrepreneurs, sole traders, single parents,
immigrants in Western markets. To address this issue, this study explores the potential use of
individuals' financial personality for inclusive credit scoring in these uncertain environments.
Examining a sample of low-income individuals in the US and the Netherlands, our
psychometric scoring models (PSMs) demonstrate that late payments can be attributed to
factors such as financial capability, materialistic tendencies, impulsive buying behavior, social
desirability, and attitudes towards debt. These findings provide evidence that PSMs offer a
viable solution to advance financial inclusion for vulnerable customer segments amidst global
uncertainty.
Keywords: Access to finance, inclusive finance, behavioral finance, psychometric credit
scoring, financial crisis, responsible lending
4.1 Introduction
To what extend can psychometrics advance inclusive finance among vulnerable customer
segments in unstable Western economies post-COVID? Prior to the COVID-19 outbreak,
approximately 2.5 billion individuals were already unbanked or underbanked (World Bank,
2018). The World Bank has recognized financial inclusion as a means to support seven out of
the 17 sustainable development goals. The global financial crisis caused by COVID-19, along
with forthcoming macroeconomic instability, has further amplified financial vulnerability and
imposed additional barriers to financial access for vulnerable customers (Bankowska et al.,
2020). Vulnerable customers are individuals who, due to personal circumstances, are at risk of
financial harm, particularly when businesses fail to provide them with adequate care (Elliot et
al., 2022; Coppack et al., 2015). The British Financial Conduct Authority (FCA) regards an
individual's health, life events, resilience, and capabilities as the primary factors influencing
their present or future vulnerability (FCA, 2019). In a poll conducted by the Associated Press
in October 2022, it was found that 46 percent of U.S. adults describe their financial situation
as poor due to high inflation (PBS, 2022). Similar levels of financial vulnerability are
observed in Western Europe (APG 2023, FCA, 2021). This includes young adults, senior
citizens with fixed incomes, startup entrepreneurs, sole traders, small business owners,
immigrants, individuals whose illnesses impact their earning capacity, those affected by
natural disasters such as extreme heat, fires, or floods, etc. A recent survey conducted by the
British Financial Conduct Authority (FCA) on customer vulnerability revealed that COVID-
19 has disproportionately affected specific population groups, including younger adults and
the self-employed (Financial Conduct Authority UK, 2021a). As indicated in Table 1, more
than 100 million Americans and 90 million Europeans categorized as vulnerable. They rely on
access to credit as a crucial necessity for improving their financial prospects and achieving
upward mobility (Hurley & Adebayo, 2016).
8842

Leveraging Financial Personality for Inclusive Credit Scoring Amidst Global Uncertainty
Table 1
Vulnerable income segments (Eurostat, 2020; Semega, 2020)
EU USA
Number of people (million) 445 328,2
Number of low-income households (million) 43 53
Number of self-employed workers (million) 23.4 44
Number of MSME entrepreneurs (million) 24.7 30.7
The concept of vulnerability includes consumers who are prone to facing high credit costs and
those excluded from conventional credit or financial services (Bourova & Ramsay, 2019).
Moreover, a rising degree of financial hardship, marked by individuals taking on debt
obligations under a contract but subsequently struggling to meet them when they become due,
serves as an indicator of their level of financial vulnerability (Bourova & Ramsay, 2019).
Limited or unstable income, which often results in being classified as high credit risk and
having limited collateral, can lead to financial exclusion or result in high costs of credit in a
tightly regulated financial environment (FCA, 2021a).
The regulatory framework for credit scoring systems in the USA and most European
countries, however, differs significantly. In contrast to the United States, most European
countries, follow a negative credit scoring system, wherein only unpaid debts are recorded. To
examine the effects of these macro-economic credit scoring systems, this research focuses on
two different systems: the positive credit scoring system in the USA and the negative credit
scoring system in the Netherlands. Regardless of the system, lenders across both markets,
including banks, credit card companies, and alternative finance providers, still assess the
creditworthiness of loan applicants. They utilize these credit scores to evaluate the potential
risk involved in lending money to customers and minimize losses resulting from bad debts.
Credit scoring comprises predictive models and techniques employed by financial institutions
to determine creditworthiness (Rezac & Rezac, 2011). It involves formal statistical methods
that classify credit applicants into "good" and "bad" risk categories (Hand, 1977). In the US, a
credit score is a numerical representation of the likelihood of individuals repaying their bills,
derived from statistical analysis of their credit files. These statistical models predicting credit
risk utilize predictor variables such as age, income, marital status, and other conventional data
to estimate the probability of defaulting (Lahsana et al., 2010). We contend that relying on
conventional data excludes vulnerable customer segments from financial services because
many of them lack traditional financial and credit information. Recent research suggests that
alternative data sources such as OB-based payment models (Rishabh, 2022), mobile phone
data (Liu et al., 2017; Oskarsdottir et al., 2019; San Pedro et al., 2015; Shema, 2019), and
social media data (Tan & Phan, 2018; Wei et al., 2016; Yuan et al., 2018; Zhang et al., 2016)
yield significantly improved predictive credit performance and repayment likelihood
compared to traditional credit scoring models. In this study, we investigate the potential
benefits of incorporating psychometric data into the development of financial profiles to
improve access to finance in the current market context.
Other recent studies suggests that AI-enabled profiles assist lenders in better understanding
consumer behaviors and subsequently assessing the likelihood of loan repayment, thereby
reducing the lender's risk when granting loans (Biallas & O'Neill, 2020). The dominant metric
for model quality in the USA is the Kolmogorov-Smirnov index (KS) (Rezac & Rezac, 2011),
which shows the accuracy of a default prediction by comparing the cumulative good
customers with the cumulative bad ones. Most European lenders, however, apply the Gini
coefficient as the leading metric for measuring model quality. The Gini coefficient indicates
8835

Chapter 4
the credit model’s discriminatory power, namely its efficiency in discriminating between good
borrowers who will not default in the future and bad borrowers who will. The Gini coefficient
applied in risk modeling equals Somers’ D, which is a measure of the ordinal relationship
between the model’s probability of default and the actual outcome (Somers, 1962). Somers’ D
is a summary of the cumulative accuracy profile curve and takes a value between -1 and 1; -1
being a perfect negative relationship, 0 being a random relationship and 1 being a perfect
positive relationship. In practice, a credit score model with a Somers’ D of 0.4 is considered a
good model (Somers, 1962). Regardless of the differences in the underlying statistics of these
metrics, both American and European lenders assess the creditworthiness of their applicants
and evaluate the predictive power of their models contentiously. In this study, we develop a
novel logistic regression model with the dual objectives of achieving the highest predictive
accuracy while adhering to regulatory requirements, such as explainability.
With growth and change come concerns about protecting consumers from firm exploitation
due to imperfect information and contracting as well as from their own decision-making
limitations (Garz et al., 2021). In the USA, the Fair Credit Reporting Act (FCRA) regulates
credit reporting agencies and compels them to ensure that the information they gather and
distribute is a fair and accurate summary of a consumer’s credit history. The FCRA is chiefly
concerned with the way credit reporting agencies use the information they receive regarding
one’s credit history. The law is intended to protect consumers from information being used
against them. It offers very specific guidelines on the methods that credit reporting agencies
can use to collect and verify information and outline the reasons for the release of
information. Vulnerable customers have issues accessing finance because of their less
favorable credit ratings (Semega, 2020). A favorable credit rating is necessary to obtain a
credit card, purchase a home or car, start a new business, seek higher education, or pursue
other important goals such as access to employment, rental housing and insurance (Hurley &
Adebayo, 2016). Nevertheless, numerous vulnerable customers possess either no credit
history or a low credit score. In Europe, the European Securities and Market Authority
(ESMA) oversees credit rating agencies and the associated credit rating agency regulation
(CRA). The CRA is designed to enhance the integrity, responsibility, good governance, and
independence of credit rating activities to ensure quality ratings and high levels of investor
protection. Hurley and Adebayo (2016) argue, however, that individuals have very little
control over how they are scored and have even less ability to contest inaccurate, biased, or
unfair assessments of their credit. Traditional, automated credit-scoring tools raise
longstanding concerns regarding accuracy and unfairness. We argue that traditional credit
scoring models are drivers of financial exclusion due to their stringent focus on financial and
credit data. However, also in our opinion, Hurley and Adebayo (2016) rightfully conclude that
the recent advent of new “big-data” credit-scoring products heightens these concerns.
Moreover, the uncertainty of the impact of the unprecedented COVID-19 pandemic on
traditional credit score cards and credit decision-making makes the development of different
responsible credit score models for granting credit to vulnerable customer segments urgent.
Therefore, the purpose of this study is to develop a credit rating system that enables
responsible lending to vulnerable customers in the regulatory context of the USA and The
Netherlands, utilizing alternative psychometric data sources in addition to the traditional
credit score data they often lack. While there is consensus on the significance of consumers'
access to finance for their financial well-being, recent events such as severe heatwaves,
floods, the COVID-19 pandemic and the energy crisis have emphasized the prevalence of
vulnerability, prompting the need to address essential underlying questions. For instance, in
the face of changing circumstances and outdated traditional credit score data, how can we
distinguish between good and bad payers among vulnerable customers in these changing
market conditions? What are the stable personality traits that contribute to favorable payment
8864

Leveraging Financial Personality for Inclusive Credit Scoring Amidst Global Uncertainty
behavior? In this research, we investigate these questions and identify the essential factors
required to create a credit scoring system specifically designed for vulnerable consumers in
Western economies. This will help us test our central hypothesis:
H1: Psychometric credit scoring increases access to finance for vulnerable consumer
segments across the USA and The Netherlands in unstable market conditions.
4.2 Vulnerability and big data
Generally speaking, customer vulnerability refers to situations in which customers do not
engage effectively with their financial service providers and, as a result, put themselves at risk
(Competition and Markets Authority (CMA), 2019). Vulnerability can manifest in various
ways, including being temporary, permanent, gradual, or sudden (Coppack et al., 2015). It can
also be subjective, influenced by beliefs and attitudes, or objective, influenced by external
factors such as debt and credit (O’Connor et al., 2019). Similar to a credit score, customers'
financial well-being fluctuates based on their financial management (Yurdakul et al. 2017).
However, vulnerability can be broadly classified into two categories: driven by personal
situations or market-specific circumstances (CMA, 2019).
The United Kingdom’s Financial Conduct Authority, one of the world’s front-runner financial
authorities, has identified a number of drivers of actual or potential vulnerability from
personal circumstances, including health problems (physical or mental), negative life events,
resilience to shocks, and inability to deal with financial matters (Mogaji, et al., 2020). The
CMA also includes physical disability or low income. Customers who are often in significant
debt are more likely to fall behind on their household bills or credit card payments. They are
also excluded from accessing financial services, such as loans. Poor or no credit scores and
large debts lead them to be high-risk customers. Due to financial exclusion, these individuals
may never gain a digital or financial footprint to indicate how well they have managed their
finances. Without a financial identity, they continue to be excluded.
Furthermore, access to financial services can be further inhibited by a lack of mobile phone,
internet connection, or technological skills. Market-specific vulnerability is due to market
contexts that limit access to financial services (CMA, 2019). Moreover, the COVID-19
pandemic is a driver of market-specific vulnerability that exacerbates inequality on a global
scale (Salampasis & Mention, 2018). However, in recent years, banks have seen technology
as a tool to boost their competitiveness. For example, Poppleton et al. (2019) state that
technology continues to significantly impact the home mortgage sector of retail banking.
Fintech embraces technology to deliver an alternative to traditional banking and is expected to
extend financial market reach to those that are excluded and underserved (Mogaji, 2020).
Fintech generates a comprehensive data view of customers refined by artificial intelligence
(AI) to improve customer offerings and experiences. Fintech is, therefore, transforming
financial inclusion on a long-term, large-scale basis. Consequently, the credit-scoring industry
has experienced a recent explosion of start-ups that take an “all data is credit data” approach,
combining conventional credit information with thousands of data points mined from
consumers’ offline and online activities (Hurley & Adebayo, 2016).
Big data scoring tools may now base credit decisions on where people shop, the purchases
they make, their online social media networks, and various other factors that are not
intuitively related to their credit scores (Van Thiel & van Raaij, 2019). Therefore, national
governments protect financial consumers against transparency, privacy, and data breaches by
maintaining regulations such as the General Data Protection Regulation (GDPR) in Europe
(EU, 2016) and the California Consumer Privacy Act (CCPA) in California (Becarra, 2018).
According to these American and European consumer protection directives, consumers have
the right to make informed decisions, the right to choose and change their mind, and the right
8857

Chapter 4
to pay back ahead of time, the right to be safe, and to be heard. However, are all customers knowledge and financial skills (Remund, 2010). Financial knowledge is the most common
capable of doing so? In the American and European Consumer Credit Directives, it is required definition of financial literacy. It is based on the idea that for effective money management,
that creditors do not engage in irresponsible lending. Moreover, they should bear the people must understand how money works. Examples of financial knowledge include
responsibility of individually checking the vulnerability of each consumer. Nevertheless, there understanding the mechanisms of compound interest, collaterals, and credit history. Besides
is evidence that some types of financial services, such as payday loan lenders, online financial knowledge, financial skills (sometimes referred to as financial behavior) are also
gambling firms, and online travel agents exacerbate and add to customer vulnerabilities considered to be part of financial literacy (Joo & Grable, 2004). Financial skills concern the
(CMA, 2019). Since they lack credit scores in the customer aggregate data, vulnerable ability to perform tasks related to money management, such as budgeting and tracking
customers cannot access fair deals, which leads to adverse and negative impacts on these expenses. Better financial skills are associated with higher savings and lower debt (Dew &
customers. For example, when vulnerable customers access a financial product, they may face Xiao, 2011; Moore 2003). We argue that vulnerable customers are often financially illiterate
higher charges than better-off customers (CMA, 2019), such as high-interest loans or high and poorly financially skilled and therefore, often end up with financial problems. Therefore,
premiums on insurance. we include financial skills as the first construct in our conceptual model and argue that it has a
negative correlation with arrears.
With consumer protection in mind, using non-traditional data for credit scoring might benefit
financial inclusion. Extant findings, for example, indicate that mobile phone data such as call Moreover, recent research on vulnerable customers shows that one of the personal
detail records, device features, mobility features, and airtime recharge are at least as good in characteristics that drives vulnerability is impulsive buying (O’Connor et al., 2019).
predicting customer payment behavior as traditional data (Liu et al., 2017; Oskarsdottir et al., Additionally, researchers found that people with low self-control tend to engage more in
2019; San Pedro et al., 2015; Shema, 2019). Additionally, social media data such as compulsive buying and have more debt (Achtziger, Hubert, Kenning, Raab, & Reisch, 2015),
someone’s activity, texts, photos and videos, network density, and someone’s centrality in the whereas people with high self-control are more likely to save money from each paycheck
network have been a research focus for credit scoring (Tan & Phan, 2018; Wei et al., 2016; (Strömbäck, Lind, Skagerlund, Västfjäll, & Tinghög, 2017). Moreover, Norvilitis et al.
Yuan et al., 2018; Zhang et al., 2016). Customer protection regulations in Western countries, (2006)found that having difficulties delaying gratification has been related to having a
however, forbid lenders to use these data sources for credit decision-making because of higher amount of debt and problematic gambling (Parke, Griffiths, & Irwing, 2004).
customer privacy and transparency. Gratification refers to the process in which a person foregoes an immediate reward in order to
receive a larger reward later. We therefore add gratification as the second variable to our
Given that vulnerable customers, especially in the context of the economic consequences of conceptual model and argue a positive correlation.
high inflation, natural disasters and the COVID-19 pandemic, need novel credit scoring
solutions to increase their access to finance, we aimed to identify transparent alternative Other debt-related research reveals that students get into deeper debts because they
drivers that correlate with their payment behavior. Inspired by venture capital investors— overestimate how much they will earn after they graduate (Seaward & Kemp, 2000).
hampered by the lack of reliable data for predicting their investment risk and having to place Consumers are also more likely to get a new credit card if they think it is easy to repay the
the quality of the founding team at the center of their seed and early-stage investments for balance (Yang, Marcoczy, & Qi, 2007). In short, consumers take high risks because they are
decades (Ruhnka & Young, 1991)—we investigated personality data to predict payment risks. too confident (Nosić & Weber, 2010). The term (over)confidence is used in at least three
As we describe in the literature section of this paper, many other studies have shown the ways: to describe overestimation, over placement, and calibration of subjective probabilities
direct effect of personality traits on financial behaviors, but few have focused on the holistic (Moore & Healy, 2008; Olsson, 2014). The first definition refers to the overestimation of
psychometric profile construct to predict payment behavior. Klinger et al. (2013), however, one’s achievements, actual ability, or chance of success in comparison to one’s actual
found the predictive value of psychometric features for predicting the credit risk of small performance, ability, or success. For example, a person’s actual score on a test is compared to
businesses in Peru. Their credit scoring model for Peruvian small businesses was built upon that person’s estimate of their score. The second definition, over placement, refers to the
the Big 5 personality model (Bernadin & Cooke, 1993), as well as measures of intelligence, comparison between a person’s achievements and the performance of others. That is, the type
numeracy, and integrity (Bernadin & Cooke, 1993; Costa & McCrae, 1992; Spearman, 1946). of overconfidence that occurs when people think they are better than others. For example, a
person’s estimate of their rank (compared to others) is compared with their actual rank. Lastly,
4.3 Influence of financial personality on financial behavior the calibration of subjective probabilities (also referred to as over precision or realism of
Although a lot of research has been performed on individual behavioral traits and financial confidence) refers to the comparison of someone’s subjective probabilities with actual
behavior, a holistic approach is lacking. Nevertheless, we made use of existing literature on objective probabilities. Based on these earlier debt-related research findings we also add
the influence of financial personality on financial behavior and debt to establish a conceptual confidence to our conceptual model and postulate a positive correlation with debt and
model with constructs that may influence late payment behavior. First, consumers’ ability to therefore also with arrears.
make informed financial decisions improves their ability to develop sound personal finance
(Klapper, Lussardi & Panos, 2013). Therefore, many studies have investigated the Other research on student and household debt shows that more positive attitudes toward debt
relationship between financial literacy and financial decision-making (Lusardi & Mitchell, are associated with more debt (Almenberg et. al, 2020; Haultain, Kemp & Chernyshenko,
2011). Financial illiteracy appears to be particularly severe for key demographic and often 2010). Moreover, they found that there were two different types of attitudes associated with
vulnerable groups: women, less educated, those with low income, ethnic minorities, and older debt. On the one hand, having more fear of debt was associated with less debt, whereas seeing
respondents (Bernheim, 1998; Lusardi & Mitchell, 2007, 2008, 2011; Lusardi & Tufano, the utility of debt was associated with more debt. We argue that vulnerable customers with
2009). The term financial literacy has been used loosely and is used both to describe financial positive attitudes toward debt face a high risk of indebtedness, consequently leading to
8886 87

Leveraging Financial Personality for Inclusive Credit Scoring Amidst Global Uncertainty
knowledge and financial skills (Remund, 2010). Financial knowledge is the most common
definition of financial literacy. It is based on the idea that for effective money management,
people must understand how money works. Examples of financial knowledge include
understanding the mechanisms of compound interest, collaterals, and credit history. Besides
financial knowledge, financial skills (sometimes referred to as financial behavior) are also
considered to be part of financial literacy (Joo & Grable, 2004). Financial skills concern the
ability to perform tasks related to money management, such as budgeting and tracking
expenses. Better financial skills are associated with higher savings and lower debt (Dew &
Xiao, 2011; Moore 2003). We argue that vulnerable customers are often financially illiterate
and poorly financially skilled and therefore, often end up with financial problems. Therefore,
we include financial skills as the first construct in our conceptual model and argue that it has a
negative correlation with arrears.
Moreover, recent research on vulnerable customers shows that one of the personal
characteristics that drives vulnerability is impulsive buying (O’Connor et al., 2019).
Additionally, researchers found that people with low self-control tend to engage more in
compulsive buying and have more debt (Achtziger, Hubert, Kenning, Raab, & Reisch, 2015),
whereas people with high self-control are more likely to save money from each paycheck
(Strömbäck, Lind, Skagerlund, Västfjäll, & Tinghög, 2017). Moreover, Norvilitis et al.
(2006)found that having difficulties delaying gratification has been related to having a
higher amount of debt and problematic gambling (Parke, Griffiths, & Irwing, 2004).
Gratification refers to the process in which a person foregoes an immediate reward in order to
receive a larger reward later. We therefore add gratification as the second variable to our
conceptual model and argue a positive correlation.
Other debt-related research reveals that students get into deeper debts because they
overestimate how much they will earn after they graduate (Seaward & Kemp, 2000).
Consumers are also more likely to get a new credit card if they think it is easy to repay the
balance (Yang, Marcoczy, & Qi, 2007). In short, consumers take high risks because they are
too confident (Nosić & Weber, 2010). The term (over)confidence is used in at least three
ways: to describe overestimation, over placement, and calibration of subjective probabilities
(Moore & Healy, 2008; Olsson, 2014). The first definition refers to the overestimation of
one’s achievements, actual ability, or chance of success in comparison to one’s actual
performance, ability, or success. For example, a person’s actual score on a test is compared to
that person’s estimate of their score. The second definition, over placement, refers to the
comparison between a person’s achievements and the performance of others. That is, the type
of overconfidence that occurs when people think they are better than others. For example, a
person’s estimate of their rank (compared to others) is compared with their actual rank. Lastly,
the calibration of subjective probabilities (also referred to as over precision or realism of
confidence) refers to the comparison of someone’s subjective probabilities with actual
objective probabilities. Based on these earlier debt-related research findings we also add
confidence to our conceptual model and postulate a positive correlation with debt and
therefore also with arrears.
Other research on student and household debt shows that more positive attitudes toward debt
are associated with more debt (Almenberg et. al, 2020; Haultain, Kemp & Chernyshenko,
2010). Moreover, they found that there were two different types of attitudes associated with
debt. On the one hand, having more fear of debt was associated with less debt, whereas seeing
the utility of debt was associated with more debt. We argue that vulnerable customers with
positive attitudes toward debt face a high risk of indebtedness, consequently leading to
8879

Chapter 4
payment difficulties. Therefore, we also add debt attitude to our conceptual model and
hypothesize a positive correlation with arrears.
Previous studies also have consistently found a relationship between materialistic value and
debt (Garðarsdóttir & Dittmar 2012; Norvilitis et al., 2006). Materialism is the extent to
which people value the acquisition and consumption of material objects (Norvilitis et.al,
2006). Moreover, research has shown that there are two scales that measure individual
differences in materialism. The first scale is the Material Values Scale (Richins & Dawson,
1992; Richins, 2004), which operationalizes materialism as a set of values related to
acquisition centrality, acquisition as the pursuit of happiness, and possession-defined success.
The second scale is the Trait Materialism Scale (Belk, 1985), which assesses three aspects of
materialism: possessiveness, non-generosity, and envy. Based on these studies we add
materialism to our conceptual model and argue a positive correlation with debt and arrears.
The issue with the materialism scales is that they are based on questionnaires that
consequently show self-reported insights in which people tend to present themselves more
favorably. This phenomenon is called social desirability (Nederhof, 1985). There are two
types of socially desirable responses: a person may actually believe the reported information
(self-deception) or a person may fake information to conform to the norm. Answering in a
socially desirable way can lead to spurious correlations and to the moderation or suppression
of the relationship between the researched constructs (Ganster, Hennesey, & Luthans, 1983).
Although Norvilitis et al. (2006) do not measure social desirability, they state that it might
influence whether people report their debt. In our research, we add social desirability to our
conceptual model too and hypothesize a positive correlation with debt and arrears.
Based on earlier research on customer vulnerability and personal drivers of debt, we develop
a financial lifestyle framework to predict payment behavior. We incorporate the demographic
variable of age into the financial lifestyle framework to account for an individual's life
experience and its negative relation with arrears. The conceptual model provides a holistic
view on the personality drivers that predict debt. Based on our research to psychometric credit
scoring, we hypothesize a positive correlation between gratification, materialism, debt
attitude, confidence and social desirability and arrears. Moreover, we hypothesize a negative
correlation between financial skills, age and arrears. The framework is shown in Figure 1
(Van Thiel et al. 2023).
9808

Leveraging Financial Personality for Inclusive Credit Scoring Amidst Global Uncertainty
4.4 The present research
In light of the literature discussed in this paper, our research entails a cross-country study
involving two nations with distinct credit scoring systems. The objective is to assess how the
psychometric constructs we've explored impact the late payment behavior of financially
vulnerable consumers during periods of market instability. In our novel conceptual model, we
postulate that the financial literacy related attributes exert an influence on payment behavior
(the dependent variable) in a manner consistent with existing research.
Utilizing an integrated dataset from our study in these two countries, we have devised and
validated a psychometric credit scoring model that can be applied across the two countries.
This model facilitates responsible credit extension to customer segments facing financial
vulnerability. Our central research question seeks to identify which personality traits are
pertinent in gauging the creditworthiness of vulnerable customers within Western economies.
A visual representation of the conceptual psychometric model can be found in Figure 1.
The choice of research countries, namely the United States and the Netherlands, was
deliberate. We selected them due to their well-regulated credit decision-making processes and
advanced levels of digitalization. Furthermore, the presence of a competitive landscape
encompassing traditional lenders, fintech lenders, and big tech lenders was a pivotal criterion
for our selection.
4.5 Data & Method
4.5.1. Data Collection
Between January 2019 and October 2019, we gathered survey data from a random sample of
low-income applicants (N=897) drawn from Dynata research panels in both the USA (N=694)
and The Netherlands (N=203). Our selection of respondents was focused on two well-
regulated banking markets with a high level of digital adoption. The Dutch study was
conducted during the first quarter of 2019, while the US study was carried out in the third
quarter of 2019. A summary of our sample is provided in Table 2.
Table 2
Research Data Set
Data sources
Country Respondents Arrears Non-Arrears
USA 694 163 531
Netherlands 203 100 103
Total 897 263 634
Our criteria for selecting low-income participants involved an annual income of €25,000 and
$25,000 for individuals residing in the Netherlands and the US, respectively, and being
residents of these countries. We extended invitations to potential respondents via email for
participation in the online research, and upon completion and submission of the questionnaire,
participants were rewarded with €/$30 gift cards. We took precautions to mitigate the
influence of this reward by incorporating a 'social desirability' feature. The respondents, on
8991

Chapter 4
average, had an age of 38 years, with approximately 50% being male, mirroring the market The AdviceRobo team developed a digital psychometric questionnaire, incorporating the
demographics. A comparison with market averages is detailed in Table 3, derived from each specified psychometric attributes and age. This questionnaire consisted of 17 questions
country's central statistics bureaus. Notably, 23% of participants were married, which falls featuring a 5-point Likert scale response or binary format. The survey aimed to collect
below the market average, while 43% were single, representing the market accurately. information regarding participants' financial skills, gratification tendencies, materialism,
However, 43% of participants reported one-person households, indicating an attitudes toward debt, confidence levels, social desirability, and their demographic details.
overrepresentation of such households. Of the total participants, 58% reported having Before starting the study, we tested Cronbach’s á of all the survey questions. Table 4 presents
children, which aligns with the US market but overrepresents the situation in the Netherlands. the psychometric survey questions and their correlations with instances of arrears.
The demographic breakdown of the data is outlined in Table 3.
Table 4
Table 3
Survey questions and correlation with arrears
Respondents (Central Bureau of Statistics, 2019; Pew Research, 2021)
Question Arrears
Sample USA Market Dutch Market I am guided by my immediate desires and do not dwell on what the future may 0.11
Age (average) 38 38.5 42.8 look like.
Sex 52% male / 49% male / 49% male / My convenience is a big factor in the decisions I make or the actions I take. -0.08
48% female 51% female 51% female I don’t think about future problems because I think the future will take care of -0.08
Income (average) $/€ 25.000, - $ 35.977, - € 36.500, - itself.
Married 23% 75% 39% Sometimes I forget to pay my bills on time. 0.02
Single 43% 31% 38% If I have an incidental expense, I have enough savings to cover the expense. 0.07
Household with 58% 56% 33% I admire people who own expensive homes, cars, and clothes. 0.10
children I place much emphasis on the amount of material objects people own as a sign -0.01
Internet penetration 100% 96% 98% of success.
I like to own things that impress people. 0.09
It is easy for me to stick to my aims and accomplish my goals. 0.13
I can stay calm if I have problems because I trust myself that I can handle it 0.01
well.
When I am confronted with a problem, I can usually find several solutions. 0.19
Taking out a loan can be a good thing, if it helps people to enjoy their life. 0.07
For many people, debt is a normal part of life. 0.11
In today’s society, it is almost impossible to live without debts. 0.11
I sometimes feel resentful when I don’t get my way. 0.03
There have been occasions when I felt like smashing things. -0.21
There have been times when I was quite jealous of the good fortune of others. -0.10
9920 91

Leveraging Financial Personality for Inclusive Credit Scoring Amidst Global Uncertainty
The AdviceRobo team developed a digital psychometric questionnaire, incorporating the
specified psychometric attributes and age. This questionnaire consisted of 17 questions
featuring a 5-point Likert scale response or binary format. The survey aimed to collect
information regarding participants' financial skills, gratification tendencies, materialism,
attitudes toward debt, confidence levels, social desirability, and their demographic details.
Before starting the study, we tested Cronbach’s á of all the survey questions. Table 4 presents
the psychometric survey questions and their correlations with instances of arrears.
Table 4
Survey questions and correlation with arrears
Question Arrears
I am guided by my immediate desires and do not dwell on what the future may 0.11
look like.
My convenience is a big factor in the decisions I make or the actions I take. -0.08
I don’t think about future problems because I think the future will take care of -0.08
itself.
Sometimes I forget to pay my bills on time. 0.02
If I have an incidental expense, I have enough savings to cover the expense. 0.07
I admire people who own expensive homes, cars, and clothes. 0.10
I place much emphasis on the amount of material objects people own as a sign -0.01
of success.
I like to own things that impress people. 0.09
It is easy for me to stick to my aims and accomplish my goals. 0.13
I can stay calm if I have problems because I trust myself that I can handle it 0.01
well.
When I am confronted with a problem, I can usually find several solutions. 0.19
Taking out a loan can be a good thing, if it helps people to enjoy their life. 0.07
For many people, debt is a normal part of life. 0.11
In today’s society, it is almost impossible to live without debts. 0.11
I sometimes feel resentful when I don’t get my way. 0.03
There have been occasions when I felt like smashing things. -0.21
There have been times when I was quite jealous of the good fortune of others. -0.10
9913

Chapter 4
To assess the latent constructs of financial skills, gratification, materialism, debt attitudes,
confidence, and social desirability, we employed a five-point Likert scale for each question in
the survey. The responses from the survey were normalized using minmax normalization and
compiled into a dataset denoted as DS = X1, X2, ..., Xn, which encompassed both
demographic information and participants' responses. Table 5 provides statistics pertaining to
the answers.

Table 5

Statistics from the questionnaire responses

| Question            | Mean  | Standard Deviation  |
| ------------------- | ----- | ------------------- |
| Gratification 1     | 2.67  | 1.11                |
| Gratification 2     | 3.30  | 0.95                |
| Gratification 3     | 2.62  | 1.10                |
| Financial skills 2  | 3.87  | 1.25                |
| Financial skills 3  | 3.47  | 1.38                |
|                     | 2.78  | 1.20                |
Materialism 1
| Materialism 2  | 2.25  | 1.01  |
| -------------- | ----- | ----- |
| Materialism 3  | 2.48  | 1.17  |
|                | 3.55  | 0.95  |
Confidence 1
| Confidence 2  | 3.73  | 0.96  |
| ------------- | ----- | ----- |
| Confidence 3  | 3.89  | 0.83  |
|               | 2.85  | 1.11  |
Debt attitude 1
| Debt attitude 2  | 3.68  | 1.00  |
| ---------------- | ----- | ----- |
| Debt attitude 3  | 3.40  | 1.15  |
|                  | 0.52  | 0.50  |
Social desirability 1
| Social desirability 2  | 0.50  | 0.50  |
| ---------------------- | ----- | ----- |
| Social desirability 3  | 0.53  | 0.50  |

4.5.2. Methodology
To examine the association between the newly devised conceptual psychometric model
attributes and payment behavior, respondents were queried about any instances of overdue
payments within the past year for five distinct bill categories: health insurance, mortgage/rent,
energy, water, and phone bills. If respondents reported arrears in at least one of these five
categories within the past year, they were classified as having arrears. Otherwise, they were
categorized as having no arrears. To ensure the accuracy of these classifications, we cross-
validated them with credit bureau data, revealing no discrepancies. In our research, good
payment behavior was defined as having no arrears, while customers exhibiting arrears were
considered to have poor payment behavior.
Additionally, we conducted a principal component analysis with Varimax rotation to evaluate
the questionnaire's structure, which involved merging questions from different sources. This
step aimed to reduce potential multicollinearity among the questions. By applying principal
component analysis and employing a selection criterion of eigenvalues exceeding 1, we
identified components predictive of arrears. The outcome was a comprehensive principal
component model consisting of five components. Subsequently, to formulate an international
personality-centric credit decision-making model for predicting arrears (referred to as the
IPSYCRED model), we conducted logistic regression. To train and validate this model, we
|     | 9942  |     |
| --- | ----- | --- |

Leveraging Financial Personality for Inclusive Credit Scoring Amidst Global Uncertainty
divided the dataset into a training set (70%) and a test set (30%). Our analysis involved
examining whether the model could statistically incorporate the factors as variables,
excluding any coefficients with zero reliability at a 95% confidence level. The result of this
regression analysis yielded a five-factor psychometric credit scoring model. Lenders can
utilize this model in their application processes, particularly for vulnerable and thin-file
customer segments, to differentiate applicants based on their projected payment behavior.

4.6 Results

4.6.1. Principal Component Analysis
To construct a cross-country logistic regression personality-centric model for predicting
payment behavior, we initially evaluated the eigenvalues to determine the appropriate number
of components. Our criterion was selecting components with eigenvalues exceeding one,
resulting in the inclusion of five components in the international model. These components
collectively account for 57% of the variance, a suitable coverage for credit scoring purposes.
Table 6 displays the eigenvalues of the international financial personality model.

Table 6

Eigenvalues and explained variance

|     | Initial Eigenvalues  |     |     | Rotation Sums of Squared  |     |     |     |
| --- | -------------------- | --- | --- | ------------------------- | --- | --- | --- |
Loadings
|            | Total  | % of           | Cumulative  | Total  | % of      | Cumulative  |     |
| ---------- | ------ | -------------- | ----------- | ------ | --------- | ----------- | --- |
| Component  |        | Variance       | %           |        | Variance  | %           |     |
| 1          |        | 3.214  18.907  | 18.907      | 2.290  | 13.468    | 13.468      |     |
| 2          |        | 2.300  13.527  | 32.434      | 2.082  | 12.244    | 25.712      |     |
| 3          |        | 1.623  9.546   | 41.980      | 1.953  | 11.487    | 37.199      |     |
| 4          |        | 1.392  8.188   | 50.168      | 1.774  | 10.435    | 47.634      |     |
| 5          |        | 1.193  7.017   | 57.185      | 1.624  | 9.551     | 57.185      |     |
| 6          |        | 0.915  5.383   | 62.568      |        |           |             |     |
| 7          |        | 0.820  4.823   | 67.392      |        |           |             |     |
| 8          |        | 0.730  4.295   | 71.687      |        |           |             |     |
| 9          |        | 0.706  4.153   | 75.839      |        |           |             |     |
| 10         |        | 0.654  3.847   | 79.687      |        |           |             |     |
| 11         |        | 0.606  3.566   | 83.253      |        |           |             |     |
| 12         |        | 0.582  3.421   | 86.674      |        |           |             |     |
| 13         |        | 0.559  3.291   | 89.965      |        |           |             |     |
| 14         |        | 0.485  2.850   | 92.815      |        |           |             |     |
| 15         |        | 0.433  2.549   | 95.363      |        |           |             |     |
| 16         |        | 0.405  2.384   | 97.748      |        |           |             |     |
| 17         |        | 0.383  2.252   | 100.000     |        |           |             |     |

|     |     |     | 9935  |     |     |     |     |
| --- | --- | --- | ----- | --- | --- | --- | --- |

Chapter 4
Subsequently, we conducted a principal component analysis to assess the data's structure,
reduce potential collinearity, and streamline features. The international principal component
analysis findings are summarized in Table 7.

Table 7

International Principal Component Analysis

Component 1  Component 2  Component 3  Component 4  Component 5
Question
| Gratification 1        |       |       | 0.80  |        |       |
| ---------------------- | ----- | ----- | ----- | ------ | ----- |
| Gratification 2        |       |       | 0.55  |        |       |
| Gratification 3        |       |       | 0.79  |        |       |
| Financial skills 2     | 0.38  |       |       | -0.45  |       |
| Financial skills 3     | 0.59  |       |       |        |       |
| Materialism 1          |       | 0.73  |       |        |       |
| Materialism 2          |       | 0.79  |       |        |       |
| Materialism 3          |       | 0.78  |       |        |       |
| Confidence 1           | 0.73  |       |       |        |       |
| Confidence 2           | 0.74  |       |       |        |       |
| Confidence 3           | 0.76  |       |       |        |       |
| Debt attitude 1        |       |       |       | 0.58   |       |
| Debt attitude 2        |       |       |       | 0.68   |       |
| Debt attitude 3        |       |       |       | 0.72   |       |
| Social desirability 1  |       |       |       |        | 0.70  |
| Social desirability 2  |       |       |       |        | 0.69  |
| Social desirability 3  |       |       |       |        | 0.71  |

The principal component table provided reveals that the first component embodies a fusion of
financial skills and confidence, appropriately labeled "Financial Acumen." This component
illuminates individuals' ability to make sound financial decisions and the degree of confidence
they have in those decisions. The second component is centered on materialism, reflecting the
extent to which respondents value material possessions they aspire to attain, and we refer to
individuals in this materialism segment as "Materialistic Magnates." The third component,
termed "Impulse Control," assesses impulsive buying tendencies and the capacity for self-
control in delaying expenditures. The fourth component, designated as "Financial Vulnerable
Optimists," displays a positive correlation with debt attitudes and a negative association with
financial preparedness for unexpected events. Lastly, the fifth component, known as
"Emotionally Spending Propensity," underscores social desirability, functioning as a measure
of respondents' inclination toward social desirability bias, and serves as a control variable in
our credit scoring model. Table 8 offers an overview of these principal components and their
interpretations.

|     |     | 9964  |     |     |     |
| --- | --- | ----- | --- | --- | --- |

Leveraging Financial Personality for Inclusive Credit Scoring Amidst Global Uncertainty
Table 8

Principal components and their meanings

| Principal Component  |     | Name  |     | Meaning  |     |     |
| -------------------- | --- | ----- | --- | -------- | --- | --- |
Component 1  Financial Accumen  The ability to make financial
decisions that one trusts
| Component 2  |     | Materialism  |     | The desire for material things   |     |     |
| ------------ | --- | ------------ | --- | -------------------------------- | --- | --- |
Component 3  Impulse Control  The level of impulsive buying or
controlled spending
Component 4  Financial Vulnerable  The openness for debt while
|     |     | Optimism  |     | having no buffer  |     |     |
| --- | --- | --------- | --- | ----------------- | --- | --- |
Component 5  Emotional Spending  The level of social desirability
|     |     | Propensity  |     | bias   |     |     |
| --- | --- | ----------- | --- | ------ | --- | --- |

4.6.2. Logistic Regression Decision Modeling
In our pursuit of enhancing credit decision-making for vulnerable and thin-file customer
segments, we trained a predictive logistic regression model. Despite the availability of more
advanced artificial intelligence models, we opted for logistic regression due to compliance
considerations. Western countries impose rigorous regulatory requirements on credit scoring
models, emphasizing their explainability and transparency. Furthermore, we encountered
issues of overfitting when employing more advanced methods.
In this approach, we selected late payments as the dependent variable, a binary variable with
positive and negative classes, enabling lenders to accept or reject applicants. From the five
ordinal explaining components identified in the principal component analysis, we chose to
exclude component 2, "materialism," as it had a p-value greater than 0.5. Utilizing these
components, we partitioned the data into a training set (70%) and a test set (30%) and trained
a logistic regression model using Python Jupyter 6.0.0 notebook. The selection of the cut-off
point for accepting or rejecting prospects was determined through the ROC curve analysis,
with the best fit logit model summarized in Table 9.

Table 9

Logit regression results
| Logit Regression Results  |     |          |                  |     |            |     |
| ------------------------- | --- | -------- | ---------------- | --- | ---------- | --- |
| Dependent variable        |     | Arrears  | No observations  |     | 627        |     |
| Model                     |     | Logit    | Df residuals     |     | 621        |     |
| Method                    |     | MLE      | Df model         |     | 5          |     |
| Pseudo R-square           |     | 0.1746   | Log likelihood   |     | -310.28    |     |
| LL-null                   |     | -375.90  | LLR-p-value      |     | 1.296e-26  |     |
Component  Coefficient  Std error  z  P > |z|  [0,025  0.975]
| Intercept  | -0.7851  | 0.319  | -2.459  | 0.014  | -1.411  | -0.159  |
| ---------- | -------- | ------ | ------- | ------ | ------- | ------- |
| PC1        | -0.7577  | 0.111  | -6.844  | 0.000  | -0.975  | -0.541  |
| PC4        | 0.7233   | 0.113  | 6.427   | 0.000  | 0.503   | 0.944   |
| PC3        | 0.5031   | 0.103  | 4.869   | 0.000  | 0.301   | 0.706   |
| PC5        | -0.2816  | 0.100  | -2.811  | 0.005  | -0.478  | -0.085  |
| Age        | -0.0087  | 0.007  | -1.252  | 0.211  | -0.022  | 0.005   |

|     |     |     | 9957  |     |     |     |
| --- | --- | --- | ----- | --- | --- | --- |

Chapter 4
The resulting international psychometric model can be represented as:
Log (arrears) = -0.79 - (0.76 * Financial Accumen) + (0.72 *Financial Vulnerable Optimism)
+ (0.50 * Impulse Control) - (0.28 * Emotional Spending Propensity) - (0.01 * Age)
It's important to acknowledge that the moderate R-squared value and the near parity between
the intercept’s beta and some other betas may be attributed to the skewed dataset with a
limited number of arrears.
Nonetheless, we expect that this model will provide value to credit scoring, given that the
individual predictor variables in the model demonstrate statistical significance. One of the
model's objectives, as we recall, was to distinguish various attributes for personality-centric
credit scoring. Furthermore, the attributes associated with the novel personality factors align
with theoretical knowledge derived from prior research as discussed in the introduction.
To further assess the model's ability to predict arrears, we examined model metrics on the test
set (N = 270). Specifically, we analyzed the area under the curve (AUC) and Gini score,
widely recognized accuracy metrics as introduced in this paper. The decision model yielded
an AUC of 0.78 and a Gini score of 0.56, which is reasonably strong considering that the
model predicts late payments solely based on personality traits. The ROC curve is depicted in
Figure 2.
To delve deeper into the model's accuracy on the test set, we examined the confusion matrix
and derived statistics, as presented in Table 10.
9986

Leveraging Financial Personality for Inclusive Credit Scoring Amidst Global Uncertainty
Table 10

Observed and predicted frequencies for late payment by logistic regression
| Observed     | Predicted    | Predicted  | % Correct  |
| ------------ | ------------ | ---------- | ---------- |
|              | Non arrears  | Arrears    |            |
| Non arrears  | 135          | 52         | 72.2%      |
| Arrears      | 27           | 56         | 67.5%      |
| Overall      |              |            | 70.7%      |
|              | 9979         |            |            |

Chapter 4
The validation of the model's predictive power demonstrates its ability to correctly predict
70.7% of instances. For lenders, the accurate prediction of which customers to accept holds
significant importance for business models and pricing strategies. The model precisely
predicts 72.2% of good-paying customers and 67.5% of actual arrears. Notably, for lenders,
the correct prediction of arrears carries substantial implications, as late-paying customers
incur significant costs. The model's precision in predicting arrears was 0.52, while its
precision in predicting good customers stood at 0.83, indicating superior performance in
identifying good customers.
Furthermore, the model exhibited a recall of 0.675, signifying that it accurately predicted
67.5% of all arrears. When focusing on the prediction of good customers, the recall was 0.72.
While the model demonstrates a slight advantage in predicting good customers, it
unquestionably enhances credit scoring, particularly in cases where financial data on
applicants is limited or nonexistent.
In conclusion, our findings affirm our core hypothesis that financial personality-centric credit
scoring enhances financial access for vulnerable consumer segments in both the USA and
The Netherlands, especially under unstable market conditions.
4.7 Discussion
The objective of this study was to explore the hypothesis that financial personality-centric
credit scoring could improve financial access for vulnerable consumer segments in the USA
and the Netherlands, especially relevant during times of market instability. This research fills
a critical gap by emphasizing the significance of financial personality factors in shaping
payment behavior when traditional financial data is scarce or outdated, as exemplified during
crises like COVID-19 or high inflationary market contexts. Our findings corroborate the core
hypothesis and align with previous studies by Klinger et al. (2013) and Hurley and Adebayo
(2016), emphasizing the relevance of personality traits also in promoting financial inclusion
of small businesses.
While prior research has focused on the impact of individual psychometric attributes on
financial behavior, this study represents a pioneering effort in merging psychometric and
behavioral economic attributes in the development of a comprehensive novel personality-
centric logistic regression model for credit scoring. Furthermore, our research uncovered new
psychometric components such as "financial accumen" and "financial vulnerable optimism."
Despite these novel findings, our results remain consistent with Lussardi & Mitchell’s (2011)
assertion that financial knowledge plays a substantial role in financial inclusion, as
hypothesized in our conceptual model. Nonetheless, our study opted for the use of financial
skills instead of financial knowledge in predicting payment behavior, drawing upon Dew and
Xiao's (2011) findings that financial skills are linked to increased savings and reduced debt.
Notably, our research has shed light on the relationship between financial skills and
confidence. While prior studies like Seaward and Kemp (2000) and Nosić and Weber (2010)
highlighted the connection between overestimating future earnings and accumulating debt or
engaging in high-risk behavior, our findings underscore the pivotal role of financial skills in
predicting payment behavior. Individuals with moderate or low financial skills combined with
overconfidence are more likely to exhibit delinquent payment behavior, a crucial component
with the most substantial impact in our logistic regression analysis (β- coefficient of 0.76).
Our study also aligns with earlier research by Davies and Lea (1995), Norvilitis et al. (2006),
and Haultain et al. (2010), which observed a positive link between positive debt attitudes and
10908

Leveraging Financial Personality for Inclusive Credit Scoring Amidst Global Uncertainty
The validation of the model's predictive power demonstrates its ability to correctly predict higher debt levels. Nevertheless, we identified a negative correlation between debt attitudes
70.7% of instances. For lenders, the accurate prediction of which customers to accept holds and the absence of savings when forecasting late payments. The interplay between various
significant importance for business models and pricing strategies. The model precisely components within a comprehensive personality model, a unique aspect in behavioral
predicts 72.2% of good-paying customers and 67.5% of actual arrears. Notably, for lenders, financial research, significantly contributes to the prediction of payment behavior. This
the correct prediction of arrears carries substantial implications, as late-paying customers component, which we call ‘financial vulnerable optimism’ has a β-coefficient of 0.72 and
incur significant costs. The model's precision in predicting arrears was 0.52, while its therefore stands as the second most influential factor. These findings pave the way for
precision in predicting good customers stood at 0.83, indicating superior performance in constructing financial personality profiles to distinguish between good and bad payers when
identifying good customers. extending loans, thus enhancing credit decision-making.
Additionally, we introduced social desirability as a control factor in our model, uncovering a
Furthermore, the model exhibited a recall of 0.675, signifying that it accurately predicted relationship between the level of social desirability and expected payment behavior (β-
67.5% of all arrears. When focusing on the prediction of good customers, the recall was 0.72. coefficient of 0.28). Our study is among the first to establish a predictive association between
While the model demonstrates a slight advantage in predicting good customers, it social desirability and payment behavior. Furthermore, we found that age had a minimal
unquestionably enhances credit scoring, particularly in cases where financial data on impact (β-coefficient of -0.01) on late payments. The logistic regression model achieved an
applicants is limited or nonexistent. accuracy rate of 70.7% and a Gini coefficient of 0.56. It demonstrates a slightly superior
In conclusion, our findings affirm our core hypothesis that financial personality-centric credit ability to predict good payment behavior, underscoring its potential significance in credit
scoring enhances financial access for vulnerable consumer segments in both the USA and scoring for vulnerable and thin-file customer segments in Western credit markets.
The Netherlands, especially under unstable market conditions. Consequently, the model's predictive power substantiates financial inclusion efforts and
mitigates information asymmetry.
4.7 Discussion
The objective of this study was to explore the hypothesis that financial personality-centric Our research has also demonstrated that the credit score model can be applied across different
credit scoring could improve financial access for vulnerable consumer segments in the USA countries and credit rating systems. In addition to discussing the aggregated model, we also
and the Netherlands, especially relevant during times of market instability. This research fills developed geographically-specific models that closely align with it. Traditional credit
a critical gap by emphasizing the significance of financial personality factors in shaping decision-making approaches have been historically localized and costly. The internationally
payment behavior when traditional financial data is scarce or outdated, as exemplified during scalable credit decision model we propose can aid multinational lenders in improving
crises like COVID-19 or high inflationary market contexts. Our findings corroborate the core cost/income ratios by reducing overhead costs and accelerating the digitization of credit
hypothesis and align with previous studies by Klinger et al. (2013) and Hurley and Adebayo assessment. We encourage the incorporation of real-time financial personality data from
(2016), emphasizing the relevance of personality traits also in promoting financial inclusion various sources such as open banking transactions, mobile phones, search engines, and social
of small businesses. media to further enrich lenders' understanding of new customers' psychometric profiles.
While prior research has focused on the impact of individual psychometric attributes on Additionally, we emphasize the importance of respecting privacy regulations when utilizing
financial behavior, this study represents a pioneering effort in merging psychometric and personal behavioral data for customer qualification and risk mitigation strategies. In a post-
behavioral economic attributes in the development of a comprehensive novel personality- COVID digital era, the number of vulnerable customers is anticipated to increase due to
centric logistic regression model for credit scoring. Furthermore, our research uncovered new deteriorating economic and environmental circumstances. Even individuals previously
psychometric components such as "financial accumen" and "financial vulnerable optimism." considered financially stable can become vulnerable suddenly, whether due to crises,
divorces, or physical disabilities. The recovery process is particularly challenging for those
Despite these novel findings, our results remain consistent with Lussardi & Mitchell’s (2011) already in vulnerable situations, leading to a rise in the overall number of vulnerable
assertion that financial knowledge plays a substantial role in financial inclusion, as consumers. Hence, we contend that adopting novel credit decision-making approaches must
hypothesized in our conceptual model. Nonetheless, our study opted for the use of financial align with customer protection regulations. In Western jurisdictions, contemporary regulators
skills instead of financial knowledge in predicting payment behavior, drawing upon Dew and have instituted regulatory frameworks, like sandboxes, to assess innovative credit decisioning
Xiao's (2011) findings that financial skills are linked to increased savings and reduced debt. solutions tailored for these customer segments while ensuring adherence to regulatory and
privacy standards. Our argument posits that these sandboxes should be employed as a
Notably, our research has shed light on the relationship between financial skills and preliminary step before introducing new solutions to the market, in order to evaluate their
confidence. While prior studies like Seaward and Kemp (2000) and Nosić and Weber (2010) ethical and equitable qualities. Regulators are progressively embracing such initiatives aimed
highlighted the connection between overestimating future earnings and accumulating debt or at mitigating vulnerability and curbing financial risks.
engaging in high-risk behavior, our findings underscore the pivotal role of financial skills in
predicting payment behavior. Individuals with moderate or low financial skills combined with We encourage (neo) banks, credit card companies, insurers, utility providers, and telecom
overconfidence are more likely to exhibit delinquent payment behavior, a crucial component companies to explore and implement personality data in their customer profiling, risk &
with the most substantial impact in our logistic regression analysis (β- coefficient of 0.76). marketing models. By doing so, they can deepen their understanding of customers, enhance
Our study also aligns with earlier research by Davies and Lea (1995), Norvilitis et al. (2006), their risk assessment and responsibly support these customer segments. We believe that these
and Haultain et al. (2010), which observed a positive link between positive debt attitudes and personality data are valuable for developing tailored solutions that promote financial well-
98 19091

Chapter 4
being across a wide range of customer segments. Moreover, we also encourage the
application of individual personality profiles to develop predictive personalization strategies
that mitigate late payment risks, enhance customer engagement, and deliver added customer
value. Additionally, we call upon regulators to consider incorporating financial personality
data into their consumer protection strategies, which can help prevent anomalies such as
students using loans to invest in stocks due to overconfidence or financial vulnerable
optimists with limited impulse control obtaining loans or mortgages through self-service
digital channels while maintaining a high level of financial vulnerability.
In conclusion, our research suggests that personality-centric credit models can be successfully
adapted across Western countries with varying credit scoring systems. Our findings indicate
that the financial personality construct is a reliable predictor of payment behavior among
vulnerable consumers. This is particularly pertinent in today's volatile market conditions.
Confidence-driven financial skills emerge as the strongest predictor of positive payment
behavior. Furthermore, the ability to delay gratification and negative debt attitudes predict
good payment behavior. These findings hold consistent reliability across different countries.
These key findings highlight the potential of financial personality profiling to responsibly
facilitate access to finance for vulnerable customers in Western markets. We conclude by
emphasizing that psychometric models can very well serve as supplementary models,
complementing traditional and alternative data sources while adhering to customer privacy
regulations. To the best of our knowledge, this study represents the first comprehensive
examination of psychometric personality profiles as predictors of payment risks among
vulnerable customer segments in highly regulated Western credit markets.
4.8 Conclusion
In a world increasingly affected by crises and high inflation rates, it is crucial to prioritize
responsible financial inclusion for those impacted. Traditional credit assessment methods that
rely on financial data often prove inadequate or unreliable in such situations. Moreover,
specific vulnerable groups in Western societies, including migrants, young individuals,
divorced individuals, those with illnesses, fixed-income seniors, start-up entrepreneurs, and
sole traders, encounter difficulties in accessing financial assistance even outside of crisis
situations.
This research underscores the significance of considering an individual's personality as an
alternative approach when conventional credit scoring methods prove insufficient in unstable
market conditions. Through an analysis of a representative sample of low-income individuals
in the US and the Netherlands, our regression model identifies various factors contributing to
late payment behavior, including financial acumen, confidence level, financial vulnerability
optimism, impulse control, emotional spending propensity, and age.
By leveraging this insight, (neo)banks can actively promote responsible financial inclusion
for vulnerable customers. Thus, when applicant data is limited, unreliable, or entirely absent,
personality data assessing an applicant's financial personality can be utilized to make well-
informed lending decisions. This approach enables lenders of all types to support individuals
lacking conventional credit history or facing exceptional circumstances, facilitating their
access to essential financial resources. Incorporating psychometric data into their evaluation
processes, financial institutions can contribute to a more inclusive and resilient financial
landscape.
110020

Leveraging Financial Personality for Inclusive Credit Scoring Amidst Global Uncertainty
being across a wide range of customer segments. Moreover, we also encourage the
application of individual personality profiles to develop predictive personalization strategies
that mitigate late payment risks, enhance customer engagement, and deliver added customer 4.9 Limitations and Future Research Directions
value. Additionally, we call upon regulators to consider incorporating financial personality This study exhibits several limitations that warrant consideration. Firstly, it is imperative to
data into their consumer protection strategies, which can help prevent anomalies such as acknowledge that the data collection was confined to two Western nations, thereby limiting
students using loans to invest in stocks due to overconfidence or financial vulnerable the scope of generalizability. To extend the applicability of our findings, future research
optimists with limited impulse control obtaining loans or mortgages through self-service should encompass a broader geographic spectrum, including developing countries. Such an
digital channels while maintaining a high level of financial vulnerability. approach could unveil opportunities for enhanced financial inclusion among vulnerable
populations in these regions.
In conclusion, our research suggests that personality-centric credit models can be successfully Secondly, our investigation relied upon self-reported arrear information, cross-validated with
adapted across Western countries with varying credit scoring systems. Our findings indicate credit bureau data spanning various product categories. To refine the precision and efficacy of
that the financial personality construct is a reliable predictor of payment behavior among predictive models, forthcoming studies should strive to acquire genuine behavioral data
vulnerable consumers. This is particularly pertinent in today's volatile market conditions. pertaining to diverse segments of vulnerable consumers.
Confidence-driven financial skills emerge as the strongest predictor of positive payment Thirdly, the temporal dimension of our study introduces potential bias, given that data
behavior. Furthermore, the ability to delay gratification and negative debt attitudes predict collection occurred prior to the onset of the COVID-19 pandemic in 2019. While
good payment behavior. These findings hold consistent reliability across different countries. psychometric traits are known for their stability over time, it is imperative to conduct
These key findings highlight the potential of financial personality profiling to responsibly supplementary research under post-pandemic market conditions to ascertain the persistence
facilitate access to finance for vulnerable customers in Western markets. We conclude by of observed trends.
emphasizing that psychometric models can very well serve as supplementary models,
complementing traditional and alternative data sources while adhering to customer privacy Another limitation relates to the use of ordinal data for the purpose of rendering results
regulations. To the best of our knowledge, this study represents the first comprehensive comparable across models. Although Likert scales were employed to assess participants'
examination of psychometric personality profiles as predictors of payment risks among financial skills, materialism, debt attitude, confidence, gratification, and social desirability,
vulnerable customer segments in highly regulated Western credit markets. these scales may inadvertently oversimplify individuals' nuanced psychological perceptions.
Recognizing that human experiences often defy rigid categorization, future research
4.8 Conclusion endeavors should explore alternative digital data sources, such as open banking transaction
In a world increasingly affected by crises and high inflation rates, it is crucial to prioritize records, social media data, mobile phone data, biometric data, and search behavior data. The
responsible financial inclusion for those impacted. Traditional credit assessment methods that integration of these sources into personality-centric models has the potential to transform
rely on financial data often prove inadequate or unreliable in such situations. Moreover, them into real-time predictive models, enabling deeper and more dynamic profiling. This, in
specific vulnerable groups in Western societies, including migrants, young individuals, turn, would not only augment credit scoring accuracy but also facilitate improved customer
divorced individuals, those with illnesses, fixed-income seniors, start-up entrepreneurs, and management, thereby promoting financial well-being.
sole traders, encounter difficulties in accessing financial assistance even outside of crisis
situations. In summary, while this study contributes valuable insights, it is essential to recognize its
limitations and to pursue future research avenues that address these constraints, thereby
This research underscores the significance of considering an individual's personality as an advancing the field of personality-centric credit scoring.
alternative approach when conventional credit scoring methods prove insufficient in unstable
market conditions. Through an analysis of a representative sample of low-income individuals
in the US and the Netherlands, our regression model identifies various factors contributing to
late payment behavior, including financial acumen, confidence level, financial vulnerability
optimism, impulse control, emotional spending propensity, and age.
By leveraging this insight, (neo)banks can actively promote responsible financial inclusion
for vulnerable customers. Thus, when applicant data is limited, unreliable, or entirely absent,
personality data assessing an applicant's financial personality can be utilized to make well-
informed lending decisions. This approach enables lenders of all types to support individuals
lacking conventional credit history or facing exceptional circumstances, facilitating their
access to essential financial resources. Incorporating psychometric data into their evaluation
processes, financial institutions can contribute to a more inclusive and resilient financial
landscape.
100 110013

Chapter 4
REFERENCES
Achtziger, A., Hubert, M., Kenning, P., Raab, G., & Reisch, L. (2015). Debt out of control:
The links between self-control, compulsive buying, and real debts. Journal of Economic
Psychology, 49, 141–149. https://doi.org/10.1016/j.joep.2015.04.003
Almenberg, J., Lusardi, A., Säve‐Söderbergh, J., & Vestman, R. (2020). Attitudes toward debt
and debt behavior. The Scandinavian Journal of
Economics. https://doi.org/10.1111/sjoe.12419
APG. (2023). Are Dutch people more financially vulnerable than they used to
be? https://apg.nl/en/publication/are-dutch-people-more-financially-vulnerable-than-they-
used-to-be/
Bankowska, K., Ferrando, A., & Garcia, A. (2020). The COVID-19 pandemic and access to
finance for small and medium-sized enterprises: Evidence from survey data. ECB Economic
Bulletin, 4.
Becerra, X. (2018). California Consumer Privacy Act
(CCPA). https://oag.ca.gov/privacy/ccpa
Belk, R. W. (1985). Materialism: Trait aspects of living in the material world. Journal of
Consumer Research, 12(3), 265–280. https://doi.org/10.1086/208515
Bernardin, H. J., & Cooke, D. K. (1993). Validity of an honesty test in predicting theft among
convenience store employees. Academy of Management Journal, 36(5), 1097–1108.
Bernheim, D. (1998). Financial illiteracy, education, and retirement saving. Living with
Defined Contribution Pensions, 3868.
Bourova, E., Ramsay, I., & Ali, P. (2019). The experience of financial hardship in Australia:
Causes, impacts, and coping strategies. Journal of Consumer Policy, 42, 189-221.
CMA. (2019). Consumer vulnerability challenges and potential
solutions. https://www.gov.uk/government/publications/consumer-vulnerability-challenges-
and-potential-solutions
Coppack, M., Raza, Y., Sarkar, S., & Scribbins, K. (2015). Consumer vulnerability. FCA
Occasional Papers in Financial Regulation, 8.
Costa Jr., P. T., & McCrae, R. R. (1992). Four ways five factors are basic. Personality and
Individual Differences, 13(6), 653–665. https://doi.org/10.1016/0191-8869(92)90236-I
Davies, E., & Lea, S. E. (1995). Student attitudes to student debt. Journal of Economic
Psychology, 16(4), 663-679.
Dew, J., & Xiao, J. J. (2011). The financial management behavior scale: Development and
validation. Journal of Financial Counseling and Planning, 22(1), 43.
110042

Leveraging Financial Personality for Inclusive Credit Scoring Amidst Global Uncertainty
Elliott, K., Coopamootoo, K., Curran, E., Ezhilchelvan, P., Finnigan, S., Horsfall, D., & van
Moorsel, A. (2022). Know Your Customer: Balancing innovation and regulation for financial
inclusion. Data & Policy, 4, e34.
European Union. (2016). The General Data Protection Regulation (GDPR), the Data
Protection Law Enforcement Directive, and other rules concerning the protection of personal
data. https://ec.europa.eu/info/law/law-topic/data-protection/data-protection-eu_nl
Financial Conduct Authority UK. (2019). Guidance on consumer
vulnerability. https://www.fca.org.uk/publication/guidance-consultation/gc19-03.pdf
Financial Conduct Authority UK. (2021a). Financial lives 2020 survey: The impact of
coronavirus. Available athttps://www.fca.org.uk/publication/research/financial-lives-survey-
2020.pdf
Garðarsdóttir, R. B., & Dittmar, H. (2012). The relationship of materialism to debt and
financial well-being: The case of Iceland’s perceived prosperity. Journal of Economic
Psychology, 33(3), 471–481. https://doi.org/10.1016/j.joep.2010.01.003
Garz, S., Giné, X., Karlan, D., Mazer, R., Sanford, C., & Zinman, J. (2021). Consumer
protection for financial inclusion in low- and middle-income countries: Bridging regulator
and academic perspectives. Annual Review of Financial Economics, 13, 219-246.
Hand, D. J., & Henley, W. E. (1997). Statistical classification methods in consumer credit
scoring: A review. Journal of the Royal Statistical Society: Series A (Statistics in Society),
160(3), 523–541.
Haultain, S., Kemp, S., & Chernyshenko, O. S. (2010). The structure of attitudes to student
debt. Journal of Economic Psychology, 31(3), 322-
330. https://doi.org/10.1016/j.joep.2010.01.003
Hurley, M., & Adebayo, J. (2016). Credit scoring in the era of big data. Yale Journal of Law
and Technology, 18, 148.
Klapper, L., Lusardi, A., & Panos, G. A. (2013). Financial literacy and its consequences:
Evidence from Russia during the financial crisis. Journal of Banking & Finance, 37(10),
3904–3923. https://doi.org/10.1016/j.jbankfin.2013.07.014
Klinger, B., Khwaja, A., & LaMonte, J. (2013). Improving credit risk analysis with
psychometrics in Peru. Inter-American Development Bank. Technical Note.
Liu, X., Wang, T., Ding, W., Liu, Y., & Xu, Q. (2017). A Credit Scoring Model Based on
Alternative Mobile Data for Financial Inclusion. In Proceedings of the 2017 Credit Scoring
and Credit Control Conference, Edinburgh, UK (Vol.
30). https://doi.org/10.1016/j.asoc.2018.10.004
Lusardi, A., & Mitchell, O. S. (2007). Financial literacy and retirement planning: New
evidence from the Rand American Life Panel. Michigan Retirement Research Center
Research Paper No. WP, 157.
110035

Chapter 4
Lusardi, A., & Mitchell, O. S. (2008). Planning and financial literacy: How do women and blue‐collar workers. Journal of Occupational and Organizational Psychology, 81(3),
fare? American Economic Review, 98(2), 413–417. 481-502.
Lusardi, A., & Mitchell, O. S. (2011). Financial Literacy and Planning: Implications for Remund, D. L. (2010). Financial literacy explicated: The case for a clearer definition in an
Retirement Wellbeing (No. w17078). National Bureau of Economic Research. increasingly complex economy. Journal of Consumer Affairs, 44(2), 276–295.
https://doi.org/10.1111/j.1745-6606.2010.01169.x
Lusardi, A., & Tufano, P. (2009). Teach workers about the perils of debt.
Řezáč, M., & Řezáč, F. (2011). How to measure the quality of credit scoring models. Finance
Mogaji, E., Soetan, T. O., & Kieu, T. A. (2020). The implications of artificial intelligence on a úvěr: Czech Journal of Economics and Finance, 61(5), 486-
the digital marketing of financial services to vulnerable customers. Australasian Marketing
Journal. https://doi.org/10.1016/j.ausmj.2020.05.003 Rishabh, K. (2022). Can open banking substitute credit bureaus. Working Paper.
Moore, D. A., & Healy, P. J. (2008). The trouble with overconfidence. Psychological Review, Ruhnka, J. C., & Young, J. E. (1991). Some hypotheses about risk in venture capital
115(2), 502. investing. Journal of Business Venturing, 6(2), 115–133. https://doi.org/10.1016/0883-
9026(91)90014-5
Moore, D. L. (2003). Survey of financial literacy in Washington State: Knowledge, behavior,
attitudes, and experiences. Washington State Department of Financial Institutions. Salampasis, D., & Mention, A. L. (2018). FinTech: Harnessing innovation for financial
inclusion. In Handbook of Blockchain, Digital Finance, and Inclusion, Volume 2 (pp. 451–
Nederhof, A. J. (1985). Methods of coping with social desirability bias: A review. European 461). Academic Press.
Journal of Social Psychology, 15(3), 263–270. https://doi.org/10.1002/ejsp.2420150303
San Pedro, J., Proserpio, D., & Oliver, N. (2015, June). MobiScore: towards universal credit
Norvilitis, J. M., Merwin, M. M., Osberg, T. M., Roehling, P. V., Young, P., & Kamas, M. M. scoring from mobile phone data. In international conference on user modeling, adaptation,
(2006). Personality factors, money attitudes, financial knowledge, and credit-card debt in and personalization (pp. 195–207). Springer, Cham.
college students. Journal of Applied Social Psychology, 36(6), 1395–
1413. https://doi.org/10.1111/j.0021-9029.2006.00065.x Seaward, H. G., & Kemp, S. (2000). Optimism bias and student debt. New Zealand Journal
of Psychology, 29(1), 17.
Nosić, A., & Weber, M. (2010). How riskily do I invest? The role of risk attitudes, risk
perceptions, and overconfidence. Decision Analysis, 7(3), 282– Semega, J. (2020, September 15). Income and poverty in the United States: 2019. US Census
301. https://doi.org/10.1287/deca.1100.0178 Bureau. https://www.census.gov/library/publications/2020.
O'Connor, G. E., Newmeyer, C. E., Wong, N. Y. C., Bayuk, J. B., Cook, L. A., Komarova, Y., Shema, A. (2019, January). Effective credit scoring using limited mobile phone data. In
& Warmath, D. (2019). Conceptualizing the multiple dimensions of consumer financial Proceedings of the Tenth International Conference on Information and Communication
vulnerability. Journal of Business Research, 100, 421–430. https://doi.org/10. Technologies and Development (pp. 1–11).
Olsson, H. (2014). Measuring overconfidence: Methodological problems and statistical Spearman, C. (1946). Theory of general factor. British Journal of Psychology,
artifacts. Journal of Business Research, 67(8), 1766–1770.
https://doi.org/10.1016/j.jbusres.2014.03.002 Strömbäck, C., Lind, T., Skagerlund, K., Västfjäll, D., & Tinghög, G. (2017). Does self-
control predict financial behavior and financial well-being? Journal of Behavioral and
Óskarsdóttir, M., Bravo, C., Sarraute, C., Vanthienen, J., & Baesens, B. (2019). The value of Experimental Finance, 14, 30–38. https://doi.org/10.1016/j.jbef.2017.04.002
big data for credit scoring: Enhancing financial inclusion using
Tan, T., & Phan, T. Q. (2018). Social Media-Driven Credit Scoring: The Predictive Value of
Parke, A., Griffiths, M., & Irwing, P. (2004). Personality traits in pathological gambling: Social Structures. Available at SSRN 3217885.
Sensation seeking, deferment of gratification and competitiveness as risk factors. Addiction
Research & Theory, 12(3), 201–212. https://doi.org/10.1080/1606635310001634500 Wei, Y., Yildirim, P., Van den Bulte, C., & Dellarocas, C. (2016). Credit scoring with social
network data. Marketing Science, 35(2), 234–258.
PBS (2022). https://www.pbs.org/newshour/politics/democrats-face-midterm-hit-as-more-
americans-feel-financially-vulnerable-poll-says Worldbank. (2018, April 19). Financial inclusion on the rise, but gaps remain, global
FINDEX database shows. https://www.worldbank.org/en/news/press- release/
Poppleton, S., Briner, R. B., & Kiefer, T. (2008). The roles of context and everyday
experience in understanding work‐non‐work relationships: A qualitative diary study of white‐
110064 105

Leveraging Financial Personality for Inclusive Credit Scoring Amidst Global Uncertainty
Lusardi, A., & Mitchell, O. S. (2008). Planning and financial literacy: How do women and blue‐collar workers. Journal of Occupational and Organizational Psychology, 81(3),
fare? American Economic Review, 98(2), 413–417. 481-502.
Lusardi, A., & Mitchell, O. S. (2011). Financial Literacy and Planning: Implications for Remund, D. L. (2010). Financial literacy explicated: The case for a clearer definition in an
Retirement Wellbeing (No. w17078). National Bureau of Economic Research. increasingly complex economy. Journal of Consumer Affairs, 44(2), 276–295.
https://doi.org/10.1111/j.1745-6606.2010.01169.x
Lusardi, A., & Tufano, P. (2009). Teach workers about the perils of debt.
Řezáč, M., & Řezáč, F. (2011). How to measure the quality of credit scoring models. Finance
Mogaji, E., Soetan, T. O., & Kieu, T. A. (2020). The implications of artificial intelligence on a úvěr: Czech Journal of Economics and Finance, 61(5), 486-
the digital marketing of financial services to vulnerable customers. Australasian Marketing
Journal. https://doi.org/10.1016/j.ausmj.2020.05.003 Rishabh, K. (2022). Can open banking substitute credit bureaus. Working Paper.
Moore, D. A., & Healy, P. J. (2008). The trouble with overconfidence. Psychological Review, Ruhnka, J. C., & Young, J. E. (1991). Some hypotheses about risk in venture capital
115(2), 502. investing. Journal of Business Venturing, 6(2), 115–133. https://doi.org/10.1016/0883-
9026(91)90014-5
Moore, D. L. (2003). Survey of financial literacy in Washington State: Knowledge, behavior,
attitudes, and experiences. Washington State Department of Financial Institutions. Salampasis, D., & Mention, A. L. (2018). FinTech: Harnessing innovation for financial
inclusion. In Handbook of Blockchain, Digital Finance, and Inclusion, Volume 2 (pp. 451–
Nederhof, A. J. (1985). Methods of coping with social desirability bias: A review. European 461). Academic Press.
Journal of Social Psychology, 15(3), 263–270. https://doi.org/10.1002/ejsp.2420150303
San Pedro, J., Proserpio, D., & Oliver, N. (2015, June). MobiScore: towards universal credit
Norvilitis, J. M., Merwin, M. M., Osberg, T. M., Roehling, P. V., Young, P., & Kamas, M. M. scoring from mobile phone data. In international conference on user modeling, adaptation,
(2006). Personality factors, money attitudes, financial knowledge, and credit-card debt in and personalization (pp. 195–207). Springer, Cham.
college students. Journal of Applied Social Psychology, 36(6), 1395–
1413. https://doi.org/10.1111/j.0021-9029.2006.00065.x Seaward, H. G., & Kemp, S. (2000). Optimism bias and student debt. New Zealand Journal
of Psychology, 29(1), 17.
Nosić, A., & Weber, M. (2010). How riskily do I invest? The role of risk attitudes, risk
perceptions, and overconfidence. Decision Analysis, 7(3), 282– Semega, J. (2020, September 15). Income and poverty in the United States: 2019. US Census
301. https://doi.org/10.1287/deca.1100.0178 Bureau. https://www.census.gov/library/publications/2020.
O'Connor, G. E., Newmeyer, C. E., Wong, N. Y. C., Bayuk, J. B., Cook, L. A., Komarova, Y., Shema, A. (2019, January). Effective credit scoring using limited mobile phone data. In
& Warmath, D. (2019). Conceptualizing the multiple dimensions of consumer financial Proceedings of the Tenth International Conference on Information and Communication
vulnerability. Journal of Business Research, 100, 421–430. https://doi.org/10. Technologies and Development (pp. 1–11).
Olsson, H. (2014). Measuring overconfidence: Methodological problems and statistical Spearman, C. (1946). Theory of general factor. British Journal of Psychology,
artifacts. Journal of Business Research, 67(8), 1766–1770.
https://doi.org/10.1016/j.jbusres.2014.03.002 Strömbäck, C., Lind, T., Skagerlund, K., Västfjäll, D., & Tinghög, G. (2017). Does self-
control predict financial behavior and financial well-being? Journal of Behavioral and
Óskarsdóttir, M., Bravo, C., Sarraute, C., Vanthienen, J., & Baesens, B. (2019). The value of Experimental Finance, 14, 30–38. https://doi.org/10.1016/j.jbef.2017.04.002
big data for credit scoring: Enhancing financial inclusion using
Tan, T., & Phan, T. Q. (2018). Social Media-Driven Credit Scoring: The Predictive Value of
Parke, A., Griffiths, M., & Irwing, P. (2004). Personality traits in pathological gambling: Social Structures. Available at SSRN 3217885.
Sensation seeking, deferment of gratification and competitiveness as risk factors. Addiction
Research & Theory, 12(3), 201–212. https://doi.org/10.1080/1606635310001634500 Wei, Y., Yildirim, P., Van den Bulte, C., & Dellarocas, C. (2016). Credit scoring with social
network data. Marketing Science, 35(2), 234–258.
PBS (2022). https://www.pbs.org/newshour/politics/democrats-face-midterm-hit-as-more-
americans-feel-financially-vulnerable-poll-says Worldbank. (2018, April 19). Financial inclusion on the rise, but gaps remain, global
FINDEX database shows. https://www.worldbank.org/en/news/press- release/
Poppleton, S., Briner, R. B., & Kiefer, T. (2008). The roles of context and everyday
experience in understanding work‐non‐work relationships: A qualitative diary study of white‐
104 110057

Chapter 4
Yang, S., Markoczy, L., & Qi, M. (2007). Unrealistic optimism in consumer credit card
adoption. Journal of Economic Psychology, 28(2), 170–185.
|     |     |     |     |
| --- | --- | --- | --- |
Yuan, H., Lau, R. Y., Xu, W., Pan, Z., & Wong, M. C. (2018). Mining Individuals' Behavior
Patterns from Social Media for Enhancing Online Credit Scoring. In PACIS (p. 163).
|     |     |     |     |
| --- | --- | --- | --- |
Yurdakul, D., Atik, D., & Dholakia, N. (2017). Redefining the bottom of the pyramid from a
| marketing perspective. Marketing Theory, 17(3), 289–303.   |     |     |     |
| ---------------------------------------------------------- | --- | --- | --- |
|                                                            |     |     |     |
Zhang, Y., Jia, H., Diao, Y., Hai, M., & Li, H. (2016). Research on credit scoring by fusing
social media information in online peer-to-peer lending. Procedia Computer Science, 91,
168–174.   Having established the benefits of personality-driven credit assessment, we now consider the

  accuracy and predictiveness potential of AI in credit risk prediction. This chapter delves

    into how AI can support more precise and equitable credit evaluations to improve
credit scoring approaches

|     | 110086  |     | 107  |
| --- | ------- | --- | ---- |

Leveraging Financial Personality for Inclusive Credit Scoring Amidst Global Uncertainty
Yang, S., Markoczy, L., & Qi, M. (2007). Unrealistic optimism in consumer credit card
adoption. Journal of Economic Psychology, 28(2), 170–185.
|     |     |     |     |
| --- | --- | --- | --- |
Yuan, H., Lau, R. Y., Xu, W., Pan, Z., & Wong, M. C. (2018). Mining Individuals' Behavior
Patterns from Social Media for Enhancing Online Credit Scoring. In PACIS (p. 163).
|     |     |     |     |
| --- | --- | --- | --- |
Yurdakul, D., Atik, D., & Dholakia, N. (2017). Redefining the bottom of the pyramid from a
| marketing perspective. Marketing Theory, 17(3), 289–303.   |     |     |     |
| ---------------------------------------------------------- | --- | --- | --- |
|                                                            |     |     |     |
Zhang, Y., Jia, H., Diao, Y., Hai, M., & Li, H. (2016). Research on credit scoring by fusing
social media information in online peer-to-peer lending. Procedia Computer Science, 91,
168–174.   Having established the benefits of personality-driven credit assessment, we now consider the

  accuracy and predictiveness potential of AI in credit risk prediction. This chapter delves

    into how AI can support more precise and equitable credit evaluations to improve
credit scoring approaches

|     | 106  |     | 110079  |
| --- | ---- | --- | ------- |

Chapter 4
110

Chapter 5
Artificial Intelligent Credit Risk Prediction
An Empirical Study of Analytical Artificial Intelligence
Tools for Credit Risk Prediction in a digital era
Published as:
Van Thiel, D., & Van Raaij, W. F. (2019).
Artificial intelligence credit risk prediction: An empirical study of analytical artificial intelligence
tools for credit risk prediction in a digital era.
Journal of Risk Management in Financial Institutions, 12(3), 268-286
Van Thiel, D., & van Raaij, W. F. (2019).
Artificial intelligent credit risk prediction: An empirical study of analytical artificial intelligence tools
for credit risk prediction in a digital era.
Journal of Accounting and Finance, 19(8).
Presented at:
The World Economic Association International (WEAI) 2019, San Francisco, USA

Chapter 5
combination of factors (Mizen 2008). Firstly, the financial stability of credit bases diminished
due to the extensive sales of sub-prime mortgages. Secondly, risk was not adequately
ABSTRACT assessed on an individual level, as existing risk management approaches were not designed
for such granularity. Thirdly, financial innovation introduced the product known as 'asset-
Global consumer lending has experienced a compound annual growth rate (CAGR) of 4.8% backed securities' (Mizen, 2008). These securities propagated global risk without a full
up to the year 2020. Predictions indicate that global digital lending is set to grow at a CAGR understanding of their distribution. This posed a global threat to the financial system.
of 26.9% until 2030. Despite more than a decade passing since the credit crunch, the financial
system is once again at risk, with unresolved root causes. Notably, the outstanding amount of A number of financial institutions have collapsed or experienced financial problems due to
credit globally has doubled compared to the lending volume in 2008. Simultaneously, an inefficient credit management systems (Njanike, 2009). Credit risk, defined as the risk of
increasing number of credit decisions are being made in the present day, with digital default on debt arising from a borrower's failure to meet required payments (Basel
advancements offering opportunities for financial inclusion. Additionally, the service Committee, 2000), highlights that poor lending decisions, such as excessive lending or
expectations of millennials are accelerating the transformation from traditional lending to mispricing, have led and will continue to lead to substantial losses and ongoing threats to the
digital lending. In this context, as we navigate the growing AI information age, new methods global financial system.
for credit risk scoring could become a central pillar for the continuity of financial institutions
and the stability of the global financial system. This paper presents what we believe to be the Once of the consequences of the credit crunch shock is the tightening of the credit system.
inaugural research on AI-based credit scoring, focusing on two advanced European credit The tightening translated into lower credit growth, higher interest rates, lower probability of
markets in the United Kingdom and the Netherlands. These markets were selected based on accepting loan applications and higher probability of relationship termination (di Patti, 2016).
their advancements in digital lending practices, aiming to explore the extent to which lenders Financial innovation and overconfidence about asset values and the riskiness of new financial
can enhance their credit decisions through individual risk assessments utilizing artificial products were important factors behind the U.S. credit crisis (Boz, 2014). A decade later, it is
intelligence. The research employed supervised learning and was conducted on 133,152 evident that these root causes of the 2008 credit crunch remain unresolved. On the contrary,
mortgage and credit card customers across prime, near-prime, and sub-prime lending the global outstanding amount of credit has doubled in comparison to the lending volume of
segments of three European lenders in the UK and the Netherlands during the period from 2008 (IMF, 2024). Presently, not only traditional banks but also tech giants such as Amazon
January 2016 to July 2017. Neural networks and random forests were chosen as candidate and Alibaba have swiftly entered the lending market. The robust growth in online retail
models due to their popularity in credit risk, offering the advantage of handling both lending, emerging markets, and peer-to-peer lending has once again compromised the quality
structured and unstructured data. The paper outlines three experiments that developed of credit bases.
artificial intelligent probability of default models and compares their quality with that of
traditionally applied logistic PD-models. Across all experiments, the artificial intelligent Central banks, in response, have pre-covid lowered interest rates to levels that render the
models consistently outperformed the traditional models. Consequently, scalable, automated, interest instrument less effective in the face of an impending economic downturn.
and inclusive credit risk solutions can leverage AI in their risk scoring processes. Additionally, they reduced risk in the system by requiring banks to increase their capital
(Bank for International Settlements, 2024). The looming threat of an economic downturn
Credit, risk scoring, digital lending, lending robotization, big data, artificial intelligence. however, which could lead to a new financial crisis, still is exacerbated by global
uncertainties such as wars, currency crises in developing countries, climate change, and other
destabilizing factors.
Another transformative development in credit is driven by changing demands from
5.1 Introduction
millennials for an enhanced customer experience. Millennials and Gen Z, known as digital
natives, are driving the shift toward digital banking (Choudhary et al., 2020). The
5.1.1. Context: the playing field a decade after the credit crunch
digitalization, resulting from the evolving requirements of the next generation, transforms
Asset backed securitization permitted the banking sector to issue mortgages ahead of
borrowers into data agents generating extensive behavioral data that may contain distinctive
deposits, such that the value of outstanding mortgages in the US at the end of 2007 exceeded
risk features. New analytical methods are needed to harness this combination of structured
annual national income (Heilpern et al. 2009). This led to the “credit crunch”, emerged as a
and unstructured data.
serious problem for the US economy towards the end of 2006 when charge off’s and default
rates on sub-prime higher risk loans increased. A growing number of US households either
The global market for the digitization of lending is expected to grow at a Compound Annual
could not repay existing mortgage debt (charged off) or defaulted (repayment schedules not
Growth Rate (CAGR) of 53% to reach $83.6 billion by 2025. Digitization enables lenders to
met). According to Brown and Moles (2014), the global credit crunch underscored the critical
more effectively target their customers with well-timed offers at lower costs. Digital lending
importance of credit decision-making. The financial risk attached to sub-prime mortgages
automates complex processes and reduces manual interventions, leading to an increasing
was less of a problem when US home prices inflated and household’s could not only trade up
demand for its services. In the coming years, there will be a rising adoption of digital lending.
but also extract additional cash resources from equity release schemes (Heilpern et al. 2009).
Charge offs and the rate of mortgage loan delinquency increased towards the end of year
Customer experience and financial advice are concepts that lack well-defined definitions and
2006 and this upward trend continued into 2008. The credit crunch was driven by a
are deficient in well-developed assessment methods and metrics (Van Thiel & Van Raaij,
111029 110

Artificial Intelligent Credit Risk Prediction - An Empirical Study of
Analytical Artificial Intelligence Tools for Credit Risk Prediction in a digital era
combination of factors (Mizen 2008). Firstly, the financial stability of credit bases diminished
due to the extensive sales of sub-prime mortgages. Secondly, risk was not adequately
ABSTRACT assessed on an individual level, as existing risk management approaches were not designed
for such granularity. Thirdly, financial innovation introduced the product known as 'asset-
Global consumer lending has experienced a compound annual growth rate (CAGR) of 4.8% backed securities' (Mizen, 2008). These securities propagated global risk without a full
up to the year 2020. Predictions indicate that global digital lending is set to grow at a CAGR understanding of their distribution. This posed a global threat to the financial system.
of 26.9% until 2030. Despite more than a decade passing since the credit crunch, the financial
system is once again at risk, with unresolved root causes. Notably, the outstanding amount of A number of financial institutions have collapsed or experienced financial problems due to
credit globally has doubled compared to the lending volume in 2008. Simultaneously, an inefficient credit management systems (Njanike, 2009). Credit risk, defined as the risk of
increasing number of credit decisions are being made in the present day, with digital default on debt arising from a borrower's failure to meet required payments (Basel
advancements offering opportunities for financial inclusion. Additionally, the service Committee, 2000), highlights that poor lending decisions, such as excessive lending or
expectations of millennials are accelerating the transformation from traditional lending to mispricing, have led and will continue to lead to substantial losses and ongoing threats to the
digital lending. In this context, as we navigate the growing AI information age, new methods global financial system.
for credit risk scoring could become a central pillar for the continuity of financial institutions
and the stability of the global financial system. This paper presents what we believe to be the Once of the consequences of the credit crunch shock is the tightening of the credit system.
inaugural research on AI-based credit scoring, focusing on two advanced European credit The tightening translated into lower credit growth, higher interest rates, lower probability of
markets in the United Kingdom and the Netherlands. These markets were selected based on accepting loan applications and higher probability of relationship termination (di Patti, 2016).
their advancements in digital lending practices, aiming to explore the extent to which lenders Financial innovation and overconfidence about asset values and the riskiness of new financial
can enhance their credit decisions through individual risk assessments utilizing artificial products were important factors behind the U.S. credit crisis (Boz, 2014). A decade later, it is
intelligence. The research employed supervised learning and was conducted on 133,152 evident that these root causes of the 2008 credit crunch remain unresolved. On the contrary,
mortgage and credit card customers across prime, near-prime, and sub-prime lending the global outstanding amount of credit has doubled in comparison to the lending volume of
segments of three European lenders in the UK and the Netherlands during the period from 2008 (IMF, 2024). Presently, not only traditional banks but also tech giants such as Amazon
January 2016 to July 2017. Neural networks and random forests were chosen as candidate and Alibaba have swiftly entered the lending market. The robust growth in online retail
models due to their popularity in credit risk, offering the advantage of handling both lending, emerging markets, and peer-to-peer lending has once again compromised the quality
structured and unstructured data. The paper outlines three experiments that developed of credit bases.
artificial intelligent probability of default models and compares their quality with that of
traditionally applied logistic PD-models. Across all experiments, the artificial intelligent Central banks, in response, have pre-covid lowered interest rates to levels that render the
models consistently outperformed the traditional models. Consequently, scalable, automated, interest instrument less effective in the face of an impending economic downturn.
and inclusive credit risk solutions can leverage AI in their risk scoring processes. Additionally, they reduced risk in the system by requiring banks to increase their capital
(Bank for International Settlements, 2024). The looming threat of an economic downturn
Credit, risk scoring, digital lending, lending robotization, big data, artificial intelligence. however, which could lead to a new financial crisis, still is exacerbated by global
uncertainties such as wars, currency crises in developing countries, climate change, and other
destabilizing factors.
Another transformative development in credit is driven by changing demands from
5.1 Introduction
millennials for an enhanced customer experience. Millennials and Gen Z, known as digital
natives, are driving the shift toward digital banking (Choudhary et al., 2020). The
5.1.1. Context: the playing field a decade after the credit crunch
digitalization, resulting from the evolving requirements of the next generation, transforms
Asset backed securitization permitted the banking sector to issue mortgages ahead of
borrowers into data agents generating extensive behavioral data that may contain distinctive
deposits, such that the value of outstanding mortgages in the US at the end of 2007 exceeded
risk features. New analytical methods are needed to harness this combination of structured
annual national income (Heilpern et al. 2009). This led to the “credit crunch”, emerged as a
and unstructured data.
serious problem for the US economy towards the end of 2006 when charge off’s and default
rates on sub-prime higher risk loans increased. A growing number of US households either
The global market for the digitization of lending is expected to grow at a Compound Annual
could not repay existing mortgage debt (charged off) or defaulted (repayment schedules not
Growth Rate (CAGR) of 53% to reach $83.6 billion by 2025. Digitization enables lenders to
met). According to Brown and Moles (2014), the global credit crunch underscored the critical
more effectively target their customers with well-timed offers at lower costs. Digital lending
importance of credit decision-making. The financial risk attached to sub-prime mortgages
automates complex processes and reduces manual interventions, leading to an increasing
was less of a problem when US home prices inflated and household’s could not only trade up
demand for its services. In the coming years, there will be a rising adoption of digital lending.
but also extract additional cash resources from equity release schemes (Heilpern et al. 2009).
Charge offs and the rate of mortgage loan delinquency increased towards the end of year
Customer experience and financial advice are concepts that lack well-defined definitions and
2006 and this upward trend continued into 2008. The credit crunch was driven by a
are deficient in well-developed assessment methods and metrics (Van Thiel & Van Raaij,
109 111103

Chapter 5
2016). The influence of self-directedness on financial decision-making is growing as the
Internet empowers consumers to learn from others' experiences and gather product
information. In their research, Van Thiel & Van Raaij developed the DCX model, unveiling
the factors and attributes that steer customer experience toward digital financial advice
models. With the digitalization of customer experience, consumers themselves become data
agents, and this data could prove invaluable for enhancing credit decisioning in the coming
decade. New analytical technologies must be adapted for the application of this behavioral
data.
The purpose of this paper is to contribute to the enhancement of responsible individual credit
decisioning around the research question “How do artificial intelligent models, specifically
random forests and neural networks, contribute to enhancing credit decisioning across diverse
asset classes, such as mortgage loans and credit card loans, and what are the comparative
performances of these and traditional models in terms of accuracy, efficiency, and
interpretability?” This paper presents the first research conducted across the United Kingdom
and the Netherlands on improving credit decisioning using these advanced modeling
techniques. Two highly advanced European lending markets, significantly impacted by the
2008 credit crunch, were selected to assess the extent to which lenders can improve their
credit decisions with individual risk assessments based on artificial intelligence. The research
employs supervised learning and has been conducted on 133,152 mortgage and credit card
customers across prime, near-prime, and sub-prime lending segments of three European
lenders in the UK and the Netherlands from January 2016 to July 2017. Neural networks and
random forests were chosen as candidate models due to their ability to work with both
structured and unstructured data.
5.1.2. Credit Risk Management
Credit risk can be defined as “the potential that a contractual party will fail to meet its
obligations in accordance with the agreed terms” (Brown and Moles, 2014). As a result of
transactions of various kinds, credit risk and credit risk management are key issues for most
firms (Brown and Moles, 2014). The possibility that a contractual arrangement is not adhered
to equates to the risk of non-performance. This has the capacity to hurt the objectives of a
firm; when a strategic plan is drawn, and it does not happen. Money can be lost if the
customer fails to pay, or if the financial institution in which money is deposited, goes
bankrupt. Companies with whom the firm has placed orders may themselves become
insolvent and fail to deliver on their promises. There are three characteristics to define this
credit risk:
1. Exposure at default (to a party that may possibly default or suffer an adverse change
in its ability to perform).
2. Probability of default. The likelihood that this party will default on its obligations (the
default probability).
3. Loss severity or it’s inverse the recovery rate (that is, how much can be retrieved if a
default takes place).
In this paper, we define the business issue as the prediction of non-performance (probability
of default); also, the larger the first two elements, the greater the risk. On the other hand, the
higher the amount that can be recovered, the lower the risk. Formally, we can therefore
express the risk as:
Credit risk = Exposure at default * Probability of Default * (1- Recovery Rate) (1)
111141

Artificial Intelligent Credit Risk Prediction - An Empirical Study of
Analytical Artificial Intelligence Tools for Credit Risk Prediction in a digital era
While the credit decision is relatively straightforward in theory (a lender must decide whether
to give credit or refuse credit to a potential client), in practice it involves experience,
judgement and a range of analytical and evaluative techniques that are designed to determine
the likelihood that money will be repaid or, equally, that the money will be lost (borrower
unable to repay). Managing credit risk therefore is a complex multi-dimensional problem, and
as a result, there are a number of different, often portfolio-based, approaches in use - some of
which are quantitative, while others involve qualitative judgements. Whatever the method
used, the key element is to understand the behavior and predict the likelihood of borrowers
defaulting on their obligations (Brown and Moles, 2014).
To understand the behavior and to predict default, all methods follow the same process and
risk management framework; namely, identification, evaluation and management. That is, the
cause of the risk must be identified, the extent of the risk has to be evaluated and decisions
have to be made as to how this risk is to be managed.
The first step in the credit management process is to identify the problem (Brown and Moles,
2014). In most cases, we look simply at the no-default/default probability variable. In some
applications it might be more complex, since we may want to monitor and evaluate changes
in credit quality, rather than simple non-performance only. Irrespective of how the initial
problem is defined, the size of the problem is then evaluated. Knowledge based models
(expert models), effect models and statistical models are applied here. However, these require
data and/or information from the business environment (i.e., application information,
payment history information and personal information).
The different analytical approaches for this can be loosely grouped into:
(1) Knowledge models, which have a degree of subjectivity (i.e., the use of expert judgement
by an analyst)
(2) Effect models, which combine some elements of subjectivity and systemic analysis (a
ratio analysis would fall into this category).
(3) Statistical models, which can be considered a more systematic approach (such as, credit
scoring models).
Model validation or, measuring the quality of the probability of default models, can be
conducted in several ways (Stein, 2002). Model validation becomes increasingly important as
artificial intelligent approaches with a black box character contain a serious risk to model
risk. Model risk is loss resulting from using insufficiently accurate models to reach decisions
(Derman, 1996). When assessing the quality of a PD model, Stein differentiates model
predictive power and model calibration. Model power describes how well a model
differentiates between non-defaulting (good) and defaulting (bad) customers. A common
statistic for assessing model power is the ROC-curve. ROCs are constructed by scoring all
credits and ordering the non-defaulters from worst-to-best on the x-axis, then plotting the
percentage of defaults excluded at each level on the y-axis. Here, the y-axis is formed by
associating every score on the x-axis with the cumulative percentage of defaults with a score
equal to, or worse than, the score in the test data. In other words, the y-axis gives the
percentage of defaults excluded as a function of the number of non-defaults excluded (Stein,
2002). A similar measure, a CAP (Cumulative Accuracy Profile) plot (Sobehart et al., 2000),
is constructed by plotting all test data from worst-to-best on the x-axis. Thus, a CAP plot
provides information on the percentage of defaulters that are excluded from a sample (TP
rate), given that we exclude all credits, good and bad, below a certain score.
111125

Chapter 5
CAP plots and ROC curves convey the same information in slightly different ways. This is
because they are geared toward answering slightly different questions. CAP plots answer the
question: “How much of an entire portfolio would a model have to exclude to avoid a
specific percentage of defaulters?”
While, ROC curves use the same information to answer the question: “What percentage of
non-defaulters would a model have to exclude to exclude a specific percentage of
defaulters?” The first question tends to be of more interest to business people, while the
second is somewhat more useful when analyzing error rates. Model calibration is
transforming classifier scores into class membership probabilities (Walker, 1996). Calibration
of credit model leads to cut off points in accepting new customers, limiting settings and credit
pricing. In this research, we aim to test if artificial intelligent models have a better quality
than traditional logistic regression models. Kaplan defines artificial intelligence as a systems
ability to correctly interpret external data, to learn from such data and to use those learnings
to achieve specific goals and tasks through flexible adaptation (Kaplan, Haenlein, 2019). The
core hypothesis in this research therefore is:
H1: Artificial intelligent models, specifically random forests and neural networks, will
demonstrate superior performance in credit decisioning for different asset classes, including
mortgage loans and credit card loans, as measured by accuracy, efficiency, and
interpretability when compared to traditional credit scoring models.
5.1.3. Regulation
In response to the credit crunch, BASEL III, a global risk framework, was developed to
enhance banks' liquidity and reduce their leverage (Basel Committee on Bank Supervision,
2010). Basel III constitutes a global, voluntary regulatory framework governing banks' capital
adequacy, stress testing, and market liquidity risk. The original Basel III rule, established in
2010, mandated banks to secure themselves with 4.5% common equity (an increase from 2%
in Basel II) of risk-weighted assets (RWAs). Since 2015, banks are required to maintain a
minimum Common Equity Tier 1 (CET1) ratio of 4.5%, supplemented by an additional
buffer of 1.5%. This results in a minimum Tier 1 capital comprising 6% of common equity.
Looking ahead, more stringent regulations, which will encompass new entrants like Amazon
and Alibaba, are anticipated regarding capital buffers after 2022 under Basel IV.
Nevertheless, driven by the involvement of new entrants, an expectation arises for simpler
and more standardized models for credit risk within Basel IV.
The transformation to Basel IV has already started through the transformation of accounting
principles of financial instruments to be introduced in 2022. As another response to increased
risk levels of lenders, namely, the International Accounting Standards Board (IASB, 2010),
promulgated stricter accountancy rules under the IFRS-9. Also, the Financial Accounting
Standards Board (FASB) published CECL standards with comparable requirements for US
credit institutions in June 2016. Both IFRS-9 and CECL contain stricter guidelines for
impairment. Therefore, lenders are challenged to transform from historical portfolio-based
credit risk buffering to individual and forward-looking credit risk buffering. In IFRS-9 the
allowance will be based on expected losses from individual defaults over the following 12
months, unless there is a significant increase in credit risk. If there is a significant increase,
the allowance will be measured as the present value of all individual credit losses projected
for the instrument over its full lifetime. If the credit risk recovers, the allowance can once
again be limited to the projected credit losses over the 12 months. Credit risk management
transforms from application and historically driven to behavioral, predictive and even
111163

Artificial Intelligent Credit Risk Prediction - An Empirical Study of
Analytical Artificial Intelligence Tools for Credit Risk Prediction in a digital era
prescriptive-driven. Innovation in credit risk management will, under pressure of regulation,
focus on risk prediction and risk prevention per individual to structurally lower defaults and
increase the financial health of customers. Therefore, 21st century advanced credit risk
management will have to merge statistics, accountancy and financial management with
behavioral and computer science to continually monitor the financial behavior of consumers,
thus prevent risk.
There are some issues to overcome, however. As, under BASEL II already signaled, one of
the big issues defined for proper credit risk management is the poor availability of robust data
to quantify banks’ risk (Basel Committee on Bank Supervision, 2000). Under IFRS-9 and
new Basel regimes coming up, data availability and quality will become more important and
banks are lagging external data adaptation, such as Fintechs and other tech-giants. Another
issue to overcome is how to effectively find ways that benefit from the increasing amount of
data while minimizing the risk of information overload. Thirdly, the increasing focus on
privacy in our digital age will lead to stricter regulations, such as the General Data Protection
Regulation (GDPR). Consumers need to be able to view, update or delete their personal data
with banks, and lenders must give specific consent for all applications of their personal data.
Finally, in Europe, the Payment Service Directive 2 (PSD-2) is currently being implemented;
a game changer. PSD-2 obliges banks whose customers empower a third-party service
provider to access their personal data and to provide transaction data to such third-party
service providers. The data-explosion that will be caused by the PSD-2 will strongly impact
risk management, and it will also raise issues for risk managers around digitally-based trust,
identification and authentication.
As traditional credit risk management is driven by historical data, portfolio management and
logistic modeling, such statistical models are unable to cope with these transformations being
enforced through legislation, and they are also unable to cope with unstructured data and can
therefore not benefit from the behavioral data explosion in delivering advanced risk
management solutions, such as continuous individual monitoring, predictive and prescriptive
services that are expected to drive customer experience. The purpose of this paper is to assess
the opportunity of artificial intelligence technologies, like random forests and neural
networks, driven by behavioral data as a solution for the increased global credit risk. Here,
experiments have been done to test the benefit of statistical artificial intelligence in credit risk
for the probability of default in consumer lending. In the experiments supervised learning was
applied to classify good and bad payers with the AI-models.
5.1.4. The Digital Consumer: Big data, Artificial Risk Intelligence and Risk
Robotization
Driven by the global digitization of lifestyles, the world is currently experiencing a
behavioral data explosion (Van Thiel and Van Raaij, 2017). Click streams, transaction
histories, social media, mobile behavior, psychometric surveys and sensors provide huge
volumes of behavioral data. New credit decisioning applications are being developed. Many
households in developing countries for example lack formal financial histories, making it
difficult for banks to extend loans, and for potential borrowers to receive them. However,
many of these households have mobile phones, which generate rich data about behavior.
Bjorkegren and Grissen show that behavioral signatures in mobile phone data predict loan
default, using call records matched to loan outcomes. Van Thiel & Van Raaij show that
psychometric features that provide inside in attitudes, lifestyles and values predict customer
engagement. Van Thiel further researched the application of psychometric data on credit
decisioning within AdviceRobo. And Zhang et al. show, in order to reduce the serious
111147

Chapter 5
problem of information asymmetry between both sides of P2P loans, the use of social
information to describe the behavior characteristics of the borrowers. A person's social
behavior and language can reflect the characteristics of their behavior, which can be used as
credit data. On the internet, the behavior and language of users can be obtained from social
media. An increasingly number of data sources with potentially more classifying and
predictive features will follow in the upcoming years.
Every day, 2.5 quintillion bytes of data are created, and 90% of data in the world today, were
already produced within the past years (IBM, 2016). Our capability for data generation has
never been so powerful and enormous since the invention of Information Technology in the
early 19th century (Wu et al., 2014). The most fundamental challenge for Big Data
applications is to explore large volumes of data and extract useful information or knowledge
for future actions (Rajaraman and Ullman, 2011). In many situations, knowledge extraction
must be highly efficient and close to real-time, because storing all observed data is infeasible.
Big data means more than simply larger storage requirements or collecting data from social
media platforms with millions of participants (Flood et al., 2016). ‘Bigness’ is a symptom of
scalability issues in one or more dimensions – namely, the three Vs: volume, velocity and
variety (IBM, 2016).
• Volume – Roughly speaking, this is the simple size in bytes of a dataset, which can
place a strain on storage and computational resources (Flood et al., 2016). ‘Big’
means that organizations must increasingly deal with a peta-byte scale of data
collection through click streams, transaction histories, sensors and elsewhere.
• Velocity – The rate at which data arrive, which can strain network bandwith and
stream analytics (O’Hara, 2015). Organizations must increasingly apply the data fast
for supporting their applications as f.e. fraud detection.
• Variety – The diversity of schemas, or formal structures, for data arriving from
different sources, which can strain data-integration processes (Halevy, et al. 2006).
Data from different sources does not fit neatly into existing processing tools.
So, a dataset is too ‘big’ when it becomes computationally infeasible to process the dataset
using traditional tools (MongoDB, 2016); new tools are required to apply the exploding
volume of behavioral data. As most of this new data is unstructured, it requires new analytical
models that can cope with both structured and unstructured data. New analytical techniques
rely on mature commercial technologies of relational database management systems
(DBMS); data warehousing; extraction, transaction and load (ETL); online analytical
processing (OLAP); and business process management (BPM) (Chaudhuri et al., 2011).
Since the late 1980s, various data mining algorithms have been developed by researchers
from artificial intelligence, algorithm and database communities. Most of these popular data
mining algorithms have been incorporated in commercial and open source data mining
systems (Witten et al., 2011). Other advances, such as, neural networks for
classification/prediction, clustering and genetic algorithms for optimization and machine
learning have all contributed to the success of data mining across different applications (Chen
et al., 2012). These scalable intelligent automated continuous, often platform, applications are
considered the first risk robots. Evaluating credit risk based on individual behavioral data
could offer greater scalability compared to situation-specific regression models. Therefore,
we contend that a key advantage of AI credit scorecards lies in their capacity to leverage both
structured and unstructured data.
111185

Artificial Intelligent Credit Risk Prediction - An Empirical Study of
Analytical Artificial Intelligence Tools for Credit Risk Prediction in a digital era
problem of information asymmetry between both sides of P2P loans, the use of social
information to describe the behavior characteristics of the borrowers. A person's social As consumer behavior becomes increasingly digital, generating an increasing volume of
behavior and language can reflect the characteristics of their behavior, which can be used as behavioral data, consumer lending will see further growth. Here, other elements like digital
credit data. On the internet, the behavior and language of users can be obtained from social privacy, identification and authentication will have to be monitored prudently. Credit risk
media. An increasingly number of data sources with potentially more classifying and management will stay the most important element of post-credit crisis lending but must re-
predictive features will follow in the upcoming years. invent itself accordingly. It will have to change from a historically portfolio-focused
monitoring function to a pro-active predictive and prescriptive service for individual
Every day, 2.5 quintillion bytes of data are created, and 90% of data in the world today, were customers. As access to good data is considered one of the issues for proper risk
already produced within the past years (IBM, 2016). Our capability for data generation has management, data architecture and data cleaning will take priority. But with all pressure from
never been so powerful and enormous since the invention of Information Technology in the society (privacy, digital trust), regulation (capital ratios and avoidance of individual risk) and
early 19th century (Wu et al., 2014). The most fundamental challenge for Big Data shareholders (cost/income and capital ratios) - scalable ‘risk robots’ will likely standardize
applications is to explore large volumes of data and extract useful information or knowledge these highly complex forward-looking activities in coming years. Across many geographies,
for future actions (Rajaraman and Ullman, 2011). In many situations, knowledge extraction an increasing number of financial service providers are currently operating or considering to
must be highly efficient and close to real-time, because storing all observed data is infeasible. utilize, the use of robo-advisors - online platforms that provide advice using complex
Big data means more than simply larger storage requirements or collecting data from social computer algorithms (Bradbury, 2014). These robo-advisors make use of the increasing
media platforms with millions of participants (Flood et al., 2016). ‘Bigness’ is a symptom of amount of behavioral data and apply algorithms that match consumers or small businesses
scalability issues in one or more dimensions – namely, the three Vs: volume, velocity and with financial products or portfolios (Van Thiel and Van Raaij, 2017). The purpose of this
variety (IBM, 2016). paper is to test the impact on risk management of artificial intelligent techniques that will
drive automated risk management for advice-robot solutions. Research has been performed to
• Volume – Roughly speaking, this is the simple size in bytes of a dataset, which can assess the extent to which the application of neural networks, random forest and support
place a strain on storage and computational resources (Flood et al., 2016). ‘Big’ vector machines, results in better default predictions in a digital and heavily regulated global
means that organizations must increasingly deal with a peta-byte scale of data market. The research describes three experiments conducted across the United Kingdom and
collection through click streams, transaction histories, sensors and elsewhere. the Netherlands, which develop advanced probability of default models and compare the
model quality with the quality of the traditionally applied PD-models. Butaru et al. (2014)
• Velocity – The rate at which data arrive, which can strain network bandwith and performed similar research on the data of US credit card lenders. The difference with this
stream analytics (O’Hara, 2015). Organizations must increasingly apply the data fast research is that we focus on different credit products over different geographies, while Butaru
for supporting their applications as f.e. fraud detection. examined only the US. Also, Khandani et al., (2010) performed research on artificial
intelligence on risk prediction. The difference with Khandani and colleagues, is that they
• Variety – The diversity of schemas, or formal structures, for data arriving from focused on one bank, while this research incorporates multiple banks. This ultimately leads to
different sources, which can strain data-integration processes (Halevy, et al. 2006). our observation that artificial intelligence models predicting default risk can be applied
Data from different sources does not fit neatly into existing processing tools. universally across various geographies and product groups without the need for
customization.
So, a dataset is too ‘big’ when it becomes computationally infeasible to process the dataset
using traditional tools (MongoDB, 2016); new tools are required to apply the exploding
volume of behavioral data. As most of this new data is unstructured, it requires new analytical
models that can cope with both structured and unstructured data. New analytical techniques
rely on mature commercial technologies of relational database management systems
(DBMS); data warehousing; extraction, transaction and load (ETL); online analytical
processing (OLAP); and business process management (BPM) (Chaudhuri et al., 2011).
Since the late 1980s, various data mining algorithms have been developed by researchers
from artificial intelligence, algorithm and database communities. Most of these popular data
mining algorithms have been incorporated in commercial and open source data mining
systems (Witten et al., 2011). Other advances, such as, neural networks for
classification/prediction, clustering and genetic algorithms for optimization and machine
learning have all contributed to the success of data mining across different applications (Chen
et al., 2012). These scalable intelligent automated continuous, often platform, applications are
considered the first risk robots. Evaluating credit risk based on individual behavioral data
could offer greater scalability compared to situation-specific regression models. Therefore,
we contend that a key advantage of AI credit scorecards lies in their capacity to leverage both
structured and unstructured data.
115 111169

Chapter 5
5.2 Method
5.2.2. Moddeling approach
5.2.1. Empirical Design
5.2.2.1. Model development
5.2.1.1. Research design After preparing the data, the candidate machine learning models were trained 50 times with a
Our dependent variable is the delinquency (default) status. For the purposes of this study, we different sample of the training data. As candidate models, we chose random forests and
define delinquency as a mortgage or credit card account greater than or equal to 90 days past neural nets since they are the most popular supervised learning methods that are able to work
being due (Basel Committee on Banking Supervision, 2016). We assume that we are solving with both structured and unstructured data in credit risk. Random forests, or random decision
a two-class classification problem; the learning algorithm takes the training dataset, forests, constitute an ensemble learning method applicable to classification, regression, and
consisting of pairs (x, y), where x X is the feature or attribute vector (and can include other tasks. This approach involves constructing numerous decision trees during training and
categorical- as well as real-valued variables), and y {0,1} as input. The output of the outputting the class mode (classification) or mean prediction (regression) of the individual
learning algorithm maps X to y {∈0,1} (or possibly, in the case of logistic regression, to [0, trees. Random decision forests address the tendency of decision trees to overfit their training
1] where the output represents Pr (y = 1)). To compa∈re the quality metrics of the models and set, exhibiting less variance by incorporating a larger number of trees.
to standardize for robo-risk inte∈lligence, banks participating in the experiments delivered the It is essential to note a significant challenge with decision trees, namely their high variance.
exact same dataset they themselves apply in their traditional logistic regression risk models. Minor changes in the data can lead to markedly different series of splits, introducing a level
The mortgage data sets contained a three-year transaction history. The thin file credit card of uncertainty in interpretations. The primary reason for this instability lies in the hierarchical
data set contained a 1-year transaction history. Because, bank datasets differentiated, to be nature of the process, where an error in the top split propagates down to all subsequent splits.
able to draw learnings for an automated robo-solution across geographies, banks, customer - While using a more stable split criterion can mitigate this to some extent, inherent instability
and product segments, we use the Azure Machine Learning Studio (see persists as a trade-off for estimating a simple, tree-based structure from the data (Hastie et al.,
https://studio.azureml.net for more information) to run the same models on the different data 2009).
sets.
The random forest method combines two important ideas to improve the performance of
5.2.1.2. Data decision trees, which are the base learners. The first idea is bagging, or bootstrap aggregation.
The first step is to collect and prepare the data. To avoid data-compliancy and privacy issues, Instead of learning a single decision tree, bagging resamples the training dataset with
participating banks shared anonymized customer data. All datasets collectively form a sample replacement T times, and learns a new decision tree model on each of these bootstrapped
of 133,152 customers. The two samples of Dutch banks for mortgage default prediction are sample training sets. The classification model then allows all T decision trees to vote on the
sized: 55.812 and 47.346. The sample for thin-file credit scoring of a British credit card issuer classification, using a majority vote to decide on the predicted class. The key benefit of
is 6,994, thus substantially smaller. bagging is that it greatly reduces the variance of decision trees, and typically leads to
significant improvements in out-of-sample classification performance. The second key idea
The data is prepared for the machine learning models using complete and coherent of random forests is to further reduce correlation among each of the induced trees by
meaningful features. Also, assessments are conducted on data definitions, the data sources artificially restricting the set of features considered for each recursive split. When learning
and banks’ policy definitions of delinquencies. To compare outcomes with traditional logistic each tree, as each recursive split is considered, the random forest learner randomly selects a
regression modeling approaches, sources applied for default predictions in these experiments subset of the features (for classification tasks, typically the square root of the total number of
are internal bank data only. However, in the UK experiment on credit scoring thin-file features), and only considers those features. Random forests have been enormously
customers, external credit bureau data are also applied in the logistic regression approach. empirically successful on many out-of-sample classification benchmarks in the last decade
Here, we cooperated in the UK with credit bureaus Experian and CallCredit. and are considered among the best ‘out of the box’ learning algorithms available today for
general tasks (Caruana and Niculescu- Mezil, 2006; Criminisi et al., 2012).
Having received the anonymized datasets, data-cleaning took place by deleting and repairing An artificial neural network is a network of simple elements called artificial neurons, which
missing values. On average 0.26% of data was missing and 10.67% qualified as outliers. receive input, change their internal state according to that input, and produce output
After cleaning the data, feature development was performed on all datasets. In feature depending on the input and activation. The main advantages of using Artificial Neural
preparation, we looked at (1) null-values; (2) whether a feature has a discrete or continuous Networks include the handling of large amount of data sets; the ability to implicitly detect
character; and, at (3) meaningful ratios, like income to loan to be designed as new features. complex nonlinear relationships between dependent and independent variables and the ability
Discrete features were made binary, and to finally check the feature quality, statistical to detect all possible interactions between predictor variables. Major limitation for credit
analyses per feature were performed, such as, f.e. calculating the maximum and minimum scoring is the black box character of the neural network as regulators demand lenders to be
value, the mean, median and standard deviation. In addition, the sample data was partitioned able to explain the reasons for accepting or rejecting new applicants. For this reason we used
following the hold-out method into a training (70%)/validation (30%) sample. the neural networks to understand their impact, but focused on the random forest models in
reporting to the lenders in the experiments.
112107 118

Artificial Intelligent Credit Risk Prediction - An Empirical Study of
Analytical Artificial Intelligence Tools for Credit Risk Prediction in a digital era
5.2 Method
5.2.2. Moddeling approach
5.2.1. Empirical Design
5.2.2.1. Model development
5.2.1.1. Research design After preparing the data, the candidate machine learning models were trained 50 times with a
Our dependent variable is the delinquency (default) status. For the purposes of this study, we different sample of the training data. As candidate models, we chose random forests and
define delinquency as a mortgage or credit card account greater than or equal to 90 days past neural nets since they are the most popular supervised learning methods that are able to work
being due (Basel Committee on Banking Supervision, 2016). We assume that we are solving with both structured and unstructured data in credit risk. Random forests, or random decision
a two-class classification problem; the learning algorithm takes the training dataset, forests, constitute an ensemble learning method applicable to classification, regression, and
consisting of pairs (x, y), where x X is the feature or attribute vector (and can include other tasks. This approach involves constructing numerous decision trees during training and
categorical- as well as real-valued variables), and y {0,1} as input. The output of the outputting the class mode (classification) or mean prediction (regression) of the individual
learning algorithm maps X to y {∈0,1} (or possibly, in the case of logistic regression, to [0, trees. Random decision forests address the tendency of decision trees to overfit their training
1] where the output represents Pr (y = 1)). To compa∈re the quality metrics of the models and set, exhibiting less variance by incorporating a larger number of trees.
to standardize for robo-risk inte∈lligence, banks participating in the experiments delivered the It is essential to note a significant challenge with decision trees, namely their high variance.
exact same dataset they themselves apply in their traditional logistic regression risk models. Minor changes in the data can lead to markedly different series of splits, introducing a level
The mortgage data sets contained a three-year transaction history. The thin file credit card of uncertainty in interpretations. The primary reason for this instability lies in the hierarchical
data set contained a 1-year transaction history. Because, bank datasets differentiated, to be nature of the process, where an error in the top split propagates down to all subsequent splits.
able to draw learnings for an automated robo-solution across geographies, banks, customer - While using a more stable split criterion can mitigate this to some extent, inherent instability
and product segments, we use the Azure Machine Learning Studio (see persists as a trade-off for estimating a simple, tree-based structure from the data (Hastie et al.,
https://studio.azureml.net for more information) to run the same models on the different data 2009).
sets.
The random forest method combines two important ideas to improve the performance of
5.2.1.2. Data decision trees, which are the base learners. The first idea is bagging, or bootstrap aggregation.
The first step is to collect and prepare the data. To avoid data-compliancy and privacy issues, Instead of learning a single decision tree, bagging resamples the training dataset with
participating banks shared anonymized customer data. All datasets collectively form a sample replacement T times, and learns a new decision tree model on each of these bootstrapped
of 133,152 customers. The two samples of Dutch banks for mortgage default prediction are sample training sets. The classification model then allows all T decision trees to vote on the
sized: 55.812 and 47.346. The sample for thin-file credit scoring of a British credit card issuer classification, using a majority vote to decide on the predicted class. The key benefit of
is 6,994, thus substantially smaller. bagging is that it greatly reduces the variance of decision trees, and typically leads to
significant improvements in out-of-sample classification performance. The second key idea
The data is prepared for the machine learning models using complete and coherent of random forests is to further reduce correlation among each of the induced trees by
meaningful features. Also, assessments are conducted on data definitions, the data sources artificially restricting the set of features considered for each recursive split. When learning
and banks’ policy definitions of delinquencies. To compare outcomes with traditional logistic each tree, as each recursive split is considered, the random forest learner randomly selects a
regression modeling approaches, sources applied for default predictions in these experiments subset of the features (for classification tasks, typically the square root of the total number of
are internal bank data only. However, in the UK experiment on credit scoring thin-file features), and only considers those features. Random forests have been enormously
customers, external credit bureau data are also applied in the logistic regression approach. empirically successful on many out-of-sample classification benchmarks in the last decade
Here, we cooperated in the UK with credit bureaus Experian and CallCredit. and are considered among the best ‘out of the box’ learning algorithms available today for
general tasks (Caruana and Niculescu- Mezil, 2006; Criminisi et al., 2012).
Having received the anonymized datasets, data-cleaning took place by deleting and repairing An artificial neural network is a network of simple elements called artificial neurons, which
missing values. On average 0.26% of data was missing and 10.67% qualified as outliers. receive input, change their internal state according to that input, and produce output
After cleaning the data, feature development was performed on all datasets. In feature depending on the input and activation. The main advantages of using Artificial Neural
preparation, we looked at (1) null-values; (2) whether a feature has a discrete or continuous Networks include the handling of large amount of data sets; the ability to implicitly detect
character; and, at (3) meaningful ratios, like income to loan to be designed as new features. complex nonlinear relationships between dependent and independent variables and the ability
Discrete features were made binary, and to finally check the feature quality, statistical to detect all possible interactions between predictor variables. Major limitation for credit
analyses per feature were performed, such as, f.e. calculating the maximum and minimum scoring is the black box character of the neural network as regulators demand lenders to be
value, the mean, median and standard deviation. In addition, the sample data was partitioned able to explain the reasons for accepting or rejecting new applicants. For this reason we used
following the hold-out method into a training (70%)/validation (30%) sample. the neural networks to understand their impact, but focused on the random forest models in
reporting to the lenders in the experiments.
117 111281

Chapter 5
5.2.2.2. Measuring performance 5.3 Results
The goal of our delinquency prediction models is to classify mortgage and credit card
accounts into two categories: accounts that become 90 days or more past due within the next 5.3.1. Experiment 1: Dutch Bank Insurance Company
n quarters (‘bad’ accounts), and accounts that do not (‘good’ accounts). Therefore, our The first experiment was held between January 2016 and August 2016 with a tier-2 Dutch
measure of performance should reflect the accuracy with which our model classifies the bank insurance company. The bank services 47,347 mortgage customers and holds a
accounts into these two categories. mortgage portfolio of €10 billion. The bank’s strategy focusses on improving customer
experience and operational excellence. To improve their customer experience, they want to
One common way to measure performance of such binary classification models is the understand the opportunity that artificial intelligence provides for lowering default rates. To
AUROC. The AUROC, or Area Under the ROC-Curve, is a score between 0 and 1 that shows accomplish this, the bank stepped into this experiment to test the quality of their traditional
the predictive power of a model by calculating the mean of the precision and recall. Precision logistic default prediction model against a machine learning champion model. Actual logistic
is defined as the number of correctly predicted delinquent accounts (true positives) divided regression area under the curve (AUROC) is 0.87 and actual defaults in 2016 were 0.9%.
by the predicted number of delinquent accounts (true positives + false positives), while recall
is defined as the number of correctly predicted delinquent accounts (true positives) divided The bank anonymized their customer data and securely shared 67 anonymized application
by the actual number of delinquent accounts (true positives + false negatives). Precision is and behavioral features per individual. After training different models, the champion model
meant to gauge the number of false positives (accounts predicted to be delinquent that stayed for their data proved to be a random forest.
current), while recall gauges the number of false negatives (accounts predicted to stay current
that went into default). The random forest champion model performs an AUROC of 0.95%. Compared to the
traditional AUROC of 0.87%, machine learning shows an improvement in AUROC of 18.8%.
Although we primarily look at the AUROC to test our hypotheses, we know other statistics For this bank, observation 1 “AI predicts default risk better than traditional logistic
are also worth looking at when qualifying a model. Indeed, a widespread metric is the Gini- regression” seems true. The AUROC is represented in the Lorenz Curve shown in Figure 1.
score. Gini is 2 times the AUROC – 1. Another metric is the F1-measure. The F-measure is
defined as the harmonic mean of precision and recall and assigns higher values to methods
that achieve a reasonable balance between precision and recall.
The other performance indicators to consider when selecting the champion prediction models Figure 1
are: (1) overall accuracy rate (bias between reference value and mean of the measurements);
and, (2) stability of model (stable over time and different datasets). Lorenz curve Dutch mortgage model ‘bank insurer’ (ROC-curve)
The modeling approach can be summarized as follows:
(1) 50 variants within each modeling algorithm are tried and applied on the training
sample. The modeling algorithms used are Neural Net and Random Forest.
(2) Each model is applied on the validation sample. The champion model within
each modeling algorithm is identified based on the above performance
indicators.
(3) The best performing champion models of the different experiments are analyzed
on similarities in features, as well in type of model.
The most predictive features for this bank’s delinquency are exposed in table 1 below.
112129 120

Artificial Intelligent Credit Risk Prediction - An Empirical Study of
Analytical Artificial Intelligence Tools for Credit Risk Prediction in a digital era
5.2.2.2. Measuring performance 5.3 Results
The goal of our delinquency prediction models is to classify mortgage and credit card
accounts into two categories: accounts that become 90 days or more past due within the next 5.3.1. Experiment 1: Dutch Bank Insurance Company
n quarters (‘bad’ accounts), and accounts that do not (‘good’ accounts). Therefore, our The first experiment was held between January 2016 and August 2016 with a tier-2 Dutch
measure of performance should reflect the accuracy with which our model classifies the bank insurance company. The bank services 47,347 mortgage customers and holds a
accounts into these two categories. mortgage portfolio of €10 billion. The bank’s strategy focusses on improving customer
experience and operational excellence. To improve their customer experience, they want to
One common way to measure performance of such binary classification models is the understand the opportunity that artificial intelligence provides for lowering default rates. To
AUROC. The AUROC, or Area Under the ROC-Curve, is a score between 0 and 1 that shows accomplish this, the bank stepped into this experiment to test the quality of their traditional
the predictive power of a model by calculating the mean of the precision and recall. Precision logistic default prediction model against a machine learning champion model. Actual logistic
is defined as the number of correctly predicted delinquent accounts (true positives) divided regression area under the curve (AUROC) is 0.87 and actual defaults in 2016 were 0.9%.
by the predicted number of delinquent accounts (true positives + false positives), while recall
is defined as the number of correctly predicted delinquent accounts (true positives) divided The bank anonymized their customer data and securely shared 67 anonymized application
by the actual number of delinquent accounts (true positives + false negatives). Precision is and behavioral features per individual. After training different models, the champion model
meant to gauge the number of false positives (accounts predicted to be delinquent that stayed for their data proved to be a random forest.
current), while recall gauges the number of false negatives (accounts predicted to stay current
that went into default). The random forest champion model performs an AUROC of 0.95%. Compared to the
traditional AUROC of 0.87%, machine learning shows an improvement in AUROC of 18.8%.
Although we primarily look at the AUROC to test our hypotheses, we know other statistics For this bank, observation 1 “AI predicts default risk better than traditional logistic
are also worth looking at when qualifying a model. Indeed, a widespread metric is the Gini- regression” seems true. The AUROC is represented in the Lorenz Curve shown in Figure 1.
score. Gini is 2 times the AUROC – 1. Another metric is the F1-measure. The F-measure is
defined as the harmonic mean of precision and recall and assigns higher values to methods
that achieve a reasonable balance between precision and recall.
The other performance indicators to consider when selecting the champion prediction models Figure 1
are: (1) overall accuracy rate (bias between reference value and mean of the measurements);
and, (2) stability of model (stable over time and different datasets). Lorenz curve Dutch mortgage model ‘bank insurer’ (ROC-curve)
The modeling approach can be summarized as follows:
(1) 50 variants within each modeling algorithm are tried and applied on the training
sample. The modeling algorithms used are Neural Net and Random Forest.
(2) Each model is applied on the validation sample. The champion model within
each modeling algorithm is identified based on the above performance
indicators.
(3) The best performing champion models of the different experiments are analyzed
on similarities in features, as well in type of model.
The most predictive features for this bank’s delinquency are exposed in table 1 below.
119 112203

Chapter 5
Table 1
Most predictive features Dutch ‘bank insurer’
We get deeper insights into model performance by looking at the underlying statistics. The
precision in this experiment is 0.99 good. It is calculated as the fraction of true positives
(101.463) divided by the sum of true and false positives (102.670). The recall in this
experiment is 0.99, which is also good. Recall is the fraction of true positives (101.463) over
the total amount of relevant instances (102.400). The precision and recall of this random
forest model are derived from the confusion matrix, shown in table 2.
112241

Artificial Intelligent Credit Risk Prediction - An Empirical Study of
Analytical Artificial Intelligence Tools for Credit Risk Prediction in a digital era
| Table 1  |     | Table 2  |     |
| -------- | --- | -------- | --- |
|          |     |          |     |
Most predictive features Dutch ‘bank insurer’  Confusion matrix Dutch ‘bank insurer’

We get deeper insights into model performance by looking at the underlying statistics. The
precision in this experiment is 0.99 good. It is calculated as the fraction of true positives
(101.463) divided by the sum of true and false positives (102.670). The recall in this
experiment is 0.99, which is also good. Recall is the fraction of true positives (101.463) over
the total amount of relevant instances (102.400). The precision and recall of this random  The quality metrics of the applied random forest champion model are shown in table 3,
forest model are derived from the confusion matrix, shown in table 2.   below.
|     |     |     |     |
| --- | --- | --- | --- |

|     |     |     |     |
| --- | --- | --- | --- |
|     |     |     |     |
|     |     |     |     |

|     |     |     |     |
| --- | --- | --- | --- |
|     |     |     |     |
|     |     |     |     |

|     |     |     |     |
| --- | --- | --- | --- |
|     |     |     |     |
|     |     |     |     |

|     |     |     |     |
| --- | --- | --- | --- |
|     |     |     |     |
|     |     |     |     |

|     |      |     |         |
| --- | ---- | --- | ------- |
|     | 121  |     | 112225  |

Chapter 5
learning champion model. The traditional logistic regression model gives a Gini-score of 0.8.
Table 3 As the AUROC = (Gini +1)/2 the AUROC is 0.9 and actual historical defaults in 2016 were
0.8%.
Model metrics Random Forest Model The bank applied the exact same method as we applied in the first experiment. They
anonymized their customer data and securely shared 51 anonymized features per individual.
For their pro-active servicing purpose, in this experiment we trained models predicting 6-
month, 3-month and 1-month defaults. To be able to compare with the traditional logistic
regression model, we focused on the 3-month (90 days) prediction model. After training
different models, the champion model proved to be a random forest.
The machine learning champion model performs an AUROC of 0,97. Compared to the
traditional AUROC of 0,8, machine learning shows an improvement in AUROC of 21,3%.
The AUROC is represented in the Lorenz Curve shown in Figure 2.
Figure 2
Lorenz curve Dutch mortgage model ‘mortgage bank’ (ROC-curve)
In a statistical analysis of binary classification, the F1 score (also known as the F-score or F-
measure) serves as a measure of a test's accuracy. It takes into account both the precision (p)
and the recall (r) of the test to calculate the score. Precision (p) represents the number of
correct positive results divided by the total number of positive results returned by the
classifier, while recall (r) signifies the number of correct positive results divided by the total
number of all relevant samples. The F1 score is the harmonic mean of precision and recall,
reaching its best value at 1 (indicating perfect precision and recall) and its worst at 0. The F1
score for the champion model is also good, standing at 0.99.
So, also having looked into the other statistics of this experiment, we conclude that in this
first experiment the random forest approach improved the predictive power of the credit
decisioning with 8% calculated on the difference between the AUROC’s.
5.3.2. Experiment 2: Dutch Mortgage Bank
The second experiment covers the period January - July 2017 with a Dutch mortgage bank.
The bank services 55,812 mortgage customers and holds a mortgage portfolio of €8.8 billion.
Different from the other bank in this experiment, this has mortgage application data only. The
bank’s strategy focusses on improving customer engagement by being there at the most
decisive moments in life. To improve their customer engagement, the bank wants to
understand the opportunities that machine learning can provide in predicting default risk at Also in this experiment we must assess the other metrics to fully prove the improvement
their currently performing customer base (the data does not contain earlier arrears or mentioned before. The most predictive features for this bank’s delinquency are shown in table
delinquencies). The bank has an ambition to proactively support people, months before they 4.
experience mortgage payment problems. To accomplish this, the bank stepped into this
experiment to test the quality of their traditional logistic default model against a machine
112263 124

Artificial Intelligent Credit Risk Prediction - An Empirical Study of
Analytical Artificial Intelligence Tools for Credit Risk Prediction in a digital era
learning champion model. The traditional logistic regression model gives a Gini-score of 0.8.
As the AUROC = (Gini +1)/2 the AUROC is 0.9 and actual historical defaults in 2016 were
0.8%.
The bank applied the exact same method as we applied in the first experiment. They
anonymized their customer data and securely shared 51 anonymized features per individual.
For their pro-active servicing purpose, in this experiment we trained models predicting 6-
month, 3-month and 1-month defaults. To be able to compare with the traditional logistic
regression model, we focused on the 3-month (90 days) prediction model. After training
different models, the champion model proved to be a random forest.
The machine learning champion model performs an AUROC of 0,97. Compared to the
traditional AUROC of 0,8, machine learning shows an improvement in AUROC of 21,3%.
The AUROC is represented in the Lorenz Curve shown in Figure 2.
Figure 2
Lorenz curve Dutch mortgage model ‘mortgage bank’ (ROC-curve)
Also in this experiment we must assess the other metrics to fully prove the improvement
mentioned before. The most predictive features for this bank’s delinquency are shown in table
4.
112247

Chapter 5
Table 4
Most predictive features ‘mortgage bank’
In the second experiment, we also gain a deeper insight into the model’s performance by
looking at underlying statistics. The precision in this experiment is 0,94 and calculated as the
fraction of true positives (985) divided by the sum of true and false positives (1,050). Recall
is 0,98; the fraction of true positives (985) over the total amount of relevant instances (1,003).
Both precision and recall also look good in this experiment.
The precision and recall of this random forest model are derived from the confusion matrix,
as shown in table 5.
112285

Artificial Intelligent Credit Risk Prediction - An Empirical Study of
Analytical Artificial Intelligence Tools for Credit Risk Prediction in a digital era
| Table 4                                   |     |          |     |
| ----------------------------------------- | --- | -------- | --- |
|                                           |     | Table 5  |     |
| Most predictive features ‘mortgage bank’  |     |          |     |
Confusion matrix random forest model Dutch ‘mortgage bank’

|     |     |     |     |
| --- | --- | --- | --- |
In the second experiment, we also gain a deeper insight into the model’s performance by
looking at underlying statistics. The precision in this experiment is 0,94 and calculated as the
fraction of true positives (985) divided by the sum of true and false positives (1,050). Recall
is 0,98; the fraction of true positives (985) over the total amount of relevant instances (1,003).
Both precision and recall also look good in this experiment.
|     |     |     |     |
| --- | --- | --- | --- |
The precision and recall of this random forest model are derived from the confusion matrix,
| as shown in table 5.   |      |     |         |
| ---------------------- | ---- | --- | ------- |
|                        |      |     |         |
|                        |      |     |         |
|                        |      |     |         |
|                        |      |     |         |
|                        |      |     |         |
|                        |      |     |         |
|                        |      |     |         |
|                        |      |     |         |
|                        |      |     |         |
|                        |      |     |         |
|                        |      |     |         |
|                        |      |     |         |
|                        |      |     |         |
|                        | 125  |     | 112269  |

Chapter 5
The quality metrics of the applied random forest champion model are shown in table 6.
Table 6. Model metrics Random Forest model
The F score in this experiment is 0.92, which implies an accurate model.
1
We can therefore conclude that also in the second experiment the random forest model
performed better than the traditional logistic regression approach.
5.3.3. Experiment 3: British Credit Card Company
The third experiment covers the period of October 2016 and February 2017 with a British
credit card issuer. The company services 5.4 million customers in the prime and near-prime
customer segments. The credit card loan book is £1.8 billion. The company’s strategy seeks
the onboarding potential of thin-file customer segments. Thin-file consumer segments are
segments with limited or no credit information. Therefore, thin-files have no access to credit.
To access these customer segments, the company wants to understand the opportunity
machine learning provides for onboarding thin-file consumers. To accomplish this, the
company stepped into this experiment to test the quality of their logistic regression scorecard-
model against a machine learning champion scorecard-model. Actual logistic regression Gini-
score is 0.25 (thin-file customers) and actual impairment rate in 2016 was 8.8%.
The company gathered data on thin-file consumers by accepting 6,994 in three months’ time;
the company monitored thin-file customer behavior for 6 months, and the data gathered
113207

Artificial Intelligent Credit Risk Prediction - An Empirical Study of
Analytical Artificial Intelligence Tools for Credit Risk Prediction in a digital era
contains 20 features. Additionally, data from credit bureaus Experian and Call Credit were
added. The company anonymized their customer data and securely shared the 901 features
The quality metrics of the applied random forest champion model are shown in table 6. per individual. Because of the thin-file character of the customers, most features were empty
and could not be used for modeling. After training different models, the champion model
proved to be a random forest. The machine learning champion model performed an AUROC
Table 6. Model metrics Random Forest model of 0.55 and a Gini of 0.32. Compared to the traditional Gini of 0.25, machine learning shows
an improvement of 28%. Also, the application of machine learning on credit cards as well as
the application in the UK seems to work.
Again, we must assess the more granular metrics to fully prove. The precision in this
experiment is 0.79 and calculated as the fraction of true positives (978) divided by the sum of
true and false positives (1,232). Recall is 0.94. Recall again is the fraction of true positives
(978) over the total amount of relevant instances (1,041). Both precision and recall look good
in this experiment. The precision and recall of this random forest model are derived from the
confusion matrix, as shown in table 7.
Table 7
Confusion matrix British ‘credit card issuer’
The F score in this experiment is 0.92, which implies an accurate model.
1
We can therefore conclude that also in the second experiment the random forest model
performed better than the traditional logistic regression approach.
5.3.3. Experiment 3: British Credit Card Company
The third experiment covers the period of October 2016 and February 2017 with a British
credit card issuer. The company services 5.4 million customers in the prime and near-prime
customer segments. The credit card loan book is £1.8 billion. The company’s strategy seeks
the onboarding potential of thin-file customer segments. Thin-file consumer segments are
segments with limited or no credit information. Therefore, thin-files have no access to credit.
To access these customer segments, the company wants to understand the opportunity
machine learning provides for onboarding thin-file consumers. To accomplish this, the The quality metrics of the applied random forest champion model are shown below in table 8.
company stepped into this experiment to test the quality of their logistic regression scorecard-
model against a machine learning champion scorecard-model. Actual logistic regression Gini-
score is 0.25 (thin-file customers) and actual impairment rate in 2016 was 8.8%.
The company gathered data on thin-file consumers by accepting 6,994 in three months’ time;
the company monitored thin-file customer behavior for 6 months, and the data gathered
127 112381

Chapter 5
Table 8 or spending data, income or estimated income, or all of them this currently is an important
feature for default prediction. We see more advanced lenders create more intelligent features
Random Forest model metrics British ‘credit card issuer’ by creating relations between income and loan and using social media data (bank insurance
company). As explained before, in our analyses we primarily looked at the random forests as
the neural networks black box character would not allow us to investigate the underlying
differentiating features.
To validate the hypothesis results were made comparable between random forest and logistic
approaches by applying the very same traditional structured dataset in the experiments and
compare on clear risk metrics. However, the benefit of the more advanced artificial
intelligence methods is that it can, on top of these traditional transaction data, also apply
unstructured non-financial data groups to improve credit application scoring, risk monitoring
and personalization strategies. Although the results support our contention that bank-specific
calibrated models are likely to be better predictors of default as opposed to a single model
applied to all banks, standardization of artificial intelligent models across banks and
geographies seems to some extend possible. Therefore, we can validate the core hypothesis in
this research. Further research has to be conducted in this area as it can bring an amazing cost
reduction benefit to international banks if they can standardize their risk modelling across
geographies and asset classes. Standardization might be started from more generic features.
If, for example, a basic risk intelligence robot works with data like (total) loan versus income,
the risk intelligence can be standardized for that part and both credit application and credit
monitoring can be structured for that part across geographies. On top of that, modules with
external scalable data groups like psychometric data, internet data, social media data and
mobile phone data can make robotized risk intelligence even more sophisticated. Advanced
artificial intelligence therefore seems to become the most powerful risk scoring approach in
this era of robotization of risk management.
The F score in this experiment is 0.24, which implies a less accurate model due to the small
1
number of features available for this thin-file customer segment.
We nevertheless conclude that random forest performs better than logistic regression in all
experiments. We can also see that AI models work across product groups and geographies.
The shorter the payment cycle, however, the better the models can be validated. Our
observations nevertheless can be validated. It is not a complete validation, as the hypotheses
were formed with the idea of standardization for robo-risk scoring in mind. The model
features, however, differ to much across the experiments to be able to standardize yet. Further
research on this needs to be conducted.
5.4 Summary
The purpose of this paper is to assess the opportunity of analytical artificial intelligence
technologies, namely random forests and neural networks, driven by behavioral data as a
solution to improve individual risk decisioning. Here, three experiments have been conducted
to test the benefit of AI credit risk models for probability of default in consumer lending. In
all experiments, artificial intelligent models performed better than traditional models. The
models of the British credit card company and the bank insurer, which could tap into payment
data, perform better than mortgage-only data models. Payment of the interest, monthly
payment are among the top predictive features with the mortgage only bank. The bank
insurance and credit card company looked more into credit score and loan to income ratio’s
which they had access to. Looking at these most predictive features the models produced,
high-level similarities can be uncovered across experiments. If banks have access to income
113229 130

Artificial Intelligent Credit Risk Prediction - An Empirical Study of
Analytical Artificial Intelligence Tools for Credit Risk Prediction in a digital era
Table 8 or spending data, income or estimated income, or all of them this currently is an important
feature for default prediction. We see more advanced lenders create more intelligent features
Random Forest model metrics British ‘credit card issuer’ by creating relations between income and loan and using social media data (bank insurance
company). As explained before, in our analyses we primarily looked at the random forests as
the neural networks black box character would not allow us to investigate the underlying
differentiating features.
To validate the hypothesis results were made comparable between random forest and logistic
approaches by applying the very same traditional structured dataset in the experiments and
compare on clear risk metrics. However, the benefit of the more advanced artificial
intelligence methods is that it can, on top of these traditional transaction data, also apply
unstructured non-financial data groups to improve credit application scoring, risk monitoring
and personalization strategies. Although the results support our contention that bank-specific
calibrated models are likely to be better predictors of default as opposed to a single model
applied to all banks, standardization of artificial intelligent models across banks and
geographies seems to some extend possible. Therefore, we can validate the core hypothesis in
this research. Further research has to be conducted in this area as it can bring an amazing cost
reduction benefit to international banks if they can standardize their risk modelling across
geographies and asset classes. Standardization might be started from more generic features.
If, for example, a basic risk intelligence robot works with data like (total) loan versus income,
the risk intelligence can be standardized for that part and both credit application and credit
monitoring can be structured for that part across geographies. On top of that, modules with
external scalable data groups like psychometric data, internet data, social media data and
mobile phone data can make robotized risk intelligence even more sophisticated. Advanced
artificial intelligence therefore seems to become the most powerful risk scoring approach in
this era of robotization of risk management.
The F score in this experiment is 0.24, which implies a less accurate model due to the small
1
number of features available for this thin-file customer segment.
We nevertheless conclude that random forest performs better than logistic regression in all
experiments. We can also see that AI models work across product groups and geographies.
The shorter the payment cycle, however, the better the models can be validated. Our
observations nevertheless can be validated. It is not a complete validation, as the hypotheses
were formed with the idea of standardization for robo-risk scoring in mind. The model
features, however, differ to much across the experiments to be able to standardize yet. Further
research on this needs to be conducted.
5.4 Summary
The purpose of this paper is to assess the opportunity of analytical artificial intelligence
technologies, namely random forests and neural networks, driven by behavioral data as a
solution to improve individual risk decisioning. Here, three experiments have been conducted
to test the benefit of AI credit risk models for probability of default in consumer lending. In
all experiments, artificial intelligent models performed better than traditional models. The
models of the British credit card company and the bank insurer, which could tap into payment
data, perform better than mortgage-only data models. Payment of the interest, monthly
payment are among the top predictive features with the mortgage only bank. The bank
insurance and credit card company looked more into credit score and loan to income ratio’s
which they had access to. Looking at these most predictive features the models produced,
high-level similarities can be uncovered across experiments. If banks have access to income
129 113303

Chapter 5
5.5 Discussion
This research validated the hypothesis that advanced credit risk modeling methods
outperform traditional logistic regression. In an era marked by rapid digital lending growth,
we argue that lenders should adopt these more accurate and predictive methods. Enhanced
individual risk assessments, limit setting, and pricing are crucial to reducing the risk of over-
lending.
Additionally, as millennials drive a shift in customer experience expectations, advanced
methods are particularly well-suited to support financial inclusion. Digitalization transforms
borrowers into data agents, generating vast amounts of behavioral data that may reveal
unique risk indicators. New analytical methods are needed to make full use of this
combination of structured and unstructured data. The global market for digital lending is
projected to grow at a Compound Annual Growth Rate (CAGR) of 26.6% through 2030,
driven by its ability to target customers more effectively with timely offers, automate
complex processes, and minimize manual interventions.
In this study, we utilize a large dataset of anonymized information from three banks across
different asset classes, such as mortgages and credit cards, in the United Kingdom and the
Netherlands. This dataset allows us to test the added value of AI-based risk models in
predicting mortgage and credit card delinquency. Our mortgage lending algorithms have
access to consumer transaction data with a three-year history, while credit card lending
algorithms utilize credit bureau data from January 2016 to July 2017. Our findings indicate
that random forests and neural networks significantly outperform logistic regression in
predictive power, as well as demonstrate an ability to process both structured and
unstructured data effectively.
We also analyze and compare risk management practices across banks and assess drivers of
delinquency across institutions. Our findings reveal substantial homogeneity across banks in
traditional risk features such as payment of interest, monthly payments, credit scores, and
loan-to-income ratios. Nevertheless, the product mix of a lender strongly influences data
availability, suggesting that no single model is likely to easily capture delinquency tendencies
across all institutions, product groups, and geographies. However, all institutions currently
focus on the relationship between income and total lending amount, indicating that parts of
the model could potentially be captured by a single cross-product, cross-geography model.
The results also indicate that portfolio characteristics alone are insufficient for identifying
drivers of delinquency, as banks actively manage their portfolios. Even nominally high-risk
portfolios may have fewer volatile delinquencies due to successful and active risk
management by the bank. Notably, the banks in the experiment are substantially
homogeneous in not yet applying external behavioral data, with only one experiment
incorporating social media as part of the credit model.
On the other hand, risk management practices exhibit heterogeneity across financial
institutions, with systemic implications. Mortgages and credit card receivables play a
significant role in modern asset-backed securities. An unexpected macroeconomic shock may
propagate through a greater delinquency rate of mortgages and credit cards issued by
financial institutions that less actively manage their portfolios in the asset-backed securities
market. Our study illustrates the potential benefits that advanced machine-learning
techniques, and the use of unstructured data, can bring to consumers in terms of a faster, more
predictive, and prescriptive customer experience. It also benefits risk managers by
113341

Artificial Intelligent Credit Risk Prediction - An Empirical Study of
Analytical Artificial Intelligence Tools for Credit Risk Prediction in a digital era
5.5 Discussion transitioning from expert-driven modeling to the digitalization of risk management through
more advanced artificial intelligent modeling and monitoring on internal and external data.
This research validated the hypothesis that advanced credit risk modeling methods Shareholders benefit from lower delinquencies, and regulators benefit from better control
outperform traditional logistic regression. In an era marked by rapid digital lending growth, over systematic credit risk. All stakeholders have a vested interest in avoiding unexpected
we argue that lenders should adopt these more accurate and predictive methods. Enhanced losses and reducing the cost of consumer credit.
individual risk assessments, limit setting, and pricing are crucial to reducing the risk of over-
lending. Moreover, when aggregated across several financial institutions, predictive analytics of
machine-learning models provide a practical means for measuring systemic risk in one of the
Additionally, as millennials drive a shift in customer experience expectations, advanced most important and vulnerable sectors of the economy. The AI models demonstrate higher
methods are particularly well-suited to support financial inclusion. Digitalization transforms accuracy and predictive power and the opportunity to scale risk models across product groups
borrowers into data agents, generating vast amounts of behavioral data that may reveal and geographies. Further research is needed to explore this scalability, promising substantial
unique risk indicators. New analytical methods are needed to make full use of this cost reductions and improved efficiencies in international risk management.
combination of structured and unstructured data. The global market for digital lending is
projected to grow at a Compound Annual Growth Rate (CAGR) of 26.6% through 2030, In this study, we develop random forest models for consumer credit delinquency, which
driven by its ability to target customers more effectively with timely offers, automate surprisingly demonstrate accuracy in forecasting credit events in three different experiments.
complex processes, and minimize manual interventions. Lenders can enhance their credit acquisition and credit management strategies with more
advanced machine learning. Traditional application data applied in machine learning models
In this study, we utilize a large dataset of anonymized information from three banks across already improves scorecard performance. As consumers and lenders become more digital and
different asset classes, such as mortgages and credit cards, in the United Kingdom and the mobile, incorporating behavioral data, both structured (e.g., payment data or credit card
Netherlands. This dataset allows us to test the added value of AI-based risk models in spending) and unstructured (e.g., search, sentiment, psychometrics, and mobile behavior),
predicting mortgage and credit card delinquency. Our mortgage lending algorithms have into these scorecards will further support sound onboarding and pricing strategies, reducing
access to consumer transaction data with a three-year history, while credit card lending mis-selling. Further research is needed in the area of alternative data for risk scoring, offering
algorithms utilize credit bureau data from January 2016 to July 2017. Our findings indicate breakthroughs in predictive model power and better control over financial risks.
that random forests and neural networks significantly outperform logistic regression in Anticipating higher growth in the lending market, especially in developing countries, there is
predictive power, as well as demonstrate an ability to process both structured and a need for improved, individual, and more effective risk assessments in lending bases.
unstructured data effectively. Regulators are enforcing lenders with stricter capital requirements and IFRS-9/CECL
compliance. Traditional logistic early warning systems assess loan portfolios based on
We also analyze and compare risk management practices across banks and assess drivers of historical behavior, while artificial intelligence offers lenders the opportunity to continually
delinquency across institutions. Our findings reveal substantial homogeneity across banks in monitor individual risk development based on structured and unstructured data. The high
traditional risk features such as payment of interest, monthly payments, credit scores, and predictive power of artificial intelligence presents opportunities for IFRS-9/CECL risk
loan-to-income ratios. Nevertheless, the product mix of a lender strongly influences data predictions and robotized solutions, contingent on the quality of underlying data. Lenders
availability, suggesting that no single model is likely to easily capture delinquency tendencies aiming to improve their risk prediction should consider collecting behavioral data from
across all institutions, product groups, and geographies. However, all institutions currently various sources for enhanced feature development.
focus on the relationship between income and total lending amount, indicating that parts of
the model could potentially be captured by a single cross-product, cross-geography model. Finally, machine learning services are offered by companies like Amazon, Microsoft, and
The results also indicate that portfolio characteristics alone are insufficient for identifying IBM. Fintech companies have flooded the markets with specific machine learning services in
drivers of delinquency, as banks actively manage their portfolios. Even nominally high-risk credit risk management. Companies such as AdviceRobo, Aire, EFL, and Lendoo operate
portfolios may have fewer volatile delinquencies due to successful and active risk their platforms internationally. This surge in machine learning services is expected to result in
management by the bank. Notably, the banks in the experiment are substantially significant cost reductions in manual labor and legacy systems of risk management,
homogeneous in not yet applying external behavioral data, with only one experiment supporting lenders' cost-to-income ratios. Risk robots are anticipated to bring high
incorporating social media as part of the credit model. effectiveness to risk management in the next 10 years, contingent on their ability to identify
and scale the best predictive features within new unstructured data. Successful credit robots
On the other hand, risk management practices exhibit heterogeneity across financial have the potential to reduce operational risk costs, such as collections and fraud fighting, on a
institutions, with systemic implications. Mortgages and credit card receivables play a large scale. Future research will further explore the benefits and challenges of robotization
significant role in modern asset-backed securities. An unexpected macroeconomic shock may and digitization in risk and marketing management.
propagate through a greater delinquency rate of mortgages and credit cards issued by
financial institutions that less actively manage their portfolios in the asset-backed securities
market. Our study illustrates the potential benefits that advanced machine-learning
techniques, and the use of unstructured data, can bring to consumers in terms of a faster, more
predictive, and prescriptive customer experience. It also benefits risk managers by
131 113325

Chapter 5
5.6 Limitations and future research
Limitations of this research center on the focus on two leading European credit markets.
Similar research should be performed in other geographies, especially in developing
countries. Secondly, the time frame of the experiments might bring bias. Although we could
work with three-year historical data, the market changes rapidly. We therefore advice to
repeat these experiments after a few years to understand the advancements in digitalization of
risk management better. Another limitation is the application of structured data in order to
make results comparable across models. Only in one experiment social media data was
applied. The application of external and unstructured data is also something that might evolve
over time. More research with the application of other data groups should be conducted to
understand the impact of unstructured behavioral data on risk scorecards.
Also, further research needs to be conducted into the scalability of artificial intelligent risk
models as the combined benefit of increased predictive power and higher international
efficiency in risk management is present. In the context of mortgage and credit card portfolio
risk management, there are account-specific costs and benefits associated with the
classification decisions that our performance statistics fail to capture. In the management of
existing lines of credit, the primary benefit of classifying bad accounts before they become
delinquent is to save the lender the run-up that is likely to occur between the current time
period and the time at which the borrower defaults. On the other hand, there are costs
associated with incorrectly classifying accounts. For example, the bank may alienate
customers and lose out on potential future business and profits on future purchases. This
research does not calculate the financial impact per bank, but primarily focuses on the
possibility of standardizing risk intelligence for the robotization of risk management.
113363

Artificial Intelligent Credit Risk Prediction - An Empirical Study of
Analytical Artificial Intelligence Tools for Credit Risk Prediction in a digital era
5.6 Limitations and future research References
Limitations of this research center on the focus on two leading European credit markets.
Similar research should be performed in other geographies, especially in developing Bank for international Settlements. (2024). https://www.bis.org/bcbs/basel3.htm
countries. Secondly, the time frame of the experiments might bring bias. Although we could
work with three-year historical data, the market changes rapidly. We therefore advice to Basel Committee. (2000). Principles for the management of credit risk. Basel Committee on
repeat these experiments after a few years to understand the advancements in digitalization of Banking Supervision.
risk management better. Another limitation is the application of structured data in order to
make results comparable across models. Only in one experiment social media data was Björkegren, D., & Grissen, D. (2018). Behavior revealed in mobile phone usage predicts loan
applied. The application of external and unstructured data is also something that might evolve repayment. Available at SSRN 2611775.
over time. More research with the application of other data groups should be conducted to
understand the impact of unstructured behavioral data on risk scorecards. Boz, E., & Mendoza, E. G. (2014). Financial innovation, the discovery of risk, and the US
credit crisis. Journal of Monetary Economics, 62, 1-22.
Also, further research needs to be conducted into the scalability of artificial intelligent risk
models as the combined benefit of increased predictive power and higher international Bradbury, T. (2014). Robo-advice is coming: What it means, who will buy it—and
efficiency in risk management is present. In the context of mortgage and credit card portfolio why. Professional Planner, 69, 40.
risk management, there are account-specific costs and benefits associated with the
classification decisions that our performance statistics fail to capture. In the management of Brown, K., & Moles, P. (2014). Credit risk management. Credit Risk Management, 16.
existing lines of credit, the primary benefit of classifying bad accounts before they become
delinquent is to save the lender the run-up that is likely to occur between the current time Butaru, F., Chen, Q., Clark, B., Das, S., Lo, A. W., & Siddique, A. (2016). Risk and risk
period and the time at which the borrower defaults. On the other hand, there are costs management in the credit card industry. Journal of Banking and Finance, 72, 218-239.
associated with incorrectly classifying accounts. For example, the bank may alienate
customers and lose out on potential future business and profits on future purchases. This Caruana, R., & Niculescu-Mizil, A. (2006). An empirical comparison of supervised learning
research does not calculate the financial impact per bank, but primarily focuses on the algorithms. In Proceedings of the 23rd International Conference on Machine Learning (pp.
possibility of standardizing risk intelligence for the robotization of risk management. 161-168). ACM.
Chaudhury, K., Garg, A., Phukan, P., & Saraf, A. (2011). U.S. Patent No.
7,986,843. Washington, DC: U.S. Patent and Trademark Office.
Choudhary, A., Raina, V., & Kumar, A. (2020). Millennials and Gen Z: Key drivers of digital
banking adoption. International Journal of Bank Marketing, 38(6), 1369-1384.
Chen, H., Chiang, R. H., & Storey, V. C. (2012). Business intelligence and analytics: From
big data to big impact. MIS Quarterly, 1165-1188.
Criminisi, A., Shotton, J., & Konukoglu, E. (2012). Decision forests: A unified framework for
classification, regression, density estimation, manifold learning, and semi-supervised
learning. Foundations and Trends® in Computer Graphics and Vision, 7(2–3), 81-227.
Derman, E. (1996). Model risk: What are the assumptions made in using models to value
securities and what are the consequent risks? Risk-London-Risk Magazine Limited, 9, 34-38.
di Patti, E. B., & Sette, E. (2016). Did the securitization market freeze affect bank lending
during the financial crisis? Evidence from a credit register. Journal of Financial
Intermediation, 25, 54-76.
Flood, M. D., Jagadish, H. V., & Raschid, L. (2016). Big data challenges and opportunities in
financial stability monitoring. Banque de France, Financial Stability Review, 20.
133 113347

Chapter 5
Halevy, A., Rajaraman, A., & Ordille, J. (2006). Data integration: The teenage years.
In Proceedings of the 32nd International Conference on Very Large Data Bases (pp. 9-16).
VLDB Endowment.
Hastie, T., Tibshirani, R., & Friedman, J. (2009). Unsupervised learning. In The Elements of
Statistical Learning (pp. 485-585). Springer.
Heilpern, E., Haslam, C., & Andersson, T. (2009, June). When it comes to the crunch: What
are the drivers of the US banking crisis?. In Accounting Forum (Vol. 33, No. 2, pp. 99-113).
IBM. (2012). Analytics: The real-world use of big data in financial services. IBM Institute of
Business Value.
International Monetary Fund (2024). Global debt database.
https://www.imf.org/external/datamapper/HH_LS@GDD/SWE
Kaplan, A., & Haenlein, M. (2019). Siri, Siri, in my hand: Who’s the fairest in the land? On
the interpretations, illustrations, and implications of artificial intelligence. Business Horizons,
62(1), 15-25.
Khandani, A. E., Kim, A. J., & Lo, A. W. (2010). Consumer credit-risk models via machine-
learning algorithms. Journal of Banking and Finance, 34(11), 2767-2787.
Mongo, D. B. (2016), Available at: https://redmonk.com/sogrady/2016/07/01/mongodb-atlas/.
Microsoft (2018) Available at: https://studio.azureml.net.
Mizen, P. (2008). The credit crunch of 2007-2008: A discussion of the background, market
reactions, and policy responses. Federal Reserve Bank of St. Louis Review, 90.
Njanike, K. (2009). The impact of effective credit risk management on bank survival. Annals
of the University of Petroşani, Economics, 9(2), 173-184.
O’Hara, M. (2015). High frequency market microstructure. Journal of Financial Economics,
116(2), 257-270.
Rajaraman, A., & Ullman, J. D. (2011). Mining of Massive Datasets.
Sobehart, J. R., Keenan, S. C., & Stein, R. (2000). Benchmarking quantitative default risk
models: A validation methodology. Moody’s Investors Service.
Stein, R. M. (2002). Benchmarking default prediction models: Pitfalls and remedies in model
validation. Moody’s KMV.
Van Thiel, D., & Van Raaij, F. (2017). Explaining customer experience of digital financial
advice. Economics, 5(1), 69-84.
Van Thiel, D., & Van Raaij, F. (2017). Targeting the robo-advice customer: The development
of a psychometric segmentation model for financial advice robots. Journal of Financial
Transformation, 46, 88-104.
113385

Artificial Intelligent Credit Risk Prediction - An Empirical Study of
Analytical Artificial Intelligence Tools for Credit Risk Prediction in a digital era
Halevy, A., Rajaraman, A., & Ordille, J. (2006). Data integration: The teenage years.
In Proceedings of the 32nd International Conference on Very Large Data Bases (pp. 9-16). Walker, E. (1996). Measurement, regression and calibration. Journal of the American
VLDB Endowment. Statistical Association, 91(433), 434-436.
Hastie, T., Tibshirani, R., & Friedman, J. (2009). Unsupervised learning. In The Elements of Witten, I. H., Frank, E., Hall, M. A., & Pal, C. J. (2016). Data mining: Practical machine
Statistical Learning (pp. 485-585). Springer. learning tools and techniques. Morgan Kaufmann.
Heilpern, E., Haslam, C., & Andersson, T. (2009, June). When it comes to the crunch: What Wu, X., Zhu, X., Wu, G. Q., & Ding, W. (2014). Data mining with big data. IEEE
are the drivers of the US banking crisis?. In Accounting Forum (Vol. 33, No. 2, pp. 99-113). Transactions on Knowledge and Data Engineering.
IBM. (2012). Analytics: The real-world use of big data in financial services. IBM Institute of Zhang, Y., Jia, H., Diao, Y., Hai, M., & Li, H. (2016). Research on credit scoring by fusing
Business Value. social media information in online peer-to-peer lending. Procedia Computer Science, 91,
168-174.
International Monetary Fund (2024). Global debt database.
https://www.imf.org/external/datamapper/HH_LS@GDD/SWE Zion Market Research. (2018) ‘Global digitization in lending’ , available at
https://www.zionmarketresearch.com/sample/digitization-in-lending-market
Kaplan, A., & Haenlein, M. (2019). Siri, Siri, in my hand: Who’s the fairest in the land? On
the interpretations, illustrations, and implications of artificial intelligence. Business Horizons,
62(1), 15-25.
Khandani, A. E., Kim, A. J., & Lo, A. W. (2010). Consumer credit-risk models via machine-
learning algorithms. Journal of Banking and Finance, 34(11), 2767-2787.
Mongo, D. B. (2016), Available at: https://redmonk.com/sogrady/2016/07/01/mongodb-atlas/.
Microsoft (2018) Available at: https://studio.azureml.net.
Mizen, P. (2008). The credit crunch of 2007-2008: A discussion of the background, market
reactions, and policy responses. Federal Reserve Bank of St. Louis Review, 90.
Njanike, K. (2009). The impact of effective credit risk management on bank survival. Annals
of the University of Petroşani, Economics, 9(2), 173-184.
O’Hara, M. (2015). High frequency market microstructure. Journal of Financial Economics,
116(2), 257-270.
Rajaraman, A., & Ullman, J. D. (2011). Mining of Massive Datasets.
Sobehart, J. R., Keenan, S. C., & Stein, R. (2000). Benchmarking quantitative default risk
models: A validation methodology. Moody’s Investors Service.
Stein, R. M. (2002). Benchmarking default prediction models: Pitfalls and remedies in model
validation. Moody’s KMV.
Van Thiel, D., & Van Raaij, F. (2017). Explaining customer experience of digital financial
advice. Economics, 5(1), 69-84.
Van Thiel, D., & Van Raaij, F. (2017). Targeting the robo-advice customer: The development
of a psychometric segmentation model for financial advice robots. Journal of Financial
Transformation, 46, 88-104.
135 113369

Chapter 5
With insights from personality-and AI-driven credit assessments, we now turn to the role
of psychometrics in small business credit risk decision making, particularly for
underserved groups like small businesses and sole traders. This chapter examines how a
novel psychometric credit scoring approach can provide these entities with better access to
credit by enhancing risk assessments, enabling financial institutions to make more informed
and inclusive lending decisions. This focus underscores psychometric’s inclusive potential to
empower traditionally overlooked segments of the market.
114307

Chapter 6
With insights from personality-and AI-driven credit assessments, we now turn to the role
of psychometrics in small business credit risk decision making, particularly for
underserved groups like small businesses and sole traders. This chapter examines how a
novel psychometric credit scoring approach can provide these entities with better access to
credit by enhancing risk assessments, enabling financial institutions to make more informed
and inclusive lending decisions. This focus underscores psychometric’s inclusive potential to
empower traditionally overlooked segments of the market.
Responsible Access to Credit for Sole-Traders
and Micro-organizations under Unstable Market
Conditions with Psychometrics
Submitted to:
Van Thiel, D., Elliott, K., Goedee, J., & Leenders, R.
Responsible Access to Credit for Sole-Traders and Micro-organizations
under Unstable Market Conditions with Psychometrics
The European Journal of Finance, 2024
137

Chapter 6
ABSTRACT
In a context of market volatility, the growing complexity of financial products, and a shift
towards self-employment, there is an increasing demand for inclusive financial services for
sole traders and micro-organizations. To address this need, we conducted a study using real-
time data from a Fintech lender in the Czech Republic to assess the effectiveness of a new
financial literacy based psychometric credit scoring model (PSM) in improving access to
finance for micro, small and medium sized enterprises (MSME) sector, particularly sole
traders, and micro-organizations, during volatile market conditions. This study affirms that
PSMs play a significant role in responsibly including this underserved sector. Specifically, we
observed a 30% higher approval rate and a 23% lower default rate when utilizing the PSM
versus the traditional credit scoring model (TCSM). Moreover, during the period of
substantial market volatility and instability, such as the state-of-emergency during the
COVID-19 pandemic, the PSM exhibited a 13% higher approval rate at a 20% lower default
rate than the TCSM. This evidence supports the proposition that PSMs offer a viable option
for promoting financial inclusion and targeted financial education among MSMEs in the face
of unstable financial markets.
Keywords: Small Business Lending, Financial inclusion, Innovative Credit Scoring, COVID-
Pandemic, Psychometrics
6.1 Introduction
Micro, small and medium-sized enterprises (MSMEs) play an exclusive role and prominence
in the world economy, wherein global prosperity is anchored on the continued growth of a
thriving MSME sector (Rao et al., 2023). The Organisation for Economic Cooperation and
Development (OECD) categorizes MSMEs into micro-enterprises, including sole traders or
self-employed (fewer than 10 employees), small enterprises (10 to 49 employees) and
medium-sized enterprises (50 to 249 employees) (OECD, 2023). Moreover, MSMEs can
provide substantial contributions toward the United Nations Sustainable Development Goals
(SDGs) through employment generation, sustainable industrialization, innovation nurturing,
and income disparity reduction (Šebestová & Sroka, 2020). SDGs are crucial aspirations and
endeavours while sustaining MSMEs and improving their financial performance (Bartolacci
et al., 2020). Likewise, MSMEs constitute 90% of the world’s economy and create 60% to
70% of employment and 55% of GDP and drive inclusion, which highlights MSMEs
continued importance as drivers of economic growth and development now, and in the future
(The World Trade Report, 2016, 2023: 63, 66). Despite these statistical reports and
contributions, MSMEs face multiple challenges and constraints to survive during periods of
volatility (ibid: 2023: 66). Extant literature reveals that access to finance is one of the most, if
not the most, pressing issue that currently hinders MSMEs growth trajectories (Rao et al.,
2023; Gupta, 2018; Ang, 1991, 1992; Baker et al., 2020; Carpenter & Petersen, 2002;
Chittenden et al., 1996; Hughes, 1997; Gibson, 1992; Guariglia et al., 2011; Hall &
Hutchinson, 1993; Hamilton & Fox, 1998; Hutchinson & Xavier, 2006; Jordan et al., 1998;
Lopez-Gracia & Aybar-Arias, 2000; Moscalu et al., 2020; Robson & Bennet, 2000).
In addition, the digital transformation of financial services via digital technologies (machine
learning and artificial intelligence) can be leveraged to help increase financial access and
broaden inclusion. For instance, Open Banking (OB) tools via Application Programming
Interfaces (APIs) enable data sharing and functionality to literally ‘open’ the market place and
increase consumers and entrepreneurs ability to compare and select preferred product and
114329

Responsible Access to Credit for Sole-Traders and
Micro-organizations under Unstable Market Conditions with Psychometrics
ABSTRACT service offers (e.g., OECD 2018). McKinsey (2017) espouse that OB may facilitate benefits
and encourage sustainable service models, particularly for underserved markets, such as
In a context of market volatility, the growing complexity of financial products, and a shift MSMEs (Long et al., 2020).
towards self-employment, there is an increasing demand for inclusive financial services for
sole traders and micro-organizations. To address this need, we conducted a study using real- The range of OB data sources moves beyond banking data to public data¾images from
time data from a Fintech lender in the Czech Republic to assess the effectiveness of a new satellites, company data, social media, and messenger services. Thus, interactional big
financial literacy based psychometric credit scoring model (PSM) in improving access to datasets permit creating an arbitrary profile of the consumer using artificial intelligence (AI)
finance for micro, small and medium sized enterprises (MSME) sector, particularly sole (Mhlanga, 2021). These profiles assist lenders in assessing the general behaviours of
traders, and micro-organizations, during volatile market conditions. This study affirms that applicants and verify the probability of potential borrowers defaulting on a loan repayment, in
PSMs play a significant role in responsibly including this underserved sector. Specifically, we essence reducing the lender’s risk in granting loans (Biallas & O’Neill, 2020). Research
observed a 30% higher approval rate and a 23% lower default rate when utilizing the PSM supports OB-based payment models (Rishabh, 2022); mobile phone data (Liu et al, 2017;
versus the traditional credit scoring model (TCSM). Moreover, during the period of Oskarsdottir et al, 2019; San Pedro et al, 2015; Shema 2019) and social media data (Tan &
substantial market volatility and instability, such as the state-of-emergency during the Phan 2018; Wei et al, 2016; Yuan et al, 2018; Zhang et al, 2016) in producing higher
COVID-19 pandemic, the PSM exhibited a 13% higher approval rate at a 20% lower default predictive credit performance and repayment likelihood compared to traditional credit scoring
rate than the TCSM. This evidence supports the proposition that PSMs offer a viable option models (TCSMs).
for promoting financial inclusion and targeted financial education among MSMEs in the face
of unstable financial markets. This obvious, but overlooked data emanates from established psychometric models, affording
insights into an individual’s skills, abilities, personality traits, attributes, competencies, and
Keywords: Small Business Lending, Financial inclusion, Innovative Credit Scoring, COVID- intelligence levels. Such attributes have been linked to predicting human behaviour¾crucial
Pandemic, Psychometrics in assessing credit worthiness and predicting default behaviours which could lead to an
accrual of arrears for lenders, therefore, predicting an applicant’s propensity to default on
repayments (Goel and Rastogi, 2023; Arraiz et al. 2017; Aitken 2017; Djeundje et al. 2021;
Klinger 2013). The use of psychometric data to predict financial behaviour, is not new,
6.1 Introduction however, a holistic but granular financial behavioural approach for responsible lending to
Micro, small and medium-sized enterprises (MSMEs) play an exclusive role and prominence MSMEs during period of market instability is missing (Bernards 2019).
in the world economy, wherein global prosperity is anchored on the continued growth of a
thriving MSME sector (Rao et al., 2023). The Organisation for Economic Cooperation and Small businesses face a liability of ‘smallness’, thus, when crises create volatility and
Development (OECD) categorizes MSMEs into micro-enterprises, including sole traders or unstable market conditions, resource, and liquidity contracts to stifle MSMEs access to
self-employed (fewer than 10 employees), small enterprises (10 to 49 employees) and finance and therefore, growth (Eggers, 2020). The situation is compounded by consumer
medium-sized enterprises (50 to 249 employees) (OECD, 2023). Moreover, MSMEs can market contraction as spending reduces, and financiers become more risk averse in their
provide substantial contributions toward the United Nations Sustainable Development Goals investment and lending protocols (ibid.). For example, the lingering effects of the global
(SDGs) through employment generation, sustainable industrialization, innovation nurturing, financial crisis (GFC, 2008-9), combined with persistent financial instability and emergent
and income disparity reduction (Šebestová & Sroka, 2020). SDGs are crucial aspirations and economic crises, diffused risk in credit markets, impacts the levels of job creation and income
endeavours while sustaining MSMEs and improving their financial performance (Bartolacci security in many OECD economies (Bakthiari et al., 2020). Smaller FS/FinTech businesses
et al., 2020). Likewise, MSMEs constitute 90% of the world’s economy and create 60% to bear the brunt, as the marketplace contracts through mergers into larger enterprises or even
70% of employment and 55% of GDP and drive inclusion, which highlights MSMEs their disappearance. This could potentially lead to greater market concentration among larger
continued importance as drivers of economic growth and development now, and in the future businesses in the FS/FinTech sector (see The World Trade Report, 2023: 66).
(The World Trade Report, 2016, 2023: 63, 66). Despite these statistical reports and
contributions, MSMEs face multiple challenges and constraints to survive during periods of Simultaneously, digital transformation has changed workforce structures from traditional- to
volatility (ibid: 2023: 66). Extant literature reveals that access to finance is one of the most, if self-employment following the 2008 recession (Struckell, 2018), and the recent pandemic,
not the most, pressing issue that currently hinders MSMEs growth trajectories (Rao et al., disrupting the traditional employee-employer relationship (Robison, 2013), paving the way
2023; Gupta, 2018; Ang, 1991, 1992; Baker et al., 2020; Carpenter & Petersen, 2002; for the digital and gig economies to emerge (Istrate & Harris, 2017). Consequently, the
Chittenden et al., 1996; Hughes, 1997; Gibson, 1992; Guariglia et al., 2011; Hall & MSME sector has witnessed rapid growth and demand for digital freelancers and gig
Hutchinson, 1993; Hamilton & Fox, 1998; Hutchinson & Xavier, 2006; Jordan et al., 1998; workers, anticipated to surpass traditional employment by 2027 (Pew, 2019; Kassi &
Lopez-Gracia & Aybar-Arias, 2000; Moscalu et al., 2020; Robson & Bennet, 2000). Lehdonvirta, 2018). This seismic shift away from traditional employment is driven by 46% of
In addition, the digital transformation of financial services via digital technologies (machine Generation Z (born 1996-2012) members preferring the flexibility of independent work
learning and artificial intelligence) can be leveraged to help increase financial access and (Upwork, 2023). At the other end of the generational spectrum, the ‘baby boomers’ (born
broaden inclusion. For instance, Open Banking (OB) tools via Application Programming 1946-1964) are increasingly turning to self-employment as a transition to, and means of
Interfaces (APIs) enable data sharing and functionality to literally ‘open’ the market place and funding their retirement (Robison, 2013; Pew, 2019). If this sector is unable to access finance,
increase consumers and entrepreneurs ability to compare and select preferred product and the sector will be monopolised by larger organisations and create the reverse of inclusion.
139 114403

Chapter 6
Previous research supports this observation, that the access to finance gap widens for sole
traders and micro-organizations, when applying for bank loans, venture capital, and
government support during economic volatility (Demeril & Parris, 2015). In summary, while
FinTech has accelerated financial inclusion, the key customer base centres on small
borrowers, most affected by market instability. We have chosen a FinTech lender to test our
novel PSM solution to assess bridging the access to finance gap utilizing data from a Czech
(CZ) FinTech lender during market instability (e.g., COVID-19).
CZ was selected as a representative EU country based on several factors: i) Gross Domestic
Product (GDP) to debt ratio, ii) levels of digital technological innovation, readiness and
adoption, iii) an identified 50% access to finance gap for small businesses that shares
similarities with comparable EU countries and the UK (WBES, 2023), and iv) CZ is a
technologically advanced Eastern European country and ranks among the world’s most
innovative countries (Hlomane, 2022). Alternative lending leveraging digital technologies are
suggested as a viable solution for closing the access to finance gap for small businesses per se
(Mhlanga, 2021, Sahah et al. 2020). Thus, CZ proffers an ideal testbed to explore the use of
our PSM solution. Our central research question therefore specifically, asks:
"To what extent can psychometric credit scoring models predict the likelihood of arrears, and
increase access to finance for micro-organizations and sole traders during market
instability?”
This paper makes three contributions to the field of PSMs, utilizing FS/FinTech innovation to
facilitate financial inclusion for small businesses and their associated lenders. First, despite
attention towards the value of PSMs for small business lending, ours is the first that
counterfactually explores the stability of a PSM during a period of high macro-economic
instability. Second, at the time of writing, this study is the first to consider the European
lending sector. Finally, where prior studies have applied small back-test experiments (e.g.,
use of traditional financial data sources (Klinger 2013)) for probability of default testing, we
employ dynamic near real-time psychometric and financial data from a CZ-based FS/FinTech
firm (August 2019-February 2022) to not only assess the validity of the PSM for
incorporation in both FS/FinTech and mainstream credit scoring procedures for probability of
default testing, but translate the results into profit impact of lenders.
This remainder of this paper is structured as follows. Section 2 illustrates the context,
concepts, and components underpinning the PSM and builds our hypotheses. Section 3
describes the empirical methodology and methods employed in developing the PSM, the
subsequent CZ sample and variables used to further test and validate the model. Section 4
presents and discusses the main results including discussing our hypotheses. Section 5
concludes our study, providing closing remarks and examines the PSM in relation to extant
literature. Section 6 discusses research limitations and insights for FinTech practitioners to
consider while offering new PSM research avenues to pursue.
114441

Responsible Access to Credit for Sole-Traders and
Micro-organizations under Unstable Market Conditions with Psychometrics
6.2 Literature review
6.2.1. Credit scoring classification: a historical perspective
Since the mid-20th century, both researchers and practitioners have emphasised developing
empirical models that assist retail lenders to engage in responsible practices, offering
affordable credit to consumers and businesses. Today, commercial banks retain billions in
capital via consumer loans and the consumer credit sector are now of substantial economic
importance to the global economy. The large volume of loans illustrates that incremental
improvements in the accuracy of credit scoring models can result in considerable financial
gains for lenders and consumers. Hence, developing accurate credit scoring models is a major
priority for financial institutions to optimize profits while effectively managing exposure to
lending risk (Baesens, et al., 2003, Jiang, et al., 2019, Lessmann, et al., 2015, Luo, et al.,
2017, Thomas, et al., 2002). Historically, managers evaluated an applicant’s creditworthiness
based on their intuitive experience. However, with the support of empirical models, managers
can now evaluate credit applicants efficiently, consistently, and accurately. Consequently,
attention has been paid to empirical credit scoring (cf. prior citations), resulting in several
techniques, referred to as credit scoring models (CSMs). CSMs classify credit applicants into
a dichotomous group of ‘good’ or ‘bad’ applicants, indicating their respective likelihood of
repaying or defaulting on a loan agreement. Credit scoring problems can be positioned within
the scope of the more widely discussed classification issues and bias reducing access to credit
for applicants (Akkoç, 2012, Baesens, Roesch, Scheule, 2016, Saberi, Mirtalaie, Hussain,
Azadeh, Hussain, Ashjari, 2013, Verbraken, Bravo, Weber, Baesens, 2014). The emergence of
machine learning and sophisticated classification techniques, such as neural networks,
support vector machines and random forests classifiers has led to extensive benchmarking
studies aimed at improving CSMs statistical performance and accuracy (Oskarsdottir et.al,
2019). Lessmann et al. (2015), concludes that multiple studies found that traditional credit
scoring models (TCSMs) based on simple logistic regression models, performed very well
and newer classification techniques offer marginal performance gains. Among statistical
techniques, Multivariate discriminant analysis (MDA) (Altman, 1968; Fisher, 1936) and
logistic regression (LR) (Baesens et al., 2003; Wiginton, 1980) are two popular methods,
because they are easy to implement and interpret (Xiao, Xiao, & Wang, 2016). However,
limitations emerge in application, because the data should be linear separable and strictly
follow certain distribution. Whereas, AI techniques, such as k-nearest neighbours (KNN)
(Henley & Hand, 1996), genetic algorithm (GA) (Ong, Huang, & Tzeng, 2005), support
vector machines (SVM) (Huang, Chen, & Wang, 2007), decision trees (DT) (Wang et al.,
2012), random forest (RF) (Malekipirbazari & Aksakalli, 2015; Van Thiel & Van Raaij, 2019)
and artificial neural network (ANN) (Lee & Chen, 2005) now provide alternatives to prior
statistical techniques based on improved performance. This is achieved via the combination
of individual classifiers and ensemble models for credit scoring application, which perform
better than individual classifiers in accuracy and stability and are now mainstream for CSMs.
The digitization of credit eliminates the traditional ability of lenders to evaluate a borrower's
personality. Consequently, a common drawback of all Credit Scoring Models (CSMs) is their
inability to quantify the importance of the borrower's character. Among the ‘six Cs’ of
granting credit criterion¾ Condition, Collateral, Credit, Character, Capacity and Currency,
the assessment of the most crucial ‘C’, namely, the borrower’s character, remains
questionable, inadequately considered, and measured to evaluate an applicant’s
creditworthiness (Capon 1982). We argue that to enhance Credit Scoring Models (CSMs), the
solution lies in adopting advanced classification techniques and, even more crucially, in
harnessing innovative big data sources like psychometrics to incorporate the borrower's
114425

Chapter 6
character traits as evaluation criteria in both traditional and contemporary classification emotional stability, openness to experience and integrity in defaulting behaviour of micro-
methods. This approach can lead to the development of comprehensive credit scoring models. entrepreneurs (Tupes & Christal, 1992). Findings reported an AUC of 0.67, signifying
Traditional credit scoring models (TCSMs) predominantly rely on demographic and financial acceptable levels of discriminatory model power including psychometric predictors and
data, creating limitations for assessing the creditworthiness of MSMEs and specifically, sole concluded that psychometrics created additional predictive power for identifying defaulting
traders and micro-organizations. As a result, TCSMs are undergoing rapid transformations to traits of MSME entrepreneurs. Such studies combined psychometric covariates with
broaden financial inclusion via access to finance (Goel & Rastogi, 2023). Recent innovations traditional financial variables like business credit history, financial statements, business
include adopting alternative variables, such as the borrower’s social media data (Hendricks assets, market conditions and a business plan. Nevertheless, while some studies indicate that
and Budree, 2019; De Cnudde et al., 2019), utility data (Djeundje et al., 2021), mobile phone there is no advantage in incorporating psychometric measures with established target
data (Agarwal et al., 2020), psychometric data (Klinger, 2013, Azma et al., 2019, Van Thiel at segments, the majority contend that psychometrics can improve the prediction of default risk,
al., 2023) and so on. The idea behind utilizing open and alternative data sets is to serve particularly for underbanked customer segments such as small businesses.
underbanked sectors and populations who face financial constraints due failing to meet the Recent research has supported the inclusion of behavioural traits and attitudes to substantially
‘Know your Customer’ (KYC) financial data requirements to verify customer identity (Elliott influence financial behaviour (Liberati & Camillo, 2018). The authors extracted six
et al., 2022). Such studies have shown that credit scoring is not limited to demographic and psychological constructs from responses to a questionnaire administered by an Italian bank.
economic variables, other variables can be explored that increase the accuracy in predicting These were i) preference for advice, ii) duty/pleasure, iii) attachment/detachment, iv)
the default traits of borrowers. A systematic literature review examining CSMs suggests that sublimation/materialism, v) idealisation/pragmatism, and vi) humility/sovereignty scale
a minimal number of articles have considered alternative variables to assess the borrower’s items. The study showed that when these constructs are integrated with TCSMs to assess
creditworthiness (Onay & Ozturk, 2018). For the above reasons, and drawing on theoretical access to banking services, cash flow, and creating a solvency score, the AUC increased
insights from psychometrics in identifying the stable ‘character traits’ of sole traders and considerably, from 0.554 to 0.850 indicating excellent discrimination effect of the model.
micro- business entrepreneurs to inform CSMs, our core research hypothesis is: Likewise, a PSM trained on a dataset from a pilot study with a Mexican bank included
psychometric variables and produced an AUC of 0.6 (acceptable discrimination) indicating
H1. Psychometric credit scoring models increase responsible access to finance for small that the inclusion of defined psychometric attributes has the potential to improve the accuracy
businesses in unstable market conditions. of TCSMs prediction capabilities (Djeundje et al., 2021).
6.2.2. Psychometric credit scoring Reflecting on the somewhat conflicting findings and design omissions regarding undefined
Extant psychometric literature suggests variables and constructs that could assist in psychometric variables in the literature, the next section presents and justifies the variable
improving the accuracy of OB data for AI-enabled credit scoring models. To explain, the selection for our psychometric scoring model (PSM), tested in CZ.
human trait of impatience is found to be correlated with defaulting behaviours (Meier & Within the next decade, the current levels of self-employed workers, is predicted to surpass
Sprenger, 2007). Similarly, sixty-six psychometric variables (not defined in the study) were that of traditional employees. Managing finances (financial literacy) is therefore an important
applied to data relating to credit applicants from MSMEs in Peru (N=275), to establish skill set for self-employed workers to attain (Struckell et al., 2022). To understand the role
psychological traits linked to the repayment traits an Area Under the Curve (AUC) measure that financial literacy plays in MSME entrepreneurs obtaining credit, we create a novel
of 0.7 was reported, indicating excellent levels of discriminatory model power (Klinger et al. psychometric credit scoring model (PSM), providing predictive financial behavioural insights
2013, Goel & Ratogi 2023, see methodology section for AUC description). To test the for the current generation of self-employed entrepreneurs, during unstable market conditions.
resultant default model premised on psychological constructs, the authors estimated a similar
model with data from four African countries¾Kenya, South Africa, Ghana, and Nigeria, and
the prior Peruvian data set. The findings reported an AUC of 0.56-0.58 in relation to an
average default period of ≥ 60 days which indicates low model discrimination effects and
limits the usability of the model for these data sets. Furthermore, the lack of clarity regarding
which sixty-six variables applied to the two data sets raises questions of internal and external
validity to warrant replicating the protocol for this study.
This problematic trend of psychometric variables within the literature providing interesting
insights but failing to define which variables were tested is reflected in Arraiz et al., (2017).
The authors used a larger sample (N=1993) investigating psychometric variables integrated
into TCSMs and concluded that psychometric models’ predictive capabilities for repayment
or default proved worse in rejecting applicants in contrast to traditional models alone. A
limitation emerges in terms of sample which contained banked entrepreneurs and excluded
underbanked entrepreneurs. For financial inclusion of this latter group and facilitating their
access to finance, data relating to micro-entrepreneurs in Kenya was explored from a
psychometric perspective (Dlogosch et al., 2017). The psychometric variables were based on
the ‘big five’ psychometric model constructs to measure the role of conscientiousness,
114463 144

Responsible Access to Credit for Sole-Traders and
Micro-organizations under Unstable Market Conditions with Psychometrics
character traits as evaluation criteria in both traditional and contemporary classification emotional stability, openness to experience and integrity in defaulting behaviour of micro-
methods. This approach can lead to the development of comprehensive credit scoring models. entrepreneurs (Tupes & Christal, 1992). Findings reported an AUC of 0.67, signifying
Traditional credit scoring models (TCSMs) predominantly rely on demographic and financial acceptable levels of discriminatory model power including psychometric predictors and
data, creating limitations for assessing the creditworthiness of MSMEs and specifically, sole concluded that psychometrics created additional predictive power for identifying defaulting
traders and micro-organizations. As a result, TCSMs are undergoing rapid transformations to traits of MSME entrepreneurs. Such studies combined psychometric covariates with
broaden financial inclusion via access to finance (Goel & Rastogi, 2023). Recent innovations traditional financial variables like business credit history, financial statements, business
include adopting alternative variables, such as the borrower’s social media data (Hendricks assets, market conditions and a business plan. Nevertheless, while some studies indicate that
and Budree, 2019; De Cnudde et al., 2019), utility data (Djeundje et al., 2021), mobile phone there is no advantage in incorporating psychometric measures with established target
data (Agarwal et al., 2020), psychometric data (Klinger, 2013, Azma et al., 2019, Van Thiel at segments, the majority contend that psychometrics can improve the prediction of default risk,
al., 2023) and so on. The idea behind utilizing open and alternative data sets is to serve particularly for underbanked customer segments such as small businesses.
underbanked sectors and populations who face financial constraints due failing to meet the Recent research has supported the inclusion of behavioural traits and attitudes to substantially
‘Know your Customer’ (KYC) financial data requirements to verify customer identity (Elliott influence financial behaviour (Liberati & Camillo, 2018). The authors extracted six
et al., 2022). Such studies have shown that credit scoring is not limited to demographic and psychological constructs from responses to a questionnaire administered by an Italian bank.
economic variables, other variables can be explored that increase the accuracy in predicting These were i) preference for advice, ii) duty/pleasure, iii) attachment/detachment, iv)
the default traits of borrowers. A systematic literature review examining CSMs suggests that sublimation/materialism, v) idealisation/pragmatism, and vi) humility/sovereignty scale
a minimal number of articles have considered alternative variables to assess the borrower’s items. The study showed that when these constructs are integrated with TCSMs to assess
creditworthiness (Onay & Ozturk, 2018). For the above reasons, and drawing on theoretical access to banking services, cash flow, and creating a solvency score, the AUC increased
insights from psychometrics in identifying the stable ‘character traits’ of sole traders and considerably, from 0.554 to 0.850 indicating excellent discrimination effect of the model.
micro- business entrepreneurs to inform CSMs, our core research hypothesis is: Likewise, a PSM trained on a dataset from a pilot study with a Mexican bank included
psychometric variables and produced an AUC of 0.6 (acceptable discrimination) indicating
H1. Psychometric credit scoring models increase responsible access to finance for small that the inclusion of defined psychometric attributes has the potential to improve the accuracy
businesses in unstable market conditions. of TCSMs prediction capabilities (Djeundje et al., 2021).
6.2.2. Psychometric credit scoring Reflecting on the somewhat conflicting findings and design omissions regarding undefined
Extant psychometric literature suggests variables and constructs that could assist in psychometric variables in the literature, the next section presents and justifies the variable
improving the accuracy of OB data for AI-enabled credit scoring models. To explain, the selection for our psychometric scoring model (PSM), tested in CZ.
human trait of impatience is found to be correlated with defaulting behaviours (Meier & Within the next decade, the current levels of self-employed workers, is predicted to surpass
Sprenger, 2007). Similarly, sixty-six psychometric variables (not defined in the study) were that of traditional employees. Managing finances (financial literacy) is therefore an important
applied to data relating to credit applicants from MSMEs in Peru (N=275), to establish skill set for self-employed workers to attain (Struckell et al., 2022). To understand the role
psychological traits linked to the repayment traits an Area Under the Curve (AUC) measure that financial literacy plays in MSME entrepreneurs obtaining credit, we create a novel
of 0.7 was reported, indicating excellent levels of discriminatory model power (Klinger et al. psychometric credit scoring model (PSM), providing predictive financial behavioural insights
2013, Goel & Ratogi 2023, see methodology section for AUC description). To test the for the current generation of self-employed entrepreneurs, during unstable market conditions.
resultant default model premised on psychological constructs, the authors estimated a similar
model with data from four African countries¾Kenya, South Africa, Ghana, and Nigeria, and
the prior Peruvian data set. The findings reported an AUC of 0.56-0.58 in relation to an
average default period of ≥ 60 days which indicates low model discrimination effects and
limits the usability of the model for these data sets. Furthermore, the lack of clarity regarding
which sixty-six variables applied to the two data sets raises questions of internal and external
validity to warrant replicating the protocol for this study.
This problematic trend of psychometric variables within the literature providing interesting
insights but failing to define which variables were tested is reflected in Arraiz et al., (2017).
The authors used a larger sample (N=1993) investigating psychometric variables integrated
into TCSMs and concluded that psychometric models’ predictive capabilities for repayment
or default proved worse in rejecting applicants in contrast to traditional models alone. A
limitation emerges in terms of sample which contained banked entrepreneurs and excluded
underbanked entrepreneurs. For financial inclusion of this latter group and facilitating their
access to finance, data relating to micro-entrepreneurs in Kenya was explored from a
psychometric perspective (Dlogosch et al., 2017). The psychometric variables were based on
the ‘big five’ psychometric model constructs to measure the role of conscientiousness,
143 114447

Chapter 6
Figure 1
Conceptual PSM attributes with their hypothesized relationships with arrears (overdue
payments)
Our psychometric credit scoring model (PSM), centres on the importance of financial literacy
reflecting global recognition of a skills gap in this area (Lussardi & Mitchell 2007, 2008,
2011; Lussardi et al. 2021). Financial literacy is defined as follows: "[Financial literacy is]
the knowledge and understanding of financial concepts and risks, and the skills, motivation,
and confidence to apply such knowledge and understanding in order to make effective
decisions across a range of financial contexts, to improve the financial well-being of
individuals and society, and to enable participation in economic life" (OECD, 2012).
Between 2009-2019, more than 500 peer-reviewed articles on financial literacy were
published (Goyal & Kumar, 2021). To inform the PSM in predicting loan repayment
behaviours, we analyzed this body of research to understand financial literacy attributes that
influence financial behavioral traits. We concluded that consumers' ability to make informed
financial decisions translates into enhanced personal financial behaviors (Lusardi et al., 2021;
Klapper & Lusardi 2020; Lusardi, 2019).
Currently, demand for access to affordable credit is increasing, especially in relation to
superannuation (pensions), increasing consumer longevity, and the lasting impacts of
financial crises. MSMEs are seeking credit to expand and drive economic recovery post-
pandemic (Dasewicz et al., 2020; Bocanet et al., 2021). This heightened demand underscores
the importance of promoting and supporting proficient financial literacy (FL) skills as a
fundamental prerequisite for individuals and society. Such skills are crucial for optimizing
financial decisions and safeguarding against financial scams, fraud, and exploitation in
today's digitalized financial landscape (Goyal & Kumar, 2021).
114485

Responsible Access to Credit for Sole-Traders and
Micro-organizations under Unstable Market Conditions with Psychometrics
Building upon the OECD's definition, the PSM has a strong emphasis on assessing the
creditworthiness of vulnerable consumer sectors including MSME entrepreneurs (Van Thiel
et al., 2023). Building on our previous work by refining and enhancing the PSM framework
for MSMEs, illustrated in Figure 1 below, the updated framework incorporates relevant
attributes for measuring personality traits associated with financial literacy among
entrepreneurs. Consequently, the PSM model, informed by an exploration of existing
psychological literature, has revealed relationships between constructs of financial
personality, financial behavior, literacy, and debt. This enables us to hypothetically classify
MSME credit applicants into categories of 'good' and 'bad' payment behaviors. The PSM
model has confirmed hypotheses of positive correlations between gratification, materialism,
debt attitude, confidence, social desirability, and debt, as well as a negative correlation
between financial skills, age, and debt accumulation (ibid.). In the following sections, we
provide a detailed exploration of the model’s attributes.
6.2.2.1. Financial skills
In their extensive financial literacy research (Lussardi & Mitchel, 2007, 2008, 2011), it is
suggested that financial skills (FSs) drive financial literacy by encompassing capabilities
associated with money management, including budgeting and expense tracking. Other
research argues that better FSs are associated with possessing higher savings and lower debt
(Dew & Xiao, 2011; Moore 2003). Hence, those with a paucity of FL or FSs (or a
combination) are financially vulnerable customers, defined in the recent Financial Conduct
Authorities (FCA, 2019-2022) work in this topic and consequently suffer severe financial
problems. We therefore hypothesize the following:
H0a: Lower levels of financial skills (FL/FSs) increases arrears.
6.2.2.2. Financial self-efficacy
The FL literature revealed the construct of self-efficacy as an aspect of FL, FSs, and
behaviour. Financial self-efficacy, based on Bandura’s (1986) social cognitive theory, refers
to a person's confidence in managing their own finances, in acting with certainty premised
on knowledge accumulation. Support is found for financial self-efficacy as vital in translating
financial literacy into financial behaviour (Dans & Haberman, 2007). Financial confidence
(aka self-efficacy) and skills required to apply financial knowledge are the key psychological
tenets that underpin the transition from knowledge into behaviour. A caveat is that financial
self-efficacy can also lead to risky financial behaviour. Debt-related research reveals that
students get into deeper debt because they overestimate how much they will earn post-
graduation (Seaward & Kemp, 2000). Similarly, consumer cohorts are shown more likely to
obtain a new credit card if they perceive repayment as easy (Yang, et al., 2007). Simply put,
consumers take higher risks because they are overconfident in their perceived abilities to
manage financial matters (Nosić & Weber, 2010). We examine the differing types of attitudes
such as positive, neutral, and negative in relation to whether this impacts accrual of arrears.
Therefore, we hypothesize the following:
H0b: Higher levels of self-efficacy (confidence) increases arrears.
114469

Chapter 6
6.2.2.3. Debt attitudes
Associated with FL is the construct of financial attitude. Research has explored student and
household debt, highlighting that more positive attitudes toward debt are associated with
accruing more debt (Almenberg et. al, 2020; Haultain, Kemp & Chernyshenko, 2010).
Studies state that there were two different types of attitudes associated with debt. On the one
hand, fear of debt was associated with less debt, whereas seeing the utility of debt was
associated with higher debt. We argue that vulnerable customers with positive attitudes
toward debt face a high risk of indebtedness, consequently exacerbating payment difficulties.
We therefore hypothesize the following:
H0c: Positive debt attitudes increase arrears.
6.2.2.4. Materialism
Part of the psychological constructs model includes the impact of personal factors on
financial literacy and financial behaviour. Evidence showed that debt attitude (as discussed)
has a consistent relationship with materialistic value, where materialism is conceptualized as
the extent to which people value the acquisition and consumption of material objects
(Norvilitis et.al, 2006; Garðarsdóttir & Dittmar 2012). Materialism reflects the prime
importance an individual affords to possessions, whereby the acquisition of goods is a central
objective and symbolic of perceived positivity, success, and (psychological) happiness for the
individual (Belk, 1984; Richins and Dawson, 1992; Richins, 2017, 2011). Materialism can
create negative consequences, such as a propensity to regularly overspend (Khare, 2014;
Donnelly et al., 2012) in the pursuit of luxurious purchases and non-essential items (Watson,
2003), thus, accruing higher debt. Furthermore, materialistic traits have been shown to be
associated with poor financial management skills, higher financial worries, and debt but
unsurprisingly, more positive attitudes towards borrowing (Watson, 2003; Garðarsdottir &
Dittmar, 2012; Pham et al., 2012; Donnelly et al., 2012; Pirog & Roberts, 2007: Ponchio and
Aranha, 2008; Richins, 2011). Similar findings were reflected within the USA and UK
populations (Brown et al., 2005), Finland (Garðarsdóttir & Dittmar, 2012) and Brazil
(Ponchio & Aranha, 2008). We therefore hypothesize the following:
H0d: Higher levels of materialism increases arrears.
6.2.2.5. Gratification
Linked to above constructs, impulsive and compulsive buying traits also leave numerous
borrowers in high levels of debt (O’Guinn and Faber, 1989; Khare, 2016; Phau and Woo,
2008; Joji and Raveendran, 2008). Recent research revealed a link between financially
vulnerable customers and increased levels of impulse buying (O’Connor et al., 2019). Thus,
people with underlying psychological constructs of low self-control and self-esteem lead to
compulsive buying behaviours, resulting in higher debt (Achtziger, et al., 2015), whereas
those consumers possessing high self-control were found to save a portion of their salaries
from each paycheque (Strömbäck, et al., 2017). Likewise, people who have difficulty in
delaying gratification have higher amounts of debt and are prone to problematic gambling
behaviours (Parke, et al., 2004; Norvilitis et al., 2006). Gratification refers to the process in
which a person foregoes engaging in immediate reward behaviour to receive a larger reward
later (aka., deferred gratification). We therefore hypothesize the following:
H0e: Higher levels of immediate gratification increases arrears.
115407

Responsible Access to Credit for Sole-Traders and
Micro-organizations under Unstable Market Conditions with Psychometrics
6.2.2.3. Debt attitudes 6.2.2.6. Fluid intelligence
Associated with FL is the construct of financial attitude. Research has explored student and Cognitive ability is one of the fundamental factors in explaining financial literacy (Munoz-
household debt, highlighting that more positive attitudes toward debt are associated with Murillo et al., 2020). Likewise, that fluid intelligence is a personality characteristic that
accruing more debt (Almenberg et. al, 2020; Haultain, Kemp & Chernyshenko, 2010). drives financial literacy (Dlogosch et al., 2017, Liberati & Camillo, 2018 and Djeundje et al.,
Studies state that there were two different types of attitudes associated with debt. On the one 2021). Fluid intelligence is the innate ability of an individual to respond to complex and
hand, fear of debt was associated with less debt, whereas seeing the utility of debt was unexpected situations. (Chen et al. 2020; Munoz-Murillo et al., 2020). Thus, fluid intelligence
associated with higher debt. We argue that vulnerable customers with positive attitudes (FI) we interpret as the ability, regardless of prior skills or experience, to grasp relationships
toward debt face a high risk of indebtedness, consequently exacerbating payment difficulties. between abstract concepts and employ problem-solving abilities, pattern recognition, and
We therefore hypothesize the following: working memory or the innate ability of an individual to respond to unexpected situations
(Snow & Yalow, 1982; Chen et al. 2020). FI is positively correlated with innovation and
H0c: Positive debt attitudes increase arrears. indicates a relationship with high-IQ and high levels of innovative traits, premised on
measures of utility (US) patents registered (Squalli & Wilson, 2014). Hence, FI has a positive
6.2.2.4. Materialism relationship with business profits, and statistically significant returns to higher FI remained
Part of the psychological constructs model includes the impact of personal factors on robust when including factors pertaining to entrepreneurship. A 1% standard deviation
financial literacy and financial behaviour. Evidence showed that debt attitude (as discussed) increases in performance of Raven’s FI test led to higher profits of around 5.7% and a higher
has a consistent relationship with materialistic value, where materialism is conceptualized as business value of about 7% for entrepreneurs. Raven’s progressive matrices consist of images
the extent to which people value the acquisition and consumption of material objects with simple 2D shapes governed by underlying abstract rules to measure someone’s FI. To
(Norvilitis et.al, 2006; Garðarsdóttir & Dittmar 2012). Materialism reflects the prime solve them, the test-taker must identify and often understand never-encountered abstract
importance an individual affords to possessions, whereby the acquisition of goods is a central patterns and generalise them to new settings, an unexpected condition. Although there exists
objective and symbolic of perceived positivity, success, and (psychological) happiness for the a wide range of abstract visual reasoning (AVR) tasks, in the cognitive literature, evidence
individual (Belk, 1984; Richins and Dawson, 1992; Richins, 2017, 2011). Materialism can places attention to the Raven’s Progressive Matrices (RPMs), finding a highly diagnostic of
create negative consequences, such as a propensity to regularly overspend (Khare, 2014; abstract and relational reasoning abilities and representative for human intelligence in general
Donnelly et al., 2012) in the pursuit of luxurious purchases and non-essential items (Watson, (Malkinski & Mandziuk, 2022). Considering these observations, recent works have
2003), thus, accruing higher debt. Furthermore, materialistic traits have been shown to be investigated whether automatic pattern discovery algorithms can achieve performance
associated with poor financial management skills, higher financial worries, and debt but comparable to humans in solving RPMs (Lecun et al., 2015). The present research adapts
unsurprisingly, more positive attitudes towards borrowing (Watson, 2003; Garðarsdottir & aspects of the Raven test within the PSM to measure FI. We hypothesize that the following:
Dittmar, 2012; Pham et al., 2012; Donnelly et al., 2012; Pirog & Roberts, 2007: Ponchio and
Aranha, 2008; Richins, 2011). Similar findings were reflected within the USA and UK H0f: Higher levels of fluid intelligence decreases arrears.
populations (Brown et al., 2005), Finland (Garðarsdóttir & Dittmar, 2012) and Brazil
(Ponchio & Aranha, 2008). We therefore hypothesize the following: 6.2.2.7. Social desirability
Aligned with materialism, social desirability bias is the tendency to present oneself and one's
H0d: Higher levels of materialism increases arrears. circumstances in a socially acceptable but not entirely accurate way (Bergen & Labonte,
2020). This creates a gap between how participants truly perceive reality and how they
6.2.2.5. Gratification portray it. It's important to differentiate between social desirability as a personality trait (like
Linked to above constructs, impulsive and compulsive buying traits also leave numerous a superiority complex) and social desirability as a response mode, where individuals try to
borrowers in high levels of debt (O’Guinn and Faber, 1989; Khare, 2016; Phau and Woo, create a favorable impression to alter how others perceive their reality (Pauls & Stemmler,
2008; Joji and Raveendran, 2008). Recent research revealed a link between financially 2003). When discussing social desirability bias in research, the focus is primarily on the latter
vulnerable customers and increased levels of impulse buying (O’Connor et al., 2019). Thus, aspect – the impression (Paulhus, 1984, 2001).
people with underlying psychological constructs of low self-control and self-esteem lead to For assessing attitudes toward debt, two types of socially desirable responses are evident: a
compulsive buying behaviours, resulting in higher debt (Achtziger, et al., 2015), whereas person genuinely believes the reported information (self-deception) or provides 'fake'
those consumers possessing high self-control were found to save a portion of their salaries responses to conform to expected behavioral norms. Consequently, social desirability can
from each paycheque (Strömbäck, et al., 2017). Likewise, people who have difficulty in introduce false correlations with debt and influence the strength or suppression of an
delaying gratification have higher amounts of debt and are prone to problematic gambling individual's relationship with debt (Ganster, Hennesey, & Luthans, 1983). Norvilitis et al.
behaviours (Parke, et al., 2004; Norvilitis et al., 2006). Gratification refers to the process in (2006) did not directly measure social desirability, however, suggest that this factor can affect
which a person foregoes engaging in immediate reward behaviour to receive a larger reward whether individuals accurately report their debt attitudes and debt levels. We argue for the
later (aka., deferred gratification). We therefore hypothesize the following: importance of measuring social desirability and mitigating its bias for responsible lending
practices. As a result, we propose the following hypothesis:
H0e: Higher levels of immediate gratification increases arrears.
H0g: Higher levels of social desirability increases arrears.
147 114581

Chapter 6
Table 1
Hypotheses model with core literature per PSM attribute
Hypothesis Hypothesis Hypothesized Core Literature
number relationship
H0 Psychometric credit scoring models do not increase Goel & Ratogi, 2023; Van Thiel et al., 2023;
responsible access to finance for small businesses in Djeundje et al., 2021; Liberati & Camillo, 2018;
unstable market conditions. Dlogish et al., 2017; Kinger, 2013;
H0a Lower levels of finanical skills increases arrears. Negative relation Struckell et al., 2022; Lussardi et al., 2021; Klap-
per & Lussardi 2020; Lusardi 2019;
H0b Higher levels of self-efficacy (confidence) increases Positive relation Nosić & Weber, 2010; Yang, et al., 2007; Dans &
arrears. Haberman, 2007; Seaward & Kemp, 2000;
H0c Positive debt-attitudes increases arrears. Positive relation Almenberg et. al., 2020; Haultain, Kemp &
Chernyshenko, 2010;
H0d Higher levels of materialism increases arrears. Positive relation Garðarsdóttir & Dittmar 2012; Pham et al., 2012;
Donnelly et al., 2012; Pirog & Roberts, 2007; Pon-
chio and Aranha, 2008; Richins, 2011; Norvilitis et
al., 2006; Richins and Dawson, 1992; Belk, 1984;
H0e Higer leveles of inmediate gratification increases arrears. Positive relation O’Connor et al. 2019; Strömbäck, et al., 2017;
Khare 2016; Achtziger et al., 2015; Phau and Woo,
2008; Joji and Raveendran, 2008;
H0f Higher levels of fluid intelligence decreases arrears Negative relation Malkinski & Mandziuk, 2022; Djeundje et al.,
2021; Murillo et al.l 2020; Munoz-Murillo et al.,
2020; Dlogosch et al., 2017, Liberati & Camillo,
2018;
H0g Higher levels of social desirability increases arrears. Positive relation Norvilitis et al.,2006; Ganster, Hennesey, &
Luthans1983;
H1 Psychometric credit scoring models increase responsible Goel & Ratogi, 2023; Van Thiel et al., 2023;
access to finance for small businesses in unstable market Djeundje et al., 2021; Liberati & Camillo, 2018;
conditions. Dlogish et al. 2017; Kinger, 2013
6.3 Data and Methods
6.3.1. Data
To compare the performance of the PSM model with that of the TCSM, we gathered real-time
data from 2,884 applicants (N=2,884) who applied to a CZ FS/FinTech lender between
August 19, 2019, and February 12, 2022. Among these applicants (N=2,884), we computed a
psychometric credit score. Out of these, 826 applicants were approved for a loan,
representing an acceptance rate of 28.6%. Our research focuses on these 826 accepted
applicants since we have default data from them, unlike the rejected applicants. Among the
approved loans, 68 applicants defaulted, which accounts for 8.2% of the sample. We define
"default" as any occurrence of late loan repayment or partial repayment observed up to
February 12, 2022, spanning the entire period. We also counterfactually analyse the
performance of both models during a period of extreme stress in the market. The period of
the state-of-emergency at the COVID-outbreak between March 2020 and November 2020. In
this period 1395 small businesses applied for a loan. Out of these applicants 356 were
approved for a loan which is a an acceptance rate of 25,5%. Among the approved loans 20
defaulted, which accounts for 5,6% of the sample. The lender provides invoice financing for
small businesses that typically issue a limited number of invoices each year. To measure the
state of financial literacy of the sole trader or micro-entrepreneur we apply a psychometric
credit score based on the psychometric traits and attitudes described in this paper (Table 2).
115429

Responsible Access to Credit for Sole-Traders and
Micro-organizations under Unstable Market Conditions with Psychometrics
| Table 1  |     | Table 2  |     |     |     |     |
| -------- | --- | -------- | --- | --- | --- | --- |
|          |     |          |     |     |     |     |
Hypotheses model with core literature per PSM attribute  Variable descriptions
|     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
Description of the variables
|     |     | Meta-variable | Definition |     | Measurement | Source  |
| --- | --- | ------------- | ---------- | --- | ----------- | ------- |
Financial literacy Knowledge, understanding of financial concepts and risks  Psychometric Credit Score OECD; van Thiel (2023);
|     |     |     | but also the skills, motivation, and confidence to apply such  |     |     | Lussardi & Mitchel  |
| --- | --- | --- | -------------------------------------------------------------- | --- | --- | ------------------- |
knowledge and understanding in order to make effective
(2007, 2008, 2011)
decisions across a range of financial contexts, to improve
the financial well-being of individuals, their enterprises and
society, and to enable participation in economic life.
|     |     | Dependent variable | Definition |     | Measurement | Source |
| --- | --- | ------------------ | ---------- | --- | ----------- | ------ |
Default Any instance of late repayment of the loan or a portion  Actual loan repayment  Lender; AdviceRobo
|     |     |     | thereof. |     | data  |     |
| --- | --- | --- | -------- | --- | ----- | --- |
Independent personality variables Definition Measurement Source
Financial skills The practical abilities and competencies entrepreneurs  5-point Likert scale Lussardi & Mitchel
|     |     |     | possess to manage their finances effectively. These skills  |     |     | (2007, 2008, 2011) |
| --- | --- | --- | ----------------------------------------------------------- | --- | --- | ------------------ |
encompass various aspects of financial management,
including budgeting, saving, investing, debt management,
financial planning, and the ability to make informed and
wise financial decisions. Financial skills enable individuals
to navigate complex financial situations and work towards
their financial goals, ultimately contributing to their finan-
cial well-being.
Self efficacy Self-efficacy refers to a sense of personal agency, the belief  5-point Likert scale Bandura (2007, 2011)
that one can achieve and succeed at a given task and is rela-
ted to self-confidence, motivation, optimism, and the belief
that one can cope with a variety of life’s challenges.
Materialism The importance an entrepreneur places on possessions and  5-point Likert scale Richins (2017, 1992)
their acquisition as a necessary or desirable form of conduct
to reach desired end states.

  Gratification The process in which an entrepreneur foregoes engaging  5-point Likert scale Norvilitus, 2006
in immediate reward behaviour to receive a larger reward
|     |     |     | later. |     |     |     |
| --- | --- | --- | ------ | --- | --- | --- |
Fluid intelligence The innate ability of an entrepreneur to respond to complex 6-point categorical  Munoz-Murillo (2020)
| 6.3  Data and Methods  |     |     | and unexpected situations. |     |     |     |
| ---------------------- | --- | --- | -------------------------- | --- | --- | --- |
  Social desirability Social desirability refers to the tendency to present oneself,  Dichotomous variable Bergen & Labonte,
|     |     |     | one's enterprise and one’s social context in a way that is  |     |     | 2020 |
| --- | --- | --- | ----------------------------------------------------------- | --- | --- | ---- |
6.3.1. Data  perceived to be socially acceptable, but not wholly reflec-
To compare the performance of the PSM model with that of the TCSM, we gathered real-time  tive of one’s reality.
data from 2,884 applicants (N=2,884) who applied to a CZ FS/FinTech lender between  Independent attitude variables Definition Measurement Source
Debt attitude An entrepreneur's emotional repsonse to debt.  5-point Likert scale Almenberg (2021)
August 19, 2019, and February 12, 2022. Among these applicants (N=2,884), we computed a
psychometric credit score. Out of these, 826 applicants were approved for a loan,  Independent demographic variables Definition Measurement Source
representing an acceptance rate of 28.6%. Our research focuses on these 826 accepted  Age The number of years an entrepreneur has been alive since  Continous variable
birth.
applicants since we have default data from them, unlike the rejected applicants. Among the

approved loans, 68 applicants defaulted, which accounts for 8.2% of the sample. We define  To subsequently compute a psychometric credit score, we developed a digital psychometric
"default" as any occurrence of late loan repayment or partial repayment observed up to  questionnaire (outlined in Table 3) on the body of financial literacy knowledge described in
February 12, 2022, spanning the entire period. We also counterfactually analyse the  this paper. The questionnaire consists of 15 questions assessing personality traits and attitudes
performance of both models during a period of extreme stress in the market. The period of
using a 5-point Likert scale, measuring the degree of agreement with each statement.
the state-of-emergency at the COVID-outbreak between March 2020 and November 2020. In  Additionally, two questions use a six-alternative pattern recognition test, three questions in a
this period 1395 small businesses applied for a loan. Out of these applicants 356 were  binary format, and one question asks for the respondent's age (demographic metric). For the
approved for a loan which is a an acceptance rate of 25,5%. Among the approved loans 20  final two intelligence-related questions, respondents selected the pattern that best matched
defaulted, which accounts for 5,6% of the sample. The lender provides invoice financing for
their perception. Similarly, for social desirability questions, respondents indicated whether
small businesses that typically issue a limited number of invoices each year. To measure the  they agreed or disagreed with the statement. To calculate the psychometric score on a scale
state of financial literacy of the sole trader or micro-entrepreneur we apply a psychometric  ranging from 0 to 1000, we allocate a maximum of 50 points to each of the 20 questions and
credit score based on the psychometric traits and attitudes described in this paper (Table 2).   then add up the scores for each question to determine the total psychometric score.
|     |      |     |     |         |     |     |
| --- | ---- | --- | --- | ------- | --- | --- |
|     |      |     |     |         |     |     |
|     |      |     |     |         |     |     |
|     |      |     |     |         |     |     |
|     | 149  |     |     | 115503  |     |     |

Chapter 6
Table 3
Psychometric attributes and their questions
Attribute Question
Financial skills I review my bills for accuracy
Sometimes I forget to pay my bills on time
If I have an incidental expense, I have enough savings to cover the expense
Self efficacy It is easy for me to stick to my aims and accomplish my goals
I can stay calm if I have problems because I trust myself that I can handle it well
When I am confronted with a problem, I can usually find several solutions
Debt attitude Taking out a loan can be a good thing, if it helps people to enjoy their life
For many people, debt is a normal part of life.
In today’s society, it is almost impossible to live without debts
Materialism I admire people who own expensive homes, cars, and clothes
I place much emphasis on the amount of material objects people own as a sign of success
I like to own things that impress people
Gratification I am guided by my immediate desires and do not dwell on what the future may look like.
My convenience is a big factor in the decisions I make or the actions I take
I don't think about future problems because I think the future will take care of itself
Fluid intelligence (1) What is the logical image in the open space?
(2) What is the logical image in the open space?
Social desirability I sometimes feel resentful when I don't get my way
There have been occasions when I felt like smashing things
There have been times when I was quite jealous of the good fortune of others
All applicants granted consent during the application process and were required to complete
the questionnaire as a prerequisite for loan eligibility.
To ensure fairness, we employed a random sampling technique, as described by Bell et al.
(2022), to provide an equal chance of selection for all 2,884 CZ lender applicants in this
study. To safeguard applicant privacy, AdviceRobo's dynamic personality data collection tool1
pseudonymized applicant data by assigning a customer ID. Personal data remained under the
lender's control, while psychometric data was transmitted to AdviceRobo for the purpose of
conducting psychometric credit score assessments using the PSM. The system automatically
gathered questionnaire responses using a data collection API, processed the data with the
PSM to produce psychometric credit scores and sub-scores for each applicant's psychometric
attributes, and then transmitted the resulting scores back to the lender through another API.
Subsequently, the lender made credit decisions based on their conventional credit decisioning
method. This allowed the researchers to make a counterfactual assessment of the quality of
both the TCSM and PSM for sole traders and micro-organizations.
The PSM scores were linked to applicant IDs to discern their acceptance status, with 826
being accepted and 2,058 being rejected. We then differentiated between sole traders (N=507)
and micro-organizations (small businesses, N= 319) based on their entity type. Our research
primarily concentrated on newly accepted customers, where we aligned their psychometric
credit scores with their payment history, which was supplied by the lender at the end of every
quarter. To stress-test the results, we specifically examined the period from March 2020 to
1 Advicerobo's applicant data collection tool is a software system designed to gather and compile information
from individuals and entrepreneurs who are applying for financial products or services. This tool streamlines
the process of collecting and organizing applicant data, making it easier for financial institutions to profile
applicants, assess creditworthiness, make lending decisions, and manage the application process efficiently.
115541

Responsible Access to Credit for Sole-Traders and
Micro-organizations under Unstable Market Conditions with Psychometrics
November 2020, which included the "states of emergency" and nationwide lockdowns at the
beginning of the pandemic. During this high-stress state-of-emergency period, the lender
gathered data from loan applicants (N=1,395), loan approvals (N=356), and defaulting
applicants (N=20) from March 2020 to November 2020. The relevant statistical summaries
for the analysis are presented in Table 4.
Table 4.
Descriptive data
Variable Coding N Mean Min Max
1. Entity type (0 = small business; 1 = sole trader) 2884 0.57 - -
2. Psychometric score Sum of the finanical psychometric attributes/ total of 2884 0.43 0.02 0.97
3. Entity status 1 = accepted; 0 = rejected 826 0.29 - -
4. Default 1 = default; 0 = no default 68 0.24 - -
5. Financial skills 1 = very low to 5 = very high 2884 3.74 0 5
6. Self-efficacy 1 =.very low to 5 = very high 2884 4.21 1 5
7. Debt attitude 1 = very low to 5 = very high 2884 2.85 1 5
8. Materialism 1 = very low to 5 = very high 2884 2.45 1 5
9. Gratification 1 = very low to 5 = very high 2884 2.17 1 5
10. Fluid intelligence Choose the right pattern 2884 2.79 0 6
10. Social desirability 0 = no social desirability ; 1 = social desirability 2884 0.60 0 1
11. Period 0 = pre-covid period; 1 = covid period 2884 0.48 - -
1 2. Age 18 - 76 2884 35.09 18 76
6.3.2. Method
To test our hypotheses, we employed a four-step approach. First, we conducted a Pearson
correlation analysis between the different psychometric attributes and arrears to examine their
relationship. A correlational relationship ranges between the value of -1 (indicating a negative
relationship) and +1 (indicating a positive relationship). A value of – or +1 indicates a perfect
relationship between the two variables. A value of 0 indicates no relationship. Correlations
are independent of scale(s) and can be used to compare the effects of different responses
(e.g., Likert scales versus binary choices). Although technically, a correlation can range
between -1 and +1, this is very rare in psychological research. For example, within the social
sciences, a correlation of .1 is seen as a small effect, .3 as a moderate effect, and .5 as a large
effect (Cohen, 1988). The higher the correlation, the stronger the effect of the construct on
having arrears.
While these correlations provide initial insights into the predictive value of each attribute, we
did not delve into further investigation in this paper. In our previous study (Van Thiel et al.,
2023), we extensively explained the creation and verification of the PSM for evaluating the
creditworthiness of low-income consumers, utilizing data from two different credit scoring
markets: the USA and The Netherlands. In this study, which focuses on PSM for MSME
entrepreneurs, we employ a linear model that encompasses responses to all questions, with
the credit score being the sum of points obtained by an applicant from the individual
questions outlined in Table 3. The linear model is presented below.
115525

Chapter 6
Y = b1X + b2X + … + b20X (1)
In which:
Y = dependent variable ‘Probability of Repayment’
b = 1
1X = independent variable score question 1
2X = independent variable score question 2
20X – independent variable score question 20
and the sum of the 20 independent variable scores give the credit score for the probability of
repayment.
Next, we aim to gain insights into the precise classification of sole traders and micro-
organizations (from the MSME sector), determining a suitable decision threshold for our
linear model, and assessing the overall effectiveness of the PSM. To evaluate our binary
classification model, we employ the Receiver Operating Characteristic (ROC) curve. This
curve visually illustrates the balance between correctly identifying positive cases (non-
creditworthy) and minimizing false positives (creditworthy businesses misclassified as non-
creditworthy) at different classification thresholds (Ho et al., 2017).
In our context of classifying small business probability of repayment, the ROC curve
demonstrates how well the system distinguishes between good paying and late paying
businesses. Thus, allowing an evaluation of the PSM's ability to accurately identify well
repaying cases while minimizing the risk of false positives (misclassifying defaulters as good
payers; ibid., 2017).
Subsequently, we determine the cut-off point, also known as the decision threshold. By
plotting the TPR (Sensitivity (4)) against the FPR (1-Specificity (7)) at various classification
thresholds, the ROC curve provides a visual representation of how the model's performance
changes as the threshold for classifying a data point as positive or negative is adjusted. This
threshold determines whether an individual or business is classified as good loan repayer or
defaulter, striking a balance between accepting higher-risk applicants (higher sensitivity in
(3)) and reducing the risk of defaults (higher specificity in (4)). The choice of the decision
threshold involves a trade-off between these considerations, considering associated costs and
optimizing the desired balance. In selecting our cut-off point, we prioritize both sensitivity
and specificity equally. We choose the point closest to the top-left corner of the ROC curve,
which is referred to as the Youden Index (Schisterman et al., 2005). This leads us to set our
cut-off point at 0.33.
We calculate the Area Under the Curve (AUC) and the corresponding confusion matrix for
the ROC curve and decision threshold. The equation for AUROC is not a simple
mathematical formula like some other metrics, but it is based on the ROC curve, a graphical
representation of the model's performance at different thresholds. The ROC curve plots the
True Positive Rate (Sensitivity) against the False Positive Rate (1 - Specificity) for various
threshold values. We define the AUC as:
AUROC=∫01Sensitivity (FPR)d(FPR) (2)
The AUC is a single metric that quantifies the overall performance of a credit scoring system,
ranging from 0 to 1, with a higher value indicating better discriminatory power (Yang &
Berdine, 2017). A higher AUC suggests that the system is more effective at ranking and
distinguishing creditworthy from non-creditworthy applicants. Generally, an AUC of 0.5-0.6
115563

Responsible Access to Credit for Sole-Traders and
Micro-organizations under Unstable Market Conditions with Psychometrics
indicates poor discrimination, 0.6-0.7 is considered acceptable discrimination, 0.7-0.8 reflects
excellent discrimination, and an AUC greater than 0.8 signifies outstanding discriminatory
power of the categorical model (ibid., 2017).
To assess the performance of our classification model, we employ a confusion matrix. This
matrix provides a structured overview of the binary classification model functions and offers
a comprehensive breakdown of PSM’s predictions in comparison to actual outcomes. The
main objective is to drive financial inclusion of sole-traders and micro-organizations, the
matrix categorizes results into four groups:
1. True Positives (TP): prediction of creditworthy applicants.
2. False Positives (FP): prediction of creditworthy applicants, who are non-
creditworthy.
3. True Negatives (TN): prediction of non-creditworthy applicants, who are non-
creditworthy.
4. False Negatives (FN): prediction of non-creditworthy applicants, who are
creditworthy.
From the confusion matrix, we can calculate various performance metrics to assess the
model's effectiveness. The accuracy in (3) is an overall measure of the model's correctness in
classifying applicants as creditworthy or non-creditworthy.
𝑇𝑇𝑇𝑇+𝑇𝑇𝑇𝑇
𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴≔ (𝟑𝟑)
While the notion of "good" accuracy can be𝑇𝑇 s𝑇𝑇u+bje𝐹𝐹c𝑇𝑇tiv+e,𝑇𝑇 in𝑇𝑇du+st𝐹𝐹ry𝑇𝑇 standards generally consider
accuracy above 70% to be "good" (Obviously.Ai, 2023).
In addition to accuracy, sensitivity (e.g., recall or true positive rate) in (4) gauges the model’s
capacity to correctly identify creditworthy applicants, while specificity in (5) evaluates its
capability to accurately spot non-creditworthy applicants.
𝑇𝑇𝑇𝑇
𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝐴𝐴 ≔ (𝟒𝟒)
𝑇𝑇𝑇𝑇+𝐹𝐹𝑇𝑇
𝑇𝑇𝑇𝑇
𝑆𝑆𝑆𝑆𝑆𝑆𝐴𝐴𝑆𝑆𝑆𝑆𝑆𝑆𝐴𝐴𝑆𝑆𝑆𝑆𝐴𝐴 ≔ (𝟓𝟓)
The combined metrics offer a comprehensive analy𝑇𝑇s𝑇𝑇is +of 𝐹𝐹th𝑇𝑇e PSM’s performance, especially
regarding its ability to minimize the risk of defaults. By examining accuracy, sensitivity, and
specificity, the PSM's capacity to make precise classifications and informed decisions
regarding applicants' creditworthiness is evaluated for reliability.
Third, we carried out a counterfactual analysis (CFA), to draw causal inferences regarding the
impact of X on Y within a specific case. Thus,"within-case" counterfactual analysis, is a
crucial tool for causal inference in small-N and case-study analyses (Mahoney &
Barrenechea, 2017). In our CFA, we evaluated whether the PSM outperforms the traditional
credit scoring model for sole traders and micro-organizations in the Czech Republic during
the market turbulence caused by COVID-19. Our analysis primarily focusses on comparing
acceptance (7) and default rates in (6) (often referred to as "bad rates") between the PSM and
the TCSM, especially during times of heightened volatility such as lockdowns and the
broader crisis period.
115547

Chapter 6
𝑇𝑇𝑇𝑇+𝐹𝐹𝑇𝑇
𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴 𝑟𝑟𝐴𝐴𝐴𝐴𝐴𝐴 ≔ (𝟔𝟔)
𝑇𝑇𝑇𝑇+𝐹𝐹𝑇𝑇+𝑇𝑇𝑇𝑇+𝐹𝐹𝑇𝑇
𝐹𝐹𝑇𝑇
𝐷𝐷𝐴𝐴𝐷𝐷𝐴𝐴𝐷𝐷𝐷𝐷𝐴𝐴 𝑟𝑟𝐴𝐴𝐴𝐴𝐴𝐴 ≔ (𝟕𝟕)
Additionally, we evaluated the extent to which the P𝐹𝐹S𝑇𝑇M+ ac𝑇𝑇c𝑇𝑇urately identifies both well
paying and late-paying applicants within the accepted customer base.
Fourth, we assessed the effectiveness of the PSM for two distinct sectors within MSMEs:
sole traders, and micro-organizations. Again, comparing the lender's default rates with the
default rates generated by the PSM. Expanding on our prior analysis, we examined
performance during both the stressed "state of emergency" period from March 2020 to
November 2020 and the overall crisis period from August 2019 to February 2022 to gain a
comprehensive understanding. Python 3.10.0, along with the Pandas and NumPy libraries,
was used for the analyses (Fuhrer, 2021). These tools and libraries were employed for tasks
like data loading, preprocessing, calculating performance metrics, plotting ROC curves, and
conducting analyses.
6.4 Results
6.4.1. Psychometric model features
In support of the conceptual model presented in figure 1, we reference baseline correlations
from our previous paper (Van Thiel, 2023). The columns in the table represent psychometric
attributes accompanied with correlations for arrears, significance levels, and conclusive
statements regarding these relationships.
We observe a robust correlation between financial skills and arrears, with a negative value of
-0.57 (p < 0.001), indicating that higher financial skills are associated with lower levels of
arrears. This aligns with Hypothesis 0a, suggesting that lower financial skills are linked to
increased arrears.
Furthermore, we find that self-efficacy (-0.25, p = 0.001), debt attitude (0.22, p = 0.01), and
social desirability (-0.31, p = 0.001) exhibit moderate relationships with arrears. However,
only 22-31% of the variation in arrears is explained by the PSM in the sampled population.
Consequently, we offer partial support for Hypotheses H0b and H0g, indicating that higher
levels of self-efficacy and social desirability are associated with lower arrears. On the
contrary, debt attitude has a positive relationship with arrears (0.22, p = 0.01), suggesting that
greater openness to debt correlates with increased arrears, in line with Hypothesis 0c.
In contrast, psychometric attributes such as materialism (0.11, p = 0.08), delayed gratification
(0.08, p = 0.58), and fluid intelligence (-0.12, p = 0.17) exhibit weak correlations with arrears
and lack statistical significance. As a result, we reject Hypotheses H0d, H0e, and H0f.
In summary, our findings provide evidence that financial skills, self-efficacy, debt attitude,
and social desirability factors exhibit statistically significant correlations with arrears, both
positively and negatively. Previous research has also indicated relationships between
financial skills and financial fragility (Lusardi et al., 2021), financial skills and financial
education (Lusardi & Mitchel, 2007, 2008), self-efficacy (Seaward & Kemp, 2000), debt
attitude (Almenberg et al., 2020; Azma et al., 2019), and social desirability (Norvilitis et al.,
2006) in the context of debt. This research contributes to the existing body of knowledge by
establishing a connection between these attributes and arrears. As a result, we reject the null
hypothesis (H0) that there is no significant correlation between psychometric attributes and
arrears.
115585

Responsible Access to Credit for Sole-Traders and
Micro-organizations under Unstable Market Conditions with Psychometrics
Table 5
𝑇𝑇𝑇𝑇+𝐹𝐹𝑇𝑇 Correlation of psychometric attributes with arrears
𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴 𝑟𝑟𝐴𝐴𝐴𝐴𝐴𝐴 ≔ (𝟔𝟔)
𝑇𝑇𝑇𝑇+𝐹𝐹𝑇𝑇+𝑇𝑇𝑇𝑇+𝐹𝐹𝑇𝑇
Variable Arrears r p <
Variable Arrears r p <
𝐷𝐷𝐴𝐴𝐷𝐷𝐴𝐴𝐷𝐷𝐷𝐷𝐴𝐴 𝑟𝑟𝐴𝐴𝐴𝐴𝐴𝐴 ≔
𝐹𝐹𝑇𝑇
(𝟕𝟕) FFininaanncicaila slk silklsills --00..5577****** --00..5555 00..000011
Additionally, we evaluated the extent to which the P𝐹𝐹S𝑇𝑇M+ ac𝑇𝑇c𝑇𝑇urately identifies both well
SSeelfl fe ffiefcfaiccaycy --00..2255****** 00..2233 00..000011
paying and late-paying applicants within the accepted customer base.
DDeebbt ta attitttuitduede 00..2222**** 00..2288 00..000011
Fourth, we assessed the effectiveness of the PSM for two distinct sectors within MSMEs:
sole traders, and micro-organizations. Again, comparing the lender's default rates with the MMaateterirailaislmism 00..1111 00..1122 00..0088
default rates generated by the PSM. Expanding on our prior analysis, we examined Delay of gratification 0.08 0.04 0.58
Delay of gratification 0.08 0.04 0.58
performance during both the stressed "state of emergency" period from March 2020 to Fluid intelligence -0.12 0.10 0.17
Fluid intelligence -0.12 0.10 0.17
November 2020 and the overall crisis period from August 2019 to February 2022 to gain a
Social desirability -0.31*** 0.28 0.001
comprehensive understanding. Python 3.10.0, along with the Pandas and NumPy libraries, Social desirability -0.31*** 0.28 0.001
Age -0.28*** 0.28 0.001
was used for the analyses (Fuhrer, 2021). These tools and libraries were employed for tasks Age -0.28*** 0.28 0.001
like data loading, preprocessing, calculating performance metrics, plotting ROC curves, and
*** = significant at < 0.001 level
conducting analyses. *** = significant at < 0.001 level
**** = = s isginginfiicfaicnat natt a<0t .<001. 0le1v elelvel
6.4 Results
6.4.1. Psychometric model features 6.4.2. Psychometric model performance assessment
In support of the conceptual model presented in figure 1, we reference baseline correlations To examine the core research question and H1, we assess the performance of the model
from our previous paper (Van Thiel, 2023). The columns in the table represent psychometric through a ROC (Receiver Operating Characteristic) analysis. This evaluation encompasses
attributes accompanied with correlations for arrears, significance levels, and conclusive the PSM’s overall performance and specifically for sectors sole-traders and micro-
statements regarding these relationships. organizations access to credit assessments.
We observe a robust correlation between financial skills and arrears, with a negative value of Our findings reveal that the PSM model demonstrates acceptable discriminatory power
-0.57 (p < 0.001), indicating that higher financial skills are associated with lower levels of (AUC, 0.61) in predicting arrears for all small business sole-trader customers combined.
arrears. This aligns with Hypothesis 0a, suggesting that lower financial skills are linked to Within the context of our ROC curve, we establish a decision threshold to determine whether
increased arrears. to accept new customers, aiming to strike a balance between the true positive rate (TPR) and
Furthermore, we find that self-efficacy (-0.25, p = 0.001), debt attitude (0.22, p = 0.01), and false positive rate (FPR) The specific threshold that balances TPR and FPR on our ROC
social desirability (-0.31, p = 0.001) exhibit moderate relationships with arrears. However, curve is set at 0.33.
only 22-31% of the variation in arrears is explained by the PSM in the sampled population.
Consequently, we offer partial support for Hypotheses H0b and H0g, indicating that higher
levels of self-efficacy and social desirability are associated with lower arrears. On the 𝐹𝐹𝐹𝐹
𝐹𝐹𝐹𝐹𝐹𝐹 ≔ (𝟖𝟖)
contrary, debt attitude has a positive relationship with arrears (0.22, p = 0.01), suggesting that Given the significant impact of credit scoring o𝑇𝑇n𝑇𝑇 le+nd𝐹𝐹in𝐹𝐹g decisions and potential financial
greater openness to debt correlates with increased arrears, in line with Hypothesis 0c. losses, careful consideration of the threshold and its implications is crucial in the context of
In contrast, psychometric attributes such as materialism (0.11, p = 0.08), delayed gratification credit assessment and risk management. By setting a threshold of 0.33 on the ROC curve, it
(0.08, p = 0.58), and fluid intelligence (-0.12, p = 0.17) exhibit weak correlations with arrears signifies that the PSM places a higher emphasis on sensitivity or recall because it shifts the
and lack statistical significance. As a result, we reject Hypotheses H0d, H0e, and H0f. balance in favor of correctly identifying positive cases, even if it results in a higher false
In summary, our findings provide evidence that financial skills, self-efficacy, debt attitude, positive rate. In other words, the model strives to detect a larger portion of true positive cases,
and social desirability factors exhibit statistically significant correlations with arrears, both which are individuals less likely to default on their credit commitments. The primary
positively and negatively. Previous research has also indicated relationships between objective of the PSM is by introducing psychometric data into the credit scoring data,
financial skills and financial fragility (Lusardi et al., 2021), financial skills and financial increase the prediction of creditworthy applicants and their likelihood to default on payments
education (Lusardi & Mitchel, 2007, 2008), self-efficacy (Seaward & Kemp, 2000), debt and accrue arrears, compared to TCSMs. By setting this threshold, the model is designed to
attitude (Almenberg et al., 2020; Azma et al., 2019), and social desirability (Norvilitis et al., be also more cautious in identifying potential defaulters, capturing a greater number of
2006) in the context of debt. This research contributes to the existing body of knowledge by individuals who may pose a credit risk. As a result, it outperforms the TCSM in both
establishing a connection between these attributes and arrears. As a result, we reject the null acceptance and default rates.
hypothesis (H0) that there is no significant correlation between psychometric attributes and
arrears. The ROC curve, presented in Figure 2, serves as a straightforward yet comprehensive
empirical representation of the impact of this decision threshold. The illustration provides all
155 115569

Chapter 6
possible combinations of the relative frequencies of various types of correct and incorrect  Initially, the PSM was assessed for accuracy, in binary classification, accuracy is defined in
decisions (Gerke & Zapf, 2022; Martínez-Camblor & Pardo-Fernández, 2019).  With the  (3). Here, TP stands for True Positives, TN for True Negatives, FP for False Positives, and FN
Roc-curve the confusion matrix of the total period is presented in table 6.  for False Negatives.
|     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Figure 2  Our findings show that the PSM has lower accuracy when considering all customer sectors
  during the entire period from 2019 to 2022 (0.55) compared to the TCSM (0.92). The
ROC-curve total period (August 2019 – February 2022)  difference in accuracy between the two credit scoring models is of lesser importance as it is
  influenced by the dataset used for assessment. As the PSM is only evaluating customers who
were already assessed by the first model and considered "good" customers, this is known as a
biased or truncated dataset. So, we have to investigate deeper to assess the value of the PSM
versus the TCSM.

Consequently, a more detailed assessment of the model's performance reveals that it excels in
avoiding false positives (Precision 0.94, as shown in (9)). This means the model supports
financial inclusion while keeping default costs low. Given that false positives result in
significant costs, this metric is essential for the effectiveness of a high-performing credit
scoring model.
Precision in (9), defined as the proportion of correctly predicted positive instances out of all
positive predictions made by the model (Fawcett, 2005), reflects the model's precision in
positive predictions.
|     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Subsequently, in examining the model's recall, define𝑇𝑇d𝑃𝑃 as "the fraction of all real anomalies
| Table 6  |     |     |     |     |     |     |     | 𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃	≔ | (𝟗𝟗) |
| -------- | --- | --- | --- | --- | --- | --- | --- | -------------------- | ---- |
  that are successfully detected" (Zhang & Zhang, 2𝑇𝑇0𝑃𝑃09+; T𝐹𝐹a𝑃𝑃tbul et al., 2018: 1), in terms of
Confusion matrices PSM & TCSM total period  precision in the PSM, recall aligns appropriately (0.55). The F1 metric in (10), defined as the
  harmonic mean of precision and recall, further confirms the model's high precision.
|     | PSMPS M  | C u t   o ff   t hr | e s h o ld :   0. 3 3   |     |     |     |     |     |     |
| --- | -------- | ------------------- | ----------------------- | --- | --- | --- | --- | --- | --- |
|     |          | C u t   o ff  t h   | r es h o l d :  0 . 3 3 |     |     |     |     |     |     |
|     |          | ActuAacltual        |                         |     |     |     |     |     |     |

PrePdricetdeidcted Default DefNaou ldtefaultNo defaTuolttal Total
|     |     |                      |     |          |        |     |     | !×#$%&'(')*×+%&,--     |        |
| --- | --- | -------------------- | --- | -------- | ------ | --- | --- | ---------------------- | ------ |
|     |     | DDefeafuaultlt       |     | 40 40341 | 341381 | 381 |     |                        |        |
|     |     |                      |     |          |        |     |     | 𝐹𝐹1	≔ #$%&'(')*.+%&,-- | (𝟏𝟏𝟏𝟏) |
|     |     |                      |     | 28 417   | 445    |     |     |                        |        |
|     |     | NNoo d defeafauultlt |     | 28       | 417    | 445 |     |                        |        |
It is noteworthy that "precision is the fraction of all detected good customers that are real
|     |     | Total |     | 68 758 | 826 |     |     |     |     |
| --- | --- | ----- | --- | ------ | --- | --- | --- | --- | --- |
Total 68 758 826 good customers, whereas recall is the fraction of all real good customers that are successfully
detected" (Zhang & Zhang, 2009; Tatbul et al., 2018: 1).

|     | Traditional model | Cut off threshold: 0.33 |     |     |     |     |     |     |     |
| --- | ----------------- | ----------------------- | --- | --- | --- | --- | --- | --- | --- |
Traditional model The analysis was repeated for each customer segment and Table 7 provides an overview of
Cut off threshold: 0.33
Actual the overall metrics and metrics specific to each period and segment. Despite the model's
Actual
lower , yet explainable, overall accuracy, we conclude that it exhibits remarkable accuracy
|     | Predicted |     |     | Default No default | Total |     |     |     |     |
| --- | --------- | --- | --- | ------------------ | ----- | --- | --- | --- | --- |
Predicted Default No default Total and acceptable discriminatory power in predicting good customers with strong precision.
|     |     | Default |     | 0   | 0   | 0   |     |     |     |
| --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
Default 0 0 0 Therefore, we believe that the PSM presents an intriguing opportunity to enhance traditional
|     |     | N o  d ef a u lt |     | 68  | 758 | 826 |     |     |     |
| --- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- |
N o  d e fa u lt 68 758 826 credit scoring model (TCSM) practices for the financial inclusion of sole traders and micro-
ToTtoatlal 68758 758826 826 organizations. We also recommend further modelling and parameter tuning to enhance the
68
|     |     |     |     |     |     |     | accuracy of the PSM model.  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------------- | --- | --- |

|     |     |     | 116507  |     |     |     |     | 158  |     |
| --- | --- | --- | ------- | --- | --- | --- | --- | ---- | --- |

Responsible Access to Credit for Sole-Traders and
Micro-organizations under Unstable Market Conditions with Psychometrics
possible combinations of the relative frequencies of various types of correct and incorrect Initially, the PSM was assessed for accuracy, in binary classification, accuracy is defined in
decisions (Gerke & Zapf, 2022; Martínez-Camblor & Pardo-Fernández, 2019). With the (3). Here, TP stands for True Positives, TN for True Negatives, FP for False Positives, and FN
Roc-curve the confusion matrix of the total period is presented in table 6. for False Negatives.
Figure 2 Our findings show that the PSM has lower accuracy when considering all customer sectors
during the entire period from 2019 to 2022 (0.55) compared to the TCSM (0.92). The
ROC-curve total period (August 2019 – February 2022) difference in accuracy between the two credit scoring models is of lesser importance as it is
influenced by the dataset used for assessment. As the PSM is only evaluating customers who
were already assessed by the first model and considered "good" customers, this is known as a
biased or truncated dataset. So, we have to investigate deeper to assess the value of the PSM
versus the TCSM.
Consequently, a more detailed assessment of the model's performance reveals that it excels in
avoiding false positives (Precision 0.94, as shown in (9)). This means the model supports
financial inclusion while keeping default costs low. Given that false positives result in
significant costs, this metric is essential for the effectiveness of a high-performing credit
scoring model.
Precision in (9), defined as the proportion of correctly predicted positive instances out of all
positive predictions made by the model (Fawcett, 2005), reflects the model's precision in
positive predictions.
Table 6 Subsequently, in examining the model's recall, define𝑇𝑇d𝑃𝑃 as "the fraction of all real anomalies
𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃 ≔ (𝟗𝟗)
that are successfully detected" (Zhang & Zhang, 2𝑇𝑇0𝑃𝑃09+; T𝐹𝐹a𝑃𝑃tbul et al., 2018: 1), in terms of
Confusion matrices PSM & TCSM total period precision in the PSM, recall aligns appropriately (0.55). The F1 metric in (10), defined as the
harmonic mean of precision and recall, further confirms the model's high precision.
PSM Cut off threshold: 0.33
Actual
Predicted Default No default Total
!×#$%&'(')*×+%&,--
Default 40 341 381
𝐹𝐹1 ≔ #$%&'(')*.+%&,-- (𝟏𝟏𝟏𝟏)
No default 28 417 445
It is noteworthy that "precision is the fraction of all detected good customers that are real
Total 68 758 826
good customers, whereas recall is the fraction of all real good customers that are successfully
detected" (Zhang & Zhang, 2009; Tatbul et al., 2018: 1).
The analysis was repeated for each customer segment and Table 7 provides an overview of
Traditional model Cut off threshold: 0.33
the overall metrics and metrics specific to each period and segment. Despite the model's
Actual
lower , yet explainable, overall accuracy, we conclude that it exhibits remarkable accuracy
Predicted Default No default Total and acceptable discriminatory power in predicting good customers with strong precision.
Default 0 0 0 Therefore, we believe that the PSM presents an intriguing opportunity to enhance traditional
No default 68 758 826 credit scoring model (TCSM) practices for the financial inclusion of sole traders and micro-
organizations. We also recommend further modelling and parameter tuning to enhance the
Total 68 758 826
accuracy of the PSM model.
157 115681

Chapter 6
Table 7
PSM metrics. Overall, per period and per customer segment
PPSSMM MMiiccrroo--bbuussinineessssees s+ + s eslef lef memplopyloeyded M Micircor-ob-ubsuinseinsesesss eosn olynly S eSlef-lef-memplopyloeyde odn olynly
TotalT poetarilo pderiod COVCIOD-VpIeDr-ipoedriod TotalT poetraiol dperiod COVCIOD-VpIeDr-ipoedriod TotaTl poetarilo pderiod COVCIOD-VpIeDr-ipoedriod
AAUUCC 0.61 0.61 0.59 0.59 0.58 0.58 0.40 0.40 0.62 0.62 0.69 0.69
GGininii 0.22 0.22 0.18 0.18 0.16 0.16 0 0 0.24 0.24 0.38 0.38
AAccccuurraaccyy 0.55 0.55 0.51 0.51 0.51 0.51 0.44 0.44 0.58 0.58 0.57 0.57
Precision 0.87 0.91 0.84 0.92 0.88 0.90
Precision 0.87 0.91 0.84 0.92 0.88 0.90
Recall 0.55 0.51 0.51 0.44 0.58 0.57
Recall 0.55 0.51 0.51 0.44 0.58 0.57
F1 0.65 0.63 0.60 0.59 0.68 0.67
F1 0.65 0.63 0.60 0.59 0.68 0.67
N 826 356 319 169 507 187
N
Arrears
826
68
356
20
319
31
169
6
507
37
187
14
A rrears 68 20 31 6 37 14
6.4.3. Psychometric model resilience
To evaluate the PSMs resilience in the face of extreme crisis conditions, we conducted a
stress test during the "state of emergency" period at the onset of the COVID-19 pandemic,
spanning from March to November 2020. During this challenging time in the Czech Republic
(CZ), historical data lost its reliability for credit scoring, as past performance could no longer
accurately predict future outcomes.
To stress test the PSMs performance in this stressed state-of-emergency period, we conducted
the same evaluation procedures, including the creation of a ROC curve and confusion
matrices for this specific period (figure 3 and table 8). The PSM maintained acceptable
discriminatory capabilities in the light of the as ‘good’ accepted customer base, achieving an
AUC of 0.59 despite the high volatility witnessed during the COVID-19 period (March-
November 2020). A decision threshold of 0.33 was once more set by maintaining a balance
between the true positive rate (TPR) and false positive rate (FPR) throughout this high-stress
period.
Turning to test the PSM during this "state of emergency" period (March – November 2020)
characterized by high volatility, we found that the PSM's accuracy during this period was
similar to its accuracy over the entire duration, with an overall accuracy of 0.51, which is
relatively low. Once more, we assert that low accuracy should not be the primary metric to
consider. Instead, we attribute this to the nature of the dataset, which predominantly consists
of "good" accepted customers, even though the model is designed to differentiate between
good and poor payers. However, upon closer examination of the model's performance, it
effectively minimized false positives during the "state of emergency" period (Precision 0.91).
The PSM's accuracy in correctly predicting good customers stands at 0.96, surpassing the
TCSM's accuracy in predicting good customers (0.94). Given the lender's focus on curtailing
false positives due to associated costs, the recall rate was deemed appropriate at 0.51.
Additionally, the F1 metric confirmed the model's elevated precision, as detailed in Table 7.
These findings underscore the PSM's robustness during periods of heightened volatility,
exemplified by the "state of emergency" during March to November 2020. Consequently, this
suggests that replacing TCSMs with PSMs during times of high volatility is a viable strategy.
TCSMs frequently fail to adapt to evolving customer circumstances, prompting banks to
resort to temporary measures such as expert adjustments of default rates at portfolio-segment
levels during similar periods (McKinsey, 2021).
116529

Responsible Access to Credit for Sole-Traders and
Micro-organizations under Unstable Market Conditions with Psychometrics
| Table 7  |     |     |     |     |     |     | Figure 3.   |     |     |     |     |     |     |
| -------- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- |
|          |     |     |     |     |     |     |             |     |     |     |     |     |     |
PSM metrics. Overall, per period and per customer segment  ROC-curve period of ‘state of emergency’ (March 2020 – November 2020)
|     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
PPSSMM             MMiiccrroo--bbuussinineessssees s+ + s eslef lef memplopyloeyded                             M  Micircor-ob-ubsuinseinsesesss eosn olynly                                    S eSlef-lef-memplopyloeyde odn olynly
TotalT poetarilo pderiod COVCIOD-VpIeDr-ipoedriod TotalT poetraiol dperiod COVCIOD-VpIeDr-ipoedriod TotaTl poetarilo pderiod COVCIOD-VpIeDr-ipoedriod
AAUUCC 0.61 0.61 0.59 0.59 0.58 0.58 0.40 0.40 0.62 0.62 0.69 0.69
GGininii 0.22 0.22 0.18 0.18 0.16 0.16 0 0 0.24 0.24 0.38 0.38
AAccccuurraaccyy 0.55 0.55 0.51 0.51 0.51 0.51 0.44 0.44 0.58 0.58 0.57 0.57
| Precision      | 0.87   | 0.91   | 0.84   | 0.92  | 0.88   | 0.90 |     |     |     |     |     |     |     |
| -------------- | ------ | ------ | ------ | ----- | ------ | ---- | --- | --- | --- | --- | --- | --- | --- |
| Precision 0.87 | 0.91   | 0.84   | 0.92   | 0.88  | 0.90   |      |     |     |     |     |     |     |     |
| Recall         | 0.55   | 0.51   | 0.51   | 0.44  | 0.58   | 0.57 |     |     |     |     |     |     |     |
| Recall 0.55    | 0.51   | 0.51   | 0.44   | 0.58  | 0.57   |      |     |     |     |     |     |     |     |
| F1             | 0.65   | 0.63   | 0.60   | 0.59  | 0.68   | 0.67 |     |     |     |     |     |     |     |
| F1 0.65        | 0.63   | 0.60   | 0.59   | 0.68  | 0.67   |      |     |     |     |     |     |     |     |
| N              | 826    | 356    | 319    | 169   | 507    | 187  |     |     |     |     |     |     |     |
| N Arrears 826  | 68 356 | 20 319 | 31 169 | 6 507 | 37 187 | 14   |     |     |     |     |     |     |     |
| A rrears 68    | 20     | 31     | 6      | 37    | 14     |      |     |     |     |     |     |     |     |

6.4.3. Psychometric model resilience
To evaluate the PSMs resilience in the face of extreme crisis conditions, we conducted a
stress test during the "state of emergency" period at the onset of the COVID-19 pandemic,
spanning from March to November 2020. During this challenging time in the Czech Republic
(CZ), historical data lost its reliability for credit scoring, as past performance could no longer

accurately predict future outcomes.
Table 8
To stress test the PSMs performance in this stressed state-of-emergency period, we conducted

the same evaluation procedures, including the creation of a ROC curve and confusion
matrices for this specific period (figure 3 and table 8). The PSM maintained acceptable  Confusion matrices PSM & TCSM state-of-emergence period

discriminatory capabilities in the light of the as ‘good’ accepted customer base, achieving an
|     |     |     |     |     |     |     | PSM COVID-period |     | Cut off threshold: 0.33 |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ----------------------- | --- | --- | --- | --- |
AUC of 0.59 despite the high volatility witnessed during the COVID-19 period (March- PSM COVID-period Cut off threshold: 0.33
November 2020). A decision threshold of 0.33 was once more set by maintaining a balance  Actual Actual
between the true positive rate (TPR) and false positive rate (FPR) throughout this high-stress
PrPerdeidcticetded Default DefaNuol tdefaulNto defaTuolttal Total
| period.  |     |     |     |     |     |     |     |     |                |     | 12 12166 | 166178 |     |
| -------- | --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | -------- | ------ | --- |
|          |     |     |     |     |     |     |     |     | DeDfeafualutlt |     |          |        | 178 |

|     |     |     |     |     |     |     |     |     | NoN od edfeafualutlt |     | 8 8170 | 170178 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | ------ | ------ | --- |
Turning to test the PSM during this "state of emergency" period (March – November 2020)  178
characterized by high volatility, we found that the PSM's accuracy during this period was  To T t o a t l al 20 20 336 336 356 356
similar to its accuracy over the entire duration, with an overall accuracy of 0.51, which is
relatively low. Once more, we assert that low accuracy should not be the primary metric to
|     |     |     |     |     |     |     | Traditional model |     | Cut off threshold: 0.33 |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | ----------------------- | --- | --- | --- | --- |
consider. Instead, we attribute this to the nature of the dataset, which predominantly consists
|     |     |     |     |     |     |     |     | Traditional model | Cut off tAhcrteusahlold: 0.33 |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | ----------------------------- | --- | --- | --- | --- |
of "good" accepted customers, even though the model is designed to differentiate between
good and poor payers. However, upon closer examination of the model's performance, it  Predicted Actual Default No default Total
|     |     |     |     |     |     |     |     | Predicted |     | Default | No default | Total |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | ------- | ---------- | ----- | --- |
effectively minimized false positives during the "state of emergency" period (Precision 0.91).  Default 0 0 0
The PSM's accuracy in correctly predicting good customers stands at 0.96, surpassing the  Default 0 0 0
|     |     |     |     |     |     |     |     |     | No default |     | 20  | 336 | 356 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- |
TCSM's accuracy in predicting good customers (0.94). Given the lender's focus on curtailing  No default 20 336 356
false positives due to associated costs, the recall rate was deemed appropriate at 0.51.  To t a l 20 336 356
|     |     |     |     |     |     |     |     |     | T o t al |     | 20 336 | 356 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | ------ | --- | --- |

Additionally, the F1 metric confirmed the model's elevated precision, as detailed in Table 7.

These findings underscore the PSM's robustness during periods of heightened volatility,
6.4.4. Counterfactual analysis of business impact
exemplified by the "state of emergency" during March to November 2020. Consequently, this
In assessing the profit contribution of the PSM, a counterfactual analysis (CFA) was
suggests that replacing TCSMs with PSMs during times of high volatility is a viable strategy.
conducted to compare the PSM's performance against the TCSM. The analysis utilized the
TCSMs frequently fail to adapt to evolving customer circumstances, prompting banks to
entire scored base (N = 2884) for comparing acceptance rates and the accepted customer base
resort to temporary measures such as expert adjustments of default rates at portfolio-segment
(N = 826) for comparing default rates. This facilitated the cross-validation of the "bad" or
levels during similar periods (McKinsey, 2021).
default rates, as described in (6), for both models using the same dataset. The CFA reveals

that the PSM raised the acceptance rates to 37.3%, as opposed to 28.6% with the traditional
  model, resulting in N=1077 (PSM) compared to 826 (TCSM) predicted good customers out

of N=2884 applicants (Table 9).
|     |     |     | 159  |     |     |     |     |     |     | 116603  |     |     |     |
| --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- |

Chapter 6
  a 20% lower bad rate, effectively reducing default costs and contributing to lender profit
| Table 9  |     |     |     |     |     | margins during market volatility.  |     |     |     |     |     |
| -------- | --- | --- | --- | --- | --- | ---------------------------------- | --- | --- | --- | --- | --- |
  Tables 9 and 10 include a detailed breakdown of the analysis of the state-of-emergency model
Acceptance rates PSM and TCSM both periods  performances. In conclusion, stress tests reveal the effectiveness of the PSM during market
|         |       |              |       |                            |     | volatility, confirming our core hypothesis H1.  |     |     |     |     |     |
| ------- | ----- | ------------ | ----- | -------------------------- | --- | ----------------------------------------------- | --- | --- | --- | --- | --- |
| Overall |       | PSM          |       | Traditional score          |     |                                                 |     |     |     |     |     |
|         |       | PredPicStMed |       | TraPdreitdioicntaeld score |     |                                                 |     |     |     |     |     |
|         | State |              | State |                            |     |                                                 |     |     |     |     |     |
Total Period AScttautael Pnore ddeicfateudlt default SAtcattueal nPor deedfiacuteltd default 6.4.5. Segmented counterfactual analysis of business impact
Total Period no default Actual no default 1049 default 1767 2816no default Actual 727 no default / default
no default 1049 1767 2816no default 727 / Having established the effectiveness of the PSM in promoting financial inclusion for small
|     | default | 28  | 40 68default | 88 / |     |     |     |     |     |     |     |
| --- | ------- | --- | ------------ | ---- | --- | --- | --- | --- | --- | --- | --- |
default 28 40 68default 88 / businesses, we proceed to evaluate its performance across different small business segments,
|     | Total | 1077 | 1807 2884Total | 815 2069 | 2884 |     |     |     |     |     |     |
| --- | ----- | ---- | -------------- | -------- | ---- | --- | --- | --- | --- | --- | --- |
Total 1077 1807 2884Total 815 2069 2884 specifically sole traders and small businesses. We conduct a repeat of the previous
aacccceeppttaannccee r artaete 3377,3,344%%aacccceeppttaannccee  rraattee 28,262%8,26%
counterfactual tests (CFA) for both segments, recognizing that both face distinct challenges in
|     |     | PSMPSM |     | TradTitiroandaitli oscnoarle score |     |     |     |     |     |     |     |
| --- | --- | ------ | --- | ---------------------------------- | --- | --- | --- | --- | --- | --- | --- |
Predicted Predicted accessing capital to support their growth. These challenges encompass limited collateral,
|     | State | Predicted | State | Predicted |     |     |     |     |     |     |     |
| --- | ----- | --------- | ----- | --------- | --- | --- | --- | --- | --- | --- | --- |
State-of-emergency Actual no default default Actual no default default sparse credit history, limited financial management capabilities, and restricted access to
State-of-emergency Actual n o   d e f a u lt no default 5 2 6 default 8 4 9 1 3 7 5 n Actual o  d e f a u l t no default 336 default /
n o   d e f a u lt 5 2 6 8 4 9 1 3 7 5 n o  d e f a u l t 336 / financial networks. Additionally, regulatory barriers and the perception of being high-risk
|     | default | 8   | 12 20default | 20  | /   |     |     |     |     |     |     |
| --- | ------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
dTeoftaaullt 5348 86112 139250Tdoetfaalult 20 356/ applicants by lenders employing traditional Credit Scoring Models (TCSMs) contribute to
1039 1395
Taoctcaelptance rate 534 861 38,2183%95aTcocteapltance rate 356 1039 139525,52%  these constraints.
|     | acceptance rate |     | 38,28%acceptance rate |     | 25,52% |     |     |     |     |     |     |
| --- | --------------- | --- | --------------------- | --- | ------ | --- | --- | --- | --- | --- | --- |

To validate the effectiveness of the scoring models we now validate their default rates.  Out  When we compare the default rates of these two segments in a counterfactual manner, the
of the N=826 accepted small businesses, the TCSM recorded N=68 false positives over the  results reveal that the PSM leads to a substantial 20.3% lower default rate for sole-traders.
entire period (2019-2022), resulting in an 8.2% bad rate for the TCSM. Conversely, the PSM  This noteworthy improvement can be attributed to the PSM's consideration of non-financial
made incorrect predictions for N=28 customers out of N=445 predicted good customers,
factors, such as the more stable personality attributes and attitudes of entrepreneurs, as
yielding a 6.3% bad rate. As a result, the PSM achieved a 23.2% lower default rate than the  opposed to relying solely on less informative traditional financial drivers for this segment.
TCSM. This analysis further demonstrates the PSM's capacity to enhance access to finance  Furthermore, concerning micro-organizations, we observed a similar trend where the PSM
for the small business (MSME) sector (see Table 10).  outperformed the traditional model, resulting in a remarkable 24.4% lower default rate for the

total period. For a comprehensive breakdown, please refer to Tables 13 and 14. These
Table 10  findings underscore the PSM's capacity to enhance credit risk assessment and reduce default
|     |     |     |     |     |     | rates for both segments.  |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------------------- | --- | --- | --- | --- | --- |
Default rates PSM & TCSM total period and state-of emergency

| Overall |       | PSM                 |             | Traditional score          |     | Table 11   |     |     |     |     |     |
| ------- | ----- | ------------------- | ----------- | -------------------------- | --- | ---------- | --- | --- | --- | --- | --- |
|         | State | PredPiScMted        | State       | TraPdrietidoinctaeld score |     |            |     |     |     |     |     |
|         |       | Pnroe ddiecftaeudlt | SAtactteual | nPor eddeifcatueltd        |     |            |     |     |     |     |     |
Total Period Actual default default Acceptance rates per sector PSM TCSM total period and state-of-emergency
Total period Anoct dueaflault no defaul4t17 default341 758Ancotu daelfault 7n5o8 default default
|     |                    |        |                                | /        |     |     |     |     |     |     |     |
| --- | ------------------ | ------ | ------------------------------ | -------- | --- | --- | --- | --- | --- | --- | --- |
|     | no default default | 417 28 | 341 40 758no default 68default | 68 758 / | /   |     |     |     |     |     |     |
|     | default            | 28     | 40 68default                   | 68       | /   |     |     |     |     |     |     |
To t a l 4 4 5 3 8 1 8 26 T o ta l 826 826 PSM Traditional score
T o t a l 4 4 5 3 8 1 82 6 T o ta l 826 826 Per sector State Predicted State Predicted
D e fa u l t   r a t e 6 , 2 9% D e fa u lt    r a t e 8,23% Total Period Micro Organisation Actual no default default Actual no default default
D e f a u l t   r a t e 6, 2 9 % D e fa u lt    r a t e 8,23%
|     |     |     |     |     |     |     | no default | 671 934 | 1605no default | 288 / |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------- | -------------- | ----- | --- |
PSMPSM TradTitiraodniatilo sncaolr escore default 16 21 37default 31 /
State PPrreeddiicctteedd State PPrreeddicictteedd Total 687 955 1642Total 319 1323 1642
State-of-emergency Actual no default default Actual no default default acceptance rate 41,84%acceptance rate 19,43%
State-of-emergency Actual no default default Actual no default default
no default 170 166 336no default 336 / Sole Trader Actual no default default Actual no default default
n o  d e f a ult 17 0 1 6 6 3 36 n o  d e fault 336 / no default 378 833 1211no default 439 /
|     | d e f a u l t | 8   | 1 2 2 0 d e fa u lt | 20  | /   |     |     |     |     |     |     |
| --- | ------------- | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
T d o e t fa a u l lt 178 8 17 1 8 2 356 20 T d o e ta fa l ult 20 356 / 356 default 12 19 31default 68 /
|     |     |     |     |     |     |     | Total | 390 852 | 1242Total | 507 735 | 1242 |
| --- | --- | --- | --- | --- | --- | --- | ----- | ------- | --------- | ------- | ---- |
DToetfaalult rate 170 178 4,493%56DTeoftaaullt rate 356 356 5,62%
Default rate 4,49%Default rate 5,62% acceptance rate 31,40%acceptance rate 40,82%

Turning to assess the robustness of the PSM versus TCSM during high volatility periods,  PSM Traditional score
State-of-emergency Micro-Organisation Actual no default default Actual no default default
specifically the state of emergency from March to November 2020, and to evaluate whether
|     |     |     |     |     |     |     | no default | 247 449 | 696no default | 163 / |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------- | ------------- | ----- | --- |
profits increased, we replicated the analysis conducted for the total period.  default 4 2 6default 6 /
|     |     |     |     |     |     |     | Total | 251 451 | 702Total | 169 533 | 702 |
| --- | --- | --- | --- | --- | --- | --- | ----- | ------- | -------- | ------- | --- |
Firstly, the TCSM accepted N=356 applicants out of the total of  during this state-of- acceptance rate 35,75% 24,07%
emergency period. Among them, N=20 were incorrectly predicted as good customers,  Sole Trader Actual no default default Actual no default default
|     |     |     |     |     |     |     | no default | 279 400 | 679no default | 173 / |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------- | ------------- | ----- | --- |
resulting in a bad rate of 5.6%. On the other hand, the PSM accepted N=178 customers
|     |     |     |     |     |     |     | default | 4   | 10 14default | 14 / |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | --- | ------------ | ---- | --- |
during this state-of-emergency period and incorrectly predicted 8 applicants as non- Total 283 410 693Total 187 506 693
|     |     |     |     |     |     |     | acceptance rate |     | 40,84%acceptance rate |     | 26,98%  |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --------------------- | --- | ------- |
defaulters, resulting in a bad rate of 4.5% (table 10). Notably, the PSM demonstrated
resilience during this high-stress state of emergency period and outperformed the TCSM with

|     |     |     | 116641  |     |     |     |     | 162  |     |     |     |
| --- | --- | --- | ------- | --- | --- | --- | --- | ---- | --- | --- | --- |

Responsible Access to Credit for Sole-Traders and
Micro-organizations under Unstable Market Conditions with Psychometrics
a 20% lower bad rate, effectively reducing default costs and contributing to lender profit
Table 9 margins during market volatility.
Tables 9 and 10 include a detailed breakdown of the analysis of the state-of-emergency model
Acceptance rates PSM and TCSM both periods performances. In conclusion, stress tests reveal the effectiveness of the PSM during market
volatility, confirming our core hypothesis H1.
PSM Traditional score
State Predicted State Predicted 6.4.5. Segmented counterfactual analysis of business impact
Total Period Actual no default default Actual no default default
Having established the effectiveness of the PSM in promoting financial inclusion for small
no default 1049 1767 2816no default 727 /
default 28 40 68default 88 / businesses, we proceed to evaluate its performance across different small business segments,
Total 1077 1807 2884Total 815 2069 2884 specifically sole traders and small businesses. We conduct a repeat of the previous
acceptance rate 37,34%acceptance rate 28,26%
counterfactual tests (CFA) for both segments, recognizing that both face distinct challenges in
PSM Traditional score
Predicted Predicted accessing capital to support their growth. These challenges encompass limited collateral,
State-of-emergency Actual no default default Actual no default default sparse credit history, limited financial management capabilities, and restricted access to
no default 526 849 1375no default 336 / financial networks. Additionally, regulatory barriers and the perception of being high-risk
default 8 12 20default 20 /
applicants by lenders employing traditional Credit Scoring Models (TCSMs) contribute to
Total 534 861 1395Total 356 1039 1395
acceptance rate 38,28%acceptance rate 25,52% these constraints.
To validate the effectiveness of the scoring models we now validate their default rates. Out When we compare the default rates of these two segments in a counterfactual manner, the
of the N=826 accepted small businesses, the TCSM recorded N=68 false positives over the results reveal that the PSM leads to a substantial 20.3% lower default rate for sole-traders.
entire period (2019-2022), resulting in an 8.2% bad rate for the TCSM. Conversely, the PSM This noteworthy improvement can be attributed to the PSM's consideration of non-financial
made incorrect predictions for N=28 customers out of N=445 predicted good customers, factors, such as the more stable personality attributes and attitudes of entrepreneurs, as
yielding a 6.3% bad rate. As a result, the PSM achieved a 23.2% lower default rate than the opposed to relying solely on less informative traditional financial drivers for this segment.
TCSM. This analysis further demonstrates the PSM's capacity to enhance access to finance Furthermore, concerning micro-organizations, we observed a similar trend where the PSM
for the small business (MSME) sector (see Table 10). outperformed the traditional model, resulting in a remarkable 24.4% lower default rate for the
total period. For a comprehensive breakdown, please refer to Tables 13 and 14. These
Table 10 findings underscore the PSM's capacity to enhance credit risk assessment and reduce default
rates for both segments.
Default rates PSM & TCSM total period and state-of emergency
Table 11
PSM Traditional score
Predicted State Predicted
Acceptance rates per sector PSM TCSM total period and state-of-emergency
Total period Actual no default default Actual no default default
no default 417 341 758no default 758 /
PSM Traditional score
default 28 40 68default 68 / PSM Traditional score
State Predicted State Predicted
Total 445 381 826Total 826 826 Per sector State Predicted State Predicted
Default rate 6,29%Default rate 8,23% TToottaall PPeerriioodd MMiiccrroo OOrrggaannisiasatitioonn AAccttuuaall nnoo d deefafauultlt defdaeufaltult AAccttuuaall nnoo ddeeffaauulltt dedefafauultlt
nnoo ddeeffaauulltt 667711 993344 11660055nnoo ddeeffaauultlt 288 288 / /
PSM Traditional score ddeeffaauulltt 1166 2211 3377ddeeffaauulltt 31 31 / /
Predicted Predicted TToottaall 668877 995555 11664422TToottaall 319 319 13231323 16421642
State-of-emergency Actual no default default Actual no default default aacccceeppttaannccee rraattee 4411,8,844%%aacccceeppttaannccee r aratete 19,1493,%43%
no default 170 166 336no default 336 / SSoollee TTrraaddeerr AAccttuuaall nnoo d deefafauultlt defdaeufaltult AAccttuuaall nnoo ddeeffaauulltt dedefafauultlt
default 8 12 20default 20 / n n o o d de e f f a a u u l l t t 378 378 833 833 1 1 2 2 1 1 1 1 n n o o d d e e f f a a u u lt lt 439 439 / /
Total 178 178 356Total 356 356 d d Te e of f ta a au u ll l t t 12 3 1 9 2 019 85 1 2 9 123 3 41 1 2d d Te e o f tf a aa u lu l l t t 68 50 6 7 8 / / 735 1242
Default rate 4,49%Default rate 5,62% Taoctcaelptance rate 390 852 311,2440%2Taocctaelptance rate 507 735 124420,82%
acceptance rate 31,40%acceptance rate 40,82%
Turning to assess the robustness of the PSM versus TCSM during high volatility periods, PSM Traditional score
State-of-emergency Micro-Organisation Actual no dPeSfMault default Actual Traditinoon daelf ascuoltre default
specifically the state of emergency from March to November 2020, and to evaluate whether Sntoa tdeefault Predicte2d47 449 696Sntoa dteefault Predicte1d63 /
profits increased, we replicated the analysis conducted for the total period. State-of-emergency Micro Organisation Adcetfuaaullt no default4default 2 6Adecftauuallt no default6 defa/ult
nToo tdaelfault 224571 444519 679062nToot dalefault 163 169 / 533 702
Firstly, the TCSM accepted N=356 applicants out of the total of during this state-of- acceptance rate 35,75% 24,07%
default 4 2 6default 6 /
emergency period. Among them, N=20 were incorrectly predicted as good customers, Sole Trader T A o c t t a u l al no defau 2 l 5 t 1 defau 4 lt 51 702T A o c t t a u l al 1 n 6 o 9 default 53 de 3 fault 702
no default 279 400 679no default 173 /
resulting in a bad rate of 5.6%. On the other hand, the PSM accepted N=178 customers adcecfeapulttance rate 4 10 35,751%4default 14 / 24,07%
during this state-of-emergency period and incorrectly predicted 8 applicants as non- Sole Trader ATcottuaall no defa2u8lt3default410 693ATocttaulal no defau1l8t7 default506 693
naocc deepftaaunclte rate 279 400 40,6874%9naocc depetfaanuclet rate 173 / 26,98%
defaulters, resulting in a bad rate of 4.5% (table 10). Notably, the PSM demonstrated
default 4 10 14default 14 /
resilience during this high-stress state of emergency period and outperformed the TCSM with Total 283 410 693Total 187 506 693
acceptance rate 40,84%acceptance rate 26,98%
161 116625

Chapter 6
its capabilities and displayed remarkable accuracy in predicting good customers. A
counterfactual analysis (CFA) showed that the PSM increased acceptance rates and reduced
Table 12 default rates, making it a promising tool for enhancing access to finance for small businesses.
However, results during the stress test period varied between micro-organizations and sole
PSM/ TCSM per sector both period default rates traders, emphasizing the importance of context and adaptable models in credit risk
assessment. This study underscores the potential of psychometric attributes in credit risk
PSM PSM Traditional scoreTraditional score assessment and the flexibility offered by the PSM in adapting to changing circumstances.
State State PredictePdredicted State StatePredicted Predicted
TToottaall PPeerriioodd MicMroi cOrrog aOnrigsaantiiosnatioAnctualActual no defaunlot ddeeffaauulltt default Actual Actuanlo default denfaou dltefault default
no defanuol tdefault 274 274196 149760no defau4l7t0no de4f7a0ult / 470 /
defaultdefault 16 1621 2317default 37defau3l7t / 37 /
Total Total 290 290217 251077Total 507Total507 507507 507 6.5 Discussion and Conclusion
bad ratbead rate 5,52%bad ra5t,e52%bad rate 7,30% 7,30% In an environment of growing macroeconomic volatility, increasingly complex financial
SoleS Torlaed Terrader ActualActual no defaunlot ddeeffaauulltt default Actual Actuanlo default denfaou dltefault default
no defanuol tdefault143 145143 124858no defau2l8t8no de2f8a8ult / 288 / products, and a widening access to finance gap for small businesses, this research explores
defaultdefault 12 19 12 1391default 31defau3l1t / 31 / whether a novel financial literacy-based psychometric credit scoring model (PSM) can
Total Total 155 164155 136149Total 319Total319 319319 319
bad ratbead rate 7,74%bad ra7t,e74%bad rate 9,72% 9,72% effectively address the access to finance challenges faced by small businesses, including sole
traders and micro-organizations, in unstable market environments. Therefore, incorporating
PSMPSM Traditional score Traditional score
State PredictedPredicted State Predicted Predicted dynamic psychometric data into the application process of a Czech fintech lender indicates
SSttaattee--ooff--eemmeerrggeennccyyMicMroi cOrrog-aOnrigsaatinoisnatiAonctualActual no defaunlot ddeeffaauulltt default Actual Actuanlo default denfaou dltefault default the potential to improve financial inclusion in this sector and support the growth of small and
no defanuol tdefault 73 7390 19603no defau1l6t3no de1f6a3ult / 163 /
defaultdefault 4 4 2 26default 6defau6lt / 6 / medium-sized enterprises (SMEs). Our results provide support for our first hypothesis (H1),
Total Total 77 7792 19629Total 169Total169 169169 169 indicating that the psychometric credit scoring model (PSM) offers an opportunity to
bad ratbead rate 5,19%bad ra5t,e19%bad rate 3,55% 3,55%
SoleS Torlaed Terrader ActualActual no defaunlot ddeeffaauulltt default Actual Actuanlo default denfaou dltefault default responsibly expedite access to finance for self-employed individuals and micro-organizations
no defanuol tdefault97 76 97 17763no defau1l7t3no de1f7a3ult / 173 / in the Czech Republic by assessing applicants' likelihood of credit default and reducing credit
defaultdefault 4 10 4 1104default 14defau1l4t / 14 /
Total Total 101 86 101 18867Total 187Total187 187187 187 risk for lenders.
bad ratbead rate 3,96%bad ra3t,e96%bad rate 7,49% 7,49%
Notably, the PSM outperformed traditional Credit Scoring Models (TCSMs) in identifying
We repeated the Counterfactual Analysis (CFA) to subject the results to a stress test and
risky customers throughout the entire pandemic period from August 19, 2019, to February 12,
validate the default rates for both sectors during the period of extreme uncertainty,
2022. To assess the robustness of our model, we conducted specific stress tests during the
characterized by the 'state of emergency' due to COVID-19. Table 11 demonstrates that the
"state of emergency" period at the COVID-outbreak between March 2020 and November
PSM continued to exhibit higher acceptance rates during the state of emergency period from
2020. Our findings suggest that the PSM also effectively distinguishes good from bad
March 2020 to November 2020 (48.5% for micro-organisations versus 51,4% for sole
payment behavior of small busines entrepreneurs, including sole traders and micro-
traders). However, table 12 reveals contrasting outcomes: the PSM exhibited a 46.2% higher
organizations in this period of high stress. These findings align with previous evidence
default rate for micro-organizations while demonstrating a 47.1% lower default rate for self-
advocating for the inclusion of psychometric factors to enhance credit scoring decision-
employed individuals (3.96% versus 7.49%).
making processes (Goel & Rastogi, 2023; Djeundje et al., 2021; Liberati & Camillo, 2018;
As we delve into the stress-tested situation for the 'state of emergency' during the COVID-19
Dlogish et al., 2017; Klinger, 2013).
period, we find that our findings hold firm for self-employed individuals. In this context, the
PSM consistently outperforms the traditional CSM, resulting in a notably lower default rate.
To the best of our knowledge, this study provides the first evidence that PSMs improve
However, the scenario differs for micro-organizations, where the stress-test results reveal a
credit accessibility for underserved MSMEs and sub-sectors during high market volatility
PSM default rate of 5.19%, which is 46% higher than the traditional CSM default rate.
within the Czech Republic, Europe. Such evidence carries particular significance for global
Several factors may contribute to this discrepancy, including potential model bias due to the
MSMEs, given the continually shifting macroeconomic landscape and the growing gap in
limited number of defaults observed (N=6), as indicated in Table 12. Another plausible
access to finance for sole-traders and micro-organizations.
explanation could be the implementation of more rigorous management oversight on the
Furthermore, by our knowledge, this study provides the first demonstration of PSM
traditional model during the high uncertainty period.
effectiveness in high-income markets (CZ EU). The core research question and Hypothesis 1
We argue that these observations indicate the importance of context and specific
receive support, indicating that the implementation of PSMs expedites responsible access to
circumstances in credit risk assessment, underscoring the need for adaptable models that can
finance for sole-traders and micro-organizations. By harnessing dynamic psychometric data
respond effectively to varying conditions.
and FinTech innovation, this evidence contributes to advancing financial inclusion for
MSMEs and sub-sectors in increased accuracy for predicting credit risk factors, beyond the
6.4.6. Summary of results
capabilities of TCSMs.
The study examined the relationship between psychometric attributes and credit arrears,
finding strong negative correlations between higher financial skills and lower arrears. The
Specifically, our findings suggest that adopting PSMs results in higher acceptance rates,
Psychometric Scoring Model (PSM) demonstrated acceptable discriminatory power in
especially under extreme market and global volatility, while simultaneously leading to
predicting arrears for small business sole-trader customers, with an emphasis on sensitivity.
significantly lower defaults and, consequently, increased profits for further lending. A closer
During a stress test in the state of emergency (March-November 2020), the PSM maintained
116663 164

Responsible Access to Credit for Sole-Traders and
Micro-organizations under Unstable Market Conditions with Psychometrics
its capabilities and displayed remarkable accuracy in predicting good customers. A
counterfactual analysis (CFA) showed that the PSM increased acceptance rates and reduced
Table 12 default rates, making it a promising tool for enhancing access to finance for small businesses.
However, results during the stress test period varied between micro-organizations and sole
PSM/ TCSM per sector both period default rates traders, emphasizing the importance of context and adaptable models in credit risk
assessment. This study underscores the potential of psychometric attributes in credit risk
PSM Traditional score assessment and the flexibility offered by the PSM in adapting to changing circumstances.
State Predicted State Predicted
Total Period Micro Organisation Actual no default default Actual no default default
no default 274 196 470no default 470 /
default 16 21 37default 37 /
Total 290 217 507Total 507 507 6.5 Discussion and Conclusion
bad rate 5,52%bad rate 7,30% In an environment of growing macroeconomic volatility, increasingly complex financial
Sole Trader Actual no default default Actual no default default
products, and a widening access to finance gap for small businesses, this research explores
no default 143 145 288no default 288 /
default 12 19 31default 31 / whether a novel financial literacy-based psychometric credit scoring model (PSM) can
Total 155 164 319Total 319 319
bad rate 7,74%bad rate 9,72% effectively address the access to finance challenges faced by small businesses, including sole
traders and micro-organizations, in unstable market environments. Therefore, incorporating
PSM Traditional score
Predicted Predicted dynamic psychometric data into the application process of a Czech fintech lender indicates
State-of-emergency Micro-Organisation Actual no default default Actual no default default the potential to improve financial inclusion in this sector and support the growth of small and
no default 73 90 163no default 163 /
default 4 2 6default 6 / medium-sized enterprises (SMEs). Our results provide support for our first hypothesis (H1),
Total 77 92 169Total 169 169 indicating that the psychometric credit scoring model (PSM) offers an opportunity to
bad rate 5,19%bad rate 3,55%
Sole Trader Actual no default default Actual no default default responsibly expedite access to finance for self-employed individuals and micro-organizations
no default 97 76 173no default 173 / in the Czech Republic by assessing applicants' likelihood of credit default and reducing credit
default 4 10 14default 14 /
Total 101 86 187Total 187 187 risk for lenders.
bad rate 3,96%bad rate 7,49%
Notably, the PSM outperformed traditional Credit Scoring Models (TCSMs) in identifying
We repeated the Counterfactual Analysis (CFA) to subject the results to a stress test and
risky customers throughout the entire pandemic period from August 19, 2019, to February 12,
validate the default rates for both sectors during the period of extreme uncertainty,
2022. To assess the robustness of our model, we conducted specific stress tests during the
characterized by the 'state of emergency' due to COVID-19. Table 11 demonstrates that the
"state of emergency" period at the COVID-outbreak between March 2020 and November
PSM continued to exhibit higher acceptance rates during the state of emergency period from
2020. Our findings suggest that the PSM also effectively distinguishes good from bad
March 2020 to November 2020 (48.5% for micro-organisations versus 51,4% for sole
payment behavior of small busines entrepreneurs, including sole traders and micro-
traders). However, table 12 reveals contrasting outcomes: the PSM exhibited a 46.2% higher
organizations in this period of high stress. These findings align with previous evidence
default rate for micro-organizations while demonstrating a 47.1% lower default rate for self-
advocating for the inclusion of psychometric factors to enhance credit scoring decision-
employed individuals (3.96% versus 7.49%).
making processes (Goel & Rastogi, 2023; Djeundje et al., 2021; Liberati & Camillo, 2018;
As we delve into the stress-tested situation for the 'state of emergency' during the COVID-19
Dlogish et al., 2017; Klinger, 2013).
period, we find that our findings hold firm for self-employed individuals. In this context, the
PSM consistently outperforms the traditional CSM, resulting in a notably lower default rate.
To the best of our knowledge, this study provides the first evidence that PSMs improve
However, the scenario differs for micro-organizations, where the stress-test results reveal a
credit accessibility for underserved MSMEs and sub-sectors during high market volatility
PSM default rate of 5.19%, which is 46% higher than the traditional CSM default rate.
within the Czech Republic, Europe. Such evidence carries particular significance for global
Several factors may contribute to this discrepancy, including potential model bias due to the
MSMEs, given the continually shifting macroeconomic landscape and the growing gap in
limited number of defaults observed (N=6), as indicated in Table 12. Another plausible
access to finance for sole-traders and micro-organizations.
explanation could be the implementation of more rigorous management oversight on the
Furthermore, by our knowledge, this study provides the first demonstration of PSM
traditional model during the high uncertainty period.
effectiveness in high-income markets (CZ EU). The core research question and Hypothesis 1
We argue that these observations indicate the importance of context and specific
receive support, indicating that the implementation of PSMs expedites responsible access to
circumstances in credit risk assessment, underscoring the need for adaptable models that can
finance for sole-traders and micro-organizations. By harnessing dynamic psychometric data
respond effectively to varying conditions.
and FinTech innovation, this evidence contributes to advancing financial inclusion for
MSMEs and sub-sectors in increased accuracy for predicting credit risk factors, beyond the
6.4.6. Summary of results
capabilities of TCSMs.
The study examined the relationship between psychometric attributes and credit arrears,
finding strong negative correlations between higher financial skills and lower arrears. The
Specifically, our findings suggest that adopting PSMs results in higher acceptance rates,
Psychometric Scoring Model (PSM) demonstrated acceptable discriminatory power in
especially under extreme market and global volatility, while simultaneously leading to
predicting arrears for small business sole-trader customers, with an emphasis on sensitivity.
significantly lower defaults and, consequently, increased profits for further lending. A closer
During a stress test in the state of emergency (March-November 2020), the PSM maintained
163 116647

Chapter 6
examination by sector over the total period (August 2019 – February 2020) reveals that the
PSM enhances access to finance versus TCSM for micro-organizations when compared to
sole-traders (a 115% increase vs. a 23% decrease). Moreover, PSM defaults rates are notably
lower during this total research period (6.3% PSM default rate versus 8.3% TCSM default
rate).
Furthermore, in the effort to narrow the access to finance gap in uncertain markets marked by
cautious credit risk management, the PSM outperforms traditional CSMs for underserved
small business segments, achieving a significantly higher acceptance rate (48.5% for micro-
organizations versus to 51.4% for sole traders) during the challenging state of emergency
period (March 2020 – November 2020). In developing a new PSM model for MSME lending
based on constructs drawn from financial literacy and skills literature, PSM explored how
psychometric attributes are related to instances of arrears (Van Thiel et al. 2023, Struckell et
al., 2022; Lusardi et al., 2021; Klapper & Lusardi 2020; Lusardi 2019). Consistent with
earlier research, the findings support H0a and H0c, as the constructs incorporated in the
PSM, indicating that higher levels of financial skills are associated with reduced instances of
arrears, while higher levels of debt attitudes are linked to increased arrears (Struckell et al.,
2022; Lusardi et al., 2021; Klapper & Lusardi 2020; Lusardi 2019).
The PSM contributions to research examining the relationship between psychometric
attributes of applicants, and the likelihood of late payment of debt and arrears accrual,
whereas previous research primarily examined the connection between these attributes and
overall debt levels or financial education needs. We found partial support for H0b and H0g,
suggesting that higher levels of self-efficacy and social desirability are associated with a
decrease in arrears. Moreover, prior research had identified a relationship between these
psychometric attributes and debt but failed to specifically explore their predictive power
regarding the likelihood of debt repayment based on individual characteristics and traits
(Nosić & Weber, 2010; Yang et al., 2007; Dans & Haberman, 2007; Seaward & Kemp, 2000;
Norvilitis et al., 2006; Ganster, Hennesey, & Luthans 1983).
We reject H0d, H0e, and H0f as evidence did not support a significant relationship between
materialism, gratification, fluid intelligence, and instances of arrears. The summarized results
of hypotheses testing are displayed in Table 13.
116685

Responsible Access to Credit for Sole-Traders and
Micro-organizations under Unstable Market Conditions with Psychometrics
Table 13
Research findings
Hypothesis Hypothesis Conclusion Result 1 Result 2 Literature
number
H0 Hy n p u o m th b e e s r is There is no significanHty dpiofftheeresins ce between the RejCeocntceludsion H0a/ H0Rce asuclcte 1pted H0b/ H0Rge spualtr t2ly Goel & Ratogi, 202L3i;t eDrajetuurnedje et al. 2021;
psychometric attributes and arrears. accepted Liberati & Camillo, 2018; Dlogish et al. 2017;
H0 T at h tr e ib re ut i e s s n an o d s a ig rr n e i a f r ic s a . ntdifferencebetweenthepsychometric Rejected H0a/ H0c accepted H0b/ H0g partly acceptedKG & ino C eg a le m &r, i R l 2 l a o 0t , 1 o 2 3g 0 i; 1 , 8 2 ; 0 D 23 lo ; g D is je h u e n t d a je l. e 2 t 0 a 1 l 7 . ; 2 K 0 i 2 n 1 g ; e L r i , b 2 e 0 r 1 a 3 ti ;
H0a Low levels of finanical skills increases arrears. Accepted Negative relation Significant correlationStruckell et al., 2022; Lussardi et al., 2021;
Accepted Negative relation SKtlraupcpkeelrl e&t aLl.u, s2s0a2r2d; iL 2u0ss2a0rd; iL eut saal.r, d2i0 2201;1 K9lapper
H0bH0a LoHwig lhe vleelvs eolfs foinfa sneiclfa-le sffikilclsa cinyc r(ecaosnefisd aerrnecaers). increases Partly Negative relation SiSgingnifiifcicaanntt ccoorrrreellaattiioonn&N oLsuisćs &ar dWi 2e0b2e0r;, L 2u0s1ar0d;i Y2a0n19g, et al., 2007; Dans
arrears. aPcacrtelyp taecdcepted Negative relation N&o Hsiać b&e rWmeabner,, 22000107;; YSeanagw, aetr dal .&, 2 K0e07m; pD,a 2ns0 0&0
H0c H0b HPigohs lietivveels d oef bset-laf-ttieftfiucdaceys ( icnocnrfeidaesnecse )a irnrceraearss.es arrears. Accepted Positive relation SiSgingnifiifcicaanntt ccoorrrreellaattiioonnHAlambeermnbaen,r g2 0e0t7. ;a Sle, a2w0a2r0d; & H Kauemltapi,n 2,0 K0e0mp &
Accepted Positive relation AChlmeernnbyesrhge ent.k aol,, 22002100; Haultain, Kemp &
H0c Positive debt-attitudes increases arrears. Significant correlation Chernyshenko, 2010
H0d High levels of materialism increases arrears. Rejected Positive relation Low correlation Garðarsdóttir & Dittmar 2012; Pham et al.,
G20ar1ð2a;r sDdoótntinr e&ll yD ietttm aal.r, 2 200112;2 P; hPaimro get &al .R, o20b1e2r;t s,
Rejected Positive relation D P 2 2o 0 0 o n 0 1 n c n7 1h e: ;i l o P N ly o ao e n n r t dv ca h iA l l . i i, rti o a 2 s n 0a he 1n at 2d ,. ; a2 PA l0, ir 0 r 2 ao 80 ng ; 0 h R & 6 a i c; ,R h 2 R o in 0 i b cs e0 h, r 8 2 t i s n ; 0 , s R 1 2 1 i a 0c ; 0 n h N 7 d i: o n r s v , i litis
eDta.awl, s2o0n06, ;1 R9i9c2h;in Bs ealnkd, 1D9a8w4son, 1992; Belk, 1984
H0d High levels of materialism increases arrears. Low correlation
H0e Inmediate gratification increases arrears. Rejected Positive relation Low correlation OO’’CCoonnnnoor re et at la. 2l.0 21091; S9t;r öSmtrböämckb, äect kal,. ,e 2t0 a1l7.,; 2K0h1ar7e;
Rejected Positive relation 2K0h1a6r;e A 2c0ht1z6ig; eAr,c eht tazli.g, e20r,1 e5t; ;a Pl.h, a2u0 a1n5d; W; Pohoa, u20 a0n8d;
H0e Inmediate gratification increases arrears. Low correlation JWojoi oan, d2 0R0a8ve; eJnodjri aann, d20 R0a8veendran, 2008
H0f Higher levels of fluid intelligence decreases arrears Rejected Negative relation Low correlation MMaallkkininsskki i& & M Manadnzdiuzkiu, 2k0, 2220; 2D2j;e uDnjdejue netd ajle., e2t0 2a1l.;,
Rejected Negative relation M20u2ri1ll;o M et uarl.i l2lo0 2e0t; aMl.u 2n0oz2-0M; uMrilulon oetz a-lM., 2u0r2il0lo; et
Dall.o, g2o0s2ch0 ;e tD allo.,g 2o0s1c7h, Leitb earla.,ti 2&0 1C7am, Lililboe, 2ra0ti18 &;
H0f Higher levels of fluid intelligence decreases arrears Low correlation Camillo, 2018;
H0gH0g HHigihgehr eler vleelvse olfs soofc isaol cdieasli rdaebsiliirtay binilcirteya isnecsr eararseeasrs a.rrears. PPaarrttllyy accepted NegNaetigvaet irveel aretilaotnion SiSgingnifiifcicaanntt ccoorrrreellaattiioonn N LNu o ot r hr v va i ni l l i s t i i ti1 s 9s e 8 t e 3 a t l . a 2 l. 0 2 06 0 ; 0 G 6 a ; n G s a te n r, s H te e r n , n H es e e n y n , e & s ey, &
H1 H1 P o P i s n y f s c c y s h lm c u oh sa mo ilol em bn tr u e i o c s t i f r n c ir se ce ms dc s ir ae te sl s l d c ibn iot u r u si s n n c i g sn o t e i a rni sb nc sl r e g e e s a C in s ein ec n sr t ur et an ah l es sE e tu f a si r n b o ta lp h e n e ec aC i a n fi e l n nm ina ta c r n ra luc kle si ai t o s l n . a A c c c cA e ec p pc t te e ep d dted A n Ac a cc ti cee o ppt n atablbel ed idscirsicmriimnait-ion n Ad a cis ti cce o rip n m A t t ai ei c n n c s ba e t l s te p p i t o t re d a n er b i is si o l n s e c d rs t i e tmr s e t is- s G L L G &i u o b o t C e e e h a ll r a am && n ti i s R l R l 1 & a o a 9 t , t o C 8 2 og a0 3 gi 1m ,i 8 ,2 i; 20 l lD 20 o 3 l 2 o, ; 3 g2 D i ; 0s j eD h1 u 8 j e ne ;t du Da jne ll. d o e 2 j g t 0 e i a 1s el 7h . t ; 2 eK a0 ti l2 n . a 1 g 2 l ; e . 0L r2 i , 2b 02 1e 01 ;r 1 a 73 t ; i ;
European markets. period Kinger, 2013;
A series of counterfactual analyses (CFA) conducted between the TCSMs employed by a
Czech-based FinTech lender and the PSM reveals a significant business opportunity.
Evidence suggests the potential to increase loan applicants by >30% and reduce the
applicant default rate by >20%. The PSM results remain consistent across the period of
extreme volatility of "states of emergency" (March-November 2020). The accrued evidence
illustrates the PSM's capacity to bridge the finance gap and responsibly promote inclusion
within the underserved MSME sector, especially during periods of higher market volatility.
Aligned with prior literature, we support the inclusion of psychometrics in credit scoring
models, leading to enhancements in predictive accuracy, albeit, metrics should be clearly
defined to thoroughly test all configurations to enhance the PSMs predictive power (Goel &
Rastogi, 2023; Djeundje et al., 2021; Liberati & Camillo, 2018; Dlogish et al., 2017; Klinger,
2013). Likewise, for accuracy metrics (Accuracy, Precision, Recall, F1; Yang & Berdine,
2017; Schisterman et al., 2005; Altman & Bland, 1994), we conducted live and automated
application design, and provide insights into the potential business growth for the Financial
Services/FinTech lender.
At a granular level, this study demonstrates the first investigation that PSMs facilitate access
to finance for MSMEs and sub-sectors of sole traders and micro-organizations, especially
during market volatility where traditional credit data may be unreliable and/or unavailable.
Prior research has explored the application of psychometric scoring in low-income markets
(Goel & Rastogi, 2023; Klinger, 2013), we are, to the best of our knowledge, the first to
illustrate its business impact in a high-income European market (Czech Republic). In the
current macroeconomic environment, as Europe teeters on the edge of a recession, lenders are
more risk averse in scrutinizing the quality of their investment portfolios while aiming to
reach valuable yet underserved customer sectors.
We argue that the PSM represents the first steps towards developing informed and
responsible small business lending practices, enabling profitable and sustainable growth
strategies, particularly during current and future periods of instability. Albeit, that there are
116669

Chapter 6
limitations of this study, we call for further research to extend and contribute evidence to the
evolution of PSMs in promote fairer and transparent lending. We now turn to address these
issues.
6.6 Limitations and Future Research
The first limitation is the generalisability of the results beyond the CZ sample and population.
That said, the PSM warrants application and testing across different upper-middle to high
income countries with increasing percentages of sole traders and micro-organizations to
examine the predictive power within and between cohorts to increase financial inclusion and
promote growth in these MSME sectors (i.e., UK, France, Germany, etc.).
Second, the study investigated the PSM performance during periods of unprecedented
volatility and financial instability caused by the COVID-19 pandemic. Entrepreneurs, and
risk managers across the world experienced financial shock, necessitating new risk
assessment strategies to develop to account for the ‘new normal’ (McKinsey, 2022). We
recommend performing additional research in the post-covid era to validate the robustness of
the PSM across differing time frames and financial market conditions.
Third, the series of CFAs to stress test the PSM against the performance of TCSMs produced
evidence in support of prior studies integrating psychometric data with traditional and
alternative credit data to facilitate responsible and fair credit decision-making processes from
lenders (Goel & Ratogi, 2023; Djeundje et al. 2021; Liberati & Camillo, 2018; Dlogish et al.
2017; Kinger, 2013). Nonetheless, it's essential to acknowledge the relatively limited sample
size, consisting of 2,884 psychometric credit scores and 826 credit scores accompanied by
behavioral payment data from accepted customers. Therefore, we recommend expanding the
research sample size and enhancing the integration of psychometrics with various dynamic
open data sources for more comprehensive insights. For instance, open banking transactions,
social media, mobile phones, biometrics, and search engines to develop consumer
behavioural insights. In so doing, use and re-use of data must adhere to ethical data
standards, abiding by GDPR and similar data privacy regulations and compliance to uphold
consumer protection (Elliott et al, 2021).
Finally, as artificial intelligence (AI) models evolve, psychometric data should be considered
to address the untapped underserved and underbanked MSME sector and low income
customer segments (Van Thiel et al. 2023). This aligns to FinTech’s claims of innovation and
driving greater financial inclusion, adopting the PSM can increase access to basic bank
accounts and financial services creating an inclusive digital society (Arner et al., 2020, 2021;
Banna et al., 2021). A final caveat and suggested research avenue(s), is on the one hand,
engaging in the responsible use of dynamic data automation via AI-enabled credit scoring
(Van Thiel & Van Raaij, 2019), whilst on the other hand, ensuring that ‘we’ uphold consumer
privacy to reduce not widen the current financial and digital divide affecting citizens and
MSMEs (van Dijk, 2019; Elliott et al, 2021).
117607

Responsible Access to Credit for Sole-Traders and
Micro-organizations under Unstable Market Conditions with Psychometrics
limitations of this study, we call for further research to extend and contribute evidence to the References
evolution of PSMs in promote fairer and transparent lending. We now turn to address these
issues. Achtziger, A., Hubert, M., Kenning, P., Raab, G., & Reisch, L. (2015). Debt out of control:
The links between self-control, compulsive buying, and real debts. Journal of Economic
6.6 Limitations and Future Research Psychology, 49, 141-149.
The first limitation is the generalisability of the results beyond the CZ sample and population.
That said, the PSM warrants application and testing across different upper-middle to high Aitken, R. (2017). ‘All data is credit data’: Constituting the unbanked. Competition &
income countries with increasing percentages of sole traders and micro-organizations to Change, 21(4), 274-300.
examine the predictive power within and between cohorts to increase financial inclusion and
promote growth in these MSME sectors (i.e., UK, France, Germany, etc.). Almenberg, J., Lusardi, A., Säve‐Söderbergh, J., & Vestman, R. (2020). Attitudes toward debt
Second, the study investigated the PSM performance during periods of unprecedented and debt behavior. The Scandinavian Journal of Economics.
volatility and financial instability caused by the COVID-19 pandemic. Entrepreneurs, and https://doi.org/10.1111/sjoe.12419
risk managers across the world experienced financial shock, necessitating new risk
assessment strategies to develop to account for the ‘new normal’ (McKinsey, 2022). We Akkoç, S. (2012). An empirical comparison of conventional techniques, neural networks and
recommend performing additional research in the post-covid era to validate the robustness of the three stage hybrid Adaptive Neuro Fuzzy Inference System (ANFIS) model for credit
the PSM across differing time frames and financial market conditions. scoring analysis: The case of Turkish credit card data. European Journal of Operational
Third, the series of CFAs to stress test the PSM against the performance of TCSMs produced Research, 222(1), 168-178.
evidence in support of prior studies integrating psychometric data with traditional and
alternative credit data to facilitate responsible and fair credit decision-making processes from Altman, E. I. (1968). Financial ratios, discriminant analysis and the prediction of corporate
lenders (Goel & Ratogi, 2023; Djeundje et al. 2021; Liberati & Camillo, 2018; Dlogish et al. bankruptcy. The Journal of Finance, 23(4), 589-609.
2017; Kinger, 2013). Nonetheless, it's essential to acknowledge the relatively limited sample
size, consisting of 2,884 psychometric credit scores and 826 credit scores accompanied by Altman, D. G., & Bland, J. M. (1994). Diagnostic tests 3: receiver operating characteristic
behavioral payment data from accepted customers. Therefore, we recommend expanding the plots. BMJ: British Medical Journal, 309(6948), 188.
research sample size and enhancing the integration of psychometrics with various dynamic
open data sources for more comprehensive insights. For instance, open banking transactions, Ang, J. S. (1991). Small business uniqueness and the theory of financial
social media, mobile phones, biometrics, and search engines to develop consumer management. Journal of Small Business Finance, 1(1), 1-13.
behavioural insights. In so doing, use and re-use of data must adhere to ethical data
standards, abiding by GDPR and similar data privacy regulations and compliance to uphold Ang, J. S. (1992). On the theory of finance for privately held firms. The Journal of
consumer protection (Elliott et al, 2021). Entrepreneurial Finance, 1(3), 185-203.
Finally, as artificial intelligence (AI) models evolve, psychometric data should be considered
to address the untapped underserved and underbanked MSME sector and low income Agarwal, P., & Alam, M. (2020). A lightweight deep learning model for human activity
customer segments (Van Thiel et al. 2023). This aligns to FinTech’s claims of innovation and recognition on edge devices. Procedia Computer Science, 167, 2364-2373.
driving greater financial inclusion, adopting the PSM can increase access to basic bank
accounts and financial services creating an inclusive digital society (Arner et al., 2020, 2021; Arner, D.W., Buckley, R.P., Zetzsche, D.A. et al. (2020). Sustainability, FinTech and
Banna et al., 2021). A final caveat and suggested research avenue(s), is on the one hand, Financial Inclusion. Eur Bus Org Law Rev 21, 7–35.
engaging in the responsible use of dynamic data automation via AI-enabled credit scoring
(Van Thiel & Van Raaij, 2019), whilst on the other hand, ensuring that ‘we’ uphold consumer Arner, D. W., Buckley, R. P., & Zetzsche, D. A. (2021). Open banking, open data, and open
privacy to reduce not widen the current financial and digital divide affecting citizens and finance: lessons from the European union. Forthcoming in Linda Jeng (ed), Open Banking
MSMEs (van Dijk, 2019; Elliott et al, 2021). (Oxford University Press, 2021), 21-69.
Arráiz, I., Bruhn, M., & Stucchi, R. (2017). Psychometrics as a model to improve credit
information. The World Bank Economic Review, 30(Supplement_1), S67-S76.
Azma, N., Rahman, M., Adeyemi, A. A., & Rahman, M. K. (2019). Propensity toward
indebtedness: Evidence from Malaysia. Review of Behavioral Finance.
Baesens, B., Setiono, R., Mues, C., & Vanthienen, J. (2003). Using neural network rule
extraction and decision tables for credit-risk evaluation. Management Science, 49(3), 312-
329.
167 116781

Chapter 6
Baesens, B., Roesch, D., & Scheule, H. (2016). Credit risk analytics: Measurement
techniques, applications, and examples in SAS. John Wiley & Sons
Baker, T. H., & Judge, K. (2020). How to help small businesses survive COVID-
19. Columbia Law and Economics Working Paper, (620).
Bakhtiari, S., Breunig, R., Magnani, L., & Zhang, J. (2020). Financial constraints and small
and medium enterprises: A Review. Economic Record, 96(315), 506-523.
Bandura, A. (1986). The explanatory and predictive scope of self-efficacy theory. Journal of
Social and Clinical Psychology, 4(3), 359-373.
Banna, H., Hassan, M.K., & Rashid, M. (2021). Fintech-based financial inclusion and bank
risk-taking: Evidence from OIC countries. Journal of International Financial Markets,
Institutions and Money, 75: 101447.
Bartolacci, F., Caputo, A., & Soverchia, M. (2020). Sustainability and financial performance
of small and medium sized enterprises: A bibliometric and systematic literature
review. Business Strategy and the Environment, 29(3), 1297-1309.
Belk, R. W. (1984). Three scales to measure constructs related to materialism: Reliability,
validity, and relationships to measures of happiness. ACR North American Advances.
Bergen, N., & Labonté, R. (2020). “Everything is perfect, and we have no problems”:
detecting and limiting social desirability bias in qualitative research. Qualitative Health
Research, 30(5), 783-792.
Bernards, N. (2019). The poverty of fintech? Psychometrics, credit infrastructures, and the
limits of financialization. Review of International Political Economy, 26(5), 815-838.
Biallas, M., & O'Neill, F. (2020). Artificial Intelligence Innovation in Financial Services.
Bocanet, A., Alpenidze, O. & Badran, O. (2021). Business analysis in post-pandemic era.
Academy of Strategic Management Journal, 4, pp.1-9.
Boot, A. W., Hoffmann, P., Laeven, L., & Ratnovski, L. (2020). Financial intermediation and
technology: What's old, what's new?.
Breza, E., Kanz, M., & Klapper, L. F. (2020). Learning to navigate a new financial
technology: Evidence from payroll accounts (No. w28249). National Bureau of Economic
Research.
Brown, S., Garino, G., & Taylor, K. (2013). Household debt and attitudes toward risk. Review
of Income and Wealth, 59(2), 283-304.
Capon, N. (1982). Credit scoring systems: A critical analysis. Journal of Marketing, 46(2),
82-91.
Carpenter, R. E., & Petersen, B. C. (2002). Is the growth of small firms constrained by
internal finance?. Review of Economics and statistics, 84(2), 298-309.
117629

Responsible Access to Credit for Sole-Traders and
Micro-organizations under Unstable Market Conditions with Psychometrics
Baesens, B., Roesch, D., & Scheule, H. (2016). Credit risk analytics: Measurement
techniques, applications, and examples in SAS. John Wiley & Sons Chen, P. Y., Chen, C. L., Hsu, Y. C., & Tseng, W. Y. I. (2020). Fluid intelligence is associated
with cortical volume and white matter tract integrity within multiple-demand system across
Baker, T. H., & Judge, K. (2020). How to help small businesses survive COVID- adult lifespan. NeuroImage, 212, 116576.
19. Columbia Law and Economics Working Paper, (620).
Chittenden, F., Hall, G., & Hutchinson, P. (1996). Small firm growth, access to capital
Bakhtiari, S., Breunig, R., Magnani, L., & Zhang, J. (2020). Financial constraints and small markets and financial structure: Review of issues and an empirical investigation. Small
and medium enterprises: A Review. Economic Record, 96(315), 506-523. Business Economics, 59-67.
Bandura, A. (1986). The explanatory and predictive scope of self-efficacy theory. Journal of Cohen, J. (1988). Set correlation and contingency tables. Applied psychological
Social and Clinical Psychology, 4(3), 359-373. Measurement, 12(4), 425-434.
Banna, H., Hassan, M.K., & Rashid, M. (2021). Fintech-based financial inclusion and bank Corrales-Garay, D., Mora-Valentín, E. M., & Ortiz-de-Urbina-Criado, M. (2019). Open data
risk-taking: Evidence from OIC countries. Journal of International Financial Markets, for open innovation: An analysis of literature characteristics. Future Internet, 11(3), 77.
Institutions and Money, 75: 101447.
Dans, S. M., & Haberman, H. R. (2007). Teen financial knowledge, self-ef- ficacy, and
Bartolacci, F., Caputo, A., & Soverchia, M. (2020). Sustainability and financial performance behavior: A gendered view. Journal of Financial Counseling and Planning, 18(2), 13.
of small and medium sized enterprises: A bibliometric and systematic literature Retrieved from https://ssrn.com/abstr act=2228406
review. Business Strategy and the Environment, 29(3), 1297-1309.
Dasewicz, A., Simon, J. and Ramanujam, S.R. (2020). Financing small business is critical for
Belk, R. W. (1984). Three scales to measure constructs related to materialism: Reliability, a strong post-covid recovery. Center for Strategic and International Studies (CSIS).
validity, and relationships to measures of happiness. ACR North American Advances.
Dealroom 2023. https://dealroom.co/uploaded/2023/01/Fintech-2022-recap.pdf?x35994.
Bergen, N., & Labonté, R. (2020). “Everything is perfect, and we have no problems”: Accessed May 2023.
detecting and limiting social desirability bias in qualitative research. Qualitative Health
Research, 30(5), 783-792. De Cnudde, S., Moeyersoms, J., Stankova, M., Tobback, E., Javaly, V., & Martens, D. (2019).
What does your Facebook profile reveal about your creditworthiness? Using alternative data
Bernards, N. (2019). The poverty of fintech? Psychometrics, credit infrastructures, and the for microfinance. Journal of the Operational Research Society, 70(3), 353-363.
limits of financialization. Review of International Political Economy, 26(5), 815-838.
Demirel, P., & Parris, S. (2015). Access to finance for innovators in the UK's environmental
Biallas, M., & O'Neill, F. (2020). Artificial Intelligence Innovation in Financial Services. sector. Technology Analysis & Strategic Management, 27(7), 782-808.
Bocanet, A., Alpenidze, O. & Badran, O. (2021). Business analysis in post-pandemic era. Demirguc-Kunt, A., Klapper, L., Singer, D., & Ansar, S. (2018). The Global Findex Database
Academy of Strategic Management Journal, 4, pp.1-9. 2017: Measuring financial inclusion and the fintech revolution. World Bank Publications.
Boot, A. W., Hoffmann, P., Laeven, L., & Ratnovski, L. (2020). Financial intermediation and Dew, J., & Xiao, J. J. (2011). The financial management behavior scale: Development and
technology: What's old, what's new?. validation. Journal of Financial Counseling and Planning, 22(1), 43.
Breza, E., Kanz, M., & Klapper, L. F. (2020). Learning to navigate a new financial Djeundje, V. B., Crook, J., Calabrese, R., & Hamid, M. (2021). Enhancing credit scoring with
technology: Evidence from payroll accounts (No. w28249). National Bureau of Economic alternative data. Expert Systems with Applications, 163, 113766.
Research.
Dlogosch, T. J., Klinger, B., & Frese, M. (2017). Personality-based selection of
Brown, S., Garino, G., & Taylor, K. (2013). Household debt and attitudes toward risk. Review entrepreneurial borrowers to reduce credit risk: two studies on prediction models in low and
of Income and Wealth, 59(2), 283-304. high-stakes settings in developing countries. Journal of Organisational Behaviour, 39, 612-
628.
Capon, N. (1982). Credit scoring systems: A critical analysis. Journal of Marketing, 46(2),
82-91. Donnelly, G., Iyer, R., & Howell, R. T. (2012). The Big Five personality traits, material
values, and financial well-being of self-described money managers. Journal of Economic
Carpenter, R. E., & Petersen, B. C. (2002). Is the growth of small firms constrained by Psychology, 33(6), 1129-1142.
internal finance?. Review of Economics and statistics, 84(2), 298-309.
169 117703

Chapter 6
Eggers, F. (2020). Masters of disasters? Challenges and opportunities for MSMEs in times of
crisis. Journal of Business Research, 116, 199-208.
Elliott, K., Coopamootoo, K., Curran, E., Ezhilchelvan, P., Finnigan, S., Horsfall, D.,
Zhichao, M, Ng, M., Spiliotopoulos, T., Wu, H., and van Moorsel, A. (2022). Know Your
Customer: Balancing Innovation and Regulation for Financial Inclusion, Data and Policy, 4:
e34. https://www.doi.org/10.1017/dap.2022.23
Elliott, K., Price, R., Shaw, P., Spiliotopoulos, T., Ng, M., Coopamootoo, K., and van
Moorsel, A. (2021) Towards an Equitable Digital Society: Artificial Intelligence (AI) and
Corporate Digital Responsibility (CDR), Springer Nature: Society
https://doi.org/10.1007/s12115-021-00594-8
https://link.springer.com/content/pdf/10.1007/s12115-021-00594-8.pdf
Fawcett, J. (2005). Criteria for evaluation of theory. Nursing science quarterly, 18(2), 131-
135.
Financial Conduct Authority (FCA), (2019). Guidance for firms on the fair treatment of
vulnerable customers, Guidance Consultation GC19/3. (Available: https://www.fca.org.uk/).
Financial Conduct Authority (FCA), (2021). Guidance for firms on the fair treatment of
vulnerable customers, FG21/1.
Financial Conduct Authority (FCA), (2022). A new Consumer Duty Feedback to CP21/36
and final rules, Policy Statement PS22/9. (Available: https://www.fca.org.uk/).
Fisher, R. A. (1936). The use of multiple measurements in taxonomic problems. Annals of
eugenics, 7(2), 179-188.
Fuhrer, C., Solem, J. E., & Verdier, O. (2021). Scientific Computing with Python: High-
performance scientific computing with NumPy, SciPy, and pandas. Packt Publishing Ltd.
Ganster, D. C., Hennessey, H. W., & Luthans, F. (1983). Social desirability response effects:
Three alternative models. Academy of Management Journal, 26(2), 321-331.
Garðarsdóttir, R. B., & Dittmar, H. (2012). The relationship of materialism to debt and
financial well-being: The case of Iceland’s perceived prosperity. Journal of Economic
Psychology, 33(3), 471–481. https://doi.org/10.1016/j.joep.2011.12.008
Gerke, O., & Zapf, A. (2022). Convergence Behavior of Optimal Cut-Off Points Derived
from Receiver Operating Characteristics Curve Analysis: A Simulation Study. Mathematics,
10(22), p.4206.
Gibson, B. (1992). Financial information for decision-making: An alternative small firm
perspective. The Journal of Entrepreneurial Finance, 1(3), 221-232.
Goel, A., & Rastogi, S. (2023). Credit scoring of small and medium enterprises: a behavioural
approach. Journal of Entrepreneurship in Emerging Economies, 15(1), 46-69.
117741

Responsible Access to Credit for Sole-Traders and
Micro-organizations under Unstable Market Conditions with Psychometrics
Eggers, F. (2020). Masters of disasters? Challenges and opportunities for MSMEs in times of  Goyal, K., & Kumar, S. (2021). Financial literacy: A systematic review and bibliometric
crisis. Journal of Business Research, 116, 199-208.  analysis. International Journal of Consumer Studies, 45(1), 80-105.
|     |     |     |     |
| --- | --- | --- | --- |
Elliott, K., Coopamootoo, K., Curran, E., Ezhilchelvan, P., Finnigan, S., Horsfall, D.,  Gupta, H., & Barua, M. K. (2018). A framework to overcome barriers to green innovation in
Zhichao, M, Ng, M., Spiliotopoulos, T., Wu, H., and van Moorsel, A. (2022). Know Your  MSMEs using BWM and Fuzzy TOPSIS. Science of the Total Environment, 633, 122-139
Customer: Balancing Innovation and Regulation for Financial Inclusion, Data and Policy, 4:
e34. https://www.doi.org/10.1017/dap.2022.23   Guariglia, A., Liu, X., & Song, L. (2011). Internal finance and growth: Microeconometric
  evidence on Chinese firms. Journal of Development Economics, 96(1), 79-94.
Elliott, K., Price, R., Shaw, P., Spiliotopoulos, T., Ng, M., Coopamootoo, K., and van
Moorsel, A. (2021) Towards an Equitable Digital Society: Artificial Intelligence (AI) and  Hall, G. C., & Hutchinson, P. J. (1993). A probit analysis of the changes in the financial
Corporate Digital Responsibility (CDR), Springer Nature: Society  characteristics of newly quoted small firms, 1970–73 and 1980–83. Small Business
https://doi.org/10.1007/s12115-021-00594-8    Economics, 5, 207-214.
https://link.springer.com/content/pdf/10.1007/s12115-021-00594-8.pdf
  Hamilton, R. T., & Fox, M. A. (1998). The financing preferences of small firm
Fawcett, J. (2005). Criteria for evaluation of theory. Nursing science quarterly, 18(2), 131- owners. International Journal of Entrepreneurial Behavior & Research.
| 135.  |     |     |     |
| ----- | --- | --- | --- |
  Hendricks, M. K., & Budree, A. (2019). Can a mobile credit-scoring model provide better
Financial Conduct Authority (FCA), (2019). Guidance for firms on the fair treatment of  accessibility to South African citizens requiring micro-lending?. International Journal of
vulnerable customers, Guidance Consultation GC19/3. (Available: https://www.fca.org.uk/).   Electronic Finance, 9(3), 157-169.
|     |     |     |     |
| --- | --- | --- | --- |
Financial Conduct Authority (FCA), (2021). Guidance for firms on the fair treatment of  Hutchinson, J., & Xavier, A. (2006). Comparing the impact of credit constraints on the
vulnerable customers, FG21/1.  growth of MSMEs in a transition country with an established market economy. Small
|     |     | Business Economics, 27, 169-179.  |     |
| --- | --- | --------------------------------- | --- |
Financial Conduct Authority (FCA), (2022). A new Consumer Duty Feedback to CP21/36
and final rules, Policy Statement PS22/9. (Available: https://www.fca.org.uk/).  Haultain, S., Kemp, S., & Chernyshenko, O. S. (2010). The structure of attitudes to student
|     |     | debt. Journal of Economic Psychology, 31(3), 322–330.  |     |
| --- | --- | ------------------------------------------------------ | --- |
Fisher, R. A. (1936). The use of multiple measurements in taxonomic problems. Annals of  https://doi.org/10.1016/j.joep.2010.01.003
| eugenics, 7(2), 179-188.  |     |     |     |
| ------------------------- | --- | --- | --- |
  Henley, W., & Hand, D. J. (1996). AK‐Nearest‐Neighbour Classifier for Assessing Consumer
Fuhrer, C., Solem, J. E., & Verdier, O. (2021). Scientific Computing with Python: High- Credit Risk. Journal of the Royal Statistical Society: Series D (The Statistician), 45(1), 77-95.
performance scientific computing with NumPy, SciPy, and pandas. Packt Publishing Ltd.
|     |     | Hlomane, (2022).  |     |
| --- | --- | ----------------- | --- |
Ganster, D. C., Hennessey, H. W., & Luthans, F. (1983). Social desirability response effects:  https://www.mzv.cz/pretoria/en/economic_and_commercial_information/czech_success_stor
Three alternative models. Academy of Management Journal, 26(2), 321-331.  y_in_the_fintech_and_e.html
|     |     |     |     |
| --- | --- | --- | --- |
Garðarsdóttir, R. B., & Dittmar, H. (2012). The relationship of materialism to debt and  Huang, C. L., Chen, M. C., & Wang, C. J. (2007). Credit scoring with a data mining approach
financial well-being: The case of Iceland’s perceived prosperity. Journal of Economic  based on support vector machines. Expert systems with applications, 33(4), 847-856.
Psychology, 33(3), 471–481. https://doi.org/10.1016/j.joep.2011.12.008
  Hughes, A. (1997). Finance for MSMEs: A UK perspective. Small Business Economics, 9,
Gerke, O., & Zapf, A. (2022). Convergence Behavior of Optimal Cut-Off Points Derived  151-168.
from Receiver Operating Characteristics Curve Analysis: A Simulation Study. Mathematics,
10(22), p.4206.  Istrate, E., & Harris, J. (2017). The future of work: The rise of the gig economy. National
|     |     | Association of Counties.  |     |
| --- | --- | ------------------------- | --- |
Gibson, B. (1992). Financial information for decision-making: An alternative small firm
perspective. The Journal of Entrepreneurial Finance, 1(3), 221-232.  Jiang, Z. Q., Xie, W. J., Zhou, W. X., & Sornette, D. (2019). Multifractal analysis of financial
  markets: a review. Reports on Progress in Physics, 82(12), 125901.
Goel, A., & Rastogi, S. (2023). Credit scoring of small and medium enterprises: a behavioural
approach. Journal of Entrepreneurship in Emerging Economies, 15(1), 46-69.  Joji, N. A., & Raveendran, P. T. (2008). Does Compulsive Buying Affect Credit Card
|     |     | Defaults?. Vision, 12(4), 23-32.  |     |
| --- | --- | --------------------------------- | --- |

|     | 171  |     | 117725  |
| --- | ---- | --- | ------- |

Chapter 6
Jordan, J., Lowe, J., & Taylor, P. (1998). Strategy and financial policy in UK small
firms. Journal of Business Finance & Accounting, 25(1‐2), 1-27.
Khare, A. (2014). Money attitudes, materialism, and compulsiveness: Scale development and
validation. Journal of Global Marketing, 27(1), 30-45.
Khare, A. (2016). Money attitudes, credit card and compulsive buying behaviour: a study on
Indian consumers. International Journal of Business Competition and Growth, 5(1-3), 49-71.
Kässi, O., & Lehdonvirta, V. (2018). Online labour index: Measuring the online gig economy
for policy and research. Technological Forecasting and Social Change, 137, 241-248.
Klapper, L., & Lusardi, A. (2020). Financial literacy and financial resilience: Evidence from
around the world. Financial Management, 49(3), 589-614.
Klinger, B., Khwaja, A., & LaMonte, J. (2013). Improving credit risk analysis with
psychometrics in Peru. Inter-American Development Bank. Technical Note No. IDB-TN-587.
Klinger, B., Castro, L., Szenkman, P., & Khwaja, A. (2013). Unlocking MSME finance in
Argentina with psychometrics. IDB Technical Note.
LeCun, Y., Bengio, Y., & Hinton, G. (2015). Deep learning. Nature, 521(7553), 436-444.
Lee, T. S., & Chen, I. F. (2005). A two-stage hybrid credit scoring model using artificial
neural networks and multivariate adaptive regression splines. Expert Systems with
applications, 28(4), 743-752.
Lessmann, S., Baesens, B., Seow, H. V., & Thomas, L. C. (2015). Benchmarking state-of-the-
art classification algorithms for credit scoring: An update of research. European Journal of
Operational Research, 247(1), 124-136.
Liberati, C., & Camillo, F. (2018). Personal values and credit scoring: new insights in the
financial prediction. Journal of the Operational Research Society, 69(12), 1994-2005.
Liu, X., Wang, T., Ding, W., Liu, Y., & Xu, Q. A (2017) A Credit Scoring Model Based on
Alternative Mobile Data for Financial Inclusion. In: Proceedings of the 2017 Credit Scoring
and Credit Control Conference, Edinburgh, UK (Vol. 30).
Long, G., Tan, Y., Jiang, J., & Zhang, C. (2020). Federated learning for open banking.
In Federated Learning: Privacy and Incentive (pp. 240-254). Cham: Springer International
Publishing.
Lopez-Gracia, J., & Aybar-Arias, C. (2000). An empirical approach to the financial behaviour
of small and medium sized companies. Small Business Economics, 14, 55-63.
Luo, C., Wu, D., & Wu, D. (2017). A deep learning approach for credit scoring using credit
default swaps. Engineering Applications of Artificial Intelligence, 65, 465-470.
Lusardi, A. (2019). Financial literacy and the need for financial education: evidence and
implications. Swiss Journal of Economics and Statistics, 155(1), 1-8.
117763

Responsible Access to Credit for Sole-Traders and
Micro-organizations under Unstable Market Conditions with Psychometrics
Jordan, J., Lowe, J., & Taylor, P. (1998). Strategy and financial policy in UK small
firms. Journal of Business Finance & Accounting, 25(1‐2), 1-27.  Lusardi, A., & Mitchell, O. S. (2007). Financial literacy and retirement planning: New
  evidence from the Rand American Life Panel. Michigan Retirement Research Center
Khare, A. (2014). Money attitudes, materialism, and compulsiveness: Scale development and  Research Paper No. WP, 157. http://dx.doi.org/10.2139/ssrn.1095869
| validation. Journal of Global Marketing, 27(1), 30-45.  |     |     |     |
| ------------------------------------------------------- | --- | --- | --- |
  Lusardi, A., & Mitchell, O. S. (2008). Planning and financial literacy: How do women
Khare, A. (2016). Money attitudes, credit card and compulsive buying behaviour: a study on  fare?. American Economic Review, 98(2), 413–417. https://doi.org/10.1257/aer.98.2.413
Indian consumers. International Journal of Business Competition and Growth, 5(1-3), 49-71.
  Lusardi, A., & Mitchell, O. S. (2011). Financial Literacy and Planning: Implications for
Kässi, O., & Lehdonvirta, V. (2018). Online labour index: Measuring the online gig economy  Retirement Wellbeing (No. w17078). National Bureau of Economic Research.
for policy and research. Technological Forecasting and Social Change, 137, 241-248.
  Lusardi, A., Hasler, A., & Yakoboski, P. J. (2021). Building up financial literacy and financial
Klapper, L., & Lusardi, A. (2020). Financial literacy and financial resilience: Evidence from  resilience. Mind & Society, 20, 181-187.
| around the world. Financial Management, 49(3), 589-614.  |     |     |     |
| -------------------------------------------------------- | --- | --- | --- |
  Mahoney, J., & Barrenechea, R. (2019). The logic of counterfactual analysis in case‐study
Klinger, B., Khwaja, A., & LaMonte, J. (2013). Improving credit risk analysis with  explanation. The British Journal of Sociology, 70(1), 306-338.
psychometrics in Peru. Inter-American Development Bank. Technical Note No. IDB-TN-587.
  Malekipirbazari, M., & Aksakalli, V. (2015). Risk assesMSMEnt in social lending via random
Klinger, B., Castro, L., Szenkman, P., & Khwaja, A. (2013). Unlocking MSME finance in  forests. Expert Systems with Applications, 42(10), 4621-4631
| Argentina with psychometrics. IDB Technical Note.  |     |     |     |
| -------------------------------------------------- | --- | --- | --- |
  Małkiński, M., & Mańdziuk, J. (2022). A review of emerging research directions in Abstract
LeCun, Y., Bengio, Y., & Hinton, G. (2015). Deep learning. Nature, 521(7553), 436-444.  Visual Reasoning. Information Fusion.
|     |     |     |     |
| --- | --- | --- | --- |
Lee, T. S., & Chen, I. F. (2005). A two-stage hybrid credit scoring model using artificial  Martínez-Camblor, P. & Pardo-Fernández, J.C. (2019). The Youden index in the generalized
neural networks and multivariate adaptive regression splines. Expert Systems with  receiver operating characteristic curve context. The International Journal of Biostatistics,
| applications, 28(4), 743-752.  |     | 15(1).  |     |
| ------------------------------ | --- | ------- | --- |
|                                |     |         |     |
Lessmann, S., Baesens, B., Seow, H. V., & Thomas, L. C. (2015). Benchmarking state-of-the- McClelland, D. 1961. The Achieving Society. Princeton, NJ: Van Nostrand.
art classification algorithms for credit scoring: An update of research. European Journal of
| Operational Research, 247(1), 124-136.  |     | Mc Kinsey 2017.  |     |
| --------------------------------------- | --- | ---------------- | --- |
  https://www.mckinsey.com/~/media/McKinsey/Industries/Financial%20Services/Our%20Insi
Liberati, C., & Camillo, F. (2018). Personal values and credit scoring: new insights in the  ghts/Data%20sharing%20and%20open%20banking/Data-sharing-and-open-banking.pdf.
financial prediction. Journal of the Operational Research Society, 69(12), 1994-2005.  Accessed May 2023
|     |     |     |     |
| --- | --- | --- | --- |
Liu, X., Wang, T., Ding, W., Liu, Y., & Xu, Q. A (2017) A Credit Scoring Model Based on  Mc Kinsey 2022.  https://www.mckinsey.com/business-functions/risk-and-resilience/our-
Alternative Mobile Data for Financial Inclusion. In: Proceedings of the 2017 Credit Scoring  insights/managing-and-monitoring-credit-risk-after-the-covid-19-pandemic. Accessed May
and Credit Control Conference, Edinburgh, UK (Vol. 30).  2023.
|     |     |     |     |
| --- | --- | --- | --- |
Long, G., Tan, Y., Jiang, J., & Zhang, C. (2020). Federated learning for open banking.  Mc Kinsey 2022. https://www.mckinsey.com/capabilities/risk-and-resilience/our-
In Federated Learning: Privacy and Incentive (pp. 240-254). Cham: Springer International  insights/covid-19-implications-for-business. Accessed May 2023.
| Publishing.  |     |     |     |
| ------------ | --- | --- | --- |
  Meier, S., & Sprenger, C. (2007). Impatience and credit behavior: evidence from a field
Lopez-Gracia, J., & Aybar-Arias, C. (2000). An empirical approach to the financial behaviour  experiment.
of small and medium sized companies. Small Business Economics, 14, 55-63.
  Mhlanga, D. (2021). Financial inclusion in emerging economies: The application of machine
Luo, C., Wu, D., & Wu, D. (2017). A deep learning approach for credit scoring using credit  learning and artificial intelligence in credit risk assesMSMEnt. International Journal of
default swaps. Engineering Applications of Artificial Intelligence, 65, 465-470.  Financial Studies, 9(3), 39.
|     |     |     |     |
| --- | --- | --- | --- |
Lusardi, A. (2019). Financial literacy and the need for financial education: evidence and  Moore, D. L. (2003). Survey of financial literacy in Washington State: Knowledge, behavior,
implications. Swiss Journal of Economics and Statistics, 155(1), 1-8.  attitudes, and experiences. Washington State Department of Financial Institutions.
|     | 173  |     | 117747  |
| --- | ---- | --- | ------- |

Chapter 6
Moscalu, M., Girardone, C., & Calabrese, R. (2020). MSMEs’ growth under financing
constraints and banking markets integration in the euro area. Journal of Small Business
Management, 58(4), 707-746.
Muñoz-Murillo, M., Álvarez-Franco, P. B., & Restrepo-Tobón, D. A. (2020). The role of
cognitive abilities on financial literacy: New experimental evidence. Journal of Behavioral
and Experimental Economics, 84, 101482.
Nosić, A., & Weber, M. (2010). How riskily do I invest? The role of risk attitudes, risk
perceptions, and overconfidence. Decision Analysis, 7(3), 282-301.
Norvilitis, J. M., Merwin, M. M., Osberg, T. M., Roehling, P. V., Young, P., & Kamas, M. M.
(2006). Personality factors, money attitudes, financial knowledge, and credit‐card debt in
college students. Journal of Applied Social Psychology, 36(6), 1395–1413.
https://doi.org/10.1111/j.0021-9029.2006.00065.x
O'Connor, G. E., Newmeyer, C. E., Wong, N. Y. C., Bayuk, J. B., Cook, L. A., Komarova, Y.,
... & Warmath, D. (2019). Conceptualizing the multiple dimensions of consumer financial
vulnerability. Journal of Business Research, 100, 421-430.
OECD 2012 https://www.oecd.org/pisa/pisaproducts/46962580.pdf . Accessed May 2023.
OECD 2023. https://one.oecd.org/document/DAF/CMF(2018)17/en/pdf. Accessed May 2023.
OECD. 2020. https://oecd.org/economy/surveys/Czech-Republic-2020-OECD-economic-
survey-overview.pdf. Accessed May 2023.
OECD 2023. https://data.oecd.org/entrepreneur/enterprises-by-business-size.htm. Accessed:
May 2023.
O'Guinn, T. C., & Faber, R. J. (1989). Compulsive buying: A phenomenological
exploration. Journal of consumer research, 16(2), 147-157.
Ong, C. S., Huang, J. J., & Tzeng, G. H. (2005). Building credit scoring models using genetic
programming. Expert systems with applications, 29(1), 41-47.
Onay, C., & Öztürk, E. (2018). A review of credit scoring research in the age of Big
Data. Journal of Financial Regulation and Compliance.
Óskarsdóttir, M., Bravo, C., Sarraute, C., Vanthienen, J., & Baesens, B. (2019). The value of
big data for credit scoring: Enhancing financial inclusion using mobile phone data and social
network analytics. Applied Soft Computing, 74, 26–39.
https://doi.org/10.1016/j.asoc.2018.10.004
Parke, A., Griffiths, M., & Irwing, P. (2004). Personality traits in pathological gambling:
Sensation seeking, deferment of gratification and competitiveness as risk factors. Addiction
Research & Theory, 12(3), 201–212. https://doi.org/10.1080/1606635310001634500
117785

Responsible Access to Credit for Sole-Traders and
Micro-organizations under Unstable Market Conditions with Psychometrics
  Paulhus, D. L. (1984). Two-component models of social desirable responding. Journal of
Moscalu, M., Girardone, C., & Calabrese, R. (2020). MSMEs’ growth under financing  Personality and Social Psychology, 46(3), 598–609.
constraints and banking markets integration in the euro area. Journal of Small Business
Management, 58(4), 707-746.  Paulhus, D. L. (2001). Socially desirable responding: The evolution of a construct. In H. I.
  Braun, D. N. Jackson, & D. E. Wiley (Eds.), The role of constructs in psychologi- cal and
Muñoz-Murillo, M., Álvarez-Franco, P. B., & Restrepo-Tobón, D. A. (2020). The role of  educational measurement (pp. 49–69). Lawrence Erlbaum.
cognitive abilities on financial literacy: New experimental evidence. Journal of Behavioral  Phau, I., & Woo, C. (2008). Understanding compulsive buying tendencies among young
and Experimental Economics, 84, 101482.  Australians: The roles of money attitude and credit card usage. Marketing Intelligence &
|     |     | Planning, 26(5), 441-458.  |     |
| --- | --- | -------------------------- | --- |
Nosić, A., & Weber, M. (2010). How riskily do I invest? The role of risk attitudes, risk
perceptions, and overconfidence. Decision Analysis, 7(3), 282-301.  Pew research center, https://www.pewresearch.org/search/gig+workers
|     |     |     |     |
| --- | --- | --- | --- |
Norvilitis, J. M., Merwin, M. M., Osberg, T. M., Roehling, P. V., Young, P., & Kamas, M. M.  Pham, T. H., Yap, K., & Dowling, N. A. (2012). The impact of financial management
(2006). Personality factors, money attitudes, financial knowledge, and credit‐card debt in  practices and financial attitudes on the relationship between materialism and compulsive
college students. Journal of Applied Social Psychology, 36(6), 1395–1413.  buying. Journal of Economic Psychology, 33(3), 461-470.
| https://doi.org/10.1111/j.0021-9029.2006.00065.x  |     |     |     |
| ------------------------------------------------- | --- | --- | --- |
  Philippon, T. (2016). The fintech opportunity (No. w22476). National Bureau of Economic
O'Connor, G. E., Newmeyer, C. E., Wong, N. Y. C., Bayuk, J. B., Cook, L. A., Komarova, Y.,  Research.
... & Warmath, D. (2019). Conceptualizing the multiple dimensions of consumer financial
vulnerability. Journal of Business Research, 100, 421-430.  Pirog, S. F., & Roberts, J. A. (2007). Personality and credit card misuse among college
  students: The mediating role of impulsiveness. Journal of Marketing Theory and
OECD 2012 https://www.oecd.org/pisa/pisaproducts/46962580.pdf . Accessed May 2023.  Practice, 15(1), 65-77.
|     |     |     |     |
| --- | --- | --- | --- |
OECD 2023. https://one.oecd.org/document/DAF/CMF(2018)17/en/pdf. Accessed May 2023.  Ponchio, M. C., & Aranha, F. (2008). Materialism as a predictor variable of low income
  consumer behavior when entering into installment plan agreements. Journal of Consumer
OECD. 2020. https://oecd.org/economy/surveys/Czech-Republic-2020-OECD-economic- Behaviour: An International Research Review, 7(1), 21-34.
| survey-overview.pdf. Accessed May 2023.  |     |     |     |
| ---------------------------------------- | --- | --- | --- |
  Richins, M. L. (2017). Materialism pathways: The processes that create and perpetuate
OECD 2023. https://data.oecd.org/entrepreneur/enterprises-by-business-size.htm. Accessed:  materialism. Journal of Consumer Psychology, 27(4), 480-499.
| May 2023.  |     |     |     |
| ---------- | --- | --- | --- |
  Richins, M. L. (2011). Materialism, transformation expectations, and spending: Implications
O'Guinn, T. C., & Faber, R. J. (1989). Compulsive buying: A phenomenological  for credit use. Journal of Public Policy & Marketing, 30(2), 141-156.
exploration. Journal of consumer research, 16(2), 147-157.
  Richins, M. L., & Dawson, S. (1992). A consumer values orientation for materialism and its
Ong, C. S., Huang, J. J., & Tzeng, G. H. (2005). Building credit scoring models using genetic  measurement: Scale development and validation. Journal of Consumer Research, 19(3), 303-
programming. Expert systems with applications, 29(1), 41-47.  316.
|     |     |     |     |
| --- | --- | --- | --- |
Onay, C., & Öztürk, E. (2018). A review of credit scoring research in the age of Big  Rishabh, K. (2022). Can open banking substitute credit bureaus. Working Paper.
| Data. Journal of Financial Regulation and Compliance.  |     |     |     |
| ------------------------------------------------------ | --- | --- | --- |
  Robison, J. (2013). How to create a culture of organizational wellbeing. Gallup Business
Óskarsdóttir, M., Bravo, C., Sarraute, C., Vanthienen, J., & Baesens, B. (2019). The value of  Journal.
big data for credit scoring: Enhancing financial inclusion using mobile phone data and social
network analytics. Applied Soft Computing, 74, 26–39.  Robson, P. J., & Bennett, R. J. (2000). MSME growth: The relationship with business advice
https://doi.org/10.1016/j.asoc.2018.10.004  and external collaboration. Small Business Economics, 15, 193-208.
|     |     |     |     |
| --- | --- | --- | --- |
Parke, A., Griffiths, M., & Irwing, P. (2004). Personality traits in pathological gambling:  Saberi, M., Mirtalaie, M. S., Hussain, F. K., Azadeh, A., Hussain, O. K., & Ashjari, B. (2013).
Sensation seeking, deferment of gratification and competitiveness as risk factors. Addiction  A granular computing-based approach to credit scoring modeling. Neurocomputing, 122, 100-
Research & Theory, 12(3), 201–212. https://doi.org/10.1080/1606635310001634500  115.
|     |      |     |         |
| --- | ---- | --- | ------- |
|     | 175  |     | 117769  |

Chapter 6
Sahay, M. R., von Allmen, M. U. E., Lahreche, M. A., Khera, P., Ogawa, M. S., Bazarbash,  Thomas, L. C., Allen, D. E., & Morkel-Kingsbury, N. (2002). A hidden Markov chain model
M., & Beaton, M. K. (2020). The promise of FinTech: Financial inclusion in the post  for the term structure of bond credit risk spreads. International Review of Financial
COVID-19 era. International Monetary Fund.  Analysis, 11(3), 311-329.
|     |     |     |     |
| --- | --- | --- | --- |
San Pedro, J., Proserpio, D., & Oliver, N. (2015, June). MobiScore: towards universal credit  Tupes, E. C., & Christal, R. E. (1992). Recurrent personality factors based on trait
scoring from mobile phone data. In international conference on user modeling, adaptation,  ratings. Journal of Personality, 60(2), 225-251.
| and personalization (pp. 195–207). Springer, Cham.  |     |     |     |
| --------------------------------------------------- | --- | --- | --- |
  Tok, Y. W., & Heng, D. (2022). Fintech: Financial Inclusion or Exclusion?. International
Seaward, H. G., & Kemp, S. (2000). Optimism bias and student debt. New Zealand Journal  Monetary Fund.
| of Psychology, 29(1), 17-19.  |     |                                                           |     |
| ----------------------------- | --- | --------------------------------------------------------- | --- |
|                               |     | Upwork 2023, https://www.upwork.com/blog/gen-z-workforce  |     |
Šebestová, J., & Sroka, W. (2020). Sustainable development goals and MSMEs decisions:
Czech Republic vs. Poland. Journal of Eastern European and Central Asian Research  Van Thiel, D., Goedee, J., Leenders, R.T.A.J. (2023). Leveraging Financial Personality for
(JEECAR), 7(1), 39-50.  Inclusive Credit Scoring Amidst Global Volatility.  Journal of Risk Management in Financial
|     |     | Institutions, Vol 17 No 1.  |     |
| --- | --- | --------------------------- | --- |
Schisterman, E. F., Perkins, N. J., Liu, A., & Bondell, H. (2005). Optimal cut-point and its
corresponding Youden Index to discriminate individuals using pooled blood  Van Thiel, D., & van Raaij, W. F. (2019). Artificial intelligence credit risk prediction: An
samples. Epidemiology, 73-81.  empirical study of analytical artificial intelligence models for credit risk prediction in a
  digital era. Journal of Risk Management in Financial Institutions, 12(3), 268–286.
Shema, A. (2019, January). Effective credit scoring using limited mobile phone data.
In Proceedings of the Tenth International Conference on Information and Communication  Verbraken, T., Bravo, C., Weber, R., & Baesens, B. (2014). Development and application of
Technologies and Development (pp. 1–11).  consumer credit scoring models using profit-based classification measures. European Journal
|     |     | of Operational Research, 238(2), 505-513.  |     |
| --- | --- | ------------------------------------------ | --- |
Snow, R. and E. Yalow. 1982. Handbook of Human Intelligence. London, UK: Cambridge
University Press.   Vives, X. (2019). Digital disruption in banking. Annual Review of Financial Economics, 11,
|     |     | 243-272.  |     |
| --- | --- | --------- | --- |
Song, L., & Zhou, Y. (2020). The COVID‐19 pandemic and its impact on the global
economy: what does it take to turn crisis into opportunity?. China & World Economy, 28(4),  Wang, G., Ma, J., Huang, L., & Xu, K. (2012). Two credit scoring models based on dual
1-25.  strategy ensemble trees. Knowledge-Based Systems, 26, 61-68.
|     |     |     |     |
| --- | --- | --- | --- |
Strömbäck, C., Lind, T., Skagerlund, K., Västfjäll, D., & Tinghög, G. (2017). Does self- Watson, J. J. (2003). The relationship of materialism to spending tendencies, saving, and
control predict financial behavior and financial well-being?. Journal of Behavioral and  debt. Journal of Economic Psychology, 24(6), 723-739.
| Experimental Finance, 14, 30-38.  |     |     |     |
| --------------------------------- | --- | --- | --- |
Struckell, E. M., Patel, P. C., Ojha, D., & Oghazi, P. (2022). Financial literacy and self  World Economic Forum 2023. https://www.weforum.org/agenda/2022/01/what-is-
employment–The moderating effect of gender and race. Journal of Business Research, 139,  sustainable-finance/. Accessed May 2023.
| 639-653.  |     |     |     |
| --------- | --- | --- | --- |
  World Trade Organisation. The world trade report 2016. “Levelling the trading field for
Squalli, J., & Wilson, K. (2014). Intelligence, creativity, and innovation. Intelligence, 46,  SME’s”. https://www.wto.org/english/res_e/booksp_e/world_trade_report16_e.pdf
| 250-257.  |     |     |     |
| --------- | --- | --- | --- |
  World Trade Organisation. The world trade report 2023.” Re-globalisation for a secure,
Tan, T., & Phan, T. Q. (2018). Social Media-Driven Credit Scoring: The Predictive Value of  inclusive and sustainable future”.
Social Structures. Available at SSRN 3217885.  https://www.wto.org/english/res_e/booksp_e/wtr23_e/wtr23_e.pdf
|     |     |     |     |
| --- | --- | --- | --- |
Tatbul, N., Lee, T.J., Zdonik, S., Alam, M. & Gottschlich, J. (2018). Precision and recall for  Wei, Y., Yildirim, P., Van den Bulte, C., & Dellarocas, C. (2016). Credit scoring with social
time series. Advances in neural information processing systems, 31.  network data. Marketing Science, 35(2), 234–258. https://doi.org/10.1287/mksc.2015.0949
|     |     |     |     |
| --- | --- | --- | --- |
Thakor, A. V. (2020). Fintech and banking: What do we know?. Journal of Financial  WHO, https://covid19.who.int. Accessed May 2023
| Intermediation, 41, 100833.  |     |     |     |
| ---------------------------- | --- | --- | --- |
  WHO, https://www.wto.org/english/res_e/booksp_e/world_trade_report16_e.pdf (2016).
Accessed May 2023.
|     | 118707  |     | 178  |
| --- | ------- | --- | ---- |

Responsible Access to Credit for Sole-Traders and
Micro-organizations under Unstable Market Conditions with Psychometrics
Thomas, L. C., Allen, D. E., & Morkel-Kingsbury, N. (2002). A hidden Markov chain model
for the term structure of bond credit risk spreads. International Review of Financial
Analysis, 11(3), 311-329.
Tupes, E. C., & Christal, R. E. (1992). Recurrent personality factors based on trait
ratings. Journal of Personality, 60(2), 225-251.
Tok, Y. W., & Heng, D. (2022). Fintech: Financial Inclusion or Exclusion?. International
Monetary Fund.
Upwork 2023, https://www.upwork.com/blog/gen-z-workforce
Van Thiel, D., Goedee, J., Leenders, R.T.A.J. (2023). Leveraging Financial Personality for
Inclusive Credit Scoring Amidst Global Volatility. Journal of Risk Management in Financial
Institutions, Vol 17 No 1.
Van Thiel, D., & van Raaij, W. F. (2019). Artificial intelligence credit risk prediction: An
empirical study of analytical artificial intelligence models for credit risk prediction in a
digital era. Journal of Risk Management in Financial Institutions, 12(3), 268–286.
Verbraken, T., Bravo, C., Weber, R., & Baesens, B. (2014). Development and application of
consumer credit scoring models using profit-based classification measures. European Journal
of Operational Research, 238(2), 505-513.
Vives, X. (2019). Digital disruption in banking. Annual Review of Financial Economics, 11,
243-272.
Wang, G., Ma, J., Huang, L., & Xu, K. (2012). Two credit scoring models based on dual
strategy ensemble trees. Knowledge-Based Systems, 26, 61-68.
Watson, J. J. (2003). The relationship of materialism to spending tendencies, saving, and
debt. Journal of Economic Psychology, 24(6), 723-739.
World Economic Forum 2023. https://www.weforum.org/agenda/2022/01/what-is-
sustainable-finance/. Accessed May 2023.
World Trade Organisation. The world trade report 2016. “Levelling the trading field for
SME’s”. https://www.wto.org/english/res_e/booksp_e/world_trade_report16_e.pdf
World Trade Organisation. The world trade report 2023.” Re-globalisation for a secure,
inclusive and sustainable future”.
https://www.wto.org/english/res_e/booksp_e/wtr23_e/wtr23_e.pdf
Wei, Y., Yildirim, P., Van den Bulte, C., & Dellarocas, C. (2016). Credit scoring with social
network data. Marketing Science, 35(2), 234–258. https://doi.org/10.1287/mksc.2015.0949
WHO, https://covid19.who.int. Accessed May 2023
WHO, https://www.wto.org/english/res_e/booksp_e/world_trade_report16_e.pdf (2016).
Accessed May 2023.
117881

Chapter 6
Wiginton, J. C. (1980). A note on the comparison of logit and discriminant models of
consumer credit behavior. Journal of Financial and Quantitative Analysis, 15(3), 757-770.
Worldbank 2023. https://www.enterprisesurveys.org/en/enterprisesurveys. Accessed May
2023
Worldbank 2023.
https://databank.worldbank.org/source/world-development-indicators. Accessed May 2023
World Value Survey 2023. https://www.worldvaluessurvey.org/WVSContents.jsp. Accessed
May 2023
Xiao, H., Xiao, Z., & Wang, Y. (2016). Ensemble classification based on supervised
clustering for credit scoring. Applied Soft Computing, 43, 73-86.
Yang, S., & Berdine, G. (2017). The receiver operating characteristic (ROC) curve. The
Southwest Respiratory and Critical Care Chronicles, 5(19), 34-36.
Yang, S., Markoczy, L., & Qi, M. (2007). Unrealistic optimism in consumer credit card
adoption. Journal of Economic Psychology, 28(2), 170-185.
Yuan, H., Lau, R. Y., Xu, W., Pan, Z., & Wong, M. C. (2018). Mining Individuals' Behavior
Patterns from Social Media for Enhancing Online Credit Scoring. In PACIS (p. 163)
Zhang, E., & Zhang, Y. (2009). F-Measure. In: LIU, L., ÖZSU, M.T. (eds) Encyclopedia of
Database Systems. Springer: Boston, MA. https://doi.org/10.1007/978-0-387-39940-9_483
Zhang, Y., Jia, H., Diao, Y., Hai, M., & Li, H. (2016). Research on credit scoring by fusing
social media information in online peer-to-peer lending. Procedia Computer Science, 91, 1.
118729

Responsible Access to Credit for Sole-Traders and
Micro-organizations under Unstable Market Conditions with Psychometrics
|     |     |     |     |     |
| --- | --- | --- | --- | --- |
Wiginton, J. C. (1980). A note on the comparison of logit and discriminant models of
consumer credit behavior. Journal of Financial and Quantitative Analysis, 15(3), 757-770.
|     |     |     |     |     |
| --- | --- | --- | --- | --- |
Worldbank 2023. https://www.enterprisesurveys.org/en/enterprisesurveys. Accessed May
| 2023              |     |     |     |     |
| ----------------- | --- | --- | --- | --- |
|                   |     |     |     |     |
| Worldbank 2023.   |     |     |     |     |
https://databank.worldbank.org/source/world-development-indicators. Accessed May 2023
|     |     |     |     |     |
| --- | --- | --- | --- | --- |
World Value Survey 2023. https://www.worldvaluessurvey.org/WVSContents.jsp. Accessed
| May 2023  |     |     |     |     |
| --------- | --- | --- | --- | --- |
|           |     |     |     |     |
Xiao, H., Xiao, Z., & Wang, Y. (2016). Ensemble classification based on supervised
clustering for credit scoring. Applied Soft Computing, 43, 73-86.  In our final chapter, we reflect on the cumulative insights and broader implications of AI-

Yang, S., & Berdine, G. (2017). The receiver operating characteristic (ROC) curve. The  driven transformations in banking. By summarizing the findings, we highlight how they
Southwest Respiratory and Critical Care Chronicles, 5(19), 34-36.
  support Banking 5.0 and its inclusive digital financial ecosystem.
Yang, S., Markoczy, L., & Qi, M. (2007). Unrealistic optimism in consumer credit card
adoption. Journal of Economic Psychology, 28(2), 170-185.  Through this exploration, we underscore the role of human centered-AI as a catalyst for

Yuan, H., Lau, R. Y., Xu, W., Pan, Z., & Wong, M. C. (2018). Mining Individuals' Behavior  change, paving the way for a future where financial services are
Patterns from Social Media for Enhancing Online Credit Scoring. In PACIS (p. 163)
|     |     |     | accessible, equitable, and personal.  |     |
| --- | --- | --- | ------------------------------------- | --- |
Zhang, E., & Zhang, Y. (2009). F-Measure. In: LIU, L., ÖZSU, M.T. (eds) Encyclopedia of
Database Systems. Springer: Boston, MA. https://doi.org/10.1007/978-0-387-39940-9_483
|     |     |     |     |     |
| --- | --- | --- | --- | --- |
Zhang, Y., Jia, H., Diao, Y., Hai, M., & Li, H. (2016). Research on credit scoring by fusing
social media information in online peer-to-peer lending. Procedia Computer Science, 91, 1.
|     |     |     |     |     |
| --- | --- | --- | --- | --- |

|     | 179  |     |     | 118803  |
| --- | ---- | --- | --- | ------- |

Chapter 6
184

Chapter 7
Conclusion

Chapter 7
CONCLUSION huge opportunities for financial firms (Dharma, 2022). Modern financial innovations come in
many forms such as sustainable finance (SuFi), social finance (SoFi), decentralized finance
7.1 Introduction (DeFi), embedded finance (EmFi), open finance (OpFi), ocean finance (OcFi), circular
This chapter combines the results of the previous chapters leading to a number of finance (CiFi), blockchain finance (BoFi) and so on. They exist mainly to increase access to
conclusions. Section 7.1 answers the research questions. Section 7.2 takes a scholarly finance for specific activities or projects (Ozilli, 2023). Definitions of these inclusive
perspective to reflect on this dissertation. It addresses this dissertation’s contributions and financial innovations and other relevant technologies are shown in table 1.
implications, its limitations, and ends with suggestions for future research. Section 7.3 takes a
practical perspective to reflect on the outcomes of this dissertation. This section discusses the
practical implications for organizations and practitioners in general, and it ends with a
presentation of scenario’s for financial advice and risk scoring beyond Banking 5.0.
This research stands at the intersection of two significant trends in the financial industry: the
impact of technological development from traditional Banking 1.0 to holistic and inclusive
Banking 5.0 and the transforming power of tech-savvy Millenials and Gen Z in an unstable
macro-economic climate. Banking 5.0 emphasizes the seamless integration of technology and
human touchpoints to enhance customer experiences and draws particular attention to
sustainable banking (Nicoletti, 2021). It includes new technology solutions like generative
AI, blockchain and Internet of Things. This research focusses on the technology intelligence
developments driven by AI.
In the current landscape, banks therefore increasingly digitalize, responding to a need for
operational resilience, consumer demand and governmental encouragement for cashless
transactions, particularly amplified by the pandemic's necessity for contactless interactions
(Windasari, 2022). Factors such as online banking, self-service machines, financial
integration, and 24-hour access have changed the outlook regarding the need for digital
banking (Chauhan, 2022). The new technology wave sweeping through the financial industry
has changed many traditional banking structures (Windasari, 2022). Creating an attractive
and simple digital banking interface is important to support an ease-of-use experience for
customers (Windasari, 2022). However, to ensure positive customer experiences, other
elements must be applied, such as rewards, unique features, and positive word-of-mouth
(Windasari, 2022). In my research on the customer experience of digital advice (Chapter 2), I
highlight and confirm the growing importance of experiential attributes in shaping customer
satisfaction with digital financial advice. Consequently, advisors must actively enhance these
attributes and expand their ecosystem of services to strengthen and diversify their offerings in
this area. Furthermore, as future generations increasingly become data agents, my research
suggests that the rapid development of AI offers promising opportunities to utilize behavioral
and psychometric data to close the advisory gap and expand access to financial services.
7.1.1. Technology innovations and banking business model innovation
As the financial industry embraces digitalization, the emergence of digital-only banks,
exemplifying the forefront of Industry 4.0 and Industry 5.0 technologies, becomes prominent.
This movement, witnessed notably in Asian regions, signifies a paradigm shift in banking
services delivery (Windasari, 2022). With the proliferation of digital banks across various
countries, including Hong Kong, Taiwan, China, Singapore, Japan, Korea, Malaysia, and
Indonesia, the banking sector is witnessing a redefinition of roles and policies to
accommodate the increasing reliance on online applications for financial transactions
(McKinsey, 2021; Alhosani & Tariq, 2020).
Moreover, with the extensive innovations in Fintech, Wealthtech and Insurtech over the past
few years, as well as the emergence of open banking and blockchain technology there are
118862 183

Conclusion
CONCLUSION huge opportunities for financial firms (Dharma, 2022). Modern financial innovations come in
many forms such as sustainable finance (SuFi), social finance (SoFi), decentralized finance
7.1 Introduction (DeFi), embedded finance (EmFi), open finance (OpFi), ocean finance (OcFi), circular
This chapter combines the results of the previous chapters leading to a number of finance (CiFi), blockchain finance (BoFi) and so on. They exist mainly to increase access to
conclusions. Section 7.1 answers the research questions. Section 7.2 takes a scholarly finance for specific activities or projects (Ozilli, 2023). Definitions of these inclusive
perspective to reflect on this dissertation. It addresses this dissertation’s contributions and financial innovations and other relevant technologies are shown in table 1.
implications, its limitations, and ends with suggestions for future research. Section 7.3 takes a
practical perspective to reflect on the outcomes of this dissertation. This section discusses the
practical implications for organizations and practitioners in general, and it ends with a
presentation of scenario’s for financial advice and risk scoring beyond Banking 5.0.
This research stands at the intersection of two significant trends in the financial industry: the
impact of technological development from traditional Banking 1.0 to holistic and inclusive
Banking 5.0 and the transforming power of tech-savvy Millenials and Gen Z in an unstable
macro-economic climate. Banking 5.0 emphasizes the seamless integration of technology and
human touchpoints to enhance customer experiences and draws particular attention to
sustainable banking (Nicoletti, 2021). It includes new technology solutions like generative
AI, blockchain and Internet of Things. This research focusses on the technology intelligence
developments driven by AI.
In the current landscape, banks therefore increasingly digitalize, responding to a need for
operational resilience, consumer demand and governmental encouragement for cashless
transactions, particularly amplified by the pandemic's necessity for contactless interactions
(Windasari, 2022). Factors such as online banking, self-service machines, financial
integration, and 24-hour access have changed the outlook regarding the need for digital
banking (Chauhan, 2022). The new technology wave sweeping through the financial industry
has changed many traditional banking structures (Windasari, 2022). Creating an attractive
and simple digital banking interface is important to support an ease-of-use experience for
customers (Windasari, 2022). However, to ensure positive customer experiences, other
elements must be applied, such as rewards, unique features, and positive word-of-mouth
(Windasari, 2022). In my research on the customer experience of digital advice (Chapter 2), I
highlight and confirm the growing importance of experiential attributes in shaping customer
satisfaction with digital financial advice. Consequently, advisors must actively enhance these
attributes and expand their ecosystem of services to strengthen and diversify their offerings in
this area. Furthermore, as future generations increasingly become data agents, my research
suggests that the rapid development of AI offers promising opportunities to utilize behavioral
and psychometric data to close the advisory gap and expand access to financial services.
7.1.1. Technology innovations and banking business model innovation
As the financial industry embraces digitalization, the emergence of digital-only banks,
exemplifying the forefront of Industry 4.0 and Industry 5.0 technologies, becomes prominent.
This movement, witnessed notably in Asian regions, signifies a paradigm shift in banking
services delivery (Windasari, 2022). With the proliferation of digital banks across various
countries, including Hong Kong, Taiwan, China, Singapore, Japan, Korea, Malaysia, and
Indonesia, the banking sector is witnessing a redefinition of roles and policies to
accommodate the increasing reliance on online applications for financial transactions
(McKinsey, 2021; Alhosani & Tariq, 2020).
Moreover, with the extensive innovations in Fintech, Wealthtech and Insurtech over the past
few years, as well as the emergence of open banking and blockchain technology there are
182 118837

Chapter 7
Table 1
Definitions
Future of Banking Concept Definition References
Obschonka, Martin, and David B. Audretsch.
Artificial Intelligence The ability of a machine to learn from experience, adjust to new "Artificial intelligence and big data in
inputs and perform human-like tasks. entrepreneurship: a new era has begun." Small
Business Economics 55 (2020): 529-539.
A technology that superimposes virtual objects on the real Azuma, R. T. (1997). A survey of augmented
Augmented Reality environment for deeper human - digital interactions reality. Presence: teleoperators & virtual
environments, 6(4), 355-385.
Large, platform-based, companies that expand towards the direct Vives, X. (2019). Digital disruption in
BigTech provision of financial services and products. F.e. Amazon, Google, banking. Annual Review of Financial
Apple Economics, 11, 243-272.
A distributed ledger that is secure, transparent, and immutable.
Blockchain technology can be used to create a decentralized Nakamoto, S. (2008). Bitcoin: A peer-to-peer
Blockchain Technology
database that is tamper-proof and has the potential to electronic cash system.
revolutionize the way we interact with the digital world.
Ozili, P. K. (2023). Assessing global interest in
A financial business model innovation build on blockchain and decentralized finance, embedded finance, open
Blockchain Finance distributed ledger technology finance, ocean finance and sustainable
finance. Asian Journal of Economics and
Banking, 7(2), 197-216.
The design of novel business models for newly formed Massa, L., & Tucci, C. L. (2013). Business model
Business Model Innovation organizations or the reconfiguration of existing business models innovation. The Oxford handbook of innovation
management, 20(18), 420-441.
Financial business model that provides external finance for Brancati, E. (2015). Innovation financing and the
Circular Finance (CiFi) circular business model innovation role of relationship lending for SMEs. Small
Business Economics, 44(2), 449-473.
Financial business model that provisions financial services Zetzsche, D. A., Arner, D. W., & Buckley, R. P.
Decentralizaed Finance (DeFi) decentralized through a mix of infrastructure, markets, (2020). Decentralized finance (defi). Journal of
technology, methods, and applications Financial Regulation, 6, 172-203.
A branch of machine leanring that typically consist of more than Janiesch, C., Zschech, P., & Heinrich, K. (2021).
Deep Learning one hidden layer, organized in deeply nested network Machine learning and deep learning. Electronic
architectures and usually contain more advanced neurons Markets, 31(3), 685-695.
Digital assistants are dynamic systems possessing the ability to Brill, T. M., Munoz, L., & Miller, R. J. (2022). Siri,
learn from customer preferences. They offer the potential to Alexa, and other digital assistants: a study of
Digital Assistants transform companies by creating more efficient business customer satisfaction with artificial intelligence
processes, automating complex tasks and improving customer applications. In The Role of Smart Technologies in
service experience Decision Making (pp. 35-70). Routledge.
Digital transformation is characterized by the fusion of advanced Almeida, F., Santos, J. D., & Monteiro, J. A. (2020).
technologies and the integration of physical and digital systems. The challenges and opportunities in the
Digitalization It requires a restructuring of processes, turning the company digitalization of companies in a post-COVID-19
more agile, investing in more organic structures, reinforcing World. IEEE Engineering Management
standardization and automation, in order to optimize the Review, 48(3), 97-103.
response capacity to customers
Fully virtual banks without individual physical branches where all Windasari, N. A., Kusumawati, N., Larasati, N., &
banking activities operate through mobile applications. Fully Amelia, R. P. (2022). Digital-only banking
Digital-only banks
virtual operations change how individuals experience the service, experience: Insights from gen Y and gen Z. Journal
and subsequently, their consumption and financial habits. of Innovation & Knowledge, 7(2), 100170.
Ozili, P. K. (2023). Assessing global interest in
Financial business model that integrates financial services into decentralized finance, embedded finance, open
Embedded Finance (EmFi) the customer offerings of non-financial institutions finance, ocean finance and sustainable
finance. Asian Journal of Economics and
Banking, 7(2), 197-216.
Fintech is a new financial industry that applies technology to Schueffel, P. (2016). Taming the beast: A scientific
Fintech improve financial activities. definition of fintech. Journal of Innovation
Management, 4(4), 32-54
Generative AI applications typically use foundation models.
These models contain expansive artificial neural networks
inspired by the billions of neurons connected in the human brain. Chui, M., Hazan, E., Roberts, R., Singla, A., &
Generative Artificial Intelligence Foundation models are part of what is called deep learning, a Smaje, K. (2023). The economic potential of
term that alludes to the many deep layers within neural generative AI.
networks. Unlike previous deep learning models, they can process
extremely large and varied sets of unstructured data and perform
more than one task.
118884

Conclusion
Table 1
Future of Banking Concept Definition References
Definitions
Human-Centered AI is a vision that supports designing AI-systems
that support human self-efficacy, promote creativity, clarify
responsibility and facilitate social participation. These human Shneiderman, B. (2020). Human-centered artificial
Future of Banking Concept Definition References Human-Centered AI aspirations also encourage consideration of privacy, security, intelligence: Three fresh ideas. AIS Transactions on
Obschonka, Martin, and David B. Audretsch. environmental protection, social jusitce and human rights. It Human-Computer Interaction, 12(3), 109-124.
reverses the 'computer controlled' vision on AI by putting humans
Artificial Intelligence The ability of a machine to learn from experience, adjust to new "Artificial intelligence and big data in at the center of systems design thinking
inputs and perform human-like tasks. entrepreneurship: a new era has begun." Small Providing a unique customer experience based on personal Jain, G., Paul, J., & Shrivastava, A. (2021). Hyper-
Business Economics 55 (2020): 529-539. Hyper-Personalization information by using a real-time big data approach in digital personalization, co-creation, digital clienteling and
A technology that superimposes virtual objects on the real Azuma, R. T. (1997). A survey of augmented environments to which customers react positively t R r e a s n e s a fo rc rm h, a 1 t 2 io 4 n , . 1 Jo 2 u -2 rn 3 a . l of Business
Augmented Reality environment for deeper human - digital interactions reality. Presence: teleoperators & virtual Inclusive finance is a core concept of finance that makes various Hasan, M., Le, T., & Hoque, A. (2021). How does
environments, 6(4), 355-385. Inclusive Finance financial products and services accessible and affordable to all financial literacy impact on inclusive
Large, platform-based, companies that expand towards the direct Vives, X. (2019). Digital disruption in individuals and businesses, especially those excluded from the finance?. Financial innovation, 7(1), 40.
formal financial system.
BigTech provision of financial services and products. F.e. Amazon, Google, banking. Annual Review of Financial
Apple Economics, 11, 243-272. Zarifis, A., & Cheng, X. (2022). A model of trust in
Insurtech Insurtech is the specialized technology used in insurance Fintech and trust in Insurtech: How Artificial
A distributed ledger that is secure, transparent, and immutable. Intelligence and the context influence it. Journal of
Blockchain technology can be used to create a decentralized Nakamoto, S. (2008). Bitcoin: A peer-to-peer Behavioral and Experimental Finance, 36, 100739.
Blockchain Technology database that is tamper-proof and has the potential to electronic cash system. IoT enables seamless communications and automatic Nguyen, D. C., Ding, M., Pathirana, P. N.,
revolutionize the way we interact with the digital world. Internet-of-Things m int a e n r a ve g n e t m io e n n w t b h e ic t h w h e a e s n t h h e e t e p r o o t g e e n n ti e a o l u t s o d re e v v o ic l e u s ti o w n i i t z h e o u in t d h u u s m tri a e n s S (2 e 0 n 2 e 1 v ) ir . a 6 t G ne I , n A te ., r n L e i, t J o ., f N T i h y i a n t g o s , : D A ., c . o .. m & p P re o h o e r, n H si . v V e .
and provide significant benefits to society through fully intelligent survey. IEEE Internet of Things Journal, 9(1), 359-
Ozili, P. K. (2023). Assessing global interest in and automated remote management systems 383.
Blockchain Finance A di s fi t n ri a b n u c t i e a d l b le u d s g in e e r s t s e c m h o n d o e lo l g in y novation build on blockchain and d fi e n c a e n n c t e r , a o li c z e e a d n f i f n in a a n n c c e e , e a m nd b e su d s d t e a d in f a in b a le n ce, open Machine Learning M p a r n o a a b c l h y le t in i m c e a - l s l e p m a e o r c n d if i e n ic l g b t d r u a e i i l s n d c i i r n n i g g b e d a s a n t t d h a s e t o o c l v a a e p u a a t c o s i m s t o y a c o t ia f e t s t e y h d s e t t e p a m r s o k s c s e . t o s s l e o a f r n from J M M an a a i c r e k h e s i c n t h s e , , l C 3 e . 1 a , r ( Z n 3 s i ) c n , h g 6 e 8 a c 5 n h - d , 6 P d 9 . e 5 , e . & p H le e a in r r n i i c n h g , . K E . l ( e 2 c 0 tr 2 o 1 n ) i . c
finance. Asian Journal of Economics and
Business Model Innovation T o h rg e a d n e iz s a ig ti n o n o s f o n r o v th e e l b r u e s c i o n n e f s ig s u m ra o t d io e n ls o f f o e r x n i e st w in ly g f b o u r s m in e e d s s models B M in a n a n o s k s v i a a n , t g i L o , . n , 7 . & ( T 2 h T ), e u 1 c O c 9 i x 7 , f - C o 2 . r 1 d L 6 . h . ( a 2 n 0 d 1 b 3 o ). o B k u o s f i n in e n s o s v m at o io d n e l Ocean Finance F f m o u i c n n a e a d r a i n s n n c e t i l h a i f e a l e c t s o e w s r y v i s l i l t c e b e m e s a c s h n o a d r n f t n i o n e a a ll n d e c d d i r a t e l o s i w s n s a e t r x r d i u s s m t i i n m e g n p t p r s o r o t v h b in a le g t m a th r s e e i n u h s e m e a d a lt r h t i o n o e r f a o is r e S , s C L u u C o ., s m r m o t A a a n m b i i a n d l u a , a a n , B b l i l U . c l a e a a . h R t n o , i . d o c P , e n . W F , a s i A , n t a z k V l e g s p o c h e a l o , r . l u a n M 1 , l o 2 d . W m , , N H T y . o , . ” o . A , ( a 2 1 N n r 0 , e n a 2 p a a t 1 p u u , ) . , r Z , e 1 K . “ , - . F , 1 B i C 1 e n o . n a x z n , a c A k in . e , g n T , a e D h . ,
management, 20(18), 420-441.
Circular Finance (CiFi) F ci i r n c a u n la c r ia b l u b s u in si e n s e s s m s m od o e d l e i l n t n h o a v t a p ti r o o n vides external finance for B ro r l a e n o ca f t r i e , l E a . t i ( o 2 n 0 s 1 h 5 i ) p . l I e n n n d o i v n a g t i f o o n r f S in M a E n s c . i n S g m a a n ll d the Open Banking O w co p h m e o n p g e b e t a n it n e i k o r i a n n t g b e e f t a t h w c e i e l d i e t a a n t t a e tr , s a w d d i a i t t t h i a o a n s a h r l e a b g ri a u n n l g a k t s c o o a r n y n s d g e o n c a h t l e a o d ll f e b p n y r g o c e u m r s f o t i o t n i m t n e g e c r h s H C th r e e e , d Z d it . a , t m H a u . a a J r o k n e u g t r , n c J a o ., l m & o p f Z e f h i t n i o t a u io n , n c J i . a w ( l 2 h e 0 e c 2 n o 3 n b ) o . o m O rr p i o c e w s n , e b 1 rs a 4 n 7 o k w ( i 2 n n ) g , :
Business Economics, 44(2), 449-473. entrants. 449-474
Financial business model that provisions financial services Zetzsche, D. A., Arner, D. W., & Buckley, R. P. FCA (2019), Call for Input: Open Finance, Financial
Decentralizaed Finance (DeFi) decentralized through a mix of infrastructure, markets, (2020). Decentralized finance (defi). Journal of Open Finance F a i c n c a e n s c s i a to l b a u w si i n d e e s s ra m ng o e d e o l f t f h in a a t n a c ll i o a w l s s e d rv a i t c a e s s h a a n r d in p g r o a d n u d c t t h s ird-party C at o : n h d tt u p c s t : / A / u w t w ho w r . i f t c y a , L .o o r n g d .u o k n / , p a u v b a l i i l c a a b t l i e o ns/calls-
technology, methods, and applications Financial Regulation, 6, 172-203. input/call-input-open-finance.
A branch of machine leanring that typically consist of more than Janiesch, C., Zschech, P., & Heinrich, K. (2021). McCoy, M. S., Allen, A. L., Kopp, K., Mello, M. M.,
Deep Learning o a n rc e h h it i e d c d t e u n re l s a y a e n r d , o u r s g u a a n ll i y z e c d o n in ta d in e e m pl o y r e n e a s d t v e a d n n c e e t d w n o e r u k r ons M M a a c rk h e in ts e , l 3 e 1 ar ( n 3 i ) n , g 6 8 a 5 n - d 6 d 9 e 5 e . p learning. Electronic Personal Data A lin n k y e i d n f w or i m th a a t n io i n n d th iv a i t d u id a e l n o t r i f h ie o s u , s r e e h la o t ld es to, or could reasonably be P E p a t e h t r i i s l c o , a n D l a . r l e J . d s , p a O o ta s n . s s o T ib r h i i o e li , t A i P e m . s , e . f . r o . i c r & a c n E o m m Jo a p u n a rn u n a e ie l l , s o E t f . h J a . t ( p 2 r 0 o 2 c 3 e ) s . s
Digital assistants are dynamic systems possessing the ability to Brill, T. M., Munoz, L., & Miller, R. J. (2022). Siri, Bioethics, 23(11), 11-23.
learn from customer preferences. They offer the potential to Alexa, and other digital assistants: a study of Psychometrics The scientific study of the quality of psychological measures that Furr, R. M. (2021). Psychometrics: an introduction.
Digital Assistants transform companies by creating more efficient business customer satisfaction with artificial intelligence is a branch of behavioral science SAGE publications.
A Psychometric Credit Score is a predictive model based on an
processes, automating complex tasks and improving customer applications. In The Role of Smart Technologies in applicant psychological and behavioral profile to assess Meier, S., & Sprenger, C. D. (2012). Time
service experience Decision Making (pp. 35-70). Routledge. Psychometric Credit Scoring c a r p e p d r i o t a w c o h r t c h o y m ne p s a s r , e o d f t f o e r t i r n a g d a it i m on o a r l e m in e c t l h u o si d v s e . a It n i d s p a e s r u s b o s n t a it li u z t e e d o f d cr is e c d o it u w n o ti r n t g h i p n r e e s d s i . c P ts s ychological science, 23(1), 56-
Digital transformation is characterized by the fusion of advanced Almeida, F., Santos, J. D., & Monteiro, J. A. (2020). the FICO and Experian score used for applicants, which, in turn is 58.
technologies and the integration of physical and digital systems. The challenges and opportunities in the mainly based on bureau data and financial historical records.
Digitalization It requires a restructuring of processes, turning the company digitalization of companies in a post-COVID-19
m s re ta o sp n re o d a n a r s g d e i i l z e c a a , t p i i n o a v n c e i t a s y t n i t d n o g a c u i u n t s o m t m o o m a r t e e i o r o s n r , g i a n n o ic r d s e tr r u t c o t u o r p e t s i , m re iz i e n f t o h r e c ing W Re o v r i l e d w . I , E 4 E 8 E ( E 3 n ), g 9 in 7 e - e 1 r 0 in 3 g . Management Social Finance (SoFi) T p a tr h r d a o e e n p q s e o u a m s a c it t t e e i i r o o l g y n n e i o a n n f n c c e d m o , r o a p t f h r o k s e r e o a r t e c t e i f f a o a t l r i h l e f u e i , n r t p e a h o , n e s w c i p e t h i r v e i i s c e r e e r o o m m r o n t e a e e c r d g k h e a a o t t n n i m i v s t e h m e e e c x h a s t a l t e o a n r n n i n s e d a m a c li r a s t d i n e d n s o o o n t f o a t A f A i n n n d a a r l n y i c k s e o is . p I , o n 7 u t 0 e lo r , s n 1 , a 0 A t 1 i . o 5 ( n 2 1 a 0 9 l 2 . R 0 e ). v i D e e w li n o e f a F t i i n n a g n s c o ia c l i al
efficiently allocate resources in a way that maximizes welfare.
Fully virtual banks without individual physical branches where all Windasari, N. A., Kusumawati, N., Larasati, N., & Venture philanthropy, microfinance, crowdfunding and social
banking activities operate through mobile applications. Fully Amelia, R. P. (2022). Digital-only banking impact bonds are examples of soclai finance
Digital-only banks
virtual operations change how individuals experience the service, experience: Insights from gen Y and gen Z. Journal Super apps are do-everything apps that bring together an
and subsequently, their consumption and financial habits. of Innovation & Knowledge, 7(2), 100170. expansive suite of services within a single interface. In some
cases, this involves the incorporation of multiple functions within
Embedded Finance (EmFi) F th in e a c n u c s i t a o l m bu e s r i n o e ff s e s r i m ng o s d e o l f t n h o a n t - i f n in te a g n r c a ia te l s in f s in ti a tu n t c i i o a n l s services into O d f f i i e n n z c a i a l e n i n , n c c P t e e r . , . a K o A li . c s z ( e i e 2 a a d 0 n n 2 f J i f 3 n o i ) n a u . a n r A n n c s a c e s e l , e o e a s f m s n i E d n b c g e s o u d n g s d o l t o e m a b d i i a n c f l a s i n i b n a a l t n e n e d c r e e , s o t p in e n Super apps A a o a a f l s s c m a i i o n n n o m g g s a l l b t e e p i i n p n a b a v p r f a t a p a i n o r m . i d n a In i b l b o y l o a f y , t n , f e h u n A a e n e s c r c r i h . c a t i a S ’ o o s s o f n e s m w a s u l , e p h i t e i n i h c n r t h e e s a g t h s p a r u a p a n p s s t c e i i e a o t r s s r n a e o o p a f w l p n a t d n r h d g e e u f e u n m s n s o u c b c t p a e t r e i e l s o e r l n l t a a a h a p n e l b i p d t r e i a r e d x n e i s o s d l m y t u i e n n u i n g n d p c . a e o e n r n t S ( a 1 2 t n 4 e 0 d 0 i 2 5 n m 2 - b 1 ) e e . 4 g r M 1 g a 9 , e c . M o d r i . a p , s M p . o M u w k e h e d e r i r a i j n e , e C d , u i g R lt it . u , a r & l e A & P s u i S a n o : a c S t i h u e a p ty m e , r b 4 a e 4 p k p ( a 8 s r ) , , A .
ventures that are highly dependent on massive, sprawling
Banking, 7(2), 197-216. corporations whose heft allows them to build the crucial internal
Fintech is a new financial industry that applies technology to Schueffel, P. (2016). Taming the beast: A scientific integration and external tie-ups that make their apps so super
Fintech improve financial activities. definition of fintech. Journal of Innovation European Commission. (2021). Overview of
Management, 4(4), 32-54 A dynamic process that takes environmental, social, and sustainable finance. European Commission.
Sustainable Financa (SuFi) governance (ESG) aspects into account when making financial Available at https://ec.europa.eu/info/business-
Generative AI applications typically use foundation models. and investment choices. economy-euro/banking-and-finance/sustainable-
These models contain expansive artificial neural networks finance/overview-sustainable-finance_en
inspired by the billions of neurons connected in the human brain. Chui, M., Hazan, E., Roberts, R., Singla, A., & Xiong, J., Hsiang, E. L., He, Z., Zhan, T., & Wu, S. T.
Generative Artificial Intelligence F te o r u m nd t a h t a io t n a l m lu o d d e e s l t s o a t r h e e p m ar a t n o y f d w e h e a p t l i a s y c e a rs ll e w d i t d h e in e p n e le u a r r a n l ing, a S g m en a e j r e a , t K iv . e ( 2 A 0 I. 23). The economic potential of Virtual Reality A ex t p e e c r h ie n n o c lo e g s y f o th r a d t e i e m pe p r o s h e u s m t a o n ta -d l i i g m it m al e i r n s t i e ve ra 3 c t d io im ns ensional ( d p 2 i e s 0 r p s 2 l p 1 a e ) y . c s t A : i v e u e m g s m e . L r e g i n g i t n h e g t d : t S r e c e c i a e h l n n it c o y e l o a & g n i d e A s v p i p a rt l n i u c d a a f l t u i r o t e u n a r s l e i , t y 1 0(1),
networks. Unlike previous deep learning models, they can process 1-30.
e m x o tr r e e m th e a ly n l o a n rg e e t a a s n k d . varied sets of unstructured data and perform Wealthtech W i
t
n
e
v
c
e e
h
a s
n
l t t
o
m h
l
-
o
e t
g
e n
i
c t
e
h
s
a i n
a
s d
s
a c
w
b li
e
r e a
l
n
l
n t
a
c p
s
h r
t
o o
a
t f
i
f
l
F o
o
i l
r
n i o
m
t e m
a
c
d
h a
e
n w a
p
h g
r
i
o
e c
d
m h
u
i e
c
s n
t s
f t o
a
u c
n
s u i
d
s n s g
s
e
e
d d
r
i
v
o g
ic
n it
e
a
s
l D m z a ia n w ag g e o m , T e . n ( t 2 s 0 e 2 c 1 t ) o . r W . ealth Tech impact on wealth
184 118859

Chapter 7
Over the last years, the rising capabilities of artificial intelligence (AI) have improved human
decision-making in many application areas (Hemmer et al., 2022). But the future is even
more exciting. Artificial intelligence (AI), the ability of a machine to learn from experience,
adjust to new inputs and perform human-like tasks (Obschonka et al., 2020) is increasingly
impacting the transformation of banking. It is the intellect exhibited by machines, in contrast
to the natural knowledge demonstrated by humans. From Siri to self-driving cars, AI is
progressing at a rapid pace. AI has many forms. Machine learning describes the capacity of
systems to learn from problem-specific training data to automate the process of analytical
model building and solve associated tasks. Deep learning is a machine learning concept based
on artificial neural networks. For many applications, deep learning models outperform
shallow machine learning models and traditional data analysis approaches (Janiesch et al.,
2022). As discussed in Chapter 5, this research substantiates these findings for three different
lenders across two distinct asset classes.
Looking ahead, AI innovations will continue to evolve and integrate into financial services
within increasingly interactive environments. These advancements will conveniently narrow
the information asymmetry gap that often arises during financial decision-making. Examples
of such technologies include smart mobile wallets, proactive robo-advisors, digital guardian
angels and other intelligent agents. However, my research indicates that these digital advice
solutions enhance access to finance and improve customer satisfaction only when they are
effectively targeted based on personality attributes. Financial service providers will be a
complex, connected web of providers (Dharma, 2022). They will deliver financial services on
increasingly interactive, experiental platforms like for example the Metaverse. The Metaverse
is the post-reality universe, a perpetual and persistent multiuser environment merging
physical reality with digital virtuality (Mystakidis, 2022). It is based on the convergence of
technologies that enable multisensory interactions with virtual environments, digital objects
and people such as virtual reality (VR) and augmented reality (AR). In the Metaverse digital
advisors and mobile apps, sometimes evolving into super apps, serve as digital guardian
angels in the realm of inclusive responsible Banking 5.0. These platforms leverage advanced
technologies such as augmented reality, generative AI and deep learning to provide hyper-
personalized financial advice and assistance to users. By integrating virtual assistants with
generative AI and machine learning driven algorithms, these tools offer unparalleled
convenience, inclusiveness and accessibility, empowering individuals to manage their
finances effectively from anywhere, at any time. This dissertation focuses on the lending
markets in the United States, the United Kingdom, the Netherlands, and the Czech Republic,
examining human-centered AI innovations that promote inclusive lending. These innovations
are grounded in psychometric and attitudinal insights within the inclusive digital Banking 5.0
paradigm.
7.1.2. Next gen behavior and banking business model innovation
Ultimately, this research aims to foster long-term financial well-being and societal prosperity
through its focus at the intersection of AI innovation and behavioral finance for Banking 5.0.
It particularly focuses on the digital financial inclusion and financial wellness of millennials
and Generation Z in this new context. Many studies proved using TAM (Technology
Acceptance Model) that millennials and Gen Z are the highest in technology acceptance (Abu
Daqar et al., 2021). On average they are technologically literate.
In their usage of digital applications they produce personal data. Digital personal data is often
described as the resource of the future, even as a “new asset class” according to the World
119806

Conclusion
Economic Forum, which argued that a massively increased amount of personal data “is
generating a new wave of opportunity for economic and societal value creation” (WEF,
2011). Personal data can be defined as “any information relating to an identified or
identifiable natural person” (Edwards, 2018). The importance of personal data is evident in
the rise of so-called “Big Tech” as the dominant firms in our societies today. The collection,
use, and exploitation of personal data has a long history, including the credit scoring activities
of data brokers like Experian and Axciom (Pasquale, 2015). However, digital personal data is
different, as others have noted, and not just in terms of “volume, velocity, variety and value”
(Prainsack, 2019). Personal data is now collected through digital processes that enable mass
collection, use, and exploitation of data with the imposition of new technical objectives and
structures of collection (e.g., patterns of online “attention”), as well as new logics of use (e.g.,
inferential predictions) (Viljoen, 2020; OECD, 2019). As such, mass digital personal data—
“Big Data”—entails different dynamics than earlier credit scoring, most obviously in terms of
the inherently collective nature of its algorithmic applications and the network effects that
arise; for example, using personal data from thousands or millions of people to predict
individual or group behaviors (Viljoen, 2020). Personal data are differentiated into
“identifiable”, “anonymous”, and “pseudonymous” with the difference largely relating to
how it is collected: identifiable being voluntary and knowingly given; anonymous being
collected by data processors, often involuntarily and unknowingly, using supposedly
anonymous identifiers; and pseudonymous being obtained from third parties. However, it is
increasingly evident that it is possible to track back from anonymous and pseudonymous data
to a person’s identifiable personal data (Edwards, 2018). Consequently, we treat the three
categories as largely similar.
An essential indicator of people’s ability to make financial decisions is their level of financial
literacy (Tiwari, 2022). However, despite the technological adeptness of younger generations,
which leads to the production of substantial personal data, financial literacy remains low
among millennials and Generation Z. (Tiwari, 2022). Financial literacy has become important
in making decisions about all aspects of our daily lives. The ability to grasp financial
products in a variety of formats, as well as financial attitude, both represent our financial
education (Lusardi, 2019). The business model innovation of digital banking therefore is also
seen as a way to drive financial education and financial literacy for these younger customer
segments (Windasari, 2022). This dissertation argues that financial education alone is
insufficient; instead, building financial capability is necessary. Consequently, financial skills
instead of financial knowledge have been included as a driver in the psychometric credit
scoring model.
Moreover, these generations place a strong emphasis on experience and sustainable practices
such as the circular economy and financial inclusion. Financial inclusion is the process of
ensuring that individuals especially poor people have access to basic financial services in the
formal financial sector (Ozilli, 2018). Financial inclusion is such a sustainability business
model innovation that these generations apppreciate. However, also other customer segments
like students, sole traders, small businesses, women in the workforce, and populations
displaced by conflict or natural disasters benefit from financial inclusion (Van Thiel et al.,
2023).
Unlike their parents and older brothers, belonging to Generation X and/or Millennials,
members of Generation Z have totally different behaviour, being even more green and
sustainability-oriented, taking into consideration mainly those companies and especially
118971

Chapter 7
brands who are able to connect with them and enhance their experiences and feelings (Dabija
et al., 2019).
The advancement of digital financial inclusion also aids managers in implementing the
concept of sustainable development, steering clear of shortsightedness, and bolstering
enterprises' ability to manage risks. According to the Upper Echelon Theory, the evolution of
digital financial inclusion enables managers to recognize and endorse the Environmental,
Social, and Governance (ESG) concept (Dhir, 2022). According to Dhir, the fulfillment of
firms' ESG social responsibility namely is contingent upon meeting stakeholders' demands,
fostering a favorable external environment for corporate advancement, mitigating potential
risks, and consequently encouraging corporate ESG engagement through information
disclosure. Moreover, the progression of digital inclusive finance has enhanced the corporate
financing landscape, curtailed external financing costs, facilitated access to external funding,
bolstered enterprises' market competitiveness, and augmented corporate value. Consequently,
it has provided firms with increased liquidity and cash flow, elevating shareholder wealth
levels, and furnishing additional support for enterprises to partake in ESG initiatives, thereby
prompting increased involvement in ESG behaviors, notably ESG information disclosure.
In addition to sustainability, my research shows that the next generations increasingly favor
experiential services. Prior research on digital banking services shows that customer
experiences are determined by service quality, functional quality, perceived value, employee-
customer engagement, perceived usability and perceived risk (Mbama, 2018). Other studies
on online customer experiences have identified easiness to locate the Web site/app, ease of
use, perceived usefulness, hedonic and utilitarian features, perceived enjoyment,
personalization, social interactions and multi-device compatibility as the antecedents of the
unified online customer experience as a proxy of the quality of online banking services
(Bilgihan, 2016). Meanwhile, next generations respond differently to e-commerce as they
process website information five times faster than older generations and are the most
emotional and least loyal customers compared to all other generations (Billgihan, 2016).
This generation shift has propelled a transition towards embedded finance (EmFi) and
Banking 5.0. EmFi is the integration of financial services into the customer offerings of non-
financial institutions (Mc Kinsey, 2022). EmFi allows the delivery of financial services
directly into the websites, mobile applications and business processes of non-financial
organization (Oracle, 2021). EmFi allows non-financial companies to incorporate financial
services into their payments journey. Customer can benefit from contextual, seamless
experiences; platforms can unlock new use cases and often unlock proprietary customer data
to improve financial access, while reducing the costs for their customers (Harris, 2022).
Nonetheless, to the best of my knowledge, there has been minimal research exploring the
transition to inclusive, responsible Banking 5.0 from a perspective that combines AI
innovation and behavioral finance lenses. This dissertation seeks to bridge this gap by
introducing a pioneering behavioral psychometric finance framework at the intersection of
personal data driven AI applications in digital financial advice and credit decision making.
This facilitates a deeper understanding of the underlying behavioral traits influencing
responsible and irresponsible financial behaviors, essential for inclusive responsible finance.
Such insights are crucial for transitioning towards digital banking business model innovations
as embedded finance in the context of Banking 4.0 and Banking 5.0.
119828

Conclusion
brands who are able to connect with them and enhance their experiences and feelings (Dabija The central research question of this dissertation, therefore, focuses on how the integration of
et al., 2019). behavioral and psychometric finance principles with AI technologies can support the
transition to inclusive and responsible Banking 5.0. In this context it explores the
The advancement of digital financial inclusion also aids managers in implementing the implications of this transition for closing the advisory gap and expanding access to financial
concept of sustainable development, steering clear of shortsightedness, and bolstering services.
enterprises' ability to manage risks. According to the Upper Echelon Theory, the evolution of
digital financial inclusion enables managers to recognize and endorse the Environmental, 7.1.3. Regulatory compliance
Social, and Governance (ESG) concept (Dhir, 2022). According to Dhir, the fulfillment of A proliferation of future-fit business models designed to achieve economic prosperity while
firms' ESG social responsibility namely is contingent upon meeting stakeholders' demands, also advancing collective causes will be a main feature of succesful businesses in the next 15
fostering a favorable external environment for corporate advancement, mitigating potential to 20 years (Dharma, 2022). As a result of the increase in data, there also have been several
risks, and consequently encouraging corporate ESG engagement through information attempts to steal the data to sell or request redemptions from organisations (Serrado, 2020).
disclosure. Moreover, the progression of digital inclusive finance has enhanced the corporate This situation has shown that organisations with regards to data protection and security do not
financing landscape, curtailed external financing costs, facilitated access to external funding, all have the same degree of maturity (Serrado, 2020). Therefore, central governments and
bolstered enterprises' market competitiveness, and augmented corporate value. Consequently, banks impose impose regulatory frameworks to protect conusmers and their data.
it has provided firms with increased liquidity and cash flow, elevating shareholder wealth Increasingly driven by both the governmental regulations like the General Data Protection
levels, and furnishing additional support for enterprises to partake in ESG initiatives, thereby Regulation (GDPR), Corporate Sustainability Reporting Directive (CSRD), AI-Act, and the
prompting increased involvement in ESG behaviors, notably ESG information disclosure. Digital Operational Resilience Act (DORA) in the European Union (EU), the Data Protection
Act (DPA) in the United Kingdom (UK) and the California Consumer Privacy Act (CCPA)
In addition to sustainability, my research shows that the next generations increasingly favor and AI-Act in the United States (US) and the UN sustainable development goals, impact on
experiential services. Prior research on digital banking services shows that customer customers and society will become increasingly central business objectives across the world.
experiences are determined by service quality, functional quality, perceived value, employee- The website of the European Commission shows that the approach to AI risk management is
customer engagement, perceived usability and perceived risk (Mbama, 2018). Other studies characterized by a more comprehensive range of legislation tailored to specific digital
on online customer experiences have identified easiness to locate the Web site/app, ease of environments. With the AI-Act, the EU plans to place new requirements on high-risk AI in
use, perceived usefulness, hedonic and utilitarian features, perceived enjoyment, socioeconomic processes, the government use of AI, and regulated consumer products with
personalization, social interactions and multi-device compatibility as the antecedents of the AI systems (EU AI-Act, 2024). Other EU legislation enables more public transparency and
unified online customer experience as a proxy of the quality of online banking services influence over the design of AI systems in social media and e-commerce. The UK follows the
(Bilgihan, 2016). Meanwhile, next generations respond differently to e-commerce as they European legislation. The US approach to AI risk management is highly distributed across
process website information five times faster than older generations and are the most federal agencies, many adapting to AI without new legal authorities. Meanwhile, the US has
emotional and least loyal customers compared to all other generations (Billgihan, 2016). invested in non-regulatory infrastructure, such as a new AI risk management framework,
evaluations of facial recognition software, and extensive funding of AI research. According to
This generation shift has propelled a transition towards embedded finance (EmFi) and US thinktank Brookings, the EU and US strategies share a conceptual alignment on a risk-
Banking 5.0. EmFi is the integration of financial services into the customer offerings of non- based approach, agree on key principles of trustworthy AI, and endorse an important role for
financial institutions (Mc Kinsey, 2022). EmFi allows the delivery of financial services international standards (Brookings, 2024). However, the specifics of these AI risk
directly into the websites, mobile applications and business processes of non-financial management regimes have more differences than similarities. Regarding many specific AI
organization (Oracle, 2021). EmFi allows non-financial companies to incorporate financial applications, especially those related to socioeconomic processes and online platforms, the
services into their payments journey. Customer can benefit from contextual, seamless EU and US are on a path to significant misalignment. Because collaboration between the EU
experiences; platforms can unlock new use cases and often unlock proprietary customer data and US is imperative due to the foundational role of their policies in shaping democratic
to improve financial access, while reducing the costs for their customers (Harris, 2022). governance of AI, their respective regulatory frameworks are steering the evolution towards
inclusive and responsible applications within the banking sector, often referred to as Banking
Nonetheless, to the best of my knowledge, there has been minimal research exploring the 5.0. For instance, this research demonstrates the increasing reputational impact of social
transition to inclusive, responsible Banking 5.0 from a perspective that combines AI proof, such as ratings and reviews, on the trust and customer experience of financial advice
innovation and behavioral finance lenses. This dissertation seeks to bridge this gap by (Chapter 2). In a world transitioning to frictionless embedded finance and with the growing
introducing a pioneering behavioral psychometric finance framework at the intersection of influence of social media platforms, these realms are beginning to converge. This dissertation
personal data driven AI applications in digital financial advice and credit decision making. underscores the growing importance of social proof for financial advisors to gain market
This facilitates a deeper understanding of the underlying behavioral traits influencing trust, highlighting the need for consistent regulation of trust across international financial
responsible and irresponsible financial behaviors, essential for inclusive responsible finance. markets.
Such insights are crucial for transitioning towards digital banking business model innovations
as embedded finance in the context of Banking 4.0 and Banking 5.0.
188 118993

Chapter 7
7.2 Research questions
In this context, the research holds significant relevance as it pioneers the development of
foundational principles driving a transformative shift towards holistic and inclusive
responsible Banking 5.0. By delving deep into the intricate relationship between personality
traits and AI-driven advancements, particularly in critical domains such as customer
experience, digital advisory services, and inclusive credit assessment, this thesis aims to
establish a foundational behavioral finance personality layer. This layer not only
comprehensively grasps but also effectively reinforces the underlying determinants of both
responsible and irresponsible financial behaviors within the dynamic framework of Banking
5.0. The establishment of this foundational personality layer heralds the era of 'mindful
finance management,' driving the delivery of hyper-personalized services, enhancing digital
customer experiences, facilitating inclusive credit assessments, ensuring robust risk
management, and cultivating a competitive edge.
The dissertation aims to offer novel insights for advisors and (neo)banks transitioning to an
inclusive Banking 5.0 business model, viewed through the lens of human-centered AI.
Human-centered AI is a way of thinking that advances the technology-centered scope of AI
by designing and making successful technologies that amplify, augment, empower and
enhance human performance (Shneiderman, 2022). The human-centered AI perspective is
chosen to generate human-centric behavioral insights that will propel inclusive AI-driven
digital banking business models and practices, incorporating digital advice, support tools, and
enhanced access to financial advice, finance and financial wellbeing. This dissertation
therefore offers a human-centric perspective applicable to the design and development of new
business models and digital strategies, advice applications, tools and ecosystems for the
Banking 5.0 era.
In summary, the study aims to provide fundamental insights to position inclusive digital
(neo)banks and advisors, which prioritize inclusive finance and their customers' financial
well-being, as central to success strategies in a competitive landscape shaped by Industry 5.0
innovations. From this perspective, the research not only addresses current industry trends but
also anticipates future trajectories, underscoring its importance in navigating the dynamic
landscape of inclusive holistic Banking 5.0.
The substantial growth in behavioral personal data and artificial intelligence modeling has
paved the way for a new era of transformation towards Banking 5.0. This aims to expedite
financial inclusion and enhance financial well-being for individuals, sole traders, and small
businesses. The current uptake of digital banking has already revolutionized the banking
sector by promoting financial inclusion through cost reduction, diverging from traditional
banking practices, and facilitating increased accessibility beyond the limitations of physical
branch locations (Loh, 2020). I contend that the trajectory leads towards a more visionary
realm, marked by the emergence of new human-centered inclusive business models such as
super apps, virtual assistants, and personal financial advice avatars in the metaverse.
119940

Conclusion
7.2 Research questions As Banking 5.0 revolves entirely around understanding the personality and behavior of
In this context, the research holds significant relevance as it pioneers the development of customers, this dissertation's core research questions are:
foundational principles driving a transformative shift towards holistic and inclusive
responsible Banking 5.0. By delving deep into the intricate relationship between personality 1. How does the integration of experiential and psychometric determinants in digital
traits and AI-driven advancements, particularly in critical domains such as customer financial advice systems increases the likelihood of advice usage and significantly
experience, digital advisory services, and inclusive credit assessment, this thesis aims to improves customer satisfaction?
establish a foundational behavioral finance personality layer. This layer not only
comprehensively grasps but also effectively reinforces the underlying determinants of both 2. How does the application of psychometric determinants in digital credit scorecards
responsible and irresponsible financial behaviors within the dynamic framework of Banking improve access to finance?
5.0. The establishment of this foundational personality layer heralds the era of 'mindful
finance management,' driving the delivery of hyper-personalized services, enhancing digital 3. How does the application of artificial intelligence in credit scoring systems improves
customer experiences, facilitating inclusive credit assessments, ensuring robust risk risk model accuracy and predictive power?
management, and cultivating a competitive edge.
The primary objective aligns with the transition towards Banking 5.0 principles, laying the
The dissertation aims to offer novel insights for advisors and (neo)banks transitioning to an groundwork for comprehending the underlying causes of financial behavior. It places
inclusive Banking 5.0 business model, viewed through the lens of human-centered AI. customers at the heart of an inclusive financial ecosystem (Mehdiabadi et al., 2022; Nicoletti,
Human-centered AI is a way of thinking that advances the technology-centered scope of AI 2021). This chapter combines the results of the previous chapters leading to a number of
by designing and making successful technologies that amplify, augment, empower and conclusions. Section 7.1 answers the research questions. Section 7.2 takes a scholarly
enhance human performance (Shneiderman, 2022). The human-centered AI perspective is perspective to reflect on this dissertation. It addresses this dissertation’s contributions and
chosen to generate human-centric behavioral insights that will propel inclusive AI-driven implications, its limitations, and ends with suggestions for future research. Section 7.3 takes a
digital banking business models and practices, incorporating digital advice, support tools, and practical perspective to reflect on the outcomes of this dissertation. This section discusses the
enhanced access to financial advice, finance and financial wellbeing. This dissertation practical implications for banking and regulatory entities.
therefore offers a human-centric perspective applicable to the design and development of new
business models and digital strategies, advice applications, tools and ecosystems for the 7.3 Answers to the research questions
Banking 5.0 era. This dissertation focuses on harnessing the real-world financial behaviors, attitudes, beliefs,
and lifestyles of the next generation of consumers and small business entrepreneurs as a
In summary, the study aims to provide fundamental insights to position inclusive digital comprehensive framework for ‘mindful banking’, known as Banking 5.0. Through the
(neo)banks and advisors, which prioritize inclusive finance and their customers' financial integration of human-centered psychometric data and AI, various approaches are explored to
well-being, as central to success strategies in a competitive landscape shaped by Industry 5.0 investigate their influence on ‘mindful banking’. The overarching objective is to establish a
innovations. From this perspective, the research not only addresses current industry trends but foundational layer for developing and customizing better accessible digital financial services
also anticipates future trajectories, underscoring its importance in navigating the dynamic that prioritize customer-centricity and inclusivity, in line with the principles of Banking 5.0.
landscape of inclusive holistic Banking 5.0. This concluding chapter addresses the three pivotal research questions outlined in the initial
chapter, which have been central to this dissertation. These research questions hold
The substantial growth in behavioral personal data and artificial intelligence modeling has significance for both practical applications and academic inquiry, as elaborated further in the
paved the way for a new era of transformation towards Banking 5.0. This aims to expedite subsequent sections of this chapter. The research inquiries delve into the advancements in
financial inclusion and enhance financial well-being for individuals, sole traders, and small inclusive Banking 5.0 business models within the realm of digital advisory, with a specific
businesses. The current uptake of digital banking has already revolutionized the banking focus on enhanced accessibility, personalization, and inclusive credit decision-making.
sector by promoting financial inclusion through cost reduction, diverging from traditional Firstly, the research examines the positive impacts of psychometric modelling on digital
banking practices, and facilitating increased accessibility beyond the limitations of physical financial advisory services. Secondly, it investigates the favorable effects of psychometric
branch locations (Loh, 2020). I contend that the trajectory leads towards a more visionary modelling on credit risk management. Lastly, it explores the role of AI in driving
realm, marked by the emergence of new human-centered inclusive business models such as advancements within the domain of inclusive Banking 5.0.
super apps, virtual assistants, and personal financial advice avatars in the metaverse.
7.3.1. Human- centric psychometric segmentation for Banking 5.0 credit advice
This dissertation was primarily aimed at shedding new inclusive light on aspects of financial
advice & management in its transformation to a digital Banking 5.0 environment. Next
generations of banking customers are looking for innovative personalized digital financial
services to help them rebuild their finances and reach their financial goals (Mondres 2019).
Financial decision-making, and thus, traditional financial advice, is therefore being
transformed by digitalization (Malhotra & Rashmi, 2006). Combining recent insights from
190 119915

Chapter 7
digital & financial advice, customer experience, service quality and psychometric
segmentation research, led to the formulation of the following research question:
Research question 1:
How does the integration of experiential and psychometric determinants in digital financial
advice systems increases the likelihood of advice usage and significantly improves customer
satisfaction?
Investors that receive financial advice from a dedicated advisor are approximately four times
better off financially than those who do not (Montmarquette & Viennot-Briot, 2016). Also,
households who kept their advisor saw the value of their assets increase by 16.4%, while
households who dropped their advisor increased the value by only 1.7% (Montmarquette &
Viennot-Briot, 2016). Yet traditional business models are under threat (Dhama, 2021). In
recent years, there has been an increasing chorus of new entrants, journalists and regulators
calling into question the practices of financial advisors (Biesenbach & Gudmundsson, 2019).
Robo-advice, the systemized placement of an investor or credit applicant into a pre-made
portfolio that is suitably alligned with the investor or applicants financial goals and time
horizon, has become a viable alternative (Dharma, 2021).
This first research question therefore focusses on the customer expectations of digital advice.
It posited the beneficial impact of personality & behavioral segmentation on digital credit
advice within a Banking 5.0 context. A cross-country survey, encompassing 2,332
respondents from the United Kingdom and The Netherlands, provided the empirical
foundation for this study. The survey probed various attributes, such as reliability, accuracy,
helpfulness, co-creation, width of the advice asn price image related to digital financial
advice, spanning process, outcome, and system-related factors. In line with Biesenbach, the
research demonstrates that younger generations, particularly Gen Z and millennials, are avid
adopters of digital lifestyles and smart digital services, which has driven the digitization of
financial services and the utilization of digital tools for financial decision-making. Within this
context, digital financial advice is posited as a credence good, characterized by sellers as
experts who discern customers' needs (Wolinsky, 1995; Nelson, 1970). Notably, this
information asymmetry can be ameliorated by smart, co-created digital financial advice
solutions (Mhlanga, 2020). Structural equation modeling (SEM) techniques have been
employed, encompassing exploratory and confirmatory factor analyses, yielding essential
insights into the factors governing customer experience with digital financial advice.
Firstly, chapter 2 explores the attributes underlying the desired customer experience of digital
advice. Culminated in the development of the Digital Customer Experience (DCX) model, a
pioneering cross-cultural framework for advancing the customer experience of financial
advice systems is developed. The DCX model provides insight in the factors and their
relevance for designing future proof digital customer experiences. The model highlights the
increasing significance of experiential attributes such as honesty, reliability, and transparency,
compared to outcome-related attributes like price and product diversity. This suggests an
impending shift in customer expectations over the next five to ten years. Key findings
highlight the importance of advisory breadth, indicating that a wider range of brands and
associated products are considered significant. Additionally, the ability for co-creation in the
digital advisory process, particularly in the UK, emerged as critical, alongside pricing
considerations, signaling a growing demand for personalization in the robo-advisory market.
These attributes can serve as a digital advice meta-model for omni-channel personalization.
The research outcomes suggest that applying a foundational personality layer to digital
119962

Conclusion
advisors can advance their digital business models, customer strategies, engagement, and
satisfaction for closing the advisory gap. Furthermore, the increasing volume and variety of
data, along with advancements in artificial intelligence techniques like machine learning,
create new opportunities for providing digital advice and support tools for financial inclusion
and wellness. Additionally, personalizing content and services based on psychometrics and
behaviors offers the potential for micro-personalization.
Secondly, chapter 3 investigates whether the use of psychometric data can improve the usage
of digital advce solutions. My study creates a psychometric customer segmentation and a
digital advice solution targetting model tailored to the preferences and personalities of the
next generation. It presents robo-advisors and generative AI models as transformative
elements in financial advice (Caspi et al., 2023). A survey was conducted with 2,332
respondents, using 12 psychometric questions from the Dutch Authority of Financial Markets
monitor. Principal component analysis and Ward clustering were utilized to identify three
components for digital advice segmentation, defining a segmentation based on customer
lifestyles: level of convenience seeking, financial literacy (knowledge and skills), and
preference for process orientation (rigidity).
Convenience, identified as the dominant factor, underscores the importance of easily
purchasing the most suitable product. Content personalization strategies and automated
services were deemed appealing to this psychometric segment, emphasizing the
approachability of financial intelligent agents and virtual assistants.
Financial literacy, the second factor, was found to have a dual perspective. Customers with
low financial literacy require education and support for decision-making, aiming for financial
security. Conversely, highly literate customers with an interest in personal finance and market
developments were identified as an attractive segment for financial advice robots. The study
suggested tailored content personalization and predictive services for this segment, along
with a preference for additional information like reviews and ratings.
The third factor highlighted the significance of considering individuals' rigidity in decision-
making. Conservative customers, preferring control and thorough decision-making, may
initially seem unappealing for financial advice robots due to trust issues. However, smartly
developed digital tools, such as virtual financial assistants supporting systematic decision-
making, could cater to this segment's needs.
Financial literacy emerged as the most potent segmenting factor for digital financial advice,
complemented by factors such as convenience, guidance in the advice process, and attitudes
toward financial advice. Chapter 3 culminates in the formulation of a digital psychometric
segmentation model (DPS), clarifying which digital and robo-advice solutions can
responsibly be tailored to specific customer segments. Three distinctive customer segments
are identified: convenience seekers, rigid individuals, and knowledgeable trustfuls.
Collectively, Chapters 2 and 3 furnish novel psychometric segmentation insights and digital
advice experience benchmarks, offering valuable guidance for organizations embracing
digital financial advice solutions for the next generation.
In summation, part one of this dissertation contributes substantially to the evolving landscape
of closing the advisory gap with digital financial services for inclusive Banking 5.0 by
advancing our understanding of human centric tailored credit advice and psychometric
119937

Chapter 7
segmentation in the context of next-generation consumers. It was hypothesized that the Research question 2:
integration of experiential and psychometric determinants in digital financial advice systems
increases the likelihood of advice usage and significantly improves customer satisfaction. How does the application of psychometric determinants in digital credit scorecards improve
The research indeed highlights the importance of experiential attributes in financial advice access to finance?
systems, as well as the role of personality insights in expanding access to digital credit advice
within the framework of inclusive, smart Banking 5.0. The second hypothesis addressed within this dissertation has undergone scrutiny through two
distinct research endeavors. In Chapter 4, a pioneering psychometric credit scoring model
The empirical insights and models generated through this research offer scalable and was devised, leveraging contemporary insights into financial literacy, with the objective of
actionable guidance to governments, NGO’s, financial institutions, financial advisors, wealth fostering intelligent and inclusive financial practices tailored to the evolving needs of the
managers, and fintech companies seeking to enhance their inclusive digital financial advice upcoming generation of consumers. Based on comprehensive expertise, a conceptual
offerings and cater effectively to the diverse preferences of their customer base. This body of framework for a psychometric credit scorecard was delineated, specifically tailored for the
work not only enriches the scholarly discourse on the topic but also holds practical evolving landscape of Banking 5.0, subsequently subjected to a cross-national survey
implications for shaping the future of banking and regulatory strategies in a digitally-driven encompassing 897 individuals from low-income brackets across the United States of America
financial ecosystem. As we move forward, it is imperative that further research builds upon and The Netherlands. This survey marked a seminal endeavor, representing the inaugural
these foundations, exploring new dimensions and possibilities in the ever-evolving landscape application of a psychometric scorecard aimed at gauging attributes pertinent to financial
of financial services. It is crucial to emphasize that digital advisors must adhere to regulatory literacy.
requirements as they play a central role (Ostrowska & Balcerowski, 2020). There has been an
increase in regulation imposed on financial companies due to financial crisis and a higher The questionnaire, comprising 17 queries, was structured based on predefined psychometric
level of financial crimes including various financial frauds (Achim et al, 2021). Adherence to attributes and participants' demographic profiles, employing a 5-point Likert scale or binary
regulation brings challenges to the implementation of robo-advisors from technical and format for responses. The survey, automated for scalability, elicited responses concerning
procedural points of view. For large companies, regulation is even more complex as they participants' financial competencies, gratification tendencies, materialistic inclinations,
must comply with regulation for all activities. For instance, the upcoming European Union AI attitudes towards indebtedness, self-assurance levels, cognitive aptitude, social desirability,
Act declares AI systems used to evaluate score or creditworthiness of people, or credit risk and demographic particulars.
scoring (El Qadi et al, 2022) as high-risk AI systems, as their access to financial resources or
services such as housing, electricity or telecommunciation systems may lead to The ensuing analysis revealed an inverse correlation between individuals' financial acumen
discrimination or perpetuate historical biases, e.g., based on sex, racial or ethnic origins (AI and their propensity for arrears, suggesting that heightened financial literacy is associated
Act 2022). with diminished default occurrences. Furthermore, through the application of structural
equation modeling, the investigation furnished nuanced insights into the relative importance
Although applicable across the European Union and UK geographies, the limitations of the of various attributes, which were subsequently translated into a refined psychometric
research, including its European geographic specificity to the UK and Dutch market, the framework for customer risk stratification.
focus on digital financial advice and financial advice systems, and the need for additional
time-series research, should be considered when interpreting findings. Nonetheless, the Government-led initiatives aimed at bolstering financial literacy stand poised to mitigate
developed models and insights offer valuable contributions to understanding and improving tardy payment incidences and fortify financial well-being. Moreover, within the context of
customer experiences in the evolving landscape of inclusive Banking 5.0. holistic and inclusive banking paradigms, digital lending entities are also presented with an
opportune juncture to proffer digital educational resources and financial management support,
particularly catering to applicants demonstrating modest or inadequate financial literacy
7.3.2. Human-centric psychometrics for Banking 5.0 credit decision-making proficiencies.
In the similar context as discussed in chapter 7.1.1, intelligent digital financial services for
next generation banking customers need to be instant, personal and smart (PWC, 2018). Additionally, the research unveiled a notable positive correlation between individuals'
Credit scoring in that context is one the most important parts of credit risk management in attitudes towards indebtedness and their susceptibility to arrears, juxtaposed with a negative
reducing the risk of client defaults and bankruptcies (Gicic, et al. 2023). The challenge for correlation between social desirability and arrears incidence.
inclusive credit scoring, however, is that traditional repayment data is always backward
looking and assuming that the future will look like the past. Also, in developing economies or Chapter 6 delineates a secondary research endeavor designed as an experimental
when targeting low-income and first-time borrowers like Gen-z and millenials, external credit investigation aimed at assessing the potential value addition of the newly developed
history sources may be scarce and less robust (Vidal & Barbon, 2019). psychometric scorecard in the risk assessment of sole traders and micro-enterprises.
Complementing the scorecard, the attribute of fluid intelligence was incorporated. The
This has led to the formulation of the following research question for this dissertation: automated scorecard underwent scrutiny through experimentation involving 2,884 micro and
small businesses in the Czech Republic. To gauge its impact on access to finance, the study
scrutinized the actual payment behaviors of accepted borrowers before and amidst the
119984 195

Conclusion
segmentation in the context of next-generation consumers. It was hypothesized that the Research question 2:
integration of experiential and psychometric determinants in digital financial advice systems
increases the likelihood of advice usage and significantly improves customer satisfaction. How does the application of psychometric determinants in digital credit scorecards improve
The research indeed highlights the importance of experiential attributes in financial advice access to finance?
systems, as well as the role of personality insights in expanding access to digital credit advice
within the framework of inclusive, smart Banking 5.0. The second hypothesis addressed within this dissertation has undergone scrutiny through two
distinct research endeavors. In Chapter 4, a pioneering psychometric credit scoring model
The empirical insights and models generated through this research offer scalable and was devised, leveraging contemporary insights into financial literacy, with the objective of
actionable guidance to governments, NGO’s, financial institutions, financial advisors, wealth fostering intelligent and inclusive financial practices tailored to the evolving needs of the
managers, and fintech companies seeking to enhance their inclusive digital financial advice upcoming generation of consumers. Based on comprehensive expertise, a conceptual
offerings and cater effectively to the diverse preferences of their customer base. This body of framework for a psychometric credit scorecard was delineated, specifically tailored for the
work not only enriches the scholarly discourse on the topic but also holds practical evolving landscape of Banking 5.0, subsequently subjected to a cross-national survey
implications for shaping the future of banking and regulatory strategies in a digitally-driven encompassing 897 individuals from low-income brackets across the United States of America
financial ecosystem. As we move forward, it is imperative that further research builds upon and The Netherlands. This survey marked a seminal endeavor, representing the inaugural
these foundations, exploring new dimensions and possibilities in the ever-evolving landscape application of a psychometric scorecard aimed at gauging attributes pertinent to financial
of financial services. It is crucial to emphasize that digital advisors must adhere to regulatory literacy.
requirements as they play a central role (Ostrowska & Balcerowski, 2020). There has been an
increase in regulation imposed on financial companies due to financial crisis and a higher The questionnaire, comprising 17 queries, was structured based on predefined psychometric
level of financial crimes including various financial frauds (Achim et al, 2021). Adherence to attributes and participants' demographic profiles, employing a 5-point Likert scale or binary
regulation brings challenges to the implementation of robo-advisors from technical and format for responses. The survey, automated for scalability, elicited responses concerning
procedural points of view. For large companies, regulation is even more complex as they participants' financial competencies, gratification tendencies, materialistic inclinations,
must comply with regulation for all activities. For instance, the upcoming European Union AI attitudes towards indebtedness, self-assurance levels, cognitive aptitude, social desirability,
Act declares AI systems used to evaluate score or creditworthiness of people, or credit risk and demographic particulars.
scoring (El Qadi et al, 2022) as high-risk AI systems, as their access to financial resources or
services such as housing, electricity or telecommunciation systems may lead to The ensuing analysis revealed an inverse correlation between individuals' financial acumen
discrimination or perpetuate historical biases, e.g., based on sex, racial or ethnic origins (AI and their propensity for arrears, suggesting that heightened financial literacy is associated
Act 2022). with diminished default occurrences. Furthermore, through the application of structural
equation modeling, the investigation furnished nuanced insights into the relative importance
Although applicable across the European Union and UK geographies, the limitations of the of various attributes, which were subsequently translated into a refined psychometric
research, including its European geographic specificity to the UK and Dutch market, the framework for customer risk stratification.
focus on digital financial advice and financial advice systems, and the need for additional
time-series research, should be considered when interpreting findings. Nonetheless, the Government-led initiatives aimed at bolstering financial literacy stand poised to mitigate
developed models and insights offer valuable contributions to understanding and improving tardy payment incidences and fortify financial well-being. Moreover, within the context of
customer experiences in the evolving landscape of inclusive Banking 5.0. holistic and inclusive banking paradigms, digital lending entities are also presented with an
opportune juncture to proffer digital educational resources and financial management support,
particularly catering to applicants demonstrating modest or inadequate financial literacy
7.3.2. Human-centric psychometrics for Banking 5.0 credit decision-making proficiencies.
In the similar context as discussed in chapter 7.1.1, intelligent digital financial services for
next generation banking customers need to be instant, personal and smart (PWC, 2018). Additionally, the research unveiled a notable positive correlation between individuals'
Credit scoring in that context is one the most important parts of credit risk management in attitudes towards indebtedness and their susceptibility to arrears, juxtaposed with a negative
reducing the risk of client defaults and bankruptcies (Gicic, et al. 2023). The challenge for correlation between social desirability and arrears incidence.
inclusive credit scoring, however, is that traditional repayment data is always backward
looking and assuming that the future will look like the past. Also, in developing economies or Chapter 6 delineates a secondary research endeavor designed as an experimental
when targeting low-income and first-time borrowers like Gen-z and millenials, external credit investigation aimed at assessing the potential value addition of the newly developed
history sources may be scarce and less robust (Vidal & Barbon, 2019). psychometric scorecard in the risk assessment of sole traders and micro-enterprises.
Complementing the scorecard, the attribute of fluid intelligence was incorporated. The
This has led to the formulation of the following research question for this dissertation: automated scorecard underwent scrutiny through experimentation involving 2,884 micro and
small businesses in the Czech Republic. To gauge its impact on access to finance, the study
scrutinized the actual payment behaviors of accepted borrowers before and amidst the
194 119959

Chapter 7
COVID-19 pandemic, utilizing data from a fintech company and conducting a counterfactual
analysis juxtaposed with their conventional credit scoring model.
The findings of this experimentation underscored the efficacy of the psychometric scorecard
in facilitating risk-appropriate differentiation for sole traders and micro-organizations.
Notably, a significant correlation emerged between financial skills, self-efficacy, debt
attitudes, and social desirability with default occurrences. Moreover, the counterfactual
analysis revealed that, within this customer segment, the psychometric scorecard exhibited
superior risk differentiation compared to the traditional scoring model, particularly evident
during the heightened stress period induced by COVID-19.
Both research investigations collectively shed light on the robustness of the novel
psychometric credit scorecard, particularly emphasizing its resilience during periods of crisis.
Moreover, it outperformed conventional credit scoring models in environments characterized
by a dearth of traditional credit data, thereby contributing to financial inclusion as an
emerging source of growth in the banking sector, while concurrently enhancing access to
finance.
7.3.3. AI-based credit scoring for Banking 5.0 credit decision-making
Credit scoring models are designed to provide financial institutions with predictions about
borrowers' probability of repaying credit and to distinguish borrowers into two categories:
good credit and bad credit (Jadhav et al., 2018; Khalili & Rastegar, 2023), facilitating
financial institutions to assess borrowers' credit risk more accurately. Accuracy and
interpretability represent two critical themes within credit scoring prediction (Bücker et al.,
2022; Kyeong & Shin, 2022). The data availability and imbalance problem and modeling
method selection affect the accuracy of credit scoring prediction (Liu et al., 2024). This has
led to the final research question:
Research question 3:
How does the application of artificial intelligence in credit scoring systems improves risk
model accuracy and predictive power?
Chapter 5 elaborates on the third research phase, which investigates AI-based credit
scorecards counterfactually compared to traditional logistic regression scorecards. To address
data imbalance issues, three major credit providers were involved, resulting in a research
sample of 133,152 mortgage and credit card customers across the United Kingdom and the
Netherlands. The research encompasses three experiments with tier 1 and tier 2 lenders,
utilizing neural networks and decision trees as AI models. Decision trees were consistently
employed for their interpretability. The AI-based models exhibited superior accuracy and
predictive power for both asset classes (mortgages and credit cards) and geographies (UK and
The Netherlands) researched compared to traditional logistic regression models and therefore
support the transformation to Banking 5.0 business models. Decision tree methodologies
were favored for their ability to capture non-linear relationships, handle missing values,
provide clear variable importance indications, automatically select relevant features,
accommodate complex decision boundaries, and minimize the influence of outliers.
Therefore, the application of AI in credit decision-making helps close the access-to-finance
gap for underserved customer segments, thanks to its improved scoring capabilities.
210906

Conclusion
COVID-19 pandemic, utilizing data from a fintech company and conducting a counterfactual However, financial regulations in Europe and the United Kingdom prioritize the
analysis juxtaposed with their conventional credit scoring model. explainability of credit decisions, still making logistic regressions the preferred model
approach for precise credit decision-making. Nevertheless, decision trees are deemed more
The findings of this experimentation underscored the efficacy of the psychometric scorecard suitable for credit scoring when integrating alternative psychometric and behavioral data to
in facilitating risk-appropriate differentiation for sole traders and micro-organizations. enhance financial inclusion. Notably, experiments involving alternative psychometric data
Notably, a significant correlation emerged between financial skills, self-efficacy, debt had a more pronounced impact on model performance enhancements than the adoption of
attitudes, and social desirability with default occurrences. Moreover, the counterfactual advanced modeling techniques.
analysis revealed that, within this customer segment, the psychometric scorecard exhibited
superior risk differentiation compared to the traditional scoring model, particularly evident In conclusion, this dissertation significantly contributes to the evolving landscape of human-
during the heightened stress period induced by COVID-19. centered inclusive Banking 5.0 by deepening our comprehension of inclusive financial advice
and credit decision-making and the transformative role of AI in granually catering to the
Both research investigations collectively shed light on the robustness of the novel needs of next-generation consumers and small businesses. Our initial hypotheses posited that
psychometric credit scorecard, particularly emphasizing its resilience during periods of crisis. the integration of AI and psychometrics would enrich digital advice and credit decision-
Moreover, it outperformed conventional credit scoring models in environments characterized making processes, and the research findings corroborate this assertion. As a result of this
by a dearth of traditional credit data, thereby contributing to financial inclusion as an research, novel foundational models for the micro-personalization of inclusive financial
emerging source of growth in the banking sector, while concurrently enhancing access to advice have been developed, along with pioneering credit scorecards tailored for inclusive
finance. finance in Europe and the USA. These models have now been implemented to enhance
financial accessibility.
7.3.3. AI-based credit scoring for Banking 5.0 credit decision-making
Credit scoring models are designed to provide financial institutions with predictions about Moving forward, it is essential for future research endeavors to build upon the foundational
borrowers' probability of repaying credit and to distinguish borrowers into two categories: insights gleaned from this study, exploring new dimensions and possibilities within the ever-
good credit and bad credit (Jadhav et al., 2018; Khalili & Rastegar, 2023), facilitating evolving landscape of financial services. However, it is crucial to acknowledge the
financial institutions to assess borrowers' credit risk more accurately. Accuracy and limitations of this research, including its geographic specificity to Western markets such as
interpretability represent two critical themes within credit scoring prediction (Bücker et al., the UK, USA, Netherlands, and Czech Republic, as well as its focus on digital credit
2022; Kyeong & Shin, 2022). The data availability and imbalance problem and modeling decision-making. Despite these limitations, the developed models and insights offer valuable
method selection affect the accuracy of credit scoring prediction (Liu et al., 2024). This has contributions to our understanding of inclusive holistic banking practices and serve as a
led to the final research question: stepping stone towards fostering greater financial inclusion and resilience in our increasingly
digital world.
Research question 3:
How does the application of artificial intelligence in credit scoring systems improves risk
model accuracy and predictive power?
Chapter 5 elaborates on the third research phase, which investigates AI-based credit
scorecards counterfactually compared to traditional logistic regression scorecards. To address
data imbalance issues, three major credit providers were involved, resulting in a research
sample of 133,152 mortgage and credit card customers across the United Kingdom and the
Netherlands. The research encompasses three experiments with tier 1 and tier 2 lenders,
utilizing neural networks and decision trees as AI models. Decision trees were consistently
employed for their interpretability. The AI-based models exhibited superior accuracy and
predictive power for both asset classes (mortgages and credit cards) and geographies (UK and
The Netherlands) researched compared to traditional logistic regression models and therefore
support the transformation to Banking 5.0 business models. Decision tree methodologies
were favored for their ability to capture non-linear relationships, handle missing values,
provide clear variable importance indications, automatically select relevant features,
accommodate complex decision boundaries, and minimize the influence of outliers.
Therefore, the application of AI in credit decision-making helps close the access-to-finance
gap for underserved customer segments, thanks to its improved scoring capabilities.
196 129071

Chapter 7
Table 2
Research findings & their implications
Research Question Key Findings Practical Implications
The Digital Customer Experience Index (DCX) provides insight in
How do individual psychological factors, like lifestyles, attitudes customer satisfaction drivers for digital advice systems: It Product development & Marketing: Understanding what drives
identifies which factors most significantly influence customer customer satisfaction allows companies to focus on enhancing
and behaviors, impact holistic digital finance within the
satisfaction in digital advice systems, such as the quality these aspects in their product offerings and tailor their
inclusive Banking 5.0 framework ?
(accuracy) of the advice, co-creation possibilities and width of marketing campaigns on them.
the product offering of the advice provided.
Customer Relationship Management: Understanding a
The DCX model provides insight in Pain Points and Frictions: customer’s psychological profile can help banks tailor their
Pinpoint common obstacles or frustrations that customer communication and service strategies. For example, customers
encounter while receiving digital advice. These could include, identified as risk-averse might prefer more conservative
unclear guidance, lack of co-creation options, or insufficient investment products and value financial advice, while those
personalization. with a higher tolerance for risk might be more open to
aggressive do-it-yourselves investment strategies
Deep Personalization: In Banking 5.0, psychometric data can be
The DCX model has predictive value for predicting customers at used to achieve unprecedented levels of service personalization.
risk: It predicts customer satisfaction levels and This data helps in understanding not just the financial behaviors
preemptively helps identifying at-risk customers or but also the psychological and emotional aspects of customers.
Banks can use this insight to design products that not only meet
scenarios where customer satisfaction might dip financial needs but also align with individual personality traits,
lifestyle choices, and behavioral tendencies.
The Digital Psychometric Segmentation Model (DPS) supports
understanding how different customer segments (e.g., Enhanced Customer Interaction: Banking 5.0 aims to leverage
convenience seekers, rigids, financially ignorants and technology to make customer interactions more intuitive and
trustfulls with knowledge) perceive and value different human-like. Psychometric data can inform AI-driven chatbots
and virtual assistants, making these technologies more adept at
digital advice applications. This can help tailor digital understanding and responding to the emotional states and
services to better meet the diverse needs and preferences of users, thus improving customer experience
preferences of various user groups.
Inclusive growth: By leveraging psychometric assessments,
Inclusion of personality traits like financial skills, confidence banks can extend their services to previously unreachable
How do individual psychological factors like lifestyles, attitudes,
levels, debt attitudes, impulse buying tendencies and segments of the population. This approach has been notably
and behaviors influence comprehensive inclusive credit risk
materialism leads to better risk prediction models for consumer successful in small business finance, where psychometric tests
management within the context of inclusive banking 5.0?
lenders help lenders evaluate the entrepreneurial potential and
trustworthiness of applicants who lack formal financial records.
Enhanced Credit Scoring Models: Psychometric data allows
banks to build more comprehensive and nuanced credit scoring
Inclusion of personality traits like financial skills, confidence models. These models assess not just financial history, but also
levels, debt attitudes, impulse buying tendencies,materialism psychological traits such as personality, attitudes towards
and fluid intelligence leads to better risk prediction models for money, and decision-making patterns. This can be particularly
retail lenders valuable in extending credit to those with thin or no traditional
credit histories, such as young people, self-empoloyed, new
immigrants, or residents of less developed regions.
Inclusion of personality traits like financial skills, confidence Enhanced Risk Management: Psychometric data can aid in the
levels, debt attitudes, impulse buying tendencies, materialism early identification of potential defaulters by analyzing behavior
and fluid intelligence leads to better risk prediction models for patterns and psychological traits associated with high financial
small business lenders risk behaviors. This proactive approach can help mitigate risks
before they manifest as financial losses.
Enhanced Risk Management: AI enhances the predictive
How does the integration of artificial intelligence into credit accuracy of credit scorecards by identifying complex patterns
scoring enhance credit scorecards within the scope of inclusive AI- models outperform tradtional models in predicting credit and relationships in the data that traditional statistical methods
Banking 5.0? risk miss. This leads to more nuanced risk assessments, reducing
the likelihood of overlooking viable candidates for credit or
incorrectly assessing the risk associated with certain profiles.
210928

Conclusion
Table 2  7.4 Contribution of the dissertation to the literature
  With the answers to our research questions in mind, we now turn to the broader scientific
Research findings & their implications  implications of our work. This section will explore how our findings contribute to the
  existing body of literature and suggest directions for future research. It discusses the
dissertation’s major contributions and implications, its limitations and suggestions for future
| Research Question |     | Key Findings |     | Practical Implications |     |     |     |
| ----------------- | --- | ------------ | --- | ---------------------- | --- | --- | --- |
The  Digital Customer Experience Index (DCX) provides insight in  research in the next three paragraphs.
How do individual psychological factors, like lifestyles, attitudes  c u s to m e r   sa t i sf a c t io n   d r ive r s   f o r  d i g it a l  a d v ic e  s y s t e m s :  I t   P ro d u ct  d e v e l o p m e n t  &   M ar k e t ing :  U n d e r s t a n d i n g  w h a t  d r i v e s
and behaviors,  impact holistic digital finance within the  id e n ti fie s   w h i c h  f a c t o r s  m o s t   s ig n i f ic a n t ly   in f lu e n c e   cu s t o m er  cu s to m e r  s a t i sf a ct io n   al l ow s  c o m p a ni e s  t o   f o c u s  o n  e n h a n c i n g
|     | satisfaction in digital advice systems, such as the quality  |     | these aspects in their product offerings and tailor their  |     |     |     |     |
| --- | ------------------------------------------------------------ | --- | ---------------------------------------------------------- | --- | --- | --- | --- |
inclusive Banking 5.0 framework ? (accuracy) of the advice, co-creation possibilities and width of  marketing campaigns on them. 7.4.1 Contributions & implications
the product offering of the advice provided. In this subsection, the dissertation’s general contributions are stated and their implications
Customer Relationship Management:  Understanding a
The DCX model provides insight in Pain Points and Frictions:  customer’s psychological profile can help banks tailor their  discussed. The first part of this subsection presents three major contributions to the human-
Pinpoint common obstacles or frustrations that customer  communication and service strategies. For example, customers  centered AI movement in multi-disciplinary research (computer science, statistics and social
|     | encounter while receiving digital advice. These could include,  |     | identified as risk-averse might prefer more conservative     |     |     |     |     |
| --- | --------------------------------------------------------------- | --- | ------------------------------------------------------------ | --- | --- | --- | --- |
|     | unclear guidance, lack of co-creation options, or insufficient  |     | investment products and value financial advice, while those  |     |     |     |     |
personalization. with a higher tolerance for risk might be more open to  & behavioral science). That is, this dissertation provides empirical insight into the
aggressive do-it-yourselves investment strategies
differentiating power of personality-centered models in the digital transformation to inclusive
Deep Personalization: In Banking 5.0, psychometric data can be  Banking 5.0. Another significant contribution is the novel psychometric credit scoring
|     | The DCX model has predictive value for predicting customers at  |     | used to achieve unprecedented levels of service personalization.  |     |     |     |     |
| --- | --------------------------------------------------------------- | --- | ----------------------------------------------------------------- | --- | --- | --- | --- |
This data helps in understanding not just the financial behaviors  methodology (developed and applied in chapter 4 and 6) for inclusive finance. Lastly, this
risk: It predicts customer satisfaction levels and
preemptively helps identifying at-risk customers or  b u t  a ls o  t h e   p s y c h o l o g i c a l  a n d   e m o t i o n a l  a s p e c t s   o f  c u s to m e rs .   study pioneers a transformative digital lifestyle-based paradigm for human-centric AI,
|     | scenarios where customer satisfaction might dip |     | B a n ks  c a n   u s e   th i s |  i n s i g h t   to   d e s ig n   p r o d u c t s  t | h a t   n o t  o n ly  m e e t   |     |     |
| --- | ----------------------------------------------- | --- | -------------------------------- | ----------------------------------------------------- | -------------------------------- | --- | --- |
financial needs but also align with individual personality traits,
lifestyle choices, and behavioral tendencies. supported by empirical research. It offers strategic decision-makers in financial institutions a
blueprint for propelling their companies into the inclusive digital future, embracing the
The  Digital Psychometric Segmentation Model (DPS) supports
understanding how different customer segments (e.g.,  Enhanced Customer Interaction: Banking 5.0 aims to leverage  human-centricity of Banking 5.0.
|     | convenience seekers, rigids, financially ignorants and   |     | technology to make customer interactions more intuitive and      |     |     |     |     |
| --- | -------------------------------------------------------- | --- | ---------------------------------------------------------------- | --- | --- | --- | --- |
|     |                                                          |     | human-like. Psychometric data can inform AI-driven chatbots      |     |     |     |     |
|     | trustfulls with knowledge) perceive and value different  |     | and virtual assistants, making these technologies more adept at  |     |     |     |     |
digital advice applications. This can help tailor digital
understanding and responding to the emotional states and  In the second part of this subsection, this dissertation’s contributions to multiple paradigm
|     | services to better meet the diverse needs and  |     | preferences of users, thus improving customer experience |     |     |     |     |
| --- | ---------------------------------------------- | --- | -------------------------------------------------------- | --- | --- | --- | --- |
preferences of various user groups. research are stated. Adopting a new paradigm, this study contributes to the extensive body of
knowledge by broadening the conceptual scope of theorizing human-centered AI adoption in
Inclusive growth: By leveraging psychometric assessments,
How do individual psychological factors like lifestyles, attitudes,  Inclusion of personality traits like financial skills, confidence  banks can extend their services to previously unreachable  financial institutions. This dissertation demonstrates that current research orientations in
|     | levels, debt attitudes,  impulse buying tendencies and  |     | segments of the population. This approach has been notably  |     |     |     |     |
| --- | ------------------------------------------------------- | --- | ----------------------------------------------------------- | --- | --- | --- | --- |
and behaviors influence comprehensive inclusive credit risk  materialism leads to better risk prediction models for consumer successful in small business finance, where psychometric tests
management within the context of inclusive banking 5.0? lenders help lenders evaluate the entrepreneurial potential and  human-centered AI are partial because they systematically stress just the technology side.
trustworthiness of applicants who lack formal financial records. That is, current human-centered AI research centralizes the importance of: explainable AI
(XAI), human-AI collaboration, design, ethics and fairness in the models. This dissertation is,
Enhanced Credit Scoring Models: Psychometric data allows
banks to build more comprehensive and nuanced credit scoring  by my knowledge, the first research to a digital financial personality-centered paradigm that
|     | Inclusion of personality traits like financial skills, confidence  |     | models. These models assess not just financial history, but also  |     |     |     |     |
| --- | ------------------------------------------------------------------ | --- | ----------------------------------------------------------------- | --- | --- | --- | --- |
|     | levels, debt attitudes, impulse buying tendencies,materialism      |     | psychological traits such as personality, attitudes towards       |     |     |     |     |
and fluid intelligence leads to better risk prediction models for  money, and decision-making patterns. This can be particularly  helps to understand what drives the root causes of customer behavior as a foundation for
retail lenders valuable in extending credit to those with thin or no traditional  hyper-personalized inclusive finance. Something that is required for designing inclusive
credit histories, such as young people, self-empoloyed, new
immigrants, or residents of less developed regions. Banking 5.0 applications.

|     | Inclusion of personality traits like financial skills, confidence  |     | Enhanced Risk Management: Psychometric data can aid in the  |     |     |     |     |
| --- | ------------------------------------------------------------------ | --- | ----------------------------------------------------------- | --- | --- | --- | --- |
levels, debt attitudes, impulse buying tendencies, materialism  early identification of potential defaulters by analyzing behavior  Finally, this dissertation’s contribution to digital banking research is stated. This dissertation
patterns and psychological traits associated with high financial
|     | and fluid intelligence leads to better risk prediction models for  |     | risk behaviors. This proactive approach can help mitigate risks  |     |     |     |     |
| --- | ------------------------------------------------------------------ | --- | ---------------------------------------------------------------- | --- | --- | --- | --- |
small business lenders provides an empirical example as on how lifestyle centered AI methodologies can improve
before they manifest as financial losses.
inclusive banking applications. These contributions are elaborated below.
Enhanced Risk Management: AI enhances the predictive
How does the integration of artificial intelligence into credit  accuracy of credit scorecards by identifying complex patterns
|     | AI- models outperform tradtional models in predicting credit  |     | and relationships in the data that traditional statistical methods   |     |     |     |     |
| --- | ------------------------------------------------------------- | --- | -------------------------------------------------------------------- | --- | --- | --- | --- |
scoring enhance credit scorecards within the scope of inclusive  risk miss. This  leads to more nuanced risk assessments, reducing  7.4.1.1. Lifestyle-centered AI for digital & robo-advice 5.0 applications
Banking 5.0? the likelihood of overlooking viable candidates for credit or
incorrectly assessing the risk associated with certain profiles.   The Big Five personality trait theory defines the lifestyle of an individual in terms of motives,
  thoughts, and emotions. In the course of time, there has been significant disagreement by
  several scholars on the Big Five trait theory because they fail to follow the patterning of
  lifestyle and personality (Epstein, 1994). After this, many scholars have found several new
  traits in the field of personality and lifestyle from different perspectives. Especially the
  impact of digital on the understanding of the personality and lifestyle impact is making
  traditional lifestyles obsolete (Desai, 2020). The development of information technology and
  the internet has played a role of change agents and transformed the market, society and
  humans’ lifestyle all together ( Kumar & Chaubey, 2017; Thaichon, 2017). The present
  generation popularly known as Generation Z is largely seeking services like shopping,
  banking and investment, learning, communication and even medical care also at their
  doorstep with the help of digital platforms (Seemiller & Grace, 2017; Thaichon, 2017). The
survey of many countries states the large proportion of internet users are availing services

|     |     | 198  |     |     |     |     | 129093  |
| --- | --- | ---- | --- | --- | --- | --- | ------- |

Chapter 7
like online education, money transfer, shopping and or keeping money into e-wallet to
upgrade their lifestyle (Kahawandala & Peter 2020). Limited research, however, has been Although the digital advice segments are new, they are partly in line with other studies to
conducted on the influence of personality on human-computer interaction, both in general traditional financial advice (Aliyousif and Kalenkoski, 2017). Using the 2012 National
and particularly in the context of financial advice and financial services. Financial Capability Study, this research shows that income, risk tolerance, and financial
literacy are related positively to the demand for financial advice and more greatly affect the
To address this research gap and fill a notable research void concerning the adoption of probability of seeking advice than do other variables. A low perception of financial
digital advisory services, this dissertation adopts an innovative approach by employing knowledge and financial fragility decrease the probability of seeking certain types of
structural equation modeling in this domain. The analysis encompasses a comprehensive inclusive financial advice. People who lack confidence in their financial knowledge, who
array of variables aimed at identifying the primary determinants of a positive customer struggle with their expenses, and are not able to save for retirement or emergency needs
experience with digital advisory solutions (as detailed in Chapter 2). might not have the luxury to think about investment or tax planning. This is called ‘the
advice-gap’. This dissertation contributes to the existing body of research on financial advice
The digital customer experience models for the UK and The Netherlands can help bridge the by highlighting that, in the realm of digital advice, the desire for convenience and a process-
advice gap by customizing digital advisory solutions for individuals who require but currently oriented approach significantly shapes the willingness to embrace digital advisory
lack access to financial advice.To effectively address the advice gap, a deeper understanding applications. Moreover, this inclination varies depending on the specific manifestation it
of the drivers of customer satisfaction with digital advisory solutions is imperative. takes. For instance, individuals seeking convenience exhibit greater receptivity to robo-
Consequently, the DCX model predicts customer satisfaction with the advisory experience advisors compared to those who prefer exploring financial matters independently. Given that
and identifies three critical groups of attributes influencing adoption: system-related, process- only 25-33% of the U.S. population is estimated to seek professional financial advice
related, and outcome-related attributes. The most significant factor in the model is the quality (Collins, 2012), despite widespread financial challenges among households (Brooks et al.
of advice or support, followed by the ability to tailor to individual situations through co- 2015), including a significant portion facing difficulties obtaining reasonably priced loans
creation. Additionally, the breadth of the product offering takes precedence over pricing due to poor credit scores (Brooks et al. 2015) and low retirement confidence (Helman,
considerations. VanDerhei and Copeland, 2015), the accessibility of smart digital financial advice could
potentially address this advice gap for a broader audience.
Nowadays, ninety percent of financial customers feel that their relationship with their
financial institutions (FIs) is based solely on simple transactional activities, such as making a Part 1 of this dissertation researches the openness to and desired user experience of digital
deposit or withdrawing money (Moise, 2018). Moise argues that today’s digitally minded and robo-advice solutions and contributes a human-centered paradigm that helps to make
customers, however, expect tailored, seamless and secure user experiences that excite and digital advice solutions more accessible and personalized. In short, the research contributes to
delight, such as those provided by leading brands like Google, Apple, Facebook and Amazon the broader understanding of inclusive digital advice adoption and user experience,
and that FIs must cater to the elevated standards for user experience and take advantage of positioning it within the context of changing lifestyles and technological transformations
how people share, consume and exchange data every day. The rapid growth of information towards an inclusive Banking 5.0 context.
technology has made it possible for bank customers to be more connected to their bank
accounts through the Internet and mobile. Li et al. call this e-banking (Li et al. 2021). E- 7.4.1.2. Psychometric credit scoring for inclusive finance
banking is the optimal combination of total bank activities through the utilization of modern This dissertation aims to promote human-centered AI paradigm for inclusive finance by
information technology that provides all the services based on customers’ needs. The investigating which customer segments are receptive to various digital/robo-advice solutions.
researchers found that four factors drive customer satisfaction towards e-banking are cloud In addition to enhancing financial accessibility through e-banking and digital/robo-advisors
services, security, e-learning, and service quality. Chapter 3 researches how personality for a broader audience, another crucial challenge is to revolutionize traditional credit scoring.
drivers can improve micro-segmentation for digital and robo-advisors. Traditional credit scoring methods currently exclude billions of people from accessing credit,
and overcoming this obstacle is essential for fostering financial inclusion.
In his study Al-Dhmour found that there were no statistically significant differences between
the lifestyle patterns of mobile banking applications of users and non-users. However, the Initially, Credit Scoring Models (CSMs) relied on demographic and financial data. However,
lifestyle patterns of users had some common themes; fashion consciousness, leadership traits, we contend that this approach has limitations when it comes to assessing the creditworthiness
family concern, health consciousness, carefree, community conscious and practicality had of underserved customer segments, such as sole traders, micro-organizations, SME’s and
significance impact on mobile applications users (Al-Dhmour et.al, 2020). This dissertation billions of people in developing countries. Nevertheless, a systematic literature review on
finds three factors for segmenting consumer markets for digital or robo-advice solutions credit scoring suggests that a minimal number of articles have considered alternative
(Chapter 3). variables (other than financial, economic, and demographic data) to assess the borrower’s
creditworthiness (Onay & Ozturk, 2018). But, to promote financial inclusion, it has been
Drawing on cross-cultural factors, this dissertation identifies four innovative segments for observed that these models are undergoing rapid transformations (Goel & Rastogi, 2023).
human-centered digital financial advice applications in Chapter 3. These segments are The lending industry has therefore transformed CSMs in adopting certain alternative
derived using a Ward-clustering methodology and distinguish themselves based on financial variables, such as the borrower’s social media data (Hendricks and Budree, 2019; De Cnudde
knowledge, preferences for convenience in financial advice, and their level of process et al., 2019), utility data (Djeundje et al., 2021), mobile phone data (Agarwal et al., 2020),
orientation. psychological data (Azma et al., 2019) and so on. The idea behind using such non-traditional
220040 201

Conclusion
like online education, money transfer, shopping and or keeping money into e-wallet to
upgrade their lifestyle (Kahawandala & Peter 2020). Limited research, however, has been Although the digital advice segments are new, they are partly in line with other studies to
conducted on the influence of personality on human-computer interaction, both in general traditional financial advice (Aliyousif and Kalenkoski, 2017). Using the 2012 National
and particularly in the context of financial advice and financial services. Financial Capability Study, this research shows that income, risk tolerance, and financial
literacy are related positively to the demand for financial advice and more greatly affect the
To address this research gap and fill a notable research void concerning the adoption of probability of seeking advice than do other variables. A low perception of financial
digital advisory services, this dissertation adopts an innovative approach by employing knowledge and financial fragility decrease the probability of seeking certain types of
structural equation modeling in this domain. The analysis encompasses a comprehensive inclusive financial advice. People who lack confidence in their financial knowledge, who
array of variables aimed at identifying the primary determinants of a positive customer struggle with their expenses, and are not able to save for retirement or emergency needs
experience with digital advisory solutions (as detailed in Chapter 2). might not have the luxury to think about investment or tax planning. This is called ‘the
advice-gap’. This dissertation contributes to the existing body of research on financial advice
The digital customer experience models for the UK and The Netherlands can help bridge the by highlighting that, in the realm of digital advice, the desire for convenience and a process-
advice gap by customizing digital advisory solutions for individuals who require but currently oriented approach significantly shapes the willingness to embrace digital advisory
lack access to financial advice.To effectively address the advice gap, a deeper understanding applications. Moreover, this inclination varies depending on the specific manifestation it
of the drivers of customer satisfaction with digital advisory solutions is imperative. takes. For instance, individuals seeking convenience exhibit greater receptivity to robo-
Consequently, the DCX model predicts customer satisfaction with the advisory experience advisors compared to those who prefer exploring financial matters independently. Given that
and identifies three critical groups of attributes influencing adoption: system-related, process- only 25-33% of the U.S. population is estimated to seek professional financial advice
related, and outcome-related attributes. The most significant factor in the model is the quality (Collins, 2012), despite widespread financial challenges among households (Brooks et al.
of advice or support, followed by the ability to tailor to individual situations through co- 2015), including a significant portion facing difficulties obtaining reasonably priced loans
creation. Additionally, the breadth of the product offering takes precedence over pricing due to poor credit scores (Brooks et al. 2015) and low retirement confidence (Helman,
considerations. VanDerhei and Copeland, 2015), the accessibility of smart digital financial advice could
potentially address this advice gap for a broader audience.
Nowadays, ninety percent of financial customers feel that their relationship with their
financial institutions (FIs) is based solely on simple transactional activities, such as making a Part 1 of this dissertation researches the openness to and desired user experience of digital
deposit or withdrawing money (Moise, 2018). Moise argues that today’s digitally minded and robo-advice solutions and contributes a human-centered paradigm that helps to make
customers, however, expect tailored, seamless and secure user experiences that excite and digital advice solutions more accessible and personalized. In short, the research contributes to
delight, such as those provided by leading brands like Google, Apple, Facebook and Amazon the broader understanding of inclusive digital advice adoption and user experience,
and that FIs must cater to the elevated standards for user experience and take advantage of positioning it within the context of changing lifestyles and technological transformations
how people share, consume and exchange data every day. The rapid growth of information towards an inclusive Banking 5.0 context.
technology has made it possible for bank customers to be more connected to their bank
accounts through the Internet and mobile. Li et al. call this e-banking (Li et al. 2021). E- 7.4.1.2. Psychometric credit scoring for inclusive finance
banking is the optimal combination of total bank activities through the utilization of modern This dissertation aims to promote human-centered AI paradigm for inclusive finance by
information technology that provides all the services based on customers’ needs. The investigating which customer segments are receptive to various digital/robo-advice solutions.
researchers found that four factors drive customer satisfaction towards e-banking are cloud In addition to enhancing financial accessibility through e-banking and digital/robo-advisors
services, security, e-learning, and service quality. Chapter 3 researches how personality for a broader audience, another crucial challenge is to revolutionize traditional credit scoring.
drivers can improve micro-segmentation for digital and robo-advisors. Traditional credit scoring methods currently exclude billions of people from accessing credit,
and overcoming this obstacle is essential for fostering financial inclusion.
In his study Al-Dhmour found that there were no statistically significant differences between
the lifestyle patterns of mobile banking applications of users and non-users. However, the Initially, Credit Scoring Models (CSMs) relied on demographic and financial data. However,
lifestyle patterns of users had some common themes; fashion consciousness, leadership traits, we contend that this approach has limitations when it comes to assessing the creditworthiness
family concern, health consciousness, carefree, community conscious and practicality had of underserved customer segments, such as sole traders, micro-organizations, SME’s and
significance impact on mobile applications users (Al-Dhmour et.al, 2020). This dissertation billions of people in developing countries. Nevertheless, a systematic literature review on
finds three factors for segmenting consumer markets for digital or robo-advice solutions credit scoring suggests that a minimal number of articles have considered alternative
(Chapter 3). variables (other than financial, economic, and demographic data) to assess the borrower’s
creditworthiness (Onay & Ozturk, 2018). But, to promote financial inclusion, it has been
Drawing on cross-cultural factors, this dissertation identifies four innovative segments for observed that these models are undergoing rapid transformations (Goel & Rastogi, 2023).
human-centered digital financial advice applications in Chapter 3. These segments are The lending industry has therefore transformed CSMs in adopting certain alternative
derived using a Ward-clustering methodology and distinguish themselves based on financial variables, such as the borrower’s social media data (Hendricks and Budree, 2019; De Cnudde
knowledge, preferences for convenience in financial advice, and their level of process et al., 2019), utility data (Djeundje et al., 2021), mobile phone data (Agarwal et al., 2020),
orientation. psychological data (Azma et al., 2019) and so on. The idea behind using such non-traditional
200 220015

Chapter 7
or open data sets is to serve those underbanked segments and unbanked populations who face
financial constraints due failing to meet the ‘Know your Customer’ (KYC) financial data
requirements to verify customer identity (Elliott et al., 2022). Such studies have shown that
inclusive credit scoring is not limited to demographic and economic variables, other variables
can be explored that increase the accuracy to predict the default nature of borrowers.
This dissertation makes four contributions to the field of inclusive human-centered credit
decision-making, utilizing FinTech innovation to facilitate financial inclusion for vulnerable
consumer segments, entrepreneurs, small businesses and their associated lenders. First, this
dissertation is the first to develop a credit score model that connects financial literacy with
lifestyle and personality of the borrower in predicting a borrowers credit worthiness (Chapter
4). This model can function as a paradigm for future human-centered AI risk scoring
solutions. Secondly, while other research has focused on psychometric credit scoring in
developing countries for SMEs, this dissertation stands out as the first to utilize data from
highly regulated Western markets such as the USA and The Netherlands in Europe for model
training (Chapter 4). Thirdly, this dissertation is the first to counterfactually test psychometric
credit scoring models for small businesses and sole traders on real behavioral small business
data in an European market (Czech Republic) (Chapter 5). Where prior studies have applied
small back-test experiments (e.g., use of traditional financial data sources (Klinger 2013)) for
probability of default testing, we employ dynamic near real-time psychometric and financial
data from a CZ-based FinTech firm to not only assess the validity of the PSM for
incorporation in both FinTech and mainstream credit scoring procedures for probability of
default testing, but also translate the results into profit impact. Fourth, this dissertation is the
first that counterfactually explores the predictiveness and stability of the psychometric credit
scoring model during a period of high stress (COVID-19 Pandemic: August 2019-February
2022).
The objective of the study is to develop a psychometric model to explore the hypothesis that
financial personality-centric credit scoring could improve financial access for vulnerable
consumer segments in the USA and the Netherlands, especially relevant during times of
market instability. This research fills a critical gap by emphasizing the significance of
financial personality factors in shaping payment behavior when traditional financial data is
scarce or outdated, as exemplified during crises like COVID-19 or high inflationary market
contexts. Our findings corroborate the core hypothesis and, also we apply novel financial
literacy related attributes in our model, align with previous studies by Klinger et al. (2013)
and Hurley and Adebayo (2016), emphasizing the relevance of personality traits also in
promoting financial inclusion of small businesses.
Prior studies have primarily examined the influence of individual psychometric traits on
financial behavior. However, this study stands out as a groundbreaking endeavor, employing
structural equation modeling to integrate personality attributes linked to financial literacy in
volatile market conditions. The outcome is the creation of a comprehensive personality-
centric logistic regression model tailored for credit scoring in highly regulated markets.
Furthermore, our research uncovered new psychometric components such as "financial
accument" and "financial vulnerable optimism."
Despite these novel findings, our results remain consistent with Lussardi & Mitchell’s (2011)
assertion that financial knowledge plays a substantial role in financial inclusion, as
hypothesized in our conceptual model. Nonetheless, our study opted for the use of financial
220062

Conclusion
or open data sets is to serve those underbanked segments and unbanked populations who face skills instead of financial knowledge in predicting payment behavior, drawing upon Dew and
financial constraints due failing to meet the ‘Know your Customer’ (KYC) financial data Xiao's (2011) findings that financial skills are linked to increased savings and reduced debt.
requirements to verify customer identity (Elliott et al., 2022). Such studies have shown that Notably, our research has shed light on the relationship between financial skills and
inclusive credit scoring is not limited to demographic and economic variables, other variables confidence. While prior studies like Seaward and Kemp (2000) and Nosić and Weber (2010)
can be explored that increase the accuracy to predict the default nature of borrowers. highlighted the connection between overestimating future earnings and accumulating debt or
engaging in high-risk behavior, our findings underscore the pivotal role of financial skills in
This dissertation makes four contributions to the field of inclusive human-centered credit predicting payment behavior. Individuals with moderate or low financial skills combined with
decision-making, utilizing FinTech innovation to facilitate financial inclusion for vulnerable overconfidence are more likely to exhibit delinquent payment behavior, a crucial component
consumer segments, entrepreneurs, small businesses and their associated lenders. First, this with the most substantial impact in our logistic regression analysis (β- coefficient of 0.76).
dissertation is the first to develop a credit score model that connects financial literacy with
lifestyle and personality of the borrower in predicting a borrowers credit worthiness (Chapter Our study also aligns with earlier research by Davies and Lea (1995), Norvilitis et al. (2006),
4). This model can function as a paradigm for future human-centered AI risk scoring and Haultain et al. (2010), which observed a positive link between positive debt attitudes and
solutions. Secondly, while other research has focused on psychometric credit scoring in higher debt levels. Nevertheless, we identified a negative correlation between debt attitudes
developing countries for SMEs, this dissertation stands out as the first to utilize data from and the absence of savings when forecasting late payments. The interplay between various
highly regulated Western markets such as the USA and The Netherlands in Europe for model components within a comprehensive personality model, a unique aspect in behavioral
training (Chapter 4). Thirdly, this dissertation is the first to counterfactually test psychometric financial research, significantly contributes to the prediction of payment behavior. This
credit scoring models for small businesses and sole traders on real behavioral small business component, which we call ‘financial vulnerable optimism’ has a β-coefficient of 0.72 and
data in an European market (Czech Republic) (Chapter 5). Where prior studies have applied therefore stands as the second most influential factor. These findings pave the way for
small back-test experiments (e.g., use of traditional financial data sources (Klinger 2013)) for constructing financial personality profiles to distinguish between good and bad payers when
probability of default testing, we employ dynamic near real-time psychometric and financial extending loans, thus enhancing credit decision-making.
data from a CZ-based FinTech firm to not only assess the validity of the PSM for Additionally, we introduced social desirability as a control factor in our model, uncovering a
incorporation in both FinTech and mainstream credit scoring procedures for probability of relationship between the level of social desirability and expected payment behavior (β-
default testing, but also translate the results into profit impact. Fourth, this dissertation is the coefficient of 0.28). Our study is among the first to establish a predictive association between
first that counterfactually explores the predictiveness and stability of the psychometric credit social desirability and payment behavior. Furthermore, we found that age had a minimal
scoring model during a period of high stress (COVID-19 Pandemic: August 2019-February impact (β-coefficient of -0.01) on late payments. The logistic regression model achieved an
2022). accuracy rate of 70.7% and a Gini coefficient of 0.56. It demonstrates a slightly superior
ability to predict good payment behavior, underscoring its potential significance in credit
The objective of the study is to develop a psychometric model to explore the hypothesis that scoring for vulnerable and thin-file customer segments in Western credit markets.
financial personality-centric credit scoring could improve financial access for vulnerable Consequently, the model's predictive power substantiates financial inclusion efforts and
consumer segments in the USA and the Netherlands, especially relevant during times of mitigates information asymmetry.
market instability. This research fills a critical gap by emphasizing the significance of
financial personality factors in shaping payment behavior when traditional financial data is Thirdly, this dissertation is the first to counterfactually test psychometric credit scoring
scarce or outdated, as exemplified during crises like COVID-19 or high inflationary market models for small businesses and sole traders on real behavioral small business data in an
contexts. Our findings corroborate the core hypothesis and, also we apply novel financial European market (Czech Republic) (Chapter 6). At a granular level, this study represents the
literacy related attributes in our model, align with previous studies by Klinger et al. (2013) first to demonstrate that PSMs facilitate access to finance for both business segments—self-
and Hurley and Adebayo (2016), emphasizing the relevance of personality traits also in employed individuals and micro-organizations—especially during unstable market conditions
promoting financial inclusion of small businesses. (COVID-19 pandemic) where traditional credit data may be unreliable or unavailable and
financial exclusion is increasingly lurking. While previous research has explored the
Prior studies have primarily examined the influence of individual psychometric traits on application of psychometric scoring in low-income markets (Goel & Rastogi, 2023; Klinger,
financial behavior. However, this study stands out as a groundbreaking endeavor, employing 2013), we are, to the best of our knowledge, the first to illustrate its business impact in a
structural equation modeling to integrate personality attributes linked to financial literacy in high-income European market (Czech Republic). In the current macroeconomic environment,
volatile market conditions. The outcome is the creation of a comprehensive personality- as Europe teeters on the edge of a recession, lenders are closely scrutinizing the quality of
centric logistic regression model tailored for credit scoring in highly regulated markets. their investment portfolios while aiming to reach valuable yet underserved customer
segments. In line with existing literature, we find support for the application of psychometrics
Furthermore, our research uncovered new psychometric components such as "financial in credit scoring models, leading to enhancements in predictive accuracy (Goel & Rastogi,
accument" and "financial vulnerable optimism." 2023; Djeundje et al., 2021; Liberati & Camillo, 2018; Dlogish et al., 2017; Klinger, 2013).
Our study contributes to the existing literature by focusing on the relationship between
Despite these novel findings, our results remain consistent with Lussardi & Mitchell’s (2011) psychometric attributes and late payment of debt and arrears, whereas previous research
assertion that financial knowledge plays a substantial role in financial inclusion, as primarily examined the connection between these attributes and overall debt levels. Likewise,
hypothesized in our conceptual model. Nonetheless, our study opted for the use of financial when considering accuracy metrics (Yang & Berdine, 2017; Shisterman et al., 2005; Altman
202 220037

Chapter 7
& Bland, 1994), our research, conducted through live and automated application design, we in widespread AI implementation. Additionally, research should delve into the integration of
find support for applying psychometrics for credit scoring. explainable AI directly into customer interfaces, examining how clear explanations enhance
Therefore, the PSM has the potential to support informed and responsible lending practices, user understanding and trust in smart banking applications.
enabling profitable and sustainable growth strategies, particularly during current and future
periods of instability. 7.6.1. Deepening relevance in human-centered alternative data
In this dissertation, the exploration of the impact of lifestyles, attitudes, and behaviors,
7.5 Limitations & suggestions for further research measured through psychometric data, prompts the suggestion for further research. One
avenue involves investigating methods to attract this data from real-time sources.
7.5.1. Limitations Additionally, there is a recommendation to explore the integration of (real-time) alternative
Below the key-limitations of this study are addressed. The study provides valuable insights data sources, including open banking, social, behavioral, or environmental data, into AI
into inclusive Banking 5.0 and human-centric AI applications in the financial industry. models for more inclusive financial advice, credit scoring, and risk assessment. Such an
However, it's essential to acknowledge that research, including the summarized studies, is not exploration should encompass an assessment of the effectiveness and ethical implications tied
without limitations. Several common limitations are associated with this body of work. to the incorporation of diverse data sets. Furthermore, delving into the principles of
Firstly, sample size and generalizability could be impacted, especially in studies using data behavioral economics within the context of smart banking is encouraged to comprehend how
from specific financial institutions or regions, potentially limiting broader global behavioral factors shape decision-making, financial habits, and responses to AI-driven
applicability. Secondly, temporal constraints pose a challenge, considering the rapid evolution interventions. A valuable area for study involves examining the impact of major economic
of financial landscapes, technology, and consumer behaviors. Thirdly, data quality and events, such as recessions or financial crises, on the effectiveness of human-centered AI
availability may also be limiting factors, with reliance on historical data and challenges in models in credit risk assessment for financial inclusion. This includes assessing the
accessing comprehensive psychometric or behavioral data. Fourthly, the interpretability of AI adaptability of AI systems to dynamic economic conditions. In summary, additional research
algorithms, ethical and privacy concerns in handling personal data, and the variability in is suggested to further enrich the customer profile for easily accessible, real-time,
regulatory landscapes across regions add further layers of complexity. Studies may establish personalized solutions.
correlations without definitively demonstrating causation, and biases in data used to train AI
models could perpetuate inequities. Furthermore, dynamic economic conditions, varying 7.6.2. Strategic impact of human-centered approaches
technology adoption rates, and a lack of long-term behavioral data present additional Delving into the factors that influence user trust in AI-driven financial services is a critical
challenges. Recognizing these limitations is crucial for practitioners and researchers when research avenue. Understanding how users perceive and place trust in AI recommendations is
interpreting and applying study findings. Future research endeavors should strive to address pivotal for fostering successful adoption and ensuring sustained engagement. Another
these limitations, providing more comprehensive insights into the evolving landscape of essential area for exploration involves designing AI-driven financial services with inclusivity
smart banking and AI in finance. in mind, specifically targeting accessibility for vulnerable groups. Research efforts should be
directed towards ensuring that AI applications contribute to reducing, rather than
7.5.2. Suggestions for further research exacerbating, existing financial disparities. Additionally, there is a need to explore effective
In this section, I offer research suggestions aimed at enhancing our comprehension of human- strategies for educating customers about the use of AI in banking and financial services. This
centric AI in inclusive Banking 5.0. Four recommendations for advancing research in smart includes assessing how heightened awareness influences customer perceptions, trust, and
Banking 5.0 include exploring human-centered AI through diverse lenses; delving into wider acceptance of AI-driven solutions. Lastly, investigating the challenges and opportunities tied
alternative data research with a human-centered focus; investigating the strategic impact of to regulatory compliance in the realm of AI applications in finance is crucial. This research
human-centric approaches; and expanding cross-cultural research in the context of inclusive should focus on understanding how regulatory frameworks can adapt to accommodate
Banking 5.0. innovative AI-driven practices, ensuring a harmonious integration of technology and
compliance standards.
7.6 Exploring human-centered AI through diverse lenses.
To gain a comprehensive understanding of human-centered AI in inclusive holistic banking, 7.5.3. Cross cultural research
researchers can explore various avenues. Conducting longitudinal studies is crucial for This dissertation draws upon a substantial volume of data gathered from the USA, the United
assessing the sustained impact of AI implementations in banking over an extended period, Kingdom, the Netherlands, and the Czech Republic, all representing Western markets. While
offering insights into long-term effectiveness, challenges, and evolution. Tailoring ethical AI these countries have diverse customer segments to be considered for financial inclusion, it's
frameworks specifically for the financial industry is essential, focusing on transparency, imperative to recognize that significant benefits from financial inclusion are anticipated in
fairness, and accountability while addressing biases and aligning with evolving ethical developing countries. To enrich the understanding of smart banking and AI applications, there
standards. Efforts should also be directed toward developing tools and methodologies that is a clear recommendation to expand research to encompass a more diverse set of regions and
enhance the interpretability and explainability of AI models, particularly for complex models cultural contexts. Analyzing the impact of these technologies in different cultural settings can
like neural networks, ensuring transparency for stakeholders. Exploring collaboration models unveil unique challenges, preferences, and adoption patterns, contributing to a more
between humans and AI in the financial advisory space is promising, optimizing the synergy comprehensive and globally relevant understanding of the subject matter.
for more effective customer interactions. Investigating the robustness of AI models against
adversarial attacks and intentional manipulations is imperative to assess security implications
220084 205

Conclusion
in widespread AI implementation. Additionally, research should delve into the integration of
explainable AI directly into customer interfaces, examining how clear explanations enhance
user understanding and trust in smart banking applications.
7.6.1. Deepening relevance in human-centered alternative data
In this dissertation, the exploration of the impact of lifestyles, attitudes, and behaviors,
measured through psychometric data, prompts the suggestion for further research. One
avenue involves investigating methods to attract this data from real-time sources.
Additionally, there is a recommendation to explore the integration of (real-time) alternative
data sources, including open banking, social, behavioral, or environmental data, into AI
models for more inclusive financial advice, credit scoring, and risk assessment. Such an
exploration should encompass an assessment of the effectiveness and ethical implications tied
to the incorporation of diverse data sets. Furthermore, delving into the principles of
behavioral economics within the context of smart banking is encouraged to comprehend how
behavioral factors shape decision-making, financial habits, and responses to AI-driven
interventions. A valuable area for study involves examining the impact of major economic
events, such as recessions or financial crises, on the effectiveness of human-centered AI
models in credit risk assessment for financial inclusion. This includes assessing the
adaptability of AI systems to dynamic economic conditions. In summary, additional research
is suggested to further enrich the customer profile for easily accessible, real-time,
personalized solutions.
7.6.2. Strategic impact of human-centered approaches
Delving into the factors that influence user trust in AI-driven financial services is a critical
research avenue. Understanding how users perceive and place trust in AI recommendations is
pivotal for fostering successful adoption and ensuring sustained engagement. Another
essential area for exploration involves designing AI-driven financial services with inclusivity
in mind, specifically targeting accessibility for vulnerable groups. Research efforts should be
directed towards ensuring that AI applications contribute to reducing, rather than
exacerbating, existing financial disparities. Additionally, there is a need to explore effective
strategies for educating customers about the use of AI in banking and financial services. This
includes assessing how heightened awareness influences customer perceptions, trust, and
acceptance of AI-driven solutions. Lastly, investigating the challenges and opportunities tied
to regulatory compliance in the realm of AI applications in finance is crucial. This research
should focus on understanding how regulatory frameworks can adapt to accommodate
innovative AI-driven practices, ensuring a harmonious integration of technology and
compliance standards.
7.5.3. Cross cultural research
This dissertation draws upon a substantial volume of data gathered from the USA, the United
Kingdom, the Netherlands, and the Czech Republic, all representing Western markets. While
these countries have diverse customer segments to be considered for financial inclusion, it's
imperative to recognize that significant benefits from financial inclusion are anticipated in
developing countries. To enrich the understanding of smart banking and AI applications, there
is a clear recommendation to expand research to encompass a more diverse set of regions and
cultural contexts. Analyzing the impact of these technologies in different cultural settings can
unveil unique challenges, preferences, and adoption patterns, contributing to a more
comprehensive and globally relevant understanding of the subject matter.
220059

Chapter 7
By pursuing these research directions, scholars and practitioners can contribute to a deeper
understanding of the evolving landscape of smart banking, AI applications in finance, and the
human-centered aspects of these technologies. This research can inform the development of
more effective, transparent, and ethically sound practices in the financial industry.
7.7 Value for practioners
Having discussed the theoretical contributions and limitations of our study, we now shift our
focus to the practical implications. This section will outline how financial institutions can
apply our findings to improve customer experiences and credit assessments. They have
significant implications for practitioners in the financial industry by providing insights into
optimizing digital financial advice systems for enhanced inclusive holistic customer
experiences, differentiation, regulatory alignment, global expansion, and ongoing innovation.
The DCX model serves as a valuable tool for shaping micro-personalization strategies that
drive value creation and customer engagement. Recognizing the importance of experiential
system aspects in customer experience, practitioners can focus on creating value through
gamification, user-friendly interfaces, personalized recommendations, offering ratings and
reviews and seamless interactions. The DCX model provides an opportunity for financial
institutions to differentiate themselves based on the tailored customer experience they offer.
The model emphasizes the importance of both objective and subjective aspects of the
customer experience and therefore supports a human-centric customer approach in the design
and delivery of digital-driven financial advice. Lastly, recognizing the importance of
experiential subjective system aspects, practitioners may need to invest in training and
development for staff involved in customer interactions or the automation of them.
The study (chapter 3) proposes the development of the world's first psychometric market
segmentation model for digital financial advice robots and assistants that has several
implications for practitioners in the financial industry. The study's implications suggest
opportunities for practitioners to enhance personalization, education, activation, and
engagement in financial services, ultimately contributing to the goal of including underserved
populations and supporting inexperienced individuals like generation Z and millennials in
securing their financial future.
Potential consequences and implications for advisors, banks, NGO’s, governments and other
stakeholders are described below. Firstly, practitioners can use the psychometric
segmentation model to tailor financial advice and services based on customers' psychometric
factors, such as convenience preferences, financial literacy levels, and personality traits and
biases. Secondly, recognizing the psychometric factor of "financial illiteracy" practioners can
target customer education efforts. Advisors and banks can create automated educational
programs, alerts, campaigns and materials that address the specific financial literacy and
financial wellness challenges identified within each customer segment. This can help bridge
the knowledge gap, increase the adaptation of the educational content and predicitve and
prescriptive alerts to empower customers to make more informed financial decisions. Thirdly,
understanding the psychometric factors, including preferences for convenience and
personality traits, can inform personalized strategies for customer activation and engagement.
This is especially relevant for young customer segments and financially fragile customer
segments. The study suggests potential insights into including underserved populations,
addressing their unique psychometric characteristics. This could involve simplifying
processes, reducing barriers, and providing education targeted at the identified psychometric
factors. But also creating automated mentorship programs, educational resources, and
221006

Conclusion
financial planning tools specifically designed for millennials. Consider integrating behavioral
finance principles to address the identified psychometric factors, such as "financial illiteracy"
and "rigid personality." Lastly, practitioners should consider ethical implications related to
psychometric profiling, ensuring that customer data is handled responsibly and transparently.
Chapter 4 analyzes individuals' financial personality for inclusive credit scoring in the
context of global uncertainty, high inflation, and rising interest rates. This research has
several potential impacts for practitioners in the financial industry. It offers practitioners
valuable insights into enhancing their traditional credit scorecards by integrating
psychometric scorecards for inclusive credit scoring, especially in challenging economic
environments.The identified personality factors offer a nuanced approach to credit
assessment, opening avenues for tailored financial products, initiatives to enhance financial
inclusion for vulnerable consumer segments and drive financial wellness for the next
generations.
The use of psychometric scoring models (PSMs) can enhance credit assessment for
vulnerable consumer groups with limited credit histories, such as young adults, senior
citizens, start-up entrepreneurs, sole traders, single parents, and migrants. Financial
institutions can consider integrating PSMs into their credit scoring models to provide a more
holistic and nuanced evaluation of individuals' creditworthiness. Understanding factors such
as financial capability, materialistic tendencies, impulsive buying behavior, social desirability,
and attitudes towards debt also allows for the development and governmental oversight of
more tailored financial products. Practitioners can design financial products that align with
the identified psychometric factors, addressing the unique needs and behaviors of vulnerable
customer segments. By identifying specific personality factors associated with late payments,
financial institutions can better assess and mitigate credit risks. Practitioners can use this
insight to adapt their credit risk management strategies, particularly during periods of
economic volatility. This may involve dynamic adjustments to credit scoring models based on
changing economic conditions that could facilitate the implementation of risk management
strategies that account for the psychometric factors identified in the research. This again
could involve adjusting interest rates, setting credit limits, or providing additional financial
education to high-risk individuals. Understanding the factors influencing late payments, such
as financial capability and impulsive buying behavior, also highlights opportunities for
targeted customer education and support. Governments, NGO’s and financial institutions can
develop educational programs and resources that address the identified psychometric factors,
helping customers build financial capability and make informed decisions that support
financial wellness. Moreover, financial institutions can contribute to social responsibility by
using PSMs to promote financial inclusion for vulnerable groups. Financial institutions and
policymakers can use this research to inform and support initiatives aimed at fostering
financial inclusion and financial wellness. This may involve creating awareness, providing
targeted financial education, and offering accessible credit options. The use of psychometric
scoring models introduces ethical and regulatory considerations related to privacy and
fairness. Practitioners must adhere to ethical standards and regulatory guidelines when
implementing PSMs. This includes ensuring transparency in data usage, obtaining informed
consent, and preventing discriminatory practices.
With the breakthrough of large language models, AI is seen as a pivotal area in any business.
Most transformative AI applications in banking currently are seen in marketing & sales,
customer operations, risk & legal and software engineering (Mc Kinsey, 2023). The research
in chapter 5 therefore provides a compelling case for the adoption of AI in credit risk
220171

Chapter 7
assessments, offering practitioners the opportunity to enhance decision-making processes, borrowers. The evidence supporting PSM as a tool for financial inclusion offers potential for
adapt to digital lending trends, and contribute to the stability of the global financial system. scaling similar initiatives in other regions or markets. Practitioners can explore opportunities
The findings encourage financial institutions to embrace AI as a transformative tool for to replicate the success of PSM in other contexts, contributing to broader efforts to provide
enhanced inclusive credit risk scoring in the Banking 5.0 context. The research demonstrates inclusive financial services globally.The success of PSM raises regulatory considerations
that AI models, particularly neural nets and random forests, outperform traditional logistic related to responsible lending and consumer protection. Practitioners must ensure that the use
PD-models in credit risk assessment. Financial institutions can consider integrating AI-driven of PSM aligns with regulatory requirements, emphasizing transparency, fairness, and ethical
credit risk models to enhance the accuracy and efficiency of credit risk assessment processes. use of customer data.
This could lead to more informed lending decisions and improved portfolio management. As
digital lending is expected to grow at a CAGR of 26.9% until 2030, the research supports the In summary, the inclusion of psychometric-oriented research adds a layer of individualized
idea that AI can form the central pillar for the continuity of financial institutions in the digital understanding of behavioral root-causes to the broader impact of AI in inclusive human-
era. Practitioners in digital lending can leverage AI to streamline decision-making processes. centric digital banking. It emphasizes the importance of holistic customer-centric micro-
This involves adopting scalable and automated credit risk solutions based on AI to cater to strategies, ethical considerations, and resilience in adapting to the unique needs of customers
the evolving expectations of consumers, especially millennials. Practitioners need to adapt to in a rapidly evolving financial landscape. Practitioners are encouraged to blend psychometric
changing consumer expectations by embracing digital lending platforms and incorporating AI insights with AI capabilities for a more empathetic and effective approach to inclusive
in credit risk assessment. This ensures that financial institutions remain competitive and Banking 5.0. Its impact is presented in table 3 below.
relevant to the preferences of the modern consumer. Financial institutions can use AI as a tool
for effective risk mitigation, potentially reducing the likelihood of financial crises. This Table 3
supports the overall stability and resilience of the financial system. On this, AI-driven credit
risk models should be considered as a fundamental component of strategic planning. Impact of psychometrics on banking evolution
Institutions can invest in building robust AI-based solutions to navigate the challenges posed
by market uncertainties and evolving consumer behaviors. Moreover, the research highlights
Banking 1.0 Banking 2.0 Banking 3.0 Banking 4.0 Banking 5.0
the scalability of automated credit risk solutions built on AI. Financial institutions can invest Timeframe
(1760 –1840) (1870 –1969) (1970 -2000) (2000 -2030) (2030 -->)
in scalable and automated systems that leverage AI for credit risk scoring. This not only
enhances efficiency but also positions institutions to handle the increasing volume of credit
Technology Mechanization Mass production Automation Digitization Human-centered
decisions. The adoption of AI in credit risk scoring can be a differentiator for financial
institutions. Financial institutions can use their adoption of AI as a marketing advantage, • Banks begin tocollect • Collection of more • Dynamic&psychometric
more structureddata, extensivebehavioral data becomesfully
positioning themselves as leaders in leveraging cutting-edge technology for more accurate • In theearlystages of includingcustomer (transactions) & integratedintofinancial
banking, financial demographicsand psychometricdata advisoryandrisk
and reliable credit risk assessment. adviceandrisk transaction history. throughonline management processes.
management Basic risk assessment interactionsanddigital • Psychometricdata is also
primarilyrelyon modelsstart to platforms. usedtofosterdeeper
manual processesand incorporate • Advanced analytics connectionswith
Chapter 6, finally, researches the adoption of a financial literacy-based psychometric credit basic financial metrics. rudimentarybehavioral techniquesderive customersandprovide
s to c o f r in ec a a n r c d e s , f d o e r f a s u m lt a l r l a t b e u s s , i a n n e d ss r e e s s i i l n i e v n o c l e a t d il u e r i m ng a r i k n e s t t a c b o i n li d t i y t i p o o n s s i . t i T o h n e s p P o S s M iti v a e s i a m v p a a lu c a t b o l n e a to cc o e l s f s o r B P Fi s e n y h a c a n h v c o i e o m r e al tric s c P b y o s e s y l h l t c e a e h c v m o t i e o m a d r t a e ic o l t a r r d l i u l a c y t t & a il i i z s e n d o . t • f O & c a o b c b n s t e t o e r h r r ib s v a . e u v d i t o e p ra t s o l y b c m h ia o o s r m e e s e tric • d i E p n n e e s h e r ig s p a o h n e n t c r s a e . b l d i e za h t a i v o i n or o a f l • h s P H o r o A e l l u I i d - s t d t i i c i o r c t i n v i f v s e i e n . n a & f n i n c p i a r a e n l v c w e ia e n l l t l a n t e i s v s e
practitioners seeking to enhance financial inclusion and support small businesses in dynamic Management • Limited applicationof refinedrisk financial adviceand adviceandrisk
psychometrics. assessment, enabling risk management management solutions
economic environments. The research finds that PSM significantly improves access to However, basic bankstobetter strategies. andapps.
customer profiling understandcustomer • Responsiverisk • Micro-personalization
finance for small businesses, with a higher approval rate. Financial institutions and fintech mayinformsome behaviorandtailor management & recommendationsthat
decision-making product offerings advice: Digital alignwithcustomer
lenders can consider integrating PSM into their credit assessment processes to broaden processes. accordingly. platforms enablereal- values, lifestyles,
• Data collected time monitoring and attitudes andgoals
financial inclusion for the underserved sector, facilitating easier access to funds for sole automatically adaptationof leadingtobetterfinancial
strategies, decisionsandincreased
traders and micro-organizations. Moreover, recognizing the resilience of PSM specifically satisfaction.
during market uncertainties, practitioners can rely on this model to maintain or even increase
lending activities during economic downturns, contributing to overall economic stability. Collectively, these studies paint a comprehensive picture of the benefits arising from the
Financial institutions and fintech lenders can use PSM as a unique selling proposition, marriage of psychometric data and AI in credit risk management within a human-centric
positioning themselves as leaders in inclusive finance and responsible lending practices. Banking 5.0 framework, which are:
Fintech companies can leverage the findings to further innovate and develop inclusive
financial products and services, potentially serving as a model for other markets facing 1. Micro-Personalized Financial Advice: Through the integration of psychometric data
similar challenges. Also, the observed lower default rate with PSM indicates a potential and AI, financial advisors can offer personalized recommendations tailored to
improvement in risk assessment. Practitioners can use PSM as a tool to refine risk individual customers' financial goals, risk tolerance, and preferences. Research has
management strategies, potentially leading to reduced default rates and better overall shown that incorporating psychometric insights into digital advisory processes
portfolio performance. Furthermore, they can complement lending activities with targeted enhances the relevance and effectiveness of financial advice, leading to better
financial education programs that address the specific needs and challenges of sole traders outcomes for customers. By analyzing customers' behavioral patterns and personality
and micro-organizations. This could lead to more informed financial decision-making among traits, advisors can offer targeted guidance that resonates with their specific needs and
221028 209

Conclusion
assessments, offering practitioners the opportunity to enhance decision-making processes, borrowers. The evidence supporting PSM as a tool for financial inclusion offers potential for
adapt to digital lending trends, and contribute to the stability of the global financial system. scaling similar initiatives in other regions or markets. Practitioners can explore opportunities
The findings encourage financial institutions to embrace AI as a transformative tool for to replicate the success of PSM in other contexts, contributing to broader efforts to provide
enhanced inclusive credit risk scoring in the Banking 5.0 context. The research demonstrates inclusive financial services globally.The success of PSM raises regulatory considerations
that AI models, particularly neural nets and random forests, outperform traditional logistic related to responsible lending and consumer protection. Practitioners must ensure that the use
PD-models in credit risk assessment. Financial institutions can consider integrating AI-driven of PSM aligns with regulatory requirements, emphasizing transparency, fairness, and ethical
credit risk models to enhance the accuracy and efficiency of credit risk assessment processes. use of customer data.
This could lead to more informed lending decisions and improved portfolio management. As
digital lending is expected to grow at a CAGR of 26.9% until 2030, the research supports the In summary, the inclusion of psychometric-oriented research adds a layer of individualized
idea that AI can form the central pillar for the continuity of financial institutions in the digital understanding of behavioral root-causes to the broader impact of AI in inclusive human-
era. Practitioners in digital lending can leverage AI to streamline decision-making processes. centric digital banking. It emphasizes the importance of holistic customer-centric micro-
This involves adopting scalable and automated credit risk solutions based on AI to cater to strategies, ethical considerations, and resilience in adapting to the unique needs of customers
the evolving expectations of consumers, especially millennials. Practitioners need to adapt to in a rapidly evolving financial landscape. Practitioners are encouraged to blend psychometric
changing consumer expectations by embracing digital lending platforms and incorporating AI insights with AI capabilities for a more empathetic and effective approach to inclusive
in credit risk assessment. This ensures that financial institutions remain competitive and Banking 5.0. Its impact is presented in table 3 below.
relevant to the preferences of the modern consumer. Financial institutions can use AI as a tool
for effective risk mitigation, potentially reducing the likelihood of financial crises. This Table 3
supports the overall stability and resilience of the financial system. On this, AI-driven credit
risk models should be considered as a fundamental component of strategic planning. Impact of psychometrics on banking evolution
Institutions can invest in building robust AI-based solutions to navigate the challenges posed
by market uncertainties and evolving consumer behaviors. Moreover, the research highlights
Banking 1.0 Banking 2.0 Banking 3.0 Banking 4.0 Banking 5.0
the scalability of automated credit risk solutions built on AI. Financial institutions can invest Timeframe
(1760 –1840) (1870 –1969) (1970 -2000) (2000 -2030) (2030 -->)
in scalable and automated systems that leverage AI for credit risk scoring. This not only
enhances efficiency but also positions institutions to handle the increasing volume of credit
Technology Mechanization Mass production Automation Digitization Human-centered
decisions. The adoption of AI in credit risk scoring can be a differentiator for financial
institutions. Financial institutions can use their adoption of AI as a marketing advantage, • Banks begin tocollect • Collection of more • Dynamic&psychometric
more structureddata, extensivebehavioral data becomesfully
positioning themselves as leaders in leveraging cutting-edge technology for more accurate • In theearlystages of includingcustomer (transactions) & integratedintofinancial
banking, financial demographicsand psychometricdata advisoryandrisk
and reliable credit risk assessment. adviceandrisk transaction history. throughonline management processes.
management Basic risk assessment interactionsanddigital • Psychometricdata is also
primarilyrelyon modelsstart to platforms. usedtofosterdeeper
manual processesand incorporate • Advanced analytics connectionswith
Chapter 6, finally, researches the adoption of a financial literacy-based psychometric credit basic financial metrics. rudimentarybehavioral techniquesderive customersandprovide
s to c o f r in ec a a n r c d e s , f d o e r f a s u m lt a l r l a t b e u s s , i a n n e d ss r e e s s i i l n i e v n o c l e a t d il u e r i m ng a r i k n e s t t a c b o i n li d t i y t i p o o n s s i . t i T o h n e s p P o S s M iti v a e s i a m v p a a lu c a t b o l n e a to cc o e l s f s o r B P Fi s e n y h a c a n h v c o i e o m r e al tric s c P b y o s e s y l h l t c e a e h c v m o t i e o m a d r t a e ic o l t a r r d l i u l a c y t t & a il i i z s e n d o . t • f O & c a o b c b n s t e t o e r h r r ib s v a . e u v d i t o e p ra t s o l y b c m h ia o o s r m e e s e tric • d i E p n n e e s h e r ig s p a o h n e n t c r s a e . b l d i e za h t a i v o i n or o a f l • h s P H o r o A e l l u I i d - s t d t i i c i o r c t i n v i f v s e i e n . n a & f n i n c p i a r a e n l v c w e ia e n l l t l a n t e i s v s e
practitioners seeking to enhance financial inclusion and support small businesses in dynamic Management • Limited applicationof refinedrisk financial adviceand adviceandrisk
psychometrics. assessment, enabling risk management management solutions
economic environments. The research finds that PSM significantly improves access to However, basic bankstobetter strategies. andapps.
customer profiling understandcustomer • Responsiverisk • Micro-personalization
finance for small businesses, with a higher approval rate. Financial institutions and fintech mayinformsome behaviorandtailor management & recommendationsthat
decision-making product offerings advice: Digital alignwithcustomer
lenders can consider integrating PSM into their credit assessment processes to broaden processes. accordingly. platforms enablereal- values, lifestyles,
• Data collected time monitoring and attitudes andgoals
financial inclusion for the underserved sector, facilitating easier access to funds for sole automatically adaptationof leadingtobetterfinancial
strategies, decisionsandincreased
traders and micro-organizations. Moreover, recognizing the resilience of PSM specifically satisfaction.
during market uncertainties, practitioners can rely on this model to maintain or even increase
lending activities during economic downturns, contributing to overall economic stability. Collectively, these studies paint a comprehensive picture of the benefits arising from the
Financial institutions and fintech lenders can use PSM as a unique selling proposition, marriage of psychometric data and AI in credit risk management within a human-centric
positioning themselves as leaders in inclusive finance and responsible lending practices. Banking 5.0 framework, which are:
Fintech companies can leverage the findings to further innovate and develop inclusive
financial products and services, potentially serving as a model for other markets facing 1. Micro-Personalized Financial Advice: Through the integration of psychometric data
similar challenges. Also, the observed lower default rate with PSM indicates a potential and AI, financial advisors can offer personalized recommendations tailored to
improvement in risk assessment. Practitioners can use PSM as a tool to refine risk individual customers' financial goals, risk tolerance, and preferences. Research has
management strategies, potentially leading to reduced default rates and better overall shown that incorporating psychometric insights into digital advisory processes
portfolio performance. Furthermore, they can complement lending activities with targeted enhances the relevance and effectiveness of financial advice, leading to better
financial education programs that address the specific needs and challenges of sole traders outcomes for customers. By analyzing customers' behavioral patterns and personality
and micro-organizations. This could lead to more informed financial decision-making among traits, advisors can offer targeted guidance that resonates with their specific needs and
208 220193

Chapter 7
circumstances, ultimately empowering them to make more informed financial
decisions.
2. Enhanced Financial Inclusion: Psychometric credit scoring models, whether based
on financial literacy or personality traits, demonstrate a remarkable capacity to
enhance financial inclusion. By leveraging dynamic psychometric insights, these
models bridge the gap for underserved micro-organizations, sole traders, and
vulnerable consumer segments during market uncertainties. Research findings
indicate that incorporating psychometric data into credit scoring processes enables
lenders to assess the creditworthiness of individuals who may have limited or no
traditional credit history, thereby expanding access to financial products and services
for previously marginalized populations.
3. Improved Decision-Making: The integration of psychometric data and AI algorithms
into credit scoring models enhances lenders' ability to make more accurate and
reliable credit decisions. By analyzing a broader range of behavioral and psychosocial
factors, lenders gain deeper insights into borrowers' credit risk profiles, enabling them
to assess risk more effectively and tailor lending decisions accordingly. Research
suggests that AI-powered credit scoring models outperform traditional approaches in
terms of predictive accuracy and risk assessment, leading to improved decision-
making processes and reduced default rates for lenders. Additionally, the automation
of credit decisions through AI streamlines the lending process, enabling faster loan
approvals and greater operational efficiency.
4. Reduced Default Rates: By leveraging psychometrics and AI for credit scoring,
lenders can identify high-risk borrowers more effectively and mitigate potential losses
by offering tailored products or adjusting lending terms to better match borrowers'
risk profiles. This helps reduce default rates and minimize credit losses for lenders.
5. Operational Efficiency: AI-powered credit scoring models streamline the lending
process by automating credit decisions, making them scalable across asset classes and
geographies and reducing the time and resources required for manual underwriting.
This improves operational efficiency for lenders and enables faster loan approvals,
enhancing the overall customer experience.
6. Expanded Customer Base: By leveraging psychometric data and AI to assess credit
risk more accurately, lenders can expand their customer base to include previously
underserved segments of the population, such as young adults or individuals with thin
credit files. This enables lenders to tap into new market opportunities and grow their
loan portfolios while maintaining prudent risk management practices.
The synthesis of these research findings heralds a new era in inclusive banking, where the
marriage of psychometric data and AI not only refines predictive capabilities but also
transforms the industry into a more inclusive, precise, and ethically aligned ecosystem. As
Banking 5.0 unfolds, the path forward involves not just embracing technological
advancements but intertwining them with a deep understanding of human behavior, ensuring
that the benefits of innovation are harnessed responsibly and inclusively for the betterment of
the financial ecosystem.
221140

Conclusion
7.8 Valorisation for next gen inclusive Banking 5.0 business models
The research presented in this dissertation holds profound implications for the evolution of
next-generation inclusive Banking 5.0 business models. From sustainable and impact banking
to personalized financial wellness solutions, the integration of cutting-edge technologies like
(gen) AI and dynamic data heralds a new era of digital banking engagement. In table 3 the
banking evolution from profit focused to sustainability focused is presented. The other
development is the evolution of decision making which is presented in Figure 1.
Figure 1
Development from traditional to advanced decision making
Degree of
Decision intelligence
+
Dynamic optimization Banking 5.0
Forecasts
Predictive analyses
Banking
Statistical analyses
4.0
Alerts
Selective drill downs
Banking
Ad hoc queries Depth of
1.0 –3.0
Standard Report Customer Knowledge
+
-
Application Customer Open Banking Search Device E-mail Gadget
Data Data Data Data Data Data Data
Psychometric & Behavioral Biases
3
Translating this into a banking transformation framework, the Y-axis differentiates between
business models that use traditional data and decision-making techniques and those that
incorporate machine learning, AI, as well as dynamic behavioral and psychometric data.
Translating the banking evolution to a banking transformation framework, the X-axis
differentiates between business models that focus solely on profit and those that balance
profit, essential for sustainability, with inclusiveness and positive impact on the world.
In the banking transformation framwork this evolution is crossed with the evolution of
banking towards holistic Banking 5.0. The banking transformation framework is presented in
figure 2.
221115

Chapter 7
Figure 2
Banking Transformation Framework
Advanced Decision Making
Banking 5.0
Banking 4.0
Intelligent Personalization
Digital Transformation
& Impact
Profit-centric focus Sustainability focus
Banking 3.5
Banking 3.0
Early digital &
Early Digital Adoption
Impact Adoption
Traditional Decision Making
At the forefront of this transformation are new business models like AI-driven super apps and
financial virtual guardian angels. Figure 3 presents some examples of business model
transformation strategies across the banking transformation framework.
Figure 3
Business Model Transformation Strategies Towards Banking 5.0
Advanced Decision Making
Robo advisors Digital Guardian Angels
Digital assistants Super apps
Embedded finance Sustainable embedded
Digital-only banks finance
Meta-verse banking
Banking 4.0 Banking 5.0
Profit-centric focus Sustainability focus
Banking 3.0 Banking 3.5
Traditional banks Impact investors
Community banking
Brokers
Micro-credit
Traditional Decision Making 5
221162

Conclusion
Figure 2
With an estimated four billion individuals globally poised to benefit from this paradigm shift,
Banking Transformation Framework these Banking 5.0 business models are set to revolutionize the landscape of financial advice
and decision-making. By harnessing insights from psychometric segmentation and AI-driven
credit analysis, these business models are profitable by providing inclusive, micro-
Advanced Decision Making
personalized financial guidance tailored to individual needs, behaviors, and creditworthiness,
while also striving for a positive impact on the world.They enhance user experience through
intuitive interfaces and inclusive financial services, bridging the gap for underserved
Banking 5.0
Banking 4.0 populations and fostering financial wellness. Ethical AI integration ensures compliance with
Intelligent Personalization
Digital Transformation & Impact regulations and builds trust, while strategic partnerships drive continuous innovation and
expansion. In summary, the rise of Banking 5.0 business models marks a pivotal moment in
the journey of banking evolution, shaping a future where everyone has access to
personalized, ethical, and empowering financial solutions.
Profit-centric focus Sustainability focus
In conclusion, the implications of the dissertation's findings reverberate far beyond the realm
of Banking 5.0, extending to the forefront of financial innovation, including the emergence of
Banking 3.5
Banking 3.0 super apps, sustainable embedded finance and virtual financial guardian angels. By laying the
Early digital &
Early Digital Adoption groundwork for heightened personalization, enriched user experiences, and inclusive
Impact Adoption
financial services, this research provides invaluable guidance for catering to diverse
preferences and seamlessly integrating ethical AI. Aligned with the principles of Banking 5.0,
these platforms are poised to leverage our insights to forge more resilient, customer-centric
Traditional Decision Making solutions and a positive impact on the world within the ever-evolving landscape of digital
financial services. Let us embark on this journey with renewed vigor, driven by the promise
of a more inclusive and holistic financial future for all.
At the forefront of this transformation are new business models like AI-driven super apps and
Like Ikea’s founder Ingvar Kamprad rightfully said:
financial virtual guardian angels. Figure 3 presents some examples of business model
transformation strategies across the banking transformation framework.
“ a lot of things remain to be done, but what a glorious future!”
Figure 3
Business Model Transformation Strategies Towards Banking 5.0
Advanced Decision Making
Robo advisors Digital Guardian Angels
Digital assistants Super apps
Embedded finance Sustainable embedded
Digital-only banks finance
Meta-verse banking
Banking 4.0 Banking 5.0
Profit-centric focus
Banking 3.0 Banking 3.5
Sustainability focus
Traditional banks Impact investors
Community banking
Brokers
Micro-credit
Traditional Decision Making 5
212 221137

Chapter 7
References
Abu Daqar, M. A., Arqawi, S., & Abu Karsh, S. (2021). Fintech in the eyes of Millennials and
Generation Z (the financial behavior and Fintech perception).
Achim, M. V., Borlea, S. N., & Văidean, V. L. (2021). Does technology matter for combating
economic and financial crime? A panel data study. Technological and Economic Development
of Economy, 27(1), 223-261.
Agarwal, P., & Alam, M. (2020). A lightweight deep learning model for human activity
recognition on edge devices. Procedia Computer Science, 167, 2364-2373.
Al-Dmour, R., Dawood, E. A. H., Al-Dmour, H., & Masa'deh, R. E. (2020). The effect of
customer lifestyle patterns on the use of mobile banking applications in Jordan. International
Journal of Electronic Marketing and Retailing, 11(3), 239-258.
Alyousif, M., & Kalenkoski, C. M. (2017). Who seeks financial advice?. Available at SSRN
2943159.
Alhosani, F. A., & Tariq, M. U. (2020). Improving Service quality of smart banking using
quality management methods in UAE. International Journal of Mechanical Production
Engineering Research and Development (IJMPERD), 10(3), 2249-8001.
Allen, F., Demirguc-Kunt, A., Klapper, L., & Peria, M. S. M. (2016). The foundations of
financial inclusion: Understanding ownership and use of formal accounts. Journal of
Financial Intermediation, 27, 1-30.
Altman, D. G., & Bland, J. M. (1994). Diagnostic tests 3: receiver operating characteristic
plots. BMJ: British Medical Journal, 309(6948), 188.
Azma, N., Rahman, M., Adeyemi, A. A., & Rahman, M. K. (2019). Propensity toward
indebtedness: Evidence from Malaysia. Review of Behavioral Finance.
Biesenbach & Gundmunsson, 2019. Robo-advisory: Assessing the threat, and how banks
should respond in a time of increased transparency requirements. Simon-Kucher and partners.
https://internationalbanker.com/banking/robo-advisory-assessing-threat-banks-respond-time-
increased-transparency-requirements/
Bilgihan, A., Kandampully, J., & Zhang, T. (2016). Towards a unified customer experience in
online shopping environments: Antecedents and outcomes. International Journal of Quality
and Service Sciences, 8(1), 102-119.
Brookings, 2024. https://www.brookings.edu/articles/the-eu-and-us-diverge-on-ai-regulation-
a-transatlantic-comparison-and-steps-to-alignment/
Brooks, J., Wiedrich, K., Sims, L., & Rice, S. (2015). Excluded from the financial
mainstream: How the economic recovery is bypassing millions of Americans. Corporation
for Enterprise Development.
221184

Conclusion
|     |     |     |     |
| --- | --- | --- | --- |
  Caspi, I., Felber, S. S., & Gillis, T. B. Generative AI and the Future of Financial Advice
| References  |     | Regulation.  |     |
| ----------- | --- | ------------ | --- |
|             |     |              |     |
Abu Daqar, M. A., Arqawi, S., & Abu Karsh, S. (2021). Fintech in the eyes of Millennials and  Chauhan, S., Akhtar, A., & Gupta, A. (2022). Customer experience in digital banking: A
Generation Z (the financial behavior and Fintech perception).  review and future research directions. International Journal of Quality and Service
|     |     | Sciences, 14(2), 311-348.  |     |
| --- | --- | -------------------------- | --- |
Achim, M. V., Borlea, S. N., & Văidean, V. L. (2021). Does technology matter for combating
economic and financial crime? A panel data study. Technological and Economic Development  Collins, J. M. (2012). Financial advice: A substitute for financial literacy?. Financial Services
| of Economy, 27(1), 223-261.  |     | Review, 21(4), 307.  |     |
| ---------------------------- | --- | -------------------- | --- |
|                              |     |                      |     |
Agarwal, P., & Alam, M. (2020). A lightweight deep learning model for human activity  Dabija, D. C., Bejan, B. M., & Dinu, V. (2019). How sustainability oriented is Generation Z
recognition on edge devices. Procedia Computer Science, 167, 2364-2373.  in retail? A literature review. Transformations in Business & Economics, 18(2).
|     |     |     |     |
| --- | --- | --- | --- |
Al-Dmour, R., Dawood, E. A. H., Al-Dmour, H., & Masa'deh, R. E. (2020). The effect of  Davies, E., & Lea, S. E. (1995). Student attitudes to student debt. Journal of Economic
customer lifestyle patterns on the use of mobile banking applications in Jordan. International  Psychology, 16(4), 663-679
Journal of Electronic Marketing and Retailing, 11(3), 239-258.
  De Cnudde, S., Moeyersoms, J., Stankova, M., Tobback, E., Javaly, V., & Martens, D. (2019).
Alyousif, M., & Kalenkoski, C. M. (2017). Who seeks financial advice?. Available at SSRN  What does your Facebook profile reveal about your creditworthiness? Using alternative data
2943159.  for microfinance. Journal of the Operational Research Society, 70(3), 353-363.
|     |     |     |     |
| --- | --- | --- | --- |
Alhosani, F. A., & Tariq, M. U. (2020). Improving Service quality of smart banking using  Dew, J., & Xiao, J. J. (2011). The financial management behavior scale: Development and
quality management methods in UAE. International Journal of Mechanical Production  validation. Journal of Financial Counseling and Planning, 22(1), 43.
Engineering Research and Development (IJMPERD), 10(3), 2249-8001.
|     |     | Dhama, J. (2022). The future of financial advice.  |     |
| --- | --- | -------------------------------------------------- | --- |
Allen, F., Demirguc-Kunt, A., Klapper, L., & Peria, M. S. M. (2016). The foundations of  https://openresearch.ocadu.ca/id/eprint/3569/
financial inclusion: Understanding ownership and use of formal accounts. Journal of
Financial Intermediation, 27, 1-30.  Dhir, A., Khan, S. J., Islam, N., Ractham, P., & Meenakshi, N. (2023). Drivers of sustainable
  business model innovations. An upper echelon theory perspective. Technological Forecasting
Altman, D. G., & Bland, J. M. (1994). Diagnostic tests 3: receiver operating characteristic  and Social Change, 191, 122409.
| plots. BMJ: British Medical Journal, 309(6948), 188.  |     |     |     |
| ----------------------------------------------------- | --- | --- | --- |
  Djeundje, V. B., Crook, J., Calabrese, R., & Hamid, M. (2021). Enhancing credit scoring with
Azma, N., Rahman, M., Adeyemi, A. A., & Rahman, M. K. (2019). Propensity toward  alternative data. Expert Systems with Applications, 163, 113766.
indebtedness: Evidence from Malaysia. Review of Behavioral Finance.
  Dlogosch, T. J., Klinger, B., & Frese, M. (2017). Personality-based selection of
Biesenbach & Gundmunsson, 2019. Robo-advisory: Assessing the threat, and how banks  entrepreneurial borrowers to reduce credit risk: two studies on prediction models in low and
should respond in a time of increased transparency requirements. Simon-Kucher and partners.   high-stakes settings in developing countries. Journal of Organisational Behaviour, 39, 612-
https://internationalbanker.com/banking/robo-advisory-assessing-threat-banks-respond-time- 628.
| increased-transparency-requirements/  |     |     |     |
| ------------------------------------- | --- | --- | --- |
  Desai, H. N., & Patel, R. (2020, September). A study of data mining methods for prediction
Bilgihan, A., Kandampully, J., & Zhang, T. (2016). Towards a unified customer experience in  of personality traits. In 2020 International Conference on Smart Electronics and
online shopping environments: Antecedents and outcomes. International Journal of Quality  Communication (ICOSEC) (pp. 58-64). IEEE.
| and Service Sciences, 8(1), 102-119.  |     |     |     |
| ------------------------------------- | --- | --- | --- |
  Edwards L (2018) Data Protection: Enter the General Data Protection Regulation. In:
Brookings, 2024. https://www.brookings.edu/articles/the-eu-and-us-diverge-on-ai-regulation- Edwards L (ed.) Law, Policy and the Internet. Oxford: Hart, pp.77–117.
| a-transatlantic-comparison-and-steps-to-alignment/  |     |     |     |
| --------------------------------------------------- | --- | --- | --- |
  Elliott, K., Coopamootoo, K., Curran, E., Ezhilchelvan, P., Finnigan, S., Horsfall, D., ... &
Brooks, J., Wiedrich, K., Sims, L., & Rice, S. (2015). Excluded from the financial  van Moorsel, A. (2022). Know Your Customer: Balancing innovation and regulation for
mainstream: How the economic recovery is bypassing millions of Americans. Corporation  financial inclusion. Data & Policy, 4, e34.
| for Enterprise Development.  |      |     |         |
| ---------------------------- | ---- | --- | ------- |
|                              | 214  |     | 221159  |

Chapter 7
El Qadi, A., Trocan, M., Diaz-Rodriguez, N., & Frossard, T. (2023). Feature contribution
alignment with expert knowledge for artificial intelligence credit scoring. Signal, Image and
Video Processing, 17(2), 427-434
Epstein, S. (1994). Trait theory as personality theory: Can a part be as great as the
whole?. Psychological Inquiry, 5(2), 120-122.
Esposito De Falco, S., Scandurra, G., and Thomas, A. (2021). How stakeholders affect the
pursuit of the Environmental, Social, and Governance. Evidence from innovative small and
medium enterprises. Corp. Soc. Responsib. Environ. Manag. 28 (5), 1528–1539.
doi:10.1002/csr.2183
EU AI-Act: https://www.artificial-intelligence-act.com
Fuster, A., Plosser, M., Schnabl, P., & Vickery, J. (2019). The role of technology in mortgage
lending. The Review of Financial Studies, 32(5), 1854-1899.
Gicić, A., Đonko, D., & Subasi, A. (2023). Intelligent credit scoring using deep learning
methods. Concurrency and Computation: Practice and Experience, 35(9), e7637.
Goel, A., & Rastogi, S. (2023). Credit scoring of small and medium enterprises: a behavioural
approach. Journal of Entrepreneurship in Emerging Economies, 15(1), 46-69.
Harris, M., Adams, B., Davis, A., & Tijssen, J. (2022). Embedded finance: What it takes to
prosper in the new value chain. Bain & Co., available at: https://www. bain.
com/contentassets/a5ad904e61324de88b62707de879f174/bain_brief_ embedded-finance. pdf
(accessed 23rd April, 2023).
Haultain, S., Kemp, S., & Chernyshenko, O. S. (2010). The structure of attitudes to student
debt. Journal of Economic Psychology, 31(3), 322–330.
https://doi.org/10.1016/j.joep.2010.01.003
Hambrick, D. C., and Mason, P. A. (1984). Upper echelons: The organization as a reflection
of its top managers. Acad. Manage. Rev. 9 (2), 193–206. doi:10.5465/amr.1984.4277628
Hendricks, M. K., & Budree, A. (2019). Can a mobile credit-scoring model provide better
accessibility to South African citizens requiring micro-lending?. International Journal of
Electronic Finance, 9(3), 157-169.
Helman, R., Copeland, C., & VanDerhei, J. (2015). The 2015 retirement confidence survey:
Having a retirement savings plan a key factor in Americans’ retirement confidence. EBRI
issue brief, (413).
Hemmer, P., Schemmer, M., Kühl, N., Vössing, M., & Satzger, G. (2022). On the effect of
information asymmetry in human-AI teams. arXiv preprint arXiv:2205.01467.
Hurley, M., & Adebayo, J. (2016). Credit scoring in the era of big data. Yale journal of law
and technology, 18, 148.
222106

Conclusion
Kahawandala, N., & Peter, S. (2020, March). Factors affecting Purchasing Behaviour of
Generation Z. In Proceedings of the International Conference on Industrial Engineering and
Operations Management Dubai, UAE.
Klinger, B., Khwaja, A., & LaMonte, J. (2013). Improving credit risk analysis with
psychometrics in Peru. Inter-American Development Bank. Technical Note No. IDB-TN-587.
Kumar, P., & Chaubey, D. S. (2017). Demonetization and its impact on adoption of digital
payment: Opportunities, issues and challenges. Abhinav National Monthly Refereed Journal
of Research in Commerce & Management, 6(6), 15.
Lande, R. S., Meshram, S. A., & Deshmukh, P. P. (2018, August). Smart banking using IoT.
In 2018 International Conference on Research in Intelligent and Computing in Engineering
(RICE) (pp. 1-4). IEEE.
Li, F., Lu, H., Hou, M., Cui, K., & Darbandi, M. (2021). Customer satisfaction with bank
services: The role of cloud services, security, e-learning and service quality. Technology in
Society, 64, 101487.
Liberati, C., & Camillo, F. (2018). Personal values and credit scoring: new insights in the
financial prediction. Journal of the Operational Research Society, 69(12), 1994-2005.
Liu, Y., Huang, F., Ma, L., Zeng, Q., & Shi, J. (2024). Credit scoring prediction leveraging
interpretable ensemble learning. Journal of Forecasting, 43(2), 286-308.
Loh, R. K., & Choi, H. S. (2020). Physical frictions and digital banking adoption (pp. 1-50).
Working Paper.
Lusardi, A., & Mitchell, O. S. (2011). Financial Literacy and Planning: Implications for
Retirement Wellbeing (No. w17078). National Bureau of Economic Research.
Malhotra, R., & Malhotra, D. K. (2006). The impact of internet and e-commerce on the
evolving business models in the financial services industry. International Journal of
Electronic Business, 4(1), 56-82.
Mbama, C. I., & Ezepue, P. O. (2018). Digital banking, customer experience and bank
financial performance: UK customers’ perceptions. International Journal of Bank
Marketing, 36(2), 230-255.
Mc Kinsey & Company, 2021: https://www.mckinsey.com/industries/financial-services/our-
insights/joining-the-next-generation-of-digital-banks-in-asia
Mc Kinsey. (2022). https://www.mckinsey.com/industries/financial-services/our-
insights/embedded-finance-who-will-lead-the-next-payments-revolution
Mc Kinsey & Company, 2023: Mc Kinsey annual AI research 2023.
https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai-in-2023-
generative-ais-breakout-year
221271

Chapter 7
Mehdiabadi, A., Shahabi, V., Shamsinejad, S., Amiri, M., Spulbar, C., & Birau, R. (2022).
Investigating Industry 5.0 and its impact on the banking industry: Requirements, approaches
and communications. Applied Sciences, 12(10), 5126.
Mhlanga, D. (2020). Industry 4.0 in finance: the impact of artificial intelligence (ai) on digital
financial inclusion. International Journal of Financial Studies, 8(3), 45.
Moise, A. (2018). Life banking: How to become trusted advisers for holistic financial
health. Journal of Digital Banking, 3(1), 65-80.
Mondres, T. (2019). How Generation Z is changing financial services. American Bankers
Association. ABA Banking Journal, 111(1), 24.
Montmarquette, C., & Viennot-Briot, N. (2019). The gamma factors and the value of
financial advice. Annals of Economics and Finance, 20(1), 387-411.
Murinde, V., Rizopoulos, E., and Zachariadis, M. (2022). The impact of the FinTech
revolution on the future of banking: Opportunities and risks. Int. Rev. Financial Analysis 81,
102103. doi:10.1016/j.irfa.2022.102103
Mystakidis, S. (2022). Metaverse. Encyclopedia, 2(1), 486-497.
Nelson, P. (1970). Information and consumer behavior. Journal of Political Economy, 78(2),
311-329.
Nicoletti, B. (2021). Banking 5.0: How Fintech Will Change Traditional Banks in the'New
Normal'Post Pandemic. Springer Nature.
Norvilitis, J. M., Merwin, M. M., Osberg, T. M., Roehling, P. V., Young, P., & Kamas, M. M.
(2006). Personality factors, money attitudes, financial knowledge, and credit‐card debt in
college students. Journal of Applied Social Psychology, 36(6), 1395–1413.
https://doi.org/10.1111/j.0021-9029.2006.00065.x
Nosić, A., & Weber, M. (2010). How riskily do I invest? The role of risk attitudes, risk
perceptions, and overconfidence. Decision Analysis, 7(3), 282-301.
Obschonka, M., & Audretsch, D. B. (2020). Artificial intelligence and big data in
entrepreneurship: a new era has begun. Small Business Economics, 55, 529-539.
OECD (2019) Vectors of Digital Transformation. Paris: Organisation for Economic Co-
operation and Development.
Onay, C., & Öztürk, E. (2018). A review of credit scoring research in the age of Big
Data. Journal of Financial Regulation and Compliance.
Oracle. (2021). https://www.oracle.com/a/ocom/docs/industries/financial-services/embedded-
finance-transaction-banking-sb.pdf
Ostrowska, M., & Balcerowski, M. (2020). The idea of robotic insurance mediation in the
light of the European union law. InsurTech: A Legal and Regulatory View, 199-210.
222128

Conclusion
Mehdiabadi, A., Shahabi, V., Shamsinejad, S., Amiri, M., Spulbar, C., & Birau, R. (2022).
Investigating Industry 5.0 and its impact on the banking industry: Requirements, approaches  Ozili, P. K. (2021). Financial inclusion: Globally important determinants. Financial Internet
and communications. Applied Sciences, 12(10), 5126.  Quarterly, 17(4), 1-11.
|     |     |     |     |
| --- | --- | --- | --- |
Mhlanga, D. (2020). Industry 4.0 in finance: the impact of artificial intelligence (ai) on digital  Ozili, P. K. (2023). Assessing global interest in decentralized finance, embedded finance,
financial inclusion. International Journal of Financial Studies, 8(3), 45.  open finance, ocean finance and sustainable finance. Asian Journal of Economics and
|     |     | Banking, 7(2), 197-216.  |     |
| --- | --- | ------------------------ | --- |
Moise, A. (2018). Life banking: How to become trusted advisers for holistic financial
health. Journal of Digital Banking, 3(1), 65-80.  Pasquale F (2015) The Black Box Society. Cambridge, MA: Harvard University Press.
|     |     |     |     |
| --- | --- | --- | --- |
Mondres, T. (2019). How Generation Z is changing financial services. American Bankers  Prainsack B (2019) Logged out: Ownership, exclusion and public value in the digital data and
Association. ABA Banking Journal, 111(1), 24.  information commons. Big Data & Society. DOI: 10.1177/205395171982977.
|     |     |     |     |
| --- | --- | --- | --- |
Montmarquette, C., & Viennot-Briot, N. (2019). The gamma factors and the value of  PWC, 2018: https://www.pwc.de/en/digitale-transformation/pwc-study-next-generation-
financial advice. Annals of Economics and Finance, 20(1), 387-411.  client-onboarding-2018.pdf
|     |     |     |     |
| --- | --- | --- | --- |
Murinde, V., Rizopoulos, E., and Zachariadis, M. (2022). The impact of the FinTech  Seaward, H. G., & Kemp, S. (2000). Optimism bias and student debt. New Zealand Journal
revolution on the future of banking: Opportunities and risks. Int. Rev. Financial Analysis 81,  of Psychology, 29(1), 17-19.
| 102103. doi:10.1016/j.irfa.2022.102103  |     |     |     |
| --------------------------------------- | --- | --- | --- |
  Sedunov, J. (2017). Does bank technology affect small business lending decisions? J.
Mystakidis, S. (2022). Metaverse. Encyclopedia, 2(1), 486-497.  Financial Res. 40 (1), 5–32. doi:10.1111/jfir.12116
|     |     |     |     |
| --- | --- | --- | --- |
Nelson, P. (1970). Information and consumer behavior. Journal of Political Economy, 78(2),  Seemiller, C., & Grace, M. (2017). Generation Z: Educating and engaging the next generation
| 311-329.  |     | of students. About campus, 22(3), 21-26.  |     |
| --------- | --- | ----------------------------------------- | --- |
|           |     |                                           |     |
Nicoletti, B. (2021). Banking 5.0: How Fintech Will Change Traditional Banks in the'New  Shneiderman, B. (2022). Human-centered AI. Oxford University Press.
| Normal'Post Pandemic. Springer Nature.  |     |     |     |
| --------------------------------------- | --- | --- | --- |
  Serrado, J., Pereira, R. F., Mira da Silva, M., & Scalabrin Bianchi, I. (2020). Information
Norvilitis, J. M., Merwin, M. M., Osberg, T. M., Roehling, P. V., Young, P., & Kamas, M. M.  security frameworks for assisting GDPR compliance in banking industry. Digital Policy,
(2006). Personality factors, money attitudes, financial knowledge, and credit‐card debt in  Regulation and Governance, 22(3), 227-244.
college students. Journal of Applied Social Psychology, 36(6), 1395–1413.
https://doi.org/10.1111/j.0021-9029.2006.00065.x  Thaichon, P. (2017). Consumer socialization process: The role of age in children's online
  shopping behavior. Journal of Retailing and Consumer Services, 34, 38-47.
Nosić, A., & Weber, M. (2010). How riskily do I invest? The role of risk attitudes, risk
perceptions, and overconfidence. Decision Analysis, 7(3), 282-301.  Thakor, A. V. (2020). Fintech and banking: What do we know? J. Financial
|     |     | Intermediation 41, 100833. doi:10.1016/j.jfi.2019.100833  |     |
| --- | --- | --------------------------------------------------------- | --- |
Obschonka, M., & Audretsch, D. B. (2020). Artificial intelligence and big data in
entrepreneurship: a new era has begun. Small Business Economics, 55, 529-539.  Tiwari, A., & Yadav, A. (2022). A study of financial literacy and financial behaviour among
  millennials and generation Z. OURNAL OF THE ASIATIC SOCIETY OF MUMBAI, ISSN,
OECD (2019) Vectors of Digital Transformation. Paris: Organisation for Economic Co- 0972-0766.
| operation and Development.   |     |     |     |
| ---------------------------- | --- | --- | --- |
  Van Thiel, D., Goedee, J., & Leenders, R. (2023). Leveraging financial personality for
Onay, C., & Öztürk, E. (2018). A review of credit scoring research in the age of Big  inclusive credit scoring amidst global uncertainty. Journal of Risk Management in Financial
Data. Journal of Financial Regulation and Compliance.  Institutions, 17(1), 22-42.
|     |     |     |     |
| --- | --- | --- | --- |
Oracle. (2021). https://www.oracle.com/a/ocom/docs/industries/financial-services/embedded- Vidal, M. F., & Barbon, F. (2019). Credit Scoring in Financial Inclusion. Washington: CGAP.
| finance-transaction-banking-sb.pdf  |     |     |     |
| ----------------------------------- | --- | --- | --- |
  Viljoen S (2020) Democratic data: A relational theory for data governance. Yale Law Review.
Ostrowska, M., & Balcerowski, M. (2020). The idea of robotic insurance mediation in the  Available at: https://papers.ssrn.com/sol3/papers.cfm?abstract_id= 3727562 (accessed 7 May
light of the European union law. InsurTech: A Legal and Regulatory View, 199-210.  2021).
|     | 218  |     | 221293  |
| --- | ---- | --- | ------- |

Chapter 7
Windasari, N. A., Kusumawati, N., Larasati, N., & Amelia, R. P. (2022). Digital-only banking
experience: Insights from gen Y and Gen Z. Journal of Innovation & Knowledge, 7(2),
100170.
Wolinsky, A. (1995). Competition in markets for credence goods. Journal of Institutional and
Theoretical Economics (JITE)/Zeitschrift für die gesamte Staatswissenschaft, 117-131
WEF (2011) Personal Data: The Emergence of a New Asset Class. Geneva: World Economic
Forum.
Yang, S., & Berdine, G. (2017). The receiver operating characteristic (ROC) curve. The
Southwest Respiratory and Critical Care Chronicles, 5(19), 34-36.
Yonker, S. E. (2017). Do managers give hometown labor an edge? Rev. Financ. Stud. 30 (10),
3581–3604. doi:10.1093/rfs/hhx030
222240

Chapter 8
Windasari, N. A., Kusumawati, N., Larasati, N., & Amelia, R. P. (2022). Digital-only banking
experience: Insights from gen Y and Gen Z. Journal of Innovation & Knowledge, 7(2),
100170.
Wolinsky, A. (1995). Competition in markets for credence goods. Journal of Institutional and
Theoretical Economics (JITE)/Zeitschrift für die gesamte Staatswissenschaft, 117-131
WEF (2011) Personal Data: The Emergence of a New Asset Class. Geneva: World Economic
Forum.
Yang, S., & Berdine, G. (2017). The receiver operating characteristic (ROC) curve. The
Southwest Respiratory and Critical Care Chronicles, 5(19), 34-36.
Yonker, S. E. (2017). Do managers give hometown labor an edge? Rev. Financ. Stud. 30 (10),
3581–3604. doi:10.1093/rfs/hhx030
Research Valorisation
220

Chapter 8
Academic publications
Van Thiel, D., & van Raaij, F. (2017). Targeting the robo-advice customer: The development
of a psychometric segmentation model for financial advice robots. Journal of
Financial Transformation, 46, 88-104.
Van Thiel, D., & Van Raaij, F. (2017). Explaining customer experience of digital financial
advice. Economics, 5(1), 69-84.
Van Thiel, D., & Van Raaij, W. F. F. (2019). Artificial intelligence credit risk prediction:
An empirical study of analytical artificial intelligence tools for credit risk
prediction in a digital era. Journal of Risk Management in Financial
Institutions, 12(3), 268-286.
Van Thiel, D., & van Raaij, W. F. (2019). Artificial Intelligent Credit Risk Prediction:
An Empirical Study of Analytical Artificial Intelligence Tools for Credit Risk
Prediction in a Digital Era. Journal of Accounting & Finance (2158-
3625), 19(8).
Van Thiel, D., Goedee, J., & Leenders, R. (2023). Leveraging financial personality for
inclusive credit scoring amidst global uncertainty. Journal of Risk
Management in Financial Institutions, 17(1), 22-42.
Van Thiel, D., Elliott, K, Goedee, J., & Leenders, R. (2024). Responsible Access to Credit for
Sole-Traders and Micro-organizations under Unstable Market Conditions with
Psychometrics. European Journal of Finance. Special issue Fintech & Risk.
Academic conference presentations
Van Thiel, D., & van Raaij, F. (2014). Robo-advice for the next generations. Annual
academic conference of The Society for the Advancement of Behavioral
Economics, July 21st – July 24th 2014, Harvey Lake Tahoe hotel,
Lake Tahoe, USA.
Van Thiel, D. (2019). AI in Risk. 94th annual conference of the World Economic Association
International (WEAI), June 28th – July 2nd 2019, Hilton Union Square,
San Francisco, USA.
Van Thiel, D. (2023). Diversity challenges for a sustainable fintech. Workshop on
Environmental Finance for the Common Good. April 13th, 2023, Pavia
University, Pavia, Italy.
Van Thiel, D. (2023). Challenges in Fintech Amid an Unstable Macroeconomic Climate.
UKFin+ launch event, July 4th – July 5th 2023, The Berkeley hotel
Knightsbridge, London, United Kingdom.
Van Thiel, D. (2024). Dynamic credit scoring for inclusive finance. 99th annual conference of
the World Economic Association International (WEAI), June 29th – July 3rd
2019, Hyatt Regency, Seattle, USA.
222262

Research Valorisation
Books
Van Thiel, D., Goedee, J., & Reijnders, W. J. M. (2008). Riding the waves. The future of
banking starts now. Pearson Education.
Van Thiel, D. (2009). Got EQ? Cool!. Pearson Education.
Caeldries, F., Goedee, J., Rijkers, A., & Wijnands, L. (2010). Financial services marketing.
Chapter: The Future of Financial Services (pp. 285–309). Lemma.
Van Thiel, D. (2025). Working title: “Empowering Finance: Navigating the Human-Centered
AI Revolution in Banking.” LID Publishing.
Professional publications
Van Thiel, D. (2023, September 22). Unlocking Underwriting Potential: The Power of Data-
Research Valorisation
Driven Transformation.
https://www.finextra.com/blogposting/24932/unlocking-underwriting-
potential-the-power-of-data-driven-transformation
Van Thiel, D. (2023, May 31). Unlocking Embedded Finance: Dynamic Data and AI Leading
the Way. https://www.finextra.com/blogposting/24282/unlocking-embedded-
finance-dynamic-data-and-ai-leading-the-way
Van Thiel, D. (2023, May 10). Harnessing The Power of AI: Navigating Macro-Economic
Instability. https://www.finextra.com/blogposting/24182/harnessing-the-
power-of-ai-navigating-macro-economic-instability
Van Thiel, D. (2023, April 19). War of the Titans: Tech Banks Lock Horns in the Battle for
Customers through Open Banking.
https://www.finextra.com/blogposting/24072/war-of-the-titans-tech-banks-
lock-horns-in-the-battle-for-customers-through-open-banking
Van Thiel, D. (2023, April 5). Urgently Resetting Banks' Growth Strategy in the Current
Climate. https://www.finextra.com/blogposting/24007/urgently-resetting-
banks-growth-strategy-in-the-current-climate
Van Thiel, D. (2022, May 24). Revolutionizing venture capital: How AI based structured
investment can improve VC ROI by 45%.
https://www.finextra.com/blogposting/22329/revolutionizing-venture-capital-
how-ai-based-structured-investment-can-improve-vc-roi-by-45
Van Thiel, D. (2022, April 14). The embedded finance transformation: Think big! Think
smart! Be bold! And do it!
https://www.finextra.com/blogposting/22145/the-embedded-finance-
transformation-think-big-think-smart-be-bold-and-do-it
222237

Chapter 8
Van Thiel, D. (2022, March 25). COOL! REVOLUTIONIZE CUSTOMER EXPERIENCE
FOR EMBEDDED FINANCE.
https://www.finextra.com/blogposting/22049/cool-revolutionize-customer-
experience-for-embedded-finance
Van Thiel, D. (2021, December 10). Game-changers: Harnessing the power of alternative
Data.
https://www.finextra.com/blogposting/21388/game-changers-harnessing-the-
power-of-alternative-data
Van Thiel, D. (2021, November 26). Sustainable Game Changers with balls.
https://www.finextra.com/blogposting/21324/sustainable-game-changers-with-
balls
Van Thiel, D. (2021, November 12). Game Changers for SME Banking.
https://www.finextra.com/blogposting/21248/game-changers-for-sme-banking
Van Thiel, D. (2021, October 29). Game Changers for Next Gen Banking.
https://www.finextra.com/blogposting/21156/game-changers-for-next-gen-
banking
Van Thiel, D. (2020, November 30). EAT OR BE EATEN: THIS IS THE POST-COVID
CHAMPION IN BANKING!
https://www.finextra.com/blogposting/19586/eat-or-be-eaten-this-is-the-post-
covid-champion-in-banking
Van Thiel, D. (2020, November 9). Win or lose? Winning banks break through the Big Tech
Nash equilibrium.
https://www.finextra.com/blogposting/19507/win-or-lose-winning-banks-
break-through-the-big-tech-nash-equilibrium
Van Thiel, D. (2020, October 27). The post COVID war has started: the leading group of
digital banks against Big tech and Fintech.
https://www.finextra.com/blogposting/19465/the-post-covid-war-has-started-
the-leading-group-of-digital-banks-against-big-tech-and-fintech
Van Thiel, D. (2020, October 13). Survival of the fittest: Digital advice, the strategic cost –
income play.
https://www.finextra.com/blogposting/19420/survival-of-the-fittest-digital-
advice-the-strategic-cost---income-play
Van Thiel, D. (2020, September 25). Last boarding call: Post-COVID Risk Decisioning starts
now!
https://www.finextra.com/blogposting/19358/last-boarding-call-post-covid-
risk-decisioning-starts-now
Van Thiel, D. (2017, November 20). How Cognitive Intelligence can drive banks’ cost
income breakthroughs.
https://www.finextra.com/blogposting/14756/how-cognitive-intelligence-can-
drive-banks-cost-income-breakthroughs
222284

Research Valorisation
Van Thiel, D. (2022, March 25). COOL! REVOLUTIONIZE CUSTOMER EXPERIENCE
FOR EMBEDDED FINANCE. Van Thiel, D. (2017, June 8). Winning the Insurers’ race with robotics.
https://www.finextra.com/blogposting/22049/cool-revolutionize-customer- https://www.finextra.com/blogposting/14165/winning-the-insurers-race-with-
experience-for-embedded-finance robotics
Van Thiel, D. (2021, December 10). Game-changers: Harnessing the power of alternative Van Thiel, D. (2016, December 27). Do or die: Robo-advice &amp; Psychometry What
Data. drives wealth management winners in 2020?
https://www.finextra.com/blogposting/21388/game-changers-harnessing-the- https://www.finextra.com/blogposting/13494/do-or-die-robo-advice-amp-
power-of-alternative-data psychometry-what-drives-wealth-management-winners-in-2020
Van Thiel, D. (2021, November 26). Sustainable Game Changers with balls. Van Thiel, D. (2016, December 3). How behavioural economics and robo-advice change cost
https://www.finextra.com/blogposting/21324/sustainable-game-changers-with- income strategies.
balls https://www.finextra.com/blogposting/13428/how-behavioural-economics-
and-robo-advice-change-cost-income-strategies
Van Thiel, D. (2021, November 12). Game Changers for SME Banking.
https://www.finextra.com/blogposting/21248/game-changers-for-sme-banking Van Thiel, D. (2016, October 21). New strategic credit weapons in the 2017 banking battle on
cost income.
Van Thiel, D. (2021, October 29). Game Changers for Next Gen Banking. https://www.finextra.com/blogposting/13285/new-strategic-credit-weapons-in-
https://www.finextra.com/blogposting/21156/game-changers-for-next-gen- the-2017-banking-battle-on-cost-income
Research Valorisation
banking
Van Thiel, D. (2016, July 6). Robo-advice: will it really change the lending market?
Van Thiel, D. (2020, November 30). EAT OR BE EATEN: THIS IS THE POST-COVID https://www.finextra.com/blogposting/12817/robo-advice-will-it-really-
CHAMPION IN BANKING! change-the-lending-market
https://www.finextra.com/blogposting/19586/eat-or-be-eaten-this-is-the-post-
covid-champion-in-banking
Van Thiel, D. (2020, November 9). Win or lose? Winning banks break through the Big Tech Professional achievements
Nash equilibrium.
https://www.finextra.com/blogposting/19507/win-or-lose-winning-banks- Teaching
break-through-the-big-tech-nash-equilibrium
Van Thiel, D. (2022 - 2024). Advanced Marketing Analytics. Visiting professor, Jheronimus
Van Thiel, D. (2020, October 27). The post COVID war has started: the leading group of Academy of Data Science. Den Bosch, The Netherlands.
digital banks against Big tech and Fintech.
https://www.finextra.com/blogposting/19465/the-post-covid-war-has-started- Van Thiel, D. (2017). Digital Behavioral Finance. Guest- lecturer, Cambridge Judge Business
the-leading-group-of-digital-banks-against-big-tech-and-fintech School. Cambridge, United Kingdom.
Van Thiel, D. (2020, October 13). Survival of the fittest: Digital advice, the strategic cost – Van Thiel, D. (2006 - 2010). Future of Finance. Visiting professor, TIAS Business School,
income play. Tilburg, The Netherlands.
https://www.finextra.com/blogposting/19420/survival-of-the-fittest-digital-
advice-the-strategic-cost---income-play Business
Van Thiel, D. (2020, September 25). Last boarding call: Post-COVID Risk Decisioning starts Founder | CEO of AdviceRobo (2015 – 2024). A pioneering Behavioral Analytics Platform
now! offering inclusive holistic finance solutions driving financial wellness for the next
https://www.finextra.com/blogposting/19358/last-boarding-call-post-covid- generations across 13 countries, The Hague, The Netherlands. https://advicerobo.com
risk-decisioning-starts-now
Founder | CEO of E-cology Innovations. (2010 – 2024). European Human-Centered AI
Van Thiel, D. (2017, November 20). How Cognitive Intelligence can drive banks’ cost boutique, The Hague, The Netherlands. https://ecologyinnovations.com
income breakthroughs.
https://www.finextra.com/blogposting/14756/how-cognitive-intelligence-can- Non – Executive Director Ikano Bank. (2014 – 2024). Ikano bank is Ikea’s retail bank across
drive-banks-cost-income-breakthroughs 8 European countries, Malmo, Sweden. https://bank.ikano
224 222259

Chapter 8
• Chairman of the board sustainability committee.
• Member of the board IT-transformation committee.
Non – Executive Director Ikano Insight. (2023 – 2024). Ikano Insight provides global retail-,
location- and sustainability analytics, London, United Kingdom. https://insight.ikano
Steering group member UKFin+. UKFin+ is an EPSRC funded £2.5M programme of
academic funding, whose aim is to bridge the gap that currently exists between the research
in universities and the needs of the financial services industry, consumers, and regulators.
Based on an inclusive, diverse and responsible research culture it has the objective to
harmonize technological know-how across regions. https://ukfin.network
Elected as London Fintech CEO of the year 2018. https://www.ceo-review.com/issues/issue-
10-2018/12/
223206

Chapter 9
• Chairman of the board sustainability committee.
• Member of the board IT-transformation committee.
Non – Executive Director Ikano Insight. (2023 – 2024). Ikano Insight provides global retail-,
location- and sustainability analytics, London, United Kingdom. https://insight.ikano
Steering group member UKFin+. UKFin+ is an EPSRC funded £2.5M programme of
academic funding, whose aim is to bridge the gap that currently exists between the research
in universities and the needs of the financial services industry, consumers, and regulators.
Based on an inclusive, diverse and responsible research culture it has the objective to
harmonize technological know-how across regions. https://ukfin.network
Elected as London Fintech CEO of the year 2018. https://www.ceo-review.com/issues/issue-
10-2018/12/
Summary of the thesis
226

Chapter 9
On
The Human-Centered AI
Transformation of Banking
Exploring the impact of behavioral finance & AI on banking transformation.
The world has been under strain since the COVID crisis. The COVID crisis itself caused
global economic lockdowns, leading people to adopt digital ways of working. Post-COVID, a
so-called ‘new normal’ emerged—a world marked by uncertainty, geopolitical tensions,
rising interest rates, and inflation. This has resulted in increased political polarization, a
growing number of people struggling to make ends meet, and younger generations finding it
increasingly difficult to build their lives. However, it has also intensified the push to reduce
our climate footprint. All this is happening in a world experiencing a technological
renaissance. Mobile phone penetration is historically high worldwide, and although AI
originated in 1956, the technology only truly broke through in 2023 with the launch of
ChatGPT. Additionally, we are witnessing an explosion of personal data through the use of
computers, mobile phones, smartwatches, and smart platforms.
As a fintech entrepreneur, non-executive board member, and former bank director, I have had
the privilege of applying these developments in my companies. With eyeOpen, we developed
a digital mortgage advisor to provide first-time homebuyers with the most suitable and
affordable mortgages. With AdviceRobo, we built a human-centered AI inclusive credit
intelligence assistant to give the next generations access to finance at affordable prices—
whether they wanted to buy a house, start a business, or needed growth capital for personal or
business purposes. Our mission is to create such smart and innovative digital assistants that
we can provide everyone in the world with access to affordable finance when and where they
need it. Through E-cology Innovations, we help companies with human-centered AI
transformations, developing new business models, strategies, and applications to improve the
well-being of these target groups. I apply my knowledge and experience to lead digital
transformations as a non-executive board member in the companies where I hold this role.
Through my work, I have developed a great passion for what I call intelligent digital
transformations. I am honored to have been able to apply this passion in fundamental
research for my PhD. In this dissertation, I investigate how financial behavioral biases can be
discovered in data patterns to provide people with better digital advice and more suitable
financial products. In four studies on psychometric behavioral biases—described in chapters
2 to 5—this dissertation aims to provide better digital financial advice and products for the
many people who have difficulty accessing or managing finance, based on the insights and
models developed. In another study, we examine the impact of AI on financial inclusion by
testing AI credit score models against traditional scorecards.
By harnessing the insights from psychometric segmentation and AI-driven credit analysis,
these business models provide inclusive, micro-personalized financial guidance tailored to
individual needs, behaviors, and creditworthiness, while also striving for a positive impact on
the world.
This thesis explores the transformative impact of human-centered AI and behavioral finance
on the banking sector, with a specific focus on the transformation to Banking 5.0. It begins by
introducing the potential of these technologies to enhance inclusive financial services and
improve customer experiences through digital advice. Subsequently, the research delves into
psychometric segmentation models aimed at targeting customers effectively for digital and
robo-advice solutions. Further investigation reveals how financial personality profiles can be
utilized for inclusive credit scoring during periods of global uncertainty, enhancing the
223228

Summary of the thesis
accuracy of credit assessments. The thesis then examines the role of AI in predicting credit
risks, particularly its application to digital lending for small enterprises and sole traders,
emphasizing its capacity to facilitate access to credit under unstable market conditions. The
study concludes by summarizing the key findings and discussing the broader implications for
the future of banking, advocating for a transition towards a more inclusive and holistic
financial system.
Through a multi-method quantitative research design, five studies were conducted and
reported in five journal articles (chapters 2–6) along with a theoretical framework chapter
(chapter 1). Subsequently, the combined results form the basis for the final findings and
conclusions presented in chapter 7. This multi-method quantitative approach included
systematic literature research, structured surveys, cluster analysis, factor analyses, logistic
regression modeling and random forest modeling, aiming to provide extensive and in-depth
insights into the application of AI, as well as behavioral and psychometric biases in digital
financial advice and credit risk scoring. The studies utilized random sampling techniques on
both actual neo-bank customers and research panels across the USA, the UK, the
Netherlands, and the Czech Republic. Data was collected from vulnerable customer
segments, such as low-income consumers, sole traders, and small businesses, who have a
high need for accessing finance in a highly unstable macroeconomic climate.
Chapter 2 explores the key attributes that underpin the desired customer experience in digital
financial advice. This chapter introduces the Digital Customer Experience (DCX) model, a
pioneering cross-cultural framework designed to advance the customer experience in
financial advice systems. The DCX model emphasizes the importance of experiential
attributes such as honesty, reliability, and transparency over outcome-related attributes like
price and product diversity. This shift suggests that customer expectations will change
significantly over the next five to ten years. Key findings indicate that offering a wider range
of brands and products is becoming increasingly important and the ability for co-creation in
the digital advisory process, particularly in the UK, is critical. Pricing considerations and the
demand for personalization in the robo-advisory market are also highlighted.
The research outcomes suggest that applying a foundational personality layer to digital
advisors can enhance customer strategies, engagement, and satisfaction. Integrating
psychometric data into digital advisory processes can improve robo-advice, and the
increasing volume and variety of data, along with advancements in AI techniques like
machine learning, present new opportunities for providing digital advice and support tools for
financial inclusion and wellness. Additionally, personalizing content and services based on
psychometrics and behaviors offers the potential for micro-personalization, creating a more
tailored and effective digital financial advice experience.
Chapter 3 investigates whether the use of psychometric data can improve market
segmentation in the digital advice sector. This study employs a combined approach to data
analysis, creating a segmentation model tailored to the preferences and personalities of the
next generation. A survey conducted with 2,332 respondents used 12 psychometric questions
from the Dutch Authority of Financial Markets monitor. Principal component analysis and
Ward clustering identified three components for digital advice segmentation: level of
convenience seeking, financial literacy, and preference for process orientation.
Convenience emerged as the dominant factor, underscoring the importance of easily
purchasing the most suitable product. Financial literacy was identified as having a dual
perspective, with low-literacy customers needing education and support, while highly literate
customers were an attractive segment for financial advice robots. The study suggested
tailored content personalization and predictive services for this segment. The third factor
highlighted the significance of considering individuals' rigidity in decision-making, with
222393

Chapter 9
conservative customers preferring control and thorough decision-making. Smartly developed
digital tools, such as virtual financial assistants, could cater to this segment's needs.
The results from Chapters 2 and 3 collectively address the first research question, which
focuses on how individual psychological factors like lifestyles, attitudes, and behaviors
impact holistic digital finance within the framework of inclusive Banking 5.0. The findings
emphasize that psychometric segmentation and the integration of personality insights are
crucial for developing smart digital credit advice. By understanding and leveraging individual
psychological factors, digital financial services can be more effectively tailored to meet the
diverse needs and preferences of customers. This approach not only enhances customer
satisfaction but also broadens access to digital financial advice, promoting financial inclusion
and wellness.
Chapter 4 introduces a pioneering psychometric credit scoring model designed to promote
intelligent and inclusive financial practices tailored to the needs of the next generation of
consumers within the context of Banking 5.0. The study involved developing a conceptual
framework for a psychometric credit scorecard, which was tested through a cross-national
survey of 897 low-income individuals from the United States and the Netherlands. This
survey, the first of its kind, aimed to gauge financial literacy attributes through a
questionnaire of 17 predefined psychometric questions. The responses, collected via an
automated, scalable survey, covered aspects such as financial competencies, gratification
tendencies, materialistic inclinations, attitudes towards indebtedness, self-assurance levels,
cognitive aptitude, social desirability, and demographic particulars.
The analysis revealed an inverse correlation between financial acumen and the propensity for
arrears, indicating that higher financial literacy is associated with fewer defaults. Structural
equation modeling provided detailed insights into the relative importance of various
attributes, which were used to refine the psychometric framework for customer risk
stratification. The study suggests that government-led initiatives to enhance financial literacy
could reduce payment delays and improve financial well-being. Additionally, digital lending
entities are encouraged to offer educational resources and financial management support to
applicants with lower financial literacy. The research also highlighted a positive correlation
between attitudes toward indebtedness and susceptibility to arrears, and a negative correlation
between social desirability and arrears incidence.
Chapter 6 details an experimental investigation to assess the value addition of the newly
developed psychometric scorecard in the risk assessment of sole traders and micro-
enterprises. The study incorporated the attribute of fluid intelligence into the scorecard and
tested it with 2,884 micro and small businesses in the Czech Republic. The experiment aimed
to evaluate the scorecard's impact on access to finance by analyzing the actual payment
behaviors of accepted borrowers before and during the COVID-19 pandemic. Data from a
fintech company was used for this purpose, and a counterfactual analysis was conducted to
compare the psychometric scorecard with traditional credit scoring models.
The findings demonstrated the psychometric scorecard's efficacy in facilitating appropriate
risk differentiation for sole traders and micro-organizations. Significant correlations were
found between financial skills, self-efficacy, debt attitudes, social desirability, and default
occurrences. The counterfactual analysis revealed that the psychometric scorecard provided
superior risk differentiation compared to traditional models, particularly during the stress
period of the COVID-19 pandemic. These results underscore the scorecard's robustness and
resilience in times of crisis, highlighting its potential to enhance financial inclusion and
access to finance in environments with limited traditional credit data.
The results from Chapters 4 and 6 collectively address the second research question, which
investigates how individual psychological factors like lifestyles, attitudes, and behaviors
223340

Summary of the thesis
influence comprehensive inclusive credit risk management within the context of inclusive
Banking 5.0. The studies illustrate that incorporating psychometric data into credit scoring
models can significantly improve risk assessment, especially for underbanked segments such
as low-income individuals, sole traders and small businesses. By leveraging attributes like
financial literacy, self-efficacy, and attitudes towards debt, the psychometric scorecard offers
a more nuanced and effective approach to credit risk management. This enhanced risk
differentiation not only improves financial inclusion but also helps digital financial services
provide more personalized and accurate credit advice, thus meeting the evolving needs of the
next generation of banking customers.
Chapter 5 focuses on the third research phase, which investigates the integration of AI-based
credit scorecards compared to traditional logistic regression models. The study addresses data
imbalance issues by involving three major credit providers, resulting in a research sample of
133,152 mortgage and credit card customers from the United Kingdom and the Netherlands.
Three experiments were conducted with tier 1 and tier 2 lenders, utilizing neural networks
and decision trees as AI models. Decision trees were favored for their interpretability and
ability to capture non-linear relationships, handle missing values, and provide clear variable
importance. The AI-based models demonstrated superior accuracy and predictive power for
both mortgages and credit cards across the studied geographies compared to traditional
logistic regression models, thus supporting the transformation to Banking 5.0 business
models.
Having synthesized the emprical findings and referring to the theoretical discussions in this
thesis, the following conclusions and implications can be derived with regard to the impact of
human- centred AI on the transformation of banking towards Banking 5.0. This dissertation
provides a comprehensive examination of how individual psychological factors and advanced
analytical techniques can enhance digital financial advice and credit scoring within the
framework of inclusive Banking 5.0. The research highlights the transformative potential of
integrating psychometric insights and AI techniques into digital financial services. By
leveraging psychometric data, the study demonstrates how financial institutions can offer
more personalized and engaging customer experiences, ultimately leading to greater
satisfaction and better financial outcomes. The findings underscore the importance of
experiential attributes such as honesty, reliability, and transparency, which are increasingly
valued by next-generation banking customers.
Furthermore, the research explores the use of psychometric data to improve market
segmentation and credit scoring models. It identifies key psychometric components, such as
convenience seeking, financial literacy, and preference for process orientation, which
influence customer preferences and behaviors. The integration of these insights into digital
advisory and credit scoring processes significantly enhances the appeal and effectiveness of
these services. AI-based models, particularly decision trees, are shown to offer superior
accuracy and predictive power in credit risk assessment, especially when incorporating
alternative psychometric and behavioral data. This approach not only improves the accuracy
of credit decisions but also supports financial inclusion by providing more nuanced and
effective risk assessments for underbanked segments.
Overall, the dissertation emphasizes the need for intelligent, personalized, and inclusive
digital financial services in the evolving landscape of Banking 5.0. The research provides
actionable solutions for enhancing financial inclusion and access to finance, offering valuable
guidance for policymakers, financial institutions, and fintech companies. By addressing the
unique needs and behaviors of next-generation banking customers, the findings contribute to
the development of more effective and inclusive digital financial services, aligning with the
goals of a digitally-driven financial ecosystem.
223315

Chapter 9
The results of this thesis can be translated into several applications for financial institutions as
it provides financial institutions with a comprehensive framework for enhancing customer
experiences and credit assessments.
1. The DCX model, developed from our research, serves as a pivotal tool for
practitioners to implement micro-personalization strategies that drive value creation
and customer engagement. By focusing on experiential system aspects, financial
institutions can optimize their digital financial advice systems to provide gamified,
user-friendly interfaces, personalized recommendations, ratings and reviews, and
seamless interactions. This human-centric approach not only differentiates financial
institutions but also aligns with regulatory requirements and supports global
expansion and innovation.
2. The development of the world's first psychometric market segmentation model for
digital financial advice robots and assistants, as discussed in Chapter 3, offers
significant practical implications. Financial institutions can leverage this model to
tailor financial advice and services based on customers' psychometric factors, such as
financial literacy levels and personality traits. This targeted approach enables
practitioners to enhance personalization, education, activation, and engagement,
particularly for underserved populations like Generation Z and millennials. By
addressing specific psychometric factors, financial institutions can bridge knowledge
gaps and empower customers to make informed financial decisions, ultimately
contributing to financial inclusion and wellness.
3. Chapter 4's analysis of individuals' financial personalities for inclusive credit scoring
highlights the potential for integrating psychometric scorecards into traditional credit
assessments. This integration provides a nuanced approach to credit evaluation,
especially in uncertain economic environments. Practitioners can enhance credit
scoring models by incorporating psychometric data, leading to tailored financial
products and improved risk management. This approach not only supports financial
inclusion for vulnerable groups but also ensures more accurate credit assessments and
reduced default rates.
4. By investing in scalable, AI-driven credit risk solutions, financial institutions can
streamline decision-making processes, adapt to digital lending trends, and contribute
to the stability and resilience of the global financial system.
Overall, our study emphasizes the importance of blending psychometric insights with AI
capabilities to create a more inclusive, empathetic, and effective approach to Banking 5.0.
Financial institutions are encouraged to adopt these innovative strategies to enhance customer
experiences, improve financial inclusion, and maintain competitive advantage in the rapidly
evolving financial landscape. By leveraging our research findings, practitioners can build
novel business models, strategies and applications that navigate market uncertainties and
evolving consumer behaviors, ensuring that their services are not only profitable but also
inclusive and aligned with ethical standards and regulatory requirements.
223362

The results of this thesis can be translated into several applications for financial institutions as
it provides financial institutions with a comprehensive framework for enhancing customer
experiences and credit assessments.
1. The DCX model, developed from our research, serves as a pivotal tool for
practitioners to implement micro-personalization strategies that drive value creation
and customer engagement. By focusing on experiential system aspects, financial
institutions can optimize their digital financial advice systems to provide gamified,
user-friendly interfaces, personalized recommendations, ratings and reviews, and
seamless interactions. This human-centric approach not only differentiates financial
institutions but also aligns with regulatory requirements and supports global
expansion and innovation.
2. The development of the world's first psychometric market segmentation model for
digital financial advice robots and assistants, as discussed in Chapter 3, offers
significant practical implications. Financial institutions can leverage this model to
tailor financial advice and services based on customers' psychometric factors, such as
financial literacy levels and personality traits. This targeted approach enables
practitioners to enhance personalization, education, activation, and engagement,
particularly for underserved populations like Generation Z and millennials. By
addressing specific psychometric factors, financial institutions can bridge knowledge
gaps and empower customers to make informed financial decisions, ultimately
contributing to financial inclusion and wellness.
3. Chapter 4's analysis of individuals' financial personalities for inclusive credit scoring
highlights the potential for integrating psychometric scorecards into traditional credit
assessments. This integration provides a nuanced approach to credit evaluation,
especially in uncertain economic environments. Practitioners can enhance credit
scoring models by incorporating psychometric data, leading to tailored financial
products and improved risk management. This approach not only supports financial
inclusion for vulnerable groups but also ensures more accurate credit assessments and
reduced default rates.
4. By investing in scalable, AI-driven credit risk solutions, financial institutions can
streamline decision-making processes, adapt to digital lending trends, and contribute
to the stability and resilience of the global financial system.
Overall, our study emphasizes the importance of blending psychometric insights with AI
capabilities to create a more inclusive, empathetic, and effective approach to Banking 5.0.
Financial institutions are encouraged to adopt these innovative strategies to enhance customer
experiences, improve financial inclusion, and maintain competitive advantage in the rapidly
evolving financial landscape. By leveraging our research findings, practitioners can build
novel business models, strategies and applications that navigate market uncertainties and
evolving consumer behaviors, ensuring that their services are not only profitable but also
inclusive and aligned with ethical standards and regulatory requirements.
Samenvatting van het proefschrift
232

De mensgerichte AI-transformatie van de banksector
Verkenning van de impact van gedragseconomie en AI op de transformatie van de banksector
De wereld staatonder hoogspanning sinds de COVID-crisis. De COVID-crisis zelf
veroorzaakte wereldwijde economische lockdowns, waardoor mensen digitaal gingen
werken. Na COVID ontstond er een zogenaamd 'nieuw normaal' - een wereld gekenmerkt
door onzekerheid, geopolitieke spanningen, stijgende rentetarieven en inflatie. Dit heeft
geleid tot toenemende politieke polarisatie, een groeiend aantal mensen dat moeite heeft om
rond te komen, en jongere generaties die het steeds moeilijker vinden om hun leven op te
bouwen. Het heeft echter ook de druk om onze ecologische voetafdruk te verminderen,
geïntensiveerd. Dit alles gebeurt in een wereld die een technologische renaissance doormaakt.
De penetratie van mobiele telefoons is wereldwijd historisch hoog, en hoewel AI in 1956
ontstond, brak de technologie pas echt door in 2023 met de lancering van ChatGPT.
Daarnaast zien we een explosie van persoonlijke data door het gebruik van computers,
mobiele telefoons, smartwatches en slimme platforms.
Als fintech-ondernemer, commissaris en voormalig bankdirecteur had ik het voorrecht deze
ontwikkelingen toe te passen in mijn bedrijven. Met eyeOpen ontwikkelden we een digitale
hypotheekadviseur om starters op de woningmarkt de meest geschikte en betaalbare
hypotheken te bieden. Met AdviceRobo bouwden we een mensgerichte AI-assistent voor
‘krediet intelligence’ om de volgende generaties toegang te geven tot betaalbare financiering
- of ze nu een huis wilden kopen, een bedrijf wilden starten of groeikapitaal nodig hadden
voor persoonlijke of zakelijke doeleinden. Onze missie is om zulke slimme en innovatieve
digitale assistenten te creëren dat we iedereen ter wereld toegang kunnen geven tot betaalbare
financiering wanneer en waar ze die nodig hebben. Via E-cology Innovations helpen we
bedrijven met mensgerichte AI-transformaties, waarbij we nieuwe businessmodellen,
strategieën en toepassingen ontwikkelen om het welzijn van hun klantsegmenten te
verbeteren. Ik pas verder mijn kennis en ervaring toe om digitale transformaties te leiden als
commissaris in de bedrijven waar ik deze rol vervul.
Door mijn werk heb ik een grote passie ontwikkeld voor wat ik noem intelligente digitale
transformaties. Ik ben vereerd dat ik deze passie heb kunnen toepassen in fundamenteel
onderzoek voor mijn promotie. In dit proefschrift onderzoek ik hoe financiële
gedragsafwijkingen kunnen worden ontdekt in datapatronen om mensen beter digitaal advies
en geschiktere financiële producten te bieden. In vier studies naar psychometrische
gedragsafwijkingen - beschreven in hoofdstukken 2 tot 6 - heeft dit proefschrift tot doel om
beter digitaal financieel advies en producten te bieden aan de vele mensen die moeite hebben
met toegang tot of beheer van hun financiën. In een andere studie (hoofdstuk 5) onderzoeken
we de impact van AI op financiële inclusie door AI-kredietscoormodellen te testen ten
opzichte van traditionele scorecards.
Door gebruik te maken van de inzichten uit psychometrische segmentatie en AI-gedreven
kredietanalyse, bieden deze businessmodellen inclusieve, micropersoonlijke financiële
begeleiding die is afgestemd op individuele behoeften, gedragingen en kredietwaardigheid,
terwijl ze ook streven naar een positieve impact op de wereld. Dit proefschrift onderzoekt de
transformerende impact van mensgerichte AI en gedragseconomie op de banksector, met een
223384

Samenvatting van het proefschrift
specifieke focus op de transformatie naar Banking 5.0. Het begint met het introduceren van
het potentieel van deze technologieën om inclusieve financiële diensten te verbeteren en
klantbelevingen te optimaliseren via digitaal advies. Vervolgens gaat het onderzoek dieper in
De mensgerichte AI-transformatie van de banksector op psychografische segmentatiemodellen die gericht zijn op het effectief targeten van klanten
voor digitale en robo-adviesoplossingen. Verder onderzoek onthult hoe financiële
persoonlijkheidsprofielen kunnen worden gebruikt voor inclusieve kredietscores tijdens
Verkenning van de impact van gedragseconomie en AI op de transformatie van de banksector
periodes van wereldwijde onzekerheid, waardoor de nauwkeurigheid van
kredietbeoordelingen verder wordt verbeterd. Het proefschrift onderzoekt vervolgens de rol
De wereld staatonder hoogspanning sinds de COVID-crisis. De COVID-crisis zelf
van AI bij het voorspellen van kredietrisico's, met name de toepassing ervan op digitale
veroorzaakte wereldwijde economische lockdowns, waardoor mensen digitaal gingen
leningen voor kleine ondernemingen en eenmanszaken, waarbij de capaciteit ervan wordt
werken. Na COVID ontstond er een zogenaamd 'nieuw normaal' - een wereld gekenmerkt
benadrukt om toegang tot krediet te vergemakkelijken onder instabiele
door onzekerheid, geopolitieke spanningen, stijgende rentetarieven en inflatie. Dit heeft
marktomstandigheden. Het onderzoek concludeert met een samenvatting van de belangrijkste
geleid tot toenemende politieke polarisatie, een groeiend aantal mensen dat moeite heeft om
bevindingen en bespreking van de bredere implicaties voor de toekomst van de banksector,
rond te komen, en jongere generaties die het steeds moeilijker vinden om hun leven op te
waarbij wordt gepleit voor een overgang naar een inclusiever en holistischer financieel
bouwen. Het heeft echter ook de druk om onze ecologische voetafdruk te verminderen,
systeem.
geïntensiveerd. Dit alles gebeurt in een wereld die een technologische renaissance doormaakt.
De penetratie van mobiele telefoons is wereldwijd historisch hoog, en hoewel AI in 1956
Via een multimethodische kwantitatief onderzoeksopzet werden vijf studies uitgevoerd en
ontstond, brak de technologie pas echt door in 2023 met de lancering van ChatGPT.
gepubliceerd in vijf tijdschriftartikelen (hoofdstukken 2-6). Vervolgens vormen de
Daarnaast zien we een explosie van persoonlijke data door het gebruik van computers,
gecombineerde resultaten de basis voor de uiteindelijke bevindingen en conclusies die in
mobiele telefoons, smartwatches en slimme platforms.
hoofdstuk 7 worden gepresenteerd. Deze multimethodische kwantitatieve benadering omvatte
systematisch literatuuronderzoek, gestructureerde enquêtes, clusteranalyse, factoranalyses,
Als fintech-ondernemer, commissaris en voormalig bankdirecteur had ik het voorrecht deze
logistische regressiemodellering en random forest-modellering, met als doel uitgebreide en
ontwikkelingen toe te passen in mijn bedrijven. Met eyeOpen ontwikkelden we een digitale
diepgaande inzichten te verschaffen in de toepassing van AI, evenals gedrags- en
hypotheekadviseur om starters op de woningmarkt de meest geschikte en betaalbare
psychometrische afwijkingen voor digitaal financieel advies en kredietrisicoscoring. De
hypotheken te bieden. Met AdviceRobo bouwden we een mensgerichte AI-assistent voor
studies maakten gebruik van willekeurige steekproeftechnieken (random sampling) op zowel
‘krediet intelligence’ om de volgende generaties toegang te geven tot betaalbare financiering
daadwerkelijke neobankklanten als onderzoekspanels in de VS, het VK, Nederland.
- of ze nu een huis wilden kopen, een bedrijf wilden starten of groeikapitaal nodig hadden
Gegevens werden verzameld van kwetsbare klantsegmenten, zoals consumenten met een laag
voor persoonlijke of zakelijke doeleinden. Onze missie is om zulke slimme en innovatieve
inkomen, eenmanszaken en kleine bedrijven, die een hoge behoefte hebben aan toegang tot
digitale assistenten te creëren dat we iedereen ter wereld toegang kunnen geven tot betaalbare
financiering in een zeer onstabiel macro-economisch klimaat.
financiering wanneer en waar ze die nodig hebben. Via E-cology Innovations helpen we
bedrijven met mensgerichte AI-transformaties, waarbij we nieuwe businessmodellen,
Hoofdstuk 2 onderzoekt de belangrijkste kenmerken die ten grondslag liggen aan de
strategieën en toepassingen ontwikkelen om het welzijn van hun klantsegmenten te
gewenste klantervaring in digitaal financieel advies. Dit hoofdstuk introduceert het Digital
verbeteren. Ik pas verder mijn kennis en ervaring toe om digitale transformaties te leiden als
Customer Experience (DCX)-model, een baanbrekend cross-cultureel raamwerk ontworpen
commissaris in de bedrijven waar ik deze rol vervul.
om de klantervaring in financiële adviessystemen te verbeteren. Het DCX-model benadrukt
het belang van ervaringskenmerken zoals eerlijkheid, betrouwbaarheid en transparantie boven
Door mijn werk heb ik een grote passie ontwikkeld voor wat ik noem intelligente digitale
resultaatgerelateerde kenmerken zoals prijs en productdiversiteit. Deze verschuiving
transformaties. Ik ben vereerd dat ik deze passie heb kunnen toepassen in fundamenteel
suggereert dat de verwachtingen van klanten de komende vijf tot tien jaar aanzienlijk zullen
onderzoek voor mijn promotie. In dit proefschrift onderzoek ik hoe financiële
veranderen. Belangrijke bevindingen geven aan dat het aanbieden van een breder scala aan
gedragsafwijkingen kunnen worden ontdekt in datapatronen om mensen beter digitaal advies
merken en producten steeds belangrijker wordt en dat de mogelijkheid voor co-creatie in het
en geschiktere financiële producten te bieden. In vier studies naar psychometrische
digitale adviesproces, met name in het VK, cruciaal is. Prijsfactoren en de vraag naar
gedragsafwijkingen - beschreven in hoofdstukken 2 tot 6 - heeft dit proefschrift tot doel om
personalisatie in de robo-advisorymarkt worden ook benadrukt.
beter digitaal financieel advies en producten te bieden aan de vele mensen die moeite hebben
met toegang tot of beheer van hun financiën. In een andere studie (hoofdstuk 5) onderzoeken
De onderzoeksresultaten suggereren dat het toepassen van een fundamentele
we de impact van AI op financiële inclusie door AI-kredietscoormodellen te testen ten
persoonlijkheidslaag op digitale adviseurs klantstrategieën, betrokkenheid en tevredenheid
opzichte van traditionele scorecards.
kan verbeteren. Integratie van psychometrische gegevens in digitale adviesprocessen kan
robo-advies verbeteren, en het toenemende volume en de verscheidenheid aan gegevens,
Door gebruik te maken van de inzichten uit psychometrische segmentatie en AI-gedreven
samen met vooruitgang in AI-technieken zoals machine learning, bieden nieuwe kansen voor
kredietanalyse, bieden deze businessmodellen inclusieve, micropersoonlijke financiële
het leveren van digitale advies- en ondersteuningshulpmiddelen voor financiële inclusie en
begeleiding die is afgestemd op individuele behoeften, gedragingen en kredietwaardigheid,
welzijn. Bovendien biedt personalisatie van content en diensten op basis van psychografische
terwijl ze ook streven naar een positieve impact op de wereld. Dit proefschrift onderzoekt de
transformerende impact van mensgerichte AI en gedragseconomie op de banksector, met een
234 223359

en gedragsfactoren het potentieel voor micropersonalisatie, waardoor een meer op maat psychometrische kader voor klant risicostratificatie te verfijnen. De studie suggereert dat door
gemaakte en effectieve digitale financiële advieservaring ontstaat. de overheid geleide initiatieven om de financiële geletterdheid te verbeteren
betalingsachterstanden in landen zouden kunnen verminderen en het financiële welzijn in die
Hoofdstuk 3 onderzoekt of het gebruik van psychometrische gegevens de marktsegmentatie landen zouden kunnen verbeteren. Bovendien worden digitale kredietverstrekkers
in de digitale adviessector kan verbeteren. Deze studie maakt gebruik van een gecombineerde aangemoedigd om training en ondersteuning bij de financien van hun klanten te bieden.
benadering van data-analyse, waarbij een segmentatiemodel wordt gecreëerd dat is afgestemd Specifiek bij klanten met een lage financiele geletterdheid. Het onderzoek toonde ook een
op de voorkeuren en persoonlijkheden van de volgende generatie. Een enquête onder 2.332 positieve correlatie tussen attitudes ten opzichte van schulden en de vatbaarheid voor
respondenten gebruikte 12 psychometrische vragen uit de monitor van de Autoriteit achterstanden, en een negatieve correlatie tussen sociale wenselijkheid en het optreden van
Financiële Markten. Hoofdcomponentanalyse en Ward-clustering identificeerden drie achterstanden.
componenten voor digitale adviessegmentatie: mate van gemakzoekendheid, financiële
geletterdheid en voorkeur voor procesoriëntatie. Hoofdstuk 6 beschrijft een experimenteel onderzoek naar de waarde toevoeging van de nieuw
ontwikkelde psychometrische scorekaart in de risico beoordeling van eenmanszaken en
Gemak bleek de dominante factor te zijn, wat het belang onderstreept van het gemakkelijk micro-ondernemingen. De studie bevatte het attribuut ‘vloeibare intelligentie’ in de scorekaart
kunnen aanschaffen van het meest geschikte product. Financiële geletterdheid werd en testte deze met 2.884 micro- en kleine bedrijven in Tsjechië. Het experiment was gericht
geïdentificeerd als een factor met een dubbel perspectief, waarbij klanten met een lage op het testen van de impact van de nieuwe scorekaart op de toegang tot financiering voor en
financiele geletterdheid educatie en ondersteuning nodig hebben, terwijl klanten met een tijdens de COVID-19 pandemie. Gegevens van een fintech-bedrijf werden hiervoor gebruikt,
hoge financiele geletterdheid een aantrekkelijk segment zijn voor financiële adviesrobots. De en een counterfactual analyse werd uitgevoerd om de psychometrische scorekaart te
studie suggereerde inhoudspersonalisatie en voorspellende diensten voor dit segment. De vergelijken met traditionele kredietscoormodellen.
derde factor benadrukte het belang van het overwegen van de rigiditeit van individuen in
besluitvorming, waarbij conservatieve klanten de voorkeur geven aan controle en grondige De bevindingen toonden de effectiviteit van de psychometrische scorekaart aan bij het zoeken
besluitvorming. Slim ontwikkelde digitale tools, zoals virtuele financiële assistenten, kunnen naar risicodifferentiatie voor eenmanszaken en micro-organisaties. Er werden significante
inspelen op de behoeften van dit segment. correlaties gevonden tussen financiële vaardigheden, zelfeffectiviteit, schuldenattitudes,
sociale wenselijkheid en wanbetalingen. De counterfactual analyse bracht he tinzicht dat de
De resultaten van hoofdstukken 2 en 3 beantwoorden gezamenlijk de eerste onderzoeksvraag, psychometrische scorekaart superieure risicodifferentiatie bood/ biedt, vergeleken met
die zich richt op hoe individuele psychologische factoren zoals levensstijlen, attitudes en traditionele modellen, vooral tijdens de stressperiode van de COVID-19 pandemie. Deze
gedragingen holistische digitale financiën beïnvloeden binnen het kader van inclusieve resultaten onderstrepen de robuustheid en veerkracht van de scorekaart in tijden van crisis, en
Banking 5.0. De bevindingen benadrukken dat psychometrische segmentatie en de integratie benadrukken het potentieel ervan om financiële inclusie en toegang tot financiering te
van persoonlijkheidsinzichten cruciaal zijn voor de ontwikkeling van slimme digitale verbeteren in omgevingen met beperkte traditionele kredietgegevens.
kredietadviezen. Door individuele psychologische factoren te begrijpen en te benutten,
kunnen digitale financiële diensten effectiever worden afgestemd op de diverse behoeften en De resultaten van Hoofdstukken 4 en 6 behandelen gezamenlijk de tweede onderzoeksvraag,
voorkeuren van klanten. Deze aanpak verhoogt niet alleen de klanttevredenheid, maar die onderzoekt hoe individuele psychologische factoren zoals levensstijlen, attitudes en
verbreedt ook de toegang tot digitaal financieel advies, wat financiële inclusie en welzijn gedragingen invloed hebben op uitgebreide inclusieve kredietrisicobeheer binnen de context
bevordert. van inclusieve Banking 5.0. De studies illustreren dat het opnemen van psychometrische
gegevens in kredietscoormodellen de risico beoordeling aanzienlijk verbetert, vooral voor
Hoofdstuk 4 introduceert een nieuw psychometrisch kredietscoormodel dat is ontworpen om laag inkomens segmenten zoals consumenten met een laag inkomen, eenmanszaken en kleine
intelligente en inclusieve financiële activiteiten te bevorderen die zijn afgestemd op de bedrijven. Door gebruik te maken van eigenschappen zoals financiële geletterdheid,
behoeften van de volgende generatie consumenten binnen de context van Banking 5.0. De zelfeffectiviteit en attitudes ten opzichte van schulden, biedt de psychometrische scorekaart
studie omvatte het ontwikkelen van een conceptueel kader voor een psychometrische een genuanceerdere en effectievere benadering van kredietrisicobeheer. Deze verbeterde
kredietscorekaart, die werd getest in een onderzoek onder 897 personen met een laag risicodifferentiatie verbetert niet alleen de financiële inclusie, maar helpt ook digitale
inkomen uit de Verenigde Staten en Nederland. Deze enquête, de eerste in zijn soort, was financiële dienstverleners om gepersonaliseerder en nauwkeuriger kredietadvies te bieden en
gericht op het meten van financiële geletterdheidseigenschappen via een vragenlijst met 17 daarmee aan de veranderende behoeften van de jongee generaties te voldoen.
vooraf gedefinieerde psychometrische vragen. De reacties, verzameld via een
geautomatiseerde enquête, bevatten aspecten zoals financiële vaardigheden, neigingen tot Hoofdstuk 5 richt zich op de derde onderzoeksfase, die de integratie van AI-gebaseerde
impulsaankoopgedrag, materialistisch gedrag, attitudes ten opzichte van schulden, kredietscorekaarten vergelijkt met traditionele logistische regressiemodellen. De studie met
zelfverzekerdheid, cognitieve vaardigheden, sociale wenselijkheid en demografische drie grote kredietverstrekkers kende een onderzoekssteekproef van 133.152 hypotheek- en
gegevens. creditcardklanten uit het Verenigd Koninkrijk en Nederland. Er werden drie experimenten
De analyse toonde een inverse correlatie tussen financiële vaardigheden en de neiging tot uitgevoerd met tier 1 en tier 2 kredietverstrekkers, waarbij neurale netwerken en
achterstanden, wat aangeeft dat een hogere financiële geletterdheid gepaard gaat met minder beslissingsbomen als AI-modellen werden gebruikt. Beslissingsbomen werden geprefereerd
wanbetalingen. Structurele-equatiemodellering verschafte gedetailleerde inzichten in het vanwege hun uitlegbaarheid en vermogen om niet-lineaire relaties vast te leggen,
relatieve belang van de verschillende eigenschappen, die werden gebruikt om het ontbrekende waarden een plek te geven en duidelijk inzicht te geven in de zwaarte van de
224306 237

Samenvatting van het proefschrift
en gedragsfactoren het potentieel voor micropersonalisatie, waardoor een meer op maat psychometrische kader voor klant risicostratificatie te verfijnen. De studie suggereert dat door
gemaakte en effectieve digitale financiële advieservaring ontstaat. de overheid geleide initiatieven om de financiële geletterdheid te verbeteren
betalingsachterstanden in landen zouden kunnen verminderen en het financiële welzijn in die
Hoofdstuk 3 onderzoekt of het gebruik van psychometrische gegevens de marktsegmentatie landen zouden kunnen verbeteren. Bovendien worden digitale kredietverstrekkers
in de digitale adviessector kan verbeteren. Deze studie maakt gebruik van een gecombineerde aangemoedigd om training en ondersteuning bij de financien van hun klanten te bieden.
benadering van data-analyse, waarbij een segmentatiemodel wordt gecreëerd dat is afgestemd Specifiek bij klanten met een lage financiele geletterdheid. Het onderzoek toonde ook een
op de voorkeuren en persoonlijkheden van de volgende generatie. Een enquête onder 2.332 positieve correlatie tussen attitudes ten opzichte van schulden en de vatbaarheid voor
respondenten gebruikte 12 psychometrische vragen uit de monitor van de Autoriteit achterstanden, en een negatieve correlatie tussen sociale wenselijkheid en het optreden van
Financiële Markten. Hoofdcomponentanalyse en Ward-clustering identificeerden drie achterstanden.
componenten voor digitale adviessegmentatie: mate van gemakzoekendheid, financiële
geletterdheid en voorkeur voor procesoriëntatie. Hoofdstuk 6 beschrijft een experimenteel onderzoek naar de waarde toevoeging van de nieuw
ontwikkelde psychometrische scorekaart in de risico beoordeling van eenmanszaken en
Gemak bleek de dominante factor te zijn, wat het belang onderstreept van het gemakkelijk micro-ondernemingen. De studie bevatte het attribuut ‘vloeibare intelligentie’ in de scorekaart
kunnen aanschaffen van het meest geschikte product. Financiële geletterdheid werd en testte deze met 2.884 micro- en kleine bedrijven in Tsjechië. Het experiment was gericht
geïdentificeerd als een factor met een dubbel perspectief, waarbij klanten met een lage op het testen van de impact van de nieuwe scorekaart op de toegang tot financiering voor en
financiele geletterdheid educatie en ondersteuning nodig hebben, terwijl klanten met een tijdens de COVID-19 pandemie. Gegevens van een fintech-bedrijf werden hiervoor gebruikt,
hoge financiele geletterdheid een aantrekkelijk segment zijn voor financiële adviesrobots. De en een counterfactual analyse werd uitgevoerd om de psychometrische scorekaart te
studie suggereerde inhoudspersonalisatie en voorspellende diensten voor dit segment. De vergelijken met traditionele kredietscoormodellen.
derde factor benadrukte het belang van het overwegen van de rigiditeit van individuen in
besluitvorming, waarbij conservatieve klanten de voorkeur geven aan controle en grondige De bevindingen toonden de effectiviteit van de psychometrische scorekaart aan bij het zoeken
besluitvorming. Slim ontwikkelde digitale tools, zoals virtuele financiële assistenten, kunnen naar risicodifferentiatie voor eenmanszaken en micro-organisaties. Er werden significante
inspelen op de behoeften van dit segment. correlaties gevonden tussen financiële vaardigheden, zelfeffectiviteit, schuldenattitudes,
sociale wenselijkheid en wanbetalingen. De counterfactual analyse bracht he tinzicht dat de
De resultaten van hoofdstukken 2 en 3 beantwoorden gezamenlijk de eerste onderzoeksvraag, psychometrische scorekaart superieure risicodifferentiatie bood/ biedt, vergeleken met
die zich richt op hoe individuele psychologische factoren zoals levensstijlen, attitudes en traditionele modellen, vooral tijdens de stressperiode van de COVID-19 pandemie. Deze
gedragingen holistische digitale financiën beïnvloeden binnen het kader van inclusieve resultaten onderstrepen de robuustheid en veerkracht van de scorekaart in tijden van crisis, en
Banking 5.0. De bevindingen benadrukken dat psychometrische segmentatie en de integratie benadrukken het potentieel ervan om financiële inclusie en toegang tot financiering te
van persoonlijkheidsinzichten cruciaal zijn voor de ontwikkeling van slimme digitale verbeteren in omgevingen met beperkte traditionele kredietgegevens.
kredietadviezen. Door individuele psychologische factoren te begrijpen en te benutten,
kunnen digitale financiële diensten effectiever worden afgestemd op de diverse behoeften en De resultaten van Hoofdstukken 4 en 6 behandelen gezamenlijk de tweede onderzoeksvraag,
voorkeuren van klanten. Deze aanpak verhoogt niet alleen de klanttevredenheid, maar die onderzoekt hoe individuele psychologische factoren zoals levensstijlen, attitudes en
verbreedt ook de toegang tot digitaal financieel advies, wat financiële inclusie en welzijn gedragingen invloed hebben op uitgebreide inclusieve kredietrisicobeheer binnen de context
bevordert. van inclusieve Banking 5.0. De studies illustreren dat het opnemen van psychometrische
gegevens in kredietscoormodellen de risico beoordeling aanzienlijk verbetert, vooral voor
Hoofdstuk 4 introduceert een nieuw psychometrisch kredietscoormodel dat is ontworpen om laag inkomens segmenten zoals consumenten met een laag inkomen, eenmanszaken en kleine
intelligente en inclusieve financiële activiteiten te bevorderen die zijn afgestemd op de bedrijven. Door gebruik te maken van eigenschappen zoals financiële geletterdheid,
behoeften van de volgende generatie consumenten binnen de context van Banking 5.0. De zelfeffectiviteit en attitudes ten opzichte van schulden, biedt de psychometrische scorekaart
studie omvatte het ontwikkelen van een conceptueel kader voor een psychometrische een genuanceerdere en effectievere benadering van kredietrisicobeheer. Deze verbeterde
kredietscorekaart, die werd getest in een onderzoek onder 897 personen met een laag risicodifferentiatie verbetert niet alleen de financiële inclusie, maar helpt ook digitale
inkomen uit de Verenigde Staten en Nederland. Deze enquête, de eerste in zijn soort, was financiële dienstverleners om gepersonaliseerder en nauwkeuriger kredietadvies te bieden en
gericht op het meten van financiële geletterdheidseigenschappen via een vragenlijst met 17 daarmee aan de veranderende behoeften van de jongee generaties te voldoen.
vooraf gedefinieerde psychometrische vragen. De reacties, verzameld via een
geautomatiseerde enquête, bevatten aspecten zoals financiële vaardigheden, neigingen tot Hoofdstuk 5 richt zich op de derde onderzoeksfase, die de integratie van AI-gebaseerde
impulsaankoopgedrag, materialistisch gedrag, attitudes ten opzichte van schulden, kredietscorekaarten vergelijkt met traditionele logistische regressiemodellen. De studie met
zelfverzekerdheid, cognitieve vaardigheden, sociale wenselijkheid en demografische drie grote kredietverstrekkers kende een onderzoekssteekproef van 133.152 hypotheek- en
gegevens. creditcardklanten uit het Verenigd Koninkrijk en Nederland. Er werden drie experimenten
De analyse toonde een inverse correlatie tussen financiële vaardigheden en de neiging tot uitgevoerd met tier 1 en tier 2 kredietverstrekkers, waarbij neurale netwerken en
achterstanden, wat aangeeft dat een hogere financiële geletterdheid gepaard gaat met minder beslissingsbomen als AI-modellen werden gebruikt. Beslissingsbomen werden geprefereerd
wanbetalingen. Structurele-equatiemodellering verschafte gedetailleerde inzichten in het vanwege hun uitlegbaarheid en vermogen om niet-lineaire relaties vast te leggen,
relatieve belang van de verschillende eigenschappen, die werden gebruikt om het ontbrekende waarden een plek te geven en duidelijk inzicht te geven in de zwaarte van de
236 223471

variabelen bij het voorspellen van betalingsachterstanden. De AI-gebaseerde modellen waren
nauwkeuriger en kenden een betere voorspelkracht voor zowel hypotheken als creditcards in
de bestudeerde geografische gebieden. Ze kunnen daarmee een belangrijke rol spelen in de
transformatie naar Banking 5.0 businessmodellen.
We kunnen nu de volgende conclusies en implicaties afleiden met betrekking tot de impact
van mensgerichte AI op de transformatie van de banksector naar Banking 5.0. Dit proefschrift
biedt een uitgebreide verkenning van hoe individuele psychologische factoren en
geavanceerde analytische technieken digitaal financieel advies en kredietscoring kunnen
verbeteren binnen het kader van inclusieve Banking 5.0. Het onderzoek benadrukt het
transformatie potentieel van het integreren van psychometrische inzichten en AI-technieken
in digitale financiële diensten. Door gebruik te maken van psychometrische gegevens, toont
de studie aan hoe financiële instellingen gepersonaliseerdere en meer betrokken
klantervaringen kunnen bieden. De modellen tonen aan dat dit uiteindelijk leidt tot grotere
tevredenheid en betere financiële resultaten. De bevindingen onderstrepen ook het belang van
ervaringsgerichte eigenschappen bij financieel advies zoals eerlijkheid, betrouwbaarheid en
transparantie. Met name de volgende generatie waardeert dit meer.
Verder onderzoekt deze studie het gebruik van psychometrische gegevens om
marktsegmentatie en kredietscoormodellen te verbeteren. Het identificeert belangrijke
psychometrische componenten, zoals gemakzoekendheid, financiële geletterdheid en
voorkeur voor procesoriëntatie, die klantvoorkeuren en -gedragingen beïnvloeden. De
integratie van deze inzichten in digitale advies- en kredietscoorprocessen verbetert significant
de aantrekkelijkheid en effectiviteit van deze diensten. AI-gebaseerde modellen, met name
beslissingsbomen, blijken superieure nauwkeurigheid en voorspellende kracht te bieden bij
kredietrisicobeoordeling, vooral wanneer alternatieve psychometrische en gedragsgegevens
worden opgenomen. Deze benadering verbetert niet alleen de nauwkeurigheid van
kredietbeslissingen, maar ondersteunt ook financiële inclusie door meer genuanceerde en
effectieve risicobeoordelingen te bieden voor laag inkomen segmenten.
Al met al benadrukt het proefschrift de noodzaak van intelligente, gepersonaliseerde en
inclusieve digitale financiële diensten in het evoluerende landschap naar Banking 5.0. Het
onderzoek biedt business modellen, strategieen en uitvoerbare oplossingen voor het
verbeteren van financiële inclusie en toegang tot financiering. Het biedt daarmee waardevolle
richtlijnen voor beleidsmakers, financiële instellingen en fintech-bedrijven. Door in te spelen
op de unieke behoeften en gedragingen van de volgende generatie bankklanten, dragen de
bevindingen bij aan de ontwikkeling van effectiever en inclusiever digitaal financieel
systeem.
De resultaten van dit proefschrift kunnen worden vertaald naar verschillende toepassingen
voor financiële instellingen, aangezien het financiële instellingen een uitgebreid raamwerk
biedt voor het verbeteren van klant ervaringen en krediet beoordelingen.
1. Het DCX-model dient als een cruciaal instrument voor neo-bankiers om micro-
personalisatie strategieën te implementeren die waardecreatie en klant loyaliteit
bevorderen. Door zich te concentreren op ervaringsgerichte systeem aspecten kunnen
financiële instellingen hun digitale financiële adviessystemen optimaliseren om
speelse, gebruiksvriendelijke interfaces, gepersonaliseerde aanbevelingen,
beoordelingen en recensies, en makkelijke interacties te bieden. Deze mensgerichte
benadering differentieert niet alleen financiële instellingen, maar zorgt ook voor
naleving van regelgeving en ondersteunt wereldwijde uitbreiding en innovatie.
224328

Samenvatting van het proefschrift
variabelen bij het voorspellen van betalingsachterstanden. De AI-gebaseerde modellen waren
nauwkeuriger en kenden een betere voorspelkracht voor zowel hypotheken als creditcards in
de bestudeerde geografische gebieden. Ze kunnen daarmee een belangrijke rol spelen in de 2. De ontwikkeling van het eerste psychografische marktsegmentatiemodel voor digitale
transformatie naar Banking 5.0 businessmodellen. financiële adviesrobots en assistenten, zoals besproken in Hoofdstuk 3, biedt
aanzienlijke praktische implicaties. Financiële instellingen kunnen dit model
We kunnen nu de volgende conclusies en implicaties afleiden met betrekking tot de impact gebruiken om financieel advies en diensten af te stemmen op de psychografische
van mensgerichte AI op de transformatie van de banksector naar Banking 5.0. Dit proefschrift factoren van klanten, zoals niveaus van financiële geletterdheid en
biedt een uitgebreide verkenning van hoe individuele psychologische factoren en persoonlijkheidstrekken. Deze gerichte aanpak stelt praktijkmensen in staat
geavanceerde analytische technieken digitaal financieel advies en kredietscoring kunnen personalisatie, educatie, activatie en betrokkenheid te verbeteren, met name voor laag
verbeteren binnen het kader van inclusieve Banking 5.0. Het onderzoek benadrukt het inkomensbevolkingsgroepen zoals Generatie Z en millennials. Door specifieke
transformatie potentieel van het integreren van psychometrische inzichten en AI-technieken psychografische factoren aan te pakken, kunnen financiële instellingen kennisgaten
in digitale financiële diensten. Door gebruik te maken van psychometrische gegevens, toont overbruggen en klanten in staat stellen weloverwogen financiële beslissingen te
de studie aan hoe financiële instellingen gepersonaliseerdere en meer betrokken nemen, wat uiteindelijk bijdraagt aan financiële inclusie en welzijn.
klantervaringen kunnen bieden. De modellen tonen aan dat dit uiteindelijk leidt tot grotere
tevredenheid en betere financiële resultaten. De bevindingen onderstrepen ook het belang van 3. De analyse van financiële persoonlijkheden van individuen voor inclusieve
ervaringsgerichte eigenschappen bij financieel advies zoals eerlijkheid, betrouwbaarheid en kredietbeoordeling in Hoofdstuk 4 benadrukt het potentieel voor de integratie van
transparantie. Met name de volgende generatie waardeert dit meer. psychometrische scorekaarten in traditionele kredietbeoordelingen. Deze integratie
biedt een genuanceerde benadering van kredietevaluatie, vooral in onzekere
Verder onderzoekt deze studie het gebruik van psychometrische gegevens om economische omgevingen. Praktijkmensen kunnen kredietbeoordelingsmodellen
marktsegmentatie en kredietscoormodellen te verbeteren. Het identificeert belangrijke verbeteren door psychometrische gegevens op te nemen, wat leidt tot op maat
psychometrische componenten, zoals gemakzoekendheid, financiële geletterdheid en gemaakte financiële producten en verbeterd risicobeheer. Deze aanpak ondersteunt
voorkeur voor procesoriëntatie, die klantvoorkeuren en -gedragingen beïnvloeden. De niet alleen financiële inclusie voor kwetsbare groepen, maar zorgt ook voor
integratie van deze inzichten in digitale advies- en kredietscoorprocessen verbetert significant nauwkeurigere kredietbeoordelingen en lagere wanbetalingspercentages.
de aantrekkelijkheid en effectiviteit van deze diensten. AI-gebaseerde modellen, met name
beslissingsbomen, blijken superieure nauwkeurigheid en voorspellende kracht te bieden bij 4. Door te investeren in schaalbare, door AI aangedreven oplossingen voor
kredietrisicobeoordeling, vooral wanneer alternatieve psychometrische en gedragsgegevens kredietrisico's, kunnen financiële instellingen besluitvormingsprocessen stroomlijnen,
worden opgenomen. Deze benadering verbetert niet alleen de nauwkeurigheid van zich aanpassen aan digitale kredietverleningstrends en bijdragen aan de stabiliteit en
kredietbeslissingen, maar ondersteunt ook financiële inclusie door meer genuanceerde en veerkracht van het wereldwijde financiële systeem.
effectieve risicobeoordelingen te bieden voor laag inkomen segmenten.
Al met al benadrukt het proefschrift de noodzaak van intelligente, gepersonaliseerde en Onze studie benadrukt het belang van de combinatie van psychometrische inzichten met
inclusieve digitale financiële diensten in het evoluerende landschap naar Banking 5.0. Het AI om een meer inclusieve, empathische en effectieve benadering voor de wereld van
onderzoek biedt business modellen, strategieen en uitvoerbare oplossingen voor het Banking 5.0 te creëren. Financiële instellingen worden aangemoedigd deze innovatieve
verbeteren van financiële inclusie en toegang tot financiering. Het biedt daarmee waardevolle strategieën te adopteren om klantervaringen te verbeteren, financiële inclusie te
richtlijnen voor beleidsmakers, financiële instellingen en fintech-bedrijven. Door in te spelen bevorderen en hun concurrentiepositie te behouden in het snel veranderende financiële
op de unieke behoeften en gedragingen van de volgende generatie bankklanten, dragen de landschap. Door gebruik te maken van onze onderzoeksresultaten kunnen neo-bankiers
bevindingen bij aan de ontwikkeling van effectiever en inclusiever digitaal financieel nieuwe bedrijfsmodellen, strategieën en toepassingen ontwikkelen om daarmee beter
systeem. tussen de marktonzekerheden en veranderend consumentengedrag te navigeren,
waardoor hun diensten niet alleen winstgevend zijn, maar ook inclusive en in
De resultaten van dit proefschrift kunnen worden vertaald naar verschillende toepassingen overeenstemming met ethische normen en regelgeving.
voor financiële instellingen, aangezien het financiële instellingen een uitgebreid raamwerk
biedt voor het verbeteren van klant ervaringen en krediet beoordelingen.
1. Het DCX-model dient als een cruciaal instrument voor neo-bankiers om micro-
personalisatie strategieën te implementeren die waardecreatie en klant loyaliteit
bevorderen. Door zich te concentreren op ervaringsgerichte systeem aspecten kunnen
financiële instellingen hun digitale financiële adviessystemen optimaliseren om
speelse, gebruiksvriendelijke interfaces, gepersonaliseerde aanbevelingen,
beoordelingen en recensies, en makkelijke interacties te bieden. Deze mensgerichte
benadering differentieert niet alleen financiële instellingen, maar zorgt ook voor
naleving van regelgeving en ondersteunt wereldwijde uitbreiding en innovatie.
238 223493

Biography
Diederick embodies the spirit of innovation and leadership in the
world of embedded finance and technology. As an esteemed board
member, data-tech entrepreneur, and visionary writer, he stands as
one of Europe’s foremost fintech pioneers. His remarkable journey
has been marked by accolades, including the prestigious London
Fintech CEO of the Year award in 2018 and the recognition of all
his fintech ventures in the European Fintech Fifty.
At the helm of fintech scale-up AdviceRobo and AI-boutique
E-cology Innovations, Diederick orchestrates groundbreaking
solutions that redefine the landscape of finance, retail and telcoms.
His visionary leadership extends to serving as a non-executive director at Ikano Bank
(IKEA) in Sweden and Ikano Insight (retal- & sustainability analytics) in London, where
his strategic insights drive impactful change. Untill 2010 he served on the boards of ING &
KPN Mobile.
Driven by a profound sense of purpose, Diederick is a staunch advocate for inclusive
finance, striving to empower future generations through AdviceRobo’s AI-driven embedded
finance solutions. As a member of Ikano Bank’s Digital, Business & IT Committee, he
oversaw the complete transformation of this traditional bank into a neo-bank over a span
of six years. As Chairman of the Digital, IT & Sustainability Committee at Ikano Bank, he
also champions ESG initiatives, driving efforts to shape a more sustainable financial future.
Beyond his corporate endeavors, Diederick is deeply committed to advancing knowledge
and understanding in his field. He completed his master’s degree at Erasmus University in
Rotterdam and holds an MBA from IMD in Lausanne. His academic PhD-pursuits delve
into human-centered AI, exploring the intersection of advanced technologies, next gen
behavior and evolving business & innovation models. He has published scientific papers
in leading journals such as the Journal of Risk Management in Financial Institutions, The
European Journal of Finance, The Journal of Accounting & Finance, and the Journal of
Financial Transformation. As a visiting professor at esteemed institutions like Eindhoven
University of Technology (Intelligent Agents) and Jheronimus Academy for Data Science
(Advanced Marketing & Risk Management), he shares his expertise, igniting curiosity and
inspiring the next generation of innovators.
244