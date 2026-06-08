# 13. Savings Goals

## Purpose

This screen helps users create, prioritize, fund, and monitor savings goals such as emergency funds, major purchases, tuition, travel, or family-related goals.

## What We Will Build

- Savings goal list.
- Goal creation form.
- Goal detail view.
- Contribution tracking.
- Progress visualization.
- On-track, behind, and achieved statuses.
- Projected completion date.
- Goal prioritization controls.

## Primary UI Elements

- Goal list cards.
- Goal progress bar.
- Target amount input.
- Target date input.
- Contribution amount input.
- Priority control.
- Projected completion date.
- Add contribution action.

## Main User Actions

- Create a savings goal.
- Edit a savings goal.
- Add a contribution.
- Link transaction contributions to goals.
- Reprioritize goals.
- Mark a goal complete or archive it.

## States

- No goals.
- Active goals.
- Goal on track.
- Goal behind.
- Goal achieved.
- Goal archived.
- Projection unavailable.

## Data Dependencies

- Savings goal records.
- Transaction ledger.
- Budget recommendation module.
- Forecast output.
- User priority settings.

## Validation Rules

- Target amount must be greater than zero.
- Target date must be valid.
- Contributions cannot be negative.
- A contribution cannot exceed available tracked funds unless explicitly allowed.

## Acceptance Criteria

- Users can create and track multiple savings goals.
- Goal progress updates when contributions are logged.
- Each goal shows status and projected completion.
- Goal priorities can influence budget recommendations.
- Completed goals remain available for reporting or archive review.
