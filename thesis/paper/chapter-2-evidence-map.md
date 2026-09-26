# Chapter 2 Evidence Map (V3.0)

Generated 2026-09-26 against `GROUP4 - CHAPTER 2 - V3 - 09.26.26.docx`.

Every author-date citation in the chapter body was resolved against the 91-paper
BUDI-Literature corpus. Counts: 15 resolved cleanly, 1 corrected, 3 **missing from the corpus**, 1 secondary citation.

| Cited as | Resolves to | Corpus stem | Metadata | Status |
| --- | --- | --- | --- | --- |
| Yoganandham (2025) | Yoganandham (2025) | `I--Yoganandham-2025` | verified | ok |
| Cumaio et al. (2026) | Cumaio et al. (2026) | `I--Cumaio-2026` | verified | ok (venue fixed, see log) |
| The Bangko Sentral ng Pilipinas (2026) | The Bangko Sentral ng Pilipinas (2026) | `L--BangkoSentral-2026` | verified | ok |
| Yeo et al. (2023) | Yeo et al. (2023) | `I--Yeo-2023` | verified | ok |
| Claro and Noval (2025) | Claro and Noval (2025) | `L--Claro-2025` | verified | ok |
| de Zarzà et al. (2024) | de Zarzà et al. (2024) | `A--DeZarza-2024` | verified | ok |
| Esperanza et al. (2025) | Esperanza (2025) | `L--Esperanza-2025` | verified | corrected |
| Francisco et al. (2026) | Francisco et al. (2026) | `L--Francisco-2026` | verified | ok (venue fixed, see log) |
| Alenazi and Sas (2023) | Alenazi and Sas (2023) | `A--Alenazi-2023` | verified | ok |
| Bitrián et al. (2021, as cited by Alenazi & Sas, 2023) | Bitrián et al. (2021, as cited by Alenazi & Sas, 2023) | `(secondary, no corpus entry needed)` | unverified | secondary citation |
| Laspiñas and Murcia (2024) | Laspiñas and Murcia (2024) | `— not in corpus —` | unverified | ok |
| Dey and Arefin (2025) | Dey and Arefin (2025) | `— not in corpus —` | unverified | **MISSING** |
| Lu et al. (2025) | Lu et al. (2025) | `A--Lu-2025` | verified | ok |
| Gulbakyt et al. (2025) | Gulbakyt et al. (2025) | `A--Gulbakyt-2025` | verified | ok |
| Santiago et al. (2025) | Santiago et al. (2025) | `L--Santiago-2025` | verified | ok |
| Huang et al. (2025) | Huang et al. (2025) | `A--Huang-2025` | verified | ok (reverted, see log) |
| Zhong (2025) | Zhong (2025) | `A--Zhong-2025` | verified | ok (was 'unpublished', see log) |
| D'Souza et al. (2026) | D'Souza et al. (2026) | `A--DSouza-2026` | verified | ok (4 authors, see log) |
| Dasmariñas et al. (2024) | Dasmariñas et al. (2024) | `— not in corpus —` | unverified | **MISSING** |
| Srisamai and Siriruk (2023) | Srisamai and Siriruk (2023) | `— not in corpus —` | unverified | **MISSING** |
## What this means

**The 15 clean resolutions are not all equally solid.** Metadata in the sidecar is marked
`verified` only where it was read off page 1 of the source PDF. As of 2026-09-26 that is 23 of
the 91 entries; the other 68 carry conversion frontmatter only. Of the works this chapter leans
on, the unverified ones are cited on the strength of the source filename alone, which is exactly
the failure mode that produced the seven wrong stems fixed in BUDI-Literature. Closing the rest
is the next metadata task.

**Two of the entries marked `verified` were wrong**, so the mark cannot be trusted without
reading the page. One was a false negative (Huang, six authors behind a two-column masthead, read
as a sole author) and three were placeholders that had never actually been transcribed: Cumaio's
venue was the literal string `"Review"`, Francisco's was `"Journal"`, and Zhong was recorded as an
unpublished manuscript when it is an ACM conference paper with a DOI. All seven are fixed. The
general lesson is in the correction log below: verify the author block visually, and do not treat
a successful extraction as a successful verification.

**Three sources do not exist in the corpus at all.**

| Cited as | Citations | Risk |
| --- | --- | --- |
| Dasmariñas et al. (2024) | 7 | The seasonal forecasting argument and the whole SARIMA section rest on this one paper. It is confirmed to exist (PUP Journal of Science & Technology 14(1), 70-90, doi 10.70922/ctzevg57) and Chapter 2's characterisation of it is accurate, but it is not in the corpus. |
| Dey and Arefin (2025) | 3 | Confirmed to exist (JISEM 10(47s), 148-182). Supports the rule-based budget claim. |
| Srisamai and Siriruk (2023) | 1 | Cited for a multi-level evaluation framework in an inventory study. A Srisamai & Siriruk 2023 IEOM paper on demand forecasting exists, but it is not confirmed to be the intended source. |

**Non-academic dependencies** (no sourcing required, listed for completeness): PSA FIES 2023,
PSA HFCE 2022 Q1-2026 Q2, and the group's own PUEPS instrument.

**Deliberately not changed.** The ISO/IEC 25010 characteristic list in the chapter was left as the
Drive V3 body has it, because Chapter 1 V6 agrees with it and diverging would desynchronise the
two chapters. The fielded ISO questionnaire disagrees with both. That conflict is recorded as an
open item in `chapter-2.md` for the adviser to settle, rather than silently resolved here.

## Correction log

### 2026-09-26 — Huang (2025) reverted to Huang et al. (2025)

An earlier pass in this same session read page 1 of `A--Huang-2025` and concluded
Anzhong Huang was the sole author, changing three body citations from
`Huang et al. (2025)` to `Huang (2025)`. That reading was wrong. The JGIM
masthead sets the six authors in a **two-column block**, and the first text
extraction only surfaced the left column:

| Column 1 | Column 2 |
| --- | --- |
| Anzhong Huang | Xin Zhang |
| Yuanyuan Wang | Sangbing Tsai |
| Ping Zhou | Lin Chen |

Six authors, so APA 7 requires `Huang et al. (2025)` in the body and all six named in the
reference list. The change has been reverted. The venue is *Journal of Global Information
Management, 33*(1), 1-26, DOI `10.4018/JGIM.395852`, received 2025-09-07, accepted 2025-12-01.

**Lesson for future passes:** a two-column author block is a known failure mode of
`pdftotext -layout`. Any paper whose author count drives an APA decision needs a visual check of
page 1, not a text extraction. Three other entries were wrong the same way and are now fixed
from page 1: Cumaio (venue had been the literal string "Review"), Francisco (venue had been the
literal string "Journal"), and D'Souza (author list truncated at three plus "et al.").

### 2026-09-26 — malformed Markdown repaired

The `## What this means` section had been written one character per line, which rendered as a
single unreadable paragraph and broke the missing-sources table. The prose was recoverable and
has been restored to normal paragraphs.
