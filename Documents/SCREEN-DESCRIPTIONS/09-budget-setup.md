# 09. Budget Setup

## Purpose

This screen lets users create or edit the budget period, total budget amount, category allocations, protected categories, and surplus handling preferences.

## What We Will Build

- Budget period setup.
- Total budget amount input.
- Per-category allocation editor.
- Protected category review.
- Budget priority settings.
- Surplus and deficit handling preferences.
- Save draft and activate budget actions.

## Primary UI Elements

- Budget period selector.
- Total budget input.
- Category allocation controls.
- Remaining-to-allocate indicator.
- Protected category badges.
- Surplus handling selector.
- Save button.
- Activate budget button.

## Main User Actions

- Create a new budget.
- Edit an active or upcoming budget.
- Allocate money by category.
- Review protected categories.
- Choose surplus handling.
- Activate the budget.

## States

- No budget.
- Draft budget.
- Active budget.
- Allocation incomplete.
- Overallocated budget.
- Balanced budget.
- Save success.

## Data Dependencies

- User profile.
- Transaction history.
- Category taxonomy.
- Protected category settings.
- Forecasts.
- Budget recommendation output.

## Validation Rules

- Total budget must be greater than zero.
- Allocations cannot be negative.
- Category allocations should not exceed total budget unless explicitly allowed as deficit planning.
- Protected categories must remain visible during setup.

## Acceptance Criteria

- Users can create and activate a budget for a selected period.
- Users can allocate amounts by category.
- The screen clearly shows remaining, overallocated, or balanced status.
- Protected categories are visible before saving.
- Saved budgets feed dashboard, alerts, reports, and recommendations.
