# 01. Login / Register

## Purpose

This screen gives users secure access to Odin and separates personal financial records by account. It is the entry point for new users, returning users, and users who need to recover access.

## What We Will Build

- A login form for existing users.
- A registration form for new users.
- A password recovery entry point.
- A short privacy and data-use notice before account creation.
- A visible link to proceed to onboarding after successful registration.
- A secure logout destination for expired or ended sessions.

## Primary UI Elements

- Email input.
- Password input.
- Confirm password input for registration.
- Login button.
- Register button.
- Forgot password link.
- Privacy notice link.
- Terms or consent checkbox for registration.
- Error message area.
- Loading state for authentication requests.

## Main User Actions

- Create a new Odin account.
- Log in to an existing account.
- Request password recovery.
- Accept required privacy and data-use terms.
- Switch between login and registration modes.

## States

- Empty form.
- Input validation error.
- Authentication error.
- Account already exists.
- Password recovery requested.
- Loading.
- Authenticated.
- Session expired.

## Data Dependencies

- User account identifier.
- Authentication token or session state.
- Consent timestamp.
- Account creation timestamp.

## Validation Rules

- Email must use a valid email format.
- Password must meet the configured security rules.
- Registration requires accepted consent.
- Login errors must not reveal whether the email or password was the incorrect field.

## Acceptance Criteria

- New users can register and are routed to onboarding.
- Returning users can log in and are routed to the dashboard if onboarding is complete.
- Returning users can log in and are routed to onboarding if onboarding is incomplete.
- Invalid credentials show a clear, non-sensitive error.
- Registration cannot complete without required consent.
- Session expiration returns the user to this screen with a clear message.
