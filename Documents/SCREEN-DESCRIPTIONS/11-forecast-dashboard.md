# 11. Forecast Dashboard

## Purpose

This screen shows expected future spending and related financial projections so users can plan before expenses happen.

## What We Will Build

- Total spending forecast.
- Per-category forecast.
- Multi-line next-month forecast graph using the four broad forecast groups: Essentials, Discretionary, Financial Allocation, and Obligatory.
- Forecast horizon selector.
- Cold-start indicator.
- Personalized forecast indicator.
- Forecast explanation summary.
- Forecast-to-budget comparison.
- Forecast history or trend view when data exists.

## Primary UI Elements

- Horizon selector: daily, weekly, monthly, or configured period.
- Total forecast card.
- Category forecast chart or list.
- Next Month line graph with one line per broad category:
  - Essentials
  - Discretionary
  - Financial Allocation
  - Obligatory
- Legend or direct labels for the four lines.
- Forecast confidence or status label.
- Cold-start notice.
- Budget comparison section.
- Data freshness timestamp.

## Main User Actions

- Change forecast horizon.
- Switch between total and category views.
- Toggle individual category lines on or off.
- Review why the forecast looks high or low.
- Compare forecast against budget.
- Navigate to budget recommendation.

## States

- Cold-start forecast.
- Personalized forecast.
- Insufficient data.
- Forecast loading.
- Forecast unavailable.
- Forecast exceeds budget.

## Data Dependencies

- Transaction history.
- User profile.
- Calendar and payday context.
- Seasonal/cultural event context, where modeled.
- LSTM forecast output or fallback forecast output.
- Active budget.

## Validation Rules

- Cold-start forecasts must be clearly labeled.
- Forecast periods must be valid and consistent.
- Forecast outputs must identify whether they are fallback or personalized.
- The graph must use the same broad category names and colors consistently across dashboard, forecast, reports, and budget recommendation screens.
- The graph must remain readable on mobile; if labels crowd the chart, use a legend or selectable category chips instead of overlapping labels.

## Acceptance Criteria

- Users can view future spending estimates.
- Users can view forecasts by broad category and total.
- Users can see a next-month trend graph for Essentials, Discretionary, Financial Allocation, and Obligatory spending.
- Users can distinguish the four forecast lines through color and labels.
- The screen explains when forecasts are population-based instead of personalized.
- Forecasts can be compared against the active budget.
- Forecast output can feed budget recommendation and dashboard highlights.
