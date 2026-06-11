# 10. Budget Recommendation

## Purpose

This screen presents Odin's recommended budget allocation based on user profile, current balance, obligations, protected categories, goals, debts, and forecasted spending.

## What We Will Build

- Recommendation summary.
- Suggested category allocations.
- Suggested Financial Allocation distribution across active savings goals when applicable.
- Explanation for each major recommendation.
- Protected category constraints.
- Surplus and deficit explanation.
- Adjustment controls.
- Accept, modify, or reject actions.
- Comparison against current or previous budget.
- Clear advisory disclaimer that recommendations are decision support, not licensed financial advice.

## Primary UI Elements

- Recommended budget total.
- Category allocation table or cards.
- Savings goal allocation table or summary.
- Explanation blocks.
- Protected category indicators.
- Forecast influence notes.
- Surplus or deficit status.
- Advisory disclaimer.
- Accept recommendation button.
- Modify recommendation button.
- Reject recommendation button.

## Main User Actions

- Review recommended allocation.
- Read explanations.
- Adjust suggested amounts.
- Adjust Financial Allocation distribution across savings goals.
- Accept recommendation as budget.
- Reject recommendation.
- Return to budget setup.

## States

- Recommendation available.
- Insufficient data.
- Cold-start recommendation.
- Recommendation modified.
- Recommendation accepted.
- Recommendation rejected.
- Protected category conflict.
- Deficit risk.

## Data Dependencies

- Active user profile.
- Current balance.
- Budget setup fields.
- Forecast output.
- Protected categories.
- Savings goals.
- Savings goal priority and allocation strategy.
- Debt accounts.
- Transaction history.

## Validation Rules

- Recommendations must not reduce protected categories unless user settings allow it.
- Recommendations must identify when they rely on cold-start assumptions.
- Recommendation outputs must include user-facing explanation fields.
- Financial Allocation amounts must be distributed across active savings goals according to the selected savings goal allocation strategy.
- Modified recommendation must still pass budget validation.

## Acceptance Criteria

- Users can see what Odin recommends and why.
- Recommendations account for profile, obligations, forecasts, and protected categories.
- Recommendations account for savings goal priority, debt pressure, surplus handling, and deficit warnings.
- Users can accept, modify, or reject recommendations.
- Accepted recommendations become active or draft budgets.
- The screen does not present advisory output as licensed financial advice.
