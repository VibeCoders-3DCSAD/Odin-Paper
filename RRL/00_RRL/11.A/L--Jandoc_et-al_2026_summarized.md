# Profiling Platform Workers in the Philippines: Evidence from the Jobs and Skills Survey

## Metadata

```yaml
---
paper_id: "f47ac10b-58cc-4372-a567-0e02b2c3d479"
designation: local
title: "Profiling Platform Workers in the Philippines: Evidence from the Jobs and Skills Survey"
authors: "Jandoc, K. R. L.; Martinez, A.; Bulan, J. A. N.; Molato, R.; Guyos, A."
year: 2026
venue: "UP School of Economics Discussion Papers"
odin_topics: ["1.A", "1.B", "1.C", "2.B", "5.A", "11.A"]
shorthand_tags: ["/yp-profile", "/income-patterns", "/budgeting-prevalence", "/calendar-spending-cycles", "/profiling-role", "/concept-drift", "/drop-off-patterns"]
member_checklist:
  - name: "Gabion, Stefanie S."
    status: "[ ]"
  - name: "Guevarra, Joaquin Luis T."
    status: "[X]"
  - name: "San Jose, Alexa Joanne Paula G."
    status: "[ ]"
  - name: "Togle, Charles Nathaniel B."
    status: "[ ]"
---
```

## TL;DR

Platform workers in the Philippines—disproportionately young, urban, highly educated, and concentrated in NCR—face volatile earnings and weak social protection, with transport workers pushed by necessity and home-based freelancers drawn by flexibility.

## Problem and Motivation

No nationally representative data exists on the scale, demographics, and job quality of Filipino platform workers, limiting evidence-based policy. Understanding this growing workforce is critical for inclusive labor markets and adaptive social protection under the Philippine Development Plan 2023–2028. Prior studies relied on small or platform-specific samples, preventing systematic comparison across worker types and with traditional employment.

## Approach

- Data: 2025 Jobs and Skills Survey (JSS), a nationally representative rider to the Labor Force Survey (LFS), with 9,244 employed respondents.
- Definition: Platform workers are those who used an online platform for paid tasks in the past two years, across four types: home-based digital work, outside-home services, ride-hailing, and delivery.
- Methods: Weighted descriptive statistics, two-sample t-tests for mean differences, and logit regressions for participation, benefits, and satisfaction.
- Key measures: Routine Task Intensity (RTI) index (higher = more automatable tasks), self-reported skill mismatch (overskilled/matched/underskilled), and employer-provided benefits (pension, health, separation pay).
- Controls in regressions: age, sex, education, urbanity, occupation, industry, firm size, exporter status, ownership, online sales presence.

## Findings

1. **8.2%** of workers (≈4.1 million) use platforms; **84.5%** report it as their sole job, averaging 42.6 hours/week.
2. Platform workers are 74.0% urban, 69.7% have higher education, and 31.0% are in NCR (vs. 15% of all workers).
3. Flexibility (88.9%) and ease of entry (79.6%) are top motivations; necessity-driven entry is higher for drivers (18.1% lack alternatives) than home-based workers (9.3%).
4. Platform workers have lower RTI (**-0.19**) than non-platform workers (**+0.56**), indicating less routine, more analytical/interpersonal tasks, but drivers/delivery workers show positive RTI (+0.12, +0.15).
5. **Overskilling** is more common among daily platform users (22.5%) than non-users (14.8%), especially for computer/software skills (42.6% vs. 26.4%).
6. After controlling for worker and firm characteristics, platform workers have significantly lower odds of employer pension contributions (logit coeff: **-1.33**), health insurance (**-0.95**), and separation benefits (**-0.81**).

- Home-based and delivery workers face the largest benefit deficits; drivers show no significant pension/health gap but lower paid leave.
- Job satisfaction and perceived safety are high across all groups (≥90%), with no significant difference after controls.

## Key Figures and Tables

- Figure 2: Mean standardized RTI by platform worker type → Platform workers have less routine work (-0.19) than non-platform (+0.56); home-based lowest (-0.73), delivery highest (+0.15).
- Table 2: Profile of platform workers vs. all workers → 31% of platform workers in NCR vs. 15% overall; 69.7% with higher education vs. 31.5%.
- Table 7: Motivations by worker type → Flexibility highest for home-based (90.7%); necessity-driven (lack of alternatives) highest for drivers (18.1%).
- Table 12: Benefit coverage by employer and worker type → Only 40.1% of drivers and 44.3% of delivery workers have separation benefits, vs. 57.4% of home-based workers.
- Table 13: Logit regressions of benefits → Platform vs. non-platform: pension coeff -1.33 (p<0.01), health -0.95 (p<0.01), separation -0.81 (p<0.01).

## Key Equations

None.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| RTI (Routine Task Intensity) | Index measuring how much a job consists of repetitive, automatable tasks vs. analytical, interpersonal, or adaptable manual work. Higher = more routine. [think: RTI = how easily a robot could do it] |
| JSS (Jobs and Skills Survey) | Nationally representative survey rider to the Philippine LFS, capturing task content, skills, and platform work. |
| LFS (Labor Force Survey) | Philippine government household survey measuring employment, unemployment, and underemployment. |
| PDP (Philippine Development Plan 2023–2028) | National policy framework for inclusive labor markets and adaptive social protection. |
| NCR (National Capital Region) | Metro Manila; accounts for 31% of platform workers but only 15% of all workers. |
| Overskilling | Worker reports having skills higher than required for their current job. |
| Platform worker | Uses online/mobile app to perform paid tasks or services (home-based digital, outside-home services, ride-hailing, or delivery). |

## Critical Citations

- [Esguerra, 2019] — Documents that Philippine social insurance systems are anchored in standard employer–employee relationships, excluding platform workers.
- [Bayudan-Dacuycuy & Baje, 2021] — Early evidence on decent work deficits and gendered patterns in Filipino crowdwork.
- [Gianan, 2023] — Qualitative study showing delivery riders face low net earnings and limited alternatives, mirrored in JSS necessity-driven motives.
- [ILO, 2021] — Global benchmark showing only 41% of online platform workers have health insurance and 20% have pensions.

## Relevance to Odin

**Topics:**

1.A — Filipino Young Professionals as a Demographic

1.B — Financial Structure of Filipino Young Professionals

1.C — Financial Behavior of Filipino Young Professionals

2.B — Seasonal and Cyclical Spending Patterns

5.A — Financial Behavioral Profiles in Personal Finance

11.A — Engagement Dynamics in Personal Finance Applications

**Contribution to Odin:**

This paper directly informs Odin's behavioral profiling and engagement modules by characterizing income volatility and financial vulnerability among Filipino platform workers—a segment overlapping heavily with Odin's target demographic of young professionals. The finding that 84.5% of platform workers rely on this as their sole job, combined with volatile earnings and weak social protection, justifies Odin's design for users with irregular income patterns and validates the need for dynamic, adaptive budget recommendations rather than static templates. The high overskilling rate (22.5% among daily platform users) suggests that Odin's users may have cognitive and digital skills exceeding typical financial app demands, supporting a design that avoids patronizing simplicity and instead offers sophisticated controls and explanations. The documented concentration of platform work in urban, highly educated prime-age workers matches Odin's user profile, making the paper's income and employment patterns directly applicable as domain knowledge for forecasting and anomaly detection.

**Directly justifies:**

- "Among Filipino platform workers, 84.5% rely on platform work as their sole job, with average weekly hours (42.6) comparable to full-time employment, indicating that non-traditional work is a primary livelihood, not a marginal supplement."
- "Platform workers face significantly lower odds of employer-provided pension (logit coeff -1.33), health insurance (-0.95), and separation benefits (-0.81) even after controlling for firm characteristics—evidence of systemic benefit precarity that affects income stability and financial planning."
- "Daily platform users report 22.5% overskilling (vs. 14.8% among non-users), with the largest gaps in software (42.6% vs. 26.4%) and communication skills (38.5% vs. 22.0%), indicating that many Filipino young professionals in platform work have skill levels exceeding job demands."
- "Necessity-driven entry (lack of other satisfactory income sources) is nearly twice as high among delivery (17.7%) and driving (18.1%) platform workers than home-based digital workers (9.3%), showing that income volatility and limited alternatives push some users into gig work."

**Limits of relevance:**

- The paper profiles employment characteristics, not spending behavior or budgeting practices—financial management inferences are indirect.
- Data are cross-sectional; causal relationships between platform work and financial outcomes are not established.
- The JSS does not track transaction-level spending, so forecasting or anomaly detection algorithms cannot be directly benchmarked against its findings.
- Platform worker categories (home-based, outside-home, driving, delivery) are distinct from Odin's functional modules; mapping requires care (e.g., income volatility applies to all, but task content relevance differs).

## Limitations

- Cross-sectional design prevents causal claims about whether platform work causes benefit deficits or simply attracts workers from unprotected sectors. [unacknowledged]
- JSS relies on self-reported skills and overskilling, which may be inflated by highly educated workers in low-complexity tasks. [unacknowledged]
- No longitudinal tracking of earnings volatility or income shocks, limiting direct use for forecasting model design.
- RTI index, while standardized, may not capture all task nuances specific to Filipino platform work (e.g., cash handling, algorithmic rating stress).
- Sample sizes for some platform worker subgroups (e.g., drivers) limit statistical power in regressions, reflected in non-significant coefficients for some benefit models.

## Remember This

- 🔑 **8.2% of Filipino workers use platforms** (~4.1M) — 84% as sole job, 42.6 hours/week → primary livelihood.
- 📌 Benefit gaps are large: pension (coeff -1.33), health (-0.95), separation (-0.81) after controls.
- ⚠️ 88.9% cite flexibility, but 18% of drivers lack alternatives — necessity and opportunity coexist.
- 💡 Overskilling rate 22.5% for daily users — Odin users may be more skilled than typical app assumes.
- 📍 31% of platform workers in NCR vs. 15% of all workers — urban concentration shapes income patterns.
