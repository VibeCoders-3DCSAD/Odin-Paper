# PUEPS Findings Summary

**Source:** "ODIN Public User Expectations and Perception Survey (Responses)" Google Sheet, exported from Google Drive on 2026-09-07. Raw CSV cached locally (gitignored) beside this file as `PUEPS-responses.csv`. This is the missing results file referenced by `chapter-1.md` (V2.1) and `chapter-1-evidence-map.md`.

## Study Design

- **Respondents:** 47 valid responses collected 2026-06-11 onwards.
- **Locale:** National Capital Region (NCR) only. Responses recorded in Taguig (30%), Pasay (17%), Manila (13%), Makati (11%), Quezon City (9%), and 7 other NCR cities.
- **Age:** 20–24 (45%), 35–40 (26%), 25–29 (21%), 30–34 (9%).
- **Employment:** Regular/Permanent (40%), Contractual/Project-based (15%), Part-time (13%), Freelancer/Self-employed (11%), Business owner (9%), Student (9%), Casual (4%).
- **Income pattern:** Fixed monthly salary (49%), Variable (30%), Mixed (21%). 51% of respondents do **not** have a purely fixed monthly income.
- **Monthly take-home income:** Below ₱14,000 (23%), ₱14,000–₱27,999 (21%), ₱28,000–₱55,499 (26%), ₱55,500–₱97,099 (13%), ₱97,100+ (6%), Prefer not to answer (11%).

## Key Headline Findings (Agree + Strongly Agree unless noted)

### Financial management is widely challenging

| Construct | % |
| :--- | ---: |
| Managing personal finances is challenging | 96% |
| Existing tools do not reflect Filipino financial realities | 89% |
| Manual expense recording is tedious / hard to sustain | 89% |
| Existing tools provide limited useful insights/recommendations | 89% |
| Difficulty consistently monitoring spending | 85% |
| Financial obligations strongly affect budgeting decisions | 85% |
| Privacy/security concerns discourage full app use | 83% |

### Frequency-based problems (Very Frequently + Frequently)

| Construct | % |
| :--- | ---: |
| Unexpected financial obligations disrupt budget plans | 72% |
| Difficulty identifying where most of the money is spent | 66% |

### Behavioral gaps (Always + Often where that scale applies)

| Behavior | % |
| :--- | ---: |
| Set monthly spending limits | 68% |
| Regularly track daily/monthly expenses | 53% |
| Follow the budget plan they prepare | 51% |
| Allocate income to savings/emergency funds every salary period | 43% |
| Allocate income to savings/emergency funds every salary period **or often** | 68% |

### Feature expectations (Agree + Strongly Agree)

| Feature | % |
| :--- | ---: |
| Personalized budget suggestions **with explanations** | 100% |
| Expense categories tailored to Filipino obligations | 100% |
| Alerts for unusual/excessive spending | 98% |
| Expense tracking as a core feature | 98% |
| Simple, user-friendly interface | 98% |
| Financial summaries and spending reports | 98% |
| Willing to manually input expenses for meaningful insights | 96% |
| Spending forecasts based on past behavior improve planning | 94% |

### Current tracking methods (multiple select)

| Method | % |
| :--- | ---: |
| Mobile budgeting app (e.g., GCash, Lista) | 40% |
| Mental tracking (in one's head) | 38% |
| Spreadsheet (Excel / Google Sheets) | 28% |
| Manual notebook/diary recording | 28% |
| Does not track budget at all | 19% |

> **Correction (2026-09-13):** the savings row was previously reported as "26%". That figure was a mislabeled reading of the item "I regularly allocate part of my income toward savings or emergency funds.", which uses an `every salary period / often / sometimes / rarely / never` scale rather than `Always/Often`. Re-computed from `PUEPS-responses.csv`: 20/47 (43%) "every salary period", 12/47 (26%) "often", 15/47 (32%) sometimes/rarely/never. Chapter 1 quotes the combined "every salary period or often" figure of 68.1% (32/47). The "0% Always / only 26%" note applied the wrong scale and is removed.

## Notes & Limitations

- These are the raw response counts; no weighting or inferential statistics were applied.
- "Mobile budgeting app (e.g., GCash, Lista)" appears as two entries in the raw export due to CSV comma-splitting of that multi-select cell — count of 19 (40%) is accurate at the option level.
- All percentages are of the 47 respondents. Where a respondent skipped a Likert item, counts may sum below 47.

## Use in Chapter 1 V4

- Directly resolves the V2.1 `<!-- VERIFY: PUEPS findings -->` markers in Section II (Project Context).
- Supports reviewer comment #3 ("include discussions on the result of the survey") with concrete, quotable figures.
- Grounds feature-to-problem mapping: e.g., anomaly alerts → 72% report unexpected obligations disrupt plans; forecasts → 94% say forecasts would improve planning.