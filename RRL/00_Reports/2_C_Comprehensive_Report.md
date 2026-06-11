# Comprehensive Report for Subtopic: `2.C`

**Total files:** 5

This report includes problem/motivation, approach, key findings, support for Odin, and limitations/contradictions.

---


## Exploring the Influence of Financial Literacy and Lifestyle Choices on Financial Management Practices among Young Workers in Batam City's Urban Landscape
**Filename:** `I--Raya_summarized.md`  
**Authors:** Raya, S. I. (2024)  
**ID:** `d9e8f7a6-5b4c-3d2e-1f0a-9b8c7d6e5f4a`  
**Odin Topics:** 1.C, 2.C, 5.A, 7.A, 13.A, 13.B  

**TLDR:** Higher financial literacy correlates with better financial management among young workers in Batam City, while urban lifestyle choices and peer influence negatively affect spending and debt practices.

**Problem & Motivation:** Young workers in Batam City face financial challenges from rising living costs and diverse lifestyle options. Limited financial literacy exacerbates inadequate planning, debt accumulation, and insufficient savings. The interplay between lifestyle choices and financial literacy lacks comprehensive research, necessitating this study.

**Approach (summary):**
- Mixed-methods design combining quantitative surveys and qualitative semi-structured interviews/focus groups.
- Purposive sample of young workers across diverse ages, education levels, and employment sectors in Batam City.
- Survey collected demographics, lifestyle choices, financial literacy levels, and financial management practices.

**Key Findings (selected):**
- Positive correlation between higher financial literacy and more robust savings habits.
- Urban lifestyle associated with greater challenges in debt management.
- Lifestyle preferences for entertainment and discretionary spending correlate with conservative investment approaches.
- Discrepancy exists between theoretical financial knowledge and practical application in daily decisions.

**Limitations / Contradictions for Odin:**
- Sample size constraints limit generalizability beyond Batam City.
- Self-reporting biases in survey responses may affect validity.
- Subjective nature of qualitative data introduces potential interpretation bias.

**Key takeaways:**
- Financial literacy alone does not guarantee prudent financial decisions due to lifestyle pressures.
- Urban living and peer influence are key determinants of young workers' financial behaviors.
- Tailored financial education should bridge theory and practical application.

---


## Optimized Financial Planning: Integrating Individual and Cooperative Budgeting Models with LLM Recommendations
**Filename:** `IA--de_Zarza-et_al_summarized.md`  
**Authors:** de Zarzà, I.; de Curtò, J.; Roig, G.; Calafate, C.T. (2024)  
**ID:** `10.3390/ai5010006`  
**Odin Topics:** 7.A, 7.B, 7.C, 13.A, 2.C  

**TLDR:** Integrates LLM recommendations into individual and cooperative budgeting optimization models to maximize savings while respecting user preferences and constraints.

**Problem & Motivation:** Financial planning is complex and overwhelming for non-experts. Traditional methods lack personalization and adaptability to dynamic needs. There is a need for accessible, AI-driven budgeting tools that combine mathematical optimization with practical recommendations.

**Approach (summary):**
- Synthetic financial data for ten households with normally distributed income and expenses across rent, groceries, utilities, and entertainment.
- Optimization models for individual and cooperative budgeting maximizing savings subject to non‑negativity and income constraints.
- Uses GPT‑4 to generate percentage‑based allocation recommendations for expense categories, savings, debt, and investments.

**Key Findings (selected):**
- LLM‑generated recommendations align with established financial planning principles such as emergency funds, retirement savings, and consumption smoothing.
- num: The LLM‑recommended savings allocation included 20% for emergency funds, 15% for retirement, and 10% for non‑retirement savings.
- Cooperative budgeting with LLM advice leads to more balanced allocations across household members.
- Long‑term LLM recommendations incorporate life‑cycle model principles, including consumption smoothing and future event planning.

**Limitations / Contradictions for Odin:**
- "LLM recommendations may contain hallucinations or errors [unacknowledged] (paper proposes mitigations but does not test them empirically)."
- "The simulation uses synthetic data; real‑world validation is missing [unacknowledged]."
- "Long‑term dependencies are acknowledged but not modeled in the optimization equations [acknowledged] (paper discusses future work)."

**Key takeaways:**
- "LLM recommendations can allocate 20% of income to emergency funds."
- "Cooperative budgeting with LLM increases household savings potential."
- "Optimization with LLM bounds outperforms LLM‑only advice in simulations."

---


## Recommendation system for financial decision-making using Artificial intelligence
**Filename:** `IA--Shuryhin-&-Zinovatna_summarized.md`  
**Authors:** Shuryhin, K. A.; Zinovatna, S. L. (2024)  
**ID:** `10.15276/aait.07.2024.24`  
**Odin Topics:** 2.C, 6.A, 6.B, 7.B, 7.C, 8.A, 8.B, 10.A, 10.B  

**TLDR:** Combines Isolation Forest for anomaly detection, ARIMA and LSTM for budget forecasting, and large language models to generate personalized financial recommendations while addressing ethical concerns like privacy and user autonomy.

**Problem & Motivation:** Cognitive biases lead to irrational financial decisions, and AI-enhanced marketing can manipulate consumer behavior. Existing recommendation systems in finance often lack personalization, fail to account for user autonomy, or ignore ethical considerations. There is a need for an intelligent system that provides unbiased, personalized financial advice without manipulation.

**Approach (summary):**
- Input data includes user transaction history, spending anomalies, budget forecasts, and user parameters like risk tolerance and financial goals.
- Isolation Forest isolates anomalies by building binary trees and calculating path lengths; anomaly score near 1 indicates anomalous expense.
- ARIMA(p,d,q) models short-term dependencies with autoregressive and moving average components after differencing for stationarity.

**Key Findings (selected):**
- Isolation Forest effectively identifies atypical financial actions by isolating deviations from normal spending patterns.
- Combining ARIMA (short-term) and LSTM (long-term) improves budget forecast stability and accuracy.
- LLM-generated recommendations adapt to different income levels and user-specific risk levels, goals, and preferences.
- The system promotes responsible financial behavior without imposing decisions, enhancing user awareness and autonomy.

**Limitations / Contradictions for Odin:**
- No quantitative validation of forecasting or anomaly detection accuracy. [unacknowledged]
- The system's LLM component is described only conceptually; no ablation study or comparison with rule-based baselines. [unacknowledged]
- Ethical claims are not operationalized or measured (e.g., how to verify user autonomy). [unacknowledged]

**Key takeaways:**
- Anomaly detection uses Isolation Forest with path length scoring.
- Forecasts combine ARIMA for short-term and LSTM for long-term trends.
- Large language model generates personalized financial advice from transaction and forecast data.

---


## "Consumer Finance Survey 2021"
**Filename:** `L--Bangko_Sentral_ng_Pilipinas-2021_summarized.md`  
**Authors:** "Bangko Sentral ng Pilipinas" (2021)  
**ID:** `f47ac10b-58cc-4372-a567-0e02b2c3d479`  
**Odin Topics:** 1.A, 1.B, 1.C, 2.A, 2.C, 3.A, 4.A, 4.B, 5.A, 10.B, 13.A, 13.B  

**TLDR:** The 2021 Consumer Finance Survey by the Bangko Sentral ng Pilipinas provides comprehensive data on income, expenditure, assets, liabilities, and demographics of Filipino households, revealing trends in financial inclusion, digital adoption, and debt during the COVID-19 pandemic.

**Problem & Motivation:** There were significant data gaps on household wealth and indebtedness in the Philippines, as existing surveys like FIES and APIS had limited coverage of assets and liabilities. Collecting detailed financial condition data was necessary to inform evidence-based socio-economic policies and monetary decisions. The survey aimed to provide a comprehensive picture of household balance sheets, income sources, spending patterns, and demographic characteristics.

**Approach (summary):**
- "Sample of 18,000 households drawn from PSA's 2013 Master Sample (two-stage cluster sampling) covering all regions including BARMM."
- "Face-to-face interviews using structured CAPI questionnaire, translated into six major languages, conducted from March to December 2022."
- "Reference period for income and expenditure was calendar year 2021; assets and liabilities as of interview date."

**Key Findings (selected):**
- "num: 91.5% of households had wage income in 2021, up from 73.7% in 2018."
- "num: Only 29.3% of households carried any debt, down from 40.4% in 2018."
- "num: 35.3% owned deposit accounts, significantly up from 9.7% in 2018."
- "num: 24.3% owned electronic money accounts, up from 0.3% in 2018."

**Limitations / Contradictions for Odin:**
- "Estimates with coefficients of variation above 20 percent should be interpreted with caution."
- "Recall bias may affect income and expenditure values reported for the previous year."
- "Non-sampling errors from intentional under-reporting of assets and liabilities. [unacknowledged]"

**Key takeaways:**
- "Wage income source increased to 91.5% of households during the pandemic."
- "Debt prevalence dropped to 29.3% as households reduced borrowing."
- "Digital financial assets grew rapidly: e-money accounts up to 24.3%."

---


## A Descriptive-Correlational Analysis of Social Media Usage and Personal Finance Competencies Among University Students
**Filename:** `L--Cadayunan-et_al_summarized.md`  
**Authors:** Cadayunan, A. M. G.; Fabe, A. C. M.; Tingabngab, G. T.; Bagtong, S. M. D. (0)  
**ID:** `7c9e6679-7425-40de-944b-e07fc1f90ae7`  
**Odin Topics:** 1.A, 1.C, 2.C, 5.A, 13.A, 13.B  

**TLDR:** High social media use correlates moderately with financial literacy and decision-making among Filipino university students, but a knowledge-action gap persists.

**Problem & Motivation:** Social media's influence on financial competencies among Filipino university students is understudied. While digital platforms can disseminate financial information, they also introduce behavioral risks. This gap hinders efforts to promote practical financial literacy within university settings.

**Approach (summary):**
- Descriptive-correlational design with stratified random sampling of 173 BSBA students from Bukidnon State University Talisayan Campus.
- Survey measured social media usage (platforms, frequency) and personal finance competencies (financial literacy and decision-making abilities).
- Pearson correlation coefficient and two-tailed significance test used to analyze relationships.

**Key Findings (selected):**
- Social media usage is high, with Facebook and TikTok as most preferred platforms.
- Financial literacy reported as high, but practical application (budget adherence, regular saving) is lower.
- Decision-making abilities rated as moderate, with difficulty resisting impulse purchases.
- num: Moderate positive correlation between social media frequency and financial literacy (r=0.359, p<0.001).

**Limitations / Contradictions for Odin:**
- Correlational design prevents causal inference.
- Self-reported financial literacy may not reflect objective competence.
- Sample limited to business students at one campus, not representative of all Filipino young professionals.

**Key takeaways:**
- Social media use correlates moderately with financial literacy (r=0.359).
- High knowledge does not guarantee good financial behavior.
- Impulse buying is a major barrier to sound decisions.

---


## Note for the Agent

The summaries above contain **essential extracts** – enough to understand each paper's relevance to Odin, including supporting evidence and limitations.
If you need additional details not shown here (e.g., **critical citations, definitions, equations, full methodology, or the complete mapping rationale**),
**ask the user to send the original summary file (`<filename>_summarized.md`) or the converted MarkItDown file(`<filename>_marked.md`)** for the specific paper(s) of interest.
Do not invent missing information. Acknowledge gaps when they exist.