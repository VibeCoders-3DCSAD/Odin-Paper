# 03. Profile Result / Financial Behavioral Profile

## Purpose

This screen shows the user's assigned Financial Behavioral Profile and explains how the profile affects forecasts, budget recommendations, anomaly baselines, and user guidance.

## What We Will Build

- A profile result page after onboarding.
- Support for four profiles: Stable-Flexible, Stable-Obligated, Variable-Flexible, and Variable-Obligated.
- Plain-language explanation of the assigned profile.
- Key factors that contributed to classification.
- Recommended first actions based on the profile.
- Reassessment and manual review entry points.
- Profile history summary once reclassification exists.

## Primary UI Elements

- Profile name.
- Profile description.
- Income stability indicator.
- Obligation level indicator.
- Key factor list.
- Confidence or explanation block, if supported.
- Continue to dashboard button.
- Reassess profile button.
- Profile history link.

## Main User Actions

- Review assigned profile.
- Continue to the dashboard.
- Request reassessment.
- Confirm or reject future profile changes.
- View why profile assignment happened.

## States

- Newly assigned profile.
- Profile reassessment suggested.
- User confirms reassessment result.
- User rejects reassessment result.
- Insufficient data for high-confidence profile.
- Profile history available.

## Data Dependencies

- Onboarding responses.
- Early transaction summaries when available.
- Profile classification output.
- Classification explanation.
- Profile history records.

## Validation Rules

- Only one active profile can be assigned at a time.
- Profile changes require user confirmation.
- Profile explanation must be available in user-facing language.

## Acceptance Criteria

- Users can see their active profile and understand its meaning.
- Users can see the factors that influenced the profile.
- Users can proceed from profile result to dashboard.
- Reclassification suggestions do not silently change the active profile.
- Profile history can show previous profile changes once they exist.
