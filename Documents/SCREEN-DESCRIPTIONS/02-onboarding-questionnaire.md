# 02. Onboarding Questionnaire

## Purpose

This screen collects the initial financial context needed to classify a user, initialize budget defaults, set protected categories, and support cold-start forecasts before Odin has enough transaction history.

## What We Will Build

- A guided multi-step onboarding flow.
- Questions for employment status, income frequency, approximate income range, and income stability.
- Employment status options: Regular / Permanent employee, Contractual / Project-based employee, Freelancer / Self-employed, Part-time employee, Business owner / Entrepreneur, and Other.
- Income stability options limited to Stable and Variable for profile classification.
- Questions for fixed obligations, debt payments, financial dependents, family support, and recurring expenses.
- Questions for savings goals and budget priorities.
- Protected category selection.
- A review step before submission.
- A clear explanation that onboarding data is used for personalization, cold-start forecasts, and budget recommendations.

## Primary UI Elements

- Step indicator.
- Multiple choice controls.
- Numeric inputs for amounts or ranges.
- Employment status selector.
- Stable / Variable income stability selector.
- Income frequency selector.
- Category selector for obligations and protected categories.
- Back and next buttons.
- Save and continue later action.
- Final submit button.
- Short explanatory text per section.

## Main User Actions

- Enter income and employment details.
- Declare obligations.
- Declare dependents or family support obligations.
- Select financial priorities.
- Mark protected categories.
- Review answers.
- Submit onboarding.

## States

- First-time onboarding.
- Partially completed onboarding.
- Review mode.
- Validation error.
- Submission loading.
- Submitted successfully.

## Data Dependencies

- User account.
- Employment status.
- Income frequency.
- Income stability.
- Income profile fields.
- Obligation fields.
- Dependent and family support fields.
- Protected category choices.
- Initial financial goals.
- Consent and privacy state.

## Validation Rules

- Required questions must be answered before final submission.
- Employment status must use one of the configured options.
- Income stability must be stored as Stable or Variable.
- Numeric amounts cannot be negative.
- Protected categories must map to valid category records.
- Users must be able to skip optional questions where exact amounts are unknown.

## Acceptance Criteria

- A first-time user can complete onboarding from start to finish.
- The app stores enough data to generate an initial financial behavioral profile.
- The app stores enough data to create cold-start budget and forecast defaults.
- Protected and culturally necessary categories can be declared without presenting them as wasteful spending.
- Users can review and edit answers before submission.
- Users can resume incomplete onboarding.
