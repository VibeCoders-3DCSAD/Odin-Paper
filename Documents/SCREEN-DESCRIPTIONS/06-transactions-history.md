# 06. Transactions List / History

## Purpose

This screen lets users review, search, filter, edit, and delete their logged financial activity.

## What We Will Build

- Chronological transaction list.
- Search by note, category, or amount.
- Filters for type, category, broad category, date range, recurring status, and amount range.
- Transaction detail view.
- Edit and delete actions.
- Summary totals for the selected range.
- Review modes for weekly, semi-monthly, monthly, and custom date ranges.

## Primary UI Elements

- Date range selector.
- Search field.
- Filter controls.
- Broad category filter.
- Transaction list grouped by date.
- Income, expense, and transfer indicators.
- Summary totals.
- Empty state.
- Transaction detail panel or screen.

## Main User Actions

- Search transactions.
- Filter transactions.
- Open a transaction.
- Edit a transaction.
- Delete a transaction.
- Review date-range totals.
- Review whether a transaction came from manual entry or a recurring template.

## States

- Empty history.
- Filtered results.
- No matching results.
- Loading.
- Edit mode.
- Delete confirmation.
- Recurring-generated transaction.
- Error state.

## Data Dependencies

- Transaction ledger.
- Category taxonomy.
- Broad forecast category mapping.
- Recurring template link, where applicable.
- Budget period metadata.

## Validation Rules

- Date filters must use valid date ranges.
- Deletes require confirmation.
- Edited transactions must pass the same validation as add transaction.
- Edited transfers must continue to be excluded from income and expense totals.

## Acceptance Criteria

- Users can find and review transactions by date range.
- Users can edit transaction details and see updated summaries.
- Users can delete accidental transactions after confirmation.
- Filters and search update the visible list correctly.
- Transaction history supports dashboard, reports, forecasts, and recommendations as the source ledger.
- History remains the user-facing view of raw transactions before model-specific datasets are derived.
