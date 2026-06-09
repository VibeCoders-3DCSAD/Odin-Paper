```yaml
paper_id: 10.3390/ijfs14030076
designation: international
title: Financial Education in the Age of Artificial Intelligence: A Systematic Review with Text Mining and Natural Language Processing
authors: Balcazar-Paiva, E. S.; Haro-Sarango, A. F.; Villanueva-Calderón, J. A.
year: 2026
venue: International Journal of Financial Studies
odin_topics:
  - 4.A
  - 4.B
  - 5.A
  - 10.A
  - 10.B
  - 11.A
  - 12.A
shorthand_tags:
  - /existing-systems
  - /gaps
  - /behavioral-profiles
  - /data-privacy
  - /user-trust
  - /engagement
  - /evaluation-frameworks
tldr: AI integration in financial education enables personalization and virtual tutoring but lacks longitudinal evidence and standardized metrics, with ethical concerns over privacy and bias.
problem_and_motivation: The convergence of AI and financial education lacks integrative synthesis despite rapid growth. Existing literature is fragmented without unifying frameworks articulating pedagogical principles with technical capabilities. Ethical and social implications remain underexplored, especially in vulnerable settings.
approach:
  - Systematic review following PRISMA 2020 guidelines.
  - Searched Scopus, ScienceDirect, and Taylor & Francis (388 initial records, 50 included).
  - Combined bibliometric mapping (VOSviewer) with NLP sentiment analysis.
  - Used three sentiment methods: VADER, TextBlob, and XLM-RoBERTa transformer.
  - Computed continuous sentiment_index and text metrics (length, lexical diversity, energy).
  - Quality appraisal adapted to heterogeneous study designs.
findings:
  - "num: 388 initial records reduced to 50 included studies."
  - AI acts as central organizing axis connecting education, finance, and health.
  - "num: Sentiment analysis shows predominantly neutral technical tone with slight positive tilt (sentiment_index mean 0.049)."
  - Longer abstracts correlate with more methodological caution and negativity.
  - Higher lexical diversity associates with opportunity-oriented framing.
  - Field lacks longitudinal studies, standardized metrics, and cultural diversity.
key_figures_tables:
  - "Figure 2: Keyword co-occurrence map shows AI as central hub connecting education, finance, health → AI integrates multiple domains."
  - "Figure 3: Temporal overlay shows shift from pandemic-era themes to generative AI and financial literacy → Field evolving toward conversational AI."
  - "Figure 4: Sentiment histogram shows most abstracts cluster near zero polarity → Neutral technical register dominates."
  - "Figure 5: Correlation matrix shows sentiment_index aligns with transformer positivity, length correlates with negativity → Abstract length biases sentiment interpretation."
  - "Table 1: Summary statistics report mean sentiment_index 0.049, mean word count 218 → Quantitative framing of discourse."
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: AI
    definition: Artificial Intelligence, technologies performing tasks associated with human intelligence.
  - term: NLP
    definition: Natural Language Processing, computational analysis of human language.
  - term: PRISMA
    definition: Preferred Reporting Items for Systematic Reviews and Meta-Analyses.
  - term: VADER
    definition: Valence Aware Dictionary and sEntiment Reasoner, lexicon-based sentiment tool.
  - term: XLM-RoBERTa
    definition: Cross-lingual RoBERTa transformer model for multilingual sentiment.
  - term: SDG
    definition: Sustainable Development Goals (UN).
critical_citations:
  - "[Zhu, 2025] — Defines machine learning for financial literacy detection."
  - "[Leal & Oliveira, 2024] — Introduces hypernudging in AI financial behavior."
  - "[Wahyudi et al., 2025] — Notes scarcity of longitudinal studies."
  - "[AL-Ghuribi et al., 2025] — Emphasizes privacy and bias as structural conditions."
relevance:
  topics:
    - code: 4.A
      name: Landscape of Existing Personal Finance Systems
      justification: Systematically maps AI tools applied to financial education.
    - code: 4.B
      name: Limitations and Gaps in Existing Systems
      justification: Identifies lack of longitudinal studies and standardized metrics.
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      justification: Discusses AI-assisted nudging and behavioral personalization.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      justification: Highlights privacy, fairness, and algorithmic bias as structural conditions.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      justification: Reviews transparency and trust determinants in robo-advisors.
    - code: 11.A
      name: Engagement Dynamics in Personal Finance Applications
      justification: Covers chatbots, recommender systems, and user interaction.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      justification: Provides methodological template combining bibliometrics and NLP sentiment analysis.
  contribution: "This systematic review offers Odin a comprehensive landscape of AI applications in financial education, directly informing the existing systems analysis (4.A). It identifies critical gaps including the shortage of longitudinal studies, lack of standardized metrics, and limited cultural diversity, which Odin must address in its gap analysis (4.B). The review's emphasis on privacy, fairness, transparency, and algorithmic bias provides actionable requirements for Odin's data privacy (10.A) and user trust (10.B) modules. Its methodological combination of bibliometric mapping and NLP sentiment analysis offers a transferable evaluation framework for Odin's system assessment (12.A). The discussion of behavioral AI and nudging supports Odin's behavioral profiling considerations (5.A)."
  directly_justifies:
    - "AI enables personalization and virtual tutoring in financial education."
    - "Evidence of sustained behavioral change from AI financial education remains nascent."
    - "Privacy, fairness, and algorithmic bias are structural conditions for responsible adoption."
    - "Longitudinal and controlled studies are scarce in AI financial education research."
    - "Sentiment analysis of academic abstracts can reveal discursive framing biases."
  limits:
    - "Systematic review does not provide causal evidence of AI effectiveness."
    - "Sentiment analysis applied only to abstracts, not full texts."
    - "Geographic diversity limited by English/Spanish database search."
    - "No meta-analysis due to methodological heterogeneity of included studies."
  mapping_rationale: "The paper was screened against Odin's functional domains. Landscape (4.A) and gaps (4.B) directly apply as the paper systematically maps existing AI tools and identifies research gaps. Behavioral profiling (5.A) was selected because the paper discusses AI-assisted nudging and behavioral personalization, though not classification algorithms. Data privacy (10.A) and user trust (10.B) are strongly supported by sections on ethics, regulation, bias, and transparency. Engagement (11.A) applies via discussion of user interaction with chatbots and recommender systems. Evaluation frameworks (12.A) apply due to the paper's methodological contribution of combining bibliometrics and NLP sentiment analysis. Rejected topics include expense categorization (3.A/B), spending forecasting (6.A/B), budget recommendation (7.A/B/C), anomaly detection (8.A/B), mobile-first design (9.A/B), and savings/debt management (13.A/B) as the paper does not address these specific PFMS modules."
limitations:
  - "Search restricted to three databases, missing gray literature and manual reference searching [acknowledged]."
  - "Sentiment analysis tools (VADER, TextBlob) less reliable in Spanish [acknowledged]."
  - "Lack of standardized metrics across studies prevents meta-analysis [acknowledged]."
  - "Transformer model trained on social media text may not fully generalize to academic writing [acknowledged]."
  - "No direct measurement of pedagogical effectiveness from sentiment analysis [acknowledged]."
  - "Exclusion of non-English/non-Spanish literature may introduce language bias [unacknowledged]."
remember_this:
  - "AI in financial education shows neutral technical tone with slight optimism."
  - "Longer abstracts include more caution about ethics and risks."
  - "Sentiment_index mean 0.049 indicates mild positive framing."
  - "Field lacks longitudinal evidence of sustained financial behavior change."
  - "Privacy and bias are structural conditions, not afterthoughts."
```