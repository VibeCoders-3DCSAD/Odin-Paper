# 07. Recurring Transactions

## Purpose

This screen manages scheduled income and expense templates so users do not need to manually re-enter predictable salary, rent, bills, subscriptions, contributions, and other repeated transactions.

## What We Will Build

- Recurring transaction list.
- Create recurring income and recurring expense templates.
- Support for predictable salary, rent, subscriptions, bills, family contributions, government contributions, paluwagan, and community obligations.
- Frequency settings.
- Next occurrence preview.
- Pause, resume, edit, and stop actions.
- Reminder preferences for upcoming recurring transactions.

## Primary UI Elements

- Recurring template list.
- Template detail view.
- Frequency selector.
- Start date and optional end date.
- Next posting date.
- Category and broad group display.
- Pause/resume toggle.
- Reminder toggle.
- Create template button.

## Main User Actions

- Create recurring income.
- Create recurring expense.
- Edit a recurring template.
- Pause or resume a template.
- Stop a recurring template.
- Confirm or skip an upcoming occurrence.
- Configure reminders before expected posting dates.

## States

- No recurring transactions.
- Active templates.
- Paused templates.
- Upcoming due templates.
- Skipped occurrence.
- Template edit mode.
- Confirmation required.

## Data Dependencies

- Transaction ledger.
- Recurring transaction templates.
- Category taxonomy.
- Alerts and notifications module.
- Notification preferences.

## Validation Rules

- Template amount must be greater than zero.
- Frequency must be valid.
- Start date is required.
- End date cannot be before start date.
- Expense templates require a valid category.
- Generated transactions must preserve a link back to the source template.

## Acceptance Criteria

- Users can create recurring income and expense templates.
- Upcoming recurring entries are visible before posting.
- Paused templates do not generate new transactions.
- Edited templates affect future occurrences without corrupting past transactions.
- Recurring items can feed dashboard, budget, forecast, and alert logic.
- Recurring items can suppress misleading anomaly alerts for predictable obligations.
