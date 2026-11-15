# Phase 11 — Notifications and User Profile

## Objective
Provide user notification records and profile management, with optional push delivery only if a provider and requirements are approved.

## Implementation tasks
1. Implement Notification records with user, category/type, title, message, optional safe deep-link metadata, read state, and timestamps.
2. Define which backend events create notifications.
3. Provide list, mark-as-read, and mark-all-as-read operations.
4. Add pagination and unread counts.
5. Implement notification preferences only for approved categories/channels.
6. Implement profile retrieval and updates using the approved user fields.
7. Prevent profile updates from changing staff permissions, roles, payment status, or enrollment entitlements.
8. If push notifications are approved, select a provider and verify its current official documentation before integration.
9. Handle invalid or rotated device tokens safely if push delivery is implemented.
10. Avoid putting sensitive personal, payment, or project data in notification text.

## API contract
- `GET /api/v1/notifications/`
- `POST /api/v1/notifications/{notification_id}/read/`
- `POST /api/v1/notifications/read-all/`
- `GET /api/v1/users/me/`
- `PATCH /api/v1/users/me/`

Optional preference/device-token endpoints require explicit product approval.

## Tests
- Notifications are scoped to the owning user.
- Read state changes correctly.
- Read-all affects only the authenticated user's notifications.
- Pagination and unread counts are correct.
- Profile updates reject protected fields.
- Push-provider failures do not corrupt core app data.

## Acceptance criteria
- Users can view and manage their notification read state.
- Profile permissions are enforced.
- Optional push functionality is not assumed or added without approval.

## Deliverables
Notification model/services/APIs, profile endpoints, admin configuration, tests, and API documentation.

## Agent instruction
Keep in-app notification storage separate from external push delivery so the app remains usable if a push provider is unavailable.
