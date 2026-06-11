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
- Priority table for all active savings goals.
- Snowball and Avalanche allocation strategy support.
- Financial Allocation subcategory link for each goal.
- Budget allocation distribution across active goals.

## Primary UI Elements

- Goal list cards.
- Active goals priority table with priority rank, target amount, saved amount, remaining amount, target date, progress state, and strategy inputs.
- Goal progress bar.
- Target amount input.
- Target date input.
- Contribution amount input.
- Priority control.
- Strategy selector: Snowball or Avalanche.
- Linked Financial Allocation subcategory field.
- Projected completion date.
- Add contribution action.

## Main User Actions

- Create a savings goal.
- Edit a savings goal.
- Add a contribution.
- Link transaction contributions to goals.
- Reprioritize goals.
- Select Snowball or Avalanche allocation.
- Review recommended contribution distribution.
- Mark a goal complete or archive it.

## States

- No goals.
- Active goals.
- Goal on track.
- Goal behind.
- Goal achieved.
- Goal archived.
- Projection unavailable.
- Strategy comparison available.
- No Financial Allocation subcategory linked.

## Data Dependencies

- Savings goal records.
- Transaction ledger.
- Budget recommendation module.
- Forecast output.
- User priority settings.
- Financial Allocation categories.
- Savings allocation strategy.

## Validation Rules

- Target amount must be greater than zero.
- Target date must be valid.
- Contributions cannot be negative.
- A contribution cannot exceed available tracked funds unless explicitly allowed.
- Each active goal must have or create a linked Financial Allocation subcategory.
- Snowball prioritizes the active goal with the smallest remaining amount first.
- Avalanche prioritizes the highest-ranked or highest-impact active goal according to the goal ranking field.

## Acceptance Criteria

- Users can create and track multiple savings goals.
- Goal progress updates when contributions are logged.
- Each goal shows status and projected completion.
- The priority table shows rank, target amount, saved amount, remaining amount, target date, progress state, and strategy inputs for all active goals.
- Budget Financial Allocation amounts can be distributed across active goals using the selected strategy.
- Goal priorities can influence budget recommendations.
- The savings goal record remains the source of truth for target amount, saved amount, progress state, priority, and strategy logic.
- Completed goals remain available for reporting or archive review.
