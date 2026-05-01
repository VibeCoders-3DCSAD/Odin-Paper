[WARNING]: Outdated.

# Registry of Papers

> **Usage**:
> One row per paper. Add a row after Step 6 of the pipeline (after the summary is complete and you have read it).
> Update the **Tally** row at the bottom whenever a row is added or a designation changes.
> Search the `topics` or `shorthand_tags` columns to find papers for a specific topic.
> `paper_id` links directly to `Papers/<paper_id>.md` and `Papers/<paper_id>-summary.md`.

---

## Source Quota Status

| Designation | Count | Target | Remaining |
| :--- | :---: | :---: | :---: |
| `local` | 0 | 25 | 25 |
| `international` | 0 | 25 | 25 |
| `algorithm-specific` | 0 | -- | -- |
| **Total** | **0** | **50** | **50** |

---

## Paper Registry

| Paper ID | Designation | Year | Author/s | Title | Venue | Topic/s | Tag/s | Notes |
| :--- | :---: | :---: | :--- | :--- | :--- | :--- | :--- | :--- |
| 10.62986/dp2024.10 | local | 2024 | Albert, J. R. G.; Briones, R. M.; Rivera, J. P. R. | Wealth Creation for Expanding the Middle Class in the Philippines | Philippine Institute for Development Studies Discussion Paper Series | [1, 2, 4, 5, 7, 9, 11, 12] | ["/income-typology", "/expenditure-patterns", "/fil-behavioral-patterns", "/western-taxonomy-gap", "/cultural-expense-types", "/profiling-role"] | ... |
| 10.20944/preprints202508.0349.v1 | local | 2025 | Ama, N. A. | Analysis of the Food and Income Expenditure Survey 2023 Among Filipino Households | Preprints.org | [1] | [/expenditure-patterns, /income-typology] | ... |
| 10.63498/ijabms2 | local | 2026 | Amado, M. A. A. | The plight of teachers on the twice-a-month salary release: Financial literacy and survival | International Journal of Accountancy, Business, and Management Studies (IJABMS) | [1, 4] | ["/income-typology", "/budget-time-horizons", "/expenditure-patterns", "/budgeting-prevalence", "/budget-failure-points", "/intelligent-vs-literacy", "/strategy-income-fit", "/surplus-logic", "/lump-sum-income", "/min-user-input", "/western-taxonomy-gap", "/fil-behavioral-patterns", "/cultural-obligations"] | ... |
| 10.69569/ijp.2026.065 | local | 2026 | Am-una, A. | Beyond Awareness: Examining Financial Behaviors Among Public School Teachers in the Philippines | Journal of Interdisciplinary Perspectives | [1, 2, 4, 10] | [/income-typology, /expenditure-patterns, /budget-failure-points, /budgeting-prevalence, /intelligent-vs-literacy, /pfms-gap, /surplus-logic, /min-user-input, /western-taxonomy-gap, /fil-behavioral-patterns, /profile-dimensions] | ... |
| a2b3c4d5-e6f7-4a8b-9c0d-1e2f3a4b5c6d | local | 2025 | Apao, A. A.; Cayanpat, R. A. B.; Edullantes, Y. P. Jr.; Cabanero, K. E. S.; Hechanova, J. M. T.; Candia, H. G. | Martime Students' Financial Knowledge, Attitude, and Behavior | Daengku: Journal of Humanities and Social Sciences Innovation | [1, 10, 11] | ["/income-typology", "/budget-time-horizons", "/intelligent-vs-literacy", "/western-taxonomy-gap", "/fil-behavioral-patterns", "/profile-dimensions", "/classification-vs-clustering"] | ... |
| 10.1371/journal.pone.0294466 | international | 2023 | Bai, R. | Impact of Financial Literacy, Mental Budgeting, and Self-Control on Financial Well-Being with the Mediating Role of Investment Decision Making | PLoS ONE | [1, 4, 5, 10] | [/expenditure-patterns, /budgeting-prevalence, /intelligent-vs-literacy, /strategy-mechanics, /budget-rec-formulation, /western-taxonomy-gap, /fil-behavioral-patterns] | ... |
| f7d9e3a2-5b1c-4e8a-9d2f-6b4e8c7a3d1f | local | 2021 | Bangko Sentral ng Pilipinas | 2021 Consumer Finance Survey (CFS) | Bangko Sentral ng Pilipinas | [1, 9, 11] | ["/income-typology", "/expenditure-patterns", "/income-type-behavior-diff", "/fil-behavioral-patterns", "/profile-dimensions", "/fies-bsp-mapping", "/cultural-expense-types", "/fil-pfms-categories", "/sss-pagibig"] | Most authoritative national baseline of Filipino household income, expenditure, and asset‑holding patterns we have yet. Highly recommended to consider in RRL despite lack of recency. |
| 53f2d4a7-1b3c-4e8e-9a2d-6c3b8e4f7a1d | local | 2025 | Cabiles, S. L. | Financial Management Practices of Employees at Bureau Of Internal Revenue | United International Journal for Research & Technology | [1, 4, 5, 7, 8, 9, 11] | ["/expenditure-patterns", "/budget-failure-points", "/cultural-obligations", "/pfms-gap", "/budget-rec-existing", "/forecasting-methods", "/anomaly-taxonomy", "/overage-vs-behavioral", "/fil-behavioral-patterns", "/western-taxonomy-gap", "/classifier-candidates", "/cultural-spending-protection"] | ... |
| f8c3e5a2-7b1d-4e9c-8a3f-2d6e9b1c4a7d | local | 2024 | Cacnio, F. Q.; Romarate, M. E. G. | How does financial literacy affect financial behavior over the life cycle? Evidence from Filipino households | Bangko Sentral ng Pilipinas | [1, 9] | ["/expenditure-patterns", "/budget-time-horizons", "/fil-behavioral-patterns", "/profile-dimensions"] | ... |
| 10.46303/tpied.2024.12 | local | 2024 | Casilan, J. J.; Baclagan, T. | Exploring Parental Expectations on Children Helping Parents out in Lower Middle-Income Families | Theory and Practice in Child Development | [1, 9] | ["/cultural-obligations", "/fil-behavioral-patterns"] | ... |
| [paper_id] | [desig.] | [year] | [authors] | [title] | [venue] | [topics] | [shorthand_tags] | ... |


---

## Column Reference

| Column | Format | Source | Description |
| :--- | :--- | :--- | :--- |
| `paper_id` | DOI, with `/` becoming `_`, or UUID v4 | converter YAML `paper_id` | Permanent identifier. Links to both files in `Papers/`. |
| `desig.` | `local` / `intl` / `algo` | converter YAML `designation` | Abbreviated designation. `algo` = algorithm-specific. |
| `year` | YYYY | converter YAML `year` | Publication year. Must be 2023–2026 unless exempted. |
| `authors` | Last, F.; Last, F. | converter YAML `authors` | First two authors. Append "et al." if more than two. |
| `title` | plain text | converter YAML `title` | Exact title, truncated at 60 chars with `…` if needed. |
| `venue` | plain text | converter YAML `venue` | Full journal or conference name. |
| `topics` | comma-separated integers | summarizer YAML `odin_topics` | Topic numbers this paper supports. See topic table below. |
| `shorthand_tags` | comma-separated `/tags` | manual, from outline | Specific `[/shorthand]` nodes from `topic-outline.md`. |
| `notes` | one line | manual | Primary contribution of this paper to Odin's RRL in ≤50 words. |

---

## Topic Reference

| # | Topic | Outline Node |
| :---: | :--- | :---: |
| 1 | Spending and Budgeting Behavior of Filipino Young Professionals | A.1 |
| 2 | Existing Personal Finance and Budget Management Systems | A.2 |
| 3 | Mobile-First Design in Personal Finance Systems | B.1 |
| 4 | Budgeting Strategies and Budget Recommendation | C.1 |
| 5 | Budget Recommendation Algorithm | C.2 |
| 6 | Predictive Modeling in Personal Finance Systems | D.1 |
| 7 | LSTM as the Spending Forecasting Algorithm | D.2 |
| 8 | Anomaly Detection in Personal Finance Systems | E.1 |
| 9 | Anomaly Detection Algorithm | E.2 |
| 10 | User Behavioral Profiling in Filipino Personal Finance Contexts | F.1 |
| 11 | Profile Classification Algorithm | F.2 |
| 12 | Expense Categorization in Filipino Personal Finance Contexts | G.1 |
| 13 | Data Privacy, Security, and User Trust in Personal Finance Systems | H.1 |
| 14 | User Retention and Engagement in Personal Finance Systems | I.1 |
| 15 | System Evaluation | J.1 |

---

## Designation Rules (Quick Reference)

Apply in priority order — stop at first match:

1. **`algorithm-specific` (algo)** — The paper primarily describes an algorithm, model, or computational method. Overrides local/international regardless of origin.
2. **`local`** — Published in or by a Philippine institution. Not algorithm-specific.
3. **`international` (intl)** — Published outside the Philippines. Not algorithm-specific.

---

## Recency Exceptions

All sources must be 2023–2026, except:

| Exception type | Rule |
| :--- | :--- |
| Laws and statutes | Any year. Cite by Republic Act number. |
| ISO standards | Any year. Always include edition year (e.g., ISO/IEC 25010:2023). |

---
