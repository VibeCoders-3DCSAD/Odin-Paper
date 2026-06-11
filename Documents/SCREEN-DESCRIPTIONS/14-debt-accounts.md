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
- Minimum payment risk.

## Data Dependencies

- Debt account records.
- Transaction ledger.
- Budget recommendation module.
- Forecast output.
- Notification preferences.

## Validation Rules

- Debt balance cannot be negative.
- Interest rate cannot be negative.
- Minimum payment cannot be negative.
- Payments must reduce the correct debt account.
- Strategy projections require at least one active debt account.
- Projections must clearly state their assumptions and avoid presenting debt guidance as licensed financial advice.

## Acceptance Criteria

- Users can create and manage debt accounts.
- Users can record payments and see balance changes.
- Users can compare Avalanche and Snowball projections.
- Users can see projected payoff dates and the assumptions behind them.
- Selected repayment strategy can influence budget recommendations.
- Paid debts can be archived without deleting history.
