# 10. Budget Recommendation

## Purpose

This screen presents Odin's recommended budget allocation based on user profile, current balance, obligations, protected categories, goals, debts, and forecasted spending.

## What We Will Build

- Recommendation summary.
- Suggested category allocations.
- Explanation for each major recommendation.
- Protected category constraints.
- Adjustment controls.
- Accept, modify, or reject actions.
- Comparison against current or previous budget.

## Primary UI Elements

- Recommended budget total.
- Category allocation table or cards.
- Explanation blocks.
- Protected category indicators.
- Forecast influence notes.
- Accept recommendation button.
- Modify recommendation button.
- Reject recommendation button.

## Main User Actions

- Review recommended allocation.
- Read explanations.
- Adjust suggested amounts.
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

## Data Dependencies

- Active user profile.
- Current balance.
- Budget setup fields.
- Forecast output.
- Protected categories.
- Savings goals.
- Debt accounts.
- Transaction history.

## Validation Rules

- Recommendations must not reduce protected categories unless user settings allow it.
- Recommendations must identify when they rely on cold-start assumptions.
- Modified recommendation must still pass budget validation.

## Acceptance Criteria

- Users can see what Odin recommends and why.
- Recommendations account for profile, obligations, forecasts, and protected categories.
- Users can accept, modify, or reject recommendations.
- Accepted recommendations become active or draft budgets.
- The screen does not present advisory output as licensed financial advice.
