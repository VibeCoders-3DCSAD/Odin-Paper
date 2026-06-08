# Wealth Creation for Expanding the Middle Class in the Philippines

## Metadata

```yaml
---
paper_id: "10.62986/dp2024.10"
designation: local
title: "Wealth Creation for Expanding the Middle Class in the Philippines"
authors: "Albert, J. R. G.; Briones, R. M.; Rivera, J. P. R."
year: 2024
venue: "PIDS Discussion Paper Series No. 2024-10"
odin_topics: ["A.1", "G.1"]
shorthand_tags: ["/income-typology", "/expenditure-patterns", "/fies-bsp-mapping", "/cultural-expense-types"]
member_checklist:
  - name: "Gabion, Stefanie S."
    status: "[ ]"
  - name: "Guevarra, Joaquin Luis T."
    status: "[ ]"
  - name: "San Jose, Alexa Joanne Paula G."
    status: "[ ]"
  - name: "Togle, Charles Nathaniel B."
    status: "[ ]"
---
```

## TL;DR

The Philippine middle class, defined as households with per capita income 2–12 times the poverty line, grew to **39.8%** of the population by 2021 but the pandemic reversed gains from the 43.5% peak in 2018.

## Problem and Motivation

The Philippines lacks an updated, data-driven profile of its middle class and a coherent strategy for wealth creation amid global headwinds like climate change and digital disruption. A strong middle class drives inclusive growth, domestic consumption, and social stability, yet no prior post-pandemic study had integrated socioeconomic characteristics with actionable policy pathways. What was missing was a comprehensive, evidence-based assessment of the middle class’s size, composition, and vulnerability to inform targeted expansion policies.

## Approach

- Dataset: 2021 Family Income and Expenditure Survey (FIES) and July 2021 Labor Force Survey (LFS), plus prior FIES rounds (1991, 2006, 2015, 2018).
- Definition: Per capita income relative to official poverty lines — poor (<1x), low-income (1–2x), lower middle (2–4x), middle middle (4–7x), upper middle (7–12x), upper-income (12–20x), rich (≥20x). Middle class = clusters 3–5 (2–12x).
- Geographic scope: National, with regional and urban/rural disaggregation.
- Key metrics: Income distribution, educational attainment, employment status, expenditure shares, asset ownership, OFW remittance contribution.
- Analysis method: Descriptive statistics, trend analysis over three decades, and merged FIES-LFS for labor outcomes.

## Findings

1. The middle class grew from 28.5% of the population in 1991 to **43.5% in 2018**, then fell to **39.8% in 2021** (34.4 million Filipinos).
2. Urban areas host 60.6% of the middle class vs. 33.8% in rural areas; NCR has the highest concentration (62.0% middle class).
3. Middle class households have average size 3.6 members vs. 5.0 for low-income; 40.6% of middle-class adults (15+) completed college vs. 14.5% of low-income.
4. Employed middle-class individuals hold permanent jobs at 79.5%, compared to 31.4% short-term/casual among low-income workers.
5. OFW remittances contribute 8.5% of total income for middle-class families, with 74.7% of OFW families belonging to the middle class.
6. Middle-class expenditure shares: food 41.9%, transportation 8.8%, health 3.2%, education 1.3% — all higher shares than low-income households.

- Middle-class households own mobile phones (98% urban, 93% rural) and have access to improved water sources (81.3% vs. 59.4% for low-income).

## Key Figures and Tables

- Figure 1: Size and share of middle class 1991–2021 → middle class peaked at 43.5% in 2018, dropped to 39.8% in 2021.
- Figure 2: Income clusters by urban/rural → urban middle class 60.6%; rural only 33.8%.
- Figure 6: Educational attainment by income class → middle class: 40.6% college; low-income: 14.5% college.
- Figure 10: Expenditure shares by income class → middle class spends more on transport (8.8%), health (3.2%), education (1.3%).
- Table 5: Average remittances by income cluster → OFW remittances = 8.5% of middle-class family income.

## Key Equations

None.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| FIES | Family Income and Expenditure Survey — Philippine household survey on income and spending. |
| LFS | Labor Force Survey — quarterly survey on employment and unemployment. |
| OFW | Overseas Filipino Worker — Filipino worker employed abroad. |
| PPP | Purchasing Power Parity — adjustment for cost-of-living differences across countries. |
| Per capita income | Total household income divided by number of household members. |
| Poverty line | Minimum income needed to meet basic food and non-food needs (varies by province and urban/rural). |
| Middle class (this paper) | Households with per capita income between 2x and 12x the official poverty line. |

## Critical Citations

- [Easterly, 2001] — Foundational theory that larger middle class leads to better institutions and growth.
- [Banerjee & Duflo, 2008] — Middle class as key driver of entrepreneurship and human capital investment in developing countries.
- [Ravallion, 2009] — Vulnerability of the middle class to economic shocks in developing economies.

## Relevance to Odin

**Topics:**

A.1 — Spending and Budgeting Behavior of Filipino Young Professionals

G.1 — Expense Categorization in Filipino Personal Finance Contexts

**Contribution to Odin:**

This paper provides empirically grounded baseline data on how Filipino households across income classes allocate spending, directly informing Odin’s expense categorization module grounded in FIES categories. The income typology (2–12x poverty line) helps define the target user segment — young professionals likely fall into lower-middle to middle-middle income ranges, with predictable expenditure shares on food, transport, health, and education. The finding that 79.5% of middle-class workers hold permanent jobs supports Odin’s spending forecasting module assumption of stable income patterns, while OFW remittance data (8.5% of income) highlights an irregular income source that must be handled by both forecasting and anomaly detection. Although the paper is macroeconomic, its micro-level household expenditure breakdowns are directly citable for justifying Odin’s category structure and spending pattern baselines in the Philippine context.

**Directly justifies:**

- “As of 2021, 39.8% of Filipinos belong to the middle class, with average family size 3.6 — smaller than low-income families — indicating higher discretionary spending capacity per capita.”
- “Middle-class households allocate 8.8% of expenditure to transportation, 3.2% to health, and 1.3% to education, providing baseline category weights for Odin’s budget recommendation logic.”
- “40.6% of middle-class Filipinos aged 15+ have completed college, suggesting digital literacy and readiness for mobile-first financial management tools.”
- “OFW remittances contribute 8.5% of total income for middle-class families — an irregular income stream that Odin’s forecasting and anomaly detection modules must accommodate.”
- “The COVID-19 pandemic reduced the middle-class share from 43.5% (2018) to 39.8% (2021), demonstrating income shock vulnerability that Odin’s anomaly detection should monitor as behavioral deviation.”

**Limits of relevance:**

- The paper focuses on macroeconomic wealth creation policy, not personal budget management systems or mobile app design.
- Data is from 2021, post-pandemic disruptions may not represent long-term stable spending patterns for young professionals.
- Income-based classification does not directly map to Odin’s behavioral profiles (Stable-Flexible, Variable-Obligated, etc.).
- No analysis of digital financial app usage or transaction-level data — only survey aggregates.
- The middle class definition includes older adults (not limited to 20–40 age range), so per-category spending shares may differ for young professionals specifically.

## Limitations

- Cross-sectional data from 2021 FIES cannot track individual household mobility into or out of the middle class over time. [unacknowledged]
- The income-based definition (2–12x poverty line) is arbitrary and may exclude lower-income households with middle-class consumption patterns. [acknowledged in Technical Annex]
- No analysis of digital financial literacy or mobile banking adoption among middle-class Filipinos, limiting direct applicability to Odin’s mobile-first design. [unacknowledged]
- COVID-19 pandemic disrupted 2021 data collection and income patterns, so findings may not reflect baseline pre-pandemic behavior. [acknowledged in text]
- Regional variations are reported but not linked to digital infrastructure or financial app usage, which would be needed for Odin’s deployment in Metro Manila vs. other regions.

## Remember This

- 🔑 **39.8%** of Filipinos were middle class in 2021 — down from 43.5% before the pandemic.
- 📌 Middle class spends 8.8% on transport, 3.2% on health — key categories for Odin’s budget allocation.
- 💡 40.6% of middle-class adults completed college — high digital literacy supports mobile-first design.
- ⚠️ OFW remittances = 8.5% of middle-class income — irregular inflows require robust forecasting.
