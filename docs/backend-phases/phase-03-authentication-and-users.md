# Phase 03 — Authentication and User Management

## Objective
Provide secure account registration, authentication, session/token lifecycle, and user profile access for the mobile app.

## Implementation tasks
1. Review the approved authentication requirements and current official documentation for candidate authentication packages.
2. Select and document a maintained authentication approach compatible with the installed Django and DRF versions.
3. Implement registration with validated input and secure password hashing through Django's supported mechanisms.
4. Implement login and the selected access/refresh token or session lifecycle.
5. Define logout and token invalidation behavior. Do not claim logout invalidates credentials unless the selected design actually does so.
6. Implement password reset/recovery using a verified delivery mechanism. Do not expose whether an email address is registered.
7. Implement email verification if required by product requirements.
8. Implement authenticated current-user and profile endpoints.
9. Enforce object-level ownership and staff-only permissions.
10. Add throttling and sensible validation for authentication endpoints.
11. Document token storage expectations for the mobile client; do not store long-lived credentials in insecure plaintext storage.

## API contract
- `POST /api/v1/auth/register/`
- `POST /api/v1/auth/login/`
- `POST /api/v1/auth/logout/`
- `GET /api/v1/auth/me/`
- `GET /api/v1/users/me/`
- `PATCH /api/v1/users/me/`

Adjust routes to the approved API specification if it differs.

## Security requirements
- Never return password hashes or secrets.
- Use generic responses for account recovery where appropriate.
- Validate input server-side.
- Prevent users from changing staff roles, permissions, payment status, or enrollment entitlements through profile updates.
- Apply authentication and authorization consistently.
- Avoid logging passwords, tokens, or sensitive personal data.

## Tests
- Successful and unsuccessful registration/login.
- Invalid credentials and malformed input.
- Token/session expiry and refresh behavior.
- Logout/invalidation behavior.
- Password recovery flow.
- Anonymous access restrictions.
- Users cannot read or modify another user's profile.

## Acceptance criteria
- Authentication works end-to-end using the documented approach.
- Profile endpoints return only permitted fields.
- Authorization tests pass.
- Mobile integration requirements are documented.

## Deliverables
Authentication implementation, serializers/views/permissions, tests, API documentation, and a concise security decision record.

## Agent instruction
Verify all third-party authentication package APIs against current official documentation. Do not invent endpoint behavior or SDK methods.
