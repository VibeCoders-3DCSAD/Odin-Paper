# 16. Settings / Privacy / Account

## Purpose

This screen centralizes account preferences, privacy controls, notification settings, consent status, security actions, and app-level configuration.

## What We Will Build

- Account profile settings.
- Privacy and consent settings.
- Notification preferences.
- Alert sensitivity or frequency settings.
- Protected category shortcut.
- Security settings.
- Data access and deletion controls.
- App disclaimers.

## Primary UI Elements

- Account information section.
- Privacy settings section.
- Consent status.
- Notification preference controls.
- Alert frequency controls.
- Security actions.
- Data export or review action.
- Delete account action.
- Advisory disclaimer.

## Main User Actions

- Update account information.
- Review consent and privacy settings.
- Change notification preferences.
- Adjust alert frequency.
- Navigate to protected categories.
- Change password or security settings.
- Request data access or export.
- Delete account and data.

## States

- Normal settings.
- Unsaved changes.
- Privacy confirmation required.
- Delete account confirmation.
- Notification preferences updated.
- Security update success.
- Error state.

## Data Dependencies

- User account.
- Consent records.
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

## Acceptance Criteria

- Users can manage account, privacy, notification, and alert settings.
- Users can review advisory disclaimers.
- Users can request access to their data where supported.
- Users can delete their account through a deliberate confirmation flow.
- Settings changes affect the relevant screens and modules.
