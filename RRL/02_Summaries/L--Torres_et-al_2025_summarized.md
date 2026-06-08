# The Shift to Gig Economy: How Traditional Employment Stacks Up Against Platform-Based Independent Workers

## Metadata

```yaml
---
paper_id: "10.1145/3785171.3785197"
designation: local
title: "The Shift to Gig Economy: How Traditional Employment Stacks Up Against Platform-Based Independent Workers"
authors: "Torres, R. C.; Bartolome, Z. M. I.; Jimena, L. G.; Paner, J. P."
year: 2025
venue: "The 9th International Conference on Business and Information Management (ICBIM 2025)"
odin_topics: ["A.1", "F.1"]
shorthand_tags: ["/income-typology", "/income-type-behavior-diff", "/fil-behavioral-patterns"]
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

Traditional employees have higher debt-to-income ratios than gig workers, but both groups show similar financial literacy, social support, and job satisfaction levels.

## Problem and Motivation

There is a lack of direct comparative analysis between platform-based gig workers and traditional employees on financial and social outcomes in the Philippine context. Understanding these differences matters because the rapid growth of the gig economy raises concerns about income instability, debt accumulation, and financial resilience among Filipino workers. Prior studies examined gig workers in isolation without systematically comparing them to traditional employees across financial literacy, debt-to-income ratio, social support, and job satisfaction.

## Approach

- Sample: 276 gig workers and 307 traditional employees recruited via purposive sampling across five Philippine provinces.
- Gig worker definition: freelance or platform-based jobs (ride-hailing, online freelancing). Traditional employee definition: full-time positions with formal contracts and benefits.
- Instrument: self-administered Google Forms survey with five sections: demographics, financial literacy multiple-choice, debt-to-income (DTI) calculation, social support Likert scale, and Job Satisfaction Survey (JSS).
- Statistical method: Mann-Whitney U test (non-parametric) after Shapiro-Wilk test rejected normality for all dependent variables.
- Theoretical framework: Dual Labor Market Theory (primary vs. secondary labor market).

## Findings

1. No significant difference in financial literacy between groups: median score 9 for both (p = 0.267).
2. **Traditional employees had a significantly higher median DTI ratio (40) than gig workers (31.41), p < 0.001.**
3. No significant difference in social support networks: traditional median 3.75, gig median 3.63 (p = 0.135).
4. No significant difference in job satisfaction: traditional 3.56, gig 3.67 (p = 0.797).

- Qualitative responses indicate gig workers value autonomy and flexibility, while traditional workers value stability and benefits.
- Some gig workers reported never receiving helpful information from work peers, highlighting inconsistent access to professional support.

## Key Figures and Tables

- Table 1: Summary of Mann-Whitney U test results for all four dependent variables → DTI is the only significant difference (U = 34567, p < 0.001); all others non-significant.

## Key Equations

None.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| Gig economy | Short-term, flexible, platform-mediated work arrangements (e.g., ride-hailing, freelancing). |
| Platform-based gig workers | Individuals earning income through digital labor platforms (e.g., Grab, Upwork, Fiverr). |
| Traditional employees | Full-time workers with formal employment contracts, benefits, and job security. |
| Debt-to-Income (DTI) ratio | Monthly debt payments divided by gross monthly income; measures debt burden relative to earnings. |
| Financial literacy | Ability to understand and use financial skills including budgeting, saving, investing, and debt management. |
| Dual Labor Market Theory | Economic theory dividing labor into a stable primary market (benefits, security) and a volatile secondary market (gig work). |
| Mann-Whitney U test | Non-parametric statistical test comparing two independent groups when data is not normally distributed. |
| JSS | Job Satisfaction Survey; a standardized instrument measuring satisfaction across multiple work dimensions. |

## Critical Citations

- [Luthi, 2024] — Defines DTI ratio and its role as a financial health indicator; used as the study's primary debt metric.
- [Sopan, 2023] — Discusses financial literacy challenges specific to gig workers; informs the study's financial literacy framework.
- [Kaiser et al., 2022] — Establishes that financial education affects both knowledge and downstream behaviors; grounds the study's literacy measurement.

## Relevance to Odin

**Topics:**

A.1 — Spending and Budgeting Behavior of Filipino Young Professionals

F.1 — User Behavioral Profiling in Filipino Personal Finance Contexts

**Contribution to Odin:**

This paper directly informs Odin's user profiling module (F.1) by providing empirical evidence on how employment type (traditional vs. gig) shapes financial indicators — specifically DTI ratios and financial literacy — among Filipino workers. The finding that gig workers maintain lower DTI ratios despite income volatility suggests more cautious debt behavior, which Odin's profile classification could use as a behavioral signal. The parity in financial literacy across both groups indicates that Odin cannot assume traditional employees have superior financial knowledge; instead, the system must design budget recommendations and financial nudges that work for both stable and volatile income profiles. Although the paper does not target budgeting directly, its comparative framework on financial behavior across income types justifies Odin's decision to treat income stability as a key profiling dimension.

**Directly justifies:**

- "Traditional employees have a significantly higher median DTI ratio (40) than gig workers (31.41), indicating greater debt burden despite more stable income (p < 0.001)."
- "No statistically significant difference in financial literacy exists between traditional employees and gig workers (median 9 for both, p = 0.267), meaning employment type does not predict financial knowledge."
- "Gig workers report similar job satisfaction levels to traditional employees (3.67 vs. 3.56, p = 0.797), with autonomy and flexibility cited as key satisfiers despite income instability."
- "Social support networks do not differ significantly between groups (p = 0.135), though some gig workers report zero access to professional guidance, indicating uneven distribution."

**Limits of relevance:**

- The study population includes five Philippine provinces but not specifically Metro Manila, where Odin's target young professionals are concentrated; urban income and spending patterns may differ.
- Sample includes both ride-hailing and online freelancing gig workers; Odin's user base may skew toward white-collar young professionals, not delivery or transport workers.
- No direct measurement of budgeting behavior, spending categories, or savings rates — only DTI and self-reported financial literacy.
- Cross-sectional design captures a snapshot; Odin's profiling requires understanding how behavior changes over time (concept drift).

## Limitations

- Purposive sampling limits generalizability; findings may not represent all gig workers or traditional employees in the Philippines.
- Data is self-reported, introducing potential recall and social desirability bias, especially for debt and financial literacy questions. [unacknowledged]
- No breakdown by age group; Odin targets 20–40 year olds, but the study includes workers of all ages. [unacknowledged]
- The study does not control for income level, education, or geographic location within provinces, making it difficult to isolate the effect of employment type alone. [unacknowledged]
- Qualitative insights are reported anecdotally (single quotes) rather than systematically analyzed, reducing their weight for RRL citation.

## Remember This

- 📌 **DTI ratio: traditional 40 vs. gig 31.41** — traditional workers carry more debt despite stable jobs.
- 🔑 Financial literacy median 9 for both groups — employment type does not predict financial knowledge.
- 💡 Gig workers value autonomy — job satisfaction matches traditional employees even with income uncertainty.
- ⚠️ No age breakdown — unknown if findings hold for Odin's 20–40 young professional target.
