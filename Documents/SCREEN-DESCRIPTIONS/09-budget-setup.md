# 09. Budget Setup

## Purpose

This screen lets users create or edit the budget period, total budget amount, category allocations, protected categories, and surplus handling preferences.

## What We Will Build

- Budget period setup.
- Budget period alignment to the user's income frequency or pay cycle.
- Total budget amount input.
- Per-category allocation editor.
- Protected category review.
- Budget priority settings.
- Surplus handling options: carry forward, reallocate, or save.
- Deficit planning and warning preferences.
- Save draft and activate budget actions.

## Primary UI Elements

- Budget period selector.
- Pay-cycle hint from onboarding.
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
- Review deficit warnings when allocations exceed available budget.
- Activate the budget.

## States

- No budget.
- Draft budget.
- Active budget.
- Allocation incomplete.
- Overallocated budget.
- Deficit warning.
- Balanced budget.
- Save success.

## Data Dependencies

- User profile.
- Transaction history.
- Category taxonomy.
- Protected category settings.
- Income frequency and pay-cycle metadata.
- Savings goal allocation strategy.
- Forecasts.
- Budget recommendation output.

## Validation Rules

- Total budget must be greater than zero.
- Allocations cannot be negative.
- Category allocations should not exceed total budget unless explicitly allowed as deficit planning.
- Protected categories must remain visible during setup.
- Surplus handling must use one of the supported options.

## Acceptance Criteria

- Users can create and activate a budget for a selected period.
- Users can allocate amounts by category.
- The screen clearly shows remaining, overallocated, or balanced status.
- The screen warns users before activating a budget with a deficit.
- Protected categories are visible before saving.
- Saved budgets feed dashboard, alerts, reports, and recommendations.
