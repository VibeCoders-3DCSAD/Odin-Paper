# Chapter 2 Evidence Map (V3.0)

Generated 2026-09-26 against `GROUP4 - CHAPTER 2 - V3 - 09.26.26.docx`. Citation-enrichment
pass applied the same day; see "Citations added 2026-09-26" below.

The original pass resolved every author-date citation against the 91-paper BUDI-Literature corpus
and found 15 clean resolutions, 1 correction, 3 missing from the corpus, and 1 secondary citation.
The enrichment pass added 8 further references, taking the list from 19 to 27, and attached
existing in-corpus citations to the Synthesis section, which had been carrying claims with no
attribution at all.

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
## Citations added 2026-09-26 (citation-enrichment pass)

The sections below previously carried no scholarly citations at all. Eleven were added, taking the
reference list from 19 to 27. Every one was checked against the publisher's own page, its DOI
registration, or at least two independent citing bibliographies before being written.

| Added citation | Section | Verification basis | In corpus |
| --- | --- | --- | --- |
| International Organization for Standardization (2023) | Software Quality Evaluation | Standard's own foreword and Annex A, read directly | no — paywalled |
| Lim et al. (2025) | Software Quality Evaluation | BMC, Springer, DOAJ, ResearchGate all agree | no |
| Brooke (1996) | Software Quality Evaluation | Window exception, instrument origin | no |
| Ariningsih and Muhammad (2024) | Software Quality Evaluation | Publisher PDF header | no |
| Lianto et al. (2023) | Software Quality Evaluation | Garuda index and journal page | no |
| Alqudah and Razali (2024) | Agile Kanban | Two independent citing bibliographies | no |
| Sathe and Panse (2023) | Agile Kanban | Publisher's own citation block | no |
| Shaout et al. (2025) | Agile Kanban | Journal's own citation block | no |
| Huss et al. (2023) | Agile Development Lifecycle | Citing bibliography only — **not verified** | no |

All nine new citations are publisher-verified except Huss et al. (2023), which is flagged
inline and in the reference list and can be cut without loss.

**The Synthesis section was given citations without adding a single new reference.** Its claims
were synthesising material already cited elsewhere in the chapter and were therefore carrying no
attribution: Yeo et al. (2023), Cumaio et al. (2026), Esperanza (2025), Francisco et al. (2026),
Claro and Noval (2025), Alenazi and Sas (2023), Yoganandham (2025), Laspiñas and Murcia (2024),
Gulbakyt et al. (2025), Lu et al. (2025), Huang et al. (2025), Zhong (2025), D'Souza et al. (2026),
and de Zarzà et al. (2024) are all already in the corpus.

**The Conceptual Model section was deliberately not padded.** Its Input, Process, and Output
components describe the group's own system design and are not claims about prior work. Only the
Evaluation component rests on external sources, and those are now cited.

### Integrity check after the pass

| Check | Result |
| --- | --- |
| References in list | 27 |
| References never cited in the body | 0 |
| In-text citations with no reference entry | 0 |
| References dated before 2023 | 1 — Brooke (1996), a declared window exception, flagged at the point of citation |
| References whose metadata is unverified | 1 — Huss et al. (2023), flagged inline and cuttable |
| Sources cited but absent from the corpus | 12 (9 pending acquisition, 3 source-needed) |

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

**The two chapters agree, and the fielded instrument is the sole outlier.** Chapter 1's stated
objective reads "Test the functionality, reliability, performance efficiency, usability, security,
and **portability** of the system", and its ISO/IEC 25010 list is Functional Suitability,
Reliability, Performance Efficiency, Usability, Security, Portability — the same six characteristics
Chapter 2 uses, in the same set. `maintainability` does not appear in Chapter 1 at all. The fielded
questionnaire on Drive, which uses five characteristics and substitutes maintainability for
portability, matches neither chapter.

> **Superseded finding, retracted 2026-09-27.** An earlier revision of this map claimed the two
> chapters differed by one characteristic and that Chapter 2 was the outlier. That was **wrong**. It
> was derived from `thesis/paper/chapter-1.md`, which is a stale V5-era mirror, rather than from the
> authoritative `GROUP4 - CHAPTER 1 - V6 - 09.24.26.docx`. The mirror is an older revision that still
> listed maintainability; V6 does not. Verified by reading the V6 `.docx` directly, and re-verified
> after a Drive re-fetch the same day.
>
> This is the mirror-lag trap `AGENTS.md` warns about, and it is the second time this session that a
> stale repo copy produced a confident wrong conclusion. **Verify against the `.docx` before asserting
> anything about Chapter 1.**

**Both chapters' lists use 2011 vocabulary, not 2023.** They agree with each other and both disagree
with the standard they cite. They retain *usability*, which ISO/IEC 25010:2023 replaced with
*interaction capability*, and *portability*, which became *flexibility*; they omit *compatibility*
and *safety*, giving six where the 2023 model has nine. Chapter 1's usability sub-list is verbatim
2011 §3.4.1–3.4.5 — appropriateness recognizability, learnability, user error protection, and *user
interface aesthetics* — the last of which the 2023 edition renamed *user engagement*.

**Deliberately not changed.** The ISO/IEC 25010 characteristic list in the chapter body is retained
as the panel accepted it, and the conflict is flagged in `chapter-2.md` rather than silently resolved
here. The researchers were asked to settle it and chose to leave it flagged for now. The cheapest
correct fix, when they take it up, is to cite **ISO/IEC 25010:2011** for the six-characteristic set:
one edit, and both chapters — which already agree — become accurate. The alternative is renaming to
the 2023 vocabulary in both chapters and adding compatibility and safety.

**Chapter 1 is being edited concurrently.** At the 2026-09-27 Drive re-fetch, Chapter 1 V6 still
carried 9 instances of `BUDI` against 10 of `BUDGIE`, and 2 of `SVM` against 4 of `rule-based` — down
from 13 and 3 respectively before the teammate's edits. Chapter 1 is therefore mid-revision, and any
figure quoted about it here is a timestamped observation, not a settled state.

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

### 2026-09-26 — the ISO/IEC 25010 characteristic list is misattributed

**Partly retracted 2026-09-27 — see below.** The standard-misattribution finding stands. The
accompanying claim about Chapter 1 does not.

The chapter body cites ISO/IEC 25010:2023 and then lists functional suitability, performance
efficiency, reliability, security, portability, and usability. Those are not the 2023
characteristics. The standard's own foreword states: *"Usability and portability have been
replaced with interaction capability and flexibility respectively"*, and *"Safety has been added
as a quality characteristic"*. The 2023 model therefore has **nine** characteristics:

> functional suitability, performance efficiency, compatibility, interaction capability,
> reliability, security, maintainability, flexibility, safety

Three further points from the same document:

- Installability is subcharacteristic 3.8.3 under **flexibility**, not a characteristic in either
  edition. The chapter's portability paragraph therefore describes a subcharacteristic while
  presenting it as a characteristic.
- The SUS belongs to the quality-in-use model, ISO/IEC 25019. Clause 3.4 of 25010:2023 states
  that *"Interaction capability is a prerequisite for usability"*, which is not the same
  relationship as the product model supplying the usability score.
- ~~Chapter 1 assigns *co-existence* to maintainability. Co-existence is 3.3.1 under
  **compatibility**.~~ **Withdrawn.** Chapter 1 V6 has no maintainability entry and no co-existence
  entry; this came from the stale V5-era mirror.

The six-characteristic list is retained because the panel accepted it, but it cannot be attributed
to the 2023 standard. Resolving this means either citing ISO/IEC 25010:2011 for the
six-characteristic set, or renaming to the 2023 vocabulary in both chapters and adding
compatibility and safety.

**Lesson:** a standard's version number is not a citation. Anyone writing `ISO/IEC 25010:2023`
into a chapter inherits responsibility for the clause numbering of that edition, and the edition
boundaries here are exactly where the vocabulary changed.

### 2026-09-27 — retracted: "this map understated the ISO conflict"

**This entry was wrong and is withdrawn.** It claimed Chapter 1 and Chapter 2 differed by one
characteristic, that the fielded instrument sided with Chapter 1, and that Chapter 2 was therefore
the outlier. All of that was derived from `thesis/paper/chapter-1.md`, a stale V5-era mirror. The
authoritative `GROUP4 - CHAPTER 1 - V6 - 09.24.26.docx` agrees with Chapter 2 on all six
characteristics. The fielded instrument matches neither chapter, and the conflict is two-way, not
three-way.

Two lessons, both now standing rules for this repo:

1. **A repo mirror is not the document.** `thesis/paper/chapter-1.md` is V5; Drive V6 is newer. Any
   claim about Chapter 1's content must come from the `.docx`. This is stated in `AGENTS.md` and was
   ignored anyway, which is the real failure.
2. **Verify before correcting.** This entry existed to correct a *previous* wrong claim, and it
   introduced a new one while doing so. A correction is a claim and needs the same evidence as the
   thing it corrects.

The retraction is recorded here rather than deleted so the error stays auditable.

