# Adviser Writing Rules — Ma'am Era's Formats & Guidelines

Consolidated rules extracted from MA'AM ERA'S formats/guidelines and inline comments, so thesis drafts (and future AI-assisted revisions) follow them consistently.

**Sources**
- `formats-templates/chapter-1/Writing Chapter 1.md`
- `formats-templates/chapter-2/Writing Chapter 2.docx` (the official guideline)
- `formats-templates/Reference Thesis (Group 10).docx` (golden example — PAWPID)
- Inline Word comments by `ERA MARIE GANNABAN` on `google-drive/` chapter drafts (chapter-1 V1/V3/V4, chapter-2 V1, topical outline V2)
- Joint-notes: `google-drive/topical-outline/` comments and `docs/thesis/paper/` drafts

---

## 1. Rules from "Writing Chapter 2" (official guideline)

### 1.1 Nature of the RRL
- Chapter 2 **must not** be a collection of article summaries. It must analyze, compare, connect, and synthesize information from multiple sources.
- Organized **thematically**, not by author. Generally **4–6 major topics/themes**.
- Each major topic may have **3–4 relevant subtopics** when further discussion is needed.
  - Example themes for computing research: Research Domain → Existing Practices and Systems → Major System Functions → Algorithms/Models/Methods (one theme per major approach + Performance Metrics) → System Evaluation (ISO/IEC 25010, SUS).
- Every theme should be built from **multiple sources** — never one article unless necessary.

### 1.2 Source quotas and recency
- Each major topic/subtopic: **≥5 scholarly sources**.
- Topics on the study's core **algorithms/models: 6–7 sources**.
- Whole chapter: **~20–30+ references**, majority within the **last 3 years** (guideline §VI also says prioritize the last 5 years).
- Older sources allowed **only** for foundational theories, algorithms, models, laws, standards, established concepts.
- Prefer: peer-reviewed journals, conference proceedings, reputable-publisher books, government publications, institutional reports, recognized standards, master's/doctoral theses, official technical documentation.
- Avoid: Wikipedia, blogs, promotional sites, Facebook posts, unsourced articles, AI-generated content passed off as sources, anonymous/random websites.
- Include both **local and foreign** literature; under a thematic RRL they may be discussed together (no mandatory separate sections).

### 1.3 Paragraph structure per theme
Quote/structure per theme: **Topic → Evidence → Comparison → Analysis → Relevance**.
1. **Topic** — introduce the main idea with the team's own sentence.
2. **Evidence** — present findings from several sources (multi-source parentheses).
3. **Comparison** — similarities/differences among studies.
4. **Analysis** — what the findings collectively mean.
5. **Relevance** — connect back to the proposed study.

### 1.4 Never write author-by-author
Avoid: "According to Santos (2024)… Cruz (2025) stated… Reyes (2025) explained…"
Write: a synthesized claim with grouped citations (Santos, 2024; Cruz, 2025; Reyes, 2025).

### 1.5 Algorithms and models (§VII) — per major algorithm/model
Cover in order: **Definition → How it works → Input/data requirements → What it produces → Previous applications → Findings from studies → Strengths → Limitations → Relevance to the proposed study**.
Do more than define: establish why the approach suits THIS research problem.
Sample ARIMA section = 6 paragraphs (definition; how it works/components; previous applications; findings; strengths & limitations; relevance to the proposed system).

### 1.6 Existing systems (§VIII)
Compare (do more than list features): **Purpose, Target users, Major features, Technologies, Algorithms/models, Data used, Results, Strengths, Limitations, Relevance to the proposed system**.

### 1.7 Synthesis (§IX)
Approximately **4–5 paragraphs**; do not repeat the RRL article-by-article:
1. Common findings
2. Technologies/algorithms used by prior researchers
3. What existing systems/studies accomplished
4. Limitations and research gap
5. How the proposed study addresses the gap

### 1.8 Research gaps (§X)
- Every gap claim must be **supported by the reviewed literature**.
- Gap types: Technology, Methodological, Integration, Feature, Contextual, Data, Evaluation.
- No unsupported absolutes. Do NOT write "No existing study has combined X, Y, Z" unless the search proves it. Prefer "Among the studies reviewed, limited attention was given to…".

### 1.9 Conceptual model (§XI)
- Show how major components relate; **IPO (Input–Process–Output)** for system-development studies.
- INPUT: Knowledge (user requirements, datasets, transaction records, variables, business rules) + Software + Hardware.
- PROCESS: Requirements analysis → algorithm/model implementation → system analysis & design → development → testing → evaluation.
- OUTPUT: Developed system + major expected capabilities.
- Add a narrative explaining each component and the Input→Process→Output relationships.

### 1.10 Citation & referencing (§XII) — APA 7th
- Narrative: one author "Santos (2025)"; two "Santos and Reyes (2025)"; 3+ "Santos et al. (2025)".
- Parenthetical: "(Santos, 2025)", "(Santos & Reyes, 2025)", "(Santos et al., 2025)".
- Multi-source: alphabetical, semicolon-separated.
- Direct quotes: author, year, page — used sparingly; prefer paraphrase and synthesis.
- Cite every borrowed idea; place citations near the supported statement; every in-text citation must have a References entry.
- Do not repeatedly begin sentences with "According to…" — vary signals (stated, found, reported, emphasized, suggested) and use transitions that genuinely reflect the relationship.
- Never use fabricated or unverified citations.

---

## 2. Rules from "Writing Chapter 1" (official guideline)

- Each major section: **~4–5 paragraphs**; each paragraph = one main idea that logically leads to the next.
- **I. Introduction** — general-to-specific. Paragraph sequence: industry background → industry challenges → role of technology → specific area of concern → need for the study. Do NOT open with beneficiary details or the full proposed system.
- **II. Project Context** — beneficiary + existing process → identified problems (based on interviews/observations/records/preliminary investigation) → effects of problems → proposed system (features tied to problems) → algorithm/technology role.
- **III. Purpose and Description** — purpose → description & major functions → algorithm & processing → expected contribution.
- **IV. Scope and Limitations** — locale/beneficiary/users → functional scope → technical/scope of the algorithm → limitations (realistic boundaries).
- **V. Operational Definition of Terms** — terms defined as used in the study, preferably alphabetical; **minimum of 10 terms** (from Ma'am Era's comments).
- Consistency rule: sections must connect; do NOT add features because they are "technologically impressive" — every feature must address an identified problem. Do NOT invent problems; support organizational difficulty claims with interviews/observations/records/surveys.

---

## 3. Rules extracted from Ma'am Era's inline comments

### 3.1 Chapter 2 V1 (2026-09-04) — direct actions for Chapter 2 V2
- **Open with your own idea, not a citation.** Never start a paragraph/section with "(Author, year)" — open with the team's claim, then support with citations.
- Every section must **show its relevance to the study** (e.g., profile/demographic literature must tie to BUDI's design). If relevance can't be shown, the content likely doesn't belong.
- Name subtopics explicitly: include **"Personalized"** in the finance-management-app subtopic.
- **Combine savings and debts** into one connected discussion; keep "ways of improving" inside the savings-and-debt theme.
- Everything discussed must be **part of the system**: map every data type/source (time-series, BSP/FIES, survey) to a concrete BUDI input; add a framing intro for system models & algorithms tied to the study.
- Fix **fragmented/duplicated sentences** (e.g., the repeated BSP-survey sentence).
- Every algorithm/paragraph must be **directed to the study** (classification/SVM → BUDI profile classification).
- **Methodology must not "story-tell" what methodology is** — write it BUDI-specifically (agile iterations, data phases for the four model families, cross-functional development).
- **Rewrite the synthesis** per §IX (was a stub).
- Strengthen weak subsections: "add more" (intelligent features), "didnt see article that would be helpful to develop your study" (models) — anchor models in citable corpus papers.

### 3.2 Chapter 1 V4 (2026-09-02/04)
- For every claimed benefit, **define how you measure users' improvement** (e.g., "how do you plan to measure users improvement in savings and debt?"). Savings-improvement reliability must have a concrete measurement plan (see also "how do you plan to ensure the reliability of saving?", "how do you plan to monitor these?").

### 3.3 Chapter 1 V3 (2026-08-28 / comments 09-02 & 09-04)
- Define acronyms the first time ("whats pfm" → define Personal Finance Management).
- For every algorithm, state **exactly what it will classify / forecast / optimize / detect** ("what do you plan to classify? forecast? optimize? and identify anomalies?"), which feature it applies to, and its category (algorithm vs software tool).
- Anything claimed must appear in the title / specific objectives / system plan — no drift ("not part", "not included in the title", "i didnt see this in specific objectives", "please match this to your specific objectives"). Title, objectives, methodology, and modules must be consistent and finalized.
- Be concrete: numerical values/targets, transaction examples (savings for emergency funds, tuition…), recurring transactions, category levels, sample bases ("basis?", "whats the good percentage? numerical value?").
- Justify models: clarify whether four models are experimental comparison or serve different purposes on the same variable.
- Scope realistically: e.g., limit the study locale (was given: Makati only, purposive sampling — "NCR is too big"; "no other regions").
- Include **survey results in the RRL** discussion: "based on the survey, savers do this which leads to…".
- Operational definitions: minimum 10 terms.
- Scope & Limitations section should stick to scope/limitation content only.
- Resolve module decisions (e.g., finalize the system admin module choice; security/system characteristics belong to the right sections).
- Revise wording to be easily understood and clearly associated with "intelligent"/personalization claims.

### 3.4 Chapter 1 V1 (2026-08-15)
- Keep the study inside the program scope; remove out-of-scope items.
- Where an algorithm is used, name it precisely; justify each possible system feature with reasons ("please include reasons of those possible system features").
- Use **actual datasets or clearly-labeled practice data** ("make sure to have actual data set of this or you may use practice instead").
- Clarify financial data sources and their purpose; specify which features get insights; specify transactions and goals with examples.
- Explain how the system will be personalized.
- Reorganize sections for coherence; remove redundancies.
- Beneficiaries must be included; scope/limitations title only; include discussion of system features, tools, research locale, and timeline.
- Identify which key feature each algorithm applies to.

---

## 4. Notes for the RRL on human memory / cognitive limits

- **Miller's Law** (Miller, 1956): working memory holds ~ **7 ± 2** chunks.
- **Cowan (2001)**: capacity is closer to **4 ± 1** chunks.
- Use case: BUDI must respect these limits (notifications, alerts, dashboard data, summarized insights) — a legitimate thematic basis for how the app presents finance insights. (Origin: joint note in topical-outline V2 comments: "Cowan - 7+-1 = Miller - 4+-1 =".)

---

## 5. Cross-cutting rules (always apply)
- Write in first-our-own-idea mode; citations support, never lead.
- Every claim/feature must tie to the study (problem → system function → algorithm → expected result → measurement).
- Consistency across title, objectives, scope, methodology, modules, and references.
- Basis and evidence for every claim (no unsupported statements, no invented problems).
- Concrete numbers/examples/sources wherever Ma'am Era asked to "specify" or "basis?".
- Most references recent (last 3 years), local + foreign, APA 7th, verified.