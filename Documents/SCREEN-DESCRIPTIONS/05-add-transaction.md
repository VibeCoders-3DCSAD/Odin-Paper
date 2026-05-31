# 05. Add Transaction

## Purpose

This screen lets users quickly record income, expense, and transfer transactions. It is the most important retention surface because manual entry is the main source of friction.

## What We Will Build

- A quick-entry transaction form.
- Transaction type selector: income, expense, transfer.
- Amount, date, account/source, category, notes, and recurrence options.
- Category selection with broad and detailed category support.
- Smart defaults based on recent entries.
- Save as recurring option.
- Clear success confirmation after saving.

## Primary UI Elements

- Transaction type segmented control.
- Amount input.
- Date picker.
- Category picker.
- Source or account selector.
- Destination selector for transfers.
- Notes field.
- Recurring toggle.
- Save button.
- Save and add another button.

## Main User Actions

- Add income.
- Add expense.
- Add transfer.
- Select category.
- Add notes.
- Save one-time transaction.
- Save recurring transaction template.

## States

- Empty form.
- Income mode.
- Expense mode.
- Transfer mode.
- Validation error.
- Saving.
- Save success.
- Save failure.

## Data Dependencies

- Category taxonomy.
- User accounts or balance containers, if implemented.
- Recurring template settings.
- Existing transactions for defaults.

## Validation Rules

- Amount must be greater than zero.
- Expense and income require a valid category.
- Transfer requires source and destination.
- Date is required.
- Recurrence rules must have a valid frequency and start date.

## Acceptance Criteria

- Users can record income, expenses, and transfers.
- Saved transactions appear in transaction history and dashboard totals.
- Invalid forms show precise validation messages.
- Repeated entries can be saved quickly.
- Recurring templates can be created from this flow.
