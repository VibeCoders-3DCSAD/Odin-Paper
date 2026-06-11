# 16. Settings / Privacy / Account

## Purpose

This screen centralizes account preferences, privacy controls, notification settings, consent status, security actions, and app-level configuration.

## What We Will Build

- Account profile settings.
- Privacy and consent settings.
- RA 10173-aligned controls for consent, access, correction, and deletion.
- Notification preferences.
- Alert sensitivity or frequency settings.
- Protected category shortcut.
- Security settings.
- Data access and deletion controls.
- App disclaimers.
- Data minimization and secure-handling summary.

## Primary UI Elements

- Account information section.
- Privacy settings section.
- Consent status.
- Data access, correction, and deletion controls.
- Notification preference controls.
- Alert frequency controls.
- Security actions.
- Data export or review action.
- Delete account action.
- Advisory disclaimer.

## Main User Actions

- Update account information.
- Review consent and privacy settings.
- Review what data Odin collects and why.
- Change notification preferences.
- Adjust alert frequency.
- Navigate to protected categories.
- Change password or security settings.
- Request data access or export.
- Correct account or profile information where supported.
- Delete account and data.

## States

- Normal settings.
- Unsaved changes.
- Privacy confirmation required.
- Delete account confirmation.
- Data access request submitted.
- Data correction requested.
- Notification preferences updated.
- Security update success.
- Error state.

## Data Dependencies

- User account.
- Consent records.
- Privacy notice versions.
- Notification preferences.
- Alert preferences.
- Protected category settings.
- Security settings.
- Data retention rules.

## Validation Rules

- Destructive actions require confirmation.
- Account deletion must clearly state consequences.
- Privacy changes must be persisted with timestamped consent where needed.
- Notification channels must respect user preferences.
- Data access, correction, and deletion actions must be auditable.
- Advisory disclaimers must distinguish budget guidance from licensed financial advice.

## Acceptance Criteria

- Users can manage account, privacy, notification, and alert settings.
- Users can review advisory disclaimers.
- Users can request access to their data where supported.
- Users can correct stored account or profile information where supported.
- Users can delete their account through a deliberate confirmation flow.
- Settings changes affect the relevant screens and modules.
