# 04. Dashboard / Overview

## Purpose

This screen is the primary daily overview. It gives users a quick view of financial status, urgent warnings, recent activity, budget progress, goal progress, and forecast highlights.

## What We Will Build

- A mobile-first dashboard.
- Current balance summary.
- Budget period status.
- Spending progress by broad category.
- Recent transactions.
- Active alerts.
- Savings goal progress preview.
- Debt repayment preview.
- Stale debt projection refresh for debt payoff preview when needed.
- Forecast highlight.
- Compact next-month forecast preview using the same four broad forecast groups as the Forecast Dashboard.
- Urgent action cards for budget risk, unusual spending, upcoming recurring obligations, savings status, and debt due dates.
- Quick actions for adding transactions, reviewing alerts, and reviewing recommendations.

## Primary UI Elements

- Current balance card.
- Budget remaining card.
- Category spending summary.
- Forecast summary card.
- Compact forecast graph or sparkline preview for Essentials, Discretionary, Financial Allocation, and Obligatory.
- Alert preview.
- Upcoming recurring transaction preview.
- Recent transaction list.
- Savings goal preview.
- Debt payoff preview.
- Debt projection freshness indicator when projection data is missing or stale.
- Quick action buttons.

## Main User Actions

- Add a transaction.
- Review budget recommendation.
- Open forecast dashboard.
- Tap the compact forecast preview to open the full forecast graph.
- Open alerts.
- Review upcoming recurring transactions.
- Open transaction history.
- Open savings goals.
- Open debt accounts.

## States

- Empty dashboard for new user.
- Cold-start dashboard.
- Normal dashboard.
- Budget at risk.
- Active alerts.
- Upcoming obligation.
- No recent transactions.
- Loading data.

## Data Dependencies

- User profile.
- Account balance.
- Transactions.
- Budget period.
- Forecast output.
- Alerts.
- Recurring transaction templates.
- Savings goals.
- Debt accounts.
- Debt repayment projection runs for payoff preview.

## Validation Rules

- Dashboard totals must be derived from stored transactions and budget records.
- Debt payoff previews should use the latest valid projection or request a refreshed projection when the existing projection is stale.
- Cold-start data must be labeled clearly.
- No card should show misleading zero values when data is unavailable.
- Forecast preview colors and labels must match the full Forecast Dashboard.

## Acceptance Criteria

- Users can understand current financial status within one screen.
- Dashboard links to the main task screens.
- Debt payoff preview reflects current projection data or clearly indicates when it needs refresh.
- New users see useful setup prompts instead of broken charts.
- Cold-start estimates are visibly labeled.
- Forecast preview gives users a quick next-month signal without replacing the full Forecast Dashboard.
- Active alerts are visible without overwhelming the page.
- Dashboard cards prioritize urgent action without shaming protected or culturally necessary expenses.
