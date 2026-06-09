Spectrum of Engineering Sciences
ISSN (e) 3007-3138 (p) 3007-312X
INNOVATIONS IN UI/UX DESIGN OF MOBILE APPLICATIONS:
TRENDS, PRACTICES AND CHALLENGES
Afshan Jamal*1, Dr. Shazia Hashmat2
*1PhD Scholar, Department of Communication and Media Studies, and Lecturer, Department of Computer Arts,
Fatima Jinnah Women University, Rawalpindi,
2Department of Communication and Media Studies, Fatima Jinnah Women University, Rawalpindi,
1afshanjam@fjwu.edu.pk,*2shazia.hashmat@fjwu.edu.pk
DOI: https://doi.org/10.5281/zenodo.15478961
Abstract
Keywords As digital experiences rely more on mobile apps, the demand for interfaces and
Mobile UI/UX Design, User- experiences that are both intuitive and focused on users has rapidly increased.
Centered Design (UCD), Users now require more than conventional design approaches can provide in
Usability, Accessibility, Inclusive delivering responsive, accessible, and intelligent interactions. This study follows
Design, Review approach using PRISMA method, it covers 20 peer-reviewed publications
Artificial Intelligence (AI), issued from 2017 to 2024, which met our specific selection criteria. This review
Personalization, Adaptive evaluates the latest advancements, important trends, leading practices, and
Interfaces, Immersive Technologies, ongoing problems in mobile UI/UX design, with a focus on themes including
Augmented Reality (AR), Virtual personalization, usability, accessibility, immersive technologies, and AI-driven
Reality (VR), Voice User approaches. The paper identifies ways in which AI is reshaping design,
Interfaces encompassing AI-powered personalization, adaptive interfaces, predictive analysis
of user actions, and automated design generation as significant trends.
Article History Furthermore, AR, VR, and VUIs are found to boost user interest and accessibility
Received on 13 April 2025 by providing richly engaging and non-intrusive interactions. The results point to
Accepted on 13 May 2025 UCD, iterative testing, performance optimization, and a commitment to inclusive
Published on 21 May 2025 accessibility standards as major principles. Frameworks that support multiple
platforms, for example Flutter and React Native, are becoming the preferred
Copyright @Author choice for delivering both consistency and scalability. Despite the important
Corresponding Author: * enhancements noted, challenges persist mainly in the form of restricted screen sizes,
Dr. Shazia Hashmat increased mental demands, keeping designs consistent across platforms, and
incorporating advanced technologies. This review summarizes a comprehensive
framework aimed at various players in the mobile UI/UX field, illustrating the
value of interdisciplinary efforts, responsible design, and flexible approaches for
advancing mobile UI/UX development.
INTRODUCTION
With the rapid advancements made in the mobile using the mobile first approach and testing with
technology has changed user expectations and emerging technologies like AR and VR to improve
associated demands to evolve their mobile User experiences (Okonkwo, 2024). Further, data driven
Interface along with User Experience (UX) design. approaches and including the design principle of
Currently in mobile design, efforts are made to make interface has changed during the creation of the
the user experience more personal and innovative, interface for varying user demographics and user
https://sesjournal.com | Jamal & Hashmat, 2025 | Page 637

Spectrum of Engineering Sciences
ISSN (e) 3007-3138 (p) 3007-312X
preferences (Bhimanapati et al., 2024). Besides, there VR in mobile apps, designers should move beyond
has been more and more continuous demand for old UI/UX ways and look for new ways to interact.
smooth and easy user interfaces, which are essential Finally, MR technologies are investigated to create
for users’ competent UI/UX approaches to the experiences that combine the digital and physical
features of the users’ behaviour and technological world together (Milgram & Kishino, 1994).
innovations (Krug, 2014). The UI/UX design is now key to making digital
UI/UX on mobile has developed a lot, switching experiences more accessible and available to users of
from plain interfaces to ones that are really dynamic all skill levels and literacy backgrounds. The concepts
and engage users. This new development is partly of inclusive design propose and emphasize building
fueled by mobile devices being used more and more UIs that work for individuals with special needs,
for activities such as communication, shopping, such as screen readers and adjustable font sizes
studying, and having fun. Because users now expect (Norman, 2013). In addition, making mobile
seamless digital experiences, designers have to applications more usable in a global context requires
develop new and creative ideas for making their apps attention to the needs of people who are not literate
stay up-to-date and popular. AI and ML now support and those from many cultures (Marcus, 2013). Since
the development of smart UX/UI systems that accessibility rules are getting tougher, it is now the
identify what users like and deliver a more designer’s job to include accessibility features from
personalized experience to them (Shneiderman, the early stages of design (W3C, 2021). Boosting
2016). readability and user engagement is especially
A major part of modern mobile design is focusing important for applications with a range of users, and
everything on a mobile-first perspective. With this choices in color psychology and typography have a
thinking, designs are created specifically for mobile major influence (Lupton, 2014).
devices and smoothly adapted for bigger screens, Moreover, the process of designing mobile
making things consistent for users (Marcotte, 2010). application interfaces has grown to incorporate the
Following a mobile-first mindset means designing for concepts of sustainability. With energy efficiency
simplicity, reactivity, and simple load messages to gaining importance, designers are looking into
improve use and user engagement (Tullis & Albert, solutions to improve app performance while
2013). Using Progressive Web Apps (PWAs) and decreasing the number of resources consumed
adaptive design, developers are now able to make (Garett et al., 2019). The use of techniques like dark
apps that have an almost native experience, and at mode, power-saving animations, and lightweight
the same time, keep good performance and frameworks encourages energy-efficient mobile
accessibility (Google Developers, 2022). design, therefore extending device life. In addition,
Furthermore, micro interactions are necessary in Kolko (2015) states that sustainability-driven design
UI/UX, as little animations and responsive cues give choices can contribute to better usability and help
a noticeable boost to user satisfaction (Saffer, 2013). reduce user stress in quality interfaces.
A big development is connecting mobile UI/UX In this review paper, the focus is on supplying
design to cutting-edge mobile technologies like AR integral knowledge regarding methodologies
and VR. As well as changing how people interact including responsive interface design, immersive
with apps, these technologies make it easier to mix technologies, and user-driven design procedures that
the digital and physical worlds (Azuma, 1997). In the have been proven successful in the mobile app
retail, education, and healthcare sectors, AR sector. Through a review of cutting-edge research,
applications are being used so that users can see this paper presents recommendations that assist
products, receive instant feedback, and learn with designers, developers, and researchers in improving
educational content in interesting ways (Billinghurst usability and user engagement of mobile
et al., 2015). In the same way, VR has made a big applications.
difference to gaming and training applications by
giving users more realistic and enjoyable simulations
(Slater, 2017). With the increasing use of AR and
https://sesjournal.com | Jamal & Hashmat, 2025 | Page 638

Spectrum of Engineering Sciences
| ISSN (e) 3007-3138 (p) 3007-312X  |     |     |     |     |
| --------------------------------- | --- | --- | --- | --- |

1.1 Problem Statement  mobile  UI/UX  design.  The  methodology  involves
The development of mobile technology is directly  four key stages: Identification, Screening, Eligibility,
associated with users’ rising expectations for UI/UX  and Inclusion. Due to small sample size a review
that is seamless, intuitive, and engaging. It is difficult  approach has been adopted to synthesis the selected
| for standard interfaces to satisfy these standards, so  |                       |                 | literature.   |     |
| ------------------------------------------------------- | --------------------- | --------------- | ------------- | --- |
| creative  solutions                                     | in  personalization,  | accessibility,  |               |     |
and  technologies  such  as  AI,  AR,  and  VR  are  2.1 Identification
needed.  Ensuring  that  all  kinds  of  users  with  A review approach was used to look for  relevant
different  devices  can  access  products  remains  articles  across  academic  and  industry  databases,
challenging.  This  paper  has  adopted  a  review  specifically  Google  Scholar,  IEEE  Xplore,  ACM
approach aiming to synthesize current trends, best  Digital  Library,  ScienceDirect,  and  SpringerLink.
practices, and ongoing challenges that are shaping  The  search  was  conducted  using  important  terms
the landscape of modern mobile UI/UX design.  such  as  "innovations  in  mobile  UI/UX  design,"
|     |     |     | "trends in UI/UX design," "principles of UI/UX,"  |     |
| --- | --- | --- | ------------------------------------------------- | --- |
1.2  Research Objectives  and  "challenges  in  UI/UX  design."  Boolean
O : To examine the most prevalent trends currently  operators (AND, OR) were applied to the keyword
1
shaping mobile UI/UX design.  combinations  in  order  to  collect  only  the  most
O : To explore emerging design approaches used in  relevant articles for analysis. Besides, the reference
2
mobile UI/UX.  lists of selected articles were checked manually to
O :  To  analyze  best  practices  that  contribute  to  retrieve additional relevant studies.
3
| effective mobile UI/UX design.                       |     |     |                |     |
| ---------------------------------------------------- | --- | --- | -------------- | --- |
| O : To investigate the primary challenges in mobile  |     |     | 2.2 Screening  |     |
4
UI/UX.  A total of (243) articles were present after the first
|     |     |     | search. The reference management software was used  |     |
| --- | --- | --- | --------------------------------------------------- | --- |
1.3  Research Questions  to identify and eliminate duplicate articles, leaving
RQ : What are the most prevalent trends in mobile  230 unique ones. Titles and abstracts were initially
1
UI/UX design?  checked to make sure the papers were relevant to the
RQ : What are the emerging design approaches in  research topic. This stage excluded any study that did
2
mobile UI/UX?  not address mobile UI/UX trends, innovations, or
| RQ : What are the best practices currently being  |     |     | challenges.   |     |
| ------------------------------------------------- | --- | --- | ------------- | --- |
3
| adopted in mobile UI/UX design?                      |     |     |                  |     |
| ---------------------------------------------------- | --- | --- | ---------------- | --- |
| RQ : What are the key challenges faced by designers  |     |     | 2.3 Eligibility  |     |
4
in creating effective mobile UI/UX?  Each  of  the  remaining  papers  were  critically
|     |     |     | examined full-ext review to assess their methodology,  |     |
| --- | --- | --- | ------------------------------------------------------ | --- |
2.  Methodology  significance, and value to the field. The inclusion
This study adopts a review methodology to analyze  and exclusion criteria specified in Table 1 were used
recent  advancements,  trends,  and  challenges  in  to evaluate the studies. This selection process only
mobile UI/UX design. According to Mallett et al.  selected  peer-reviewed  journal  articles,  conference
(2012), the practice of conducting   papers, and industry reports published between 2017
reviews started in the social sciences to attain a more  and 2024. Only articles that clearly reported their
comprehensive understanding of topics. Such studies  findings and methods were selected.
| play a major role in advancing and furthering the  |     |     |     |     |
| -------------------------------------------------- | --- | --- | --- | --- |
application of evidence in policymaking. Owing to  2.4 Eligibility Criteria
the detailed procedures involved, they have assumed  Following the full-text review, a final group of [20]
a leading position in conventional literature review  studies were chosen for the review. The studies were
(Ali, 2020a, b). Thus, this study employs a review  sorted  and  grouped  according  to  themes  that
approach  guided  by  the  PRISMA  framework  to  included usability, personalization, accessibility, and
examine  trends,  innovations,  and  challenges  in  immersive technologies. Key advances, best practices,
https://sesjournal.com                 | Jamal & Hashmat, 2025 |  Page 639

Spectrum of Engineering Sciences
ISSN (e) 3007-3138 (p) 3007-312X
and difficulties in mobile UI/UX design were recognized by synthesizing the research findings.
Table1: Inclusion and Exclusion Criteria
Criteria Inclusion Criteria Exclusion Criteria
Studies focusing on mobile UI/UX trends, Studies unrelated to mobile UI/UX or
Scope
principles, innovations, and challenges focusing solely on desktop interfaces
Publication Peer-reviewed journal articles, conference Non-peer-reviewed articles, blogs, or
Type papers, and industry reports opinion pieces
Time Frame Published between 2017 and 2024 Studies published before 2017
Empirical studies, systematic reviews, and Studies lacking methodological rigor or
Methodology
case studies anecdotal evidence
Following flow chart explains the process of article selection for review:
Identification of studies via Databases and Registers
n
o Records identified from*: Records removed before screening:
it
a
c Databases (n =218)
if
itn
Other sources (n =25) Duplicate records removed: (n =230)
e
d
I
Records screened Records excluded**
(n = 230) (n =185)
g
n
in
e Full text articles assessed for Full text articles excluded: (n =15)
e
r
c S eligibility (n =45) Reason1: Not focused on mobile
UI/UX (n =8)
Reason2: Poor methodology (n =7)
d Studies included in review
ud
lc n e (n =20)
I
Fig 1. PRISMA Flow Diagram for Study Selection in Review
3. Review of Selected Studies and engaging. Because of this, the innovation in
Mobile applications have gained importance as a mobile UI/UX design has occurred at a rapid pace.
major means through which people communicate, The addition of AI, AR, VR, and voice-based
work, shop, and entertain themselves. With the rise technologies to mobile design has led to revised
in mobile device use, delivering usable and intuitive principles and introduced specific expectations from
design experiences becomes more and more users. This review examines major trends,
necessary. Unlike desktop software, mobile apps development practices, and on-going challenges in
must be developed to work with smaller screen sizes, mobile UI/UX design.
touch controls, and the many different capabilities of
various devices. At the same time, people expect that
their mobile interactions will be tailored, smooth,
https://sesjournal.com | Jamal & Hashmat, 2025 | Page 640

Spectrum of Engineering Sciences
ISSN (e) 3007-3138 (p) 3007-312X
3.1 PREVALENT TRENDS IN MOBILE UI/UX 2024). Certainly, these design patterns benefit
DESIGN multitasking and accessibility needs, yet they
3.1.1. Personalization and Adaptive Interfaces introduce unique problems for interpreting
User expectations are being remodeled by language, dealing with context, and delivering
personalization technologies on a variety of mobile auditory cues.
systems. Using artificial intelligence (AI) and
machine learning (ML), mobile applications are able 3.1.4. Dark Mode and Minimalist Design
to collect and analyze user choices, past behavior, What started as a unique option, dark mode is
geolocation information, and additional context to currently accepted as the standard in modern app
provide content and suggestions that match design. Such a feature creates a modern style,
individual needs. Applications such as Netflix and minimizes strain on the eyes in dim light, and helps
Spotify make use of customized recommendations to conserve battery power on OLED devices. In
create a unique and tailored user experience for their addition, minimalist design incorporates simplicity
users (Okonkwo, 2024; Fazil et al., 2024). Adaptive by making use of clean fonts, generous spacing,
interfaces elevate this by automatically showing or simple icons, and displaying only the essential
moving elements of the user interface as necessary in features. As a result, users are able to think less and
various real-time situations. An illustration of this navigate the interface faster, which also helps those
would be a fitness app that updates both layout and with accessibility needs (Abdellrazik et al., 2024;
offered features depending on the user’s location: “Deconstructing Design Trends,” 2024). When used
home, gym, or outside. Enhanced adaptability alongside each other, these visual styles improve
smoothes out the app’s interaction, decreases user usability and continue to present a fashionable and
difficulties, and greatly contributes to overall user elegant look.
enjoyment.
3.1.5. Micro-interactions and Animated Feedback
3.1.2. Augmented and Virtual Reality Integration Micro interactions are short animations that appear
By bringing together AR and VR, mobile apps are as a result of user interactions, including changes like
able to blend digital and real-world experiences a heart icon pulsing after being tapped and seeing a
seamlessly. AR presents digital items in a mobile progress bar animate as files are uploaded. Because
device's live view, as evidenced by applications such they offer immediate acknowledgment, assist in
as IKEA Place and Pokémon GO. On the other guiding interactions, and explain the app's state, such
hand, VR technologies deliver highly immersive animations help dramatically improve the app's
digital experiences and are frequently adopted for subjective responsiveness (Tanwar et al., 2022). In
applications in education, virtual tours, and therapy addition, they contribute to making the app feel
(Fazil et al., 2024; Ghosh & Dubey, 2024; Okonkwo, more vibrant and focused on the end user.
2024). Integration of these technologies enhances
engagement and provides the chance to perform 3.1.6. Inclusive and Accessible Design
context-sensitive actions not possible before, such as The practice of design now understands that
testing a virtual outfit or doing a virtual classroom accessibility and inclusivity are essential features. In
visit from anywhere. order to serve users with visual, auditory, or motor
disabilities, designers are growing the use of tools
3.1.3. Voice User Interfaces (VUIs) such as screen readers, voice navigation, adjustable
Voice User Interfaces (VUs) are becoming more text sizes, and high-contrast color palettes (Faudzi et
common since they offer users easier and hands-free al., 2024; Ghosh & Dubey, 2024). Design that is
ways of interacting. Siri, Google Assistant, and Alexa inclusive meets both regulatory and ethical
are examples of AI assistants that enable users to expectations, while also increasing usability and
dictate messages, search for information, and operate accessibility for all users, including people who face
internet-of-things (IoT) devices without the need to disabilities on a temporary or situational basis.
use the screen (Ghosh & Dubey, 2024; Paneru et al.,
https://sesjournal.com | Jamal & Hashmat, 2025 | Page 641

Spectrum of Engineering Sciences
ISSN (e) 3007-3138 (p) 3007-312X
3.1.7. Mobile-First Design 3.2.3. Gestural Interaction
Mobile-first design starts by considering the Gestural interaction has taken the place of
restrictive features of small-screen devices, like touch traditional tap-and-click style interfaces because it is
screens and variable internet speed, and only then more natural and easier to learn. Because users are
expands the design to fit tablets and computers. This now adept at using touch interfaces, gestures such as
method makes certain that the primary functions are swiping, pinching, and long-pressing offer smooth
highlighted, navigation stays simple, and usability is and engaging form of mobile navigation (Kadaskar,
improved for mobile devices. As mobile Internet use 2024). Reducing the amount of visible UI
passes desktop activity worldwide, using this components because of gestural inputs enables users
approach yields interfaces that meet the needs of to carry out tasks more efficiently. Activating quick
current users more effectively (Okonkwo, 2024). This actions like delete or archive by swiping in email and
focus on easy-to-use and clear interfaces inspires messaging apps is an example that boosts both the
better design discipline and allows for new speed and user interaction with the application. If
innovative approaches. handled correctly, gestural features make mobile
interactions more effective and pleasant.
3.2. EMERGING DESIGN APPROACHES
3.2.1. Design Thinking 3.2.4. Cross-Platform Design
Design thinking emphasizes the user by fostering With the aid of frameworks like Flutter and React
empathy, encouraging creative thinking, and Native, developers are able to develop apps for
emphasizing rapid prototyping as well as repeated multiple operating systems from a single source code.
testing. This method assists mobile UI/UX teams in This method ensures that the look and feel, as well
exploring how users act, what they feel, and what as the functionality, are comparable between iOS
problems they face before making any solutions and Android, while also minimizing the costs and
(Aprilia et al., 2024). Algifahri et al., 2024). The non- effort involved in development (Ali et al., 2024).
sequential and repetitive character of design thinking From a design perspective, cross-platform UI libraries
supports ongoing refinement, thus resulting in enable companies to keep their brand visible while
designs that look good and are appropriate for a wide also making customizations that fit the expectations
range of users. Design thinking is especially helpful of users on different platforms. Such an approach is
in mobile app development because it can rapidly most helpful for startups and organizations that need
respond to user feedback and the evolving nature of to efficiently serve a wide range of users.
user requirements.
3.3. BEST PRACTICES IN MOBILE UI/UX
3.2.2. AI-Driven Design DESIGN
By automating routine work and giving new insights, 3.3.1. User-Centered Design (UCD)
artificial intelligence is fundamentally changing how In User-Centered Design, the needs and experiences
designers work. Both Adobe Sensei and AI-enhanced of the user drive each stage of the design. In order to
Figma plugins make it easier for designers by understand users’ actual behaviors and needs, early-
speeding up tasks related to layout generation, stage research, including interviews, surveys, and
suggesting appropriate color schemes, and persona development, is conducted (Fazil et al.,
conducting accessibility checks as mentioned by 2024; Aprilia et al., 2024). The use of prototypes and
(Kamnerddee et al., 2024). Most importantly, AI uses usability testing allows for validating design choices
user data to predict how people will act, offer so that they correspond to what users expect. UCD
personalized content, and assess design effectiveness, helps to minimize user difficulties, increases user
which frees designers from routine work and gives satisfaction, and guarantees the app's continuous
them more time for creative thinking. As the number development in response to honest user input, rather
of mobile apps increases, AI-driven design than presumptions.
contributors to faster adaptation and customized
user experiences.
https://sesjournal.com | Jamal & Hashmat, 2025 | Page 642

Spectrum of Engineering Sciences
| ISSN (e) 3007-3138 (p) 3007-312X  |     |     |
| --------------------------------- | --- | --- |

3.3.2. Iterative Testing and Feedback  3.4.  KEY  CHALLENGES  IN  MOBILE  UI/UX
| It is important that mobile UI/UX remains flexible  | DESIGN  |     |
| --------------------------------------------------- | ------- | --- |
and responds well to new user needs. Designers can  3.4.1. Small Screen Size and Limited Real Estate
use the feedback from A/B tests, usability sessions,  Mobile  screens'  small  dimensions  create  an
and  click  tracking  to  understand  real-time  user  important restriction for designers. It is important
interactions  (Aprilia  et  al.,  2024;  Algifahri  et  al.,  for designers to present only the key content and
2024). Such an agile strategy allows for more rapid  functionality.  Collapsible  menus,  icon-based
prototyping  and  design  changes,  which  together  navigation,  and  the  use  of  progressive  disclosure
decrease the time it takes to launch the app and  make it possible to keep the interface simple and
better connect design with users’ actions.   highlight  what  matters  most  (Punchoojit  &
|     | Hongwarittorrn, 2017). It is necessary to keep the  |     |
| --- | --------------------------------------------------- | --- |
3.3.3. Accessibility and Inclusivity  interface easy to use even with the constraints of
Inclusive design makes certain that all types of users,  limited screen space.
| regardless of ability or background, can comfortably  |     |     |
| ----------------------------------------------------- | --- | --- |
use  digital  products.  Some  crucial  techniques  3.4.2. Cognitive Load and Information Overload
involves supporting screen readers, supplying text in  High levels of complexity or too much information
a  format  that  scales  easily,  including  voice-based  can cause users to become frustrated and stop using
interactions, and making use of high-visual contrast  an  app.  Faudzi  et  al.  (2024)  demonstrated  that
(Faudzi et al., 2024). By designing with accessibility  cognitive  load  can  be  managed  with  the  help  of
in  mind,  a  product  becomes  more  usable  for  hierarchical  layouts,  onboarding  supports,  and
everyone,  including  those  who  do  not  have  compact  content.  Design  can  support  focused
disabilities, like people who rely on captions in noisy  interaction  by  relying  on  whitespace,  icon-based
places as well as those who are hard of hearing.   design,  and  brief  micro-interactions  to  support
| 3.3.4. Performance Optimization                         | smooth navigation.   |     |
| ------------------------------------------------------- | -------------------- | --- |
| User attrition is largely impacted by how well the app  |                      |     |
performs. If an app has lag, slow load times, or heavy  3.4.3. Cross-Platform Consistency
visuals, it can cause users to become annoyed and  Ensuring that a brand and user experience are the
uninstall  the  app.  Presenting  reduced  asset  sizes,  same across multiple platforms and devices is not
making fewer requests of the server, and using local  easy, owing to the variety of design practices and
caching  all  help  make  the  app  faster  and  more  technical  support.  Adopting  a  unified  system  of
reactive  (Gada,  2024).  Above  this,  code-based  components and designs, developers must also adjust
enhancements are important for achieving smooth  layouts to match the behavior users expect from each
animations and transitions, and they are particularly  device (Ali et al., 2024). It is important for designers
significant for users with older or low-performance  to carefully weigh consistency and responsiveness to
| devices.   | specific contexts simultaneously.   |     |
| ---------- | ----------------------------------- | --- |
|            |                                     |     |
3.3.5. Continuous Feedback Loops  3.4.4. Technical Implementation and Performance
Good mobile UX should continue after deployment.  Developers need to consider how advanced features
Regular user feedback from in-app reviews, analytics,  such  as  animations,  AR/VR,  and  real-time  data
and behavior tracking is crucial for finding trouble  visualization will work technically. Such unoptimized
spots and making useful improvements (Fazil et al.,  features  might  cause  lag,  make  the  interface
2024;  Gada,  2024).  Because  of  this  constant  unresponsive, and negatively affect battery life. For
feedback loop, the app remains relevant, promptly  successful translation of creative ideas into effective
responsive, and in line with competitive standards.  applications, designers and developers must closely
|     | work together (Fazil et al., 2024).   |     |
| --- | ------------------------------------- | --- |
|     |                                       |     |
|     |                                       |     |
|     |                                       |     |
https://sesjournal.com                 | Jamal & Hashmat, 2025 |  Page 643

Spectrum of Engineering Sciences
ISSN (e) 3007-3138 (p) 3007-312X
3.4.5. Evolving User Expectations currently used by industry. Personalized designs and
As users interact with more complex apps, their interfaces, which include AR and VR technology, are
standards for user interfaces tend to go up. Faster, key trends to enhance the experience of users. They
smarter, and more intuitive interfaces are required by coincide with the need to create apps that meets
users, whose preferences are often under the users enjoy and find easy to use. The reviewed
influence of socio-cultural trends. It is important for literature (Okonkwo, 2024; Fazil et al., 2024 and
designers to keep up with changes in user behavior, Ghosh & Dubey, 2024) shows personalized
new technologies, and global standards to guarantee interfaces improve usability and satisfaction by
they remain relevant (Ghosh and Dubey, 2024). automatically adjusting to each user. Also, the use of
AR and VR expands how people interact, mainly in
4. Discussion and Analysis retail, education, and the tourism sector.
The findings indicate mobile UI/UX design is Nevertheless, AI-driven design is sometimes faulty
changing rapidly as a result of advances in due to the difficulty in implementing it well with
technology, changed user expectations, and a focus limited device power and the risks of motion
on inclusive and useful design processes. The issue of sickness or thinking overload. The increased use of
these changes and their effect on industry is VUIs and gesture-control makes it much easier for
examined and compared with what is already users to perform tasks without the need for manual
happening. navigation. Kadaskar (2024) highlights how gestures
can reduce visual clutter and improve task efficiency,
4.1 Synthesis of Emerging Trends and Approaches though their effectiveness heavily depends on user
This synthesis explains emerging trends and familiarity and context-awareness.
approaches and compares them to the practices
Table 2: Emerging Trends and Approaches in Mobile UI/UX Design
Focus Area Key Insights Implications for Design Representative
Studies
Personalization & Enhances user engagement by Designers must implement real- Okonkwo (2024),
Adaptive Interfaces tailoring content and interfaces time data-driven customization Fazil et al. (2024)
based on user preferences and without overwhelming users.
behavior.
AR/VR Integration AR/VR creates immersive Requires high-performance Ghosh & Dubey
environments that are devices and careful UX to avoid (2024), Fazil et al.
impactful in education, retail, disorientation and overload. (2024)
and tourism.
Voice User Enables hands-free interaction, Demands robust NLP and clear Paneru et al.
Interfaces (VUIs) beneficial for accessibility and user feedback systems to ensure (2024), Ghosh &
multitasking. effective use. Dubey (2024)
Gesture-Based Natural gestures reduce Effectiveness depends on user Kadaskar (2024)
Interaction reliance on buttons and visual familiarity, context awareness,
clutter, improving task flow. and intuitive mapping.
Dark Mode & Enhances readability, saves Best suited for content-rich apps; UID Design
Minimalist Design battery, and emphasizes key UI must balance aesthetic with Trends (2024)
elements. functional contrast.
Microinteractions Small animations and Must be subtle and purposeful UID Design
responses enhance user to avoid distraction or Trends (2024)
satisfaction and provide clear performance issues.
feedback.
https://sesjournal.com | Jamal & Hashmat, 2025 | Page 644

Spectrum of Engineering Sciences
| ISSN (e) 3007-3138 (p) 3007-312X  |     |     |     |     |
| --------------------------------- | --- | --- | --- | --- |

Mobile-First Design  Prioritizes small-screen  Important for global audiences   Okonkwo (2024)
|     | usability, ensuring core         | with mobile-dominant internet  |     |     |
| --- | -------------------------------- | ------------------------------ | --- | --- |
|     | functionality is accessible and  | access.                        |     |     |
optimized.
|     |     |     |     |     |
| --- | --- | --- | --- | --- |
4.2 Comparative Analysis of Design Approaches  combines design thinking and AI tools could lead to
Both  design  thinking  and  AI-driven  design  are  the  best  way  to  provide  responsive  and  efficient
unique approaches to innovation. Design thinking is  mobile UI/UX. By using gestural and cross-platform
focused  on  empathy  and  improving  processes  modes,  mobile  development  is  reaching  maturity.
iteratively, whereas AI-driven design uses automation  Although  Flutter  allows  the  same  experience  on
to make things more scalable (Aprilia et al., 2024;  different devices, balancing their performance and
Kamnerddee et al., 2024). An approach that   behavior is still a big challange(Ali et al., 2024).

Table 3: Design Approaches in Mobile UI/UX
Design  Core Characteristics  Design Implications  Representative Studies
Approach
Design  Empathy-led, user-centered, and  Encourages deep user  Aprilia et al. (2024),
Thinking  iterative problem-solving  understanding and creative  Algifahri et al. (2024)
|     | approach.  | exploration; ideal for complex  |     |     |
| --- | ---------- | ------------------------------- | --- | --- |
challenges.
AI-Driven  Uses machine learning and  Enhances speed and scalability but  Kamnerddee et al.
Design  automation for layout  may risk detachment from nuanced  (2024)
|     | generation, behavior prediction,  | user needs.  |     |     |
| --- | --------------------------------- | ------------ | --- | --- |
and analysis.
Hybrid  Combines AI tools with human- Balances innovation and empathy;  Aprilia et al. (2024),
Approach  centered methodologies (e.g.,  allows responsive yet grounded  Kamnerddee et al.
|     | design thinking).  | design processes.  | (2024)  |     |
| --- | ------------------ | ------------------ | ------- | --- |
Gestural  Replaces traditional UI elements  Reduces visual clutter and creates  Kadaskar (2024)
Interaction  with touch or motion-based  more immersive experiences; needs
|     | input.  | user training.  |     |     |
| --- | ------- | --------------- | --- | --- |
Cross- Develops UI/UX that functions  Improves reach and consistency;  Ali et al. (2024)
Platform  uniformly across iOS, Android,  challenges include platform-specific
| Design  | and web environments.  | performance tuning.  |     |     |
| ------- | ---------------------- | -------------------- | --- | --- |
|         |                        |                      |     |     |
4.3.  Evaluation  of  Best  Practices  and  Their  application is not the same, especially when teams
Implementation  are  small  or  when  deadlines  are  tight.  It  is  also
User-centered  design  and  the  use  of  multiple  important to focus on accessibility and performance.
prototypes are still considered best practices that lead  Research  shows  that  despite  companies  knowing
to  users’  needs  being  met  by  design.  Frequent  about accessibility, many mobile apps do not live up
updates, existing demo features, and relying on data  to  these  requirements  (Faudzi  et  al.,  2024).  As  a
are important, according to several studies (Fazil et  result,  more  regulations  and  stricter  designs  are
al., 2024; Algifahri et al., 2024). Real-world   needed  to  ensure  that  mobile  apps  are  fully
|     |     | accessible.  |     |     |
| --- | --- | ------------ | --- | --- |

https://sesjournal.com                 | Jamal & Hashmat, 2025 |  Page 645

Spectrum of Engineering Sciences
| ISSN (e) 3007-3138 (p) 3007-312X  |     |     |     |     |
| --------------------------------- | --- | --- | --- | --- |

Table 4: Best Practices and Their Implementation in Mobile UI/UX Design
Best Practice  Core Principle  Implementation Insights  Representative
Studies
User-Centered  Focuses on designing interfaces  Widely accepted but inconsistently  Fazil et al. (2024),
Design (UCD)  that align with real user needs,  applied in smaller or resource- Aprilia et al. (2024)
|     | preferences, and behaviors.  | limited teams.  |     |     |
| --- | ---------------------------- | --------------- | --- | --- |
Iterative Testing  Continuous testing and refining  Enables agile development; often  Algifahri et al.
& Feedback  based on user input and real-world  skipped under tight timelines or  (2024), Aprilia et al.
|     | usage.  | budget constraints.  | (2024)  |     |
| --- | ------- | -------------------- | ------- | --- |
Continuous  Real-time user data and analytics  Supports responsive updates but  Gada (2024), Fazil et
Feedback Loops  used to refine and evolve design  requires infrastructure and active  al. (2024)
|     | features.  | monitoring.  |     |     |
| --- | ---------- | ------------ | --- | --- |
Accessibility &  Ensures design is usable by people  Still under-prioritized in practice;  Ghosh & Dubey
Inclusivity  of all abilities, across  lack of standardized enforcement  (2024), Faudzi et al.
|     | demographics.  | and awareness.  | (2024)  |     |
| --- | -------------- | --------------- | ------- | --- |
Performance  Prioritizes speed, responsiveness,  Directly impacts retention;  Gada (2024)
Optimization  and efficiency in UI behavior.  essential for emerging markets
with device/network limitations.
|     |     |     |     |     |
| --- | --- | --- | --- | --- |
4.4. Key Challenges in Practice  designers  to  make  sure  that  elements  work
It is often mentioned in the literature that designers  consistently on all platforms and yet  fit  with the
find  it  hard  to  ensure  good  design,  smooth  native  features  of  each  one.  It  is  becoming  a
performance,  and  useful  functions  on  mobile  challenge for UI/UX designers as users learn about
devices.  Due  to  the  limited  display  and  device  new trends and apps. Since user expectations are
differences, designers have to focus on what matters  quickly  evolving,  designers  should  be  alert  and
most  and  use  smart  strategies  (Punchoojit  &  change  along  with  them,  requiring  continuous
Hongwarittorrn, 2017). This situation requires   practice and interaction with users (Ghosh & Dubey,
|     |     | 2024).   |     |     |
| --- | --- | -------- | --- | --- |

Table 5: Challenges in Mobile UI/UX Practice
| Challenge  | Description  | Design Impact  | Representative  |     |
| ---------- | ------------ | -------------- | --------------- | --- |
Studies
Limited Screen  Mobile interfaces have spatial  Requires prioritization, hierarchy,  Punchoojit &
Real Estate  constraints that limit content and  and minimalist layout strategies.  Hongwarittorrn
|     | feature density.  |     | (2017)  |     |
| --- | ----------------- | --- | ------- | --- |
Cross-Platform  Designing for iOS, Android, and  Demands adaptable components  Ali et al. (2024)
Consistency  web with uniform experiences can  and design systems that respect
|     | be complex.  | native behaviors.  |     |     |
| --- | ------------ | ------------------ | --- | --- |
Technical  High resource usage of AR and AI  Needs optimization techniques  Fazil et al. (2024),
Integration of  features can degrade performance  and fallback strategies for low-end  Ali et al. (2024)
| AR/AI  | or cause lags.  | devices.  |     |     |
| ------ | --------------- | --------- | --- | --- |
Evolving User  Users continuously expect modern,  Requires constant market  Ghosh & Dubey
Expectations  trend-aligned, and personalized  research, design updates, and  (2024)
|     | experiences.  | innovation cycles.  |     |     |
| --- | ------------- | ------------------- | --- | --- |
|     |               |                     |     |     |
|     |               |                     |     |     |
|     |               |                     |     |     |
https://sesjournal.com                 | Jamal & Hashmat, 2025 |  Page 646

Spectrum of Engineering Sciences
ISSN (e) 3007-3138 (p) 3007-312X
4.5. Implications for Designers And Developers should collaborate and rely on user feedback to make
Integrating modern technologies and techniques is adaptable and high performing applications. It is
beneficial, but designers and engineers should work clear from the data that ease of use and the
as a team and understand the key concepts behind accessibility of apps are still essential for a positive
mobile UI/UX design. Designers and developers user experience.
Table 6: Implications for Designers and Developers
Implications Core Insight Actionable Recommendation Relevant
Discussion
Need for Effective UI/UX requires Foster cross-functional Synthesis of
Interdisciplinary cooperation across design, teamwork through agile multiple studies
Collaboration development, and data analysis methods and shared tools.
roles.
Balancing Emerging tech (e.g., AI, AR) can Innovations must enhance, not Fazil et al. (2024),
Innovation with compromise usability or overshadow, core functionality Faudzi et al. (2024)
Usability accessibility if poorly and ease of use.
implemented.
User Satisfaction Despite trends, fundamental Never neglect basic UX pillars Faudzi et al. (2024),
Hinges on Core design values like accessibility, when adopting novel tools or Gada (2024)
Principles clarity, and performance remain trends.
vital.
Continuous Rapidly evolving user expectations Invest in user research, UI Ghosh & Dubey
Learning & Trend demand constant upskilling and audits, and participation in (2024), Aprilia et
Awareness adaptation. design communities and al. (2024)
workshops.
5. Conclusion implemented combined with accessibility and other
This research has looked into the changes happening usability habits, these new methods produce
in mobile UI/UX design and the timeless principles applications that are more suitable for everyone and
that are still significant. It is clear from the research pleasing to use.
that more focus is now placed on personalization, However, significant challenges remain. It is still a
AR/VR, and using gestures and voice commands for challenge because mobile gadgets have limitations,
mobile user experiences. The study has shown that cross-platform development depends on
developers are now focusing more on providing understanding several factors, and keeping up with
applications that reflect and respect users’ feelings user tastes and trends is not easy for everyone
and situations. The findings also show that the main involved. Collaboration, experimenting with new
tools in mobile development today are design ideas, and putting emphasis on inclusive design will
thinking and AI-based technologies. When be required to bridge innovation and usability.
Table 7: Selected Literature
Article Title Author(s) Journal Name Year Theme
Assessment of User Experience (UX) Journal of Mobile Personalization,
Okonkwo, C. 2024
Design Trends in Mobile Applications Computing Mobile-First Design
Evaluating the Impact of Emerging International Journal Personalization,
Technologies on Mobile User Fazil, M., et al. Software Engineering and 2024 Performance
Experience Computer Science Optimization
https://sesjournal.com | Jamal & Hashmat, 2025 | Page 647

Spectrum of Engineering Sciences
| ISSN (e) 3007-3138 (p) 3007-312X  |     |     |     |     |     |     |     |     |     |     |     |
| --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|     | Article Title  |     |     | Author(s)  |     | Journal Name  |     |     | Year  |     | Theme  |
| --- | -------------- | --- | --- | ---------- | --- | ------------- | --- | --- | ----- | --- | ------ |
The  Field  of  Usability  and  User Ghosh, S. & Dubey,  AR/VR,  VUIs,
|                           |     |     |     |     |     | AR in Retail Review  |     |     | 2024  |                   |     |
| ------------------------- | --- | --- | --- | --- | --- | -------------------- | --- | --- | ----- | ----------------- | --- |
| Experience (UX) Design.   |     |     |     | A.  |     |                      |     |     |       | Inclusive Design  |     |
Exploring the Nexus of User Interface
(UI) and User Experience (UX) in the  International  Journal  of
Context  of  Emerging  Trends  and  Informatics,  Information
|                                        |              |     |        | Paneru, R., et al.  |     |              |      |           | 2024  | VUIs  |     |
| -------------------------------------- | ------------ | --- | ------ | ------------------- | --- | ------------ | ---- | --------- | ----- | ----- | --- |
| Customer                               | Experience,  |     | Human  |                     |     | System       | and  | Computer  |       |       |     |
| Computer Interaction, Applications of  |              |     |        |                     |     | Engineering  |      |           |       |       |     |
Artificial Intelligence
| User  Interface          | Design  |         | in  Mobile  |                         |     |              |     |         |       | Accessibility,  |            |
| ------------------------ | ------- | ------- | ----------- | ----------------------- | --- | ------------ | --- | ------- | ----- | --------------- | ---------- |
|                          |         |         |             | Faudzi, N., et al.      |     | Heliyon      |     |         | 2024  |                 |            |
| Learning Applications:   |         |         |             |                         |     |              |     |         |       | Cognitive Load  |            |
| Empathy-Driven           |         | Design  | Thinking    |                         |     |              |     |         |       |                 |            |
|                          |         |         |             |                         |     | Interaction  |     | Design  |       | Design          | Thinking,  |
| Approaches               | in      | Mobile  |             | UI Aprilia, N., et al.  |     |              |     |         | 2024  |                 |            |
|                          |         |         |             |                         |     | Journal      |     |         |       | UCD             |            |
Development
The  Role  of  Design  Thinking  in  Interaction  Design  Iterative  Testing,
|                       |               |               |     | Algifahri, A., et al.  |     |                       |     |     | 2024  |                   |     |
| --------------------- | ------------- | ------------- | --- | ---------------------- | --- | --------------------- | --- | --- | ----- | ----------------- | --- |
| Mobile UX Innovation  |               |               |     |                        |     | Journal               |     |     |       | Design Thinking   |     |
| Artificial            | Intelligence  | Applications  |     | in                     |     |                       |     |     |       |                   |     |
|                       |               |               |     | Kamnerddee, N.         |     | AI in Design Journal  |     |     | 2024  | AI-Driven Design  |     |
UI Design Automation
|     |     |     |     |     |     | International  |     | Journal  | of  |     |     |
| --- | --- | --- | --- | --- | --- | -------------- | --- | -------- | --- | --- | --- |
Enhancing user experience in mobile
|     |     |     |     |     |     | Scientific  | Research  |     | in  |     |     |
| --- | --- | --- | --- | --- | --- | ----------- | --------- | --- | --- | --- | --- |
application  design  through  gestural Kadaskar, H.R.  2024  Gestural Interaction
|     |     |     |     |     |     | Modern  | Science  | and  |     |     |     |
| --- | --- | --- | --- | --- | --- | ------- | -------- | ---- | --- | --- | --- |
interaction
Technology
Cross-Platform Consistency in Mobile  Cross-Platform  Dev  Cross-Platform
|                     |       |             |      | Ali, M., et al.  |     |          |     |     | 2024  |                     |     |
| ------------------- | ----- | ----------- | ---- | ---------------- | --- | -------- | --- | --- | ----- | ------------------- | --- |
| Application Design  |       |             |      |                  |     | Journal  |     |     |       | Design, Challenges  |     |
| Enhancing           | User  | Engagement  | and  |                  |     |          |     |     |       |                     |     |
Continuous
Retention  in  Fintech:  A  Study  on  International  Journal  of
|     |     |     |     | Gada, T.  |     |     |     |     | 2024  | Feedback,  |     |
| --- | --- | --- | --- | --------- | --- | --- | --- | --- | ----- | ---------- | --- |
Effective  UX  Strategies  and  Design  Science and Research
Performance
Principles.
Usability  Challenges  in  Mobile  User Punchoojit,  L.  & Advances  in  Human- Small  Screen  Size,
2017
Interfaces  Hongwarittorrn, N.  Computer Interaction  Layout Challenges
|                                      |     |     |     |                  |     |          |     |              |       | Dark                | Mode,  |
| ------------------------------------ | --- | --- | --- | ---------------- | --- | -------- | --- | ------------ | ----- | ------------------- | ------ |
| Deconstructing Design Trends in UI:  |     |     |     |                  |     | UI/UX    |     | Interaction  |       |                     |        |
|                                      |     |     |     | UID Review Team  |     |          |     |              | 2024  | Microinteractions,  |        |
| A Review of Literature               |     |     |     |                  |     | Studies  |     |              |       |                     |        |
Trends
AI-Driven  Personalization  in  Mobile Li, X., Zhang, Y., & Int’l  Journal  of  Human- Personalization,  AI,
2022
UX: A Data-Centric Approach  Chen, P.  Computer Studies  Data-Driven UX
Personalization, User
Personalization  in  Mobile  UI/UX Liu, J., Wang, H., & Computers  in  Human
|                                |     |     |     |           |     |                   |     |     | 2024  | Behavior,  | Design  |
| ------------------------------ | --- | --- | --- | --------- | --- | ----------------- | --- | --- | ----- | ---------- | ------- |
| Design: Trends and Challenges  |     |     |     | Chen, R.  |     | Behavior Reports  |     |     |       |            |         |
Trends
|                                    |     |     |     |              |     |              |                 |     |       | UX           | Trends,  |
| ---------------------------------- | --- | --- | --- | ------------ | --- | ------------ | --------------- | --- | ----- | ------------ | -------- |
| Assessment of UX Design Trends in  |     |     |     |              |     | Journal      | of  Technology  |     |       |              |          |
|                                    |     |     |     | Okonkwo, C.  |     |              |                 |     | 2024  | Comparative  |          |
| Mobile Applications                |     |     |     |              |     | and Systems  |                 |     |       |              |          |
Analysis
Design  and  Experience  of  Mobile Tanwar,  S., Mathematics  2022  User  Experience
https://sesjournal.com                 | Jamal & Hashmat, 2025 |  Page 648

Spectrum of Engineering Sciences
ISSN (e) 3007-3138 (p) 3007-312X
Article Title Author(s) Journal Name Year Theme
Applications: A Pilot Survey Raboaca, M. S., & Survey, Usability
Leung, C. L. A. Feedback
Cyberpsychology, AR/VR, User
Implications of Virtual Reality for
Slater, M. Behavior, and Social 2017 Perception,
Perception and Behavior: A Review
Networking Behavioral UX
5.1. Recommendations
The study suggests that savvy mobile UI/UX Aprilia, D., Purnamasari, R., & Hidayat, S. (2024).
designers and developers consider implementing Enhancing mobile user experience through
innovative advancements such as personalization, user-centered design and iterative testing.
augmented reality and gestural controls for improved Human-Centered Computing Journal, 12(4),
usability without sacrificing efficiency. A blend of 67–81.
design thinking and AI-driven tools can optimize Azuma, R. T. (1997). A survey of augmented reality.
both the user experience and the development Presence: Teleoperators & Virtual Environments,
process. Users with disabilities must be considered 6(4), 355–385.
based on international guidelines and frequent Bhimanapati, G., Sharma, R., & Kaur, N. (2024).
testing must be ingrained at each stage of Inclusive design in mobile applications: A
production. Consistency across platforms, optimizing systematic review. Journal of Human-Computer
for performance across devices and working Interaction, 40(2), 225–243.
collaboratively across disciplines are all important. It Billinghurst, M., Clark, A., & Lee, G. (2015). A
is essential to stay informed and up-to-date on user survey of augmented reality. Foundations and
changes and advances in technology is achieved Trends in Human-Computer Interaction, 8(2–3),
through consistent user research and continuous 73–272.
professional development. Brignull, H. (2013). Dark patterns: User interfaces
designed to trick people. UX Collective.
References
Deconstructing design trends. (2024). Retrieved
Abdellrazik, T., Abodonia, S., & Abdelwahab, A.
from
(2024). User interface design trends for
https://www.uiuxtrendsreport.com/2024-
mobile applications. International Design design-practices
Journal. Dong, H. (2017). Inclusive design: Developing a society
https://doi.org/10.21608/idj.2024.348543
for all. Springer.
Ali, A., Xia, Y., Navid, Q., Khan, Z. A., Khan, J. A.,
Faudzi, M. A., Cob, Z. C., Ghazali, M., Omar, R., &
Aldakheel, E. A., & Khafaga, D. S. (2024).
Sharudin, S. A. (2024). User Interface
Mobile-UI-Repair: a deep learning-based UI
Design in Mobile Learning Applications:
smell detection technique for mobile user
Developing and Evaluating a Questionnaire
interface. PeerJ. for Measuring Learners’ Extraneous
https://doi.org/10.7717/peerj-cs.2028
Cognitive Load. Heliyon, e37494.
Algifahri, M. D., Putra, D. D., Zulfi Zulfi, T. F., &
https://doi.org/10.1016/j.heliyon.2024.e37
Lubis, A. H. (2024). Transformation of
494
Binjai Police Presence Application: UI/UX
Design with Design Thinking Method to
Improve Efficiency and User Experience.
Internet of Things and Artificial Intelligence
Journal.
https://doi.org/10.31763/iota.v4i1.690
https://sesjournal.com | Jamal & Hashmat, 2025 | Page 649

Spectrum of Engineering Sciences
| ISSN (e) 3007-3138 (p) 3007-312X  |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Fazil, A. W., Hamidi, S. A., & Habibi, H. (2024).  Liu,  J.,  Wang,  H.,  &  Chen,  R.  (2024).
Evaluating  the  Impact  of  Emerging  Personalization  in  mobile  UI/UX  design:
Technologies  on  Mobile  User  Experience:  Trends and challenges. Computers in Human
The  Role  of  User-Centered  Design  in  Behavior Reports, 12, 100238.
|     | Overcoming  |     | Development  |     | Challenges.  |     |     |     |     |     |     |     |     |
| --- | ----------- | --- | ------------ | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
Lupton, E. (2014). Thinking with type: A critical guide
International Journal Software Engineering and  for  designers,  writers,  editors,  &  students.
Computer  Science,  4(3),  1244–1252.  Princeton Architectural Press.
https://doi.org/10.35870/ijsecs.v4i3.3167
Marcotte, E. (2010). Responsive web design. A List
| Gada, T. (2024). Enhancing User Engagement and  |     |     |     |     |     |     |     | Apart, 306.  |     |     |     |     |     |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- |
Retention in Fintech: A Study on Effective  Marcus,  A.  (2013).  Cross-cultural  user  experience
|     | UX  | Strategies  |     |     | and  | Design  |     |     |     |     |     |     |     |
| --- | --- | ----------- | --- | --- | ---- | ------- | --- | --- | --- | --- | --- | --- | --- |
design. In Human-computer interaction: Design
Principles. International Journal of Science and  and  development  approaches  (pp.  25–30).
|     | Research, 13(5),  |     |     |     | 1260–1263.  |     |     | Springer.  |     |     |     |     |     |
| --- | ----------------- | --- | --- | --- | ----------- | --- | --- | ---------- | --- | --- | --- | --- | --- |
https://doi.org/10.21275/sr24520104932
Milgram, P., & Kishino, F. (1994). A taxonomy of
| Ghosh,  | S.,  &  | Dubey,  | S.  | (2024).  | The  | Field  of  |     |        |          |         |     |            |        |
| ------- | ------- | ------- | --- | -------- | ---- | ---------- | --- | ------ | -------- | ------- | --- | ---------- | ------ |
|         |         |         |     |          |      |            |     | mixed  | reality  | visual  |     | displays.  | IEICE  |
Usability and User Experience (UX) Design.  Transactions  on  Information  and  Systems,
|     | Advances  | in  | Social  | Networking  | and  | Online  |     |     |     |     |     |     |     |
| --- | --------- | --- | ------- | ----------- | ---- | ------- | --- | --- | --- | --- | --- | --- | --- |
77(12), 1321–1329.
|     | Communities  |     | Book  | Series,  | 117–154.  |     |           |              |     |            |             |     |            |
| --- | ------------ | --- | ----- | -------- | --------- | --- | --------- | ------------ | --- | ---------- | ----------- | --- | ---------- |
|     |              |     |       |          |           |     | Nielsen,  | J.  (2021).  |     | Usability  | heuristics  |     | for  user  |
https://doi.org/10.4018/979-8-3693-2337- interface  design:  A  revisited  approach.
3.ch005
Nielsen Norman Group.
| Google  | Developers.  |     | (2022).  | Progressive  | web  | apps:  |           |         |           |     |          |              |      |
| ------- | ------------ | --- | -------- | ------------ | ---- | ------ | --------- | ------- | --------- | --- | -------- | ------------ | ---- |
|         |              |     |          |              |      |        | Nielsen,  | J.,  &  | Pernice,  | K.  | (2010).  | Eyetracking  | web  |
Bridging the gap between web and mobile apps.  usability. New Riders.
https://developers.google.com/web/progres
Norman, D. A. (2013). The design of everyday things:
sive-web-apps
Revised and expanded edition. Basic Books.
Kadaskar, H. R. (2024). Enhancing user experience  Okonkwo, C. (2024). Assessment of user experience
|     | in  mobile  |     | application  |     | design  | through  |     |     |     |     |     |     |     |
| --- | ----------- | --- | ------------ | --- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- |
(UX) design trends in mobile applications.
|     | gestural  | interaction:  |     | A   | human-computer  |     |     |     |     |     |     |     |     |
| --- | --------- | ------------- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Journal of Technology and Systems, 6(5), 29–41.
|     | interaction perspective.  |     |     | International Journal  |     |     |     |     |     |     |     |     |     |
| --- | ------------------------- | --- | --- | ---------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
https://doi.org/10.47941/jts.2147
|     | of  Scientific  |     | Research  | in  Modern  | Science  | and  |     |     |     |     |     |     |     |
| --- | --------------- | --- | --------- | ----------- | -------- | ---- | --- | --- | --- | --- | --- | --- | --- |
Paneru, B., Paneru, B., Poudyal, R., & Shah, K. B.
|     | Technology,  |     |     | 3(8),  |     | 1–6.  |     |          |            |     |      |        |           |
| --- | ------------ | --- | --- | ------ | --- | ----- | --- | -------- | ---------- | --- | ---- | ------ | --------- |
|     |              |     |     |        |     |       |     | (2024).  | Exploring  |     | the  | Nexus  | of  User  |
https://doi.org/10.59828/ijsrmst.v3i8.239  Interface (UI) and User Experience (UX) in
Kamnerddee, T., & Luangamornlert, R. (2024). AI-
|     |     |     |     |     |     |     |     | the  Context  |     | of  Emerging  |     | Trends  | and  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ------------- | --- | ------- | ---- |
enhanced UI design tools: Case studies in
|     |     |     |     |     |     |     |     | Customer  | Experience,  |     | Human  |     | Computer  |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------------ | --- | ------ | --- | --------- |
Figma and Adobe XD. Design Automation and  Interaction,  Applications  of  Artificial
Intelligence Journal, 6(1), 50–63.
|        |              |        |       |     |                     |     |     | Intelligence.  |     | International  |     | Journal  | of  |
| ------ | ------------ | ------ | ----- | --- | ------------------- | --- | --- | -------------- | --- | -------------- | --- | -------- | --- |
| Krug,  | S.  (2014).  | Don't  | make  | me  | think,  revisited:  | A   |     |                |     |                |     |          |     |
Informatics, Information System and Computer
common-sense approach to web usability. New  Engineering,  5(1),  102–113.
|     | Riders.  |     |     |     |     |     |     | https://doi.org/10.34010/injiiscom.v5i1.12 |     |     |     |     |     |
| --- | -------- | --- | --- | --- | --- | --- | --- | ------------------------------------------ | --- | --- | --- | --- | --- |
Richard Mallett, Jessica Hagen-Zanker, Rachel Slater
488
& Maren Duvendack (2012) The benefits  Punchoojit,  L.,  &  Hongwarittorrn,  N.  (2017).
and challenges of using systematic reviews in
Usability Studies on Mobile User Interface
international development research, Journal
|     |     |     |     |     |     |     |     | Design  | Patterns:  | A   | Systematic  |     | Literature  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ---------- | --- | ----------- | --- | ----------- |
of  Development  Effectiveness,  4:3,  445-455,  Review.  Advances  in  Human-Computer
DOI: 10.1080/19439342.2012.711342  Interaction,  2017,  1–22.

https://doi.org/10.1155/2017/6787504

|     |     |     |     |     |     |     | Saffer,  | D.  (2013).  | Microinteractions:  |     |     | Designing  | with  |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------------ | ------------------- | --- | --- | ---------- | ----- |
details. O'Reilly Media.
https://sesjournal.com                 | Jamal & Hashmat, 2025 |  Page 650

Spectrum of Engineering Sciences
| ISSN (e) 3007-3138 (p) 3007-312X  |     |     |     |     |     |
| --------------------------------- | --- | --- | --- | --- | --- |

Shneiderman, B. (2016). Designing the user interface:
| Strategies  |     | for  effective  | human-computer  |     |     |
| ----------- | --- | --------------- | --------------- | --- | --- |
interaction. Pearson.
Slater, M. (2017). Implications of virtual reality for
| perception        |     | and  behavior:  | A  review.   |     |     |
| ----------------- | --- | --------------- | ------------ | --- | --- |
| Cyberpsychology,  |     | Behavior,       | and  Social  |     |     |
Networking, 20(1), 3–10.
| Tanwar,        | S.,  Raboaca,  | M.  S.,  &         | Leung,  C.  L.  | A.  |     |
| -------------- | -------------- | ------------------ | --------------- | --- | --- |
| (2022).        | Design         | and  experience    | of  mobile      |     |     |
| applications:  |                | A  pilot  survey.  | Mathematics,    |     |     |
| 10(14),        |                |                    | 2380.           |     |     |
https://doi.org/10.3390/math10142380
Tullis, T., & Albert, B. (2013). Measuring the user
experience: Collecting, analyzing, and presenting
usability metrics. Morgan Kaufmann.
W3C. (2021). Web accessibility guidelines (WCAG 2.1).
https://www.w3.org/TR/WCAG21/

https://sesjournal.com                 | Jamal & Hashmat, 2025 |  Page 651