# Phase 04 — Training Academy

## Objective
Build the backend catalogue for GlintPM training courses, tracks, course content structure, and cohort schedules.

## Product context
GlintPM provides professional training in areas including Primavera P6, project planning and scheduling, project controls, Microsoft Project, Excel, and Power BI. Use the approved product catalogue as the source of truth. Do not assume every course is available in the app.

The known P6 track concepts are Self-paced, Launchpad, and Mentored. Confirm the current commercial and delivery rules from approved product documentation before encoding them.

## Implementation tasks
1. Implement course categories and published course records.
2. Implement course tracks and their descriptions, delivery modes, and pricing configuration.
3. Implement course modules and lessons, including ordering and publication status.
4. Implement cohorts and cohort sessions with dates, time zones, delivery details, and capacity where applicable.
5. Support draft/unpublished content for administrators.
6. Add search, filtering, pagination, and stable ordering.
7. Register content-management models in Django Admin.
8. Keep pricing and currency in backend-managed records/configuration; do not hardcode prices in API serializers or mobile UI.
9. Ensure unpublished content is not exposed to ordinary users.
10. Add API documentation and tests.

## API contract
- `GET /api/v1/courses/`
- `GET /api/v1/courses/{course_id}/`
- `GET /api/v1/courses/categories/`
- `GET /api/v1/courses/{course_id}/tracks/`
- `GET /api/v1/courses/{course_id}/cohorts/`

## Tests
- Published courses are visible according to access rules.
- Draft courses and lessons are not publicly exposed.
- Filters and pagination work.
- Course, track, module, lesson, and cohort relationships are correct.
- Dates and time zones serialize consistently.

## Acceptance criteria
- Catalogue data can be maintained through the admin.
- API responses match the approved API contract.
- Pricing is data-driven.
- Publication and visibility rules are tested.

## Deliverables
Course catalogue models/services/API endpoints, admin screens, tests, and updated API documentation.

## Agent instruction
Do not add video hosting, learning management integrations, certificates, quizzes, or other unapproved functionality in this phase.
