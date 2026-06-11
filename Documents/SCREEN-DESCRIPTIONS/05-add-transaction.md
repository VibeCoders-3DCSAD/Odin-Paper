# 05. Add Transaction

## Purpose

This screen lets users quickly record income, expense, and transfer transactions. It is the most important retention surface because manual entry is the main source of friction.

## What We Will Build

- A quick-entry transaction form.
- Transaction type selector: income, expense, transfer.
- Amount, date, account/source, category, notes, and recurrence options.
- Category selection with broad and detailed category support.
- Smart defaults based on recent entries.
- Category suggestions for common Filipino-context entries.
- Optional links to savings goals or debt accounts when the selected category requires it.
- Draft or offline-tolerant entry behavior for poor connectivity.
- Save as recurring option.
- Clear success confirmation after saving.

## Primary UI Elements

- Transaction type segmented control.
- Amount input.
- Date picker.
- Category picker.
- Suggested category chips.
- Source or account selector.
- Destination selector for transfers.
- Linked savings goal or debt account selector when applicable.
- Notes field.
- Recurring toggle.
- Save button.
- Save and add another button.

## Main User Actions

- Add income.
- Add expense.
- Add transfer.
- Select category.
- Accept or change a suggested category.
- Add notes.
- Save one-time transaction.
- Save recurring transaction template.
- Save a draft when the transaction cannot be posted immediately.

## States

- Empty form.
- Income mode.
- Expense mode.
- Transfer mode.
- Draft saved.
- Offline or sync pending.
- Validation error.
- Saving.
- Save success.
- Save failure.

## Data Dependencies

- Category taxonomy.
- User accounts or balance containers, if implemented.
- Savings goal records.
- Debt account records.
- Recurring template settings.
- Existing transactions for defaults.

## Validation Rules

- Amount must be greater than zero.
- Expense and income require a valid category.
- Transfer requires source and destination.
- Transfers must not inflate income or expense totals.
- Linked savings contributions must reference an active savings goal.
- Linked debt payments must reference an active debt account.
- Date is required.
- Recurrence rules must have a valid frequency and start date.

## Acceptance Criteria

- Users can record income, expenses, and transfers.
- Transaction capture is manual or recurring-template based; no bank, e-wallet, OCR, or import flow is required on this screen.
- Saved transactions appear in transaction history and dashboard totals.
- Invalid forms show precise validation messages.
- Repeated entries can be saved quickly.
- Recurring templates can be created from this flow.
- Saved transactions become raw ledger records used by forecasts, recommendations, anomaly detection, and reports.
