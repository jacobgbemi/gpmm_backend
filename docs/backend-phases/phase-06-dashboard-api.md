# Phase 06 — Home Dashboard API

## Objective
Provide a concise authenticated dashboard response that the mobile home screen can render without making many unrelated requests.

## Dashboard content
Include only approved and available data, such as:
- User display name or greeting data.
- Active course/enrollment summary.
- Learning progress summary.
- Upcoming cohort sessions.
- Career Hub job highlights or saved-job count.
- Featured resources the user is entitled to access.
- Notification summary and unread count.

Do not fabricate metrics or return data the user is not authorized to see.

## Implementation tasks
1. Review the mobile screen requirements and API specification.
2. Define a stable dashboard response schema.
3. Compose data through reusable query/service functions rather than duplicating business logic.
4. Enforce the same ownership and resource-entitlement rules as the underlying endpoints.
5. Optimize database access using appropriate query loading and aggregation.
6. Define empty states for users with no enrollments, saved jobs, resources, or notifications.
7. Add pagination or limits for dashboard lists.
8. Document cache behavior if caching is introduced; do not cache private data across users.

## API contract
- `GET /api/v1/dashboard/`

## Tests
- Anonymous users are rejected.
- Dashboard data is scoped to the authenticated user.
- Empty-state responses are valid.
- Upcoming sessions are ordered correctly and use consistent time-zone handling.
- Query count is reasonable for representative data.
- Entitlement rules are respected.

## Acceptance criteria
- One documented endpoint provides the dashboard data required by the app.
- Response remains stable and versioned.
- No sensitive or unrelated records are exposed.

## Deliverables
Dashboard serializer/service/view, tests, response examples, and API documentation.

## Agent instruction
Do not add analytics claims, AI recommendations, or predictive scores unless separately specified and supported by real data.
