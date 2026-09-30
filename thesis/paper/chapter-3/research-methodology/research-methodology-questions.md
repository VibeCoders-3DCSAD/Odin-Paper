# 3.2 Research Methodology — Question Log

Status last updated: 2026-09-25
Source: questions raised during the review of `research-methodology-v1.md`, with answers from group deliberation, plus clarity, redundancy, and missing-element notes from the same review.

## Status Overview

| # | Section | Question | Status |
|---|---------|----------|--------|
| 1 | 3.2.1 | Locale rationale (why NCR when the reference data is national) | Unanswered — to be deliberated |
| 2 | 3.2.3 | IT-expert inclusion criteria | Answered |
| 3 | 3.2.3 | Specific number of respondents per group | Answered |
| 4 | 3.2.4 | Who responded to each survey and number of responses collected | Answered (partially — see note) |
| 5 | 3.2.5 | When and how the survey was distributed and number of responses collected | Answered |
| 6 | 3.2.6 | Number of evaluators per group | Answered |
| 7 | 3.2.7 | Model-specific performance metrics and where they will be reported | Unanswered — pending |
| 8 | 3.2.8 | Institutional permission / ethics approval | Answered |
| 9 | 3.2.8 | Ethics coverage for the system evaluation phase (consent, anonymity) | Unanswered — to be clarified |
| 10 | 3.2.3 / 3.2.6 | Recruitment procedure for evaluation respondents (how, where, online/onsite) | Unanswered — to be clarified |
| 11 | 3.2.4 | Reliability/validity citations for instruments (SUS source, ISO/IEC 25010) | Unanswered — to be added |

## Answered Questions

### 2. 3.2.3 Sampling Technique – IT-expert inclusion criteria

> [QUESTION: confirm the inclusion criteria, such as relevant educational background, years of experience, or specialization in software development and testing]

**ANSWER:** No inclusion criteria for IT experts for now.

### 3. 3.2.3 Sampling Technique – Sample size per group

> [QUESTION: confirm whether a specific number of respondents per group is required]

**ANSWER:** 30 IT experts and 10 Non-IT experts. *(Updated inline in `research-methodology-v1.md`.)*

### 4. 3.2.4 Research Instruments – Survey respondents and response counts

> [QUESTION: confirm who responded to each survey and the number of responses collected]

**ANSWER:** Both the PUEPS and the preliminary investigation survey will be used as pre-survey instruments. The PUEPS collected 47 responses, distributed online through Google Forms.
**NOTE:** The number of responses for the preliminary investigation survey is not yet stated — confirm whether it is the same distribution as the PUEPS or a separate count.

### 5. 3.2.5 Data Gathering Procedure – Survey distribution details

> [QUESTION: confirm when and how the survey was distributed and the number of responses collected] *(appears in both the original and revised text)*

**ANSWER:** The PUEPS was distributed online through Google Forms and collected 47 responses. The exact date of distribution is not yet stated.

### 6. 3.2.6 System Evaluation Procedure – Evaluators per group

> [QUESTION: confirm the number of evaluators per group]

**ANSWER:** SUS: 10 Non-IT experts; ISO 25010: 30 IT experts.

### 8. 3.2.8 Ethical Considerations – Institutional permission

> [QUESTION: confirm whether institutional permission is required before conducting the study, given that the survey was administered through a public form]

**ANSWER:** Ethics approval is not needed.

## Unanswered / Pending Questions

### 1. 3.2.1 Research Locale – Rationale for NCR

**QUESTION:** The locale is justified on the basis that the reference data are drawn from national statistics (PSA FIES 2023 and HFCE quarterly series), but national statistics would justify national coverage rather than NCR specifically — why is the study limited to NCR?

**STATUS:** To be deliberated.

### 7. 3.2.7 Statistical Treatment of Data – Model-specific performance metrics

> [QUESTION: identify the model-specific performance metrics for the classification, forecasting, optimization, and anomaly detection models, and confirm whether these will be reported in this section or in the system development methodology.]

**STATUS:** Pending — not yet decided. To be confirmed in the group.

### 10. 3.2.3 / 3.2.6 – Recruitment procedure for evaluation respondents

**QUESTION:** How will the 10 Non-IT and 30 IT evaluation respondents be recruited (e.g., online posting, personal networks, referrals), and where will the evaluation be conducted (online or onsite)?

**STATUS:** To be clarified (related to questions 9 and 3).

### 11. 3.2.4 – Reliability/validity citations for instruments

**QUESTION:** Should the section cite the SUS (e.g., Brooke, 1996) and the ISO/IEC 25010 standard to establish the reliability/validity of the evaluation instruments?

**STATUS:** To be added.

## Resolved Items (no longer open)

- **6. Informed consent / DPA wording** — **RESOLVED:** Revised to "an informed consent statement compliant with the Data Privacy Act of 2012."
- **7. System evaluation vs. technical system testing** — **RESOLVED:** Revised; the statement that system evaluation is kept separate from technical system testing (reported in Chapter 4) is retained.

## Clarity Issues

1. **Tense consistency (all sections).** Past tense is correct for the already-administered preliminary survey; everything else should stay in future tense. In sentences that mix both (e.g., "was administered … and will serve as the basis"), make the past→future transition explicit (e.g., "was administered during the requirements phase and will serve as…").

2. **Unexplained jargon (§3.2.5).** "Temporally disaggregated into monthly expense estimates with seasonal expense patterns" needs a short clarification for first-time readers and panelists, e.g., "splitting the quarterly HFCE totals into monthly estimates using the HFCE series as a seasonal indicator," or cite the disaggregation method.

3. **Terminology: "Non-IT Experts" vs "IT experts" (§3.2.2/3.2.3).** Inconsistent capitalization, and "Non-IT Expert" is an awkward label since "expert" implies expertise. Suggest "end-user respondents (non-IT)" for clarity.

4. **"Weighted mean" target (§3.2.7).** State that the weighted mean will be computed per ISO 25010 characteristic (functional suitability, performance efficiency, etc.); otherwise it is unclear what is being averaged.

5. **Age bound omission (§3.2.1).** The locale paragraph says "Filipinos residing in the NCR," while the stated scope (Chapter 1) is "Filipinos aged 18 to 59 in the NCR." Include the age range in the locale paragraph for consistency.

6. **No sample size / recruitment method in the narrative.** Purposive sampling should be accompanied by a target *N* per group (now answered) and a "how respondents will be recruited" sentence (question 10).

## Redundancies

1. **§3.2.3 — Sampling justification said twice.** The purposive-sampling rationale ("non-probability technique to gather insights from individuals who can provide meaningful and specific feedback… will be chosen based on specific qualifications") repeats the same claim in consecutive sentences. Keep one justification sentence, then the criteria.

2. **§3.2.4 and §3.2.5 — Preliminary survey narrated twice.** The survey is described in both the Research Instruments paragraph and the Data Gathering Procedure paragraph. Keep the instrument *description* in 3.2.4 and only the *chronological sequencing* in 3.2.5.

3. **§3.2.5 and §3.2.6 — Evaluation flow described twice.** "The completed application will be evaluated by qualified respondents using the instruments described above" (3.2.5) re-appears in more detail in 3.2.6. Split cleanly: 3.2.5 states the timeline, 3.2.6 states who evaluates what.

4. **Dataset names repeated.** FIES/HFCE are spelled out in the locale, instruments, data-gathering, and ethics paragraphs. Spell them out once; use "the PSA datasets" afterwards.

5. **§3.2.8 — Triple restatement of data availability.** "Published and publicly available … free to use … publicly published by the PSA on their website" says the same thing three times in one sentence. Simplify to "only datasets published openly by the PSA."

## Missing Elements (vs. standard methodology guidance)

Typical methodology guidance (e.g., Scribbr) expects the chapter to cover the research approach, data collection details, analysis methods, and justification of choices. Items currently absent or thin:

1. **Bridge to the research design (3.1).** No sentence connects the descriptive + developmental design to this section. Add a one-sentence transition at the start of 3.2.
2. **Sample size justification.** Per your own 3.2.3 guidelines, "sample size should be justified according to the study purpose, qualified participant pool, inclusion criteria, and evaluation requirements" — the headcounts now exist (question 3), but the justification sentence does not.
3. **Recruitment procedure for evaluation respondents** (question 10) — how, where, online/onsite.
4. **Reliability/validity of instruments** (question 11) — cite the SUS and ISO/IEC 25010 as established instruments.
5. **Description of the preliminary survey instrument** — what it measures and its structure, since it feeds the user/system requirements.
6. **Justification of methodological choices** — brief rationale for purposive sampling, SUS, ISO 25010, and the weighted mean.
7. **Ethics for the evaluation phase** (question 9) — consent, voluntariness, and anonymity for SUS and ISO 25010 respondents.
8. **Model-specific performance metrics** (question 7) — classification, forecasting, optimization, and anomaly detection metrics, and where they will be reported.