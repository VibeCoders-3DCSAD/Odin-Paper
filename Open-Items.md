## Open Items Summary

### Article I – Platform and Target Users
| Section | Item | Type | Description |
|---------|------|------|-------------|
| Section 2.1.3 | Employment capacities | **Definition needed** | The six capacities (full‑time, part‑time, self‑employed, freelancer, contractual, gig economy worker) must be explicitly defined operationally. |

### Article II – Input and Transaction
| Section | Item | Type | Description |
|---------|------|------|-------------|
| Section 5.2 | Retention limit (13 months) | **RRL validation needed** | The 13‑month retention period must be validated against BSP guidelines, Data Privacy Act, or relevant literature. Fallback: 24 months or 3 years. |

### Article III – Financial Behavioral Profiles
| Section | Item | Type | Description |
|---------|------|------|-------------|
| Section 2.1.2 | CV threshold of 0.25 | **RRL validation needed** | Validate against BSP Consumer Finance Survey or literature on income variability among Filipino young adults. |
| Section 3.1.2 | Obligation ratio threshold of 0.50 | **RRL validation needed** | Validate against research; definition of unavoidable expenses is provided but threshold needs support. |
| Section 4.1 | Reclassification thresholds (CV Δ ≥ 0.10, obligation Δ ≥ 0.15, 60‑day sustained) | **RRL validation needed** | Validate against literature on how long financial behavioral profiles take to shift. |
| Section 6.2 | Questionnaire response mapping to profiles | **RRL validation needed** | Provisional mapping (No to income stability → Variable; ≥50% obligation → Obligated) requires validation. |
| Section 6 (NOTE) | Explainability and evaluation metrics for classification | **Missing section** | User notes that Article III may need sections for explainability and evaluation metrics, similar to forecasting module. |

### Article IV – Expense Groups and Categories
| Section | Item | Type | Description |
|---------|------|------|-------------|
| (none) | No open items identified. | | |

### Article V – Financial Flows
| Section | Item | Type | Description |
|---------|------|------|-------------|
| Section 3.1 | At least one account must be held | **Clarification needed** | User note: add a clause that at least one account must be retained (cannot delete all accounts). |

### Article VI – Budgeting Module
| Section | Item | Type | Description |
|---------|------|------|-------------|
| Section 2.1 | Budget period recommendations (30d for stable, 14d for variable) | **RRL validation needed** | Validate against literature on budget horizon effectiveness for different income stability profiles. |
| Section 4.2 | Default priorities per profile | **RRL validation needed** | Validate against literature on financial goal prioritisation among different user segments. |
| Section 5 | Surplus handling strategies (Rollover, Save, Reset) and default assignments | **RRL validation needed** | Validate against literature on user preferences for windfall or surplus allocation. |

### Article VII – Forecasting Module
| Section | Item | Type | Description |
|---------|------|------|-------------|
| Section 3.2 | FIES data older than 3 years | **RRL / method validation** | If most recent FIES is older than 3 years, adjustment method using PSA inflation data needs validation. |
| Section 5 | Three‑week persistence threshold for action | **RRL validation needed** | Justify based on concept drift literature or adjust after pilot testing. Note: models are frozen for thesis, so this applies only to synthetic evaluation. |
| Decision D6 | Synthetic data design documented separately | **Decision** | Already resolved (separate file). No action needed. |
| Decision D7 | No attention layer for LSTM explainability | **Decision** | Already resolved. |

### Article VIII – Anomaly Detection Module
| Section | Item | Type | Description |
|---------|------|------|-------------|
| Section 3.2 | Occasions (holidays, celebrations, special dates) | **Terminology clarification** | User note: these should be classified under a term called "Occasions". Recommend adding a definition in Article XVI. |
| Section 4 | Whitelist mechanism | **No open item** | Fully specified. |
| Section 6 | Alert fatigue prevention | **No open item** | Fully specified. |
| Section 8 | Evaluation metrics | **No open item** | Fully specified. |
| Decision D8 | Merchant novelty hard 60‑day cutoff | **Decision** | Resolved. |
| Decision D9 | Day‑of‑period default period | **Decision** | Resolved. |
| Decision D10 | Manual JSON holiday calendar (no API) | **Decision** | Resolved. |
| Decision D11 | No user sensitivity adjustment for anomaly threshold | **Decision** | Resolved. |
| Section 9 (Future Work) | Forecasted category spending as anomaly feature | **Future work** | Recommended for future versions. |

### Article IX – Savings Goal Management
| Section | Item | Type | Description |
|---------|------|------|-------------|
| Section 2 (NOTE) | Limit on number of savings goals | **Alternative proposal** | User note: consider using sum of savings goal amounts instead of number of goals for limit. Needs discussion or decision. |
| Section 4 | Default strategies (Goal‑based for all profiles) | **RRL validation needed** | Validate against literature on savings motivation and goal prioritisation among Filipino young adults. |

### Article X – Debt Management
| Section | Item | Type | Description |
|---------|------|------|-------------|
| Decision D13 | Compound interest excluded | **Decision** | Resolved (noted in Article XV). |
| Decision D14 | Hardship detection on payment attempt (not proactive) | **Decision** | Resolved (limitation noted). |

### Article XI – System Alerts and Notifications
| Section | Item | Type | Description |
|---------|------|------|-------------|
| Decision D15 | No user sensitivity adjustment | **Decision** | Resolved. |
| Future Work | Weekly email summary of alerts | **Future work** | Recommended. |

### Article XII – Explainability
| Section | Item | Type | Description |
|---------|------|------|-------------|
| Decision D16 | SUS measures for explainability (comprehension check, trust rating) | **Recommended but optional** | Researchers may include these in post‑task questionnaire. Not mandatory. |

### Article XIII – System and Algorithm Evaluation
| Section | Item | Type | Description |
|---------|------|------|-------------|
| Section 1.6 | Cyclomatic complexity threshold of 10 | **RRL validation needed** | Validate against software engineering benchmarks (e.g., McCabe). |
| Section 3.5 (Note) | Three‑week threshold for retraining/logging | **RRL validation needed** | Justify based on concept drift literature. Applies only to synthetic evaluation. |

### Article XIV – Data Privacy, Security, and Ethical Compliance
| Section | Item | Type | Description |
|---------|------|------|-------------|
| Section 1.4 | Retention period (13 months) | **RRL validation needed** | Same as Article II Section 5.2. Must be validated against BSP, DPA, or literature. |
| Section 3.5 | Ethical declaration | **Resolved** | Statement included. |
| Section 3.6 (duplicate) | Right to remove from training corpus | **Minor duplicate** | Paragraphs 6 and 6.1 are duplicated. Clean up. |
| Decision D18 | Pseudonymisation scheme | **Decision** | Resolved (sufficient for thesis). |

### Article XV – System Scope and Delimitations
| Section | Item | Type | Description |
|---------|------|------|-------------|
| All exclusions | Paluwagan, CSV import, credit cards, compound interest, etc. | **Exclusions documented** | No open items; all are explicitly excluded with reasons. |

### Article XVI – Definitions of Terms
| Section | Item | Type | Description |
|---------|------|------|-------------|
| None | All terms defined. | **No open items** | However, if "Occasions" is introduced (Article VIII Section 3.2), add it here. |

---

## Paper Specification – Open Items

| Article | Section | Item | Type | Description |
|---------|---------|------|------|-------------|
| Article II (RRL) | Section 1.2.1 | Minimum citations per RRL pillar | **Correction needed** | User notes actual minima: Local studies (≥25), International studies (≥25), Random Forest (≥20 total: 10 local + 10 int'l), LSTM (≥20 total), Isolation Forest (≥20 total), Rule‑based budget recommendation (≥20 total). Update the specification accordingly. |
| Article III (Methodology) | Section 3 | Agile development | **Correction** | User note: "No. Just normal agile." Remove the specific Scrum roles (Product Owner, Scrum Master) or keep as is? Recommend removing role assignments unless strictly required. |
| Article III (Methodology) | Section 4 onward | Chapters 4 and 5 | **Missing** | User notes that there is no Chapter 4 (Results) and Chapter 5 (Discussion) specification. Add if needed. |
| Article VII (References) | Minimum references | **Correction needed** | User note: update the minimum references to match the RLR pillar minima. Suggested: at least 60 total, but specific per category as above. |

---

## Summary Table of Actionable Open Items

| Priority | Item | Article | Action Required |
|----------|------|---------|------------------|
| High | RRL validation for 13‑month retention | II, XIV | Find BSP/DPA/study support or change to 24 months. |
| High | RRL validation for CV threshold (0.25) | III | Validate with BSP survey or literature. |
| High | RRL validation for obligation ratio (0.50) | III | Validate with research. |
| High | RRL validation for reclassification thresholds | III | Validate with literature on behavioral shift duration. |
| High | RRL validation for questionnaire mapping | III | Validate conversion algorithm. |
| High | RRL validation for budget period recommendations | VI | Validate with literature. |
| High | RRL validation for default priorities | VI | Validate with literature. |
| High | RRL validation for surplus handling strategies | VI | Validate with literature. |
| High | RRL validation for savings goal default strategies | IX | Validate with literature. |
| High | RRL validation for cyclomatic complexity threshold | XIII | Cite McCabe or software engineering source. |
| High | RRL validation for three‑week threshold | VII, VIII, XIII | Justify with concept drift literature. |
| Medium | Define employment capacities | I | Add operational definitions for six work types. |
| Medium | Add "at least one account" clause | V | Specify that user cannot delete all accounts. |
| Medium | Add "Occasions" terminology | VIII, XVI | Define in Article XVI. |
| Medium | Resolve savings goal limit (number vs. sum) | IX | Team decision required. |
| Medium | Clean duplicate paragraphs in Article XIV.3 | XIV | Remove duplicate Section 3.6. |
| Medium | Update RRL citation minimums | Paper II | Revise to local/global/algorithm-specific counts. |
| Low | Clarify Agile methodology (Scrum roles) | Paper III | Remove or keep role assignments. |
| Low | Add missing Chapters 4 & 5 specification | Paper | If needed, define Results and Discussion sections. |
| Low | Update minimum references count | Paper VII | Align with RRL minima. |