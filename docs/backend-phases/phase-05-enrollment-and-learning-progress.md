# Phase 05 — Enrollment and Learning Progress

## Objective
Allow users to view their course enrollments and track progress through entitled lessons.

## Implementation tasks
1. Implement enrollment creation according to the approved business rules.
2. Define enrollment states and valid transitions. Candidate states include Pending, Active, Completed, Cancelled, and Expired; confirm the final list before implementation.
3. Enforce duplicate-enrollment rules.
4. Enforce cohort capacity safely using database transactions and appropriate row locking or another verified concurrency-safe approach.
5. Implement lesson progress linked to the correct user, enrollment, and lesson.
6. Validate that a user has access to a lesson before accepting progress updates.
7. Calculate progress consistently and document the calculation.
8. Prevent clients from assigning themselves an Active or paid entitlement by submitting a status field.
9. Ensure users can only access their own enrollment and progress records.
10. Add admin views and audit-friendly status management.

## API contract
- `GET /api/v1/enrollments/`
- `GET /api/v1/enrollments/{enrollment_id}/`
- `GET /api/v1/enrollments/{enrollment_id}/progress/`
- `POST /api/v1/enrollments/{enrollment_id}/progress/`

Adapt request and response fields to the approved API specification.

## Tests
- User sees only their own enrollments.
- Unauthorized users cannot access course lessons or progress.
- Duplicate enrollment is rejected or handled according to the business rules.
- Cohort capacity cannot be exceeded under concurrent requests.
- Invalid enrollment state transitions are rejected.
- Progress cannot be recorded for lessons outside the enrolled course.

## Acceptance criteria
- Enrollment ownership and access checks are enforced.
- Progress is persisted and calculated consistently.
- Capacity and duplicate rules are protected against race conditions.
- Payment-dependent activation remains controlled by the payment workflow in Phase 10.

## Deliverables
Enrollment/progress models or services, APIs, admin configuration, tests, and documented state-transition rules.

## Agent instruction
Do not treat a successful request from the mobile client as proof of payment. Paid enrollment activation is implemented only after verified payment in Phase 10.
