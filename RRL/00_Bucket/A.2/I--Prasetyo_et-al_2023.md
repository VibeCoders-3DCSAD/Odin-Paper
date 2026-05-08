```python
import pypdf
import re
import uuid

def extract_pdf_data(pdf_path):
    with open(pdf_path, 'rb') as f:
        reader = pypdf.PdfReader(f)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text

full_text = extract_pdf_data('IJCS_12_3+Prasetyo.pdf')

# Check for DOI
doi_match = re.search(r'10\.\d{4,9}/[-._;()/:A-Z0-9]+', full_text, re.IGNORECASE)
doi = doi_match.group(0) if doi_match else None

# Generate UUID v4 seeded by title
title = "Integrating Financial Management and Gamification: A Systematic Literature Review and Future Research Agenda"
paper_uuid = str(uuid.uuid5(uuid.NAMESPACE_DNS, title.replace(" ", "").lower()))

print(f"DOI: {doi}")
print(f"UUID: {paper_uuid}")
print("-" * 20)
print(full_text)


```

```text
DOI: 10.1108/IJBM-12-2020-0612.
UUID: c8b2b27f-2af5-574e-a98f-4cdc89c44ba7
--------------------
Indonesian Journal of Computer Science 
ISSN 2549-7286 (online) 
Jln. Khatib Sulaiman Dalam No. 1, Padang, Indonesia 
Website: ijcs.stmikindonesia.ac.id | E-mail: ijcs@stmikindonesia.ac.id 
Attribution-ShareAlike 4.0 International License Vol. 12, No. 2, Ed. 2023 | page 961  
      
 
Integrating Financial Management and Gamification: A Systematic Literature 
Review and Future Research Agenda 
 
Amrisandha Pranantya Prasetyo, Harry Budi Santoso, Panca Oktavia Hadi Putra 
amrisandha.pranantya@ui.ac.id, harrybs@cs.ui.ac.id, hadiputra@cs.ui.ac.id 
Faculty of Computer Science, Universitas Indonesia, Depok, Indonesia 
 
Article Information  Abstract 
Submitted :  17 Jun 2023 
Reviewed :  23 Jun 2023 
Accepted :  27 Jun 2023 
 
 
The implementation of gamification in personal financial management (PFM) 
apps has the potential to motivate users to e ngage in positive financial 
behaviors. However, several research gaps corroborate the need to 
investigate gamification in the financial domain further . T o address these 
gaps, this systematic literature review comprehensively examines current 
research on fi nancial behavior and gamification . This review utilizes the 
Theory, Context, Characteristics, and Methodology (T CCM) framework to  
provide a holistic understanding of financial behavior and gamification -
related behavioral int ention. A total of 53 articles p ublished between 2018 
and 2022 were analyzed to assess the present r esearch landscape and 
provide directions for future studies. This review makes three key 
contributions: (1) synthesiz es current research on financial behavi or and 
gamification-related behavioral intention, (2) presents integrated conceptual 
models that elucidate financial behavior and gamification -related behavioral 
intention, and (3) identif ies research gaps and suggest s avenues for future 
investigation. 
 
Keywords   
Systematic literature 
review, financial 
behavior, gamification, 
behavioral intention, 
TCCM 
 
 
 
 
 
  ISSN 2549-7286 (online) 
Indonesian Journal of Computer Science   Vol. 12, No. 2, Ed. 2023 | page 962   
A. Introduction 
 In recent years, there has been growing concern regarding the low l evel of 
public financial behavior [1]. Researchers have found that many individuals make 
bad financial decisions, save too little, spend too much [2], and invest in things they 
later regret [3]. Financial behavior has a significant impact on an individual’s long-
term financial outcomes and can lead to long-term financial problems  [1], [4]–[6]. 
 The financial sector is among the first to adopt mobile technology  [7], [8]. 
Along w ith the rise of mobile banking and payment a pps [9], personal financial 
management (PFM) apps have emerged as one of the fastest -growing categories of 
financial appli cations [7]. In addition to the rise in mobile banking and payment 
apps [9], PFM apps are one of the fastest -growing categories of financial 
applications [7]. The global PFM application market is expected to reach $3,338 
million by 2025 with an annual growth rate of 12.65 % from 2018 [10]. 
 However, there is a curr ent challenge in effectively int egrating technology 
to enhance the quality of life [11]–[13]. One way to improve user experience, 
motivation, and interest is through gamification , the implementation of  game 
features and game -like designs in apps [7], [ 14]. Gamification has gained 
significant attention from academic resea rchers and practitioners [15], [ 16]. 
However, most of the existing research related to gamification has focused on the  
education and learning sector, while other sect ors, such as finance, have received 
limited att ention [7], [17] –[19]. This highlights a research gap in gamification in 
personal finance, despite its recognized importance [15] and widespread adoption 
[7], [20].  
 Previous reviews have only examined  financial behavior [1] or gamification 
[21]. Therefore, it i s beneficial to add ress these research gaps by conducting a 
study that reviews and synthesizes the relationship between these two topics.  This 
study employs a systematic literature review methodology to map the current 
financial behavior and gamification r esearch state. Specifically, this study aims to 
bridge the gap between financial behavior with gamification by reviewing research 
on gamification-related behavioral intention. 
 This review employs the Theory, Context, Chara cteristics, and Methodology 
(TCCM) framework develop ed by [22]. The T CCM framework provides more 
comprehensive and robust insights comp ared to other approaches  [23], [24] , 
enabling a holistic understanding of a research domain  [25]. Furthermore, the 
TCCM framework allows for theoretical and empirical  mapping of a research field  
[25]–[27]. This analysis includes 53 articles to review the current state of research 
and provide directions for future resea rch. Overall, this review provid es th ree 
contributions by (1) providing a holistic synthesis of existing research on financial 
behavior and gamification -related behavioral in tention, (2) present ing integrated 
conceptual models that explain financial behavi or and gamification-related 
behavioral intention, a nd (3) identif ying research gaps and providing directions 
for future research. 
 The remainder of the paper is structured as  follows. Section 2 explains the 
methodology employed in this systematic literature review. Section 3 presents this 
review’s results and future research agendas based on  the TCCM framework. 
Finally, Section 4 concludes the study. 
 
  ISSN 2549-7286 (online) 
Indonesian Journal of Computer Science   Vol. 12, No. 2, Ed. 2023 | page 963   
 
B. Research Method 
 The systematic literature review  was conducted  following the 
methodological guidelines outlin ed by [28]. This study aim s to identi fy, evaluate, 
and interpret exist ing research in the domains of financial behavior and 
gamification-related behavioral in tention using the TCCM framework [25]. The 
search strategy, stu dy selection process, and d ata extraction methods  are 
deescribed as follows. 
 
Search Strategy 
Four reputabl e online research databases  were selec ted: Emerald Insights, 
IEEE Xplore, Science Direct, and  Taylor & Francis. For each domain, specific search 
strings were developed incorporating relevant key terms. In addition to core terms 
related to financial  behavior and gamification, terms such as “theory," 
“framework,” and “model” were included . The resulting  search strings were as 
follows. 
 
(“personal”) AND ( “financial” OR “finance”) AND ( “management” OR 
“managing”) AND ( “behavior” OR “behavior”) AND ( “theory” OR “theoretical” OR 
“framework” OR “model”) 
 
(“gamification” OR “gamify” OR “gamified”) AND ( “theory” OR “theoretical” 
OR “framework” OR “model”) 
 
The search was conducted in September 2 022, limited to article titles, 
abstracts, and keywords. Only journal art icles and proceedings papers published 
between 2018 and 2022  were inc luded. This search resulted i n 27,888 articles: 
20,078 articl es on financial behavior  and 7,810 articles on gamification-related 
behavioral intention. 
 
Study Selection 
The study selection process consisted of title and abstract selection, followed 
by full-text selection. Throughout bo th steps, articles were assessed  based on the 
following inc lusion criteria: (1) articles written in English, (2) articles that 
investigated either financial behavior or gamification-related behavioral intention, 
(3) empirical research presenting a research  model or hypotheses, and (4) ar ticles 
that were not litera ture reviews. Fifty six relevant arti cles were identified in the 
first step : 27  on financial behavi or and  29 on gamification -related behavioral 
intention. In the second  step, three articles on financi al behavior  were excluded , 
resulting in a final selection of 53 articles. 
 
 
  ISSN 2549-7286 (online) 
Indonesian Journal of Computer Science   Vol. 12, No. 2, Ed. 2023 | page 964   
 
 
Figure 1. Study selection process 
 
 
Data Extraction 
 This systematic literat ure revi ew followed the domain -based approach 
using the TCCM framework developed by [22]. Relevant publication details such as 
title, year of publication, and publication outlet  were extracted . Furthermore, 
information related to theori es, contexts, characteristics or cons tructs, and 
research me thodologies was extracted following the TCCM framework . Finally, 
research limitations  and suggestions provided by the authors for future research  
were extracted to identify potential research directions. 
 
C. Result and Discussion 
Overview of Reviewed Articles 
This section organizes the articles based on their publication year and outlet.  
Figure 2 illustrates the growth of research on financial behavior and gamification -
related behavioral intention from 2018 to 2022. It is evident that research interest 
in both domains has been increasing in recent years. 
  ISSN 2549-7286 (online) 
Indonesian Journal of Computer Science   Vol. 12, No. 2, Ed. 2023 | page 965   
 
 
Figure 2. Number of articles by year of publication 
 
Furthermore, Table 1 presents the finance, business, and management 
journals as publication outlets for articles on financial behavior. On the other hand, 
Table 2 shows that articles on gamification -related behavioral intention have been 
published in various journals, including those focused on human -computer 
interaction, information systems, management, computer s cience, education , a nd 
business. Some articles on gamification -related behavioral intention were also  
sourced from management and education technology proceedings. 
 
Table 1. Publication Outlets of Financial Behavior Research 
Publication Outlet SJR # % References 
International Journal of Bank Marketing Q2 4 16.7 [29]–[32] 
Young Consumers Q1 3 12.5 [15], [33], [34] 
Cogent Business and Management Q2 3 12.5 [4], [35], [36] 
Managerial Finance Q3 2 8.3 [37], [38] 
Applied Developmental Science Q1 1 4.2 [39] 
Economics of Innovation and New Technology Q1 1 4.2 [40] 
International Journal of Sociology and Social Policy Q1 1 4.2 [41] 
Journal of Services Marketing Q1 1 4.2 [42] 
Asia-Pacific Journal of Business Administration Q2 1 4.2 [43] 
Cogent Social Sciences Q2 1 4.2 [44] 
Journal of Behavioral and Experimental Economics Q2 1 4.2 [45] 
Kybernetes Q2 1 4.2 [46] 
Marriage and Family Review Q2 1 4.2 [47] 
Review of Behavioral Finance Q2 1 4.2 [48] 
Journal of Workplace Behavioral Health Q3 1 4.2 [49] 
Journal of Money and Business - 1 4.2 [50] 
 
  ISSN 2549-7286 (online) 
Indonesian Journal of Computer Science   Vol. 12, No. 2, Ed. 2023 | page 966   
Table 2. Publication Outlets of Gamification-Related Behavioral Intention 
Research 
Publication Outlet SJR # % References 
International Journal of Human-Computer Interaction Q1 3 10.3 [51]–[53] 
Industrial Management and Data Systems Q1 2 6.9 [54], [55] 
Information Technology and People Q1 2 6.9 [11], [56] 
International Journal of Human Computer Studies Q1 2 6.9 [57], [58] 
Computers in Human Behavior Q1 1 3.4 [59] 
Enterprise Information Systems Q1 1 3.4 [60] 
International Journal of Information Management Q1 1 3.4 [61] 
Internet Research Q1 1 3.4 [62] 
Journal of Business Research Q1 1 3.4 [63] 
Journal of Enterprise Information Management Q1 1 3.4 [64] 
Journal of Further and Higher Education Q1 1 3.4 [65] 
Journal of Service Theory and Practice Q1 1 3.4 [66] 
Journal of Small Business and Enterprise Development Q1 1 3.4 [67] 
Young Consumers Q1 1 3.4 [68] 
Education and Training Q2 1 3.4 [69] 
Interactive Technology and Smart Education Q2 1 3.4 [70] 
International Journal of Bank Marketing Q2 1 3.4 [7] 
International Journal of Sports Marketing and Sponsorship Q2 1 3.4 [71] 
Journal of Systems and Information Technology Q2 1 3.4 [72] 
Learning and Motivation Q2 1 3.4 [73] 
World Journal of Science, Technology and Sustainable 
Development - 1 3.4 [74] 
2019 16th International Conference on Service Systems and 
Service Management, ICSSSM 2019 - 1 3.4 [75] 
2020 8th International Conference on Cyber and IT Service 
Management, CITSM 2020 - 1 3.4 [76] 
Proceedings - IEEE 10th International Conference on 
Technology for Education, T4E 2019 - 1 3.4 [77] 
 
Theory 
Upon reviewing the literature, it was found that six theories have been  
employed as theoretical foundations to investigate fi nancial behavior. The theory 
of planned behavior emerged as the most freq uently used theory, accoun ting for 
50% of the studies. Other theories utilized included the family stress theory 
(16.7%), behavioral life -cycle theory (8.3%), family financial sociali zation theory 
(8.3%), management system theory (8.3%), and self-determination theory (8.3%). 
 While the reviewed studies on financial behavior did not provide specific 
suggestions for future theory development, a systematic literature review on 
personal fina ncial management behavior [1] offers potential avenues for 
theoretical exploration. This review suggests employing interdisciplinary 
theoretical approaches to examine how individuals ’ financial behavior is 
influenced by different life stages [78], [79] . [1] also proposes investigating the 
connections between financial education, personal financial managem ent 
behavior, and life satisfaction [79]–[81]. Additionally, socio-psychological theories 
could be developed to understand behavioral biases from c ultural and social 
factors [1]. Finally, [1] also recommends employing the theory of planned behavior 
and the transtheoretical model in investigating diverse behaviors and populations 
[29].  
 
  ISSN 2549-7286 (online) 
Indonesian Journal of Computer Science   Vol. 12, No. 2, Ed. 2023 | page 967   
Table 3. Theories Used in Financial Behavior Research 
Theory # % References 
Theory of Planned Behavior 6 50 [4], [29], [32], [36], [43], [45] 
Family Stress Theory 2 16.7 [47], [49] 
The Behavioral Life-Cycle Theory 1 8.3 [50] 
Family Financial Socialization Theory 1 8.3 [31] 
Management System Theory 1 8.3 [47] 
Self-Determination Theory 1 8.3 [33] 
 
 On the other  hand, 25 theories were identified in studies exploring 
gamification-related behavioral intention. The majority of these theories (54%) 
focused on technology adopt ion. Notably, the self -determination theory (14.3%), 
technology acceptance model (11.9%), theory of planned behavior (9.5%), 
expectation-confirmation model (7.1 %), and the unified theory of acceptance and 
use of technology (7.1% f or both version 1 and 2) w ere t he most frequently 
employed. Other theories related to technology use include  the continuance 
theory, diffusion of innovation, flow theory, hedonic motiva tion system adoption 
model, uses and gratification theory, and user eng agement theory. In additio n, 
there were gamification-specific theories such as the gamification theory, Landers ’ 
theory of gamified learning, and work gamification theory. The remaining  theories 
used in gamification research pertained to psychology (e.g., cognitive absorption 
theory, co gnitive evaluation theory, goal framing theory, goal priming theory, 
theory of reasoned action, prospect theory, theory of perceived risk, and theory of 
consumption values) and social theories (e.g., generational cohort theor y and 
social identity theory). 
 Regarding theoretical development opportunities in gamification -related 
behavioral intention research, future studies can employ relevant theories to 
investigate adoption, reuse, and continuance intention [56], [59] . Motivation 
theory is also suggested as a viable option [53], [82]. Additionally, using existing or 
new theories on dynamic and cyclical gamification is recommended [21]. Exploring 
potential similarities between constructs from different theories over time is 
another avenue for investigation [53]. 
 
Table 4. Theories Used in Gamification-Related Behavioral Intention 
Research 
Theory # % References 
Self-Determination Theory 6 14.3 [7], [51], [57], [59], [67], [70] 
Technology Acceptance Model  5 11.9 [7], [11], [52], [70], [73] 
Theory of Planned Behavior 4 9.5 [52], [67], [73], [77] 
Expectation-Confirmation Model 3 7.1 [56], [64], [69], [75] 
Unified Theory of Acceptance and Use of 
Technology 2 
3 7.1 [53], [71], [72] 
Unified Theory of Acceptance and Use of 
Technology 
2 4.8 [68], [74] 
Cognitive Absorption Theory 1 2.4 [64] 
Cognitive Evaluation Theory 1 2.4 [63] 
Continuance Theory 1 2.4 [51] 
Diffusion of Innovation 1 2.4 [74] 
Flow Theory 1 2.4 [69] 
Generational Cohort Theory 1 2.4 [72] 
Gamification Theory 1 2.4 [72] 
  ISSN 2549-7286 (online) 
Indonesian Journal of Computer Science   Vol. 12, No. 2, Ed. 2023 | page 968   
Goal Framing Theory 1 2.4 [54] 
Goal Priming Theory 1 2.4 [60] 
Hedonic Motivation System Adoption Model 1 2.4 [76] 
Landers’ Theory of Gamified Learning 1 2.4 [65] 
Prospect Theory 1 2.4 [11] 
Social Identity Theory 1 2.4 [51] 
Theory of Consumption Values 1 2.4 [62] 
Theory of Reasoned Action 1 2.4 [73] 
Theory of Perceived Risk 1 2.4 [62] 
User Engagement Theory 1 2.4 [55] 
Uses and Gratification Theory 1 2.4 [68] 
Work Gamification Theory 1 2.4 [55] 
 
While it is evident that a wide range of theories have been utilized to analyze 
gamification, there is a narrower selection of theories applied i n financial behavior 
research. Nevertheless, the theory of planned behavior, commonly employed in 
financial behavior studies, is also relevant to gamification research. Furthermore, 
the self-determination theory demonstrates relevance in both domains and has the 
potential for increased utilization in financial behavior research. 
 
Context 
 Table 5 summarizes the financial contexts covered in the reviewed articles 
investigating financial behavior. Most research in this area generally focuses on 
financial beha vior (21%). Other aspects of financial behavior that have been 
studied include responsible financial behavior, saving behavior, spending 
behavior, and retirement behavior. Additionally, common research areas include 
financial lit eracy (10.5%), financial sa tisfaction (7.9%), financial well -being 
(7.9%), financial goals (5.3%), and financial stress (5.3%). 
 Future research on financial behavior is encouraged to explore previously 
studied financial behaviors in different c ountries, cultures, and demographics [45]. 
Furthermore, investigating financial behavior across various life stages [31], 
including the transitional period of young adults and their partners [39], [83], is 
recommended. Additionally, research can focus on f inancial behavior within 
different financial sectors, such as banking, insurance, and securities markets [38]. 
 
Table 5. Contexts of Financial Behavior Research 
Context # % References 
General financial behavior 8 21 [4], [15], [30], [33], [39], [44]–[46] 
Financial literacy 4 10.5 [37], [38], [40], [43] 
Financial satisfaction 3 7.9 [36], [39], [47] 
Financial well-being 3 7.9 [36], [42], [48] 
Financial goals 2 5.3 [35], [39] 
Financial stress 2 5.3 [4], [49] 
Responsible financial behavior 2 5.3 [29], [34] 
Saving behavior 2 5.3 [40], [41] 
Attitudes 1 2.6 [45] 
Depositor discipline 1 2.6 [37] 
Family financial socialization 1 2.6 [31] 
Financial confidence 1 2.6 [44] 
Financial knowledge 1 2.6 [44] 
Investment decision 1 2.6 [50] 
Learning capacity 1 2.6 [44] 
  ISSN 2549-7286 (online) 
Indonesian Journal of Computer Science   Vol. 12, No. 2, Ed. 2023 | page 969   
Retirement behavior 1 2.6 [35] 
Retirement planning 1 2.6 [32] 
Self-control 1 2.6 [45] 
Spending behavior 1 2.6 [40] 
Workplace productivity 1 2.6 [49] 
 
 Meanwhile, Table 6 presen ts the contexts of the reviewed articles 
investigating gamification -related behavioral intention. These articles  explore 
gamification in education (20.7%), finance (17.2%), games and gamified systems 
in general (17.2%), health and fitness (17.2%), e -commerce (6.9%), and 
management (6.9%). Furthermore, gamification research has also started to 
extend into business, entertainment, environmental, and marketing contexts. Table 
7 summarizes the gamification elements investigated or implemented in these 
reviewed articles. The analysis reveals the involvement of various  gamification 
elements, encompassing achievement -related, social -related, and immersion -
related aspects. 
 Future research on gamification -related behavioral intention is suggested 
to explore new sect ors [72] or types of gamified apps [56]. Specifically, 
investigating specific gamified apps rather than considering an entire app category 
as a whole is encouraged [56]. Analyzing these new contex ts can deepen the 
understanding of gamification implementation methods and outcomes [63]. 
Additionally, future research can explore new gamification elements and  the 
consequences of each element [57], [72] . Elements of gamification that can be 
further explored include narrative, mechanics, aesthetics, and technological 
aspects [68]. As mentioned in the systematic literature review by [21], future 
research can also investigate cooperative and collective gamification. 
 
Table 6. Contexts of Gamification-Related Behavioral Intention Research 
Context # % References 
Education 6 20.7 [51], [57], [65], [69], [70], [77] 
Finance 5 17.2 [7], [11], [64], [72], [74] 
Games and general gamified systems 5 17.2 [53], [56], [58], [59], [73] 
Health and fitness 5 17.2 [52], [60]–[62], [71] 
E-commerce 2 6.9 [68], [75] 
Management 2 6.9 [55], [59] 
Business 1 3.4 [67] 
Entertainment 1 3.4 [76] 
Environmental 1 3.4 [54] 
Marketing 1 3.4 [66] 
 
 
Table 7. Gamification Elements Investigated in Gamification-Related 
Behavioral Intention Research 
Gamification Element # % References 
Badge 6 9.7 [55], [57], [67], [71], [73], [77] 
Point 6 9.7 [55], [64], [67], [69], [72] 
Games 5 8.0 [53], [64], [68]–[70] 
Leaderboards 4 6.4 [53], [55], [67], [73] 
Monitoring 4 6.4 [52], [61], [66], [71] 
Social 4 6.4 [52], [61], [71], [75] 
Challenge 3 4.8 [66], [67], [77] 
  ISSN 2549-7286 (online) 
Indonesian Journal of Computer Science   Vol. 12, No. 2, Ed. 2023 | page 970   
Feedback 3 4.8 [59], [66], [77] 
Levels 3 4.8 [55], [61], [67] 
Training 3 4.8 [66], [67], [71] 
Achievements 2 3.2 [53], [54] 
Competition 2 3.2 [54], [73] 
Goal 2 3.2 [52], [73] 
Prizes 2 3.2 [72], [73] 
Rewards 2 3.2 [52], [72] 
Autonomy support 1 1.6 [54] 
Avatar 1 1.6 [59] 
Character 1 1.6 [66] 
Cooperation 1 1.6 [73] 
Gifting 1 1.6 [11] 
Immersion 1 1.6 [75] 
Interactivity 1 1.6 [54] 
Medals 1 1.6 [61] 
Narrative 1 1.6 [60] 
Storytelling 1 1.6 [73] 
Time constraint 1 1.6 [73] 
 
 The results also indicate that several studies examine gamification in 
financial contexts. These studies are conducted by [7], [11], [64], [72], [74]. Most of 
these studies focus on gamification in ban king contexts, as seen in the works of 
[74], [72], and [11]. Additionally, a study by [64] specifically explores gamification 
in robo-advisor apps, while a study by [7] concentrates on gamification in the PFM 
app Mint. 
 
Characteristics 
This review encompasses a r ange of factors that influence financial behavior 
and gamification -related behavioral intention, including antecedents, mediators, 
moderators, and consequences. Figures 3 and 4  illustrate i ntegrated conceptual 
models depicting financial behavior and gamification -related behavioral intention. 
We further synthesize these constructs in detail. 
 
 
  ISSN 2549-7286 (online) 
Indonesian Journal of Computer Science   Vol. 12, No. 2, Ed. 2023 | page 971   
 
 
Figure 3. Integrated conceptual model of financial behavior 
 
  ISSN 2549-7286 (online) 
Indonesian Journal of Computer Science   Vol. 12, No. 2, Ed. 2023 | page 972   
 
 
Figure 4. Integrated conceptual model of gamification-related behavioral intention 
 
1) Antecedents — Antecedents of financial behavior can be categorized into 
several groups: financial -related, socio -demographic, psycholo gical, and external 
constructs. Financial -related antecedents, such as financial literacy, attitude, and  
knowledge, have been widely employed to investigate financial behavior. 
  ISSN 2549-7286 (online) 
Indonesian Journal of Computer Science   Vol. 12, No. 2, Ed. 2023 | page 973   
Furthermore, socio -demographic constructs, including e ducation, gender, age, 
income, and marital status, have demonstrat ed significant relevance in prior 
research. Additionally, a psychological construct that bears relevance is self -
control. Turning to antecedents of gamification -related behavioral intention, they 
can be classified into psychological, socio -demographic, soc ial, gamification, and 
context-specific constructs. Notably, these constructs commonly revolve around 
hedonic ...

```

```python
import pypdf

def extract_all_pages(pdf_path):
    with open(pdf_path, 'rb') as f:
        reader = pypdf.PdfReader(f)
        pages_content = []
        for i, page in enumerate(reader.pages):
            pages_content.append(f"--- PAGE {i+1} ---\n" + page.extract_text())
    return "\n".join(pages_content)

full_content = extract_all_pages('IJCS_12_3+Prasetyo.pdf')
# Print the last few pages to see references and conclusion
print(full_content[-5000:])


```

```text
ating effect of generational cohorts, ” J. Syst. Inf. 
Technol., vol. 12, no. 3, p p. 243–263, Jan. 2020, doi: 10.1108/JSIT -01-2020-
0005. 
[73] H. Treiblmaier and L. M. Putz, “Gamification as a moderator for the impact of 
intrinsic motivation: Findings from  a multigroup field experiment, ” Learn. 
Motiv., vol. 71, p. 101655, 2020, doi: 10.1016/j.lmot.2020.101655. 
[74] S. Rahi and M. Abd. Ghani, “The role of UTAUT, DOI, perceived technology 
security and game elements in internet banking adoption, ” World J. Sci.  
Technol. Sustain. Dev. , vol. 15, no. 4, pp. 338 –356, Jan. 2018, doi: 
10.1108/wjstsd-05-2018-0040. 
[75] Y. Feng, Z. Liu, W. Qian, M. Guo, and J. Chen, “Research on the influence 
mechanism of gamification elements on users ’ willingness to continue using 
in interest-based virtual communities - Based on ECM -ISC model, ” in 2019 
16th Internat ional Conference on Service Systems and Service Management, 
ICSSSM 2019, 2019, pp. 1–6, doi: 10.1109/ICSSSM.2019.8887645. 
--- PAGE 25 ---
  ISSN 2549-7286 (online) 
Indonesian Journal of Computer Science   Vol. 12, No. 2, Ed. 2023 | page 985   
[76] M. Qomarul Huda, N. Aeni Hidayah, T. Nur Hafiz ah Hersyaf, I. Sujoko, and 
Asmawi, “Analysis of Continuance Use of Video on Demand Applications by 
Using the Hedonic Motivation System Adoption Model, ” 2020 8th Int. Conf. 
Cyber IT Serv. Manag. CITSM 2020 , 2020, doi: 
10.1109/CITSM50537.2020.9268910. 
[77] O. Mata, I. Mendez, M. Aguilar, P. Ponce, and A. Molina, “A Methodology to 
Motivate Students to Develop Transversal Competencies in Academic 
Courses Based on the Theory of Planned Behavior by using Gamification and 
ANNs,” in Proceedings - IEEE 10th International Conference on Technology for 
Education, T4E 2019, 2019, pp. 174–177, doi: 10.1109/T4E.2019.00041. 
[78] T. Gamst -Klaussen, P. Steel, and F. Svartdal, “Procrastination and personal 
finances: Exploring the roles of planning and financial self -efficacy,” Front. 
Psychol., vol. 10, no. APR, 2019, doi: 10.3389/fpsyg.2019.00775. 
[79] J. J. Xiao, “Applying behavior theories to financial behavior, ” in Handbook of 
Consumer Finance Research, 2008, pp. 69–81. 
[80] J. J. Xiao, C. Tang, J. Serido, and S. Shim, “Antecedents and consequences of 
risky credit behavior among college students: Applicati on a nd extension of 
the theory of planned behavior,” J. Public Policy Mark., vol. 30, no. 2, pp. 239–
245, 2011, doi: 10.1509/jppm.30.2.239. 
[81] D. Fernandes, J. G. Lynch, and R. G. Netemeyer, “Financial literacy, financial 
education, and downstream financ ial behaviors,” Manage. Sci., vol. 60, no. 8, 
pp. 1861–1883, 2014, doi: 10.1287/mnsc.2013.1849. 
[82] R. M. Ryan, C. S. Rigb y, and A. Przybylski, “The motivational pull of video 
games: A self -determination theory approach, ” Motiv. Emot. , vol. 30, no. 4, 
pp. 347–363, 2006, doi: 10.1007/s11031-006-9051-8. 
[83] M. A. Curran, X. Li, M. Barnett, O. Kopystynska, A. B. Chandler, and A . B. 
LeBaron, “Finances, Depressive Symptoms, Destructive Conflict, and 
Coparenting Among Lower -Income, Unmarried Couples: A Two -Wave, 
Cross-Lagged Analysis, ” J. Fam. Psychol. , vol. 35, no. 4, pp. 489 –499, 2021, 
doi: 10.1037/fam0000821. 
[84] S. Joo, “Personal financial wellness, ” in Handbook of Consumer Finance 
Research, Financial Planning Standards Board of Korea, 17th FL., Seongji 
Bldg, Dohwa 2-dong, Mapo-gu, Seoul 121-743, South Korea, 2008, pp. 21–33. 
[85] R. G. Netemeyer, D. Warmath, D. Fernandes, and J. G. Lynch, “How Am i 
Doing? Perceived Financial Well -Being, Its Potential Antecedents, and Its 
Relation to Overall Well -Being,” J. Consum. Res. , vol. 45, no. 1, pp. 68 –89, 
2018, doi: 10.1093/jcr/ucx109. 
[86] G. Gunay, A. A. Boylu, and A. O ğuz, “Determinants of financial management 
behaviors of families, ” in Handbook of Research on Behavioral Finance and 
Investment Strategies: Decision Making in the Financial Industry , 2015, pp. 
236–254. 
[87] O. M. Mugenda, T. K. Hira, and A. M. Fanslow, “Assessing the cau sal 
relationship among communication, money management practices, 
satisfaction with financial status, and satisfaction with quality of life, ” 
Lifestyles Fam. Econ. Issues , vol. 11, no. 4, pp. 343 –360, 1990, doi: 
10.1007/BF00987345. 
[88] A. Bandura, “Self-regulation of motivation and action through goal systems, ” 
--- PAGE 26 ---
  ISSN 2549-7286 (online) 
Indonesian Journal of Computer Science   Vol. 12, No. 2, Ed. 2023 | page 986   
Cogn. Perspect. Emot. Motiv., pp. 37–61, 1988. 
[89] C. Cheshire and J. Antin, “The social psychological effects of feedback on the 
production of internet information pools, ” J. Comput. Commun., vol. 13, no. 3, 
pp. 705–727, 2008, doi: 10.1111/j.1083-6101.2008.00416.x. 
[90] A. N. Kluger and A. DeNisi, “The effects of feedback interventions on 
performance: A historical review, a meta -analysis, and a preliminary 
feedback intervention theor y,” Psychol. Bu ll., vol. 119, no. 2, pp. 254 –284, 
1996, doi: 10.1037/0033-2909.119.2.254. 
  
 


```

```python
import pypdf

def extract_middle_pages(pdf_path):
    with open(pdf_path, 'rb') as f:
        reader = pypdf.PdfReader(f)
        text = ""
        for i in range(12, 23): # Pages 13 to 23 (0-indexed 12 to 22)
            text += f"--- PAGE {i+1} ---\n" + reader.pages[i].extract_text() + "\n"
    return text

middle_text = extract_middle_pages('IJCS_12_3+Prasetyo.pdf')
print(middle_text)


```

```text
--- PAGE 13 ---
  ISSN 2549-7286 (online) 
Indonesian Journal of Computer Science   Vol. 12, No. 2, Ed. 2023 | page 973   
Furthermore, socio -demographic constructs, including e ducation, gender, age, 
income, and marital status, have demonstrat ed significant relevance in prior 
research. Additionally, a psychological construct that bears relevance is self -
control. Turning to antecedents of gamification -related behavioral intention, they 
can be classified into psychological, socio -demographic, soc ial, gamification, and 
context-specific constructs. Notably, these constructs commonly revolve around 
hedonic and affective aspects. Overall, intersecting constructs in financial behavior 
and gamification research  pertain to education, autonomy, control, a nd self -
efficacy, thereby warranting further exploration in the investigation of financial 
behavior and gamification. 
2) Mediators of antecedents and behavi or —Mediators of financial behavior 
and its antecedents can be categorized into psychological, socio -demographic, 
financial-related, and external constructs. Among these, habit is the most 
commonly observed mediating construct between financial behavior and its 
antecedents. On the other hand, mediators of gamification -related behavioral 
intention and its  antecedents can be classified into psychological, technological, 
socio-demographic, external gamification, and context -specific constructs. These 
mediators are predominantly derived from technology adoption theories such as 
the theory of planned behavior,  technology acceptance model, unified theory of 
acceptance and use of technology, expectation -confirmation model, and self -
determination theory. They encompass factors such as attitude, satisfaction, 
perceived ease of use or effort expectancy, perceived us efulness or performance 
expectancy, confirmation, social influence, competence, perceived behavioral 
control, subjective norms, and facilitating conditions. 
3) Moderators of antecedents and behavior — Moderators of financial 
behavior and its antecedents en compass variables such as financial risk tolerance, 
gamifying features, and PFM products. Meanwhile, moderators of gamification -
related behavioral intention and its antecedents primarily revolve around 
constructs associated with gamification. Besides gender differences , moderators 
include achievement-related gamification elements, affective feedback, immersion-
related gamification elements, informational feedback, social feedback, and social -
related gamification elements.  Considering the se findings, it is evident that 
gamifying features and PFM products influence financial behavior.  Given this 
connection between financial behavior and gamification, further exploration of 
both constructs is warranted and holds a substantial interest. 
4) Behavior — This review encompasses a range of constructs that capture 
both financial behavior and gamification -related behavioral intention. In the realm 
of financial behavior, various constructs have been examined, inclu ding savin g, 
spending, investment, deb t, herding, and ret irement behavior. On the other hand, 
in the context of gamification -related behavioral intention, in addition to 
behavioral intention itself, other variables that have been investigated include 
continuance intention, intention to use, discontinuance intent ion, persistent usage 
intentions, reuse intention, and intention. Notably, when comparing the research 
on financial behavior and gamification, it becomes evident that the current focus of 
gamification resear ch leans more toward  behavioral intention rather than the 
actual observed behavior. 
--- PAGE 14 ---
  ISSN 2549-7286 (online) 
Indonesian Journal of Computer Science   Vol. 12, No. 2, Ed. 2023 | page 974   
5) Mediators of behavior and consequences — This review identified 
mediating variables  between financial behavior and its associated consequen ces. 
Two mediators th at emerged from the literature are financial satisfaction and 
short-term financial goals. 
6) Consequences —In the realm of financial behavior, the consequences 
encompass financial well -being, depressive symptoms, hindrances in achieving 
financial goals, fo resight in future saving and spending, happiness, investme nt 
decisions, long-term financial goals, market discipline, and workplace productivity.  
Meanwhile, the consequences linked to gamification -related behavioral intention 
include behavio r, learning out comes, sustained usage, broader system -level 
changes, perceived impact on learning, use behavior, and user behavioral change. 
From these findings, it is interesting to examine if gamification may influence 
financial behavioral intention and manifest into actual financial behavior. 
 This review highlights potential avenues for future research on financial 
behavior and gamification -related behavioral intention. Firstly, in the domain of 
financial behavior,  there is a need to delve deeper into so cio-economic a nd 
demographic antecedents, as suggested by previous studi es [15], [36] . 
Furthermore, the exploration of psychological factors can contribute to a better 
understanding of financial behavior  [29], [44] , particularly in relation to the five 
personality traits: extraversion, agreeableness, conscientiousness, neuroticism, 
and openness [36], [50] . Additionally, it is important to  objectively measure 
subjective factors such as financial wellness [84], [85] and financial satisfaction [1], 
[30], [86], [87] . Lastly, investigating the consequences of financial behavior 
warrants further attention [1], [30]. 
 Regarding gamification-related behavioral intention, future research should 
aim to develop a c omprehensive model that incorporates new design 
characteristics, user demographics, and contextual factors to gain a deeper 
understanding of user motivation, experience, and behavior in relation to 
gamification [57]. Rather than solely focu sing on the effe ctiveness of gamification 
for users who have already adopted it, researchers are encouraged to explore 
determinants of gamification success, as suggested by [21]. F urthermore, 
investigating the potential negative consequences of gamification and methods fo r 
mitigation should also be pursued [21].  
 Future gamification research can also explore the influence of cultural 
factors [11], [64], [69] –[71] and financial background  [72] on gamification 
adoption. Additionally, investigating constructs such as trust, inf ormation 
asymmetry, perceived ris k, and persona l innovation holds promise for enhancing 
understanding of gamification effects [72]. Lastly, specific gamification elements 
warrant further investigation. For example, [61] suggests future research to 
explore a new perspective on gamification feedback by examining normative, 
formative, corrective, positive, and negative feedback [88]–[90]. 
 
Methodology 
 This review identified a range of methods employed in the reviewed 
studies. The studies focusing on financial behavior primarily utilized qua ntitative 
methods, with a predomin ant use of pr imary rather than secondary data. 
Questionnaires were commonly employed to collect primary data, and the analysis 
--- PAGE 15 ---
  ISSN 2549-7286 (online) 
Indonesian Journal of Computer Science   Vol. 12, No. 2, Ed. 2023 | page 975   
of obtained data involved techniques such as structural equation modeling, partial 
least s quares structural equation modeling, a nd confirmatory and exploratory 
factor analysis. 
 For future research on financial behavior, it is recommended to incorporate 
experimental designs to explore the relationship between personal finances and 
financial behavior [29]. Additionally, adopting a longitudinal approach would 
provide valuable insights into how financial be havior and its consequences evolve 
over time [49]. The utilization of lo ngitudinal and experimental approaches 
facilitates the identificati on of direct and indirect relationships between variables  
[29] and helps mitigate common method bias [43], [44] . Lastly, qualitative 
approaches are also valuable in enhancing understanding of financial behavior 
[43]. 
 
Table 8. Methodologies of Financial Behavior Research 
Source Data Collection # 
(%) Data Analysis # 
(%) Ref. 
Primary 
data 
Questionnaire 26 
(81) 
Structural equation 
modeling  
7 
(22) 
[35], [37], [40], 
[41], [44], [46], 
[50] 
Partial least squares 
structural equation 
modeling 
 
6 
(19) 
[4], [29], [34], 
[36], [48], [49] 
Confirmatory factor 
analysis (CFA) 
 
3 
(9.4) 
[38], [39], [46] 
Exploratory factor 
analysis (EFA) 
 
2 
(6.3) 
[39], [46] 
 
Covariance-based 
structural equation 
modeling (CB-SEM) 
 
1 
(3.1) 
[15] 
Exploratory mediational 
analysis with latent 
change scores 
 
1 
(3.1) 
[39] 
Generalized structured 
component analysis 
(GSCA) 
 
1 
(3.1) 
[30] 
Logistic regression 1 
(3.1) 
 
[41] 
Multi-group analysis 
(MGA) 
 
1 
(3.1) 
[35] 
Partial least squares path 
modeling 
 
1 
(3.1) 
[42] 
Welch t-test 
 
1 
(3.1) 
[38] 
--- PAGE 16 ---
  ISSN 2549-7286 (online) 
Indonesian Journal of Computer Science   Vol. 12, No. 2, Ed. 2023 | page 976   
 
Welch analysis of 
variance 
 
1 
(3.1) 
[38] 
Secondary 
data 
2010 National 
Longitudinal Survey of 
Youth 1997 (NLSY97) 
 
1 
(3.1) 
Structural equation 
modeling (SEM) 
2 
(6.3) 
[31], [33] 
the 2016 National 
Financial Well-Being 
Survey 
 
1 
(3.1) 
the Financial Literacy 
and Behavior Among 
Malaysian Young Adults 
project 
 
1 
(3.1) 
Covariance-based 
structural equation 
modeling 
1 
(3.1) 
[43] 
National Survey on 
Financial Inclusion 
2018 
1 
(3.1) 
Generalized structural 
equation models (GSEM) 
with logistic regression 
basis 
 
1 
(3.1) 
[32] 
the 2018 FINRA 
Investor Education 
Foundation’s National 
Financial Capability 
Study (NFCS) 
 
1 
(3.1) 
Stepwise ordinary least 
squares regression 
analysis 
1 
(3.1) 
[47] 
the 2017 Survey of 
Financial Competences 
of Spanish individuals 
1 
(3.1) 
Univariate and 
multivariate analysis 
1 
(3.1) 
[45] 
 
 Similarly to research on fin ancial behavior, most studies investigating 
gamification-related behavioral intention also employ quantitative methods. Data 
collection predominantly relies on questionnaires, while data analysis methods 
commonly include pa rtial least s quares structural equation m odeling, structural 
equation modeling, a nd confirmatory factor analysis. In addition, a few studies 
utilize qualitative methods, such as interviews for data collection and axial coding 
and open coding for analysis. Apart from th e empirical studies reviewed , three 
conceptual studies contribute by  presenting research models that elucidate 
gamification-related behavioral intention. 
 For future research on gamification -related behavioral intention, it is 
recommended to i nvolve larger sample sizes and diverse participants to enhance 
the significance of research findings [53], [54], [57], [60]. Moreover, future studies 
should gather primary and secondary data from various sources to 
comprehensively understand the topic [54]. 
 
Table 9. Methodologies of Gamification-Related Behavioral Intention 
Method Data 
Collection 
# 
(%) Ref Data Analysis # 
(%) Ref 
Quantitative 
 
Questionnaire 25 
(71) 
[7], [11], 
[51]–[56], 
[59]–[64], 
Partial least 
square 
structural 
11 
(24) 
[7], [54], 
[76], [56], 
[61], [66], 
--- PAGE 17 ---
  ISSN 2549-7286 (online) 
Indonesian Journal of Computer Science   Vol. 12, No. 2, Ed. 2023 | page 977   
[66]–[76] equation 
modeling (PLS-
SEM) 
 
[68], 
[70]–[72], 
[74] 
Structural 
equation 
modeling 
(SEM) 
 
11 
(24) 
[11], 
[51]–[53], 
[55], [59], 
[62]–[64], 
[69], [75] 
Confirmatory 
factor analysis 
(CFA) 
 
6 
(13) 
[11], [52], 
[55], [64], 
[69], [73] 
Covariance 
based 
approach 
structural 
equation 
modeling (CB-
SEM) 
 
1 
(2.2) 
[73] 
Cross-temporal 
correlation 
 
1 
(2.2) 
[53] 
Exploratory 
factor analysis 
(EFA) 
 
1 
(2.2) 
[11] 
Harman’s one-
factor analysis 
 
1 
(2.2) 
[55] 
Hierarchical 
multiple 
regression 
 
1 
(2.2) 
[62] 
Mixed analysis 
of variance 
(ANOVA) 
 
1 
(2.2) 
[62] 
Time-lagged 
regression 
 
1 
(2.2) 
[53] 
Variance-based 
SEM 
 
1 
(2.2) 
[60] 
Experiment 3 
(8.6) 
[59], [60], 
[73] 
Analysis of 
variance 
(ANOVA) 
 
1 
(2.2) 
[59] 
Confirmatory 
factor analysis 
(CFA) 
 
1 
(2.2) 
[73] 
Multivariate 
analysis of 
variance 
(MANOVA) 
1 
(2.2) 
[62] 
--- PAGE 18 ---
  ISSN 2549-7286 (online) 
Indonesian Journal of Computer Science   Vol. 12, No. 2, Ed. 2023 | page 978   
 
Qualitative Focus group 1 
(2.8) 
 
[66] Axial coding 
and open 
coding 
2 
(4.4) 
[66], [71] 
Interview 2 
(5.7) 
[57], [71] 
 
   Diagrammatic 
sense-making 
1 
(2.2) 
[57] 
Diary 1 
(2.8) 
[57] 
      
Conceptual 3 
(8.6) 
[58], [65], 
[77] 
Conceptual 3  [58], [65], 
[77] 
 
 
D. Conclusion 
This systematic literature review focused on the domains of financial 
behavior and gamification -related behavioral intention, reveal ing a growing 
interest in these research areas. This review analyzed 53 articles published from 
2018 to 2022 and synthesized them using the TCCM framework to understand the 
current research landscape comprehensively. In addition to providing insights into 
theories, contexts, characteristics, and methodologies employed in current 
research, this review also identifies several areas for future research. 
 
Theoretical Contributions  
 Gamification research has predominantly emerged from the education and 
learning domain, while researc h on gamification in the financial sector remains 
limited. This review h ighlights the theories utilized in past research on financial 
behavior and gamification-related behavioral intention. Given the current lack of a 
robust theoretical foundation in gamification research, researchers must leverage 
this understanding to guide future studies. Additionally, there is an opportunity to 
develop new theories that explore novel aspects of financial behavior and 
gamification-related behavioral int ention. Furthermore, future research should 
encompass a wider range of  contexts, including  different countries, cultures, 
demographics, specific financial apps, and gamification elements. 
 This review identifies various constructs, including antecedents, med iators, 
moderators, and consequences, that contribute to understanding financial 
behavior and gamification -related behavioral intention. This review underscores 
the need for future research to investigate t heir relationships by providing a 
comprehensive overview of these construct s. Furthermore, this review suggests 
additional constructs t o e xplore in future studies to enhance understanding of 
financial behavior and gamification-related behavioral intention. 
 This review also exami nes the methodologies employed in previous 
research and provides guidance for future studies to deepen understanding of 
financial behavior and gamification -related behavioral intention. These 
methodologies encompass experimental, longitudinal, and qual itative approaches 
utilizing primary and secondary data from diverse and large samples. 
 
 
 
--- PAGE 19 ---
  ISSN 2549-7286 (online) 
Indonesian Journal of Computer Science   Vol. 12, No. 2, Ed. 2023 | page 979   
Managerial Implications 
 This review emphasizes the importance of implementing gamification 
strategies to enhance behavioral intention. It encourages financial app managers 
and developers, particularly those involved in PFM apps, to consider integrating 
gamification elements. Im plementing gamification in PFM apps can foster 
behavioral intention toward  various behaviors. The integrated conceptual models 
presented in this review, outlining key variables and their relationships with 
financial behavior and gamification -related behavi oral intention, offer valuable 
guidance for app managers and developers in incorporating gamification. 
  
 In conclusion, this review provides a comprehensive overview of current 
financial behavior and gamification -related behavioral intention research . 
Researchers are encouraged to leverage these findings and pursue future r esearch 
opportunities to enhance understanding of these domains. 
 
E. References 
[1] K. Goyal, S. Kumar, and J. J. Xiao, “Antecedents and consequences of Personal 
Financial Management Behavior: a systematic literature review and future 
research agenda,” Int. J. Bank Mark. , vol. 39, no. 7, pp. 1166 –1207, Jan. 2021, 
doi: 10.1108/IJBM-12-2020-0612. 
[2] V. Sotiropoulos and A. d ’Astous, “Attitudinal, Self-Efficacy, and Social Norms 
Determinants of Young Consumers ’ Propensity to Overspend on Credit 
Cards,” J. Consum. Policy , vol. 36, no. 2, pp. 179 –196, 2 013, doi: 
10.1007/s10603-013-9223-3. 
[3] C. Strömbäck, T. Lind, K. Skagerlund, D. V ästfjäll, and G. Tinghög, “Does self-
control predict financial behavior and financial well -being?,” J. Behav. Exp. 
Financ., vol. 14, pp. 30–38, 2017, doi: 10.1016/j.jbef.2017.04.002. 
[4] K. A. Fachrudin and S. Latifah, “Relationship between individual 
characteristics, neurotic personality, personal financial distress, and 
financial behavior, ” Cogent Bus. Manag. , vol. 9, no. 1, 2022, doi: 
10.1080/23311975.2022.2105565. 
[5] N. Lajuni, I. Bujang, A. A. Karia, and Y. Yacob, “Religiosity, monetary 
knowledge, and monetary beh avior influence on personal monetary distress 
among millennial generation, ” J. Manaj. Dan Kewirausahaan , vol. 20, no. 2, 
pp. 92–98, 2018. 
[6] H. Estelami, “An e thnogrphic study of consumer financial sophistication, ” J. 
Consum. Behav., vol. 13, no. 5, pp. 328–341, 2014, doi: 10.1002/cb.1472. 
[7] P. Bitri án, I. Buil, and S. Catal án, “Making finance fun: the gamification of 
personal financial management apps, ” Int. J. Bank Mark. , vol. 39, no. 7, pp. 
1310–1332, Jan. 2021, doi: 10.1108/IJBM-02-2021-0074. 
[8] M. Jun and S. Palacios, “Examining the key dimensions of mobile banking 
service quality: an exploratory study, ” Int. J. Bank Mark. , vol. 34, no. 3, pp. 
307–326, Jan. 2016, doi: 10.1108/IJBM-01-2015-0015. 
[9] H. Karjaluoto, A. A. Shaikh, H. Saarij ärvi, and S. Saraniemi, “How perceived 
value drives the use of mobile financial services apps,” Int. J. Inf. Manage., vol. 
47, pp. 252–261, 2019, doi: 10.1016/j.ijinfomgt.2018.08.014. 
[10] QYResearch, “Global personal finance apps market size, status and forecast 
--- PAGE 20 ---
  ISSN 2549-7286 (online) 
Indonesian Journal of Computer Science   Vol. 12, No. 2, Ed. 2023 | page 980   
2018-2025,” 2019. https://www.marketresearch.com/QYResearch -Group-
v3531/Global-Personal-Financial- Management-Tools-12732938/ (accessed 
Jun. 15, 2022). 
[11] D. Wong,  H. Liu, Y. Meng -Lewis, Y. Sun, and Y. Zhang, “Gamified money: 
exploring the effectiveness of ga mification in mobile payment adoption 
among the silver generation in China, ” Inf. Technol. People , vol. 35, no. 1, pp. 
281–315, Jan. 2022, doi: 10.1108/ITP-09-2019-0456. 
[12] J. Choudrie, S. Pheeraphuttharangkoon, E. Zamani, and G. Giaglis, 
“Investigating the adop tion and use of smartphones in the UK: A silver -
surfers perspective, ” Investig. Adopt. Use Smartphones UK A Silver -surfers 
Perspect., 2014. 
[13] Y.-H. K im, J. H. Jeon, E. K. Choe, B. Lee, K. Kim, and J. Seo, “TimeAware: 
Leveraging framing effects t o enhance personal productivity, ” in Conference 
on Human Factors in Computing Systems - Proceedings, 2016, pp. 272 –283, 
doi: 10.1145/2858036.2858428. 
[14] S. Deterding, D. Dixon, R. Khaled, and L. Nacke, “From game design elements 
to gamefulness: Defining ‘gamification,’" in Proceedings of the 15th 
International Academic MindTrek Conference: Envisioning Future Media 
Environments, MindTrek 2011 , 2011, pp. 9 –15, do i: 
10.1145/2181037.2181040. 
[15] A. Pal, K. Indapurkar, and K. P. Gupta, "Gamification of financ ial applications 
and financial behavior of young investors, " Young Consum., vol. 22, no. 3, pp. 
503–519, Jan. 2021, doi: 10.1108/YC-10-2020-1240. 
[16] A. J. Kim, "Putting the fun in functional," Software, 2008. 
[17] K. Seaborn and D. I. Fels, "Gamification in theory and action: A survey, " Int. J. 
Hum. Comput. Stud. , vol. 74, pp. 14 –31, 2015, doi: 
10.1016/j.ijhcs.2014.09.006. 
[18] J. Kasurinen and A. Knutas, "Publication trends in gamification: A systematic 
mapping study, " Comput. Sci. Rev. , vol. 27, pp. 33 –44, 2018 , doi: 
10.1016/j.cosrev.2017.10.003. 
[19] J. Koivisto and J. Hamari, "The rise of motivational information systems: A 
review of gamification research, " Int. J. Inf. Manage. , vol. 45, pp. 191 –210, 
2019, doi: https://doi.org/10.1016/j.ijinfomgt.2018.10.013. 
[20] G. Baptista and T. Oliveira, “Why so serious? Gamification impact in the 
acceptance of mobile banking services, " Internet Res., vol. 27, no. 1, pp.  118–
139, 2017, doi: 10.1108/IntR-10-2015-0295. 
[21] J. Koivisto and J. Hamari, "The rise of mot ivational information systems: A 
review of gamification research, " Int. J. Inf. Manage. , vol. 45, pp. 191 –210, 
2019, doi: 10.1016/j.ijinfomgt.2018.10.013. 
[22] J. Paul and A. Rosado -Serrano, "Gradual Internationalization vs Born -
Global/International new ve nture mo dels: A review and research agenda, " 
Int. Mark. Rev., vol. 36, no. 6, pp. 830 –858, 2019, doi: 10.1108/IMR-10-2018-
0280. 
[23] J. Paul and A. R. Criado, "The art of writing literature review: What do we 
know and what do we need to know?," Int. Bus. Rev., vol. 29, no. 4, p. 101717, 
2020, doi: 10.1016/j.ibusrev.2020.101717. 
[24] J. K. Hentzen, A. Hoffmann, R. Dolan, and E. Pala, "Artificial intelligence in 
--- PAGE 21 ---
  ISSN 2549-7286 (online) 
Indonesian Journal of Computer Science   Vol. 12, No. 2, Ed. 2023 | page 981   
customer-facing financial services: a  systematic literature review 
and agenda for future research, " Int. J. Bank Mark. , vol. 40, no. 6, pp. 1299 –
1336, 2022, doi: 10.1108/IJBM-09-2021-0417. 
[25] M. Ghorbani, M. Karampela, and A. Tonner, "Consumers’ brand pers onality 
perceptions in a digital world: A  systematic literature review and research 
agenda,” Int. J. Con sum. Stud. , vol. 46, no. 5, pp. 1960 –1991, 2022, doi: 
10.1111/ijcs.12791. 
[26] A. Akhmedova, A. Manresa, D. Escobar Rivera, and A. Bikfalvi, “Service 
quality in the sharing economy: A review and research agenda, ” Int. J. 
Consum. Stud., vol. 45, no. 4, pp. 889–910, 2021, doi: 10.1111/ijcs.12680. 
[27] S. M. Hassan, Z. Rahman, and J. Pa ul, “Consumer ethics: A review and 
research agenda, ” Psychol. Mark. , vol. 39, no. 1, pp. 111 –130, 2022, doi: 
10.1002/mar.21580. 
[28] B. Kitchenham, “Procedures for perfo rming sy stematic reviews, ” Keele, UK, 
Keele Univ., vol. 33, no. 2004, pp. 1–26, 2004. 
[29] D. Bapat, “Antecedents to responsible financial management behavior 
among young adults: moderating role of financial risk tolerance, ” Int. J. Bank 
Mark., vol. 38, no . 5, pp.  1177–1194, Jan. 2020, doi: 10.1108/IJBM -10-2019-
0356. 
[30] L. K. Meneau and J.  Moorthy, “Struggling to make ends meet: can  consumer 
financial behaviors improve?, ” Int. J. Bank Mark. , vol. 40, no. 2, pp. 263 –296, 
2022, doi: 10.1108/IJBM-12-2020-0595. 
[31] H. Zhao and L. Zhang, “Talking money at home: the value of family financial 
socialization,” Int. J. Bank Mark., vol. 38, no. 7, pp. 1617 –1634, Jan. 2020, doi: 
10.1108/IJBM-04-2020-0174. 
[32] O. Garc ía Mata, “The effect of financial literacy and gen der on r etirement 
planning among young adults, ” Int. J. Bank Mark. , vol. 39, no. 7, pp.  1068–
1090, 2021, doi: 10.1108/IJBM-10-2020-0518. 
[33] H. Park, “Financial behavior among young adult consumers: the influence of 
self-determination and financial psycho logy,” Young Consum., vol. 22, no. 4, 
pp. 597–613, 2021, doi: 10.1108/YC-12-2020-1263. 
[34] A. Lučić, M. Uzelac, and A. Previ šić, “The power of materialism among young 
adults: exploring the effects of values on impulsiveness and responsible 
financial behav ior,” Young Consum. , vol. 22, no. 2, pp. 254 –271, 2021, doi: 
10.1108/YC-09-2020-1213. 
[35] C. Ketkaew, C. Sukitprapanon, and P. Naruetharadhol, “Association between 
retirement behavior and financial goals: A comparison between urban and 
rural citizens in C hina,” Cogent Bus. Manag. , vol. 7, no. 1, 2020, doi: 
10.1080/23311975.2020.1739495. 
[36] K. A. Fachrudin, K. Pirzada, and M. F. Iman, “The role of financial behavior in 
mediating the influence of socioeconomic characteristics and neurotic 
personality traits on fin ancial satisfaction,” Cogent Bus. Manag. , vol. 9, no. 1, 
2022, doi: 10.1080/23311975.2022.2080152. 
[37] V. I. Dewi and L. I. Wardhana, “The nexus of financial literacy and  depositor 
discipline in commercial banks,” Manag. Financ., vol. 48, no. 9/10 , pp. 1472–
1487, Jan. 2022, doi: 10.1108/MF-09-2021-0445. 
[...

```

---

## name: converted-paper
paper_id: "c8b2b27f-2af5-574e-a98f-4cdc89c44ba7"
designation: international
title: "Integrating Financial Management and Gamification: A Systematic Literature Review and Future Research Agenda"
authors: "Prasetyo, A. P.; Santoso, H. B.; Putra, P. O. H."
year: 2023
venue: "Indonesian Journal of Computer Science"
conversion_date: 2026-05-08
original_filename: "IJCS_12_3+Prasetyo.pdf"
version: "1.0"

# Integrating Financial Management and Gamification: A Systematic Literature Review and Future Research Agenda

## Abstract

The implementation of gamification in personal financial management (PFM) apps has the potential to motivate users to engage in positive financial behaviors. However, several research gaps corroborate the need to investigate gamification in the financial domain further. To address these gaps, this systematic literature review comprehensively examines current research on financial behavior and gamification. This review utilizes the Theory, Context, Characteristics, and Methodology (TCCM) framework to provide a holistic understanding of financial behavior and gamification-related behavioral intention. A total of 53 articles published between 2018 and 2022 were analyzed to assess the present research landscape and provide directions for future studies. This review makes three key contributions: (1) synthesizes current research on financial behavior and gamification-related behavioral intention, (2) presents integrated conceptual models that elucidate financial behavior and gamification-related behavioral intention, and (3) identifies research gaps and suggests avenues for future investigation.

**Keywords:** Systematic literature review, financial behavior, gamification, behavioral intention, TCCM

## A. Introduction

In recent years, there has been growing concern regarding the low level of public financial behavior [1]. Researchers have found that many individuals make bad financial decisions, save too little, spend too much [2], and invest in things they later regret [3]. Financial behavior has a significant impact on an individual’s long-term financial outcomes and can lead to long-term financial problems [1], [4]–[6].

The financial sector is among the first to adopt mobile technology [7], [8]. Along with the rise of mobile banking and payment apps [9], personal financial management (PFM) apps have emerged as one of the fastest-growing categories of financial applications [7]. The global PFM application market is expected to reach $3,338 million by 2025 with an annual growth rate of 12.65% from 2018 [10].

However, there is a current challenge in effectively integrating technology to enhance the quality of life [11]–[13]. One way to improve user experience, motivation, and interest is through gamification, the implementation of game features and game-like designs in apps [7], [14]. Gamification has gained significant attention from academic researchers and practitioners [15], [16]. However, most of the existing research related to gamification has focused on the education and learning sector, while other sectors, such as finance, have received limited attention [7], [17]–[19]. This highlights a research gap in gamification in personal finance, despite its recognized importance [15] and widespread adoption [7], [20].

Previous reviews have only examined financial behavior [1] or gamification [21]. Therefore, it is beneficial to address these research gaps by conducting a study that reviews and synthesizes the relationship between these two topics. This study employs a systematic literature review methodology to map the current financial behavior and gamification research state. Specifically, this study aims to bridge the gap between financial behavior with gamification by reviewing research on gamification-related behavioral intention.

This review employs the Theory, Context, Characteristics, and Methodology (TCCM) framework developed by [22]. The TCCM framework provides more comprehensive and robust insights compared to other approaches [23], [24], enabling a holistic understanding of a research domain [25]. Furthermore, the TCCM framework allows for theoretical and empirical mapping of a research field [25]–[27]. This analysis includes 53 articles to review the current state of research and provide directions for future research. Overall, this review provides three contributions by (1) providing a holistic synthesis of existing research on financial behavior and gamification-related behavioral intention, (2) presenting integrated conceptual models that explain financial behavior and gamification-related behavioral intention, and (3) identifying research gaps and providing directions for future research.

The remainder of the paper is structured as follows. Section 2 explains the methodology employed in this systematic literature review. Section 3 presents this review’s results and future research agendas based on the TCCM framework. Finally, Section 4 concludes the study.

## B. Research Method

The systematic literature review was conducted following the methodological guidelines outlined by [28]. This study aims to identify, evaluate, and interpret existing research in the domains of financial behavior and gamification-related behavioral intention using the TCCM framework [25]. The search strategy, study selection process, and data extraction methods are described as follows.

### Search Strategy

Four reputable online research databases were selected: Emerald Insights, IEEE Xplore, Science Direct, and Taylor & Francis. For each domain, specific search strings were developed incorporating relevant key terms. In addition to core terms related to financial behavior and gamification, terms such as “theory," “framework,” and “model” were included. The resulting search strings were as follows:

* (“personal”) AND (“financial” OR “finance”) AND (“management” OR “managing”) AND (“behavior” OR “behavior”) AND (“theory” OR “theoretical” OR “framework” OR “model”)
* (“gamification” OR “gamify” OR “gamified”) AND (“theory” OR “theoretical” OR “framework” OR “model”)

The search was conducted in September 2022, limited to article titles, abstracts, and keywords. Only journal articles and proceedings papers published between 2018 and 2022 were included. This search resulted in 27,888 articles: 20,078 articles on financial behavior and 7,810 articles on gamification-related behavioral intention.

### Study Selection

The study selection process consisted of title and abstract selection, followed by full-text selection. Throughout both steps, articles were assessed based on the following inclusion criteria: (1) articles written in English, (2) articles that investigated either financial behavior or gamification-related behavioral intention, (3) empirical research presenting a research model or hypotheses, and (4) articles that were not literature reviews. Fifty-six relevant articles were identified in the first step: 27 on financial behavior and 29 on gamification-related behavioral intention. In the second step, three articles on financial behavior were excluded, resulting in a final selection of 53 articles.

### Data Extraction

This systematic literature review followed the domain-based approach using the TCCM framework developed by [22]. Relevant publication details such as title, year of publication, and publication outlet were extracted. Furthermore, information related to theories, contexts, characteristics or constructs, and research methodologies was extracted following the TCCM framework. Finally, research limitations and suggestions provided by the authors for future research were extracted to identify potential research directions.

## C. Result and Discussion

### Overview of Reviewed Articles

This section organizes the articles based on their publication year and outlet. Figure 2 illustrates the growth of research on financial behavior and gamification-related behavioral intention from 2018 to 2022. It is evident that research interest in both domains has been increasing in recent years.

Furthermore, Table 1 presents the finance, business, and management journals as publication outlets for articles on financial behavior. On the other hand, Table 2 shows that articles on gamification-related behavioral intention have been published in various journals, including those focused on human-computer interaction, information systems, management, computer science, education, and business. Some articles on gamification-related behavioral intention were also sourced from management and education technology proceedings.

**Table 1. Publication Outlets of Financial Behavior Research**

| Publication Outlet | SJR | # | % | References |
| --- | --- | --- | --- | --- |
| International Journal of Bank Marketing | Q2 | 4 | 16.7 | [29]–[32] |
| Young Consumers | Q1 | 3 | 12.5 | [15], [33], [34] |
| Cogent Business and Management | Q2 | 3 | 12.5 | [4], [35], [36] |
| Managerial Finance | Q3 | 2 | 8.3 | [37], [38] |
| Applied Developmental Science | Q1 | 1 | 4.2 | [39] |
| Economics of Innovation and New Technology | Q1 | 1 | 4.2 | [40] |
| International Journal of Sociology and Social Policy | Q1 | 1 | 4.2 | [41] |
| Journal of Services Marketing | Q1 | 1 | 4.2 | [42] |
| Asia-Pacific Journal of Business Administration | Q2 | 1 | 4.2 | [43] |
| Cogent Social Sciences | Q2 | 1 | 4.2 | [44] |
| Journal of Behavioral and Experimental Economics | Q2 | 1 | 4.2 | [45] |
| Kybernetes | Q2 | 1 | 4.2 | [46] |
| Marriage and Family Review | Q2 | 1 | 4.2 | [47] |
| Review of Behavioral Finance | Q2 | 1 | 4.2 | [48] |
| Journal of Workplace Behavioral Health | Q3 | 1 | 4.2 | [49] |
| Journal of Money and Business | - | 1 | 4.2 | [50] |

**Table 2. Publication Outlets of Gamification-Related Behavioral Intention Research**

| Publication Outlet | SJR | # | % | References |
| --- | --- | --- | --- | --- |
| International Journal of Human-Computer Interaction | Q1 | 3 | 10.3 | [51]–[53] |
| Industrial Management and Data Systems | Q1 | 2 | 6.9 | [54], [55] |
| Information Technology and People | Q1 | 2 | 6.9 | [11], [56] |
| International Journal of Human Computer Studies | Q1 | 2 | 6.9 | [57], [58] |
| Computers in Human Behavior | Q1 | 1 | 3.4 | [59] |
| Enterprise Information Systems | Q1 | 1 | 3.4 | [60] |
| International Journal of Information Management | Q1 | 1 | 3.4 | [61] |
| Internet Research | Q1 | 1 | 3.4 | [62] |
| Journal of Business Research | Q1 | 1 | 3.4 | [63] |
| Journal of Enterprise Information Management | Q1 | 1 | 3.4 | [64] |
| Journal of Further and Higher Education | Q1 | 1 | 3.4 | [65] |
| Journal of Service Theory and Practice | Q1 | 1 | 3.4 | [66] |
| Journal of Small Business and Enterprise Development | Q1 | 1 | 3.4 | [67] |
| Young Consumers | Q1 | 1 | 3.4 | [68] |
| Education and Training | Q2 | 1 | 3.4 | [69] |
| Interactive Technology and Smart Education | Q2 | 1 | 3.4 | [70] |
| International Journal of Bank Marketing | Q2 | 1 | 3.4 | [7] |
| International Journal of Sports Marketing and Sponsorship | Q2 | 1 | 3.4 | [71] |
| Journal of Systems and Information Technology | Q2 | 1 | 3.4 | [72] |
| Learning and Motivation | Q2 | 1 | 3.4 | [73] |
| World Journal of Science, Technology and Sustainable Development | - | 1 | 3.4 | [74] |
| 2019 16th International Conference on Service Systems and Service Management, ICSSSM 2019 | - | 1 | 3.4 | [75] |
| 2020 8th International Conference on Cyber and IT Service Management, CITSM 2020 | - | 1 | 3.4 | [76] |
| Proceedings - IEEE 10th International Conference on Technology for Education, T4E 2019 | - | 1 | 3.4 | [77] |

### Theory

Upon reviewing the literature, it was found that six theories have been employed as theoretical foundations to investigate financial behavior. The theory of planned behavior emerged as the most frequently used theory, accounting for 50% of the studies. Other theories utilized included the family stress theory (16.7%), behavioral life-cycle theory (8.3%), family financial socialization theory (8.3%), management system theory (8.3%), and self-determination theory (8.3%).

While the reviewed studies on financial behavior did not provide specific suggestions for future theory development, a systematic literature review on personal financial management behavior [1] offers potential avenues for theoretical exploration. This review suggests employing interdisciplinary theoretical approaches to examine how individuals’ financial behavior is influenced by different life stages [78], [79]. [1] also proposes investigating the connections between financial education, personal financial management behavior, and life satisfaction [79]–[81]. Additionally, socio-psychological theories could be developed to understand behavioral biases from cultural and social factors [1]. Finally, [1] also recommends employing the theory of planned behavior and the transtheoretical model in investigating diverse behaviors and populations [29].

**Table 3. Theories Used in Financial Behavior Research**

| Theory | # | % | References |
| --- | --- | --- | --- |
| Theory of Planned Behavior | 6 | 50 | [4], [29], [32], [36], [43], [45] |
| Family Stress Theory | 2 | 16.7 | [47], [49] |
| The Behavioral Life-Cycle Theory | 1 | 8.3 | [50] |
| Family Financial Socialization Theory | 1 | 8.3 | [31] |
| Management System Theory | 1 | 8.3 | [47] |
| Self-Determination Theory | 1 | 8.3 | [33] |

On the other hand, 25 theories were identified in studies exploring gamification-related behavioral intention. The majority of these theories (54%) focused on technology adoption. Notably, the self-determination theory (14.3%), technology acceptance model (11.9%), theory of planned behavior (9.5%), expectation-confirmation model (7.1%), and the unified theory of acceptance and use of technology (7.1% for both version 1 and 2) were the most frequently employed. Other theories related to technology use include the continuance theory, diffusion of innovation, flow theory, hedonic motivation system adoption model, uses and gratification theory, and user engagement theory. In addition, there were gamification-specific theories such as the gamification theory, Landers’ theory of gamified learning, and work gamification theory. The remaining theories used in gamification research pertained to psychology (e.g., cognitive absorption theory, cognitive evaluation theory, goal framing theory, goal priming theory, theory of reasoned action, prospect theory, theory of perceived risk, and theory of consumption values) and social theories (e.g., generational cohort theory and social identity theory).

Regarding theoretical development opportunities in gamification-related behavioral intention research, future studies can employ relevant theories to investigate adoption, reuse, and continuance intention [56], [59]. Motivation theory is also suggested as a viable option [53], [82]. Additionally, using existing or new theories on dynamic and cyclical gamification is recommended [21]. Exploring potential similarities between constructs from different theories over time is another avenue for investigation [53].

**Table 4. Theories Used in Gamification-Related Behavioral Intention Research**

| Theory | # | % | References |
| --- | --- | --- | --- |
| Self-Determination Theory | 6 | 14.3 | [7], [51], [57], [59], [67], [70] |
| Technology Acceptance Model | 5 | 11.9 | [7], [11], [52], [70], [73] |
| Theory of Planned Behavior | 4 | 9.5 | [52], [67], [73], [77] |
| Expectation-Confirmation Model | 3 | 7.1 | [56], [64], [69], [75] |
| Unified Theory of Acceptance and Use of Technology 2 | 3 | 7.1 | [53], [71], [72] |
| Unified Theory of Acceptance and Use of Technology | 2 | 4.8 | [68], [74] |
| Cognitive Absorption Theory | 1 | 2.4 | [64] |
| Cognitive Evaluation Theory | 1 | 2.4 | [63] |
| Continuance Theory | 1 | 2.4 | [51] |
| Diffusion of Innovation | 1 | 2.4 | [74] |
| Flow Theory | 1 | 2.4 | [69] |
| Generational Cohort Theory | 1 | 2.4 | [72] |
| Gamification Theory | 1 | 2.4 | [72] |
| Goal Framing Theory | 1 | 2.4 | [54] |
| Goal Priming Theory | 1 | 2.4 | [60] |
| Hedonic Motivation System Adoption Model | 1 | 2.4 | [76] |
| Landers’ Theory of Gamified Learning | 1 | 2.4 | [65] |
| Prospect Theory | 1 | 2.4 | [11] |
| Social Identity Theory | 1 | 2.4 | [51] |
| Theory of Consumption Values | 1 | 2.4 | [62] |
| Theory of Reasoned Action | 1 | 2.4 | [73] |
| Theory of Perceived Risk | 1 | 2.4 | [62] |
| User Engagement Theory | 1 | 2.4 | [55] |
| Uses and Gratification Theory | 1 | 2.4 | [68] |
| Work Gamification Theory | 1 | 2.4 | [55] |

While it is evident that a wide range of theories have been utilized to analyze gamification, there is a narrower selection of theories applied in financial behavior research. Nevertheless, the theory of planned behavior, commonly employed in financial behavior studies, is also relevant to gamification research. Furthermore, the self-determination theory demonstrates relevance in both domains and has the potential for increased utilization in financial behavior research.

### Context

Table 5 summarizes the financial contexts covered in the reviewed articles investigating financial behavior. Most research in this area generally focuses on financial behavior (21%). Other aspects of financial behavior that have been studied include responsible financial behavior, saving behavior, spending behavior, and retirement behavior. Additionally, common research areas include financial literacy (10.5%), financial satisfaction (7.9%), financial well-being (7.9%), financial goals (5.3%), and financial stress (5.3%).

Future research on financial behavior is encouraged to explore previously studied financial behaviors in different countries, cultures, and demographics [45]. Furthermore, investigating financial behavior across various life stages [31], including the transitional period of young adults and their partners [39], [83], is recommended. Additionally, research can focus on financial behavior within different financial sectors, such as banking, insurance, and securities markets [38].

**Table 5. Contexts of Financial Behavior Research**

| Context | # | % | References |
| --- | --- | --- | --- |
| General financial behavior | 8 | 21 | [4], [15], [30], [33], [39], [44]–[46] |
| Financial literacy | 4 | 10.5 | [37], [38], [40], [43] |
| Financial satisfaction | 3 | 7.9 | [36], [39], [47] |
| Financial well-being | 3 | 7.9 | [36], [42], [48] |
| Financial goals | 2 | 5.3 | [35], [39] |
| Financial stress | 2 | 5.3 | [4], [49] |
| Responsible financial behavior | 2 | 5.3 | [29], [34] |
| Saving behavior | 2 | 5.3 | [40], [41] |
| Attitudes | 1 | 2.6 | [45] |
| Depositor discipline | 1 | 2.6 | [37] |
| Family financial socialization | 1 | 2.6 | [31] |
| Financial confidence | 1 | 2.6 | [44] |
| Financial knowledge | 1 | 2.6 | [44] |
| Investment decision | 1 | 2.6 | [50] |
| Learning capacity | 1 | 2.6 | [44] |
| Retirement behavior | 1 | 2.6 | [35] |
| Retirement planning | 1 | 2.6 | [32] |
| Self-control | 1 | 2.6 | [45] |
| Spending behavior | 1 | 2.6 | [40] |
| Workplace productivity | 1 | 2.6 | [49] |

Meanwhile, Table 6 presents the contexts of the reviewed articles investigating gamification-related behavioral intention. These articles explore gamification in education (20.7%), finance (17.2%), games and gamified systems in general (17.2%), health and fitness (17.2%), e-commerce (6.9%), and management (6.9%). Furthermore, gamification research has also started to extend into business, entertainment, environmental, and marketing contexts. Table 7 summarizes the gamification elements investigated or implemented in these reviewed articles. The analysis reveals the involvement of various gamification elements, encompassing achievement-related, social-related, and immersion-related aspects.

Future research on gamification-related behavioral intention is suggested to explore new sectors [72] or types of gamified apps [56]. Specifically, investigating specific gamified apps rather than considering an entire app category as a whole is encouraged [56]. Analyzing these new contexts can deepen the understanding of gamification implementation methods and outcomes [63]. Additionally, future research can explore new gamification elements and the consequences of each element [57], [72]. Elements of gamification that can be further explored include narrative, mechanics, aesthetics, and technological aspects [68]. As mentioned in the systematic literature review by [21], future research can also investigate cooperative and collective gamification.

**Table 6. Contexts of Gamification-Related Behavioral Intention Research**

| Context | # | % | References |
| --- | --- | --- | --- |
| Education | 6 | 20.7 | [51], [57], [65], [69], [70], [77] |
| Finance | 5 | 17.2 | [7], [11], [64], [72], [74] |
| Games and general gamified systems | 5 | 17.2 | [53], [56], [58], [59], [73] |
| Health and fitness | 5 | 17.2 | [52], [60]–[62], [71] |
| E-commerce | 2 | 6.9 | [68], [75] |
| Management | 2 | 6.9 | [55], [59] |
| Business | 1 | 3.4 | [67] |
| Entertainment | 1 | 3.4 | [76] |
| Environmental | 1 | 3.4 | [54] |
| Marketing | 1 | 3.4 | [66] |

**Table 7. Gamification Elements Investigated in Gamification-Related Behavioral Intention Research**

| Gamification Element | # | % | References |
| --- | --- | --- | --- |
| Badge | 6 | 9.7 | [55], [57], [67], [71], [73], [77] |
| Point | 6 | 9.7 | [55], [64], [67], [69], [72] |
| Games | 5 | 8.0 | [53], [64], [68]–[70] |
| Leaderboards | 4 | 6.4 | [53], [55], [67], [73] |
| Monitoring | 4 | 6.4 | [52], [61], [66], [71] |
| Social | 4 | 6.4 | [52], [61], [71], [75] |
| Challenge | 3 | 4.8 | [66], [67], [77] |
| Feedback | 3 | 4.8 | [59], [66], [77] |
| Levels | 3 | 4.8 | [55], [61], [67] |
| Training | 3 | 4.8 | [66], [67], [71] |
| Achievements | 2 | 3.2 | [53], [54] |
| Competition | 2 | 3.2 | [54], [73] |
| Goal | 2 | 3.2 | [52], [73] |
| Prizes | 2 | 3.2 | [72], [73] |
| Rewards | 2 | 3.2 | [52], [72] |
| Autonomy support | 1 | 1.6 | [54] |
| Avatar | 1 | 1.6 | [59] |
| Character | 1 | 1.6 | [66] |
| Cooperation | 1 | 1.6 | [73] |
| Gifting | 1 | 1.6 | [11] |
| Immersion | 1 | 1.6 | [75] |
| Interactivity | 1 | 1.6 | [54] |
| Medals | 1 | 1.6 | [61] |
| Narrative | 1 | 1.6 | [60] |
| Storytelling | 1 | 1.6 | [73] |
| Time constraint | 1 | 1.6 | [73] |

The results also indicate that several studies examine gamification in financial contexts. These studies are conducted by [7], [11], [64], [72], [74]. Most of these studies focus on gamification in banking contexts, as seen in the works of [74], [72], and [11]. Additionally, a study by [64] specifically explores gamification in robo-advisor apps, while a study by [7] concentrates on gamification in the PFM app Mint.

### Characteristics

This review encompasses a range of factors that influence financial behavior and gamification-related behavioral intention, including antecedents, mediators, moderators, and consequences. Figures 3 and 4 illustrate integrated conceptual models depicting financial behavior and gamification-related behavioral intention. We further synthesize these constructs in detail.

1. **Antecedents** — Antecedents of financial behavior can be categorized into several groups: financial-related, socio-demographic, psychological, and external constructs. Financial-related antecedents, such as financial literacy, attitude, and knowledge, have been widely employed to investigate financial behavior. Furthermore, socio-demographic constructs, including education, gender, age, income, and marital status, have demonstrated significant relevance in prior research. Additionally, a psychological construct that bears relevance is self-control. Turning to antecedents of gamification-related behavioral intention, they can be classified into psychological, socio-demographic, social, gamification, and context-specific constructs. Notably, these constructs commonly revolve around hedonic and affective aspects. Overall, intersecting constructs in financial behavior and gamification research pertain to education, autonomy, control, and self-efficacy, thereby warranting further exploration in the investigation of financial behavior and gamification.
2. **Mediators of antecedents and behavior** — Mediators of financial behavior and its antecedents can be categorized into psychological, socio-demographic, financial-related, and external constructs. Among these, habit is the most commonly observed mediating construct between financial behavior and its antecedents. On the other hand, mediators of gamification-related behavioral intention and its antecedents can be classified into psychological, technological, socio-demographic, external gamification, and context-specific constructs. These mediators are predominantly derived from technology adoption theories such as the theory of planned behavior, technology acceptance model, unified theory of acceptance and use of technology, expectation-confirmation model, and self-determination theory. They encompass factors such as attitude, satisfaction, perceived ease of use or effort expectancy, perceived usefulness or performance expectancy, confirmation, social influence, competence, perceived behavioral control, subjective norms, and facilitating conditions.
3. **Moderators of antecedents and behavior** — Moderators of financial behavior and its antecedents encompass variables such as financial risk tolerance, gamifying features, and PFM products. Meanwhile, moderators of gamification-related behavioral intention and its antecedents primarily revolve around constructs associated with gamification. Besides gender differences, moderators include achievement-related gamification elements, affective feedback, immersion-related gamification elements, informational feedback, social feedback, and social-related gamification elements. Considering these findings, it is evident that gamifying features and PFM products influence financial behavior. Given this connection between financial behavior and gamification, further exploration of both constructs is warranted and holds a substantial interest.
4. **Behavior** — This review encompasses a range of constructs that capture both financial behavior and gamification-related behavioral intention. In the realm of financial behavior, various constructs have been examined, including saving, spending, investment, debt, herding, and retirement behavior. On the other hand, in the context of gamification-related behavioral intention, in addition to behavioral intention itself, other variables that have been investigated include continuance intention, intention to use, discontinuance intention, persistent usage intentions, reuse intention, and intention. Notably, when comparing the research on financial behavior and gamification, it becomes evident that the current focus of gamification research leans more toward behavioral intention rather than the actual observed behavior.
5. **Mediators of behavior and consequences** — This review identified mediating variables between financial behavior and its associated consequences. Two mediators that emerged from the literature are financial satisfaction and short-term financial goals.
6. **Consequences** — In the realm of financial behavior, the consequences encompass financial well-being, depressive symptoms, hindrances in achieving financial goals, foresight in future saving and spending, happiness, investment decisions, long-term financial goals, market discipline, and workplace productivity. Meanwhile, the consequences linked to gamification-related behavioral intention include behavior, learning outcomes, sustained usage, broader system-level changes, perceived impact on learning, use behavior, and user behavioral change. From these findings, it is interesting to examine if gamification may influence financial behavioral intention and manifest into actual financial behavior.

This review highlights potential avenues for future research on financial behavior and gamification-related behavioral intention. Firstly, in the domain of financial behavior, there is a need to delve deeper into socio-economic and demographic antecedents, as suggested by previous studies [15], [36]. Furthermore, the exploration of psychological factors can contribute to a better understanding of financial behavior [29], [44], particularly in relation to the five personality traits: extraversion, agreeableness, conscientiousness, neuroticism, and openness [36], [50]. Additionally, it is important to objectively measure subjective factors such as financial wellness [84], [85] and financial satisfaction [1], [30], [86], [87]. Lastly, investigating the consequences of financial behavior warrants further attention [1], [30].

Regarding gamification-related behavioral intention, future research should aim to develop a comprehensive model that incorporates new design characteristics, user demographics, and contextual factors to gain a deeper understanding of user motivation, experience, and behavior in relation to gamification [57]. Rather than solely focusing on the effectiveness of gamification for users who have already adopted it, researchers are encouraged to explore determinants of gamification success, as suggested by [21]. Furthermore, investigating the potential negative consequences of gamification and methods for mitigation should also be pursued [21].

Future gamification research can also explore the influence of cultural factors [11], [64], [69]–[71] and financial background [72] on gamification adoption. Additionally, investigating constructs such as trust, information asymmetry, perceived risk, and personal innovation holds promise for enhancing understanding of gamification effects [72]. Lastly, specific gamification elements warrant further investigation. For example, [61] suggests future research to explore a new perspective on gamification feedback by examining normative, formative, corrective, positive, and negative feedback [88]–[90].

### Methodology

This review identified a range of methods employed in the reviewed studies. The studies focusing on financial behavior primarily utilized quantitative methods, with a predominant use of primary rather than secondary data. Questionnaires were commonly employed to collect primary data, and the analysis of obtained data involved techniques such as structural equation modeling, partial least squares structural equation modeling, and confirmatory and exploratory factor analysis.

For future research on financial behavior, it is recommended to incorporate experimental designs to explore the relationship between personal finances and financial behavior [29]. Additionally, adopting a longitudinal approach would provide valuable insights into how financial behavior and its consequences evolve over time [49]. The utilization of longitudinal and experimental approaches facilitates the identification of direct and indirect relationships between variables [29] and helps mitigate common method bias [43], [44]. Lastly, qualitative approaches are also valuable in enhancing understanding of financial behavior [43].

**Table 8. Methodologies of Financial Behavior Research**

| Source | Data Collection | # (%) | Data Analysis | # (%) | Ref. |
| --- | --- | --- | --- | --- | --- |
| Primary data | Questionnaire | 26 (81) | Structural equation modeling | 7 (22) | [35], [37], [40], [41], [44], [46], [50] |
|  |  |  | Partial least squares structural equation modeling | 6 (19) | [4], [29], [34], [36], [48], [49] |
|  |  |  | Confirmatory factor analysis (CFA) | 3 (9.4) | [38], [39], [46] |
|  |  |  | Exploratory factor analysis (EFA) | 2 (6.3) | [39], [46] |
|  |  |  | Covariance-based structural equation modeling (CB-SEM) | 1 (3.1) | [15] |
|  |  |  | Exploratory mediational analysis with latent change scores | 1 (3.1) | [39] |
|  |  |  | Generalized structured component analysis (GSCA) | 1 (3.1) | [30] |
|  |  |  | Logistic regression | 1 (3.1) | [41] |
|  |  |  | Multi-group analysis (MGA) | 1 (3.1) | [35] |
|  |  |  | Partial least squares path modeling | 1 (3.1) | [42] |
|  |  |  | Welch t-test | 1 (3.1) | [38] |
|  |  |  | Welch analysis of variance | 1 (3.1) | [38] |
| Secondary data | 2010 National Longitudinal Survey of Youth 1997 (NLSY97) | 1 (3.1) | Structural equation modeling (SEM) | 2 (6.3) | [31], [33] |
|  | the 2016 National Financial Well-Being Survey | 1 (3.1) |  |  |  |
|  | the Financial Literacy and Behavior Among Malaysian Young Adults project | 1 (3.1) | Covariance-based structural equation modeling | 1 (3.1) | [43] |
|  | National Survey on Financial Inclusion 2018 | 1 (3.1) | Generalized structural equation models (GSEM) with logistic regression basis | 1 (3.1) | [32] |
|  | the 2018 FINRA Investor Education Foundation’s National Financial Capability Study (NFCS) | 1 (3.1) | Stepwise ordinary least squares regression analysis | 1 (3.1) | [47] |
|  | the 2017 Survey of Financial Competences of Spanish individuals | 1 (3.1) | Univariate and multivariate analysis | 1 (3.1) | [45] |

Similarly to research on financial behavior, most studies investigating gamification-related behavioral intention also employ quantitative methods. Data collection predominantly relies on questionnaires, while data analysis methods commonly include partial least squares structural equation modeling, structural equation modeling, and confirmatory factor analysis. In addition, a few studies utilize qualitative methods, such as interviews for data collection and axial coding and open coding for analysis. Apart from the empirical studies reviewed, three conceptual studies contribute by presenting research models that elucidate gamification-related behavioral intention.

For future research on gamification-related behavioral intention, it is recommended to involve larger sample sizes and diverse participants to enhance the significance of research findings [53], [54], [57], [60]. Moreover, future studies should gather primary and secondary data from various sources to comprehensively understand the topic [54].

**Table 9. Methodologies of Gamification-Related Behavioral Intention**

| Method | Data Collection | # (%) | Ref | Data Analysis | # (%) | Ref |
| --- | --- | --- | --- | --- | --- | --- |
| Quantitative | Questionnaire | 25 (71) | [7], [11], [51]–[56], [59]–[64], [66]–[76] | Partial least square structural equation modeling (PLS-SEM) | 11 (24) | [7], [54], [76], [56], [61], [66], [68], [70]–[72], [74] |
|  |  |  |  | Structural equation modeling (SEM) | 11 (24) | [11], [51]–[53], [55], [59], [62]–[64], [69], [75] |
|  |  |  |  | Confirmatory factor analysis (CFA) | 6 (13) | [11], [52], [55], [64], [69], [73] |
|  |  |  |  | Covariance based approach structural equation modeling (CB-SEM) | 1 (2.2) | [73] |
|  |  |  |  | Cross-temporal correlation | 1 (2.2) | [53] |
|  |  |  |  | Exploratory factor analysis (EFA) | 1 (2.2) | [11] |
|  |  |  |  | Harman’s one-factor analysis | 1 (2.2) | [55] |
|  |  |  |  | Hierarchical multiple regression | 1 (2.2) | [62] |
|  |  |  |  | Mixed analysis of variance (ANOVA) | 1 (2.2) | [62] |
|  |  |  |  | Time-lagged regression | 1 (2.2) | [53] |
|  |  |  |  | Variance-based SEM | 1 (2.2) | [60] |
|  | Experiment | 3 (8.6) | [59], [60], [73] | Analysis of variance (ANOVA) | 1 (2.2) | [59] |
|  |  |  |  | Confirmatory factor analysis (CFA) | 1 (2.2) | [73] |
|  |  |  |  | Multivariate analysis of variance (MANOVA) | 1 (2.2) | [62] |
| Qualitative | Focus group | 1 (2.8) | [66] | Axial coding and open coding | 2 (4.4) | [66], [71] |
|  | Interview | 2 (5.7) | [57], [71] | Diagrammatic sense-making | 1 (2.2) | [57] |
|  | Diary | 1 (2.8) | [57] |  |  |  |
| Conceptual |  | 3 (8.6) | [58], [65], [77] | Conceptual | 3 | [58], [65], [77] |

## D. Conclusion

This systematic literature review focused on the domains of financial behavior and gamification-related behavioral intention, revealing a growing interest in these research areas. This review analyzed 53 articles published from 2018 to 2022 and synthesized them using the TCCM framework to understand the current research landscape comprehensively. In addition to providing insights into theories, contexts, characteristics, and methodologies employed in current research, this review also identifies several areas for future research.

### Theoretical Contributions

Gamification research has predominantly emerged from the education and learning domain, while research on gamification in the financial sector remains limited. This review highlights the theories utilized in past research on financial behavior and gamification-related behavioral intention. Given the current lack of a robust theoretical foundation in gamification research, researchers must leverage this understanding to guide future studies. Additionally, there is an opportunity to develop new theories that explore novel aspects of financial behavior and gamification-related behavioral intention. Furthermore, future research should encompass a wider range of contexts, including different countries, cultures, demographics, specific financial apps, and gamification elements.

This review identifies various constructs, including antecedents, mediators, moderators, and consequences, that contribute to understanding financial behavior and gamification-related behavioral intention. This review underscores the need for future research to investigate their relationships by providing a comprehensive overview of these constructs. Furthermore, this review suggests additional constructs to explore in future studies to enhance understanding of financial behavior and gamification-related behavioral intention.

This review also examines the methodologies employed in previous research and provides guidance for future studies to deepen understanding of financial behavior and gamification-related behavioral intention. These methodologies encompass experimental, longitudinal, and qualitative approaches utilizing primary and secondary data from diverse and large samples.

### Managerial Implications

This review emphasizes the importance of implementing gamification strategies to enhance behavioral intention. It encourages financial app managers and developers, particularly those involved in PFM apps, to consider integrating gamification elements. Implementing gamification in PFM apps can foster behavioral intention toward various behaviors. The integrated conceptual models presented in this review, outlining key variables and their relationships with financial behavior and gamification-related behavioral intention, offer valuable guidance for app managers and developers in incorporating gamification.

In conclusion, this review provides a comprehensive overview of current financial behavior and gamification-related behavioral intention research. Researchers are encouraged to leverage these findings and pursue future research opportunities to enhance understanding of these domains.

## E. References

[1] K. Goyal, S. Kumar, and J. J. Xiao, “Antecedents and consequences of Personal Financial Management Behavior: a systematic literature review and future research agenda,” Int. J. Bank Mark., vol. 39, no. 7, pp. 1166–1207, Jan. 2021, doi: 10.1108/IJBM-12-2020-0612.

[2] V. Sotiropoulos and A. d’Astous, “Attitudinal, Self-Efficacy, and Social Norms Determinants of Young Consumers’ Propensity to Overspend on Credit Cards,” J. Consum. Policy, vol. 36, no. 2, pp. 179–196, 2013, doi: 10.1007/s10603-013-9223-3.

[3] C. Strömbäck, T. Lind, K. Skagerlund, D. Västfjäll, and G. Tinghög, “Does self-control predict financial behavior and financial well-being?,” J. Behav. Exp. Financ., vol. 14, pp. 30–38, 2017, doi: 10.1016/j.jbef.2017.04.002.

[4] K. A. Fachrudin and S. Latifah, “Relationship between individual characteristics, neurotic personality, personal financial distress, and financial behavior,” Cogent Bus. Manag., vol. 9, no. 1, 2022, doi: 10.1080/23311975.2022.2105565.

[5] N. Lajuni, I. Bujang, A. A. Karia, and Y. Yacob, “Religiosity, monetary knowledge, and monetary behavior influence on personal monetary distress among millennial generation,” J. Manaj. Dan Kewirausahaan, vol. 20, no. 2, pp. 92–98, 2018.

[6] H. Estelami, “An ethnographic study of consumer financial sophistication,” J. Consum. Behav., vol. 13, no. 5, pp. 328–341, 2014, doi: 10.1002/cb.1472.

[7] P. Bitrián, I. Buil, and S. Catalán, “Making finance fun: the gamification of personal financial management apps,” Int. J. Bank Mark., vol. 39, no. 7, pp. 1310–1332, Jan. 2021, doi: 10.1108/IJBM-02-2021-0074.

[8] M. Jun and S. Palacios, “Examining the key dimensions of mobile banking service quality: an exploratory study,” Int. J. Bank Mark., vol. 34, no. 3, pp. 307–326, Jan. 2016, doi: 10.1108/IJBM-01-2015-0015.

[9] H. Karjaluoto, A. A. Shaikh, H. Saarijärvi, and S. Saraniemi, “How perceived value drives the use of mobile financial services apps,” Int. J. Inf. Manage., vol. 47, pp. 252–261, 2019, doi: 10.1016/j.ijinfomgt.2018.08.014.

[10] QYResearch, “Global personal finance apps market size, status and forecast 2018-2025,” 2019. [https://www.marketresearch.com/QYResearch-Group-v3531/Global-Personal-Financial-Management-Tools-12732938/](https://www.marketresearch.com/QYResearch-Group-v3531/Global-Personal-Financial-Management-Tools-12732938/) (accessed Jun. 15, 2022).

[11] D. Wong, H. Liu, Y. Meng-Lewis, Y. Sun, and Y. Zhang, “Gamified money: exploring the effectiveness of gamification in mobile payment adoption among the silver generation in China,” Inf. Technol. People, vol. 35, no. 1, pp. 281–315, Jan. 2022, doi: 10.1108/ITP-09-2019-0456.

[12] J. Choudrie, S. Pheeraphuttharangkoon, E. Zamani, and G. Giaglis, “Investigating the adoption and use of smartphones in the UK: A silver-surfers perspective,” Investig. Adopt. Use Smartphones UK A Silver-surfers Perspect., 2014.

[13] Y.-H. Kim, J. H. Jeon, E. K. Choe, B. Lee, K. Kim, and J. Seo, “TimeAware: Leveraging framing effects to enhance personal productivity,” in Conference on Human Factors in Computing Systems - Proceedings, 2016, pp. 272–283, doi: 10.1145/2858036.2858428.

[14] S. Deterding, D. Dixon, R. Khaled, and L. Nacke, “From game design elements to gamefulness: Defining ‘gamification,’" in Proceedings of the 15th International Academic MindTrek Conference: Envisioning Future Media Environments, MindTrek 2011, 2011, pp. 9–15, doi: 10.1145/2181037.2181040.

[15] A. Pal, K. Indapurkar, and K. P. Gupta, "Gamification of financial applications and financial behavior of young investors," Young Consum., vol. 22, no. 3, pp. 503–519, Jan. 2021, doi: 10.1108/YC-10-2020-1240.

[16] A. J. Kim, "Putting the fun in functional," Software, 2008.

[17] K. Seaborn and D. I. Fels, "Gamification in theory and action: A survey," Int. J. Hum. Comput. Stud., vol. 74, pp. 14–31, 2015, doi: 10.1016/j.ijhcs.2014.09.006.

[18] J. Kasurinen and A. Knutas, "Publication trends in gamification: A systematic mapping study," Comput. Sci. Rev., vol. 27, pp. 33–44, 2018, doi: 10.1016/j.cosrev.2017.10.003.

[19] J. Koivisto and J. Hamari, "The rise of motivational information systems: A review of gamification research," Int. J. Inf. Manage., vol. 45, pp. 191–210, 2019, doi: [https://doi.org/10.1016/j.ijinfomgt.2018.10.013](https://www.google.com/url?sa=E&source=gmail&q=https://doi.org/10.1016/j.ijinfomgt.2018.10.013).

[20] G. Baptista and T. Oliveira, “Why so serious? Gamification impact in the acceptance of mobile banking services," Internet Res., vol. 27, no. 1, pp. 118–139, 2017, doi: 10.1108/IntR-10-2015-0295.

[21] J. Koivisto and J. Hamari, "The rise of motivational information systems: A review of gamification research," Int. J. Inf. Manage., vol. 45, pp. 191–210, 2019, doi: 10.1016/j.ijinfomgt.2018.10.013.

[22] J. Paul and A. Rosado-Serrano, "Gradual Internationalization vs Born-Global/International new venture models: A review and research agenda," Int. Mark. Rev., vol. 36, no. 6, pp. 830–858, 2019, doi: 10.1108/IMR-10-2018-0280.

[23] J. Paul and A. R. Criado, "The art of writing literature review: What do we know and what do we need to know?," Int. Bus. Rev., vol. 29, no. 4, p. 101717, 2020, doi: 10.1016/j.ibusrev.2020.101717.

[24] J. K. Hentzen, A. Hoffmann, R. Dolan, and E. Pala, "Artificial intelligence in customer-facing financial services: a systematic literature review and agenda for future research," Int. J. Bank Mark., vol. 40, no. 6, pp. 1299–1336, 2022, doi: 10.1108/IJBM-09-2021-0417.

[25] M. Ghorbani, M. Karampela, and A. Tonner, "Consumers’ brand personality perceptions in a digital world: A systematic literature review and research agenda,” Int. J. Consum. Stud., vol. 46, no. 5, pp. 1960–1991, 2022, doi: 10.1111/ijcs.12791.

[26] A. Akhmedova, A. Manresa, D. Escobar Rivera, and A. Bikfalvi, “Service quality in the sharing economy: A review and research agenda,” Int. J. Consum. Stud., vol. 45, no. 4, pp. 889–910, 2021, doi: 10.1111/ijcs.12680.

[27] S. M. Hassan, Z. Rahman, and J. Paul, “Consumer ethics: A review and research agenda,” Psychol. Mark., vol. 39, no. 1, pp. 111–130, 2022, doi: 10.1002/mar.21580.

[28] B. Kitchenham, “Procedures for performing systematic reviews,” Keele, UK, Keele Univ., vol. 33, no. 2004, pp. 1–26, 2004.

[29] D. Bapat, “Antecedents to responsible financial management behavior among young adults: moderating role of financial risk tolerance,” Int. J. Bank Mark., vol. 38, no. 5, pp. 1177–1194, Jan. 2020, doi: 10.1108/IJBM-10-2019-0356.

[30] L. K. Meneau and J. Moorthy, “Struggling to make ends meet: can consumer financial behaviors improve?,” Int. J. Bank Mark., vol. 40, no. 2, pp. 263–296, 2022, doi: 10.1108/IJBM-12-2020-0595.

[31] H. Zhao and L. Zhang, “Talking money at home: the value of family financial socialization,” Int. J. Bank Mark., vol. 38, no. 7, pp. 1617–1634, Jan. 2020, doi: 10.1108/IJBM-04-2020-0174.

[32] O. García Mata, “The effect of financial literacy and gender on retirement planning among young adults,” Int. J. Bank Mark., vol. 39, no. 7, pp. 1068–1090, 2021, doi: 10.1108/IJBM-10-2020-0518.

[33] H. Park, “Financial behavior among young adult consumers: the influence of self-determination and financial psychology,” Young Consum., vol. 22, no. 4, pp. 597–613, 2021, doi: 10.1108/YC-12-2020-1263.

[34] A. Lučić, M. Uzelac, and A. Previšić, “The power of materialism among young adults: exploring the effects of values on impulsiveness and responsible financial behavior,” Young Consum., vol. 22, no. 2, pp. 254–271, 2021, doi: 10.1108/YC-09-2020-1213.

[35] C. Ketkaew, C. Sukitprapanon, and P. Naruetharadhol, “Association between retirement behavior and financial goals: A comparison between urban and rural citizens in China,” Cogent Bus. Manag., vol. 7, no. 1, 2020, doi: 10.1080/23311975.2020.1739495.

[36] K. A. Fachrudin, K. Pirzada, and M. F. Iman, “The role of financial behavior in mediating the influence of socioeconomic characteristics and neurotic personality traits on financial satisfaction,” Cogent Bus. Manag., vol. 9, no. 1, 2022, doi: 10.1080/23311975.2022.2080152.

[37] V. I. Dewi and L. I. Wardhana, “The nexus of financial literacy and depositor discipline in commercial banks,” Manag. Financ., vol. 48, no. 9/10, pp. 1472–1487, Jan. 2022, doi: 10.1108/MF-09-2021-0445.

[38] O. M. Mugenda, T. K. Hira, and A. M. Fanslow, “Assessing the causal relationship among communication, money management practices, satisfaction with financial status, and satisfaction with quality of life,” Lifestyles Fam. Econ. Issues, vol. 11, no. 4, pp. 343–360, 1990, doi: 10.1007/BF00987345.

[39] A. Bandura, “Self-regulation of motivation and action through goal systems,” Cogn. Perspect. Emot. Motiv., pp. 37–61, 1988.

[40] C. Cheshire and J. Antin, “The social psychological effects of feedback on the production of internet information pools,” J. Comput. Commun., vol. 13, no. 3, pp. 705–727, 2008, doi: 10.1111/j.1083-6101.2008.00416.x.

[41] A. N. Kluger and A. DeNisi, “The effects of feedback interventions on performance: A historical review, a meta-analysis, and a preliminary feedback intervention theory,” Psychol. Bull., vol. 119, no. 2, pp. 254–284, 1996, doi: 10.1037/0033-2909.119.2.254.