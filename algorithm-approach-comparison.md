# Algorithm Approach Comparison

## Purpose

This document compares:

1. the earlier algorithm plan proposed before the constraint of keeping only one machine learning model, and
2. the revised algorithm plan based on the requirement that the system should use only one ML model.

## Option A: Previous Multi-Algorithm Recommendation

This was the earlier recommended setup when there was no restriction on the number of machine learning models.

### Components

- `Financial behavioral profile classification`: `Decision Tree` or `Random Forest` classifier
- `Overage detection`: `Rule-based algorithm`
- `Spending forecast`: `LSTM`
- `Budget recommendation`: `Constraint-based` or `rule-based recommendation engine`

### Rationale

- A `Decision Tree` or `Random Forest` could classify users into the four financial behavioral profiles using onboarding data such as income type, income variability, fixed obligations, debt burden, and dependent count.
- A `rule-based algorithm` was recommended for overage detection because budget overage is determined by explicit thresholds and business rules rather than hidden patterns.
- `LSTM` was recommended for spending forecasting because it is suited for sequential time-series data and can model weekly or monthly spending behavior.
- A `constraint-based recommendation engine` was recommended for budget suggestions because recommendation in this context is an allocation problem, not a traditional recommender-system problem.

### Strengths

- Stronger algorithmic separation by feature
- More technically sophisticated framing
- Classification can be data-driven rather than purely policy-driven
- Each feature can be optimized with a specialized method

### Weaknesses

- Uses more than one intelligent decision mechanism, increasing implementation complexity
- Requires more data preparation and more evaluation work
- Makes the thesis harder to defend if the classification dataset is small
- Risks overengineering features that can be handled well with deterministic logic

## Option B: Revised One-ML-Model Approach

This is the recommended setup after clarifying that the study should use only one machine learning model.

### Components

- `Financial behavioral profile classification`: `Rule-based classification`
- `Overage detection`: `Rule-based algorithm`
- `Spending forecast`: `LSTM`
- `Budget recommendation`: `Rule-based` or `constraint-based recommendation engine`

### Rationale

- `LSTM` remains the only machine learning model because spending forecasting is the feature that most clearly benefits from sequence learning.
- Financial behavioral profile assignment can be derived from explicit onboarding rules based on `income stability` and `obligation burden`.
- Reclassification can be handled by recalculating those same indicators over time and applying significance thresholds.
- Overage detection remains rule-based because the logic is explicit: spending is over budget when actual or forecasted spending exceeds the assigned budget.
- Budget recommendation remains rule-based or constraint-based because it is fundamentally a budget allocation problem subject to financial rules and protected categories.

### Example Rule Logic

- `Stable` vs `Variable`: based on income regularity or observed income volatility
- `Obligated` vs `Flexible`: based on fixed obligations as a proportion of monthly income
- `Reclassification`: triggered only when changes in income variability or obligation ratio are significant and persistent
- `Overage detection`: triggered when category spending, total spending, or forecasted end-of-period spending exceeds budget thresholds
- `Recommendation`: allocate income first to protected categories, then debts, then savings, then flexible categories

### Strengths

- Keeps the system consistent with the requirement of using only one ML model
- Easier to implement within thesis scope
- Easier to explain and justify academically
- More transparent and interpretable for users and panel members
- Lower data requirement for onboarding and profile assignment

### Weaknesses

- Profile classification is less adaptive than a trained classifier
- The system depends more heavily on manually designed thresholds and business rules
- Recommendations may appear less technically advanced than a multi-model design

## Side-by-Side Comparison

| System Function | Option A: Previous Recommendation | Option B: One-ML-Model Recommendation |
| --- | --- | --- |
| Financial behavioral profile assignment | Decision Tree or Random Forest classifier | Rule-based classification |
| Reclassification | Re-run classifier on updated features | Recompute rules on updated features |
| Overage detection | Rule-based algorithm | Rule-based algorithm |
| Spending forecast | LSTM | LSTM |
| Budget recommendation | Constraint-based or rule-based recommendation engine | Constraint-based or rule-based recommendation engine |
| Number of ML models | More than one possible ML-driven component | Exactly one ML model |
| Implementation complexity | Higher | Lower |
| Interpretability | Moderate to high | High |
| Data requirement | Higher | Lower |
| Thesis defensibility for limited dataset | Moderate | Stronger |

## Conclusion

The previous recommendation was appropriate when multiple algorithms were acceptable. It treated financial behavioral profile classification as a separate machine learning problem and reserved `LSTM` for forecasting.

However, once the design goal changed to keeping only one machine learning model, the stronger approach is to retain `LSTM` as the sole ML component and convert the other features into deterministic logic. This revised setup is more practical, more interpretable, and better aligned with a thesis project that must remain implementable and defensible within limited time and data constraints.

## Recommended Final Framing

- `Financial behavioral profile classification`: rule-based
- `Overage detection`: rule-based
- `Spending forecast`: `LSTM`
- `Budget recommendation`: rule-based or constraint-based

In this final framing, `LSTM` is the only machine learning model used in the system.
