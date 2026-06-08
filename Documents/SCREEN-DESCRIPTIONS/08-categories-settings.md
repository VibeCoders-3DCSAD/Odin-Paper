# 08. Categories / Category Settings

## Purpose

This screen manages the expense category system used by transaction entry, budgeting, forecasting, anomaly detection, reports, and recommendations.

## What We Will Build

- Category browser grouped by broad category.
- Detailed category list for Filipino-context spending.
- Protected category controls.
- Optional custom label support.
- Category descriptions to reduce ambiguity.
- Mapping display from detailed categories to broad forecast groups.

## Primary UI Elements

- Broad category sections: Essentials, Obligatory, Discretionary, Financial Allocation.
- Detailed category rows.
- Protected category toggle.
- Category description.
- Custom label field, if allowed.
- Search field.

## Main User Actions

- Browse categories.
- Search categories.
- Read category definitions.
- Mark or unmark protected categories.
- Customize category labels where allowed.
- Review how detailed categories roll up to broad groups.

## States

- Default taxonomy.
- User-customized labels.
- Protected defaults.
- User-protected categories.
- Search results.
- Validation error.

## Data Dependencies

- Category taxonomy.
- Protected category settings.
- Budget recommendation rules.
- Forecast category mapping.

## Validation Rules

- Every detailed category must map to one broad category.
- System-required categories cannot be deleted.
- Protected category changes must be intentional and persisted.
- Custom labels cannot create duplicate ambiguous categories within the same group.

## Acceptance Criteria

- Users can understand which category to use for common transactions.
- Filipino-context categories are visible and usable.
- Protected category settings affect budget recommendations.
- Category mappings remain stable for reports and model features.
- Category changes do not break historical transaction records.
