# 12. Alerts / Anomaly Review

## Purpose

This screen lets users review budget warnings, anomaly alerts, forecast-based advisories, and savings or debt notifications in one place.

## What We Will Build

- Alert inbox.
- Alert severity and type labels.
- Anomaly detail view.
- Explanation for why an alert was generated.
- Acknowledge, dismiss, and mark intentional actions.
- Whitelist or suppress similar future alerts where appropriate.
- Alert preference links.

## Primary UI Elements

- Alert list.
- Type filter.
- Severity filter.
- Alert detail panel.
- Explanation text.
- Acknowledge button.
- Mark intentional button.
- Dismiss button.
- Related transaction link.

## Main User Actions

- Review active alerts.
- Filter alerts.
- Open alert details.
- Acknowledge alert.
- Mark anomaly as intentional.
- Suppress repeated intentional alerts.
- Navigate to related transaction, budget, or forecast.

## States

- No alerts.
- Active alerts.
- Acknowledged alerts.
- Dismissed alerts.
- Anomaly pending review.
- Suppressed future alert rule.
- Loading.

## Data Dependencies

- Alert records.
- Transaction ledger.
- Anomaly detection output.
- Budget status.
- Forecast output.
- Notification preferences.
- User whitelist rules.

## Validation Rules

- Alerts must reference a valid trigger source.
- User acknowledgements must be stored.
- Intentional anomaly marking must not delete the original transaction.
- Suppression rules must be reversible.

## Acceptance Criteria

- Users can review and understand alerts.
- Users can acknowledge or dismiss alerts.
- Users can mark planned outliers as intentional.
- Alert explanations are specific enough to be actionable.
- Alert behavior respects cooldowns and user preferences.
