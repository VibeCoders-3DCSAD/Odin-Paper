# 14. Debt Accounts

## Purpose

This screen helps users record debts, understand repayment pressure, compare repayment strategies, and track payoff progress.

## What We Will Build

- Debt account list.
- Debt account creation form.
- Debt detail view.
- Minimum payment tracking.
- Interest rate support.
- Avalanche strategy projection.
- Snowball strategy projection.
- Strategy switching.
- Payoff date projection.
- Plain-language explanation of strategy tradeoffs.
- On-demand projection generation when no current projection exists or debt inputs change.

## Primary UI Elements

- Debt account cards.
- Balance input.
- Interest rate input.
- Minimum payment input.
- Due date field.
- Strategy selector.
- Payoff projection chart or summary.
- Projected payoff date.
- Strategy explanation.
- Payment history section.

## Main User Actions

- Create debt account.
- Edit debt account.
- Record debt payment.
- Compare Avalanche and Snowball strategies.
- Select active repayment strategy.
- View projected payoff date.
- Regenerate projections after strategy, extra payment, account detail, or payment changes.
- Review minimum-payment pressure.
- Archive paid debt.

## States

- No debts.
- Active debt accounts.
- Payment due soon.
- Payment overdue.
- Strategy selected.
- Debt paid off.
- Projection unavailable.
- Projection stale after debt account or payment changes.
- Minimum payment risk.

## Data Dependencies

- Debt account records.
- Transaction ledger.
- Budget recommendation module.
- Forecast output.
- Notification preferences.
- Debt repayment projection runs, items, and points.

## Validation Rules

- Debt balance cannot be negative.
- Interest rate cannot be negative.
- Minimum payment cannot be negative.
- Payments must reduce the correct debt account.
- Strategy projections require at least one active debt account.
- Projections must clearly state their assumptions and avoid presenting debt guidance as licensed financial advice.
- Projections should be generated on demand when the user opens the debt strategy or projection screen and no current projection exists, switches payoff strategy, changes extra payment amount, edits a debt account balance, interest rate, or minimum payment, or records a debt payment that changes the current balance.
- Existing projections should be treated as stale when their debt account, payment, strategy, or extra-payment inputs no longer match the latest user data.

## Acceptance Criteria

- Users can create and manage debt accounts.
- Users can record payments and see balance changes.
- Users can compare Avalanche and Snowball projections.
- Users see refreshed projections after changing strategy, extra payment amount, debt account details, or debt payment history.
- Users can see projected payoff dates and the assumptions behind them.
- Selected repayment strategy can influence budget recommendations.
- Paid debts can be archived without deleting history.
