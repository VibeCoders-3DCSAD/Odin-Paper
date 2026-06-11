# 15. Reports / Analytics

## Purpose

This screen helps users review financial behavior over time through summaries, comparisons, and progress reports.

## What We Will Build

- Date-range report view.
- Weekly, monthly, and custom date-range reports.
- Spending by category.
- Spending by broad group: Essentials, Obligatory, Discretionary, and Financial Allocation.
- Income versus expense summary.
- Budget versus actual comparison.
- Forecast versus actual comparison.
- Protected category and obligation summary.
- Savings progress report.
- Debt progress report.
- Export or share preparation if approved later.

## Primary UI Elements

- Date range selector.
- Summary cards.
- Category breakdown chart.
- Broad group breakdown chart.
- Budget versus actual table.
- Forecast versus actual table.
- Savings progress section.
- Debt progress section.
- Report empty state.

## Main User Actions

- Select report period.
- Review spending breakdowns.
- Compare budget to actual spending.
- Compare forecast to actual spending.
- Review protected categories and obligations.
- Review savings and debt progress.
- Filter by category or transaction type.

## States

- No report data.
- Report loading.
- Weekly report.
- Monthly report.
- Custom range report.
- Forecast comparison unavailable.
- Export unavailable.

## Data Dependencies

- Transaction ledger.
- Budget records.
- Forecast history.
- Category taxonomy.
- Broad category mapping.
- Savings goals.
- Debt accounts.
- Protected category settings.

## Validation Rules

- Report period must be valid.
- Reports must use posted transaction data.
- Forecast comparison must only appear when forecast data exists for the selected period.
- Report numbers must reconcile to the raw transaction ledger.

## Acceptance Criteria

- Users can review reports by date range.
- Reports show category, budget, forecast, savings, and debt views where data exists.
- Reports compare planned budget, actual spending, and forecasted spending where data exists.
- Reports show how much money is tied to protected categories and obligations.
- Empty states explain what data is needed.
- Report numbers reconcile with transaction history.
- Reports support both mobile glanceability and wider web review.
